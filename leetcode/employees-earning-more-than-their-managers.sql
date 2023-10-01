-- https://leetcode.com/problems/employees-earning-more-than-their-managers
-- Subquery approach
SELECT
    e1.name AS Employee
FROM
    Employee e1
WHERE
    e1.salary > (
        SELECT
            e2.salary
        FROM
            Employee e2
        WHERE
            e2.id = e1.managerId
    );

-- Join approach
SELECT
    e1.name AS Employee
FROM
    Employee e1
    LEFT JOIN Employee e2 ON e1.managerId = e2.id
WHERE
    e1.salary > e2.salary