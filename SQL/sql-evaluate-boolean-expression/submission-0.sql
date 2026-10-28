-- Write your query below
SELECT e.left_operand,e.operator, e.right_operand,
    CASE
        WHEN e.operator = '=' AND v1.value = v2.value THEN True
        WHEN e.operator = '>' AND v1.value > v2.value THEN True
        WHEN e.operator = '<' AND v1.value < v2.value THEN True
        ELSE False
    END AS value
FROM variables as v1
JOIN expressions as e
ON v1.name = e.left_operand
JOIN variables as v2
ON v2.name = e.right_operand
        