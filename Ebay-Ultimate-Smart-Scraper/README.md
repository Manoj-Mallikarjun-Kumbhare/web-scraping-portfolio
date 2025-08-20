🛒 Ebay Ultimate Smart Scraper

A powerful web scraping bot built with Python + Playwright that extracts product data from eBay and exports results into CSV/Excel.
This project is designed for data collection, automation, and e-commerce analysis.

🚀 Features

✅ Scrapes product titles, prices, sellers, ratings, and links

✅ Handles dynamic pages with Playwright

✅ Stores results in CSV & Excel formats

✅ Includes logging for debugging (ebay_bot.log)

✅ Configurable search terms via config.json

🛠️ Tech Stack

Python 3.10+

Playwright (browser automation)

Pandas (data cleaning & export)

Logging (for error tracking)

📂 Project Structure
Ebay-Ultimate-Smart-Scraper/
│── smart_ebay_scraper.py   # Main scraper script
│── config.json             # Config file (search keywords, settings)
│── ebay_bot.log            # Log file
│── ebay_results_*.csv      # Exported CSV results
│── ebay_results_*.xlsx     # Exported Excel results
│── README.md               # Project documentation

⚡ Usage
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Update search keywords

Edit config.json and set your target product/search query.

3️⃣ Run the scraper
python smart_ebay_scraper.py

4️⃣ Check results

Data saved in CSV and Excel

Logs saved in ebay_bot.log

📊 Example Output
Product Name	Price	Seller	Rating	Link
iPhone 14 Pro Max	$1099	BestSeller123	4.9⭐	ebay.com/...
Samsung Galaxy S23	$899	MobileHub	4.8⭐	ebay.com/...
🌟 Future Improvements

 Proxy & CAPTCHA handling

 Multi-threaded scraping

 Real-time dashboard with Streamlit

👨‍💻 Author

Manoj Mallikarjun Kumbhare
📧 Contact: shrianandvishwa@gmail.com
💼 Portfolio: https://github.com/Manoj-Mallikarjun-Kumbhare/web-scraping-portfolio/tree/main/Ebay-Ultimate-Smart-Scraper

