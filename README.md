# tuple_label
标注服务的后台

本地安装mysql并手动创建一个mysql数据库并修改项目的配置文件
```
1.手动创建一个mysql的数据库，名为tuple_lable
2.把项目路径下的tuple_table/settings.py中的mysql数据库的用户名、密码进行修改
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "tuple_label",
            "USER": "xxx",
            "PASSWORD": "xxx",
            "HOST": "localhost",
            "PORT": 3306,
        }
    }
```
安装python3.8，pip3后安装依赖运行
```
#在本项目根目录下运行安装python的依赖包
pip3 install -r requirements.txt
# 建立本地库
python3 manage.py makemigrations
python3 manage.py migrate
# 本地运行
python3 manage.py runserver 0.0.0.0:8000
```

功能：
````
提供project项目表、label标签表、label_document标注表的基础增删改查接口
项目的整体导入、导出
````

接口示例(以project为例)：
```
# 获取project 列表
method: get
url: localhost:8000/api/project/
返回结果：
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "三元组标记",
                "description": "百度Ai比赛数据"
            },
            {
                "id": 2,
                "name": "project2",
                "description": "测试说明"
            }
        ]
    }

# 获取id 为1的project 
method: get
url:localhost:8000/api/project/1
返回结果：
    {
        "id": 1,
        "name": "三元组标记",
        "description": "百度Ai比赛数据"
    }

# 增加 project
method: post
url: localhost:8000/api/project/
json data:
{
    "id": 1,
    "name": "三元组标记",
    "description": "百度Ai比赛数据"
}

# 修改id 为1的project
method: post
url: localhost:8000/api/project/1
json data:
    {
        "id": 1,
        "name": "三元组标记modify",
        "description": "百度Ai比赛数据modify"
    }

# 删除id 为1的project 
method: delete
url:localhost:8000/api/project/1
```