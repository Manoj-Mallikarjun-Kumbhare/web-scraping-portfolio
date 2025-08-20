import logging
import json
import csv
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from playwright.sync_api import sync_playwright

#-----------------------------------------------
# 1. Logging setup
#-----------------------------------------------

logging.basicConfig(
    filename='ebay_bot.log',
    level= logging.INFO,
    format = '%(asctime)s-%(levelname)s-%(message)s'
    )

#-----------------------------------------------------
# 2. Load Congig
#-----------------------------------------------------
with open('config.json') as f:
    config = json.load(f)
keywords = config.get('keywords',['laptop'])
max_price = config.get('max_price',500)
location = config.get('location','US')
send_email_alert = config.get('send_email_alert',False)
email_receiver = config.get('email_receiver','manojkumbhare189@gmail.com')

#----------------------------------------------------------------------------
# 3. Helper : Email function
#----------------------------------------------------------------------------
def send_email(results_file):
    try:
        msg = MIMEText(f'Your eBay bot finished.')
        msg['Subject'] = 'eBay Bot Results'
        msg['From'] = 'mnjkumbhare@gmail.com'
        msg['To'] = email_receiver

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
            server.login('mnjkumbhare@gmail.com','Manoj@97636') # your email,password
            server.send_message(msg)
        logging.info('Email sent successfully')
    except Exception as e:
        logging.error(f'Failed to send email:{e}.... check emailid and password')

#--------------------------------------------------------------------------------------------
# 4. eBay Scraper
#--------------------------------------------------------------------------------------------
def run_ebay_bot():
    try:
        logging.info('Bot Started...')
        now = datetime.now().strftime('%y-%m-%d_%H:%M:%S')
        csv_file = f'ebay_results_{now}.csv'
        excel_file =f'ebay_results_{now}.xlsx'

        all_results = []

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            for keyword in keywords:
                logging.info(f'Searching for:{keyword}...')
                page.goto('https://www.ebay.com/')
                page.fill('input[placeholder="Search for anything"]',keyword)
                page.press('input[placeholder="Search for anything"]','Enter')
                page.wait_for_selector('.s-card')

                cards = page.query_selector_all('.s-card')
                for card in cards:
                    title = card.query_selector('.s-card__title')
                    price = card.query_selector('.s-card__price')
                    link = card.query_selector('a.su-link')

                    if title and price and link:
                        title_text = title.inner_text()
                        price_text = price.inner_text().replace('$','').replace(',','')
                        link_url = link.get_attribute('href')
                        
                        try:
                            price_val = float(price_text.split()[0])
                        except:
                            price_val = None

                        if price_val and price_val <= max_price:
                            all_results.append({
                                'keyword':keyword,
                                'title':title_text,
                                'price': price_val,
                                'link':link_url,
                                'date':datetime.now().strftime('%y/%m/%d_%H:%M:%S')
                        
                            })
            browser.close()

        #----------------------------------------------------------------------------------
        # 5. Save to csv and Excel
        #----------------------------------------------------------------------------------
        if all_results:
            keys = all_results[0].keys()

            # save csv
            with open(csv_file,'w',newline='',encoding='utf-8') as f:
                writer = csv.DictWriter(f,fieldnames=keys)
                writer.writeheader()
                writer.writerows(all_results)

            # save to Excell
            df = pd.DataFrame(all_results)
            df.to_excel(excel_file,index=False)

            logging.info(f'Saved {len(all_results)} results')
            if send_email_alert:
                send_email(excel_file)
    
    except Exception as e:
        logging.error(f'Bot failed:{e}')

#---------------------------------------------------------------
# Run
#---------------------------------------------------------------
if __name__=='__main__':
    run_ebay_bot()