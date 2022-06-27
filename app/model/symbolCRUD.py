from app.models import ContentSymbol, StockSymbol, Message
from django.core import serializers


def delete_all_stock_symbols():
    StockSymbol.objects.all().delete()


def read_all_stock_symbols():
    entries = StockSymbol.objects.values()

    return [entries, entries.count()]


def delete_all_content_symbol():
    ContentSymbol.objects.all().delete()


def read_all_content_symbol():
    entries = ContentSymbol.objects.values()

    return [entries , entries.count()]


def create_content_symbol(message_id, symbol_code):
    message = Message.objects.filter(id=message_id).first()
    stock_symbol = StockSymbol.objects.filter(code=symbol_code).first()

    content_symbol = ContentSymbol(content=message, stock_symbol=stock_symbol)
    content_symbol.save()
