from app.models import Keyword, KeywordValue
from django.core import serializers


def delete_all_keywords():
    Keyword.objects.all().delete()


def get_all_keywords():
    entries = Keyword.objects.all()
    response = {'keywords ': serializers.serialize("json", entries)}

    return [response, entries.count()]


def delete_all_keyword_values():
    KeywordValue.objects.all().delete()


def get_all_keyword_values():
    entries = KeywordValue.objects.all()
    response = {'keyword values ': serializers.serialize("json", entries)}

    return [response, entries.count()]
