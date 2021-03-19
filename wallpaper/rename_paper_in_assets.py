'''
将win10锁屏壁纸转换为jpg格式，从而看到图片内容
图片包含有长屏的和宽屏的

'''

import os, shutil

# win10锁屏壁纸存储位置
# 不同电脑应该差不多
wallpaper_path = r'C:\Users\cpyy103\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'

os.chdir(wallpaper_path)
for image in os.listdir():
    shutil.copy(image, image + '.jpg')
    
print('Done')
