from stockAPI import StockApi
from database import database
from operations import StockOperations

# APIs Used:
# - MarketStack: https://marketstack.com/
# - Polygon.io: https://polygon.io/

if __name__ == "__main__":
    marketstack_key = "29aaad172bd67bbefb3594346b7e58cb"
    polygon_key = "Fz1d2Tintn4Yjl4JVDLpqosrOodSBiph"

    stock_api = StockApi(marketstack_key, polygon_key)

    # List of stock tickers to process, for now we will keep just one for testing, since its lightweight
    ticker_list = ["AAPL"] 

    # Date range for fetching historical prices and financials
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

        # Fetch historical dividends from Polygon.io
        polygon_dividends = stock_api.get_polygon_dividends(ticker)
        if polygon_dividends:
            StockOperations().create_dividends(ticker, polygon_dividends)

        # Fetch stock splits from Polygon.io
        polygon_splits = stock_api.get_polygon_stock_splits(ticker)
        if polygon_splits:
            StockOperations().create_stock_splits(ticker, polygon_splits)

        polygon_ipos = stock_api.get_polygon_ipos(order="asc", limit=10)
        if polygon_ipos:
            StockOperations().create_ipos(polygon_ipos)

        # Fetch market news from Polygon.io
        polygon_news = stock_api.get_polygon_news(ticker)
        if polygon_news:
            StockOperations().create_market_news(ticker, polygon_news)

        # Fetch financial data from Polygon.io
        financials = stock_api.get_polygon_financials(
            ticker=ticker, 
            filing_date_gte=start_date, 
            filing_date_lt=end_date
        )
        if financials:
            StockOperations().create_financial_data(ticker, financials)

    database.close()
