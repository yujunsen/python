from lxml import etree
import requests
import pymongo
import time

list = []

#连接数据库
client = pymongo.MongoClient('localhost', 27017)
demo = client['xpatn_demo']
demo2 = demo['demo2']

urls = [
    'https://www.baidu.com',
    'https://www.lagou.com/',
    'http://httpbin.org/get'
]
filenames = [
    r'down/demo_2.html',
    r'down/demo_2_parse.html'
    ]
proxy = {
    'http':'183.167.217.152:63000'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36',
    'Upgrade-Insecure-Requests': '1'
    #'Referer': 'https://www.lagou.com'
    #'Cookie': '_ga=GA1.2.2094003925.1532625280; user_trace_token=20180727011439-613eec22-90f7-11e8-a4d6-525400f775ce; LGUID=20180727011439-613ef0f5-90f7-11e8-a4d6-525400f775ce; index_location_city=%E6%88%90%E9%83%BD; _gid=GA1.2.1762767001.1533132824; fromsite="localhost:63342"; LGSID=20180802232509-3dac184f-9668-11e8-a0db-5254005c3644; PRE_UTM=; PRE_HOST=localhost; PRE_SITE=http%3A%2F%2Flocalhost%3A63342%2Fnew%2F03_xpath_demo%2Fdown%2Fdemo_2.html%3F_ijt%3Del0cjof4v6dem54h5jck51h631; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FC%2B%2B%2F3%2F%3FfilterOption%3D2; _gat=1; JSESSIONID=ABAAABAAAGFABEF79E90AAB40514288C4F4F17B6221442B; SEARCH_ID=05e42b4fad0b49ab8c51edd8e86c0d8d; LGRID=20180802233024-f999b4da-9668-11e8-aebf-525400f775ce'

}

def save_html(url, is_save, data = None):
    req = requests.get(url, headers=headers, proxies = proxy, data=data)
    if is_save == True:
        with open(filenames[0], 'w', encoding='utf-8') as fp:
            fp.write(req.content.decode('utf-8'))
    return  req


def html_parse_1(html):
    parse = etree.HTMLParser(encoding='utf-8')
    html = etree.parse(html, parser=parse)
    #html = etree.HTML(html)
    print(type(html))
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))
    with open(filenames[1], 'w', encoding='utf-8') as fp:
        fp.write(etree.tostring(html, encoding='utf-8').decode('utf-8'))
    for i in html.xpath('//a[@data-lg-tj-id="4A00"]'):
        print(etree.tostring(i, encoding='utf-8').decode('utf-8'))
    return html

def html_parse_2(html):
    parse = etree.HTMLParser(encoding='utf-8')
    html = etree.parse(html, parser=parse)
    with open(filenames[1], 'w', encoding='utf-8') as fp:
        fp.write(etree.tostring(html, encoding='utf-8').decode('utf-8'))
    #for i in html.xpath('//a[@data-lg-tj-id="4A00"]/@href'):
    for i in html.xpath('//a[@data-lg-tj-id="4A00"]/text()'):
        #print(etree.tostring(i, encoding='utf-8').decode('utf-8'))
        print(i)
    return html

def get_str(html):
    return etree.tostring(html, encoding='utf-8').decode('utf-8')

def html_parse_3(html):
    #parse = etree.HTMLParser(encoding='utf-8')
    #html = etree.parse(html, parser=parse)
    html = etree.HTML(html)
    #print(get_str(html))
    jobs = html.xpath('//h3/text()')
    ems = html.xpath('//em/text()')
    times = html.xpath('//span[@class="format-time"]/text()')
    url = html.xpath('//a[@class="position_link"]/@href')
    names = html.xpath('//div[@class="company_name"]/a/text()')
    indus = html.xpath('//div[@class="industry"]/text()')
    moneys = html.xpath('//span[@class="money"]/text()')
    claims = html.xpath('///div[@class="p_bot"]/div/text()')
    cates = html.xpath('//div[@class="list_item_bot"]/div[1]')
    welfares = html.xpath('//div[@class="list_item_bot"]/div[2]/text()')
    for job, em, tim, ur, name, indu, money, claim, cate, welfare, in zip(jobs, ems, times, url, names, indus, moneys, claims, cates, welfares):
        #print(get_str(x))
        #print(x)

        info = {
            '职位': job,
            '位置': em,
            '时间': tim,
            '网页': ur,
            '公司': name,
            '公司规模': ''.join(indu.split()),
            '薪水': money,
            '要求': ''.join(claim.split()),
            '标签': ' '.join(get_str(cate).replace('</', '').replace('>', '').replace('span', '').
                             replace('<', '').replace('div', '').replace('&#13;', '').
                             replace(' ', '').replace(r'class="li_b_l"', '').split()),
            '福利': welfare.replace('“', '').replace('”', '')#x.split()#get_str(x)

        }
        demo2.insert_one(info)
        print(info)

        #print(x)
def get_mogo_data():
    #print(demo2.next)
    for x in demo2.find():
       print(x)

def test(url = None):
    # if url == None:
    #    return None
    data = {
        'first': 'true',
        'pn': '1',
        'kd': 'c++'
    }
    url = 'https://www.lagou.com/zhaopin/C++/'
    req = save_html(url, False)
    html = etree.HTML(req.text)
    num = html.xpath('//a[@class="page_no"][last()-1]/text()')[0]
   # b = demo['urls']
    for x in range(1, int(num) + 1, 1):
        #print(url + str(x))
        list.append(url+str(x))
        #b.insert_one({ str(x) : url + str(x)})
    for i in list:
        req = save_html(i, False, data)
        html_parse_3(req.text)
        print(i)
        time.sleep(1)
    #url.insert(list)


if __name__ == '__main__':
    #req = save_html('https://www.lagou.com/zhaopin/C++/4', True)
    test()
    #html_parse_3(req.text)
    #html_parse_3(req)
    #get_mogo_data()


