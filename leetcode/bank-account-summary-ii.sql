-- https://leetcode.com/problems/bank-account-summary-ii/
WITH
    Balances AS (
        SELECT
            account,
            SUM(amount) AS balance
        FROM
            Transactions
        GROUP BY
            account
    )
SELECT
    u.name,
    b.balance
FROM
    Users u
    JOIN Balances b
WHERE
    u.account = b.account
    AND b.balance > 10000;