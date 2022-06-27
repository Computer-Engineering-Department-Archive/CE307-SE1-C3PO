import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CE307_SE1_C3P0.settings')

django.setup()
# This Python file uses the following encoding: utf-8
import re
from app.controller.initializer import *
from app.model.urlCRUD import read_all_urls
from app.model.symbolCRUD import create_content_symbol
from app.model.signalCRUD import create
from app.model.contentCRUD.messageCRUD import read_messages


def word_counter(string):
    return len(re.findall(r'\w+', string))


def data_cleaner(message_info):
    if not message_info['is_signal']:
        message_info['is_buy'] = False
        message_info['is_sell'] = False
    elif message_info['is_buy'] is True and message_info['is_sell'] is True:
        message_info['is_buy'] = False
        message_info['is_sell'] = False


def value_adder(message: str):
    message_info = {'is_signal': False, 'is_buy': False, 'is_sell': False, 'category': []}
    sig_count = 0
    buy_count = 0
    sell_count = 0
    non_signal_count = 0

    try:
        for string in signal_keywords:
            sig_count += message.count(string[0]) * string[1]
        for string in non_signal_keywords:
            non_signal_count += message.count(string[0]) * string[1]
        if ((sig_count - non_signal_count) / (word_counter(message) * 2)) >= 0.4:
            message_info['is_signal'] = True
        for string in buy_keywords:
            buy_count += message.count(string[0]) * string[1]
        if (buy_count / word_counter(message)) >= 0.4:
            message_info['is_buy'] = True
        for string in sell_keywords:
            sell_count += message.count(string[0]) * string[1]
        if (sell_count / word_counter(message)) >= 0.4:
            message_info['is_sell'] = True
    except ZeroDivisionError as e:
        print(e)

    data_cleaner(message_info)
    is_signal, is_buy, is_sell = message_info['is_signal'], message_info['is_buy'], message_info['is_sell']

    return is_signal, is_buy, is_sell


def analyse():
    initializer()

    urls = read_all_urls()
    message_count, from_date, to_date = 50, None, None

    channel_messages = []
    for url in urls:
        channel_messages.append(read_messages(url, message_count, from_date, to_date))

    for message_set in channel_messages:
        for message in message_set:
            is_signal, is_buy, is_sell = value_adder(message['text'])
            create(message['id'], is_signal, is_buy, is_sell)

            symbols = []
            for symbol in symbols:
                create_content_symbol(message['id'], symbol)


analyse()