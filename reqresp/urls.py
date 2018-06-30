from django.conf.urls import url
from . import views

urlpatterns = [
    #解析顺序是从上至下的，上面的就可能会吧下面的屏蔽掉，不解析。解决办法是在后面加空间命名
    url(r'^qs/$',views.qs,name = 'qs'),
    url(r'^qs_hello/$',views.qs_hello),
    url(r'^demo/(?P<city>\w+)/(?P<weather>\d+)/$',views.demo_view),
    url(r'get_qs/$',views.get_qs),
    url(r'get_form_data/$',views.get_form_data),
    url(r'get_json_data/$',views.get_json_data),
    url(r'^header/$',views.get_header),
    url(r'^resp/$',views.get_resp),
]