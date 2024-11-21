from stockAPI import StockApi
from database import database
from operations import StockOperations

# APIs Used:
# - MarketStack: https://marketstack.com/
# - Polygon.io: https://polygon.io/

if __name__ == "__main__":
    # Replace with your actual API keys
    marketstack_key = "904c5a774b7856475c7159d50ddc972b"
    polygon_key = "ernOzepzqAEFJdCq1gGfkgBAkkSpo1Kw"

    # Initialize API handler
    stock_api = StockApi(marketstack_key, polygon_key)

    # List of stock tickers to process
    ticker_list = ["AAPL", "MSFT", "GOOG", "TSLA", "AMZN"]

    # Date range for fetching historical prices
    start_date = "2023-01-01"
    end_date = "2023-01-31"

    for ticker in ticker_list:
        # Fetch company details from MarketStack
        marketstack_details = stock_api.get_marketstack_ticker_details(ticker)
        if marketstack_details:
            StockOperations().create_company(marketstack_details)

        # Fetch historical prices from MarketStack
        marketstack_prices = stock_api.get_marketstack_eod(ticker, start_date, end_date)
        if marketstack_prices:
            StockOperations().create_stock_prices(marketstack_prices)

        # Fetch company details from Polygon.io
        polygon_details = stock_api.get_polygon_ticker_details(ticker)
        if polygon_details:
            StockOperations().update_company_with_polygon_details(ticker, polygon_details)

        # Fetch historical prices from Polygon.io
        polygon_prices = stock_api.get_polygon_eod(ticker, start_date, end_date)
        if polygon_prices:
            StockOperations().create_stock_prices(polygon_prices)

        # Fetch market news from Polygon.io
        polygon_news = stock_api.get_polygon_news(ticker)
        if polygon_news:
            StockOperations().create_market_news(ticker, polygon_news)

    # Close the database connection
    database.close()
