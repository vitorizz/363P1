from peewee import IntegrityError
from models import Company, StockPrice, AdjustedStockPrice, MarketNews, CompanyFinancials, StockSplit, Dividend, IPO
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

    def create_financial_data(self, ticker, financial_data):
        """Insert financial data records."""
        for record in financial_data.get('results', []):
            try:
                company = Company.get_or_none(ticker_symbol=ticker)
                if company:
                   
                    start_date = record.get('start_date')
                    end_date = record.get('end_date')
                    filing_date = record.get('filing_date')
                    acceptance_datetime = record.get('acceptance_datetime')
                    timeframe = record.get('timeframe')
                    fiscal_period = record.get('fiscal_period')
                    fiscal_year = record.get('fiscal_year')
                    cik = record.get('cik')
                    sic = record.get('sic')
                    source_filing_url = record.get('source_filing_url')
                    source_filing_file_url = record.get('source_filing_file_url')

                    financials = record.get('financials', {})
                    balance_sheet = financials.get('balance_sheet', {})
                    income_statement = financials.get('income_statement', {})
                    cash_flow_statement = financials.get('cash_flow_statement', {})

                    CompanyFinancials.create(
                        company=company,
                        start_date=start_date,
                        end_date=end_date,
                        filing_date=filing_date,
                        acceptance_datetime=acceptance_datetime,
                        timeframe=timeframe,
                        fiscal_period=fiscal_period,
                        fiscal_year=fiscal_year,
                        cik=cik,
                        sic=sic,
                        source_filing_url=source_filing_url,
                        source_filing_file_url=source_filing_file_url,
                        equity=balance_sheet.get('equity', {}).get('value'),
                        long_term_debt=balance_sheet.get('long_term_debt', {}).get('value'),
                        current_liabilities=balance_sheet.get('current_liabilities', {}).get('value'),
                        liabilities=balance_sheet.get('liabilities', {}).get('value'),
                        accounts_payable=balance_sheet.get('accounts_payable', {}).get('value'),
                        assets=balance_sheet.get('assets', {}).get('value'),
                        current_assets=balance_sheet.get('current_assets', {}).get('value'),
                        inventory=balance_sheet.get('inventory', {}).get('value'),
                        income_tax_expense=income_statement.get('income_tax_expense_benefit', {}).get('value'),
                        operating_expenses=income_statement.get('operating_expenses', {}).get('value'),
                        gross_profit=income_statement.get('gross_profit', {}).get('value'),
                        operating_income=income_statement.get('operating_income_loss', {}).get('value'),
                        net_income=income_statement.get('net_income_loss', {}).get('value'),
                        revenues=income_statement.get('revenues', {}).get('value'),
                        diluted_eps=income_statement.get('diluted_earnings_per_share', {}).get('value'),
                        basic_eps=income_statement.get('basic_earnings_per_share', {}).get('value'),
                        net_cash_flow=cash_flow_statement.get('net_cash_flow', {}).get('value'),
                    )
                    print(f"Financial data for {ticker} from {start_date} to {end_date} created successfully.")
            except IntegrityError as e:
                print(f"Error creating financial data for {ticker}: {e}")
            except Exception as e:
                print(f"Unexpected error creating financial data for {ticker}: {e}")



    def create_stock_prices(self, stock_price_data):
        """Insert stock price and adjusted stock price data."""
        for record in stock_price_data.get('data', []):
            try:
                # Normalize fields
                open_price = record.get('open')
                close_price = record.get('close')
                high_price = record.get('high')
                low_price = record.get('low')
                volume = record.get('volume')
                split_factor = record.get('split_factor')
                dividend = record.get('dividend')

                adj_open_price = record.get('adj_open')
                adj_close_price = record.get('adj_close')
                adj_high_price = record.get('adj_high')
                adj_low_price = record.get('adj_low')
                adj_volume = record.get('adj_volume')

                price_date = record.get('date')  

                price_date = datetime.fromisoformat(price_date.split('T')[0]).date()

                company = Company.get_or_none(ticker_symbol=record.get('symbol'))
                
                if company:
                    stock_price, created = StockPrice.get_or_create(
                        company=company,
                        price_date=price_date,
                        defaults={
                            'open_price': open_price,
                            'close_price': close_price,
                            'high_price': high_price,
                            'low_price': low_price,
                            'volume': volume,
                            'split_factor': split_factor,
                            'dividend': dividend
                        }
                    )
                    if created:
                        print(f"Stock price for {record.get('symbol')} on {price_date} created successfully.")
                    
                    if stock_price:
                        AdjustedStockPrice.get_or_create(
                            price=stock_price,
                            defaults={
                                'adj_open_price': adj_open_price,
                                'adj_close_price': adj_close_price,
                                'adj_high_price': adj_high_price,
                                'adj_low_price': adj_low_price,
                                'adj_volume': adj_volume
                            }
                        )
                        print(f"Adjusted stock price for {record.get('symbol')} on {price_date} created successfully.")
            except IntegrityError as e:
                print(f"Integrity Error creating stock price: {e}")
            except Exception as e:
                print(f"Error creating stock price: {e}")

    
    def create_dividends(self, ticker, dividend_data):
        try:
            for record in dividend_data.get('results', []):
                cash_amount = record.get('cash_amount')
                currency = record.get('currency')
                declaration_date = record.get('declaration_date')
                dividend_type = record.get('dividend_type')
                ex_dividend_date = record.get('ex_dividend_date')
                frequency = record.get('frequency')
                pay_date = record.get('pay_date')
                record_date = record.get('record_date')

                company = Company.get_or_none(ticker_symbol=ticker)
                if not company:
                    print(f"Skipping record due to missing company for ticker: {ticker}")
                    continue

                Dividend.get_or_create(
                    company=company,
                    defaults={
                        'cash_amount': cash_amount,
                        'currency': currency,
                        'declaration_date': declaration_date,
                        'dividend_type': dividend_type,
                        'ex_dividend_date': ex_dividend_date,
                        'frequency': frequency,
                        'pay_date': pay_date,
                        'record_date': record_date
                    }
                )
                print(f"Dividend for {ticker} on {declaration_date} created or updated successfully.")
        except IntegrityError as e:
            print(f"Error creating/updating dividend: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    
    def create_stock_splits(self, ticker, split_data):
        try:
            for record in split_data.get('results', []):
                execution_date = record.get('execution_date')
                split_from = record.get('split_from')
                split_to = record.get('split_to')

                company = Company.get_or_none(ticker_symbol=ticker)
                if not company:
                    print(f"Skipping record due to missing company for ticker: {ticker}")
                    continue

                StockSplit.get_or_create(
                    company=company,
                    execution_date=execution_date,
                    defaults={
                        'split_from': split_from,
                        'split_to': split_to
                    }
                )
                print(f"Stock split for {ticker} on {execution_date} created or updated successfully.")
        except IntegrityError as e:
            print(f"Error creating/updating stock split: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


    def update_company_with_polygon_details(self, ticker, polygon_data):
        """Update company details with additional data from Polygon.io."""
        try:
            company = Company.get_or_none(ticker_symbol=ticker)
            if company:
                company.description = polygon_data.get('results', {}).get('description', company.description)
                company.market_cap = polygon_data.get('results', {}).get('marketcap', company.market_cap)
                company.market = polygon_data.get('results', {}).get('market', company.market)
                company.locale = polygon_data.get('results', {}).get('locale', company.locale)
                company.primary_exchange = polygon_data.get('results', {}).get('primary_exchange', company.primary_exchange)
                company.active = polygon_data.get('results', {}).get('active', company.active)
                company.currency_name = polygon_data.get('results', {}).get('currency_name', company.currency_name)
                company.phone_number = polygon_data.get('results', {}).get('phone_number', company.phone_number)
                company.sic_code = polygon_data.get('results', {}).get('sic_code', company.sic_code)
                company.sic_description = polygon_data.get('results', {}).get('sic_description', company.sic_description)
                company.total_employees = polygon_data.get('results', {}).get('total_employees', company.total_employees)
                company.list_date = polygon_data.get('results', {}).get('list_date', company.list_date)
                company.share_class_shares_outstanding = polygon_data.get('results', {}).get('share_class_shares_outstanding', company.share_class_shares_outstanding)
                company.weighted_shares_outstanding = polygon_data.get('results', {}).get('weighted_shares_outstanding', company.weighted_shares_outstanding)
                company.round_lot = polygon_data.get('results', {}).get('round_lot', company.round_lot)
                company.save()
                print(f"Company {ticker} updated with additional Polygon.io details.")
        except IntegrityError as e:
            print(f"Error updating company {ticker}: {e}")

    def create_ipos(self, ipo_data):
        """Insert IPO data records."""
        for record in ipo_data.get('results', []):
            try:
                ticker = record.get('ticker')
                last_updated = record.get('last_updated')
                issuer_name = record.get('issuer_name')
                currency_code = record.get('currency_code')
                us_code = record.get('us_code')
                isin = record.get('isin')
                max_shares_offered = record.get('max_shares_offered')
                lowest_offer_price = record.get('lowest_offer_price')
                highest_offer_price = record.get('highest_offer_price')
                total_offer_size = record.get('total_offer_size')
                primary_exchange = record.get('primary_exchange')
                shares_outstanding = record.get('shares_outstanding')
                security_type = record.get('security_type')
                lot_size = record.get('lot_size')
                security_description = record.get('security_description')
                ipo_status = record.get('ipo_status')
                final_issue_price = record.get('final_issue_price')

                if not issuer_name:
                    print(f"Skipping record due to missing issuer name: {record}")
                    continue

                IPO.get_or_create(
                    ticker=ticker,
                    last_updated=last_updated,
                    defaults={
                        'issuer_name': issuer_name,
                        'currency_code': currency_code,
                        'us_code': us_code,
                        'isin': isin,
                        'max_shares_offered': max_shares_offered,
                        'lowest_offer_price': lowest_offer_price,
                        'highest_offer_price': highest_offer_price,
                        'total_offer_size': total_offer_size,
                        'primary_exchange': primary_exchange,
                        'shares_outstanding': shares_outstanding,
                        'security_type': security_type,
                        'lot_size': lot_size,
                        'security_description': security_description,
                        'ipo_status': ipo_status,
                        'final_issue_price': final_issue_price
                    }
                )
                print(f"IPO data for {ticker or issuer_name} created or updated successfully.")
            except IntegrityError as e:
                print(f"Error creating/updating IPO data: {e}")
            except Exception as e:
                print(f"Unexpected error creating IPO data: {e}")


    def create_market_news(self, ticker, news_data):
        """Insert market news records."""
        for article in news_data.get('results', []):
            try:
                company = Company.get_or_none(ticker_symbol=ticker)
                if company:
                    news_date = article['published_utc'].split("T")[0]  
                    MarketNews.get_or_create(
                        company=company,
                        news_date=news_date,
                        defaults={
                            'headline': article.get('title', ''),
                            'sentiment_score': self._calculate_sentiment(article, ticker),
                            'title': article.get('title', ''),
                            'author': article.get('author', ''),
                            'article_id': article.get('id', ''),
                            'publisher_name': article.get('publisher', {}).get('name', ''),
                            'publisher_homepage_url': article.get('publisher', {}).get('homepage_url', ''),
                            'publisher_logo_url': article.get('publisher', {}).get('logo_url', ''),
                            'publisher_favicon_url': article.get('publisher', {}).get('favicon_url', ''),
                            'article_url': article.get('article_url', ''),
                            'image_url': article.get('image_url', ''),
                            'description': article.get('description', ''),
                        }
                    )
                    print(f"Market news for {ticker} on {news_date} created successfully.")
            except IntegrityError as e:
                print(f"Error creating market news: {e}")
            except Exception as e:
                print(f"Unexpected error creating market news: {e}")


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
