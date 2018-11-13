
from urllib import parse

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=06074089_4_pg&wd=%E5%88%98%E5%BE%B7%E5%8D%8E%20aas&oq=%25E5%2588%2598%25E5%25BE%25B7%25E5%258D%258E&rsv_pq=a29af6ee0002b941&rsv_t=e698Mn2ixKF52Md325mlfsLt1YXyzbn9Z8VfjJpkj4H9MZumD3vvOzkw55IkOEQGgKUOVw&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&inputT=2655&rsv_sug4=2656'
#ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='ie=utf-8&f=8&rsv_bp=1&tn=06074089_4_pg&wd=%E5%88%98%E5%BE%B7%E5%8D%8E%20aas&oq=%25E5%2588%2598%25E5%25BE%25B7%25E5%258D%258E&rsv_pq=a29af6ee0002b941&rsv_t=e698Mn2ixKF52Md325mlfsLt1YXyzbn9Z8VfjJpkj4H9MZumD3vvOzkw55IkOEQGgKUOVw&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&inputT=2655&rsv_sug4=2656', fragment='')

# result = parse.urlparse(url)
# print(result)
# print('scheme', result.scheme)
# print('netloc', result.netloc)
# print('path', result.path)
# print('query', result.query)

result = parse.urlsplit(url)# 没有 params='',
#SplitResult(scheme='https', netloc='www.baidu.com', path='/s', query='ie=utf-8&f=8&rsv_bp=1&tn=06074089_4_pg&wd=%E5%88%98%E5%BE%B7%E5%8D%8E%20aas&oq=%25E5%2588%2598%25E5%25BE%25B7%25E5%258D%258E&rsv_pq=a29af6ee0002b941&rsv_t=e698Mn2ixKF52Md325mlfsLt1YXyzbn9Z8VfjJpkj4H9MZumD3vvOzkw55IkOEQGgKUOVw&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&inputT=2655&rsv_sug4=2656', fragment='')

print(result)
print('scheme', result.scheme)
print('netloc', result.netloc)
print('path', result.path)
print('query', result.query)