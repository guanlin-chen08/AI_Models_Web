# Generated by Django 3.1.7 on 2021-03-09 04:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('historyapp', '0004_himage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='himage',
            name='EmpPhoto',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image/'),
            preserve_default=False,
        ),
    ]
