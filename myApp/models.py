from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class bannerlist(models.Model):
    #如果没有models.AutoField，默认会创建一个id的自增列
    name = models.CharField(max_length=20, verbose_name='广告名字')
    imagepath = models.ImageField(upload_to='images', verbose_name='图片链接', default='')

    class Meta:
        verbose_name = '广告列表'  # 单数形式
        verbose_name_plural = '广告列表'  # 这个是复数形式

class auth_profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name='用户名')
    userimg = models.ImageField(upload_to='images', verbose_name='用户头像')
    phonenum = models.CharField(max_length=20, default='', verbose_name='电话号码')

    class Meta:
        verbose_name = '用户信息'  # 单数形式
        verbose_name_plural = '用户信息'  # 这个是复数形式
