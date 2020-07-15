# 通过python标准库，wsgiref模块开发web框架
# encoding:utf-8
from wsgiref.simple_server import make_server

def index():
    return 'index'

def login():
    return 'login'

def routes():

    urlpatterns = {('/index/', index),
                   ('/login/', login)}
    return urlpatterns

def RunServer(environ, start_response):
    start_response('200 Ok', [('Conten-Type', 'text/html')])
    url = environ['PATH_INFO']
    urlpatterns = routes()
    func = None
    for item in urlpatterns:
        if item[0] == url:
            func = item[1]
            break
    if func:
        return func()
    else:
        return '404 not found'


if __name__ == '__main__':
    httpd = make_server('', 8080, RunServer)
    print('Serving Http on port 8080...')
    httpd.serve_forever()