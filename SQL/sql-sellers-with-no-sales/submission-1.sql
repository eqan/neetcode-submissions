-- Write your query below

-- Using Pure WHERE and Count
-- SELECT s.seller_name FROM seller as s WHERE 0 = (SELECT COUNT(o.order_id) FROM orders as o WHERE s.seller_id = o.seller_id AND o.sale_date BETWEEN '2020-01-01' AND '2020-12-31') ORDER BY s.seller_name ASC;

-- Using NOT Exists
SELECT s.seller_name FROM seller as s WHERE NOT EXISTS (SELECT 1 FROM orders as o WHERE s.seller_id = o.seller_id AND o.sale_date BETWEEN '2020-01-01' AND '2020-12-31') ORDER BY s.seller_name ASC;