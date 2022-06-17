import sqlite3
from dbconn.database import Database

db = Database()


def create(name,
           message_id,
           message,
           date,
           from_id,
           forward_from,
           forward_count,
           edited_date,
           edit_hide,
           is_reply,
           num_replies,
           reply_to_message_id):
    query, params = '''INSERT INTO MESSAGE (CATEGORY, ELEMENT)
                            VALUES(NAME, MESSAGE_ID, MESSAGE_TEXT,
                            DATE, FROM_ID, FORWARD_FROM, FORWARD_COUNT,
                            EDITED_DATE, EDIT_HIDE, IS_REPLY, NUM_REPLY,
                            REPLY_TO_MESSAGE_ID)''', ()

    value = '(\'' + name + '\'' + ', \'' + message_id + '\'' + ', \'' + message + '\'' + ', \'' + date + '\'' + ', \''\
            + from_id + '\'' + ', \'' + forward_from + '\'' + ', \'' + forward_count + '\'' + ', \'' + edited_date + '\'' \
            + ', \'' + edit_hide + '\'' + ', \'' + is_reply + '\'' + ', \'' + num_replies + '\'' + ', \'' + reply_to_message_id + '\')'

    db.cur.execute(query, params)
    db.commit()
