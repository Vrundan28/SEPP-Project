# Generated by Django 3.1.5 on 2021-03-29 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20210329_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Username',
            new_name='Uname',
        ),
    ]