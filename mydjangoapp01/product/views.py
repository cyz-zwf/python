# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 路由处理函数  称为MTV中的V
def doProductList(req):
    res = HttpResponse('这是商品列表<hr>')
    return res

def doProductDetail(req):
    res = HttpResponse('商品详情<hr>')
    return res

