import requests #导入requests模块
import json     #导入json
#import js2py    #导入js执行模块
#from lxml import etree #xpath使用lxml的etree解析
#请求链接
url = 'https://www.ly.com/flights/api/getflightlist'
#构造请求头 接口中请求头有的参数最好全写上,之后再了解这些请求头信息是干什么的,这里不做介绍
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
#请求参数
data = {
    "Departure": "CTU",
    "Arrival": "SHA",
    "GetType": "1",
    "QueryType": "1",
    "fromairport": "",
    "toairport": "",
    "DepartureDate": "2020-08-06",
    "DepartureName": "成都",
    "ArrivalName": "上海",
    "IsBaby": 0,
    "paging": {
        "cid": "a44fa2b5-44f2-443b-9fd7-b9432826cf1d",
        "dataflag": "some"
    },
    "DepartureFilter": "",
    "ArrivalFilter": "",
    "flat": "465",
    "plat": "465",
    "isFromKylin": 1,
    "refid": ""
}
#发起请求
html = requests.post(url, headers=headers,data=data).text
lis_result = json.loads(html)['FlightInfoSimpleList']

list = []

print(html)