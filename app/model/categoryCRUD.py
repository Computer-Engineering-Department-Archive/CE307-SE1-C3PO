from app.models import Category
from django.core import serializers


def delete_all():
    Category.objects.all().delete()


def get_all():
    entries = Category.objects.all()
    response = {'categories ': serializers.serialize("json", entries)}

    return [response, entries.count()]


def create(category, item):
    c = Category(category=category, item=item)
    c.save()
