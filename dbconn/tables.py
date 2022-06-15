import sqlite3
from database import Database

db = Database()


def suspicious():
    query, params = '''CREATE TABLE IF NOT EXISTS SUSPICIOUS(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT          NOT NULL,
                            URLS_ID INTEGER                               NOT NULL,
                            CONSTRAINT FK_URLS
                                FOREIGN KEY (URLS_ID)
                                REFERENCES URLS(ID)
                            );''', ()

    db.cur.execute(query, params)
    db.commit()


def validation():
    query, params = '''CREATE TABLE IF NOT EXISTS VALIDATION(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT          NOT NULL,
                        VALUE INTEGER DEFAULT 0                               ,
                        SIGNAL_TYPE_ID INTEGER                                ,
                        CONSTRAINT FK_CATEGORY_ELEMENT
                            FOREIGN KEY (SIGNAL_TYPE_ID)
                            REFERENCES CATEGORY_ELEMENT(ID)
                        );''', ()

    db.cur.execute(query, params)
    db.commit()


def message():
    query, params = '''CREATE TABLE IF NOT EXISTS MESSAGE(
                        NAME TEXT                                     NOT NULL,
                        MESSAGE_ID INTEGER PRIMARY KEY                NOT NULL,
                        MESSAGE_TEXT TEXT                             NOT NULL,
                        DATE DATETIME                                 NOT NULL,
                        FROM_ID INTEGER                                       ,
                        FORWARD_FROM INTEGER                                  ,
                        FORWARDS_COUNT INTEGER                                ,
                        EDITED_DATE DATETIME                                  ,
                        EDIT_HIDE INTEGER                                     ,
                        IS_REPLY INTEGER                                      ,
                        NUM_REPLIES INTEGER                                   ,
                        REPLY_TO_MESSAGE_ID INTEGER                           
                        );''', ()

    db.cur.execute(query, params)
    db.commit()


"""
URL TABLE
STORES URLS AND CATEGORIES
"""


def urls():
    query, params = '''CREATE TABLE IF NOT EXISTS URLS(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT         NOT NULL,
                        URL TEXT                                     NOT NULL,
                        CATEGORY_ID INTEGER                          NOT NULL,
                        CONSTRAINT FK_CATEGORY_ELEMENT
                            FOREIGN KEY (CATEGORY_ID)
                            REFERENCES CATEGORY_ELEMENT(ID)
                        );''', ()

    db.cur.execute(query, params)
    db.commit()


def urls_init():
    f = open('../resources/urls.txt', 'r')

    urls = f.read().split('\n')
    for i in urls:
        query, params = 'INSERT INTO URLS (URL, CATEGORY_ID) VALUES ', ()

        if 't.me' in i:
            values = '(\'' + get_telegram_id(i) + '\', 1)'
            query = query + values

        db.cur.execute(query, params)
        db.commit()


def get_telegram_id(url):
    return '@' + url[url.rindex('/') + 1:]


"""
CATEGORY_ELEMENT TABLE
USAGE: DETERMINE URL CATEGORIES, GROUPS
"""


def category():
    query, params = '''CREATE TABLE IF NOT EXISTS CATEGORY_ELEMENT(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT          NOT NULL,
                        CATEGORY TEXT               NOT NULL,
                        ELEMENT TEXT                   NOT NULL,
                        CREATION_DATE DATETIME      DEFAULT CURRENT_TIMESTAMP,
                        VERSION                     DEFAULT 1
                        );''', ()

    db.cur.execute(query, params)
    db.commit()


def category_default():
    query, params = '''INSERT INTO CATEGORY_ELEMENT (CATEGORY, ELEMENT)
                        VALUES('TELEGRAM', 'CHANNEL')''', ()

    db.cur.execute(query, params)
    db.commit()

    query, params = '''INSERT INTO CATEGORY_ELEMENT (CATEGORY, ELEMENT)
                            VALUES('TELEGRAM', 'GROUP')''', ()

    db.cur.execute(query, params)
    db.commit()


def sqlite():
    query, params = 'SELECT * FROM sqlite_master', ()
    db.cur.execute(query, params)
