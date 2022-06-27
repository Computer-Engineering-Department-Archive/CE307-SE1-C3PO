from app.models import Keyword, KeywordValue
from django.core import serializers


def delete_all_keywords():
    Keyword.objects.all().delete()


def read_all_keywords_query_set():
    return Keyword.objects.all()


def read_all_keywords():
    entries = read_all_keywords_query_set()

    results = {}
    for e in entries:
        results[e['type']] = e['key']

    return results


def create_keyword(_key, _type):
    keyword = Keyword(key=_key, type=_type)
    keyword.save()


def delete_all_keyword_values():
    KeywordValue.objects.all().delete()


def read_all_keyword_values():
    entries = KeywordValue.objects.values()

    return [entries, entries.count()]


def read_all_keyword_values_query_set():
    return KeywordValue.objects.all()
