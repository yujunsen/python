from bs4 import BeautifulSoup

data = []

with open("D:\code\python\pycharm\day01\web\sample1.html", "r") as wb_data:
    Soup = BeautifulSoup(wb_data, "html.parser")    #BeautifulSoup4 把"html"改成html.parser
    titles = Soup.select('ul > li > div.article-info > h3 > a')
    images = Soup.select('ul > li > img')
    descs = Soup.select('ul > li > div.article-info > p.description')
    rates = Soup.select('ul > li > div.rate > span')
    cates = Soup.select('ul > li > div.article-info > p.meta-info')
    """
    images  = Soup.select("body > div.main-content > ul > li:nth-of-type(1) > img")
    titles  = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > div.article-info > h3 > a')
    descs   = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > div.article-info > p.description')
    rates   = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > div.rate > span')
    cates   = Soup.select('ul > li > div.article-info > p.meta-info')"""
"""
print(images)
print(titles)
print(descs)
print(rates)
print(cates)
"""

for title, image, desc, rate, cate in zip(titles, images, descs, rates, cates):
   # print(titles, image, desc, rate, cate )
    info = {
        'title' : title.get_text(),
        'image' : image.get('src'),
        'desc'  : desc.get_text(),
        'rate'  : rate.get_text(),
        'cate'  : list(cate.stripped_strings)
    }
    data.append(info)

#print(data['title'])
for i in data:
    if(len(i['title'])) >= 3:
        print(i['title'], i['cate'])
    #print(i)

"""
with open(r"D:\code\python\pycharm\day01\web\sample1.html", "r") as wb_data:
    soup = BeautifulSoup(wb_data, 'lxml')
    image = soup.select('body > div.main-content > ul > li:nth-of-type(1) > img')
    #print(soup)
    print(image)
    print(titles)
    print(decs)
    print(rates)

"""

#cates.stripped_strings
"""
for title,image,desc,rate,cate in zip(titles, images, descs, rates, cates):
    data = {
        'title' : title.get_text(),
        'cate1' : list(cates.stripped_strings),
        #'cate2' : cates[1].get_text(),
        'desc'  : desc.get_text(),
        'rate'  : rate.get_text(),
        'image' : image.get('src')
    }
    print(data)"""