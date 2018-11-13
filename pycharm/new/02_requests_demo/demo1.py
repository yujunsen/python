import requests

# req = requests.get('https://www.baidu.com')
#
# print(req.text) #text uncode编码
# print(req.content.decode('utf-8')) #content 未编码

params = {
    'wd':'中国'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
}


req = requests.get('https://www.baidu.com/s', params = params, headers = headers)

with open(r'down/02_demo1.html', 'w', encoding='utf-8') as fp:
    fp.write(req.content.decode('utf-8'))
print(req.url)