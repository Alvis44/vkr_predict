# Generated by Django 3.2.5 on 2021-07-28 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskBoard', '0013_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': [('can_add_task', 'Добавление задачи'), ('can_delete_task', 'Удаление задачи'), ('can_edit_task', 'Изменение задачи')]},
        ),
    ]
