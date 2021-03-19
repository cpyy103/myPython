'''
将win10锁屏界面的壁纸全部加入壁纸库
'''
import os, shutil
from PIL import Image
from rename_wallpaper import rename

# win10锁屏壁纸存储地址
win_paper_path = r'C:\Users\cpyy103\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
# 本地壁纸库
wallpaper_path = os.getcwd() + '/wallpaper'

os.chdir(win_paper_path)

for image in os.listdir():
    shutil.copy(image, image + '.jpg')
    with Image.open(image + '.jpg') as img:
        size = img.size

    # 长宽合适的图片
    if size[0] > size[1]: 
        shutil.copyfile(image + '.jpg', os.path.join(wallpaper_path, image + '.jpg'))

    os.remove(image + '.jpg')
        
os.chdir(wallpaper_path)
rename(100000)
rename(1)

print('Done')




