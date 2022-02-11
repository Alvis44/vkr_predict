# Generated by Django 3.2.5 on 2022-02-11 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskBoard', '0014_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('NEW', 'Новая'), ('INWORK', 'В работе'), ('PAUSE', 'Отложена'), ('CLOSED', 'Закрыта')], default='NEW', max_length=20, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='TaskWorkingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField(verbose_name='Дата с')),
                ('date_to', models.DateTimeField(blank=True, null=True, verbose_name='Дата по')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskBoard.task', verbose_name='Задача')),
            ],
        ),
    ]
