from urllib import request, parse
from bs4 import  BeautifulSoup

#url = 'https://www.lagou.com/zhaopin/C++/?labelWords=label'
url = ' https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false'
headers = {
    'Referer'   : 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
}

data = {
    'first': 'true',
    'pn' : '1',
    'kd' : 'python'
}

wb_data = request.Request(url, headers = headers, data = parse.urlencode(data).encode('utf-8'), method='POST')
wb_data = request.urlopen(wb_data)

print(wb_data.read().decode('utf-8'))

#soup = BeautifulSoup(wb_data.read(), "html.parser")

#a = soup.select('div.p_top > a > h3')
#for x in a:
#    print(x)