import json

person = [
    {
        'usernmae' : '地方',
        'age':'14',
        'country':'china'
    },
    {
        'usernmae' : 'aa',
        'age':'19',
        'country':'china'
    }
]
json_str = json.dumps(person)
print(json_str)
with open('person.json', 'w', encoding='utf-8') as fp:
    json.dump(person, fp,ensure_ascii=False)