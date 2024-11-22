from peewee import IntegrityError
from models import Company, StockPrice, AdjustedStockPrice, MarketNews
from datetime import datetime, timezone
class StockOperations:
    def create_company(self, company_data):
        """Insert or update a company record based on the API data."""
        try:
            ticker_symbol = company_data.get('symbols', company_data.get('symbol'))
            if not ticker_symbol:
                print("Warning: No 'symbols' or 'symbol' key found in company_data.")
                return

            Company.get_or_create(
                ticker_symbol=ticker_symbol,
                defaults={
                    'company_name': company_data.get('name', 'Unknown'),
                    'description': company_data.get('description'),
                    'country': company_data.get('stock_exchange', {}).get('country')
                }
            )
            print(f"Company {ticker_symbol} created or updated successfully.")
        except IntegrityError as e:
            print(f"Error creating/updating company {ticker_symbol}: {e}")


    def create_stock_prices(self, stock_price_data):
        """Insert stock price and adjusted stock price data."""
        for record in stock_price_data.get('data', []):
            try:
                # Normalize fields
                open_price = record.get('open')
                close_price = record.get('close')
                high_price = record.get('high')
                low_price = record.get('low')

                adj_open_price = record.get('adj_open')
                adj_close_price = record.get('adj_close')
                adj_high_price = record.get('adj_high')
                adj_low_price = record.get('adj_low')

                price_date = record.get('date')  # ISO 8601 format

                # Parse ISO 8601 date
                price_date = datetime.fromisoformat(price_date.split('T')[0]).date()

                # Find associated company
                company = Company.get_or_none(ticker_symbol=record.get('symbol'))
                
                if company:
                    # Create StockPrice entry
                    stock_price, created = StockPrice.get_or_create(
                        company=company,
                        price_date=price_date,
                        defaults={
                            'open_price': open_price,
                            'close_price': close_price,
                            'high_price': high_price,
                            'low_price': low_price
                        }
                    )
                    if created:
                        print(f"Stock price for {record.get('symbol')} on {price_date} created successfully.")
                    
                    # Create AdjustedStockPrice entry
                    if stock_price:
                        AdjustedStockPrice.get_or_create(
                            price=stock_price,
                            defaults={
                                'adj_open_price': adj_open_price,
                                'adj_close_price': adj_close_price,
                                'adj_high_price': adj_high_price,
                                'adj_low_price': adj_low_price
                            }
                        )
                        print(f"Adjusted stock price for {record.get('symbol')} on {price_date} created successfully.")
            except IntegrityError as e:
                print(f"Integrity Error creating stock price: {e}")
            except Exception as e:
                print(f"Error creating stock price: {e}")

    def update_company_with_polygon_details(self, ticker, polygon_data):
        """Update company details with additional data from Polygon.io."""
        try:
            company = Company.get_or_none(ticker_symbol=ticker)
            if company:
                company.description = polygon_data.get('results', {}).get('description', company.description)
                company.market_cap = polygon_data.get('results', {}).get('marketcap', company.market_cap)
                company.save()
                print(f"Company {ticker} updated with additional Polygon.io details.")
        except IntegrityError as e:
            print(f"Error updating company {ticker}: {e}")

    def create_market_news(self, ticker, news_data):
        """Insert market news records."""
        for article in news_data.get('results', []):
            try:
                company = Company.get_or_none(ticker_symbol=ticker)
                if company:
                    news_date = article['published_utc'].split("T")[0]  # Extract date from UTC timestamp
                    MarketNews.get_or_create(
                        company=company,
                        news_date=news_date,
                        defaults={
                            'headline': article['title'],
                            'sentiment_score': self._calculate_sentiment(article, ticker)
                        }
                    )
                    print(f"Market news for {ticker} on {news_date} created successfully.")
            except IntegrityError as e:
                print(f"Error creating market news: {e}")

    def _calculate_sentiment(self, article, ticker):
        """Extract sentiment for a specific ticker from the article."""
        insights = article.get('insights', [])
        for insight in insights:
            if insight['ticker'] == ticker:
                sentiment = insight.get('sentiment', 'neutral').lower()
                if sentiment == 'positive':
                    return 1
                elif sentiment == 'negative':
                    return -1
                return 0
        return 0
