# Generated by Django 3.1.5 on 2021-03-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='special',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
