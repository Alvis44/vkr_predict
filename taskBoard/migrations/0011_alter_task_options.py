# Generated by Django 3.2.5 on 2021-07-28 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskBoard', '0010_alter_task_date_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('can_add_task', 'Добавление задачи'), ('can_delete_task', 'Удаление задачи'), ('can_edit_tasl', 'Редактирование задачи'))},
        ),
    ]
