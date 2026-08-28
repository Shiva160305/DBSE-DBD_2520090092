CREATE DATABASE Joinsandsetoperations_2520090092;
USE Joinsandsetoperations_2520090092;
-- ===================== SETUP =====================
CREATE TABLE class (
    id INT,
    name VARCHAR(30)
);

CREATE TABLE class_info (
    id INT,
    address VARCHAR(30)
);

INSERT INTO class VALUES
(1,'abhi'),
(2,'adam'),
(4,'alex');

INSERT INTO class_info VALUES
(1,'DELHI'),
(2,'MUMBAI'),
(3,'CHENNAI');

-- Q1: CROSS JOIN
SELECT *
FROM class
CROSS JOIN class_info;


-- ===================== INNER JOIN SETUP =====================
CREATE TABLE class (
    id INT,
    name VARCHAR(30)
);

CREATE TABLE class_info (
    id INT,
    address VARCHAR(30)
);

INSERT INTO class VALUES
(1,'abhi'),
(2,'adam'),
(3,'alex'),
(4,'anu');

INSERT INTO class_info VALUES
(1,'DELHI'),
(2,'MUMBAI'),
(3,'CHENNAI');

-- Q2: INNER JOIN
SELECT *
FROM class
INNER JOIN class_info
ON class.id = class_info.id;

-- Q3: INNER JOIN (specific columns)
SELECT class.name,
       class_info.address
FROM class
INNER JOIN class_info
ON class.id = class_info.id;

-- Q4: NATURAL JOIN
SELECT *
FROM class
NATURAL JOIN class_info;


-- ===================== LEFT/RIGHT JOIN SETUP =====================
INSERT INTO class VALUES
(5,'ashish');

INSERT INTO class_info VALUES
(7,'NOIDA'),
(8,'PANIPAT');

-- Q5: LEFT JOIN
SELECT *
FROM class
LEFT OUTER JOIN class_info
ON class.id = class_info.id;

-- Q6: LEFT JOIN - unmatched only
SELECT *
FROM class
LEFT JOIN class_info
ON class.id = class_info.id
WHERE class_info.id IS NULL;

-- Q7: RIGHT JOIN
SELECT *
FROM class
RIGHT OUTER JOIN class_info
ON class.id = class_info.id;

-- Q8: RIGHT JOIN - unmatched only
SELECT *
FROM class
RIGHT JOIN class_info
ON class.id = class_info.id
WHERE class.id IS NULL;

-- Q9: FULL OUTER JOIN
SELECT *
FROM class
FULL OUTER JOIN class_info
ON class.id = class_info.id;

-- Q10: FULL OUTER JOIN - unmatched only
SELECT *
FROM class
FULL OUTER JOIN class_info
ON class.id = class_info.id
WHERE class.id IS NULL
OR class_info.id IS NULL;


-- ===================== UNION SETUP =====================
CREATE TABLE first_table(
id INT,
name VARCHAR(30)
);

CREATE TABLE second_table(
id INT,
name VARCHAR(30)
);

INSERT INTO first_table VALUES
(1,'abhi'),
(2,'adam');

INSERT INTO second_table VALUES
(2,'adam'),
(3,'chester');

-- Q11: UNION
SELECT * FROM first_table
UNION
SELECT * FROM second_table;

-- Q12: UNION (names only)
SELECT name FROM first_table
UNION
SELECT name FROM second_table;

-- Q13: UNION ALL
SELECT * FROM first_table
UNION ALL
SELECT * FROM second_table;

-- Q14: UNION ALL - count
SELECT COUNT(*)
FROM
(
SELECT * FROM first_table
UNION ALL
SELECT * FROM second_table
) A;

-- Q15: INTERSECT
SELECT * FROM first_table
INTERSECT
SELECT * FROM second_table;

-- Q16: INTERSECT (names only)
SELECT name FROM first_table
INTERSECT
SELECT  name FROM second_table;

-- Q17: MINUS
SELECT * FROM first_table
MINUS
SELECT * FROM second_table;

-- Q18: MINUS (names only)
SELECT name FROM first_table
MINUS
SELECT name FROM second_table;


-- ===================== ADVANCED =====================
-- Q19
SELECT c.id, c.name, ci.address
FROM class c
INNER JOIN class_info ci
ON c.id = ci.id;

-- Q20
SELECT c.id,
       c.name,
       CASE
           WHEN ci.address IS NULL
           THEN 'Address Missing'
           ELSE 'Address Available'
       END AS Status
FROM class c
LEFT JOIN class_info ci
ON c.id = ci.id;	