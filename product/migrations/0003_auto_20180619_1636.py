# Generated by Django 2.0.6 on 2018-06-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180619_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='creattime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updatetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
