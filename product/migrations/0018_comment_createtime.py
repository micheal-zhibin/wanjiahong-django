# Generated by Django 2.0.6 on 2018-07-11 12:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20180711_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='createtime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
