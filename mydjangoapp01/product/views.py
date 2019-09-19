# from django.shortcuts import render
from django.http import HttpResponse
import json   #引入json模块

# Create your views here.

# 路由处理函数  称为MTV中的V
def doProductList(req):
    '''
    print(req.GET)         #<QueryDict: {'kw': ['dell'], 'pno': ['3']}>
    print(type(req.GET))   #<class 'django.http.request.QueryDict'>
    print(req.GET['kw'])   #dell
    print(req.GET['pno'])  #3
    print(req.GET['age'])  #报错
    '''

    kw = req.GET['kw']
    pno = req.GET['pno']

    res = HttpResponse('这是商品列表<hr>查询关键字为 :%s<br> 显示字符串位 %s' %(kw,pno))
    return res

def doProductDetail(req):
    res = HttpResponse('商品详情<hr>')
    return res

