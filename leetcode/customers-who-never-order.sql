-- https://leetcode.com/problems/customers-who-never-order
SELECT
    name AS Customers
FROM
    Customers c
WHERE
    (
        SELECT
            COUNT(*)
        FROM
            Orders
        WHERE
            customerId = c.id
    ) = 0;