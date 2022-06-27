from app.models import Category, URL, Message, StockSymbol, Keyword, KeywordValue
from app.model.contentCRUD.messageCRUD import create

PATH = '/Users/Bardia/Documents/aut/courses/CE307_SE1_C3P0/Resources'

# CATEGORIES
CATEGORY_TELEGRAM = 'CATEGORY_TELEGRAM'
CATEGORY_INSTAGRAM = 'CATEGORY_INSTAGRAM'
CATEGORY_TWITTER = 'CATEGORY_TWITTER'
CATEGORY_WHATSAPP = 'CATEGORY_WHATSAPP'
CATEGORY_REDDIT = 'CATEGORY_REDDIT'

# TELEGRAM
TELEGRAM_CHANNEL = 'TELEGRAM_CHANNEL'
TELEGRAM_GROUP = 'TELEGRAM_GROUP'

TELEGRAM_CATEGORY_ITEMS = [
    TELEGRAM_CHANNEL,
    TELEGRAM_GROUP,
]


def add_category():
    for item in TELEGRAM_CATEGORY_ITEMS:
        c = Category(category=CATEGORY_TELEGRAM, item=item)
        c.save()


def add_channels():
    category = Category.objects. \
        filter(category__iexact=CATEGORY_TELEGRAM, item__exact=TELEGRAM_CHANNEL).first()

    f = open(PATH + '/urls.txt', 'r')

    urls = f.read().split('\n')
    for i in urls:
        if 't.me' in i:
            domain = '@' + i[i.rindex('/') + 1:]
            url = URL(category=category, domain=domain)
            url.save()


def add_symbols():
    f = open(PATH + '/fsymbols.csv', 'r')

    table = f.read().split('\n')
    for line in table:
        symbol = line.split(',')
        symbol = [s[1:-1] for s in symbol]
        s = StockSymbol(code=symbol[0], group=symbol[1], industry=symbol[2], table=symbol[3],
                        english_symbol=symbol[4], english_name=symbol[5], symbol=symbol[6], name=symbol[7])
        s.save()


def add_keywords():
    f = open(PATH + '/labels.txt', 'r')

    table = f.read().split('\n')
    for line in table:
        labels = line.split(',')
        value, _type, _key = labels[2], labels[1], labels[0]

        keyword = Keyword(key=_key, type=_type)
        keyword.save()

        val = KeywordValue(keyword=keyword, value=value)
        val.save()


def add_messages():
    f = open(PATH + '/message.csv', 'r')

    table = f.read().split('\n')
    for line in table[1:]:
        fields = line.split(',')
        fields = [None if v == '' else v for v in fields]
        create(_id=fields[1], name=fields[2], text=fields[3], pub_date=fields[4], from_id=fields[5],
               forward_from=fields[6], forward_count=fields[7], edited_date=fields[8], edit_hide=fields[9],
               is_reply=fields[10], reply_count=fields[11], reply_to=fields[12])


# add_category()
# add_channels()
# add_symbols()
# add_keywords()
# add_messages()
