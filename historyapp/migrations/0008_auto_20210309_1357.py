# Generated by Django 3.1.7 on 2021-03-09 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historyapp', '0007_auto_20210309_1234'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Himage',
            new_name='HistoryImage',
        ),
        migrations.AlterModelTable(
            name='historyimage',
            table='Image',
        ),
    ]