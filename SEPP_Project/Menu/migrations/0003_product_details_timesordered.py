# Generated by Django 3.1.5 on 2021-03-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_product_details_special'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='timesOrdered',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
