-- https://leetcode.com/problems/duplicate-emails
SELECT
    email AS Email
FROM
    Person p
GROUP BY
    email
HAVING
    COUNT(p.email) > 1;