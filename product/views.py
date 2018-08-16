from django.shortcuts import render

# Create your views here.

import json,os,base64
from product import models
from django.http import HttpResponse
import time
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

def getProductlist(request):
    index = int(request.GET.get('index', 0))
    length = int(request.GET.get('length', 10))
    fulllist = models.product.objects.all()[index:index+length]
    productlist = []
    for x in fulllist:
        productlist.append({
            'name': x.name,
            'imagepath': x.imgpath.url,
            'skuid': x.id,
            'desc': x.desc,
            'discount': x.discount,
            'createtime': time.mktime(x.creattime.timetuple()),
            'updatetime': time.mktime(x.updatetime.timetuple()),
            'commentamount': x.commentamount,
            'salesamount': x.salesamount,
            'producttype': x.producttype,
            'price': x.price,
            'ext1': x.ext1,
            'ext2': x.ext2,
            'ext3': x.ext3,
        })
    return HttpResponse(json.dumps({'productlist': productlist}), content_type="application/json")

def getProduct(request):
    skuid = int(request.GET.get('skuid'))
    fulllist = models.producttab.objects.filter(skuid=skuid)
    tablist = []
    for x in fulllist:
        tablist.append({
            'name': x.name,
            'id': x.id,
            'skuid': x.skuid,
            'tabname': x.tabname,
        })
    x = models.product.objects.filter(id=skuid)[0]
    product = {
        'name': x.name,
        'imagepath': x.imgpath.url,
        'skuid': x.id,
        'desc': x.desc,
        'discount': x.discount,
        'createtime': time.mktime(x.creattime.timetuple()),
        'updatetime': time.mktime(x.updatetime.timetuple()),
        'commentamount': x.commentamount,
        'salesamount': x.salesamount,
        'price': x.price,
        'producttype': x.producttype,
        'ext1': x.ext1,
        'ext2': x.ext2,
        'ext3': x.ext3,
        'tablist': tablist
    }

    return HttpResponse(json.dumps({'product': product}), content_type="application/json")

def my_image(request, filename):
    d = os.path.dirname(__file__)
    print(str(d))
    imagepath = os.path.join(d, '../statics/images/'+str(filename))
    print(str(imagepath))
    image_data = open(imagepath, "rb").read()
    return HttpResponse(image_data, content_type='image/jpg')

def getProducttablist(request):
    skuid = int(request.GET.get('skuid'))
    fulllist = models.producttab.objects.filter(skuid=skuid)
    tablist = []
    for x in fulllist:
        tablist.append({
            'name': x.name,
            'id': x.id,
            'skuid': x.skuid,
            'tabname': x.tabname,
        })
    return HttpResponse(json.dumps({'tablist': tablist}), content_type="application/json")

@csrf_exempt
def searchitem(request):
    querymsg = request.GET.get('msg')
    errmsg = ''

    fulllist = models.product.objects.filter(Q(name__contains=querymsg)|Q(desc__contains=querymsg))
    productlist = []
    for x in fulllist:
        productlist.append({
            'name': x.name,
            'imagepath': x.imgpath.url,
            'skuid': x.id,
            'desc': x.desc,
            'discount': x.discount,
            'createtime': time.mktime(x.creattime.timetuple()),
            'updatetime': time.mktime(x.updatetime.timetuple()),
            'commentamount': x.commentamount,
            'salesamount': x.salesamount,
            'producttype': x.producttype,
            'price': x.price,
            'ext1': x.ext1,
            'ext2': x.ext2,
            'ext3': x.ext3,
        })
    return HttpResponse(json.dumps({'productlist': productlist}), content_type="application/json")

@csrf_exempt
def addcomment(request):
    skuid = request.POST.get('skuid')
    stars = request.POST.get('stars')
    content = request.POST.get('content')
    imglist = request.POST.get('imglist')
    # uploadimg(imglist)
    models.comment.objects.create(user=request.user,skuid=skuid,content=content,stars=stars)
    return HttpResponse(json.dumps({'ret': 0, 'error': 'logout success'}), content_type="application/json")

def uploadimg(imgdata):
    imgdata = bytes(imgdata,encoding='utf-8')
    safe_base64_decode(imgdata)
    result = base64.b64decode(imgdata, '-_')
    randomname = 'img' + int(time.time());
    imgtype = '';
    if imgdata[11, 14] is 'jpeg':
        imgtype = 'jpg'
    else:
        imgtype = imgdata[11, 13]
    print('../statics/images/' + randomname + imgtype)
    # file = open('../statics/images/' + randomname + imgtype, 'wb')
    # file.write(str)
    # file.close()
    # return HttpResponse(json.dumps({'error': 'logout success'}), content_type="application/json")

