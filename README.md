# PhotOasis

## What I want
旅行积累了大量的照片，但是电子存储就很难让孩子们看到。
现有开源的图片系统也太复杂，所以想自己弄一个简简单单用来展示照片的网站就好了。

具体来说:
1. 可以读取本地的文件夹生成album
2. 图片展示用类似Pinterest的瀑布流方式

# 设定

在`global_variables.py`里设定路径：
- `path`: 小照片的地址，用于在瀑布流展示
- `big`: 大照片地址，用户点击照片的时候看大图用
- `original`: 原始图片
- `password`: admin页面的认证密码

# 使用

1. 按照相册的需求分文件夹，文件夹的命名规则参考`<album id>_<album name>`这样的格式，比如`001_theFirstAlbum`
2. 把需要展示的文件夹放在`original`文件夹里，默认地址为`photo/photo_original`
3. 修改`global_variables.py`里的路径，如果没有修改的话就不用动就行
4. 修改`global_variables.py`里的密码，如果没有修改的话就不用动就行
5. 准备处理图片，这一步会调用一个python程序，把`original`文件夹里的大图片压缩转化到`path`和`big`文件夹，命令`python3 photo_handler.py`
6. 启动服务 `python3 app.py`
7. 打开管理页面 `http://127.0.0.1:15001/admin/`，输入密码登录
8. 点击`扫描文件夹`,更新相册内容
9. 点击`Toggle Display`来切换这个相册显示或者不显示
10. 如果希望修改相册显示的名字，可以打开本地的`folders.json`，找到相应的相册，修改`name`这个项目就行，然后回到`admin`重新`扫描文件夹`，这个操作不会影响文件夹，只会修改显示的名字
11. 打开相册页面，开始使用吧 `http://127.0.0.1:15001/`


# 项目结构
```
- photoasis
    L app.py # 主入口，从这里启动
    L photo_handler.py # 处理original图片进行压缩
    L global_variables.py # 定义路径和密码
    L index.py # 主页入口，显示相册列表
    L album.py # 相册页面，显示相册内的图片
    L admin.py # 管理入口，管理相册是否展示
    L folder_action.py # 文件夹的读取操作
    L folders.json # 相册(文件夹)列表管理，自动生成，可以手动进去修改相册名 `name`
    L run.sh # 合并处理图片和启动服务的脚本
    L templates　# 各个页面的静态文件
        L index.html # 主页
        L admin.html # 管理页
        L album.html # 相册页
        L login.html # 登录页
    L photo # 图片文件夹
        L photo_original # 默认的原图片文件夹，可以在global_variables.py里修改这个地址
        L photo_big # 自动生成，存储大图片
        L photo_small # 自动生成，存储小图片
```
# folder.json

```
[
    {
        "id": 0, 
        "path": "0_default",
        "name": "default",
        "display": false
    }
]
```

## 版本更新记录

### v1.01
1. 新增了制作docker镜像需要的`dockerfile`和`requirements.txt`
2. docker相关内容可以看博客：[自制Docker镜像Photoasis](https://blog.yakumo2.uk/2024/03/29/2024/20240329_DockerPhotoasis/)

### v0.2

1. 分拆了不同功能的python文件
2. 添加了admin的页面，可以管理哪些文件夹展示，哪些不展示
3. 添加了admin页面的认证，需要输入密码(设定方法见后面）