from django.contrib import admin

# Register your models here.

from myApp import models
admin.site.register(models.bannerlist)
admin.site.register(models.auth_profile)
