from bs4 import BeautifulSoup
import requests
import time
urll = 'https://knewone.com/discover?page=1'

def get_page(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('header > a > img')
    for img in imgs:
        data = {
            'title' : img.get('alt'),
            'img'   : img.get('src')
        }
        print(img)



def get_more_pages(start,end):
    for one in range(start,end):
        global urll
        if one == 1:
            pass
        else:
            urll = urll + r'&page=' + str(one)
        get_page(urll)
get_more_pages(1, 9)
#get_page('https://knewone.com/discover?page=1&page=2&page=2')
#print(soup)
