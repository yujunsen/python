import csv

def write_csv_demo1():
    headers = ['username', 'age', 'height']
    values = [
        ('张山', 18, 165),
        ('李四', 20, 190),
        ('王五', 22, 180)
    ]

    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        witer = csv.writer(fp)
        witer.writerow(headers)
        witer.writerows(values)

def write_csv_demo2():
    headers = ['username', 'age', 'height']
    values = [
        {'username': '张山', 'age': '18', 'height' : 190},
        {'username': '李四', 'age': '20', 'height' : 188},
        {'username': '王五', 'age': '22', 'height' : 198}
    ]
    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        witer = csv.DictWriter(fp, headers)
        witer.writeheader()
        witer.writerows(values)



if __name__ == '__main__':
    write_csv_demo2()