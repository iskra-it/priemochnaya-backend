# Generated by Django 4.2 on 2023-11-25 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_case_create_date_alter_case_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attrvalue',
            name='attr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attr', to='core.attr'),
        ),
        migrations.AlterField(
            model_name='attrvalue',
            name='case_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case', to='core.case'),
        ),
    ]
