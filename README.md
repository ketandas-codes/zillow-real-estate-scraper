# 🏠 Zillow Real Estate Scraper

## 📋 Project Overview

Zillow Real Estate Scraper is a  production-ready Python web scraping solution designed to

extract real estate property listings from Zillow with stealth-based browsing techniques and

comprehensive data cleaning. This project demonstrates professional-grade web automation,

anti-detection methods, and data engineering best practices.


## 🎯 Purpose
🔍 Extract property listing data (price, address, beds, baths, sqft) from Zillow search results for market research, analysis, and portfolio demonstration. Built with ethical scraping practices and compliance in mind.

✨ What Makes It Different
🥸 Stealthy Browsing: Uses undetected-chromedriver + selenium-stealth to minimize detection

🤖 Human-Like Behavior: Randomized scrolling, delays, and user-agent rotation

🔄 Dual Pipeline: Separate scraper and cleaning modules for maintainability

⚙️ Production Ready: Error handling, logging, deduplication built-in

📈 Portfolio Grade: Clean code, documentation, and best practices


## 📊 Key Features

 Stealthy Anti-Detection 🛡️
 undetected-chromedriver + selenium-stealth integration

 Random user-agent selection (Chrome 131-133)

 CDP-level webdriver masking

 Human-like scrolling patterns

 Smart Data Extraction 🎯
 Pagination support (up to 20 pages)

 Structured CSV output

🔗 Robust XPath/CSS selectors

 Duplicate removal

 Comprehensive Data Cleaning 🧹
 Address parsing (street, city, state, zip)

 Price normalization (remove $, commas)

 Numeric field conversion (beds, baths, sqft)

 Missing value handling

 Production-Grade Code 💻
 Try-catch error handling

 Configurable timeouts & retry logic

 Graceful degradation on missing elements

 Clean OOP architecture

## 🛠️ Tech Stack

| 🔧 Technology              | 📌 Version | 🎯 Purpose               |
| -------------------------- | ---------- | ------------------------ |
| 🐍 Python                  | 3.9+       | Core language            |
| 🌐 Selenium                | 4.x        | Browser automation       |
| 🔓 undetected-chromedriver | Latest     | Anti-detection WebDriver |
| 👤 selenium-stealth        | Latest     | Stealth mode             |
| 📊 pandas                  | 2.0+       | Data processing          |
| 🔢 numpy                   | 1.26+      | Numerical operations     |

## 📁 Project Structure

text
zillow-real-estate-scraper/
├──  README.md
├──  requirements.txt
├──  zillow_scraper.py
├──  clean_zillow_data.py
├──  data/
│   ├── Zillow_Propertys_data.csv
│   └── zillow_clean.csv
└──  samples/
    └── screenshots/
 Quick Start
 Prerequisites
 Python 3.9+ (3.10+ recommended)

 Google Chrome (latest version)

 pip & Git

🔧 Installation
1️ Clone Repository
bash
git clone https://github.com/ketandas-codes/zillow-real-estate-scraper.git
cd zillow-real-estate-scraper
2️⃣ Create Virtual Environment
bash
## macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

## Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
requirements.txt:

text
selenium==4.15.2
undetected-chromedriver==3.5.4
selenium-stealth==1.0.1
pandas==2.1.4
numpy==1.26.3
python-dotenv==1.0.0
4️⃣ Verify Chrome Installation ✅
bash
## macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version

## Linux
google-chrome --version

## Windows
"C:\Program Files\Google\Chrome\Application\chrome.exe" --version
💻 Usage
▶️ Run the Scraper
bash
python zillow_scraper.py
## 🎯 Custom Search Location
Edit __main__ in zillow_scraper.py:

python
if __name__ == "__main__":
    scraper = Zillow_scraper(url="https://www.zillow.com/")
    scraper.script_rum(texts="Austin, TX")  # 👈 Change location here
📍 Supported formats:

City, State: "Austin, TX"

City only: "Austin"

State only: "Texas" or "TX"

Zip code: "78701"

## 📤 Output - Raw Data
File: Zillow_Propertys_data.csv

text
address | price_dollar | beds | baths | sqft
 Run the Data Cleaner
bash
python clean_zillow_data.py
 Output - Cleaned Data ✨
File: zillow_clean.csv

text
address | street_number | street_name | city | state | zip_code | price_dollar | beds | baths | sqft
🔧 Configuration & Customization
⚙️ Adjust Scraper Parameters
Edit values in zillow_scraper.py:

 TIMEOUT: Increase if network is slow (default: 10s)

 USER_AGENTS: Add more agents to rotate between them

 MAX_PAGES: Pages to scrape (default: 20)

 WINDOW_SIZE: Browser resolution (default: 1920x1080)

 HEADLESS_MODE: Set to False for debugging (default: True)

 Environment Variables
Create .env file in project root:

text
ZILLOW_URL=https://www.zillow.com/
TIMEOUT=10
MAX_PAGES=20
DEBUG_MODE=False
 Important Notes & Best Practices
 Chrome & Driver Compatibility
If you encounter driver version mismatch errors:

bash
## Update Chrome to latest version
pip install --upgrade undetected-chromedriver
 Anti-Detection Best Practices
 
✅ DO:

 Add random delays (1-3 seconds)

 Rotate user agents

 Use residential proxies for large jobs

 Respect robots.txt

 Spread requests over time

❌ DON'T:

 Scrape without delays

 Use same user-agent repeatedly

 Hammer the server with rapid requests

 Ignore blocking/CAPTCHA signals

 Extract personal data

 Rate Limiting & Ethical Scraping
 Zillow's servers get significant traffic. Be responsible:

 Don't scrape during peak hours if possible

 Increase delays between requests

 Monitor for blocking signals (403, 429 errors)

 Consider using proxies for large-scale jobs

 Test on small dataset first

## 📝 Common Use Cases
1.  Real Estate Market Analysis
Scrape property listings for Austin, TX, then analyze price trends and market insights.

2.  Price Trend Monitoring
Save scrapes with timestamps to track price changes over time and identify patterns.

3.  Portfolio Project Showcase
Use cleaned data to create visualizations, interactive maps, or dashboards for your portfolio.

## 📜 License
. MIT License

## 📬 Contact
. Ketan Das

. Python Developer | Web Scraping & Automation

. GitHub: @ketandas-codes

. 📧 Email: ketandas.codes@gmail.com
🐙 GitHub: @ketandas-codes
