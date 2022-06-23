# Generated by Django 4.0.5 on 2022-06-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_keyword_keywordvalue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keyword',
            options={'ordering': ['key']},
        ),
        migrations.AlterModelOptions(
            name='keywordvalue',
            options={'ordering': ['value']},
        ),
        migrations.AddConstraint(
            model_name='keyword',
            constraint=models.UniqueConstraint(fields=('key', 'type'), name='unique_key_type_combination'),
        ),
    ]
