-- Use the database
USE TestDB;

-- Create the table
CREATE TABLE students (
    id INT PRIMARY KEY,
    name NVARCHAR(100),
    score INT,
    passed BIT,
    class INT
);

-- Insert sample data
INSERT INTO students (id, name, score, passed, class) VALUES
(1, 'Aarav', 92, 1, 10),
(2, 'Diya', 76, 1, 10),
(3, 'Rohan', 65, 0, 9),
(4, 'Meera', 88, 1, 10),
(5, 'Kabir', 54, 0, 9),
(6, 'Ananya', 95, 1, 10),
(7, 'Rahul', 81, 1, 9),
(8, 'Sneha', 73, 1, 9),
(9, 'Arjun', 84, 1, 10),
(10, 'Kavya', 69, 0, 9);