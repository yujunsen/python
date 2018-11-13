from lxml import etree
import requests
import pymongo
import time

url_dty ='http://www.ygdy8.net'

proxy = {
    'https':'124.89.2.250:63000'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'

}

def get_str(html):
    return etree.tostring(html, encoding='utf-8').decode('utf-8')

def test_url():
    pro = {
        'http': '115.223.208.25:9000'
    }

    response = requests.get('http://httpbin.org/get', headers = headers)
    print('源')
    print(response.text)
    response = requests.get('http://httpbin.org/get', headers = headers ,proxies = pro)
    print('now')
    print(response.text)



def get_detail_urls(url):
    response = requests.get(url, headers = headers, proxies = proxy)
    #print(response.content.decode('gbk'))
    html = response.content.decode('gbk')
    html = etree.HTML(html)
    url = url_dty + html.xpath('//em/a/@href')[0]#精品链接
    #print(url)
    get_pase_num(url)

def get_pase_url(url): #解析页面电影链接
    response = requests.get(url, headers=headers, proxies=proxy)
    html = response.text
    #print(response.encoding)
    html = etree.HTML(html)
    urls = html.xpath('//a[@class="ulink"]/@href')
    names = html.xpath('//a[@class="ulink"]/text()')
    for url, name in zip(urls, names):
        # #print(name + ':' + url_dty + url)
        # temp = name + ''
        # #print(temp.encode('urf-8'))
        # name = temp.encode('ISO-8859-1').decode('gbk')
        # #print(type(temp))
        # #print(temp)
        # print(name + ':' + url_dty + url)
        #print(url_dty + url)
        get_pase_data(url_dty + url)
        #time.sleep(1)

def get_pase_num(url, num = 0):#解析页面链接
    base_url = url.replace('index.html', '')

    response = requests.get(url, headers=headers, proxies=proxy)
    html = response.content.decode('gbk')
    html = etree.HTML(html)
    urls = html.xpath('//select[@name="sldd"]/option/@value')
    #print(urls)
    if num == 0:
        num = 5
    for i in range(0, num, 1):
        print(str(i + 1) + 'start' )
        #print(base_url + urls[i])
        get_pase_url(base_url + urls[i])
        print(str(i + 1) + 'end')
        #time.sleep(1)

    # for x in urls:
    #     print(base_url + x)
        #print(get_str(x))

def get_pase_data(url):
    moive = {}
    response = requests.get(url, headers = headers, proxies = proxy)
    html = response.content.decode('gbk')
    html = etree.HTML(html)
    title = html.xpath('//font[@color="#07519a"]/text()')[0]
    img = html.xpath('//div[@id="Zoom"]//img/@src')
    infos = html.xpath('//div[@id="Zoom"]//text()')
    moive['title'] = title
    #print(img)
    moive['cover'] = img[0]
    if len(img) == 2:
        moive['screenshot'] = img[1]

    def parse_info(info, text):
        return  info.replace(text, '').strip()

    for index, info in enumerate(infos):
        if info.startswith('◎年　　代'):
            #info = info.replace('◎年　　代', '').strip()
            moive['year'] = parse_info(info, '◎年　　代')
        if info.startswith('◎产　　地'):
            moive['country'] = parse_info(info, '◎产　　地')
        if info.startswith('◎类　　别'):
            moive['category'] = parse_info(info, '◎类　　别')
        if info.startswith('◎豆瓣评分'):
            moive['douban_rating'] = parse_info(info, '◎豆瓣评分')
        if info.startswith('◎片　　长'):
            moive['duration'] = parse_info(info, '◎片　　长')
        if info.startswith('◎导　　演'):
            moive['director'] = parse_info(info, '◎导　　演')
        if info.startswith('◎主　　演'):
            info = parse_info(info, '◎主　　演')
            actors = [info]
            for x in range(index +1, len(infos)):
                actor = infos[x].strip()
                #print(actor)
                if actor.startswith('◎'):
                    break
                actors.append(actor)
            moive['actor'] = actors
        if info.startswith('◎简　　介'):
            texts =[]
            for x in range(index + 1, len(infos)):
                text = infos[x].strip()
                #print(text)
                if len(text) == 0:
                    break
                texts.append(text)
            moive['profile'] = texts

    down_ftp_url = html.xpath('//div[@id="Zoom"]//a/text()')[0]
    down_magnet_url = html.xpath('//div[@id="Zoom"]//a/@href')[0]
    moive['down_ftp_url'] = down_ftp_url
    moive['down_magnet_url'] = down_magnet_url


    print(moive)

def a():
    a='a:'
    y = {"adsda", "dasdas", "dasd"}
    b = map(lambda a: a+'1', y)
    for x in b:
        print(x)



if __name__ == '__main__':
    # get_detail_urls(url_dty)
    #get_pase_url('http://www.ygdy8.net/html/gndy/dyzz/list_23_3.html')
    # s = '大撒大撒'.encode('utf-8')
    # print(s.decode('utf-8'))
    # get_pase_data('http://www.ygdy8.net/html/gndy/dyzz/20180603/56925.html')
    test_url()
