import datetime
from telethon.tl.functions.messages import (GetHistoryRequest)
from app.model.contentCRUD.messageCRUD import create
from app.model.urlCRUD import read_all
from teleton import connect

message_count = 50
from_date = 30
to_date = 5
messages_list = []
table = dict.fromkeys(
    ['name', '_id', 'message', 'pub_date', 'from_id', 'forward_from', 'forward_count', 'edit_date', 'edit_hide',
     'is_reply', 'reply_count', 'reply_to'])


def read_all_messages():
    client = connect()
    urls = read_all()

    for url in urls:
        read(client, url, from_date, to_date)


def read(client, chat, msg_count, from_date, to_date):
    chat = chat[1:]
    channel_entity = client.get_entity(chat)
    posts = client(GetHistoryRequest(
        peer=channel_entity,
        limit=msg_count,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))

    date_limit = datetime.datetime.now(posts.messages[0].date.tzinfo) - datetime.timedelta(days=to_date)
    for message in posts.messages:

        if message.date > date_limit:
            table['name'] = chat
            table['_id'] = message.id
            if message.raw_text is None:
                continue
            table['message'] = message.raw_text.replace("\n", " ").replace("(", " ").replace(")", " ")
            table['pub_date'] = message.date.strftime("%Y/%m/%d,%H:%M:%S")
            table['from_id'] = message.from_id
            if message.fwd_from is not None:
                table['forward_from'] = message.fwd_from.from_name
            else:
                table['forward_from'] = None

            if message.forwards is not None:
                table['forward_count'] = message.forwards
            else:
                table['forward_count'] = None

            if message.edit_date is not None:
                table['edit_date'] = message.edit_date.strftime("%Y/%m/%d,%H:%M:%S")
                table['edit_hide'] = message.edit_hide
            else:
                table['edit_date'] = None
                table['edit_hide'] = None

            if message.is_reply is not None:
                table['is_reply'] = message.is_reply
                table['reply_to'] = message.reply_to_msg_id
            else:
                table['is_reply'] = None
                table['reply_to'] = None

            if message.replies is not None:
                table['reply_count'] = message.replies
            else:
                table['reply_count'] = 0

        create(table['name'],
               table['_id'],
               table['message'],
               table['pub_date'],
               table['from_id'],
               table['forward_from'],
               table['forward_count'],
               table['edit_date'],
               table['edit_hide'],
               table['is_reply'],
               table['reply_count'],
               table['reply_to'])
