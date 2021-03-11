# Generated by Django 3.1.7 on 2021-03-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bs1', models.IntegerField(null=True)),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('credits', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'history',
            },
        ),
    ]