from app.models import Message
from app.model import urlCRUD
from django.core import serializers


def delete_all():
    Message.objects.all().delete()


def get_all():
    entries = Message.objects.all()
    response = {'messages ': serializers.serialize("json", entries)}

    return [response, entries.count()]


def create(name,
           _id,
           message,
           pub_date,
           from_id,
           forward_from,
           forward_count,
           edited_date,
           edit_hide,
           is_reply,
           reply_count,
           reply_to):
    url = urlCRUD.read(name)
    message = Message(id=_id, name=name, message=message, pub_date=pub_date, from_id=from_id,
                      forward_from=forward_from, forward_count=forward_count, edited_date=edited_date,
                      edit_hide=edit_hide, is_reply=is_reply, reply_count=reply_count, reply_to=reply_to,
                      URL=url)
    message.save()


def read(name, msg_count, from_date, to_date):
    entries = Message.objects.filter(name__contains=name, pub_date__gte=from_date, pub_date__lte=to_date)[:msg_count]
    response = {'messages ': serializers.serialize("json", entries)}

    return [response, entries.count()]
