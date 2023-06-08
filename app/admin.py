from django.contrib import admin
from app.models import AppPost

from .models import UserInfo, BooksInfo


# Register your models here.


# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['UserId', 'username', 'password']
 
class BooksInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'Booksname', 'Bookstime']
 
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(BooksInfo, BooksInfoAdmin)