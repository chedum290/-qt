import sqlite3

with sqlite3.connect('questions.db') as con:
    cur = con.cursor()
    cur.execute("""
        INSERT INTO questions (content, quiz_id) 
        VALUES 
            ('Что такое Python?', 1), 
            ('Как объявить функцию в Python?', 1), 
            ('Какая функция используется...', 1)
    """)
    con.commit()