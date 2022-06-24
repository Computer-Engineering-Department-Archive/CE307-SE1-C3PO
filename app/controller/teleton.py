from telethon.sync import TelegramClient

api_id = '14744394'
api_hash = '886c291a4bc69b5bacd66310cc26c782'
phone_number = '+989387754805'
telegram_id = 'Kamyarhsn'

client = TelegramClient(telegram_id,
                        api_id,
                        api_hash)


def connect():
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Enter code: '))

    return client
