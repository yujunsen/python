from bs4 import BeautifulSoup
import string

data = []
path = r'D:\code\python\pycharm\day01\1_2_homework_required\index.html'

with open(path, "r") as wb_data:
    soup = BeautifulSoup(wb_data, "html.parser")
    images      = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    prices       = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    tardemarks  = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    stars       = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2) > span')
    reviews     = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')

    grades = []  # 设置一个空列表
    while len(stars) != 0:
        e = stars[0:5]  # 提取星星描述前五个元素，也就是一个商品的星级 0-4
        grades.insert(1, e)
        del stars[0:5]

for image, price, tardemark,  review, start in zip(images, prices, tardemarks, reviews, grades):
    star = []
    b = str(start)
    c = b.replace('<span class="glyphicon glyphicon-star"></span>', '★')  # 将描述实五角星的替换为图案
    d = c.replace('<span class="glyphicon glyphicon-star-empty"></span>', '☆')
    star.append(d)
    info = {
        'image'     : image.get('src'),
        'price'     : price.get_text(),
        'tardemark' : tardemark.get_text(),
        'star'      : ''.join(star).replace('[', '').replace(']', '').replace(',', '').replace(' ', ''),
        'review'    : review.get_text()
    }
    data.append(info)
    print(''.join(star).replace('[', '').replace(']', '').replace(' ', '').replace(',', ''))
 #   print(data)



#for i in data:
#    print(i)

"""
for i in grades[0]:
    print(i)
"""
