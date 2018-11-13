from bs4 import BeautifulSoup

data = []
path = r'D:\code\python\pycharm\day01\1_2_homework_required\index.html'

with open(path, "r") as wb_data:
    soup = BeautifulSoup(wb_data, "html.parser")
    imgaes      = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    prices       = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    tardemarks  = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    stars       = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    # 为了从父节点开始取,此处保留:nth-of-type(2),观察网页,多取几个星星的selector,就发现规律了
    reviews     = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')

for image, price, tardemark ,star, review in zip(imgaes, prices, tardemarks, stars, reviews):
    info = {
        'image'     : image.get('src'), # 使用get 方法取出带有src的图片链接
        'price'     : price.get_text(), # 使用get_text()方法取出文本
        'tardemark' : tardemark.get_text(),
        'star'      : len(star.find_all("span", "glyphicon glyphicon-star")),
        # 观察发现,每一个星星会有一次<span class="glyphicon glyphicon-star"></span>,所以我们统计有多少次,就知道有多少个星星了;
        # 使用find_all 统计有几处是★的样式,第一个参数定位标签名,第二个参数定位css 样式,具体可以参考BeautifulSoup 文档示例http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find-all;
        # 由于find_all()返回的结果是列表,我们再使用len()方法去计算列表中的元素个数,也就是星星的数量
        'review'    : review.get_text()
    }
    #print(data)
    data.append(info)

for i in data:
    if i['star'] >= 5:
        print(i)

#body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img
#body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4.pull-right
#body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4:nth-child(2) > a
#body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p:nth-child(2)
#body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p.pull-right