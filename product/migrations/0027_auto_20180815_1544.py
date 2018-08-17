# Generated by Django 2.0.6 on 2018-08-15 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20180815_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '商品评论', 'verbose_name_plural': '商品评论'},
        ),
        migrations.AlterModelOptions(
            name='producttab',
            options={'verbose_name': '商品颜色信息', 'verbose_name_plural': '商品颜色信息'},
        ),
        migrations.AddField(
            model_name='shopcar',
            name='tabname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='createtime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='评论id'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='skuid',
            field=models.IntegerField(default=0, verbose_name='商品id'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.IntegerField(default=0, verbose_name='评分'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='评论用户'),
        ),
        migrations.AlterField(
            model_name='producttab',
            name='name',
            field=models.CharField(max_length=20, verbose_name='商品名'),
        ),
        migrations.AlterField(
            model_name='producttab',
            name='skuid',
            field=models.IntegerField(default=0, verbose_name='商品id'),
        ),
        migrations.AlterField(
            model_name='producttab',
            name='tabname',
            field=models.CharField(max_length=50, verbose_name='详细信息'),
        ),
    ]