from app.models import Category
from django.core import serializers


def delete_all():
    Category.objects.all().delete()


def get_all():
    entries = Category.objects.values()

    return [entries, entries.count()]


def create(category, item):
    c = Category(category=category, item=item)
    c.save()
