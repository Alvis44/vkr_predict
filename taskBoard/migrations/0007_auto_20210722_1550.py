# Generated by Django 3.2.5 on 2021-07-22 12:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskBoard', '0008_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 22, 15, 50, 17, 14817), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('NEW', 'Новая'), ('INWORK', 'В работе'), ('CLOSED', 'Закрыта')], default='NEW', max_length=20, verbose_name='Статус'),
        ),
    ]