# Generated by Django 2.0.6 on 2018-06-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20180619_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]