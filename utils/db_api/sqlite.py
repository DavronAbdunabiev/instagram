
import sqlite3

import requests
from data import config


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('data/class.db',detect_types=sqlite3.PARSE_DECLTYPES |
                                                         sqlite3.PARSE_COLNAMES)
        self.cursor = self.connection.cursor()
    def create_table_users(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id integer,
            username varchar(255),
            first_name text,
            tili varchar(10) NULL,
            soni varchar(10) DEFAULT 0
            )""")

    def add_user(self, telegram_id: int,username: str,first_name: str):
        user = self.select_sevimlilar(telegram_id)
        if user is None:
            self.cursor.execute(f"""INSERT INTO Users(telegram_id,username,first_name) VALUES({telegram_id},"{username}","{first_name}")""")
            self.connection.commit()
            for i in config.ADMINS:
                try:
                    requests.post(f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage?chat_id={int(i)}&text=Botimizda yangi foydalanuvchi:\n\nUsername: @{username}\nID: {telegram_id}")
                except:
                    continue
            return True
        
        
    def count_users(self):
        self.cursor.execute("SELECT COUNT(*) FROM Users")
        return self.cursor.fetchone()
    def all_users(self):
        self.cursor.execute("SELECT telegram_id FROM Users")
    
    def select_sevimlilar(self,telegram_id: int,):
        self.cursor.execute(f"""SELECT * FROM Users  where telegram_id="{telegram_id}" """)
        return self.cursor.fetchone()
    