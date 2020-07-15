from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from sign.models import Event,Guest
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging


logger = logging.getLogger(__name__)


# 首页（登录）
def index(request):
    # return HttpResponse('hello django')
    return render(request, 'index.html')


# 登录动作
def login_action(request):
    # 寻找名为'username'和'password'的POST参数，而且如果参数没有提交，返回一个为空的字符串
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == '' or password == '':
            return render(request, 'index.html',
                          {'error':'username or password null!'})

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user) # 登录验证
            response = HttpResponseRedirect('/event_manage/') # 登录成功跳转发布会管理
            #request.seesion['username'] = username # 将seesion信息写到服务器
            return response

        else:
            return render(request, 'index.html',
                          {'error':'username or password error!'})
    # 防止直接通过浏览器访问/index_action/地址
    return render(request, 'index.html')


# 退出登录
@login_required
def logout(request):
    auth.logour(request) # 退出登录
    response = HttpResponseRedirect('/index/')
    return response


# 发布会管理(登录成功默认页面)
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('username','')
    return render(request, "event_manage.html",{'user':username,'events':event_list})

'''
待优化能容：前端展示布尔类型，未映射中文字段
'''
# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('username', '')
    search_name = request.GET.get('name', '')
    search_name_type = search_name.encode(encoding='utf-8')
    event_list = Event.objects.filter(name_contains=search_name_type)
    return render(request, 'event_manage.html', {'user':username, 'events':event_list})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('username', '')
    guest_list = Guest.objects.all()


    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    '''
    查询出来的所有嘉宾列表guest_list到paginator类中, 划分每页显示2条数据，一般情况下，一页会显示10条
    '''

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果Page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果Page不在范围内，取最后一页面
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'guest_manage.html', {'user':username, 'guests':contacts})

# 嘉宾手机号的查询
@login_required
def search_phone(request):
    username = request.session.get('username', '')
    search_phone = request.GET.get('phone', '')
    search_phone_type = search_phone.encode(encoding='utf-8')
    guest_list = Guest.objects.filter(phone__contains=search_phone_type)


    paginator = Paginator(guest_list, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果Page不在范围内，去最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'guest_manage.html',
                  {'user':username, 'guests':contacts, 'phone':search_phone})


# 签到页面
@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    guest_list = Guest.objects.filter(event_id=event_id)           # 签到人数
    sign_list = Guest.objects.filter(sign="1", event_id=event_id)   # 已签到数
    guest_data = str(len(guest_list))
    sign_data = str(len(sign_list))
    return render(request, 'sign_index.html', {'event': event,
                                               'guest':guest_data,
                                               'sign':sign_data})


# 前端签到页面
def sign_index2(request, event_id):
    event_name = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index2.html',
                  {'eventID': event_id, 'eventName': event_name})


# 签到动作
@login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    guest_list = Guest.objects.filter(event_id=event_id)
    guest_data = str(len(guest_list))
    sign_data = 0 # 统计已签到的发布会
    for guest in guest_list:
        if guest.sign == True:
            sign_data += 1
    phone = request.POST.get('phone', '')
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html',
                      {'event': event, 'hint': 'phone error', 'guest': guest_data, 'sign': sign_data})


    result = Guest.objects.filter(event_id=event_id, phone=phone)
    if not result:
        return render(request, 'sign_index.html',
                  {'event': event, 'hint': 'phone or eventid error', 'guest': guest_data, 'sign': sign_data})

    if result.sign:
        return render(request, 'sign_index.html',
                      {'event': event, 'hint': 'user has sign in.', 'guest': guest_data, 'sign': sign_data})
    else:
        Guest.objects.filter(event_id=event_id, phone=phone).update(sign='1')
        return render(request, 'sign_index.html',
                      {'event': event, 'hint': 'sign in success!', 'user': result, 'guest': guest_data, 'sign': str(int(sign_data)+1)})

'''get（）是从db取一个匹配的结果，返回一个对象，如果记录不存在，报错
filter（）从db取匹配结果，返回一个对象列表，如果记录不存在，返回[]'''
