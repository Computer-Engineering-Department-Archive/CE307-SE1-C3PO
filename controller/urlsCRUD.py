import sqlite3
from dbconn.database import Database

db = Database()


def get_telegram_channels():
    query, params = '''SELECT URL FROM URLS WHERE CATEGORY_ID = 1''', ()

    db.cur.execute(query, params)
    db.commit()

    return [str(row)[2:-2] for row in db.cur.fetchall()]


def get_telegram_groups():
    query, params = '''SELECT URL FROM URLS WHERE CATEGORY_ID = 2''', ()

    db.cur.execute(query, params)
    db.commit()

    return [str(row)[2:-2] for row in db.cur.fetchall()]
