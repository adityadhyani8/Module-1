--This is the data provided

-- Users table
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name TEXT,
    signup_date DATE
);

-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    amount INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Activity table
CREATE TABLE activity (
    user_id INT,
    login_count INT
);

-- Insert sample data
INSERT INTO users (user_id, name, signup_date) VALUES
(1, 'Aarav', '2023-01-10'),
(2, 'Diya', '2023-02-14'),
(3, 'Rohan', '2023-03-01'),
(4, 'Meera', '2023-04-11'),
(5, 'Kabir', '2023-05-06');

INSERT INTO orders (order_id, user_id, amount) VALUES
(101, 1, 500),
(102, 1, 700),
(103, 2, 300),
(104, 4, 900),
(105, 4, 400);

INSERT INTO activity (user_id, login_count) VALUES
(1, 25),
(2, 10),
(3, 5),
(5, 12);

SELECT * FROM users;
SELECT * FROM orders;
SELECT * FROM activity;

--Retrieve each user’s name and order amount using an INNER JOIN between users and orders
SELECT 
    u.user_id,
    u.name,
    o.amount
FROM users u
INNER JOIN orders o
    ON u.user_id = o.user_id;

--user name aur total order amount for each user
SELECT u.name, SUM(o.amount) AS total_order_amount
FROM users u
INNER JOIN orders o
    ON u.user_id = o.user_id
GROUP BY u.name;

-- Retrieve all users and their login counts, including users with no recorded activity
SELECT u.name, a.login_count
FROM users u
LEFT JOIN activity a
    ON u.user_id = a.user_id;

--Retrieve users who have never placed an order
SELECT u.name
FROM users u
LEFT JOIN orders o
    ON u.user_id = o.user_id
WHERE o.order_id IS NULL;

--Combine all three tables
SELECT u.name
FROM users u
LEFT JOIN orders o
    ON u.user_id = o.user_id
WHERE o.order_id IS NULL;

--Retrieve users who placed orders greater than 400
SELECT DISTINCT u.user_id, u.name
FROM users u
INNER JOIN orders o
    ON u.user_id = o.user_id
WHERE o.amount > 400;

--Retrieve the top 3 users by total order amount
SELECT TOP 3 
    u.user_id,
    u.name,
    SUM(o.amount) AS total_order_amount
FROM users u
INNER JOIN orders o
    ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
ORDER BY SUM(o.amount) DESC;

--Retrieve users
SELECT 
    u.user_id,
    u.name,
    ISNULL(SUM(o.amount), 0) AS total_order_amount,
    ISNULL(a.login_count, 0) AS login_count
FROM users u
LEFT JOIN orders o
    ON u.user_id = o.user_id
LEFT JOIN activity a
    ON u.user_id = a.user_id
GROUP BY u.user_id, u.name, a.login_count
ORDER BY total_order_amount DESC, login_count DESC;

--Return the average order amount per user
SELECT 
    u.user_id,
    u.name,
    AVG(o.amount) AS average_order_amount
FROM users u
INNER JOIN orders o
    ON u.user_id = o.user_id
GROUP BY u.user_id, u.name;

--Combined query
SELECT TOP 3
    u.user_id,
    u.name,
    ISNULL(SUM(o.amount), 0) AS total_order_amount,
    ISNULL(a.login_count, 0) AS login_count
FROM users u
LEFT JOIN orders o
    ON u.user_id = o.user_id
LEFT JOIN activity a
    ON u.user_id = a.user_id
GROUP BY u.user_id, u.name, a.login_count
ORDER BY total_order_amount DESC;