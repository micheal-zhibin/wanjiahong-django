# Generated by Django 2.0.6 on 2018-06-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_producttab'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='producttype',
            field=models.CharField(default='', max_length=20),
        ),
    ]
