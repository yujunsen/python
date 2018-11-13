from urllib import request
from urllib import parse

#url = 'http://www.baidu.com/'
#wb_data = request.urlopen(url)

#request.urlretrieve(url, r'D:\code\python\pycharm\new\01_urllib_demo\down\baidu.html')

#print(wb_data.read())
#
# params = {'name' : 'yy', 'age': '18', 'greet' : 'hello world'}
# result = parse.urlencode(params)
# print(result)

# url = 'https://www.baidu.com/s'
# params = {'wd': '刘德华'}
# result = parse.urlencode(params)
# #print(result)
# url = url + '?' + result
# wb_data = request.urlopen(url)
#
# print(wb_data.read())

params = {'wd': '刘德华'}
result = parse.urlencode(params)#编码

qs = parse.parse_qs(result) #解码
print(qs)