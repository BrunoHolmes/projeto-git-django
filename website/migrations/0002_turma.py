# Generated by Django 2.0.7 on 2020-09-11 00:59

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('periodo', models.CharField(max_length=255)),
            ],
            managers=[
                ('turma', django.db.models.manager.Manager()),
            ],
        ),
    ]
