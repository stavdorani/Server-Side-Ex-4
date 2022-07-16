create table users
(
    id       int auto_increment
        primary key,
    name     varchar(255) null,
    email    text         null,
    nic_name varchar(255) null,
    password varchar(255) null
);

INSERT INTO myDb.users (id, name, email, nic_name, password) VALUES (1, 'Omri', 'omri@gmail.com', 'omi', 'om123');
INSERT INTO myDb.users (id, name, email, nic_name, password) VALUES (2, 'Ziv', 'ziv@gmail.com', 'Dido', 'zi123');
INSERT INTO myDb.users (id, name, email, nic_name, password) VALUES (3, 'Ran', 'ran@gmail.com', 'rano', 'ra123');
INSERT INTO myDb.users (id, name, email, nic_name, password) VALUES (4, 'Gal', 'gal@gmail.com', 'galcha', 'ga123');
INSERT INTO myDb.users (id, name, email, nic_name, password) VALUES (5, 'Moshe', 'moshe@gmail.com', 'mushnic', 'mo123');
