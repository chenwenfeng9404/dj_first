from django.conf.urls import url
from . import views

#urlpatterns是被django 自动识别的路由列表变量
urlpatterns = [
    #每个路由信息都需要使用url 函数来构造
    url(r'^show_books/$',views.show_books)
    # 第一个参数是路由地址 是最后的那一部分，
    # 后面指向的是同目录下views文件里的show_books函数

]