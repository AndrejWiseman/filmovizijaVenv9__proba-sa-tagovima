# Generated by Django 5.1.2 on 2024-10-30 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_category_filmovi'),
    ]

    operations = [
        migrations.AddField(
            model_name='serije',
            name='category',
            field=models.ManyToManyField(related_name='serije', to='home.category'),
        ),
    ]
