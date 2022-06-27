from app.models import Message
from app.model import urlCRUD


def delete_all():
    Message.objects.all().delete()


def get_all():
    entries = Message.objects.values()

    return [entries, entries.count()]


def create(name,
           _id,
           text,
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

    if text is None:
        text = ''
    message = Message(id=_id, name=name, text=text, pub_date=pub_date, from_id=from_id,
                      forward_from=forward_from, forward_count=forward_count, edited_date=edited_date,
                      edit_hide=edit_hide, is_reply=is_reply, reply_count=reply_count, reply_to=reply_to,
                      URL=url)
    message.save()


def read_messages(name, message_count, from_date, to_date):
    entries = Message.objects
    if name is not None:
        entries.filter(name__contains=name[1:])
    if from_date is not None:
        entries.filter(pub_date__gte=from_date)
    if to_date is not None:
        entries.filter(pub_date__lte=to_date)
    entries = entries.values()[:message_count]

    return entries
