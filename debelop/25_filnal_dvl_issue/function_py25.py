import random
import hashlib
import MySQLdb
# メール送信用のインポートーーーーーーーーーーー
import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# ーーーーーーーーーーーーーーーーーーーーーーー


# ソルトを作る関数
def get_salt():
    random_source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    salt = ''
    for i in range(16):
        salt += random.choice(random_source)
    return salt

# パスワードをハッシュする関数
def get_hashed_password(plain_pw, salt):
    hashed_pw = hashlib.pbkdf2_hmac('sha256', plain_pw.encode(), salt.encode(), 19720).hex()   
    return hashed_pw

# mysqlと接続する関数
def get_connection():
    connection = MySQLdb.connect(user = 'root',
                                 password='yuzechi02',
                                 host= 'localhost',
                                 database='python25')
    return connection

# ユーザテーブルにユーザーを登録する関数
def insert_user(name, mail, pw, auth):
    salt = get_salt()   # saltを生成
    hashed_pw = get_hashed_password(pw, salt) # PWをハッシュ

    connection = get_connection()
    cursor = connection.cursor()
    sql = 'INSERT INTO users (name, salt, hashed_pass, mail, auth) VALUES(%s, %s, %s, %s, %s)'

    cursor.execute(sql, (name, salt, hashed_pw, mail, auth))
    connection.commit()
    cursor.close()
    connection.close()

# IDでユーザテーブルのデータをとってくる関数
def get_account_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'select * from users where id = %s'
    
    cursor.execute(sql, (id,))
    account = cursor.fetchone()
    cursor.close()
    connection.close()
    return account

# mailでユーザテーブルのデータをとってくる関数
def get_account_by_mail(mail):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'select * from users where mail = %s'
    
    cursor.execute(sql, (mail,))
    account = cursor.fetchone()
    cursor.close()
    connection.close()
    return account

