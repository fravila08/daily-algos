DROP TABLE IF EXISTS employees;

CREATE TABLE employees(
  id SERIAL PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  joined_date DATE NOT NULL,
  left_date DATE
  CONSTRAINT name_format CHECK (name ~ '^[A-Z][a-z]*\s[A-Z][a-z]*$')
);

\COPY employees FROM './data.csv' DELIMITER ',' CSV HEADER;

SELECT SUM(res) as hidden_code
FROM (
  SELECT ASCII(LEFT(SUBSTRING(name, POSITION(' ' IN name)+1, LENGTH(name)), 1)) as res
  FROM employees
  WHERE left_date is NULL
  ORDER BY joined_date
  LIMIT 5
) as subquery;
