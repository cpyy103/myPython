# wallpaper

win10设置桌面壁纸幻灯片放映，手动建立一个壁纸图片库

图片库中壁纸为自己手动挑选下载，未使用爬虫

win10的锁屏壁纸也挺好看（会自动更新），直接当做壁纸

图片名字乱七八糟，以数字编号重命名（随机）

| 项目                      | 描述                                                       |
| ------------------------- | ---------------------------------------------------------- |
| wallpaper                 | 图片库，win10设置背景幻灯片放映，并选择该图片库            |
| rename_wallpaper.py       | 将自己下载的壁纸图片重命名                                 |
| rename_paper_in_assets.py | 将win10锁屏壁纸元素转图片格式（win10内部不以图片格式存储） |
| main.py                   | 将win10锁屏壁纸全加入壁纸库                                |

使用前需配置代码中相关信息



喜欢手动挑选壁纸

- 从网上下载喜欢的放入图片库

- 重命名图片库中图片（rename_wallpaper.py）

或者

- 将win10壁纸手动转换为jpg（rename_paper_in_assets.py）
- 然后挑选喜欢的放入图片库
- 将win10锁屏壁纸存储文件夹下生成的图片删除
- 重命名图片库中图片（rename_wallpaper.py）