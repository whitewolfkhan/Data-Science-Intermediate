import requests   # The requests module allows you to send HTTP requests using Python.
from bs4 import BeautifulSoup   # BeautifulSoup : helps parse (read & extract data) from HTML pages.
import yfinance as yf   # yfinance : library to directly fetch stock data from Yahoo Finance API instead of scraping manually.
import matplotlib.pyplot as plt
import pandas as pd 
import time


def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0 Safari/537.36"
    }   
    response = requests.get(url, headers=headers)
    if response.status_code == 200:    # 200 = successful, 404 = page not found, 429 = too many requests
        return response.text
    
    else:
        print(f"Failed to fetch page : {response.status_code}")
        return None
    
    
# print(fetch_page("https://example.com"))
def parseHtml(html):
    soup = BeautifulSoup(html, "html.parser")   # Parses raw html into a structured object
    return soup


def getStockPrice(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    # link = https://finance.yahoo.com/quote/AAPL/?p=AAPL (check out)
    html = fetch_page(url)
    if not html:
        return None
    
    soup = parseHtml(html)
    priceTag  = soup.find("fin-streamer", {"data-symbol" : ticker, "data-field" : "regularMarketPrice"})
    
    if priceTag:
        return priceTag.text
    else:
        print("Stock price not found")
        return None
    
   
# ticker = "AAPL" 
# price = getStockPrice(ticker)


ticker = yf.Ticker("AAPL")
# price = ticker.info.get("regularMarketPrice")

# if price:
#     print(f"The current price of {ticker} is ${price}")
# else:
#     print("Price not available")


# Plot Historical Stock Prices
# history = ticker.history(period="6mo")

# plt.plot(history.index, history["Close"], label="Close Price")
# plt.title("Apple Stock Price last 6 month")
# plt.xlabel("Date")
# plt.ylabel("Price($)")
# plt.legend()
# plt.show()
   
   
# Add Moving Averages (Technical Indicator) (Helps identify trends (uptrend, downtrend, sideways)) 
# history["20 Day MA"] = history["Close"].rolling(20).mean()
# history["50 Day MA"] = history["Close"].rolling(50).mean()

# plt.plot(history.index, history["Close"], label="Close") 
# plt.plot(history.index, history["20 Day MA"], label="20 Day MA") 
# plt.plot(history.index, history["50 Day MA"], label="50 Day MA")
# plt.legend()
# plt.title("Moving Averages")
# plt.show()   


# Compare Multiple Stocks
stocks = ["AAPL", "TSLA", "MSFT", "GOOGL", "AMZN"]
data = yf.download(stocks, period="3mo")["Close"]

# data.plot(figsize=(10,6))
# plt.title("Stock Comparison")
# plt.xlabel("Date")
# plt.ylabel("Price($)")
# plt.show()   



# Download Fundamental Data
# print("PE Ratio:", ticker.info.get("forwardPE"))
# print("Market Cap:", ticker.info.get("marketCap"))
# print("EPS:", ticker.info.get("trailingEps"))



# Create a report of fundamentals for 5 companies.
# fundamentalList = []

# for symbol in stocks:
#     ticker = yf.Ticker(symbol)
#     info = ticker.info
#     fundamentalList.append({
#         "Ticker": symbol,
#         "Company Name": info.get("shortName"),
#         "PE Ratio": info.get("forwardPE"),
#         "Market Cap": ticker.info.get("marketCap"),
#         "EPS": ticker.info.get("trailingEps"),
#         "Dividend Yield" : info.get("dividendYield")
#     })
    
# fundamentalsDF = pd.DataFrame(fundamentalList)  # convert list to a dataframe for a clean data

# print(fundamentalsDF)
# fundamentalsDF.to_csv("fundamentals report.csv", index=False)   # save in csv file



# Save the Company data
# history.to_csv("AAPL_history.csv")
# print("Data saved to AAPL_history.csv")



# A simple Stock Portfolio Tracker
# portfolio = {
#     "AAPL" : 10,
#     "TSLA" : 5,
#     "MSFT": 8,
#     "GOOGL": 2,
#     "AMZN" : 1
    
# }

# portfolioData = []

# for symbol, shares in portfolio.items():    # .items() returns key-value pairs from the dictionary.
#     ticker = yf.Ticker(symbol)
#     price = ticker.info.get("regularMarketPrice")  # Running market price
#     totalValue = price * shares if price else 0
#     portfolioData.append({
#         "Ticker" : symbol,
#         "Shares" : shares,
#         "Price($)" : price,
#         "Total Value ($)" : totalValue
#     })
    
# df = pd.DataFrame(portfolioData)
    
# totalPortValue = df["Total Value ($)"].sum()
    
# print(df)
# print(f"\n Total portfolio value: ${totalPortValue:,.2f}")
# # df.to_csv("portfolioreport.csv", index=False)

# plt.figure(figsize=(8,8))
# plt.pie(df["Total Value ($)"], labels=df["Ticker"], autopct="%1.1f%%", startangle=140)    
# plt.title("Portfolio Distribution by stock")
# plt.show()



# Update for real time tracking
def trackStockPrice(ticker, interval=60):
    while True:
        price = getStockPrice(ticker)
        if price:
            print(f"{ticker}: ${price}")
        time.sleep(interval)
        
trackStockPrice(ticker, 2)