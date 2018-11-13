import os

# a = os.path.dirname(__file__) #D:/code/python/pycharm/new/09_scray_demo/bmw/bmw
# a = os.path.dirname(a) #D:/code/python/pycharm/new/09_scray_demo/bmw
# a =os.path.join(a, 'imgs')
images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imgs')
#os.path.exists(images_path) #判断路径是否存在
if not os.path.exists(images_path):
    #print('imgs文件夹不存在')
    os.mkdir(images_path) #创建文件夹
else:
    print('imgs文件夹存在')
