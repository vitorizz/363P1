from stockAPI import StockApi
from database import database
from operations import StockOperations

# APIs Used:
# - MarketStack: https://marketstack.com/
# - Polygon.io: https://polygon.io/

if __name__ == "__main__":
    # Replace with your actual API keys
    marketstack_key = "664f2cfe477fecfb277c3f867fb9d887"
    polygon_key = "Fz1d2Tintn4Yjl4JVDLpqosrOodSBiph"

    # Initialize API handler
    stock_api = StockApi(marketstack_key, polygon_key)

    # List of stock tickers to process
    # ticker_list = ["AAPL", "MSFT", "GOOG", "TSLA", "AMZN"]
    ticker_list = ["AAPL"]


    # Date range for fetching historical prices
    start_date = "2024-10-01"
    end_date = "2024-11-15"

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

        # Fetch market news from Polygon.io
        polygon_news = stock_api.get_polygon_news(ticker)
        if polygon_news:
            StockOperations().create_market_news(ticker, polygon_news)

    # Close the database connection
    database.close()
