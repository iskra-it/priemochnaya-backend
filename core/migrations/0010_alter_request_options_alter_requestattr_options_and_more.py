# Generated by Django 4.2 on 2023-11-26 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_request_update_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Запрос пользователя', 'verbose_name_plural': 'Запросы пользователя'},
        ),
        migrations.AlterModelOptions(
            name='requestattr',
            options={'verbose_name': 'Атрибут запроса пользователя', 'verbose_name_plural': 'Атрибуты запроса пользователя'},
        ),
        migrations.AlterModelOptions(
            name='requestfile',
            options={'verbose_name': 'Файл запроса пользователя', 'verbose_name_plural': 'Файлы запроса пользователя'},
        ),
        migrations.RemoveField(
            model_name='request',
            name='files',
        ),
    ]
