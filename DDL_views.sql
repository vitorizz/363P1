CREATE VIEW AdminView AS
SELECT 
    c.company_id,
    c.company_name, 
    c.ticker_symbol,
    c.market_cap,
    c.country,
    s.price_date, 
    s.open_price, 
    s.close_price, 
    s.high_price, 
    s.low_price,
    s.volume,
    s.split_factor,
    n.news_date,
    n.headline,
    n.title,
    n.sentiment_score,
    n.author,
    n.article_url
FROM Company c
LEFT JOIN Stock_Price s ON c.company_id = s.company_id
LEFT JOIN MarketNews n ON c.company_id = n.company_id;

CREATE VIEW UserView AS
SELECT 
    c.company_name, 
    c.ticker_symbol,
    s.price_date, 
    s.close_price,
    n.news_date,
    n.headline,
    n.title
FROM Company c
LEFT JOIN Stock_Price s ON c.company_id = s.company_id
LEFT JOIN MarketNews n ON c.company_id = n.company_id
WHERE n.sentiment_score IS NOT NULL; -- Only show news with sentiment analysis available
