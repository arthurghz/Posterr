CREATE TABLE if not exists `user`(
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `username` varchar(14) NOT NULL,
    `date_joined` DATE not null default(CURRENT_DATE),
    PRIMARY KEY (id),
    UNIQUE (username),
    CHECK (username REGEXP '^[A-Za-z0-9]+$')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE if not exists `post`(
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `repost_from_id` bigint(20), 
    `quote_from_id` bigint(20), 
    `user_id` bigint(20),
    `datetime_creation` TIMESTAMP NOT NULL DEFAULT(CURRENT_TIMESTAMP),
    `text` varchar(777),
    `is_deleted` BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (id),
    FOREIGN KEY (repost_from_id) REFERENCES post(id) ON DELETE SET NULL,
    FOREIGN KEY (quote_from_id) REFERENCES post(id) ON DELETE SET NULL,
    FOREIGN KEY (user_id) REFERENCES user(id),
    INDEX (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `user` (`username`) VALUES ('Arthur');
INSERT INTO `user` (`username`) VALUES ('Ruhtra');
INSERT INTO `user` (`username`) VALUES ('AzraAi');



INSERT INTO `post` (`user_id`, `text`) 
SELECT `id`, 'I am happy to share that i started working on Azra AI' FROM `user` WHERE `username` = 'Arthur';


INSERT INTO `post` (`user_id`, `text`, `repost_from_id`) 
SELECT `id`, 'Take a look at what Arthur is posting', (SELECT `id` FROM `post` WHERE `text` = 'I am happy to share that i started working on Azra AI' AND `username` = 'Arthur' ) 
FROM `user` WHERE `username` = 'Ruhtra';


INSERT INTO `post` (`user_id`, `text`, `quote_from_id`) 
SELECT `id`, 'Welcome !!', (SELECT `id` FROM `post` WHERE `text` = 'I am happy to share that i started working on Azra Ai'  AND `username` = 'Arthur' ) 
FROM `user` WHERE `username` = 'AzraAi';