# rental_returnテーブルにデータを挿入する関数
def insert_rental_return(mail, book_id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'insert into rental_return(return_date, rental_date, mail, book_id) values(null, current_date, %s, %s)'
    
    cursor.execute(sql, (mail, book_id))
    connection.commit()
    cursor.close()
    connection.close()
    return

# rental_returnとbooksから本の情報を取ってくる関数
def get_books(mail):
    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT books.id, books.title, books.genre, books.author, books.publisher, books.isbn, CASE WHEN rental_return.book_id IS NOT NULL AND rental_return.return_date IS NULL AND rental_return.mail = %s THEN '借りてる本' WHEN rental_return.book_id IS NOT NULL AND rental_return.return_date IS NULL THEN '不可' else '可能' END AS '貸出状況' FROM books LEFT JOIN rental_return ON books.id = rental_return.book_id GROUP BY books.id, books.title, books.genre, books.author, books.publisher, books.isbn, rental_return.return_date, rental_return.mail, rental_return.book_id order by books.id asc, 貸出状況 asc"
    cursor.execute(sql, (mail,))
    books = cursor.fetchall()

    cursor.close()
    connection.close()
    return books

# rental_returnとbooksから本の情報を取ってくる関数(管理者)
def get_books_adomin():
    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT books.id, books.title, books.genre, books.author, books.publisher, books.isbn, users.name, rental_return.mail, rental_return.rental_date FROM books LEFT JOIN rental_return ON books.id = rental_return.book_id JOIN users ON users.mail = rental_return.mail WHERE rental_return.return_date IS NULL GROUP BY books.id, books.title, books.genre, books.author, books.publisher, books.isbn, rental_return.rental_date, rental_return.mail, rental_return.book_id ORDER BY books.id ASC"
    cursor.execute(sql)
    books = cursor.fetchall()

    cursor.close()
    connection.close()
    return books

# rental_returnとbooksから本の情報を取ってくる関数2(管理者)
def get_books2_adomin():
    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT books.id, books.title, books.genre, books.author, books.publisher, books.isbn, users.name, rental_return.mail, rental_return.rental_date, rental_return.return_date FROM books LEFT JOIN rental_return ON books.id = rental_return.book_id join users on users.mail = rental_return.mail WHERE rental_return.book_id is not null  and rental_return.return_date is not null"
    cursor.execute(sql)
    books = cursor.fetchall()

    cursor.close()
    connection.close()
    return books


# rental_returnとbooksから条件に合った本の情報を取ってくる関数
def get_search_books(search_value, mail):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT books.id, books.title, books.genre, books.author, books.publisher, books.isbn, CASE WHEN rental_return.book_id IS NOT NULL AND rental_return.return_date IS NULL and rental_return.mail = %s THEN '借りてる本' WHEN rental_return.book_id IS NOT NULL AND rental_return.return_date IS NULL THEN '不可' ELSE '可能' END AS '貸出状況' FROM books LEFT JOIN rental_return ON books.id = rental_return.book_id where books.title like %s or books.genre like %s or books.author like %s or books.publisher like %s GROUP BY books.id, books.title, books.genre, books.author, books.publisher, books.isbn, rental_return.return_date, rental_return.mail, rental_return.book_id order by books.id asc, 貸出状況 asc"
    
    cursor.execute(sql, (mail, '%' + search_value + '%', '%' + search_value + '%', '%' + search_value + '%', '%' + search_value + '%',))
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

# rental_returnとbooksからidに合った本の情報を取ってくる関数
def get_book(id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT books.id, books.title, books.genre, books.author, books.publisher, books.isbn, CASE WHEN rental_return.book_id IS NOT NULL AND rental_return.return_date IS NULL THEN '不可' ELSE '可能' END AS '貸出状況' FROM books LEFT JOIN rental_return ON books.id = rental_return.book_id where books.id = %s GROUP BY books.id, books.title, books.genre, books.author, books.publisher, books.isbn, rental_return.return_date, rental_return.mail, rental_return.book_id order by books.id asc, 貸出状況 asc"
    
    cursor.execute(sql, (id,))
    book = cursor.fetchone()
    cursor.close()
    connection.close()
    return book

# rental_returnとbooksから指定されたIDの本のデータを削除
def delete_book(id):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "delete from rental_return where book_id = %s"
    cursor.execute(sql, (id,))
    connection.commit()
    
    sql = "delete from books where id = %s"
    cursor.execute(sql, (id,))
    connection.commit()
    
    cursor.close()
    connection.close()
    return

# booksの一冊の情報を更新
def update_book(old_id, id, title, genre, author, publisher, isbn):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "insert into books(id, title, genre, author, publisher, isbn) values(%s, %s, %s, %s, %s, %s)"   
    cursor.execute(sql, (id, title, genre, author, publisher, isbn))
    connection.commit() 

    sql = "update rental_return set book_id = %s where book_id = %s"   
    cursor.execute(sql, (id, old_id,))
    connection.commit()
    
    sql = "delete from books where id = %s"   
    cursor.execute(sql, (old_id,))
    connection.commit()
    
    cursor.close()
    connection.close()
    return

# booksの一冊の情報を更新
def update_book2(id, title, genre, author, publisher, isbn):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "update books set title = %s, genre = %s, author = %s, publisher = %s, isbn = %s where id = %s"   
    cursor.execute(sql, (title, genre, author, publisher, isbn, id))
    connection.commit() 
    
    cursor.close()
    connection.close()
    return

# booksに本を追加
def insert_book(id, title, genre, author, publisher, isbn):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "insert into books(id, title, genre, author, publisher, isbn) values(%s, %s, %s, %s, %s, %s)"   
    cursor.execute(sql, (id, title, genre, author, publisher, isbn))
    connection.commit() 
    cursor.close()
    connection.close()
    return

# rental_returnとbooksから借りられてる本の情報を取ってくる関数
def get_rental_books(mail):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT books.id, books.title, books.genre, books.author, books.publisher, books.isbn, CASE WHEN rental_return.book_id IS NOT NULL AND rental_return.return_date IS NULL and rental_return.mail = %s THEN '借りてる本' when rental_return.book_id IS NOT NULL AND rental_return.return_date IS NULL THEN '不可' ELSE '可能' END AS '貸出状況', rental_return.rental_date FROM books LEFT JOIN rental_return ON books.id = rental_return.book_id WHERE rental_return.book_id IS NOT NULL AND rental_return.return_date IS NULL AND rental_return.mail = %s"
    
    cursor.execute(sql, (mail, mail,))
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books
    
# rental_returnとbooksから返された本の情報を取ってくる関数
def get_return_books(mail):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT books.id, books.title, books.genre, books.author, books.publisher, books.isbn, rental_return.rental_date, rental_return.return_date FROM books LEFT JOIN rental_return ON books.id = rental_return.book_id WHERE rental_return.book_id is not null and rental_return.mail = %s and rental_return.return_date is not null"
    
    cursor.execute(sql, (mail,))
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

# パスワードを上書きする関数
def reset_pw(mail, input_newPw):
    salt = get_salt()   # saltを生成
    hashed_newpw = get_hashed_password(input_newPw, salt) # PWをハッシュ
    
    connection = get_connection()
    cursor = connection.cursor()
    sql = "update users set salt = %s, hashed_pass = %s where mail = %s"
    
    cursor.execute(sql, (salt, hashed_newpw, mail,))
    connection.commit()
    cursor.close()
    connection.close()
    return     

# 本を返す関数
def return_book(book_id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "update rental_return set return_date = current_date where book_id = %s"
    
    cursor.execute(sql, (book_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return

# usersからメールで名前をとってくる関数
def get_name(mail):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "select name from users where mail = %s"
    
    cursor.execute(sql, (mail,))
    name = cursor.fetchone()
    cursor.close()
    connection.close()
    return name

# usersからメールでメールをとってくる関数
def get_mail(mail):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "select mail from users where mail = %s"
    
    cursor.execute(sql, (mail,))
    name = cursor.fetchone()
    cursor.close()
    connection.close()
    return name

# 名前を上書きする関数
def update_name(name, mail):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "update users set name = %s where mail = %s"
    
    cursor.execute(sql, (name, mail,))
    connection.commit()
    cursor.close()
    connection.close()
    return

# メールを上書きする関数
def update_mail(mail_input, mail):
    connection = get_connection()
    cursor = connection.cursor()
    
    account = get_account_by_mail(mail)
    
    sql = "insert into users(name,salt,hashed_pass,mail,auth) value(1,1,1,%s,1);"
    cursor.execute(sql, (mail_input,))
    connection.commit()
           
    sql = "update rental_return set mail = %s where mail = %s"
    cursor.execute(sql, (mail_input, mail,))
    connection.commit()

    sql = "update users set name = %s, salt = %s, hashed_pass = %s, auth = %s where mail = %s"
    cursor.execute(sql, (account[0], account[1], account[2], account[4] ,mail_input))
    connection.commit()
    
    sql = "delete from users where mail = %s"
    cursor.execute(sql, (mail,))
    connection.commit()

    cursor.close()
    connection.close()
    return

# メールとパスワードの一致を確かめてアカウント情報を返す関数
def login(mail, input_pw):
    account = get_account_by_mail(mail)
    if account is None:
        return None
    
    hashed_db_pw = account[2]
    
    salt = account[1]
    hashed_input_pw = get_hashed_password(input_pw, salt)
    
    if hashed_input_pw == hashed_db_pw:
        return account
    else:
        return None
    
# メール送信関数ーーーーーーーーーーーーーーーーーーーー
def send_mail(to, subject, body):
    ID = 'c.yuze.sys24@morijyobi.ac.jp'
    PASS = os.environ['MAIL_PASS']
    HOST = 'smtp.gmail.com'
    PORT = 587
    
    msg = MIMEMultipart()
    
    msg.attach(MIMEText(body, 'html'))
    
    msg['Subject'] = subject
    msg['From'] = ID
    msg['To'] = to
    
    # ここから送信処理
    server = SMTP(HOST, PORT)
    server.starttls()
    server.login(ID, PASS)
    
    server.send_message(msg)
    server.quit
# ーーーーーーーーーーーーーーーーーーーーーーーーーーー