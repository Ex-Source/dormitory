from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from management import models
from django.views.generic import ListView
# Create your views here.


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写的内容！'
        if username.strip() and password:  # 确保用户名和密码都不为空
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.Student.objects.get(student_id=username)
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html',{'message': message})
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.student_id
                request.session['user_name'] = user.student_name

                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})

    return render(request, 'login/login.html')

def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")

def info(request):
    mistake = request.session.get('user_id')
    mistake_list = models.Mistake.objects.filter(mistake_id=mistake)
    return render(request,'login/info.html',{"mistake_list": mistake_list})

def pay(request):
    return render(request,'login/pay.html')

# class InfoListView(ListView):
#     """通用视图"""
#     models = Mistake    #指定类
#     context_object_name = 'mistake'    #courses被传到模板中
#     template_name = "login/info.html"  #渲染页面

