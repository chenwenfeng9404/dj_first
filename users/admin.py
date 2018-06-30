from django.contrib import admin

# Register your models here.

from django.contrib import admin
from users.models import BookInfo
from users.models import HeroInfo

#注册模型类

admin.site.register(BookInfo)
admin.site.register(HeroInfo)