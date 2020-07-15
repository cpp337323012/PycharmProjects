# 导包
import requests

# 给接口地址定义变量名称
url = "http://v.juhe.cn/weather/index"
# para = {"cityname":"北京","key":"221ec2c9d854d2859310ea808cb760fd"}
#
# # 发送请求
# r = requests.get(url,params=para)
# print(r.status_code)
#
# # 获取json数据
# print(r.json())
# res = r.json()
# print(res["reason"])
# print(res["result"])
# print(res["result"]["sk"])
# print(res["result"]["sk"]["temp"])

para = {"cityname":"北京","key":"221ec2c9d854d2859310ea808cb760f"}
r = requests.get(url,params=para)



res = r.json()
print(res)
print(res["error_code"])



