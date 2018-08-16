from django.contrib import admin

# Register your models here.

from product import models
admin.site.register(models.product)
admin.site.register(models.producttab)
# admin.site.register(models.productstar)
# admin.site.register(models.comment)