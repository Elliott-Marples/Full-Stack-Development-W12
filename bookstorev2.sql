-- bookstorev2.sql (Week 12)
DROP DATABASE IF EXISTS bookstore;
CREATE DATABASE bookstore;
USE bookstore;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year_published INT NULL,
    publisher VARCHAR(255) NULL
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user'
);

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT NOT NULL,
    comment VARCHAR(500) NULL,
    CONSTRAINT fk_reviews_books FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
    CONSTRAINT fk_reviews_users FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO books (title, author, year_published, publisher) VALUES
('FastAPI: Modern Python Web Development', 'Bill Lubanovic', 2023, 'Pragmatic Bookshelf'),
('Designing Web APIs', 'Brenda Jin, Saurabh Sahni, Amir Shevat', 2018, 'O''Reilly Media'),
('Building APIs with Node.js', 'Caio Ribeiro Pereira', 2016, 'Apress');