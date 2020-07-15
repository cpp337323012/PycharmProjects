from django.contrib.auth.models import User
from sign.models import Guest, Event
from django.test import TestCase

# Create your tests here.

class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000, address='shenzhen',
                             start_time='2016-08-31 02:18:22'
        )
        Guest.objects.create(id=1, event_id=1, realname='alen', phone='137110011001', email='alen@mail.com',
                             sign=False

        )
    def test_event_models(self):
        result = Event.objects.get(name="oneplus 3 event")
        self.assertEqual(result.address, "shenzhen")
        self.assertEqual(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='13711011001')
        self.assertEqual(result.realname, 'alen')
        self.assertEqual(result.sing)




'''
python3 manage.py test sign 运行sign应用下的所有测试用例
python3 manage.py test sign.tests.py 运行sign应用下的tests.py测试文件
python3 manage.py test sign.tests.py.ModelTest 运行sign应用下tests.py的ModelTest测试类
python3 manage.py test sign.test.py.ModelTest.test_event_models 运行ModelTest测试类下的test_event_models方法
python3 manage.py test -p test*.py 使用-p匹配测试文件
'''


'''
客户端测试
'''
class IndexPageTest(TestCase):
    def test_index_page_renders_index_template(self):
        '''
        测试Index试图
        :return:
        '''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html') # 断言服务器是否用给定的index.html模板

class LoginActionTest(TestCase):
    '''
    测试登录操作
    '''
    def setUp(self):
        User.objects.create('admin', 'admin@mail.com', 'admin123456')

    def test_add_admin(self):
        '''
        测试添加用户
        :return:
        '''
        user = User.objects.get(username='admin')
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.mail, 'admin@mail.com')

    def test_login_action_username_password_null(self):
        '''
        用户名密码为空
        :return:
        '''
        test_data = {'username':'', 'password':''}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_username_password_error(self):
        '''
        用户名密码错误
        :return:
        '''
        test_data = {'username':'abc', 'password':'123'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_login(self):
        '''
        登录成功
        :return:
        '''
        test_data = {'username':'admin', 'password':'admin123456'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)

    '''
    测试发布会管理
    '''
class EventManageTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123')
        Event.objects.create(name='xiaomi5', limit=2000, address='beijing', status=1, start_time='2019-01-01 12:30:00')
        self.login_user = {'username':'admin', 'password':'admin123'}

    def test_event_manage_success(self):
        '''
        测试发布会
        :return:
        '''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)

    def test_evnet_manage_search_success(self):
        '''
        测试发布会搜索
        :return:
        '''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/search_name/', {'name': 'xiaomi5'})

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaomi5', response.content)
        self.assertIn(b'beijing', response.content)
    '''
    由于发布会管理event_manage和发布会名称搜索search_name两个视图被@login_required修饰，必须先登录，并构造用户请求数据
    
    '''

    '''
    测试嘉宾管理
    '''

class GuestManageTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123')
        Event.objects.create(id=1, name='xiaomi5', limit=2000, address='beijing',
                             status=1, start_time='2019-01-01 21:20:00')
        Guest.objects.create(realname='alen', phone=1810000000, email='alen@mail.com',
                             sign=0, event_id=1)
        self.login_user = {'username':'admin', 'password':'admin123'}

    def test_evnet_manage_success(self):
        '''测试嘉宾信息：alen'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'alen', response.content)
        self.assertIn(b'181000000', response.content)

    '''
    测试用户签到
    '''
class SignIndexActionTest(TestCase):
    '''
    发布会签到
    '''
    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123')
        Event.objects.create(id=1, name='xiaomi5', limit=2000, address='beijing',
                             status=1, start_time='2019-01-01 12:20:10')
        Event.objects.create(id=2, name='oneplus3', limit=2000, address='shenzhen',
                             status=1, start_time='2019-01-02 12:20:10')
        Guest.objects.create(realname='alen', phone=181200000, email='alen@mail.com',
                             sign=0, event_id=1)
        Guest.objects.create(realname='una', phone=1812202000, email='una@mail.com',
                             sign=0, event_id=2)

        self.login_user = {'username':'amdin', 'password':'admin123'}

    def test_sign_index_action_phone_null(self):
        '''手机号为空'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/1/', {'phone':''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'phone error.', response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        '''
        发布会id错误或手机号码错误
        :return:
        '''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('sign_index_action/2/', {'phone':'182000000'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'event id or phone error!', response.content)

    def test_sign_index_action_user_sign_has(self):
        '''
        用户已签到
        :return:
        '''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.clinet.post('/sign_index_action/2/', {'phone':'182000000'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'user has sign in ', response.content)

    def test_sign_index_action_sign_success(self):
        '''签到成功'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/1/', {'phone':'182000000'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sign in successful!', response.content)

        '''
        关于签到功能，测试验证的情况比较多，在setUp()中构造测试数据时需要创建两条发布会信息，嘉宾alen属于发布会'xiaomi5'，
        嘉宾una属于发布会'oneplus4',并且'una'状态为已签到。
        当通过'alen'手机号在'oneplus4'发布会页面签到时，页面将会提示'event id or phone error'。
        当通过'una'手机号签到时，将会提示'user has sign in '（用户已签到）
        另外两个是手机号为空和签到成功
        '''