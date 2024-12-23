CREATE DOMAIN currency AS DECIMAL(10, 2) CHECK (VALUE >= 0);
CREATE DOMAIN name_type AS VARCHAR(100) CHECK (VALUE <> '');

CREATE TABLE Company (
    company_id SERIAL PRIMARY KEY,
    ticker_symbol VARCHAR(10) UNIQUE NOT NULL,
    company_name name_type NOT NULL,
    description TEXT,
    country VARCHAR(50),
    market_cap DECIMAL(20, 2),
    market VARCHAR(50),
    locale VARCHAR(50),
    primary_exchange VARCHAR(50),
    active BOOLEAN,
    currency_name VARCHAR(50),
    phone_number VARCHAR(15),
    sic_code VARCHAR(10),
    sic_description TEXT,
    total_employees INT,
    list_date DATE,
    share_class_shares_outstanding BIGINT,
    weighted_shares_outstanding BIGINT,
    round_lot INT
);

CREATE TABLE company_financials (
    financial_id SERIAL PRIMARY KEY,
    company_id INT NOT NULL REFERENCES Company(company_id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    filing_date DATE NOT NULL,
    acceptance_datetime TIMESTAMP NOT NULL,
    timeframe VARCHAR(50) NOT NULL,
    fiscal_period VARCHAR(10) NOT NULL,
    fiscal_year INT NOT NULL,
    cik VARCHAR(20) NOT NULL,
    sic VARCHAR(10) NOT NULL,
    source_filing_url TEXT,
    source_filing_file_url TEXT,
    equity DECIMAL(20, 2),
    long_term_debt DECIMAL(20, 2),
    current_liabilities DECIMAL(20, 2),
    liabilities DECIMAL(20, 2),
    accounts_payable DECIMAL(20, 2),
    assets DECIMAL(20, 2),
    current_assets DECIMAL(20, 2),
    inventory DECIMAL(20, 2),
    income_tax_expense DECIMAL(20, 2),
    operating_expenses DECIMAL(20, 2),
    gross_profit DECIMAL(20, 2),
    operating_income DECIMAL(20, 2),
    net_income DECIMAL(20, 2),
    revenues DECIMAL(20, 2),
    diluted_eps DECIMAL(10, 2),
    basic_eps DECIMAL(10, 2),
    net_cash_flow DECIMAL(20, 2)
);

CREATE TABLE Stock_Price (
    price_id SERIAL PRIMARY KEY,
    company_id INT NOT NULL REFERENCES Company(company_id),
    price_date DATE NOT NULL,
    open_price currency,
    close_price currency,
    high_price DECIMAL(10, 5), 
    low_price DECIMAL(10, 5),
    volume BIGINT,
    split_factor DECIMAL(10, 5),
    dividend currency,
    UNIQUE (company_id, price_date) -- Ensure no duplicate stock prices for the same company and date
);

-- Is a Stock Price
CREATE TABLE Adjusted_Stock_Price (
    price_id INT PRIMARY KEY REFERENCES Stock_Price(price_id),
    adj_open_price currency,
    adj_close_price currency, 
    adj_high_price DECIMAL(10, 5),
    adj_low_price DECIMAL(10, 5),
    adj_volume BIGINT
);

CREATE TABLE Dividend (
    dividend_id SERIAL PRIMARY KEY,
    company_id INT NOT NULL REFERENCES Company(company_id) ON DELETE CASCADE,
    cash_amount DECIMAL(10, 2),
    currency VARCHAR(10),
    declaration_date DATE,
    dividend_type VARCHAR(10),
    ex_dividend_date DATE,
    frequency INTEGER,
    pay_date DATE,
    record_date DATE 
);

CREATE TABLE Stock_Split (
    split_id SERIAL PRIMARY KEY,            
    company_id INT NOT NULL REFERENCES Company(company_id) ON DELETE CASCADE,  
    execution_date DATE,           
    split_from INT,             
    split_to INT     
);

CREATE TABLE IPO (
    ipo_id SERIAL PRIMARY KEY,
    ticker VARCHAR(10),
    last_updated DATE NOT NULL,
    issuer_name VARCHAR(255) NOT NULL,
    currency_code VARCHAR(10),
    us_code VARCHAR(20),
    isin VARCHAR(20),
    max_shares_offered BIGINT,
    lowest_offer_price DECIMAL(10, 2),
    highest_offer_price DECIMAL(10, 2),
    total_offer_size DECIMAL(20, 2),
    primary_exchange VARCHAR(10),
    shares_outstanding BIGINT,
    security_type VARCHAR(50),
    lot_size INT,
    security_description TEXT,
    ipo_status VARCHAR(50),
    final_issue_price DECIMAL(10, 2)
);

-- Weak Entity
CREATE TABLE MarketNews (
    company_id INT NOT NULL REFERENCES Company(company_id),
    news_date DATE NOT NULL,
    headline TEXT,
    sentiment_score DECIMAL(5, 2),
    title TEXT,
    author VARCHAR(100),
    article_id VARCHAR(255) NOT NULL, 
    publisher_name VARCHAR(255), 
    publisher_homepage_url TEXT,
    publisher_logo_url TEXT, 
    publisher_favicon_url TEXT, 
    article_url TEXT, 
    image_url TEXT, 
    description TEXT,
    PRIMARY KEY (company_id, news_date, article_id) 
);

CREATE INDEX idx_ticker_symbol ON Company(ticker_symbol);
CREATE INDEX idx_price_date ON Stock_Price(price_date);
CREATE INDEX idx_news_date ON MarketNews(news_date);
CREATE INDEX idx_company_news ON MarketNews(company_id, news_date);

CREATE OR REPLACE FUNCTION prevent_duplicate_stock_price()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM Stock_Price
        WHERE company_id = NEW.company_id AND price_date = NEW.price_date
    ) THEN
        RAISE EXCEPTION 'Duplicate stock price for the same company and date is not allowed.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER prevent_price_duplicates
BEFORE INSERT ON Stock_Price
FOR EACH ROW
EXECUTE FUNCTION prevent_duplicate_stock_price();
