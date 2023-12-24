# Database-Project
大三上学期数据库系统大作业<br>
超市库存管理系统<br>
仅供学习使用<br>
***
代码在code文件夹下<br>
成品见 ```http://8.134.218.23:8080/```
|角色|账号|密码|
|---|---|---|
|管理员|manager|manager|
|进货员|buyer|buyer|
|售货员|seller|seller|
***
## 后端运行
使用pip3安装库 ```psycopg2``` ， ```flask``` 和 ```flask_cors```<br>
在 ```code/rear-end/dal/database.py``` 中设置数据库连接参数，指定数据库名，用户名，密码，主机名，端口号<br>
然后在 ```main``` 中指定后端服务器监听的IP地址 ```0.0.0.0``` 和端口号 ```8888```<br>
运行 ```main.py```<br>
***
## 前端运行
参考网上教程，安装vue<br><br>
根据后端服务器ip地址和端口号，修改 ```code\front-end\src\components\``` 中所有文件内部出现的URL，初始为 ```http://8.134.218.23:8888/``` ， 修改为后端服务器监听的IP地址和端口号<br><br>
安装依赖，以管理员身份打开终端，在项目目录下运行 ```npm install```<br>
运行时间较长，请耐心等待(貌似不需要安装全部依赖)<br><br>
运行web服务器 ```npm run serve``` 或 ```npm run dev```
