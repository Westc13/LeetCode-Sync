# Write your MySQL query statement below
SELECT p.firstName, p.lastName,
COALESCE(a.city, NULL) AS city,
COALESCE(a.state, NULL) AS state
FROM
Person p
LEFT JOIN
Address a
ON
p.personId = a.personId