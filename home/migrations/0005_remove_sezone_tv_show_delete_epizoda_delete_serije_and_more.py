# Generated by Django 5.1.2 on 2024-10-30 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sezone',
            name='tv_show',
        ),
        migrations.DeleteModel(
            name='Epizoda',
        ),
        migrations.DeleteModel(
            name='Serije',
        ),
        migrations.DeleteModel(
            name='Sezone',
        ),
    ]
