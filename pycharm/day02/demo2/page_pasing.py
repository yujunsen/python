from bs4 import BeautifulSoup
import requests
import pymongo

#url = 'https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.251448b0BzfJU3&st_edtime=1&page=2&q=%CF%D4%CA%BE%C6%F7&ist=0'
urls = 'https://2.taobao.com/'
#https://s.2.taobao.com/list/list.htm?spm=2007.1000261.641120289.2.135334f1qzF1FZ&st_edtime=1&q=%CF%D4%CA%BE%C6%F7&ist=0
test = 'https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E6%98%BE%E7%A4%BA%E5%99%A8&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest'
header = {
   # 'Cookie': 'mt=ci%3D0_0; swfstore=256333; thw=cn; cna=mNrDE4PeEQECAavfIJrlCVWb; t=57b29a24b6489287d6853738ce11a86b; hng=CN%7Czh-CN%7CCNY%7C156; enc=wuQUZ9wR5al5j3pvTbsK%2BsUH4Kc5qe71NxDA6Rz34HeC1vqXAjpfnOGsne6kZhRzfIj8mwAHMwX1XiJOhNrgHw%3D%3D; _m_h5_tk=db0bb048533ffca776638b30346916b2_1532322658331; _m_h5_tk_enc=63a93df7836e9671e7d3d18c66e179bd; miid=894817263574478884; cookie2=1f3e165978abf68345c70654d331f8b5; _tb_token_=e1ee56efbe807; l=AqmphbJJ/Z9abbFsu05OGATPOV4Ddp2o; tg=0; v=0; unb=2671586444; sg=%E7%BB%934e; _l_g_=Ug%3D%3D; skt=2f0e734c8cb7a75c; cookie1=WvBhSPQVMMarLsixn8FTEpmY8dNPzjKDuYAN8q6Qols%3D; csg=9839a036; uc3=vt3=F8dBzrmVk7OTBB2P69E%3D&id2=UU6m3oShI5kl6A%3D%3D&nk2=sFDSx0a2lvOPcA%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; existShop=MTUzMjUxMDcxMw%3D%3D; tracknick=%5Cu6709%5Cu6CA1%5Cu6709%5Cu7EA0%5Cu7ED3; lgc=%5Cu6709%5Cu6CA1%5Cu6709%5Cu7EA0%5Cu7ED3; _cc_=UIHiLt3xSw%3D%3D; dnk=%5Cu6709%5Cu6CA1%5Cu6709%5Cu7EA0%5Cu7ED3; _nk_=%5Cu6709%5Cu6CA1%5Cu6709%5Cu7EA0%5Cu7ED3; cookie17=UU6m3oShI5kl6A%3D%3D; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTfKfJ%2FGUG5BA%3D%3D&tag=8&lng=zh_CN; mt=ci=0_1; whl=-1%260%260%260; isg=BAAA-_eLT5t0VDOfEZPLkF090Y4SIeVRohdiMXqRgJuu9aEfIp1h4mOPCR2QxZwr; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'

}

list = []

def get_data(url):
    wb_data = requests.get(url)

# J_Pages > a.paginator-next

def get_url(url):
    wb_data = requests.get(url, headers = header)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    a = soup.select('img')
    print(a)
    #url = soup.select('a.paginator-next')
    #for a in url:
    #    print(a)




if __name__ == '__main__':
    # url = urls
    # wb_data = requests.get(url)
    # # if wb_data.status_code != 200:
    # #     # print(wb_data.status_code)  # 打印状态码
    # #     return
    # soup = BeautifulSoup(wb_data.text, 'lxml')
    # url = soup.select(' div.left-mod.col > div.tag-cloud > a')
    # print(url[0].get('href'))
    get_url(test)