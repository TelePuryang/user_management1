from django.db import models

# # Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=32)
#     email = models.EmailField()
#     password = models.CharField(max_length=32)
class AppPost(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()



# 1.创建模型类
# 创建用户类
class UserInfo(models.Model):
# 2.定义字段 属性
   UserId = models.AutoField(primary_key=True)
   username = models.CharField(max_length=16, blank=False, verbose_name="用户名")
   password = models.CharField(max_length=16, blank=False, verbose_name="密码")

# 创建图书类
class BooksInfo(models.Model):
   id = models.AutoField(primary_key=True)
   Booksname = models.CharField(max_length=16, verbose_name="书籍名")
   Bookstime = models.CharField(max_length=16, verbose_name="出版日期")

   
