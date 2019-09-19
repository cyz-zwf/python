"""mydjangoapp01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from product import views as pv  #引入product 里面的views
from user import views as uv
from car import views as cv

# 路由处理函数, -MTV中的view 接收请求消息,返回响应消息
def doLogin(req):
    print('===服务器接收到一个login请求===')
    res= HttpResponse('这是一个登陆 ')
    return res

# 路由处理韩式, 接收请求消息 返回响应消息
def doregister(req):
    print('===服务器接收到一个regist请求===')
    res = HttpResponse('这是一个注册')
    return res

#路由词典:路由地址不能以 / 开头
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login',doLogin),
    path('register',doregister),
    path('product/list',pv.doProductList),
    path('product/detail/<int:pid>/<laptoptype>',pv.doProductDetail), #路由传参<pid>也可指定类型
    path('product/index',pv.doproductIndex),
]
