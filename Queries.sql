--Basic SELECT with Simple WHERE Clause
SELECT company_name, market_cap, country
FROM Company
WHERE total_employees > 1000;

--Basic SELECT with Simple GROUP BY Clause
--Without HAVING Clause
SELECT country, COUNT(*) AS company_count
FROM Company
GROUP BY country;

--With HAVING Clause
SELECT country, COUNT(*) AS company_count
FROM Company
GROUP BY country
HAVING COUNT(*) > 3;

-- Simple Join Query and Cartesian Product
-- Simple Join Query
SELECT c.company_name, s.price_date, s.close_price
FROM Company c
INNER JOIN Stock_Price s ON c.company_id = s.company_id
WHERE s.close_price > 100;

-- Equivalent Cartesian Product with WHERE Clause
SELECT c.company_name, s.price_date, s.close_price
FROM Company c, Stock_Price s
WHERE c.company_id = s.company_id AND s.close_price > 100;

-- Various Join Types
-- INNER JOIN
SELECT c.company_name, n.headline
FROM Company c
INNER JOIN MarketNews n ON c.company_id = n.company_id;

-- LEFT OUTER JOIN
SELECT c.company_name, n.headline
FROM Company c
LEFT JOIN MarketNews n ON c.company_id = n.company_id;

-- RIGHT OUTER JOIN
SELECT c.company_name, n.headline
FROM Company c
RIGHT JOIN MarketNews n ON c.company_id = n.company_id;

-- FULL OUTER JOIN
SELECT c.company_name, n.headline
FROM Company c
FULL OUTER JOIN MarketNews n ON c.company_id = n.company_id;

-- Use of NULL Values
SELECT c.company_name
FROM Company c
WHERE c.market_cap IS NULL;

-- Correlated Queries
-- Example 1
SELECT company_name
FROM Company c
WHERE EXISTS (
    SELECT 1
    FROM Stock_Price s
    WHERE s.company_id = c.company_id AND s.close_price > 200
);

-- Example 2
SELECT company_name, total_employees
FROM Company c
WHERE total_employees > (
    SELECT AVG(total_employees)
    FROM Company
    WHERE country = c.country
);

-- Set Operations
-- UNION
SELECT company_name FROM Company WHERE country = 'USA'
UNION
SELECT company_name FROM Company WHERE market_cap > 5000000000;

-- INTERSECT
SELECT company_name FROM Company WHERE country = 'USA'
INTERSECT
SELECT company_name FROM Company WHERE total_employees > 500;

-- DIFFERENCE
SELECT company_name FROM Company WHERE country = 'USA'
EXCEPT
SELECT company_name FROM Company WHERE total_employees > 500;

-- Without Using Set Operations
-- UNION Equivalent
SELECT DISTINCT company_name 
FROM Company 
WHERE country = 'USA' OR total_employees > 500;

-- INTERSECT Equivalent
SELECT c1.company_name
FROM Company c1
JOIN Company c2 ON c1.company_name = c2.company_name
WHERE c1.country = 'USA' AND c2.total_employees > 500;

-- DIFFERENCE Equivalent
SELECT c1.company_name
FROM Company c1
LEFT JOIN (
    SELECT company_name FROM Company WHERE total_employees > 500
) c2 ON c1.company_name = c2.company_name
WHERE c1.country = 'USA' AND c2.company_name IS NULL;

-- View with Hard-Coded Criteria
CREATE VIEW ManyEmployeeCompanies AS
SELECT company_name, total_employees
FROM Company
WHERE total_employees > 10000;

-- Overlap and Covering Constraints
-- Overlap Constraint
SELECT company_name
FROM Company
WHERE company_name IS NOT NULL AND total_employees IS NOT NULL;

-- Covering Constraint
SELECT company_name
FROM Company
WHERE company_name IS NULL OR total_employees IS NULL;

-- Division Operator
-- Using NOT IN
SELECT c.company_name
FROM Company c
WHERE NOT EXISTS (
    SELECT s.price_id
    FROM Stock_Price s
    WHERE s.price_date BETWEEN '2023-11-01' AND '2023-12-31'
    AND s.company_id = c.company_id
);

-- Using NOT EXISTS
SELECT c.company_name
FROM Company c
WHERE NOT EXISTS (
    SELECT 1
    FROM Stock_Price s
    WHERE s.price_date BETWEEN '2024-11-01' AND '2024-12-31'
    AND NOT EXISTS (
        SELECT 1
        FROM Stock_Price sp
        WHERE sp.price_date = s.price_date AND sp.company_id = c.company_id
    )
);