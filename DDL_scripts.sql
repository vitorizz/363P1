CREATE DOMAIN currency AS DECIMAL(10, 2) CHECK (VALUE >= 0);
CREATE DOMAIN name_type AS VARCHAR(100) CHECK (VALUE <> '');

CREATE TABLE Companies (
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

CREATE TABLE Stock_Prices (
    price_id SERIAL PRIMARY KEY,
    company_id INT NOT NULL REFERENCES Companies(company_id),
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
CREATE TABLE Adjusted_Stock_Prices (
    price_id INT PRIMARY KEY REFERENCES Stock_Prices(price_id),
    adj_open_price currency,
    adj_close_price currency, 
    adj_high_price DECIMAL(10, 5),
    adj_low_price DECIMAL(10, 5),
    adj_volume BIGINT
);

-- Weak Entity
CREATE TABLE MarketNews (
    company_id INT NOT NULL REFERENCES Companies(company_id),
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

CREATE INDEX idx_ticker_symbol ON Companies(ticker_symbol);
CREATE INDEX idx_price_date ON Stock_Prices(price_date);
CREATE INDEX idx_news_date ON MarketNews(news_date);
CREATE INDEX idx_company_news ON MarketNews(company_id, news_date);

CREATE OR REPLACE FUNCTION prevent_duplicate_stock_prices()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM Stock_Prices
        WHERE company_id = NEW.company_id AND price_date = NEW.price_date
    ) THEN
        RAISE EXCEPTION 'Duplicate stock price for the same company and date is not allowed.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER prevent_price_duplicates
BEFORE INSERT ON Stock_Prices
FOR EACH ROW
EXECUTE FUNCTION prevent_duplicate_stock_prices();
