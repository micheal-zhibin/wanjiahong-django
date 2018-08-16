from django.db import models
from datetime import timedelta,tzinfo
import datetime,time
from django.contrib import admin
from django.contrib.auth import get_user_model

# Create your models here.

class product(models.Model):
    #如果没有models.AutoField，默认会创建一个id的自增列
    id = models.AutoField(primary_key=True, editable=False, verbose_name='id')
    name = models.CharField(max_length=20, verbose_name='名字')
    imgpath = models.ImageField(upload_to='images', verbose_name='图片')
    price = models.CharField(max_length=200, verbose_name='价格')
    desc = models.CharField(max_length=200, verbose_name='描述')
    discount = models.CharField(max_length=200, verbose_name='折扣')
    creattime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updatetime = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    commentamount = models.IntegerField(default=0, verbose_name='评论数')
    salesamount = models.IntegerField(default=0, verbose_name='售出数量')
    producttype = models.CharField(max_length=20, default='', verbose_name='商品类型')
    ext1 = models.CharField(max_length=200, default='', verbose_name='额外字段1')
    ext2 = models.CharField(max_length=200, default='', verbose_name='额外字段2')
    ext3 = models.CharField(max_length=200, default='', verbose_name='额外字段3')

    class Meta:
        verbose_name = '商品信息'  # 单数形式
        verbose_name_plural = '商品信息'  # 这个是复数形式

class producttab(models.Model):
    #如果没有models.AutoField，默认会创建一个id的自增列
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=20, verbose_name='商品名')
    skuid = models.IntegerField(default=0,null=False, verbose_name='商品id')
    tabname = models.CharField(max_length=50, verbose_name='详细信息')

    class Meta:
        verbose_name = '商品颜色信息'  # 单数形式
        verbose_name_plural = '商品颜色信息'  # 这个是复数形式

class comment(models.Model):
    #如果没有models.AutoField，默认会创建一个id的自增列
    id = models.AutoField(primary_key=True, editable=False, verbose_name='评论id')
    stars = models.IntegerField(null=False,default=0, verbose_name='评分')
    skuid = models.IntegerField(null=False,default=0, verbose_name='商品id')
    content = models.TextField(default='', verbose_name='内容')
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL, null=True, verbose_name='评论用户')

    class Meta:
        verbose_name = '商品评论'  # 单数形式
        verbose_name_plural = '商品评论'  # 这个是复数形式

class userstar(models.Model):
    product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

class shopcar(models.Model):
    product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    createtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    addnum = models.IntegerField(default=1)
    ischose = models.IntegerField(default=0)
    tabname = models.CharField(max_length=50, default='')
