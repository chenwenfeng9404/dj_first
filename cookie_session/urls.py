from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'cs/$',views.cookie_session),
    url(r'reg/$',views.register),
    url(r'register/$',views.RegisterView.as_view()),
    url(r'bookview/$',views.BooksView.as_view()),
    url(r'index/$',views.index),
]