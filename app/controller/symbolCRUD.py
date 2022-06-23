from app.models import ContentSymbol, StockSymbol
from django.core import serializers


def delete_all_stock_symbols():
    StockSymbol.objects.all().delete()


def get_all_stock_symbols():
    entries = StockSymbol.objects.all()
    response = {'stock symbols ': serializers.serialize("json", entries)}

    return [response, entries.count()]


def delete_all_content_symbol():
    ContentSymbol.objects.all().delete()


def get_all_content_symbol():
    entries = ContentSymbol.objects.all()
    response = {'content symbols ': serializers.serialize("json", entries)}

    return [response, entries.count()]
