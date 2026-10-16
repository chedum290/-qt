import sqlite3

with sqlite3.connect('answers.db') as con:
    cur = con.cursor()
    cur.execute("""
        INSERT into  answers (question_id, answer, is_right) 
        VALUES 
            (1, "Утюг", 0),
            (1 "Язык программирования", 1),
            (1, "Редактор кода", 0),
            (1, "Редактор кода", 0),
            (1, "Змея", 1),
            (2, "function Name(){}", 1),
            (2, "def func():", 1),
            (3, "print()", 1),
            (3, "read()",  0),
            (3, "input()")
            
            
    con.commit()