# Generated by Django 3.2.9 on 2022-02-22 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20220222_2214'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Works',
            new_name='Work',
        ),
    ]