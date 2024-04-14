-- query_number.sql

-- Query number: [Replace with query number]

[Replace with SQL instruction]

-- Створення таблиці "teachers"
CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    subject VARCHAR(100)
);

-- Вставка даних про вчителів
INSERT INTO teachers (first_name, last_name, subject) VALUES 
('Anna Ivanova', 'Mathematics'),
('Петро Петров', 'Physics'),
('Олена Сидорова', 'Biology'),
('Іван Смирнов', 'History'),
('Bohdan Petrovskyi', 'Chemistry');

