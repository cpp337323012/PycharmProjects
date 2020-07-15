#encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from sign.models import Event

# Create your views here.
# 测试返回结果为字符串
#
# def test(request):
#     if request.method == 'GET':
#         return render(request, 'test.html', {'msg':'请输入账号密码'})
#     else:
#         u = request.POST.get('user')
#         p = request.POST.get('pwd')
#         if u == 'root' and p =='123123':
#             # 登录成功，重定向新的url
#             return redirect('/test01/')
#         else:
#             # 登录失败
#             return render(request, 'test.html', {'msg':'用户名或密码错误'})
# def test01(request):
#     return HttpResponse('这是一个字符串测试返回结果')
#     #返回字符串
#
# def index(request):
#    return render(request, 'index.html')  # 未使用HttpResponse类，转而使用Django的render(),返回对象html给请求
#
# def login_welcome(request):
#    return render(request, 'fireworks_PG.html')




'''
2019年12月26日22:13:56
发布会管理和发布会名称搜索功能的开发

'''
# 登录动作
def login_action(request):

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123456':
            return HttpResponse('success')
        else:
            return render (request, 'start_index.html', {'error': 'username or password error!'})

# 发布会管理
# def event_manage(request):
#     return render(request, '')