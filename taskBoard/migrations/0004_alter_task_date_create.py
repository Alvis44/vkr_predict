# Generated by Django 3.2.5 on 2021-07-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskBoard', '0003_task_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_create',
            field=models.DateTimeField(verbose_name='Дата создания'),
        ),
    ]
