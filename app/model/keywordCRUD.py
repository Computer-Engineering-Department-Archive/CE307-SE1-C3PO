from app.models import Keyword, KeywordValue
from django.core import serializers


def delete_all_keywords():
    Keyword.objects.all().delete()


def read_all_keywords():
    entries = Keyword.objects.all()
    response = {'keywords ': serializers.serialize("json", entries)}

    return [response, entries.count()]


def read_all_keywords_query_set():
    return Keyword.objects.all()


def create_keyword(_key, _type):
    keyword = Keyword(key=_key, type=_type)
    keyword.save()


def delete_all_keyword_values():
    KeywordValue.objects.all().delete()


def read_all_keyword_values():
    entries = KeywordValue.objects.all()
    response = {'keyword values ': serializers.serialize("json", entries)}

    return [response, entries.count()]


def read_all_keyword_values_query_set():
    return KeywordValue.objects.all()
