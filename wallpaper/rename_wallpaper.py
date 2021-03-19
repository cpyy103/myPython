'''
修改壁纸的名字

随机打乱壁纸
将壁纸名字改为数字，并递增
'''
import os
import random

wallpaper_path = os.getcwd() + '/wallpaper'
TempNum = 10000


def rename(start):
    files = os.listdir(wallpaper_path)
    random.shuffle(files)  # 有序列表变无序，在原来列表上修改
    for i, f in enumerate(files, start=start):
        suffix = '.' + f.split('.')[-1]
        os.rename(f, str(i) + suffix)


if __name__ == '__main__':
    os.chdir(wallpaper_path)
    rename(TempNum)
    rename(1)
    print('Done')

