CREATE DOMAIN currency AS DECIMAL(10, 2) CHECK (VALUE >= 0);
CREATE DOMAIN name_type AS VARCHAR(100) CHECK (VALUE <> '');

CREATE TABLE Companies (
    company_id SERIAL PRIMARY KEY,
    ticker_symbol VARCHAR(10) UNIQUE NOT NULL,
    company_name name_type NOT NULL,
    description TEXT,
    country VARCHAR(50)
);

CREATE TABLE Stock_Prices (
    price_id SERIAL PRIMARY KEY,
    company_id INT NOT NULL REFERENCES Companies(company_id),
    price_date DATE NOT NULL,
    open_price currency,
    close_price currency,
    high_price DECIMAL(10,5), 
    low_price DECIMAL(10,5),
    UNIQUE (company_id, price_date) -- Ensure no duplicate stock prices for the same company and date
);

-- Is a Stock Price
CREATE TABLE Adjusted_Stock_Prices (
    price_id INT PRIMARY KEY REFERENCES Stock_Prices(price_id),
    adj_open_price currency,
    adj_close_price currency
);

-- Weak Entity
CREATE TABLE MarketNews (
    company_id INT NOT NULL REFERENCES Companies(company_id),
    news_date DATE NOT NULL,
    headline TEXT,
    sentiment_score DECIMAL(5, 2),
    PRIMARY KEY (company_id, news_date)
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
