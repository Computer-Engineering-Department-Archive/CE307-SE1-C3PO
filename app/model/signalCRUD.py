from app.models import Signal, Message
from django.core import serializers


def delete_all():
    Signal.objects.all().delete()


def read_all():
    entries = Signal.objects.values

    return [entries, entries.count()]


def create(message_id, is_signal, is_buy, is_sell):
    message = Message.objects.filter(id=message_id).first()

    signal = Signal(content=message,
                    is_signal=is_signal, is_buy=is_buy, is_sell=is_sell)
    signal.save()
