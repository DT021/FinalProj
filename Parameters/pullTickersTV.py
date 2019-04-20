import requests
from bs4 import BeautifulSoup as BS

def pullTickersTV(url):
	page = requests.get(url)
	soup = BS(page.content, 'html.parser')
	tickers = soup.find_all(True, {"class": ["tv-screener__symbol","apply-common-tooltip"]})

	with open("volatileTickers.txt", "w") as file:

		for ticker in tickers:

			if len(ticker.text) < 5:
				print(ticker.text, file=file)


pullTickersTV("https://www.tradingview.com/markets/stocks-usa/market-movers-most-volatile/")
