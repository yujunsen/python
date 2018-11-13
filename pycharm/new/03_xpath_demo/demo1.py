from lxml import etree
import requests

urls = [
    'https://www.baidu.com',
    'https://www.lagou.com/',
    'http://httpbin.org/get'
]
proxy = {
    'http':'183.167.217.152:63000'
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}


def html_parse_1(html):
    html = etree.HTML(html)
    #html = etree.parse(html)
    print(type(html))
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))

    with open(r'down/demo1.html', 'w', encoding='utf-8') as fp:
        fp.write(etree.tostring(html, encoding='utf-8').decode('utf-8'))

    return html

def html_parse_2(html):
    parse = etree.HTMLParser(encoding='utf-8')
    html = etree.parse(html, parser=parse)
    #html = etree.HTML(html)
    print(type(html))
    print(etree.tostring(html, encoding='utf-8').decode('utf-8'))
    with open(r'down/demo1_parse.html', 'w', encoding='utf-8') as fp:
        fp.write(etree.tostring(html, encoding='utf-8').decode('utf-8'))

    return html

if __name__ == '__main__':
    #html_parse
    #req = requests.get(urls[1], headers = headers, proxies = proxy)
    #with open(r'down/demo1.html', 'w', encoding='utf-8') as fp:
    #    fp.write(req.content.decode('utf-8'))
    #print(req.content.decode('utf-8'))
    html=html_parse_2(r'down/demo1.html')


