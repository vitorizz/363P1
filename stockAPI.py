import requests

class StockApi:
    def __init__(self, marketstack_key, polygon_key):
        self.marketstack_key = marketstack_key
        self.polygon_key = polygon_key

    # Fetch company details from MarketStack
    def get_marketstack_ticker_details(self, ticker):
        url = f"http://api.marketstack.com/v1/tickers/{ticker}"
        response = requests.get(url, params={'access_key': self.marketstack_key})

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching MarketStack data for ticker {ticker}: {response.status_code}")
            return None
        
    # Fetch financial data from Polygon.io
    def get_polygon_financials(self, ticker, filing_date_gte, filing_date_lt, timeframe="annual", limit=5, order="asc"):
        url = f"https://api.polygon.io/vX/reference/financials"
        response = requests.get(url, params={
            'ticker': ticker,
            'filing_date.gte': filing_date_gte,
            'filing_date.lt': filing_date_lt,
            'timeframe': timeframe,
            'limit': limit,
            'order': order,
            'apiKey': self.polygon_key
        })

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching Polygon financials data for ticker {ticker}: {response.status_code}")
            return None


    # Fetch historical stock prices from MarketStack
    def get_marketstack_eod(self, ticker, start_date, end_date):
        url = "http://api.marketstack.com/v1/eod"
        response = requests.get(url, params={
            'access_key': self.marketstack_key,
            'symbols': ticker,
            'date_from': start_date,
            'date_to': end_date
        })

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching MarketStack EOD data for ticker {ticker}: {response.status_code}")
            return None

    # Fetch company details from Polygon.io
    def get_polygon_ticker_details(self, ticker):
        url = f"https://api.polygon.io/v3/reference/tickers/{ticker}"
        response = requests.get(url, params={'apiKey': self.polygon_key})

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching Polygon data for ticker {ticker}: {response.status_code}")
            return None

    # Fetch historical stock prices from Polygon.io
    def get_polygon_eod(self, ticker, start_date, end_date):
        url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}"
        response = requests.get(url, params={'apiKey': 'ernOzepzqAEFJdCq1gGfkgBAkkSpo1Kw'})

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching Polygon EOD data for ticker {ticker}: {response.status_code}")
            return None

    # Fetch market news from Polygon.io
    def get_polygon_news(self, ticker):
        url = f"https://api.polygon.io/v2/reference/news"
        response = requests.get(url, params={'ticker': ticker, 'limit':'500', 'published_utc.gte':
        '2023-01-01', 'published_utc.lte': '2023-12-01','apiKey': self.polygon_key})

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching Polygon news for ticker {ticker}: {response.status_code}")
            return None
