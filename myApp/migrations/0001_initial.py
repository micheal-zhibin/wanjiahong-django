# Generated by Django 2.0.6 on 2018-06-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bannerlist',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('imgpath', models.CharField(max_length=200)),
            ],
        ),
    ]