import requests
import json

url = "http://httpbin.org/get"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}

proxy = {
    'http': '124.231.30.13:9000'
}

resp = requests.get(url,headers=headers,proxies=proxy)
#resp = requests.get(url,headers=headers)
# with open('xx.html','w',encoding='utf-8') as fp:
#     fp.write(resp.text)

origin = json.loads(resp.text)['origin']

print(origin)

#print(resp.text['origin'])

"""
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
  }, 
  "origin": "110.184.37.18", 
  "url": "http://httpbin.org/get"
}
"""