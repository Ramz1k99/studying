import sqlite3
from datetime import datetime

def init_db():
    """Инициализация базы данных"""
    conn = sqlite3.connect('organization.db')
    cursor = conn.cursor()
    
    # Создание таблиц
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS computers (
        id INTEGER PRIMARY KEY,
        purchase_date DATE NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        room_id INTEGER NOT NULL,
        FOREIGN KEY (room_id) REFERENCES rooms(id)
    )
    ''')
    
    # Добавление тестовых данных
    if not cursor.execute("SELECT COUNT(*) FROM rooms").fetchone()[0]:
        cursor.executemany(
            "INSERT INTO rooms VALUES (?, ?)",
            [(1, "Кабинет 101"), (2, "Кабинет 205"), (3, "Серверная"), (4, "Приемная")]
        )
    
    if not cursor.execute("SELECT COUNT(*) FROM computers").fetchone()[0]:
        cursor.executemany(
            "INSERT INTO computers VALUES (?, ?, ?, ?)",
            [
                (1, "2022-01-15", 45000.00, 1),
                (2, "2022-03-20", 52000.50, 1),
                (3, "2021-11-10", 38000.00, 2),
                (4, "2023-02-05", 62000.75, 3),
                (5, "2022-12-18", 41000.25, 4),
                (6, "2023-01-30", 48000.00, 2)
            ]
        )
    
    conn.commit()
    conn.close()

def get_computers_by_room(room_id):
    """Получение компьютеров по ID помещения"""
    conn = sqlite3.connect('organization.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM rooms WHERE id = ?", (room_id,))
    room = cursor.fetchone()
    if not room:
        return None, None
    
    cursor.execute('''
    SELECT c.id, c.purchase_date, c.price, r.name 
    FROM computers c JOIN rooms r ON c.room_id = r.id
    WHERE c.room_id = ?
    ORDER BY c.purchase_date
    ''', (room_id,))
    
    computers = cursor.fetchall()
    conn.close()
    return computers, room[0]