from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth.models import User
from app import models
from app.models import AppPost
 
# Create your views here.


def archive(request):
    posts=AppPost.objects.all()
    return render(request,'archive.html',{'posts':posts})
#欢迎界面
def home(request):
    return render(request,"home.html")
def welcome(request):
    return render(request,"welcome.html")

#增加图书信息  
def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method =='POST':
        list = ['id', 'Booksname', 'Bookstime']
        info = []
        for li in list:
            info.append(request.POST.get(li))
        if globals()['LoginId'] != 1:
            return HttpResponse("非root用户,没有权限添加用户！")
        #仿照register判断
        #s = models.BooksInfo.objects.filter(id=info[0])
        s = models.BooksInfo.objects.filter(id=info[0])
       
        if s.count() != 0:
            return render(request, 'add.html', {'err': '图书信息已存在，请勿重复添加'})
        Books = models.BooksInfo()
        Books.id = info[0]
        Books.Booksname = info[1]
        Books.Bookstime = info[2]
        Books.save()  #保存数据
        return render(request, 'add.html', {'success': '图书信息添加成功!!'})
    
#删除图书信息   
def delete(request):
    if request.method == 'GET':
        return render(request, 'delete.html')

    id = request.POST.get('id', None)
    print(id)
    if id.isspace() == True:
        return render(request, 'delete.html', {'err': '不能由空格组成,请重新输入！！！'})
    if len(id) == 0:
        return render(request, 'delete.html', {'err': '不能为空,请重新输入！！！'})
    emp = models.BooksInfo.objects.filter(id=id)
    if emp.count() == 0:
        return render(request, 'delete.html', {'err': '该图书不存在,请重新输入！！！'})
    models.BooksInfo.objects.filter(id=id).delete()
    return render(request, 'delete.html', {'success': '删除成功'})
   
#更新图书信息
def update(request):
    if request.method =='GET':
        return render(request, 'update.html')
    list = ['id', 'Booksname', 'Bookstime']
    info = []
    for li in list:
        info.append(request.POST.get(li))
    if globals()['LoginId'] != 1:
        return render(request, 'update.html', {'err': '权限不够，请切换为 root 用户重试'})
    id = request.POST.get('id', None)
    if id.isspace() == True:
        return render(request, 'update.html', {'err': '不能为空格组成,请重新输入！'})
    s = models.BooksInfo.objects.filter(id=info[0])
    if s.count() == 0:
        return render(request, 'update.html', {'err': '没有此图书信息，无法修改'})
    Books = models.BooksInfo()
    Books.id = info[0]
    Books.Booksname = info[1]
    Books.Bookstime = info[2]
    Books.save()
    return render(request, 'update.html', {'success': '图书信息修改成功！'})

#查询图书信息
def select(request):
    if request.method =='GET':
        return render(request, 'select.html')
    if globals()['LoginId'] != 1:
        return render(request, 'select.html', {'err': '非 root 用户，无法查看！'})
    #从表单中获取id值
    id = request.POST.get('id', None)
    #判断id不能为空的字符串类型
    if id.isspace() == True:
        return render(request, 'select.html', {'err': "不能为空值,请重新输入！"})
    #从数据库根据id值将对应信息赋值给Books
    Books = models.BooksInfo.objects.filter(id=id)
    if Books.count() == 0:
        return render(request, 'select.html', {'err': '没有查询到此图书信息，请确定是否录入系统'})
    info = models.BooksInfo.objects.values('id', 'Booksname', 'Bookstime').filter(id=id)[0]
    print("info=", info)
    return render(request, 'select.html', info)

#查询所有图书信息
def info(request):
    if request.method == 'POST':
        return render(request, 'info.html')
    info = models.BooksInfo.objects.all()
    print(info)
    return render(request, 'info.html', {"info": info})


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")
 
    def post(self, request):
        rname = request.POST.get("rname")
        rpasswd = request.POST.get("rpasswd")
        
 
        # 注册成功跳转到到登录页面，注册加判断已经存在提示改用用户已存在
        users = User.objects.all()
        for i in users:
            if rname == i.username:
                return HttpResponse("用户已存在")
        try:
            models.UserInfo.objects.create(username=rname, password=rpasswd)
        except Exception as e:
            print(e)
            return HttpResponse(rname+rpasswd+"注册失败")
 
        return redirect('/login/') 
        
LoginId = 0
def login(request):
    #判断请求类型
    if request.method =="GET":
        return render(request, "login.html")
    else:
        #从前端表单中获取输入的数据，即账号和密码
        name = request.POST.get("username", None)
        pwd = request.POST.get("password", None)
        #获取数据库中的账号密码数据
        emp = models.UserInfo.objects.values("username", "password", "UserId").filter(username=name)
        #判断根据账号筛选前端输入的数据是否存在于数据库中
        if emp.count() == 0:
            return HttpResponse("登录失败,账号不存在")
        else:
            if emp[0]['password'] == pwd:
                globals()["LoginId"] = emp[0]['UserId']
             
            
                return redirect('所有图书信息')
            
            else:
                return HttpResponse("登录失败,密码错误")        
        
        







