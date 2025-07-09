import hashlib
import random

def get_salt():
    random_source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    salt = ''
    for i in range(16):
        salt += random.choice(random_source)
    return salt

def get_hashed_password(plain_pw, salt):
    hashed_pw = hashlib.pbkdf2_hmac('sha256', plain_pw.encode(), salt.encode(), 19720).hex()
    return hashed_pw

# データ生成
users_data = []
for i in range(1, 11):
    salt = get_salt()
    hashed_pass = get_hashed_password('a', salt)
    if i == 1:
        users_data.append(("鈴木 一郎", salt, hashed_pass, f"suzuki@mj.com", 0))
    else:
        name = ["佐藤 花子", "高橋 太郎", "田中 美咲", "伊藤 大輔", "渡辺 結衣", "山本 直樹", "小林 由美", "加藤 祐樹", "松本 真由"][i-2]
        mail_prefix = ["sato", "taka", "tana", "ito", "wata", "yama", "koba", "kato", "matsu"][i-2]
        users_data.append((name, salt, hashed_pass, f"{mail_prefix}@mj.com", 1))

# SQL文の生成
sql_values = ",\n".join([f"('{name}', '{salt}', '{hashed_pass}', '{mail}', {auth})" for name, salt, hashed_pass, mail, auth in users_data])
sql = f"INSERT INTO users (name, salt, hashed_pass, mail, auth) VALUES\n{sql_values};"

print(sql)