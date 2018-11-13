import re
import requests

base_url = 'https://www.qiushibaike.com/'
base = 'https://www.qiushibaike.com/8hr/page/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'
}

def parse_url(url):
    wb_data = requests.get(url, headers = headers )

    contents = re.findall('<div\sclass="content">.*?<span>(.*?)</span>', wb_data.text, re.DOTALL)
    duanzi = []
    for content in contents:
        #print(content)
        x = re.sub(r'<.*?>', '', content)
        print(x.strip())
        print('==' * 30)
        duanzi.append(x.strip())
    #print(wb_data.text)

def parse_page(url):
    wb_data = requests.get(url, headers=headers)
    #lis = re.findall('<li>\s<a\shref="(.*)"\srel="nofollow">', wb_data.text)
    #print(lis[5])

    lis = re.findall('<span\sclass="page-numbers">\s?(.*?)\s?</span>', wb_data.text, re.DOTALL)
    #print(lis[-1])
    for x in range(1, int(lis[-1]) + 1):
        temp = base + str(x)
        print(temp)
        parse_url(temp)
    # #for index, s in enumerate(lis):
    #     print(str(index) + ':' + s)
    #     print('=='*30)

if __name__ == '__main__':
    parse_page(base_url)