import requests

url = 'http://www.mmjpg.com/data.php?id=1439&page=8999'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36',
    'Referer': 'http://www.mmjpg.com/mm/1439'
}

data = {
    'id': '1439',
    'page': '8999'
}

wb_data = requests.get(url, headers = headers, data = data)
print(wb_data.text)