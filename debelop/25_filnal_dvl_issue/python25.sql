create database python25;

create table books(
    id INT NOT NULL AUTO_INCREMENT,
    title varchar(100) not null,
    genre varchar(100) not null,
    author varchar(100) not null,
    publisher varchar(50) not null,
    isbn char(20) not null,
    primary key (id)
);

create table users(
    name varchar(100) not null,
    salt varchar(300) not null,
    hashed_pass varchar(300) not null,
    mail varchar(300) not null,
    auth char(10) not null,
    primary key (mail)
);

CREATE TABLE rental_return (
    rental_return_number INT NOT NULL AUTO_INCREMENT,
    return_date DATE,
    rental_date DATE,
    mail VARCHAR(100) NOT NULL,
    book_id int NOT NULL,
    PRIMARY KEY (rental_return_number),
    FOREIGN KEY (mail) REFERENCES users(mail),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

insert into books(title, genre, author, publisher, isbn) values('', '', '', '', '');
INSERT INTO books (title, genre, author, publisher, isbn) VALUES 
('吾輩は猫である', '小説', '夏目漱石', '春陽堂', '9784101010014'),
('坊っちゃん', '小説', '夏目漱石', '春陽堂', '9784101010021'),
('こころ', '小説', '夏目漱石', '岩波書店', '9784003101045'),
('雪国', '小説', '川端康成', '新潮社', '9784101050010'),
('羅生門', '短編小説', '芥川龍之介', '春陽堂', '9784101100012'),
('源氏物語', '古典', '紫式部', '河出書房新社', '9784309301010'),
('走れメロス', '短編小説', '太宰治', '新潮社', '9784101001044'),
('蟹工船', '小説', '小林多喜二', '新潮社', '9784101001051'),
('銀河鉄道の夜', '児童文学', '宮沢賢治', '新潮社', '9784101001068'),
('おくのほそ道', '紀行文学', '松尾芭蕉', '岩波書店', '9784003101076'),
('坊っちゃん', '小説', '夏目漱石', '春陽堂', '9784101010021'),
('こころ', '小説', '夏目漱石', '岩波書店', '9784003101045'),
('吾輩は猫である', '小説', '夏目漱石', '春陽堂', '9784101010014'),
('雪国', '小説', '川端康成', '新潮社', '9784101050010'),
('羅生門', '短編小説', '芥川龍之介', '春陽堂', '9784101100012'),
('源氏物語', '古典', '紫式部', '河出書房新社', '9784309301010'),
('走れメロス', '短編小説', '太宰治', '新潮社', '9784101001044'),
('蟹工船', '小説', '小林多喜二', '新潮社', '9784101001051'),
('銀河鉄道の夜', '児童文学', '宮沢賢治', '新潮社', '9784101001068'),
('おくのほそ道', '紀行文学', '松尾芭蕉', '岩波書店', '9784003101076'),
('坊っちゃん', '小説', '夏目漱石', '春陽堂', '9784101010021'),
('こころ', '小説', '夏目漱石', '岩波書店', '9784003101045'),
('吾輩は猫である', '小説', '夏目漱石', '春陽堂', '9784101010014'),
('雪国', '小説', '川端康成', '新潮社', '9784101050010'),
('羅生門', '短編小説', '芥川龍之介', '春陽堂', '9784101100012'),
('源氏物語', '古典', '紫式部', '河出書房新社', '9784309301010'),
('走れメロス', '短編小説', '太宰治', '新潮社', '9784101001044'),
('蟹工船', '小説', '小林多喜二', '新潮社', '9784101001051'),
('銀河鉄道の夜', '児童文学', '宮沢賢治', '新潮社', '9784101001068'),
('おくのほそ道', '紀行文学', '松尾芭蕉', '岩波書店', '9784003101076');


insert into users(name, salt, hashed_pass, mail, auth) values('', '', '', '', '');
-- user_create.py

-- import hashlib
-- import random

-- def get_salt():
--     random_source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
--     salt = ''
--     for i in range(16):
--         salt += random.choice(random_source)
--     return salt

-- def get_hashed_password(plain_pw, salt):
--     hashed_pw = hashlib.pbkdf2_hmac('sha256', plain_pw.encode(), salt.encode(), 19720).hex()
--     return hashed_pw

-- # データ生成
-- users_data = []
-- for i in range(1, 11):
--     salt = get_salt()
--     hashed_pass = get_hashed_password('a', salt)
--     if i == 1:
--         users_data.append(("鈴木 一郎", salt, hashed_pass, f"suzuki@mj.com", 0))
--     else:
--         name = ["佐藤 花子", "高橋 太郎", "田中 美咲", "伊藤 大輔", "渡辺 結衣", "山本 直樹", "小林 由美", "加藤 祐樹", "松本 真由"][i-2]
--         mail_prefix = ["sato", "taka", "tana", "ito", "wata", "yama", "koba", "kato", "matsu"][i-2]
--         users_data.append((name, salt, hashed_pass, f"{mail_prefix}@mj.com", 1))

-- # SQL文の生成
-- sql_values = ",\n".join([f"('{name}', '{salt}', '{hashed_pass}', '{mail}', {auth})" for name, salt, hashed_pass, mail, auth in users_data])
-- sql = f"INSERT INTO users (name, salt, hashed_pass, mail, auth) VALUES\n{sql_values};"

-- print(sql)
-- パスワードは全員　a


insert into rental_return(return_date, rental_date, user_id, book_id) values('', '', '', '');