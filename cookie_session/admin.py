from django.contrib import admin

from . models import BookInfo

# Register your models here.
# admin.site.register(BookInfo)
admin.site.site_title = '传智书城mis'
admin.site.site_header = '传智书城'
admin.site.index_title = '欢迎使用传智书城Mis'

@admin.register(BookInfo)
class BookInfoManager(admin.ModelAdmin):
    #每页展示几个数据
    list_per_page = 2
    #操作选项的显示位置，上下控制
    actions_on_bottom = True
    actions_on_top = False
    #在列表中添加要字段显示,
    list_display = ['id','btitle','pub_date','bpub_date']
    #可以排序，按照时间早晚进行排序,自定仪的不带排序功能，要取models里面设置
    #搜索框
    #  search_fields = [id]
    # fields = ['btitle','bpub_date']
    # fieldsets = (
    #             ('基本',{'fields':['btitle','bpub_date']}),
    #             ('高级',{'fileds':['bread','bcomment'],'classes':('collapse',)})
    #              )
    #根据等级分配不同的管理哦功能
    fieldsets = (
        ('基本', {'fields': ['btitle', 'bpub_date']}),
        ('高级', {
            'fields': ['bread', 'bcomment'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )