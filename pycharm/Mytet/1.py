import json

# with open(r'C:\Users\yujun\Desktop\replaceRule.akr', 'r', encoding='utf-8', newline='') as fp:
#     a = fp.readlines()
#
# a = json.dumps(a)
# #a = json.loads(a)
#
# with open(r'C:\Users\yujun\Desktop\aa.akr', 'w', encoding='utf-8', newline='') as fp:
#     fp.write(a)
#
# print(a)
true = 'true'
a = [
  {
    "enable": true,
    "id": 1,
    "regex": "(?<!\\d)6(?=[地离续])|(?<=[大着内])6",
    "replaceSummary": "6/陆",
    "replacement": "陆",
    "serialNumber": 1
  },
  {
    "enable": true,
    "id": 2,
    "regex": "cha(?=[槽头座队])",
    "replaceSummary": "cha/插",
    "replacement": "插",
    "serialNumber": 2
  },
  {
    "enable": true,
    "id": 3,
    "regex": "chou(?=[天风雨季雷])|chou(?=[如])",
    "replaceSummary": "chou/春",
    "replacement": "春",
    "serialNumber": 3
  },
  {
    "enable": true,
    "id": 4,
    "regex": "(?<=[空晃]|dang)dang",
    "replaceSummary": "dang/荡",
    "replacement": "荡",
    "serialNumber": 4
  },
  {
    "enable": true,
    "id": 5,
    "regex": "(?<=[震振])dang",
    "replaceSummary": "dang/动",
    "replacement": "动",
    "serialNumber": 5
  },
  {
    "enable": true,
    "id": 6,
    "regex": "(?<=[空漏])dong",
    "replaceSummary": "dong/洞",
    "replacement": "洞",
    "serialNumber": 6
  },
  {
    "enable": true,
    "id": 7,
    "regex": "(?<=[心浪水])hua|hua(?=[样式开椒招])",
    "replaceSummary": "hua/花",
    "replacement": "花",
    "serialNumber": 7
  },
  {
    "enable": true,
    "id": 8,
    "regex": "(?<=[精灵])hun|hun(?=魄)",
    "replaceSummary": "hun/魂",
    "replacement": "魂",
    "serialNumber": 8
  },
  {
    "enable": true,
    "id": 9,
    "regex": "(?<=[迷困疑蛊所])huo",
    "replaceSummary": "huo/惑",
    "replacement": "惑",
    "serialNumber": 9
  },
  {
    "enable": true,
    "id": 10,
    "regex": "(?<=[感冲刺过])ji|ji(?=[动烈进昂战发怒增将化荡活情励])",
    "replaceSummary": "ji/激",
    "replacement": "激",
    "serialNumber": 10
  },
  {
    "enable": true,
    "id": 11,
    "regex": "(jīng|jing|\\*)(?=[力神灵怪魄确魂气血锐])",
    "replaceSummary": "jīng/精",
    "replacement": "精",
    "serialNumber": 11
  },
  {
    "enable": true,
    "id": 12,
    "regex": "jiao(?=[流给待火])",
    "replaceSummary": "jiao/交",
    "replacement": "交",
    "serialNumber": 12
  },
  {
    "enable": true,
    "id": 13,
    "regex": "jianyin",
    "replaceSummary": "jianyin/奸淫",
    "replacement": "奸淫",
    "serialNumber": 13
  },
  {
    "enable": true,
    "id": 14,
    "regex": "(?<=赤)luo|luo(?=[露睡体奔])",
    "replaceSummary": "luo/祼",
    "replacement": "祼",
    "serialNumber": 14
  },
  {
    "enable": true,
    "id": 15,
    "regex": "mén",
    "replaceSummary": "mén/门",
    "replacement": "门",
    "serialNumber": 15
  },
  {
    "enable": true,
    "id": 16,
    "regex": "(?<=[捉玩摆])n[oò]ng|n[oò]ng(?=[虚手臣明点权])",
    "replaceSummary": "nòng/弄",
    "replacement": "弄",
    "serialNumber": 16
  },
  {
    "enable": true,
    "id": 17,
    "regex": "nv(?=[人孩子士儿子官装帝王奴])|(?<=[一男儿淑美少])nv",
    "replaceSummary": "nv/女",
    "replacement": "女",
    "serialNumber": 17
  },
  {
    "enable": true,
    "id": 18,
    "regex": "sao(?=[动气乱扰气客话])|(?<=[发牢风])sao",
    "replaceSummary": "sao/骚",
    "replacement": "骚",
    "serialNumber": 18
  },
  {
    "enable": true,
    "id": 19,
    "regex": "sè",
    "replaceSummary": "sè/色",
    "replacement": "色",
    "serialNumber": 19
  },
  {
    "enable": true,
    "id": 20,
    "regex": "(?<=[弹发暗影注喷反辐放])shè|shè(?=[箭日击程手])",
    "replaceSummary": "shè/射",
    "replacement": "射",
    "serialNumber": 20
  },
  {
    "enable": true,
    "id": 21,
    "regex": "(?<=[大小])tui|tui(?=[部上软])",
    "replaceSummary": "tui/腿",
    "replacement": "腿",
    "serialNumber": 21
  },
  {
    "enable": true,
    "id": 22,
    "regex": "(?<=[属血人能攻害征死])xing|xing(?=[情能格致质])",
    "replaceSummary": "xing/性",
    "replacement": "性",
    "serialNumber": 22
  },
  {
    "enable": true,
    "id": 23,
    "regex": "(?<=白日宣|奇)yin|yin(?=[邪僧贼])",
    "replaceSummary": "yin/淫",
    "replacement": "淫",
    "serialNumber": 23
  },
  {
    "enable": true,
    "id": 24,
    "regex": "(?<=[太光遮])y[iī]n|y[iī]n(?=[沉阳历霾暗干面凉影谋毒险湿天魂文晦冷骘])",
    "replaceSummary": "yin/阴",
    "replacement": "阴",
    "serialNumber": 24
  },
  {
    "enable": true,
    "id": 25,
    "regex": "(?<=[真])zhèng",
    "replaceSummary": "zhèng/正",
    "replacement": "正",
    "serialNumber": 25
  },
  {
    "enable": true,
    "id": 26,
    "regex": "(?<=[求帮])zhù",
    "replaceSummary": "zhù/助",
    "replacement": "助",
    "serialNumber": 26
  },
  {
    "enable": true,
    "id": 27,
    "regex": "(?<=[之九]|十有)\\*\\*|\\*\\*(?=[岁年月日周天个米丈里层成熟点]|不离十)",
    "replaceSummary": "**/八九",
    "replacement": "八九",
    "serialNumber": 27
  },
  {
    "enable": true,
    "id": 28,
    "regex": "\\*\\*(?=[纵控])",
    "replaceSummary": "**/被操",
    "replacement": "被操",
    "serialNumber": 28
  },
  {
    "enable": true,
    "id": 29,
    "regex": "(?<=[帝俄法])\\*\\*|\\*\\*(?=[队务需人])",
    "replaceSummary": "**/国军",
    "replacement": "国军",
    "serialNumber": 29
  },
  {
    "enable": true,
    "id": 30,
    "regex": "巨\\*",
    "replaceSummary": "巨*/巨大",
    "replacement": "巨大",
    "serialNumber": 30
  },
  {
    "enable": true,
    "id": 31,
    "regex": "\\*轮",
    "replaceSummary": "*轮/法轮",
    "replacement": "法轮",
    "serialNumber": 31
  },
  {
    "enable": true,
    "id": 32,
    "regex": "\\*\\*(?=裸)",
    "replaceSummary": "**/赤裸",
    "replacement": "赤裸",
    "serialNumber": 32
  },
  {
    "enable": true,
    "id": 33,
    "regex": "(?<=[头匹])\\*\\*\\*",
    "replaceSummary": "***/草泥马",
    "replacement": "草泥马",
    "serialNumber": 33
  },
  {
    "enable": true,
    "id": 34,
    "regex": "(\\B\\W*)?([最更][快新优優]|天才|[找看]?本[站书](?![看籍])|如果您喜欢|[一1壹]秒记?|(第?[1壹一eE])?小说|(为了方便下次|欢迎)阅读|罩杯女|看\\W?小\\W?说|原创|以下是|章节(内容)?|[a-zA-Z]+\\.|手(打|机(阅读|用户))|2[kK]|为您提|(提供)?无弹窗|(高速)?首发|[纯全]文字|免费电|请用搜|(猎文|奇书)网|(武林|三七)中文|泰国最|(新书|月票)榜?).*(\\r\\n)?.*(((小[说說])?(在线)?(首发地?|(阅读|閱讀|用户)(體驗|体验|网|器)?))|复制|求?(订阅|推荐|票?支持)|访问|来发现|下载|广告|[章情]节|搜索|站哦?|赛吧?|用户独享|[网網地]址?|[mMgG]|[最更][快新])\\W*",
    "replaceSummary": "通用长垃圾集合",
    "replacement": "",
    "serialNumber": 34
  },
  {
    "enable": true,
    "id": 35,
    "regex": "(^\\W*)?(\\(未完待续|求(.{1,2}票|收藏|订阅).*|本文地址|欢迎阅读|.?顶\\W?点\\W?小\\W?说|请使用访问.*|请牢记.*|里面(小说)?.*破防盗|\\[搜索尽在.*\\]|《书.?香.?阁.*|.*免费更新|最\\s{0,3}新.{0,3}全.*)\\W*",
    "replaceSummary": "通用短垃圾集合",
    "replacement": "",
    "serialNumber": 35
  },
  {
    "enable": true,
    "id": 36,
    "regex": "(记住mt?|nt|浏览阅读地址|推荐一本.*|看爽的小说就到.*?|(\\[|［)棉花.*?(\\]|］)|正文.+请欣赏|(?<![怂a-zA-Z0-9])[a-zA-Z](?![a-zA-Z0-9市\"”形格恤])|2网|超.+?发|百度.*搜索|.*?章节内容.*|<.*|小說.*|双倍.*月票)\\W?",
    "replaceSummary": "合集补充",
    "replacement": "",
    "serialNumber": 36
  },
  {
    "enable": true,
    "id": 37,
    "regex": "(^请记住.*|&.*|\\(|（|【.{2,5}|（第.更.）|([pP][Ss](?=[:：])|感谢[盟书]友).*)$",
    "replaceSummary": "补充2",
    "replacement": "",
    "serialNumber": 37
  },
  {
    "enable": true,
    "id": 38,
    "regex": "(http://)?([a-zA-Z]+\\.)+[a-zA-Z]+|(https?\\:)?(//)?[WwｗＷ]{1,3}.*",
    "replaceSummary": "去网址",
    "replacement": "",
    "serialNumber": 38
  },
  {
    "enable": true,
    "id": 39,
    "regex": "[^\\u4e00-\\u9fa5a-zA-Z0-9\\W]{1,}|^\\W+$|—{4,}.*|[≦＜＞≤．﹤≯≧≥┡]+",
    "replaceSummary": "去特殊符号，纯标点行",
    "replacement": "",
    "serialNumber": 39
  }
]
json_str = json.dumps(a, ensure_ascii=False)
b = json.loads(json_str)
# print(json_str)
c = []
false = 'false'
e = [{"enabled":true,"first":"十([之|有]?)\\*\\*","id":1,"name":"十之八九等","noRegular":false,"order":0,"second":"十$1八九"},{"enabled":true,"first":"十\\*\\*([岁|年|月|日|周|天|个|米|丈|里]*?)","id":2,"name":"十八九岁等","noRegular":false,"order":0,"second":"十八九$1"},{"enabled":true,"first":"[^\\d]6([地|续])","id":3,"name":"陆地、陆续","noRegular":false,"order":0,"second":"陆$1"},{"enabled":true,"first":"大6","id":4,"name":"大陆","noRegular":false,"order":0,"second":"大陆"},{"enabled":true,"first":"([\\s]*?[\\(\\（]?未完待续[\\）\\)]?)","id":5,"name":"未完待续","noRegular":false,"order":0,"second":""}]

for x in e:
    print(x)
id = 0
for x in b:
    data = {}
    #print(x['enable'])
    data['enable'] = x['enable']
    data['first'] = x['regex']
    data['id'] = int(x['id']) + 5
    data['name'] = x['replaceSummary']
    data['order'] = 1
    data['second'] = x['replacement']
    id = int(x['id']) + 5
    c.append(data)

data['enable'] = true
data['first'] = '偷kui'
data['id'] = id
data['name'] = '偷窥'
data['order'] = 1
data['second'] = '偷窥'
id += 1
c.append(data)

#print(c)
d = json.dumps(c, ensure_ascii=False)
with open(r'C:\Users\yujun\Desktop\aa.akr', 'w', encoding='utf-8') as fp:
    fp.write(d)

"""
[
    {
        "enabled":true,
        "first":"十([之|有]?)\*\*",
        "id":1,
        "name":"十之八九等",
        "noRegular":false,
        "order":0,
        "second":"十$1八九"
    },
    {
        "enabled":true,
        "first":"十\*\*([岁|年|月|日|周|天|个|米|丈|里]*?)",
        "id":2,
        "name":"十八九岁等",
        "noRegular":false,
        "order":0,
        "second":"十八九$1"
    },
    {
        "enabled":true,
        "first":"[^\d]6([地|续])",
        "id":3,
        "name":"陆地、陆续",
        "noRegular":false,
        "order":0,
        "second":"陆$1"
    },
    {
        "enabled":true,
        "first":"大6",
        "id":4,
        "name":"大陆",
        "noRegular":false,
        "order":0,
        "second":"大陆"
    },
    {
        "enabled":true,
        "first":"([\s]*?[\(\（]?未完待续[\）\)]?)",
        "id":5,
        "name":"未完待续",
        "noRegular":false,
        "order":0,
        "second":""
    },
    {
        "enabled":true,
        "first":"cha(?=[槽头座队])",
        "id":6,
        "name":"cha/插",
        "noRegular":false,
        "order":0,
        "second":"插"
    },
    {
        "enabled":true,
        "first":"chou(?=[天风雨季雷])|chou(?=[如])",
        "id":7,
        "name":"chou/春",
        "noRegular":false,
        "order":0,
        "second":"春"
    },
    {
        "enabled":true,
        "first":"(?<=[空晃]|dang)dang",
        "id":8,
        "name":"dang/荡",
        "noRegular":false,
        "order":0,
        "second":"荡"
    },
    {
        "enabled":true,
        "first":"(?<=[震振])dang",
        "id":9,
        "name":"dang/动",
        "noRegular":false,
        "order":0,
        "second":"动"
    }
]
"""