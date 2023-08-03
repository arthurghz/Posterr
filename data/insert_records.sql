CREATE TABLE user (
    id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    joined_date DATETIME NOT NULL
);

CREATE TABLE post (
    id INT PRIMARY KEY AUTO_INCREMENT,
    content TEXT NOT NULL,
    post_date DATETIME NOT NULL,
    user_id INT NOT NULL,
    original_post_id INT,
    quote VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (original_post_id) REFERENCES post (id)
);

INSERT INTO user (id, username, joined_date) VALUES
(1, 'User1', '2023-01-01 10:00:00'),
(2, 'User2', '2023-01-02 11:00:00'),
(3, 'User3', '2023-01-03 12:00:00'),
(4, 'User4', '2023-01-04 13:00:00'),
(5, 'User5', '2023-01-05 14:00:00');

INSERT INTO post (id, content, post_date, user_id, original_post_id, quote) VALUES
(1, 'Hello, this is User1!', '2023-01-01 10:10:00', 1, NULL, NULL),
(2, 'This is my second post, User1.', '2023-01-01 10:20:00', 1, NULL, NULL),
(3, 'Hello, this is User2!', '2023-01-02 11:10:00', 2, NULL, NULL),
(4, 'This is my second post, User2.', '2023-01-02 11:20:00', 2, NULL, NULL),
(5, 'Hello, this is User3!', '2023-01-03 12:10:00', 3, NULL, NULL),
(6, 'This is my second post, User3.', '2023-01-03 12:20:00', 3, NULL, NULL),
(7, 'Hello, this is User4!', '2023-01-04 13:10:00', 4, NULL, NULL),
(8, 'This is my second post, User4.', '2023-01-04 13:20:00', 4, NULL, NULL),
(9, 'Hello, this is User5!', '2023-01-05 14:10:00', 5, NULL, NULL),
(10, 'This is my second post, User5.', '2023-01-05 14:20:00', 5, NULL, NULL);

