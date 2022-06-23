from app.models import URL
from django.core import serializers


def delete_all():
    URL.objects.all().delete()


def get_all():
    entries = URL.objects.all()
    response = {'urls ': serializers.serialize("json", entries)}

    return [response, entries.count()]
