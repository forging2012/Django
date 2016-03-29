用mysql 首先在settings.py

定义:
(1) DATABASES

(2) INSTALLED_APPS = 


然后使用命令初始化数据库(第一次加载Django的数据库信息）

python manage.py syncdb

再次初始化

python manage.py makemigrations blog       #blog是库名称

python manage.py syncdb    #同步模型中的数据库
 

并先创建好新的数据库.

创建好数据库之后并插入数据库之后发现，admin中没有看到数据库

所以要将你的Models加入到Admin管理中：
from django.db import models：


#将数据库的信息在后台admin显示，
#创建BlogPostAdmin类，继承admin.ModelAdmin父类，以列表的形式显示BlogPost的标题和时间。

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(BlogsPost,BlogPostAdmin)

###############################

