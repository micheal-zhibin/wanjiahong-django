# Generated by Django 2.0.6 on 2018-07-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_shopcar'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcar',
            name='updatetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
