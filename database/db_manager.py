import sqlite3
from config.config import Config


class DatabaseManager:
    def __init__(self):
        """初始化数据库连接和创建表"""
        self.conn = sqlite3.connect(Config.DATABASE_PATH)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """创建必要的数据库表"""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            mood INTEGER NOT NULL,
            health INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        self.conn.commit()

    def save_pet(self, pet):
        """保存新宠物到数据库"""
        self.cursor.execute('''
        INSERT INTO pets (name, mood, health)
        VALUES (?, ?, ?)
        ''', (pet.name, pet.mood, pet.health))
        pet.id = self.cursor.lastrowid
        self.conn.commit()

    def update_pet(self, pet):
        """更新宠物信息"""
        self.cursor.execute('''
        UPDATE pets 
        SET mood = ?, health = ?
        WHERE id = ?
        ''', (pet.mood, pet.health, pet.id))
        self.conn.commit()

    def get_last_pet(self):
        """获取最后创建的宠物"""
        self.cursor.execute('''
        SELECT * FROM pets 
        ORDER BY created_at DESC 
        LIMIT 1
        ''')
        return self.cursor.fetchone()

    def __del__(self):
        """确保关闭数据库连接"""
        if hasattr(self, 'conn'):
            self.conn.close()