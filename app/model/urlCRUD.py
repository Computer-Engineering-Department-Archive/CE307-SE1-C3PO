from app.models import URL
from django.core import serializers


def delete_all():
    URL.objects.all().delete()


def read_all():
    return URL.objects.values()


def read_all_urls():
    entries = read_all()

    results = []
    for e in entries:
        results.append(e['domain'])

    return results


def read(domain):
    return URL.objects.filter(domain__contains=domain).first()
