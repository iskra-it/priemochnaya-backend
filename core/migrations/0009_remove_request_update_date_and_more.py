# Generated by Django 4.2 on 2023-11-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_request_requestfile_requestattr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='update_date',
        ),
        migrations.AlterField(
            model_name='request',
            name='additional_contacts',
            field=models.CharField(blank=True, max_length=255, verbose_name='Контакты заявителя'),
        ),
        migrations.AlterField(
            model_name='request',
            name='body',
            field=models.TextField(blank=True, verbose_name='Тело заявки'),
        ),
        migrations.AlterField(
            model_name='request',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='request',
            name='email',
            field=models.CharField(blank=True, max_length=255, verbose_name='Email заявителя'),
        ),
        migrations.AlterField(
            model_name='request',
            name='files',
            field=models.TextField(blank=True, verbose_name='Приложенные файлы'),
        ),
        migrations.AlterField(
            model_name='request',
            name='user_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Имя заявителя'),
        ),
    ]