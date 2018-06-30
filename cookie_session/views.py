from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator

def cookie_session(request):
    request.session['itcast'] = 'python'
    print(request.session.get('itcast'))
    return HttpResponse('OK')

#不同的请求方式
def register(request):
    if request.method == "GET":
        return HttpResponse('get请求')
    else:
        return HttpResponse('post请求')


        # 装饰器，在功能执行前，先执行装饰器内的业务

def my_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        # 在闭包里面写入业务功能，除了下面三行，其他的都是固定写法
        print("自定义装饰器被调用了")
        print('请求的方法', request.method)
        print('请求路径%s' % request.path)
        return func(self, request, *args, **kwargs)

    return wrapper

# 通过类视图的方式，来自动判别是get还是post请求方式，可读性好，直观
# @method_decorator(my_decorator,name = 'dispatch')
#加在类上面就是全部添加装饰器，可以分别加到下面的方法上，单独使用装饰器
class RegisterView(View):
    # @method_decorator(my_decorator)  #这个写法是上面装饰器闭包内，没有写self时的写法
    @my_decorator      #这个写法是上面def wrapper（）里面 传了self的写法，这样就可以使用自定义的装饰器都可以达到效果
    def get(self,request):
        return HttpResponse('GET请求')
    @my_decorator
    def post(self,request):
        return HttpResponse('post请求')

###############扩展类 (多继承的方式)

class ListModelMixin(object):
    def list(self,request,*args,**kwargs):
        print('list函数')

class CreateModelMixin(object):
    def create(self,request,*args,**kwargs):
        print('create函数')

class BooksView(ListModelMixin,CreateModelMixin,View):
    def get(self,request):
        self.list(request)
        return HttpResponse('OK')

    def post(self,request):
        self.create(request)
        return HttpResponse('OK')



def index(request):
    context = {'itcast':'python'}
    return render(request,'index.html',context)