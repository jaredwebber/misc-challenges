-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier
SELECT
    (
        SELECT
            unique_id
        FROM
            EmployeeUNI
        WHERE
            id = emp.id
    ) AS unique_id,
    name
FROM
    Employees emp