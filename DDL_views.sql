-- Full Access View
CREATE VIEW AdminView AS
SELECT 
    c.company_name, 
    s.price_date, 
    s.open_price, 
    s.close_price, 
    s.high_price, 
    s.low_price,
    n.news_date,
    n.headline,
    n.sentiment_score
FROM Companies c
LEFT JOIN StockPrices s ON c.company_id = s.company_id
LEFT JOIN MarketNews n ON c.company_id = n.company_id;

-- Restricted View
CREATE VIEW UserView AS
SELECT 
    c.company_name, 
    s.price_date, 
    s.close_price,
    n.news_date,
    n.headline
FROM Companies c
LEFT JOIN StockPrices s ON c.company_id = s.company_id
LEFT JOIN MarketNews n ON c.company_id = n.company_id;
