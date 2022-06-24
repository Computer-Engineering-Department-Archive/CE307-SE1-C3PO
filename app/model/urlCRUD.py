from app.models import URL
from django.core import serializers


def delete_all():
    URL.objects.all().delete()


def read_all():
    entries = URL.objects.all()
    response = {'urls ': serializers.serialize("json", entries)}

    return [response, entries.count()]


def read(domain):
    return URL.objects.filter(domain__contains=domain).first()