def safe_base64_decode(s):
    if len(s)%4:
        s+=(4-len(s)%4)*b'='
    return base64.b64decode(s)

def getitemcommentlist(request):
    skuid = request.GET.get('skuid')
    fulllist = models.comment.objects.filter(skuid=skuid)
    commentlist = []
    for x in fulllist:
        commentlist.append({
            'skuid': x.skuid,
            'content': x.content,
            'userid': x.user.id,
            'star': x.stars,
            'createtime': time.mktime(x.createtime.timetuple()),
            'username': x.user.username,
            'useremail': x.user.email,
        })
    return HttpResponse(json.dumps({'commentlist': commentlist}), content_type="application/json")

def toggleStar(request):
    skuid = request.GET.get('skuid')
    product = models.product.objects.filter(id=skuid)[0]
    fulllist = models.userstar.objects.filter(product=product.id, user=request.user.id)
    if len(fulllist) > 0:
        fulllist.delete()
        return HttpResponse(json.dumps({'isstar': 0}), content_type="application/json")
    else:
        models.userstar.objects.create(user=request.user, product=product)
        return HttpResponse(json.dumps({'isstar': 1}), content_type="application/json")

def getStar(request):
    skuid = request.GET.get('skuid')
    product = models.product.objects.filter(id=skuid)[0]
    fulllist = models.userstar.objects.filter(product=product.id, user=request.user.id)
    if len(fulllist) > 0:
        return HttpResponse(json.dumps({'isstar': 1}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'isstar': 0}), content_type="application/json")

def getStarList(request):
    fulllist = models.userstar.objects.filter(user=request.user.id)
    starlist = []
    for item in fulllist:
        x = item.product
        starlist.append({
            'name': x.name,
            'imagepath': x.imgpath.url,
            'skuid': x.id,
            'desc': x.desc,
            'discount': x.discount,
            'createtime': time.mktime(x.creattime.timetuple()),
            'updatetime': time.mktime(x.updatetime.timetuple()),
            'commentamount': x.commentamount,
            'salesamount': x.salesamount,
            'producttype': x.producttype,
            'price': x.price,
            'ext1': x.ext1,
            'ext2': x.ext2,
            'ext3': x.ext3,
        })
    return HttpResponse(json.dumps({'starlist': starlist}), content_type="application/json")

def getShopCarList(request):
    fulllist = models.shopcar.objects.filter(user=request.user.id)
    shopcarlist = []
    for item in fulllist:
        x = item.product
        shopcarlist.append({
            'name': x.name,
            'imagepath': x.imgpath.url,
            'skuid': x.id,
            'desc': x.desc,
            'discount': x.discount,
            'addnum': item.addnum,
            'createtime': time.mktime(item.createtime.timetuple()),
            'updatetime': time.mktime(item.updatetime.timetuple()),
            'productcreatetime': time.mktime(x.creattime.timetuple()),
            'productupdatetime': time.mktime(x.updatetime.timetuple()),
            'commentamount': x.commentamount,
            'salesamount': x.salesamount,
            'producttype': x.producttype,
            'price': x.price,
            'ext1': x.ext1,
            'ext2': x.ext2,
            'ext3': x.ext3,
        })
    return HttpResponse(json.dumps({'shopcarlist': shopcarlist}), content_type="application/json")

def addShopCar(request):
    skuid = request.GET.get('skuid')
    fulllist = models.shopcar.objects.filter(product=skuid, user=request.user.id)
    if len(fulllist) > 0:
        fulllist[0].addnum += 1
        fulllist[0].save()
        return HttpResponse(json.dumps({'status': 2}), content_type="application/json")
    else:
        product = models.product.objects.filter(id=skuid)[0]
        models.shopcar.objects.create(user=request.user, product=product)
        return HttpResponse(json.dumps({'status': 1}), content_type="application/json")

def updateShopCar(request):
    skuids = request.GET.get('skuids')
    skuidarr = skuids.split(';')
    print(skuidarr)
    for skuiditem in skuidarr:
        skuid = skuiditem.split(',')[0]
        addnum = int(skuiditem.split(',')[1])
        fulllist = models.shopcar.objects.filter(product=skuid, user=request.user.id)
        if addnum > 0:
            models.shopcar.objects.filter(product=skuid, user=request.user.id).update(addnum=addnum)
        else:
            fulllist[0].delete()
    return HttpResponse(json.dumps({'status': 1}), content_type="application/json")