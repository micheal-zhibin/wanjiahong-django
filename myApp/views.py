from django.shortcuts import render

# Create your views here.

import json,time
from django.http import HttpResponse
from myApp import models
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

def getImg(request):
    fulllist = models.bannerlist.objects.all()
    imglist = []
    for x in fulllist:
        imglist.append(x.imagepath.url)
    return HttpResponse(json.dumps({'imglist': imglist}), content_type="application/json")

@csrf_exempt
def mylogin(request):
    if request.method=='GET':
        return HttpResponse(json.dumps({'error': 'wrong method'}), content_type="application/json")
    else:
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = authenticate(username=name,password=pwd)
        if user is not None:
            if user.is_active:
                login(request, user)
                req = HttpResponse(json.dumps({'error': '', 'code':0}), content_type="application/json")
                req.set_signed_cookie(key='username', value=user.username,max_age=3600)
                req.set_signed_cookie(key='userid', value=user.id,max_age=3600)
                return req
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                return HttpResponse(json.dumps({'error': 'wrong account', 'code':100}), content_type="application/json")
        else:
            # Return an 'invalid login' error message.
            return HttpResponse(json.dumps({'error': 'wrong account message', 'code':200}), content_type="application/json")

@csrf_exempt
def mylogout(request):
    logout(request)
    return HttpResponse(json.dumps({'ret': 0,'error': 'logout success'}), content_type="application/json")

def getUserInfo(request):
    if request.user.is_authenticated is False:
        return HttpResponse(json.dumps({'ret': 2, 'userinfo': {}}), content_type="application/json")
    else:
        fulllist = models.auth_profile.objects.filter(user=request.user.id)[0]
        userinfo = {
            'name': fulllist.user.username,
            'userid': fulllist.user.id,
            'email': fulllist.user.email,
            'last_login': time.mktime(fulllist.user.last_login.timetuple()),
            'imgurl': fulllist.userimg.url,
            'phonenum': fulllist.phonenum,
        }
        return HttpResponse(json.dumps({'ret': 0, 'userinfo': userinfo}), content_type="application/json")

@csrf_exempt
def updatephonenum(request):
    if request.user.is_authenticated is False:
        return HttpResponse(json.dumps({'ret': 2, 'userinfo': {}}), content_type="application/json")
    else:
        print(request.POST)
        phonenum = request.POST.get('phonenum')
        fulllist = models.auth_profile.objects.filter(user=request.user.id).update(phonenum=phonenum)
        return HttpResponse(json.dumps({'ret': 0}), content_type="application/json")

@csrf_exempt
def updatepwd(request):
    if request.user.is_authenticated is False:
        return HttpResponse(json.dumps({'ret': 2, 'userinfo': {}}), content_type="application/json")
    else:
        oldpwd = request.POST.get('oldpwd')
        newpwd = request.POST.get('newpwd')
        fulllist = get_user_model().objects.filter(id=request.user.id)
        if fulllist[0].check_password(oldpwd):
            get_user_model().objects.filter(id=request.user.id).update(password=make_password(newpwd))
            return HttpResponse(json.dumps({'ret': 0}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'ret': 4, 'errmsg': 'wrong password'}), content_type="application/json")

