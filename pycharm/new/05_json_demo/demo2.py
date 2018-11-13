import json

# person = [
#     {
#         'usernmae' : '地方',
#         'age':'14',
#         'country':'china'
#     },
#     {
#         'usernmae' : 'aa',
#         'age':'19',
#         'country':'china'
#     }
# ]
# json_str = json.dumps(person)
# #print(json_str)
#
# json_str = json.loads(json_str)
# # print(json_str)
# # with open('person.json', 'w', encoding='utf-8') as fp:
# #     json.dump(person, fp,ensure_ascii=False)
#   json_str = ''
with open('person.json', 'r', encoding='utf-8') as fp:
    json_str = json.load(fp)

for x in json_str:
    print(x)