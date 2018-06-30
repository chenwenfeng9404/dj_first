from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import BookInfo

from .models import HeroInfo


def show_books(request):
    """
    index的视图
    :param request:
    :return:

    """
    books = BookInfo.objects.all()

    content = {'books':books}
    return render(request,'index.html', context = content)

