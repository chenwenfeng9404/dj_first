from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    # upload_to 保存图片的目录
    # logo = models.ImageField(upload_to='img', verbose_name='封面', null=True)
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'books1'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle

    #自定义显示字段的名字，要添加到显示字段的那段代码里面
    def pub_date(self):
        return self.bpub_date.strftime('%Y年%m月%d日')
    pub_date.short_description = "发布日期"

    pub_date.admin_order_field = 'bpub_date'
