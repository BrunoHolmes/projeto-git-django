# Generated by Django 2.0.7 on 2020-09-24 22:55

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200924_1928'),
    ]

    operations = [
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
