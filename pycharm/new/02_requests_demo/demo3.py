import requests

url = 'http://httpbin.org/get'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
}

proxy = {
    'https': '106.56.102.111:8070'
}

req = requests.get(url, headers = headers, proxies = proxy)

print(req.text)