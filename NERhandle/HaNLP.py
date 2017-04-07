# -*- coding:utf8 -*-
import requests

args = {
        'api_key': '81L0G674l9lbhwriXAmfwUKhRECplSFCPttvpJ9J',
        'text': '锯齿形螺纹 如图 9 - 5 所示 牙型 为 不等腰梯形 ， 工作面 的 牙侧角 为 3° ， 非工作面 的 牙侧角 为 30°。',
        'pattern': 'dp',
        'format': 'plain'
    }
result = requests.post("http://api.ltp-cloud.com/analysis/", args)
print(result.content.decode('utf-8'))