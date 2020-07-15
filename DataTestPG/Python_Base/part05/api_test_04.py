'''测试对象需要接受一个user_session
'''

import requests
import re
url2 = "http://192.168.103.106:1080/webtours/nav.pl?in=home"
s = requests.session()
res = s.get(url2)
print(res.text)
usersession = re.findall(r'name=userSession value=(.+?)>', res.text)
print(usersession)
url ="http://192.168.103.106:1080/webtours/login.pl"
para ={'UserSession':usersession[0], "username":"jojo","password":"bean","login.x":"54","login.y":"11","login":"Login","JSFormSubmit":"off"}
r = s.post(url, data=para)
print(r.text)
