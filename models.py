from peewee import *
from database import database 

class BaseModel(Model):
    class Meta:
        database = database

class Company(BaseModel):
    company_id = AutoField()
    ticker_symbol = CharField(unique=True, max_length=10)
    company_name = CharField(max_length=100, constraints=[Check("company_name <> ''")])
    description = TextField(null=True)
    country = CharField(max_length=50, null=True)
    market_cap = DecimalField(max_digits=20, decimal_places=2, null=True)
    market = CharField(max_length=50, null=True)
    locale = CharField(max_length=50, null=True)
    primary_exchange = CharField(max_length=50, null=True)
    active = BooleanField(default=True)
    currency_name = CharField(max_length=50, null=True)
    phone_number = CharField(max_length=15, null=True)
    sic_code = CharField(max_length=10, null=True)
    sic_description = TextField(null=True)
    total_employees = IntegerField(null=True)
    list_date = DateField(null=True)
    share_class_shares_outstanding = BigIntegerField(null=True)
    weighted_shares_outstanding = BigIntegerField(null=True)
    round_lot = IntegerField(null=True)

    class Meta:
        table_name = 'company'

class CompanyFinancials(BaseModel):
    financial_id = AutoField()
    company = ForeignKeyField(Company, backref='financials', on_delete='CASCADE')
    start_date = DateField(null=False)
    end_date = DateField(null=False)
    filing_date = DateField(null=False)
    acceptance_datetime = DateTimeField(null=False)
    timeframe = CharField(max_length=50, null=False)
    fiscal_period = CharField(max_length=10, null=False)
    fiscal_year = IntegerField(null=False)
    cik = CharField(max_length=20, null=False)
    sic = CharField(max_length=10, null=False)
    source_filing_url = TextField(null=True)
    source_filing_file_url = TextField(null=True)
    equity = DecimalField(max_digits=20, decimal_places=2, null=True)
    long_term_debt = DecimalField(max_digits=20, decimal_places=2, null=True)
    current_liabilities = DecimalField(max_digits=20, decimal_places=2, null=True)
    liabilities = DecimalField(max_digits=20, decimal_places=2, null=True)
    accounts_payable = DecimalField(max_digits=20, decimal_places=2, null=True)
    assets = DecimalField(max_digits=20, decimal_places=2, null=True)
    current_assets = DecimalField(max_digits=20, decimal_places=2, null=True)
    inventory = DecimalField(max_digits=20, decimal_places=2, null=True)
    income_tax_expense = DecimalField(max_digits=20, decimal_places=2, null=True)
    operating_expenses = DecimalField(max_digits=20, decimal_places=2, null=True)
    gross_profit = DecimalField(max_digits=20, decimal_places=2, null=True)
    operating_income = DecimalField(max_digits=20, decimal_places=2, null=True)
    net_income = DecimalField(max_digits=20, decimal_places=2, null=True)
    revenues = DecimalField(max_digits=20, decimal_places=2, null=True)
    diluted_eps = DecimalField(max_digits=10, decimal_places=2, null=True)
    basic_eps = DecimalField(max_digits=10, decimal_places=2, null=True)
    net_cash_flow = DecimalField(max_digits=20, decimal_places=2, null=True)

    class Meta:
        table_name = 'company_financials'


class StockPrice(BaseModel):
    price_id = AutoField()
    company = ForeignKeyField(Company, backref='stock_prices', on_delete='CASCADE')
    price_date = DateField()
    open_price = DecimalField(max_digits=10, decimal_places=2, constraints=[Check("open_price >= 0")])
    close_price = DecimalField(max_digits=10, decimal_places=2, constraints=[Check("close_price >= 0")])
    high_price = DecimalField(max_digits=10, decimal_places=5, null=True)
    low_price = DecimalField(max_digits=10, decimal_places=5, null=True)
    volume = BigIntegerField(null=True)
    split_factor = DecimalField(max_digits=10, decimal_places=5, null=True)
    dividend = DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        table_name = 'stock_price'
        indexes = (
            (('company', 'price_date'), True),  
        )

class AdjustedStockPrice(BaseModel):
    price = ForeignKeyField(StockPrice, backref='adjusted_prices', primary_key=True, on_delete='CASCADE')
    adj_open_price = DecimalField(max_digits=10, decimal_places=2, constraints=[Check("adj_open_price >= 0")])
    adj_close_price = DecimalField(max_digits=10, decimal_places=2, constraints=[Check("adj_close_price >= 0")])
    adj_high_price = DecimalField(max_digits=10, decimal_places=5, null=True)
    adj_low_price = DecimalField(max_digits=10, decimal_places=5, null=True)
    adj_volume = BigIntegerField(null=True)

    class Meta:
        table_name = 'adjusted_stock_price'

class Dividend(BaseModel):
    dividend_id = AutoField()
    company = ForeignKeyField(Company, backref='dividends', on_delete='CASCADE')
    cash_amount = DecimalField(max_digits=10, decimal_places=2, null=False)
    currency = CharField(max_length=10, null=False)
    declaration_date = DateField(null=False)
    dividend_type = CharField(max_length=10, null=False)
    ex_dividend_date = DateField(null=False)
    frequency = IntegerField(null=False)
    pay_date = DateField(null=False)
    record_date = DateField(null=False)

    class Meta:
        table_name = 'dividend'

class StockSplit(BaseModel):
    split_id = AutoField()
    company = ForeignKeyField(Company, backref='stock_splits', on_delete='CASCADE')
    execution_date = DateField(null=False)
    split_from = IntegerField(null=False)
    split_to = IntegerField(null=False)

    class Meta:
        table_name = 'stock_split'

class IPO(BaseModel):
    ipo_id = AutoField()
    ticker = CharField(max_length=10, null=True)
    last_updated = DateField()
    issuer_name = CharField(max_length=255)
    currency_code = CharField(max_length=10, null=True)
    us_code = CharField(max_length=20, null=True)
    isin = CharField(max_length=20, null=True)
    max_shares_offered = BigIntegerField(null=True)
    lowest_offer_price = DecimalField(max_digits=10, decimal_places=2, null=True)
    highest_offer_price = DecimalField(max_digits=10, decimal_places=2, null=True)
    total_offer_size = DecimalField(max_digits=20, decimal_places=2, null=True)
    primary_exchange = CharField(max_length=10, null=True)
    shares_outstanding = BigIntegerField(null=True)
    security_type = CharField(max_length=50, null=True)
    lot_size = IntegerField(null=True)
    security_description = TextField(null=True)
    ipo_status = CharField(max_length=50, null=True)
    final_issue_price = DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        table_name = 'ipo'

class MarketNews(BaseModel):
    company = ForeignKeyField(Company, backref='market_news', on_delete='CASCADE')
    news_date = DateField()
    headline = TextField(null=True)
    sentiment_score = DecimalField(max_digits=5, decimal_places=2, null=True)
    title = TextField(null=True)
    author = CharField(max_length=100, null=True)
    article_id = CharField(max_length=255, unique=True, null=False)  
    publisher_name = CharField(max_length=255, null=True)
    publisher_homepage_url = TextField(null=True)
    publisher_logo_url = TextField(null=True)
    publisher_favicon_url = TextField(null=True)
    article_url = TextField(null=True)
    image_url = TextField(null=True)
    description = TextField(null=True)

    class Meta:
        table_name = 'marketnews'
        primary_key = CompositeKey('company', 'news_date', 'id')



    class Meta:
        table_name = 'marketnews'
        primary_key = CompositeKey('company', 'news_date')
