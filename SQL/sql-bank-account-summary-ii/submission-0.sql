-- Write your query below

SELECT u.name, SUM(t.amount) as balance FROM users as u INNER JOIN transactions as t ON u.account = t.account GROUP BY u.account HAVING SUM(t.amount) > 10000;