# Generated by Django 3.1.5 on 2021-02-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('quantity', models.DecimalField(decimal_places=1, max_digits=3)),
                ('total', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
    ]
