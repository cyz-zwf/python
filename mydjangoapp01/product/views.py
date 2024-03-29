# from django.shortcuts import render
from django.http import HttpResponse
import json   #引入json模块
from django.http import JsonResponse  #导入json  比较简单的方法

# Create your views here.

# 路由处理函数 处理商品列表页  称为MTV中的V 
def doProductList(req):   #?kw=dell&pno=3
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
#
def doProductDetail(req,pid,laptoptype):   #http://.../product/detail/23/thin
    print(pid,type(pid))
    print(laptoptype,type(laptoptype))
    res = HttpResponse('商品详情<hr>')
    return res

''' 
demo1
#路由处理函数 处理商品首页  
def doproductIndex(req):
    data = [
        {'pid':101,'title':'笔记本','price':5000},
        {'pid':102,'title':'笔记本2','price':6000},
        {'pid':103,'title':'笔记本3','price':7000}
    ]
    # 把python对象系列化为json字符串 先导入json
    data = json.dumps(data)
    # 构建响应消息,其主体是json字符串
    res = HttpResponse(data)
    #修改响应消息头部
    res['Content-Type'] = 'application/json'
    res['Access-Control-Allow-Origin'] = '*'
    return res
'''

#demo2  
def doproductIndex(req):
    data = [
        {'pid':101,'title':'笔记本','price':5000},
        {'pid':102,'title':'笔记本2','price':6000},
        {'pid':103,'title':'笔记本3','price':7000}
    ]
    # 构建一个json响应消息 无需手工执行对象序列化,无需设置内容类型为json
    #只要输出的数据不是字典类型(Dict),就必须设置安全吗? safe=False 
    #需要自己手动设置允许来源 即跨域请求
    res = JsonResponse(data,safe=False) #不安全的转换
    res['Access-Control-Allow-Origin'] = '*'
    return res

