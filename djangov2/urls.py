"""djangov2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import *
from django.contrib import admin
from myApp import views as myapp_views
from product import views as product_views
from chatroom import views as chatroom_views
from django.conf.urls.static import static
import os
from djangov2 import settings

admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('myApp/', myapp_views.getImg),
    url('user/getUserInfo/', myapp_views.getUserInfo),
    url('user/updatePhonenum/', myapp_views.updatephonenum),
    url('user/updatepwd/', myapp_views.updatepwd),
    url('login/', myapp_views.mylogin),
    url('logout/', myapp_views.mylogout),
    url('search/', product_views.searchitem),
    url('product/show/', product_views.getProductlist),
    url('product/showid/', product_views.getProduct),
    url('product/addcomment/', product_views.addcomment),
    url('product/getcomment/', product_views.getitemcommentlist),
    url('product/isstar/', product_views.getStar),
    url('product/getStarList/', product_views.getStarList),
    url('product/toggleStar/', product_views.toggleStar),
    url('product/addShopCar/', product_views.addShopCar),
    url('product/getShopCarList/', product_views.getShopCarList),
    url('product/updateShopCarList/', product_views.updateShopCar),
    url('statics/images/(?P<filename>.*)$', product_views.my_image,name="images"),
    url('wsapp/echo_once', chatroom_views.echo_once),
] + static(settings.STATIC_URL, document_root=settings.STATIC_PATH)

