from urllib import request

# 这个是没有使用代理的
# resp = request.urlopen('http://httpbin.org/get')
# print(resp.read().decode("utf-8"))#"origin": "64.137.250.136"

handler = request.ProxyHandler({'https' : '114.232.163.238:18118'})
opener = request.build_opener(handler)
req = request.Request("http://httpbin.org/ip")
resp = opener.open(req)
print(resp.read()) #"origin": "222.211.182.170"\n

# 西刺免费代理IP：http://www.xicidaili.com/
# 快代理：http://www.kuaidaili.com/
# 代理云：http://www.dailiyun.com/