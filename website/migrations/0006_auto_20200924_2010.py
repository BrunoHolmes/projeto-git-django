# Generated by Django 2.0.7 on 2020-09-24 23:10

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200924_1959'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Funcionarios',
            new_name='Funcionario',
        ),
        migrations.RenameModel(
            old_name='Turmas',
            new_name='Turma',
        ),
        migrations.AlterModelManagers(
            name='funcionario',
            managers=[
                ('funcionario', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='turma',
            managers=[
                ('turma', django.db.models.manager.Manager()),
            ],
        ),
    ]
