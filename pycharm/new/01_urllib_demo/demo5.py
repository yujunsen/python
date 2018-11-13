from urllib import request


handler = request.ProxyHandler({'https' : '114.232.163.238:18118'})
opener = request.build_opener(handler)
#req = request.Request("http://httpbin.org/ip")
#resp = opener.open(req)

#print(resp.read())

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Cookie': 'anonymid=jk4w0s34-dxbr2d; depovince=SC; _r01_=1; ick_login=7429f714-df50-4727-95aa-2685288470d0; jebecookies=5e618720-78d4-42c2-9b94-7b252f83c836|||||; _de=EA5778F44555C091303554EBBEB4676C696BF75400CE19CC; p=44796cbb064e0233711e1ba3f3e952f51; first_login_flag=1; ln_uact=970138074@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20170428/1700/main_nhiB_aebd0000854a1986.jpg; t=61dbdff10c03b70c532255c1c0814b9b1; societyguester=61dbdff10c03b70c532255c1c0814b9b1; id=443362311; xnsid=14a74266; loginfrom=syshome; jebe_key=1104b83e-11e3-413d-a5f5-980d4395a30d%7Ca022c303305d1b2ab6b5089643e4b5de%7C1532956821677%7C1%7C1532956828491; wpsid=15221228637850; wp_fold=0'
}

url = 'http://www.renren.com/880151247/profile'



req = request.Request(url,headers=headers)
#resp = request.urlopen(req)
resp = opener.open(req)
# with open('renren.html','w') as fp:
#     fp.write(resp.read().decode('utf-8'))

with open(r'D:\code\python\pycharm\new\01_urllib_demo\down\test.html', 'w', encoding="utf-8") as fp:
    fp.write(resp.read().decode('utf-8'))