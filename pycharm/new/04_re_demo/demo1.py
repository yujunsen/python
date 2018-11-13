import re

#1 匹配字符串
# text = 'hello'
# ret = re.match('he', text)
# print(ret.group())

# #2 匹配任意字符 . 任意
# text = 'ahello'
# ret = re.match('.he', text)
# print(ret.group())

# #3 匹配任意数字 \d 0-9
# text = '0hello'
# ret = re.match('\dhe', text)
# print(ret.group())

# #4 匹配任意非数字 \D !(0-9)
# text = '+hello'
# ret = re.match('\Dhe', text)
# print(ret.group())

# #4 匹配空白字符 (\n, \t, \r, 空格)
# text = '\t \nhe'
# ret = re.match('\s\s\she', text)
# print(ret.group())

# #5 \w匹配的是a-z和A-Z以及数字和下划线：
# text = 'h1_'
# ret = re.match('\w\w\w', text)
# print(ret.group())

# #6 \W匹配的是和\w相反的
# text = ' +='
# ret = re.match('\W\W\W', text)
# print(ret.group())

# #7 []组合的方式，只要满足中括号中的某一项都算匹配成功：
# text = 'a +='
# ret = re.match('[a1]', text)
# print(ret.group())

# #8 []组合的方式，只要满足中括号中的某一项都算匹配成功：
# text = '78521-565a'
# ret = re.match('[\d\-]+', text) #+匹配多个
# #ret = re.match('[^0-9\-]a+', text)  #^非
# print(ret.group())

# #9 *：可以匹配0或者任意多个字符
# text = '78521-565a'
# ret = re.match('[0-9]*', text) #+匹配多个
# #ret = re.match('[^0-9\-]a+', text)  #^非
# print(ret.group())

# #10 +：可以匹配1个或者多个字符。最少一个
# text = '78521-565a'
# ret = re.match('\d+', text) #+匹配多个
# #ret = re.match('[^0-9\-]a+', text)  #^非
# print(ret.group())

# #11 ?：匹配的字符可以出现一次或者不出现（0或者1
# text = '78521-565a'
# ret = re.match('\d?', text) #+匹配多个
# #ret = re.match('[^0-9\-]a+', text)  #^非
# print(ret.group())

# #12 {m}：匹配m个字符
# text = '78521-565a'
# ret = re.match('\d{5}', text) #+匹配多个
# #ret = re.match('[^0-9\-]a+', text)  #^非
# print(ret.group())


# text = 'dsadas_sd@fdsf.com' #"hynever@163.com"
# ret = re.match('\w+@[\w\.]+', text) #re.match('\w+@\w+\.\w+', text)
# print(ret.group())

# #验证URL：URL的规则是前面是http或者https或者是ftp然后再加上一个冒号，再加上一个斜杠，再后面就是可以出现任意非空白字符了
# text = "http://www.baidu.com/"
# ret = re.match('(http|https|ftp):[^\s]+', text)
# print(ret.group())

# #13 ^（脱字号）：表示以...开始
# text = '78521-565a'
# #ret = re.match('^7', text) #match相当于使用了^
# ret = re.search('^7', text)
# #ret = re.match('[^0-9\-]a+', text)  #^非
# print(ret.group())

# #14 $：表示以...结束
# text = '78521-565a'
# ret = re.search('a$', text)
# #ret = re.match('[^0-9\-]a+', text)  #^非
# print(ret.group())

# #匹配0-100之间的数字
# text = '5'
# ret = re.match('[1-9]\d?$|100$',text)
# print(ret.group())

text = '5dsad ids $58 dfdsf dfdsf hujhy $88'
ret = re.match('.*(\$\d+).*(\$\d+)',text)
#print(ret.group()) # == group(0)
#print(ret.group(1))
#print(ret.group(1, 2))
print(ret.groups())
