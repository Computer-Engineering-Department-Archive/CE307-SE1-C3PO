from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Version(models.Model):
    creation = models.DateTimeField(auto_now_add=True, editable=False)
    version = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True


class Category(Version):
    # Category
    CATEGORY_TELEGRAM = 'telegram'
    CATEGORY_INSTAGRAM = 'instagram'
    CATEGORY_TWITTER = 'twitter'
    CATEGORY_WHATSAPP = 'whatsapp'
    CATEGORY_REDDIT = 'reddit'

    CATEGORY_CH = [
        (CATEGORY_TELEGRAM, 'تلگرام'),
        (CATEGORY_INSTAGRAM, 'اینستاگرام'),
        (CATEGORY_TWITTER, 'تویتتر'),
        (CATEGORY_WHATSAPP, 'واتساپ'),
        (CATEGORY_REDDIT, 'رددیت'),
    ]

    # Telegram Category Items
    TELEGRAM_CHANNEL = 'channel'
    TELEGRAM_GROUP = 'group'

    CATEGORY_ITEM_CH = [
        (TELEGRAM_CHANNEL, 'کانال تلگرامی'),
        (TELEGRAM_GROUP, 'گروه تلگرامی'),
    ]

    category = models.CharField('دسته‌بندی', max_length=256, choices=CATEGORY_CH, null=False)
    item = models.CharField('دسته‌بندی دسته‌بندی‌ها', max_length=256, choices=CATEGORY_ITEM_CH, null=False)

    class Meta:
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['category', 'item'], name='unique_category_item_combination'
            )
        ]


class URL(Version):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_element')
    domain = models.CharField('ادرس وبسایت', max_length=256, null=False)

    class Meta:
        ordering = ['domain']


class StockSymbol(Version):
    code = models.CharField(max_length=256, null=False)
    group = models.CharField(max_length=256, null=False)
    industry = models.CharField(max_length=256, null=False)
    table = models.CharField(max_length=256, null=False)
    english_symbol = models.CharField(max_length=256, null=False)
    english_name = models.CharField(max_length=256, null=False)
    symbol = models.CharField(max_length=256, null=False)
    name = models.CharField(max_length=256, null=False)

    class Meta:
        ordering = ['code']

        constraints = [
            models.UniqueConstraint(
                fields=['code'], name='unique_code_combination'
            )
        ]


class Message(Version):
    id = models.IntegerField('مشخصه', primary_key=True)
    name = models.CharField('اسم کانال/گروه', max_length=256, null=False)
    text = models.CharField('محتوا متنی', max_length=512, null=False)
    pub_date = models.DateTimeField(null=False)
    views = models.IntegerField('تعداد بازدید', null=False, default=0)
    from_id = models.IntegerField('فرستنده مستقیم پیام', null=True)
    forward_from = models.IntegerField('فرستنده غیرمستقیم پیام', null=True)
    forward_count = models.IntegerField('تعداد دفعات ارسال غیرمستقیم پیام', null=True)
    edited_date = models.DateTimeField('تاریخ تغییر محتوای متنی پیام', null=True)
    edit_hide = models.BooleanField('مخفی کردن تغییر پیام', null=True)
    is_reply = models.BooleanField('پیام فرستاده شده پاسخی به پیام‌های دیگر است/نیست', null=True)
    reply_count = models.IntegerField('دفعاتی که به پیام پاسخ داده شده', null=True)
    reply_to = models.IntegerField('مشخصه پیام اصلی پاسخ داده شده', null=True)

    URL = models.ForeignKey(URL, on_delete=models.CASCADE, related_name='URL')

    class Meta:
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['id', 'name', 'edited_date'], name='unique_id_name_edit_combination'
            )
        ]


class ContentSymbol(Version):
    stock_symbol = models.ForeignKey(StockSymbol, on_delete=models.CASCADE, related_name='StockSymbol')

    content = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='MessageContent')


class Signal(Version):
    is_signal = models.BooleanField(null=False)
    is_buy = models.BooleanField(null=False)
    is_sell = models.BooleanField(null=False)

    content = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='MessageSignal')


class Keyword(Version):
    key = models.CharField(max_length=256, null=False)
    type = models.CharField(max_length=256, null=False)

    class Meta:
        ordering = ['key']
        constraints = [
            models.UniqueConstraint(
                fields=['key', 'type'], name='unique_key_type_combination'
            )
        ]


class KeywordValue(Version):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='Keyword')
    value = models.IntegerField(null=False)

    class Meta:
        ordering = ['value']
