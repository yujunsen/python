from urllib import  request
from http.cookiejar import MozillaCookieJar

cookjar = MozillaCookieJar(r'down\cook.txt')
cookjar.load(ignore_discard=True, ignore_expires=True)#加载cook
handler = request.HTTPCookieProcessor(cookjar)
opener = request.build_opener(handler)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
}

req = request.Request('http://httpbin.org/cookies/set?course=abs', headers = headers)
resp = opener.open(req)
print(resp.read())
#cookjar.save(ignore_discard=True, ignore_expires=True) #保存cook