CREATE DATABASE practical5_2520090092;
USE practical5_2520090092;
-- -----------------------------------------------------
-- Members table (stores bcrypt password hashes only)
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS members (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    username      VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role          VARCHAR(30)  NOT NULL DEFAULT 'member'
);

-- -----------------------------------------------------
-- Books table (embedding stored as a JSON array of floats)
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS books (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    title          VARCHAR(250)  NOT NULL,
    author         VARCHAR(200)  NOT NULL,
    isbn           VARCHAR(13)   NOT NULL UNIQUE,
    price          DECIMAL(10,2) NOT NULL,
    published_date DATE          NOT NULL,
    description    TEXT,
    embedding      JSON
);

-- -----------------------------------------------------
-- Optional: sample book (embedding left NULL; the API
-- generates embeddings when you add books via POST /books)
-- -----------------------------------------------------
INSERT INTO books (title, author, isbn, price, published_date, description)
VALUES (
    'Python for Beginners',
    'John Smith',
    '9781234567890',
    450.00,
    '2024-06-10',
    'An introduction to Python programming.'
);

-- -----------------------------------------------------
-- Useful queries for checking your data
-- -----------------------------------------------------
SHOW TABLES;
DESCRIBE members;
DESCRIBE books;

SELECT id, username, role FROM members;
SELECT id, title, author, isbn, price, published_date FROM books;

-- Confirm passwords are hashed (should start with $2b$)
SELECT username, LEFT(password_hash, 7) AS hash_prefix FROM members;

-- Books that have an embedding stored
SELECT id, title, JSON_LENGTH(embedding) AS vector_size
FROM books
WHERE embedding IS NOT NULL;

-- Search by title or author
SELECT * FROM books
WHERE title LIKE '%Python%' OR author LIKE '%Smith%';

-- Update a price / delete a book
UPDATE books SET price = 399.00 WHERE isbn = '9781234567890';
DELETE FROM books WHERE isbn = '9781234567890';