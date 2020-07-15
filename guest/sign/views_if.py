# encoding:utf-8
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError
# 添加嘉宾接口
from sign.models import Event, Guest
from django.db.utils import IntegrityError
import time


# 添加发布会接口
def add_event(request):
    # 发布会id
    eid = request.POST.get('eid', '')
    # 发布会标题
    name = request.POST.get('name', '')
    # 限制人数
    limit = request.POST.get('limit', '')
    # 状态
    status = request.POST.get('status', '')
    # 地址
    address = request.POST.get('address', '')
    # 发布会时间
    start_time = request.POST.get('start_time', '')

    if eid == '' or name == '' or limit == '' or start_time == '':
        return JsonResponse({'status':10021, 'message':'parameter error'})
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status':10022, 'message':'event id already exists'})
    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status':10023, 'message':'event name already exists'})
    if status == '':
        status = 1
    try:
        Event.objects.create(id=eid, name=name, limit=limit, address=address,
                             status=int(status), start_time=start_time)
    except ValidationError as e:
        error = 'Start_time format error, It must be in YYYY-MM-DD HH：MM：SS format.'
        return JsonResponse({'status':10024, 'message':error})
    return JsonResponse ({'status':200, 'message':'add event success'})
'''
POST请求接收发布会参数：发布会id(eid)、名称（name）、人数(limit)、状态(status)、地址(address)和时间(start_time)
等参数
判断1：eid、name、limit、status、address、start_time等字段不能为空，否则JsonResponse()返回相对应的状态码和提示。JSONResponse（）
    将字典转化为json格式返回客户端；
判断2：id、name是否存在；如果存在则说明添加数据重复，需要返回相应的状态码和提示信息；
判断3：发布会状态字段不是必填项，字段为空时，默认赋值1，即为开启状态；
判断4：将数据插入Event表，如果日期格式错误，则抛出ValidationError异常。插入成功，返回状态码200和'add event success'


'''
# 添加嘉宾接口
def add_guest(request):
    eid =  request.POST.get('eid','')                # 关联发布会id
    realname = request.POST.get('realname','')       # 姓名
    phone = request.POST.get('phone','')             # 手机号
    email = request.POST.get('email','')             # 邮箱

    if eid =='' or realname == '' or phone == '':
        return JsonResponse({'status':10021,'message':'parameter error'})

    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status':10022,'message':'event id null'})

    result = Event.objects.get(id=eid).status
    if not result:
        return JsonResponse({'status':10023,'message':'event status is not available'})

    event_limit = Event.objects.get(id=eid).limit        # 发布会限制人数
    guest_limit = Guest.objects.filter(event_id=eid)     # 发布会已添加的嘉宾数

    if len(guest_limit) >= event_limit:
        return JsonResponse({'status':10024,'message':'event number is full'})

    event_time = Event.objects.get(id=eid).start_time     # 发布会时间
    timeArray = time.strptime(str(event_time), "%Y-%m-%d %H:%M:%S")
    e_time = int(time.mktime(timeArray))

    now_time = str(time.time())          # 当前时间
    ntime = now_time.split(".")[0]
    n_time = int(ntime)

    if n_time >= e_time:
        return JsonResponse({'status':10025,'message':'event has started'})

    try:
        Guest.objects.create(realname=realname,phone=int(phone),email=email,sign=0,event_id=int(eid))
    except IntegrityError:
        return JsonResponse({'status':10026,'message':'the event guest phone number repeat'})

    return JsonResponse({'status':200,'message':'add guest success'})


# 查询发布会接口
def get_event_list(request):
    eid = request.GET.get('eid', '') # 发布会id
    name = request.GET.get('name', '') # 发布会名称

    if eid == '' and name == '':
        return JsonResponse({'status':10021, 'message':'parameter error'})

    if eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'query result is empty'})
        else:
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status':200, 'message':'success', 'data':event})

    if name != '':
        datas = []
        results = Event.objects.filter(name_contains=name)
        if results:
            for r in results:
                event = {}
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status':200, 'message':'success', 'data':datas})
        else:
            return JsonResponse({'status':10022, 'message':'query result is empty'})

'''
通过GET请求发布会id和发布会名称。两个参数为可选项，但不能同时为空，否则返回状态码10021和parameter error错误提示

如果发布会id不为空，则优先使用发布会id查询，所以查询结果只有一条。将查询结果以字典的形式存放到定义的event中，将event作为借口返回字典中data对应的值

发布会名称为模糊查询，查询数据可为多条。首先将查询的每一条数据放到一个event字典中，再把每个event字典放到datas数组中，最后将整个
datas数组作为接口返回字典中data对应值
'''
#
# 发布会名称为模糊查询，查询数据可为多条。首先将查询的每一条数据放到一个event字典中，再把每个event字典放到datas数组中，最后将整个
# datas数组作为接口返回字典中data对应值
# '''
# 嘉宾查询接口
def get_guest_list(request):
    eid = request.GET.get("eid", "")       # 关联发布会id
    phone = request.GET.get("phone", "")   # 嘉宾手机号

    if eid == '':
        return JsonResponse({'status':10021,'message':'eid cannot be empty'})

    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            for r in results:
                guest = {}
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status':200, 'message':'success', 'data':datas})
        else:
            return JsonResponse({'status':10022, 'message':'query result is empty'})

    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone,event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'query result is empty'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status':200, 'message':'success', 'data':guest})

'''
查询嘉宾接口与发布会接口相似
'''

# 嘉宾签到接口
def user_sign(request):
    eid = request.POST.get('eid', '') # 发布会id
    phone = request.POST.get('phone', '') # 嘉宾手机号

    if eid == '' or phone == '':
        return JsonResponse({'status':10221, 'message':'pararmeter error'})

    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status':10022, 'message':'event id null'})

    result = Event.objects.get(id=eid).status
    if not result:
        return JsonResponse({'status':10023, 'message':'event status is not available'})

    event_time = Event.objects.get(id=eid).start_time # 发布会时间
    etime = str(event_time).split('.')[0]
    timeArray = time.strptime(etime, '%Y-%m-%d %H:%M:%S')
    e_time = int(time.mktime(timeArray))

    now_time = str(time.time()) # 当前时间
    ntime = now_time.split('.')[0]
    n_time = int(ntime)

    if n_time > e_time:
        return JsonResponse({'status':10024, 'message':'event has started'})
    result = Guest.objects.filter(phone=phone)
    if not result:
        return JsonResponse({'status':10025, 'message':'user phone null'})

    result = Guest.objects.filter(event_id=eid, phone=phone)
    if not result:
        return JsonResponse({'status':10026, 'message':'user did not participate in the conference'})

    result = Guest.objects.get(event_id=eid, phone=phone).sign
    if result:
        return JsonResponse({'status':10027, 'message':'user has sign in '})
    else:
        Guest.objects.filter(event_id=eid, phone=phone).update(sign='1')
        return JsonResponse({'status':200, 'message':'sign success'})
    '''
    签到接口通过POST接收发布会id和嘉宾手机号
    判断1：发布会id和嘉宾手机号不能都为空
    判断2：通过查询发布会id是否存在，如果不存在则返回相应错误码。在判断发布会状态是否为True，如果不为True。说明未开启发布会
    判断3：当前时间是否大于发布会时间，如果大于说明发布会已开始，不能操作签到
    判断4：嘉宾手机号是否存在，如果不存在返回错误码
    判断5：判断嘉宾手机号和发布会id是否对应关系，如果不是对应关系，则返回相应状态和提示信息
    判断6：判断嘉宾的签到状态
    '''