from django.urls import path
from app import views
from django.conf.urls import url
from . import views
 
urlpatterns = [
    
    path('', views.home, name="主页"),
    path('home/',views.home,name="首页"),
    path('register/', views.RegisterView.as_view(),name="注册界面"),
    path("login/", views.login,name="登录界面"),
    path("welcome/",views.welcome,name="欢迎界面"),
    path("add/", views.add,name="添加信息"),
    path("delete/", views.delete,name="删除信息"),
    path("update/", views.update,name="更新信息"),
    path("select/", views.select,name="查询信息"),
    path("info/", views.info,name="所有图书信息"),
    
    
   
]

 
    # path('', views.home, name="主页"),
    # path('home/',views.home,name="首页"),
    # path('register/', views.RegisterView.as_view(),name="注册界面"),
    # path("login/", views.login,name="登录界面"),
    # path("welcome/",views.welcome,name="欢迎界面"),
    # path("add/", views.add,name="添加信息"),
    # path("delete/", views.delete,name="删除信息"),
    # path("update/", views.update,name="更新信息"),
    # path("select/", views.select,name="查询信息"),
    # path("info/", views.info,name="所有图书信息"),
    