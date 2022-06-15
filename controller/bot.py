from telethon.client import chats
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import (GetHistoryRequest)
from dotenv import load_dotenv
import datetime
import json
import os

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
telegram_id = os.getenv('TELE_ID')
phone_number = os.getenv('PHONE_NUMBER')

client = TelegramClient(telegram_id,
                        api_id,
                        api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

# channel_username='GoldenSignalChannel' # your channel
# channel_entity=client.get_entity(channel_username)

listOfMessages = []
table = dict.fromkeys(
    ['channelName', 'message_id', 'message', 'date', 'from_id', 'forward_from', 'forwards', 'edit_date', 'edit_hide',
     'is_reply', 'NumReplies', 'reply_to_message_id'])


def readingFromChannel(chat, numberOfMessages, priorDays, lastDateRead):
    chat = chat[1:]
    channel_entity = client.get_entity(chat)
    posts = client(GetHistoryRequest(
        peer=channel_entity,
        limit=numberOfMessages,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))
    dateLimit = datetime.datetime.now(posts.messages[0].date.tzinfo) - datetime.timedelta(days=priorDays)
    for message in posts.messages:

        if message.date > dateLimit and message.date > lastDateRead:
            table['channelName'] = chat
            table['message_id'] = message.id
            if message.raw_text == None:
                continue
            table['message'] = message.raw_text.replace("\n", " ")
            table['date'] = message.date.strftime("%Y/%m/%d,%H:%M:%S")
            table['from_id'] = message.from_id
            if message.fwd_from != None:
                table['forward_from'] = message.fwd_from.from_name
            else:
                table['forward_from'] = None

            if message.forwards != None:
                table['forwards'] = message.forwards
            else:
                table['forwards'] = None

            if message.edit_date != None:
                table['edit_date'] = message.edit_date.strftime("%Y/%m/%d,%H:%M:%S")
                table['edit_hide'] = message.edit_hide
            else:
                table['edit_date'] = None
                table['edit_hide'] = None

            if message.is_reply != None:
                table['is_reply'] = message.is_reply
                table['reply_to_message_id'] = message.reply_to_msg_id
            else:
                table['is_reply'] = None
                table['reply_to_message_id'] = None

            if message.replies != None:
                table['NumReplies'] = message.replies
            else:
                table['NumReplies'] = 0

            listOfMessages.append(json.dumps(table, ensure_ascii=False))

    return listOfMessages
