import csv

with open('classroom.csv', 'r', encoding='utf-8') as fp:
    reader = csv.DictReader(fp)
    next(reader)
    for x in reader:
        print('name:' + x['username'])
        print('age:' + x['age'])
        print('height:' + x['height'])

    # reader = csv.reader(fp)
    # for x in reader:
    #     print(x)