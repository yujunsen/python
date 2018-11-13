import requests
import json

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}

data = {
    'first': 'true',
    'pn'    : '1',
    'kd'    : 'python'
}

req = requests.post(url, data = data, headers = headers)

#print(req.content.decode('utf-8'))
print(req.json())
#data = json.loads(req.text)
#print(data)

#
# import json
# data= json.loads('{"ID": "2", "IP":"12.12.12.12", "Port": "3000"}')
# print(data['ID'])
# #输出结果:"2"
# data = json.dumps(data)
# print(data)