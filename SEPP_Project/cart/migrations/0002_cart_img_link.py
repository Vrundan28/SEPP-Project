# Generated by Django 3.1.5 on 2021-02-27 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='img_link',
            field=models.CharField(default='none', max_length=2083),
            preserve_default=False,
        ),
    ]
