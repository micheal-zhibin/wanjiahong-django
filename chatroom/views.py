from dwebsocket.decorators import accept_websocket,require_websocket
from django.http import HttpResponse
import json
from myApp import models
from collections import defaultdict

# 保存所有接入的用户地址
allconn = defaultdict(list)
@require_websocket
def echo_once(request):
    allresult = {}
    # 获取用户信息
    userinfo = request.user
    allresult['userinfo'] = userinfo
    # 声明全局变量
    global allconn
    if not request.is_websocket():  # 判断是不是websocket连接
        message = request.GET['message']
        return HttpResponse(message)
    else:
        # 将链接(请求？)存入全局字典中
        allconn[str(userinfo.id)] = request
        for message in request.websocket:
            msgobj = json.loads(message)
            if msgobj['type'] == 'start':
                msg = {
                    'type': 'info',
                    'content': '加入聊天室成功',
                }
                request.websocket.send(bytes(json.dumps(msg), encoding = "utf8"))  # 发送消息到客户端
                for i in allconn:
                    if i != str(userinfo.id):
                        msg = {
                            'type': 'middle',
                            'content': userinfo.username + '加入聊天室',
                            'imagepath': models.auth_profile.objects.filter(user=userinfo.id)[0].userimg.url,
                        }
                        allconn[i].websocket.send(bytes(json.dumps(msg), encoding = "utf8"))
            elif msgobj['type'] == 'speak':
                for i in allconn:
                    type = 'right'
                    if i != str(userinfo.id):
                        type = 'left'
                    msg = {
                        'type': type,
                        'content': msgobj['content'],
                        'imagepath': models.auth_profile.objects.filter(user=userinfo.id)[0].userimg.url,
                    }
                    allconn[i].websocket.send(bytes(json.dumps(msg), encoding = "utf8"))
            elif msgobj['type'] == 'heartbeat':
                msg = {
                    'type': 'info',
                    'content': '心跳维持成功',
                }
                request.websocket.send(bytes(json.dumps(msg), encoding="utf8"))  # 发送消息到客户端
            else:
                msg = {
                    'type': 'info',
                    'content': '请联系开发',
                }
                request.websocket.send(bytes(json.dumps(msg), encoding="utf8"))  # 发送消息到客户端
