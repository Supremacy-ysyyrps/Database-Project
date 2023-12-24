from flask import Flask
from flask_cors import CORS
from controller.role_controller import role_route
from controller.product_controller import product_route
from controller.purchase_controller import purchase_route
from controller.sales_controller import sales_route
from controller.inventory_controller import inventory_route


# 中枢控制器
class App:
    # 输入主模块名，创建Flask对象，并使用URL注册视图函数
    def __init__(self, name) -> None:
        # 创建Flask对象并初始化
        self.app = Flask(name)
        # 为应用程序初始化跨源资源共享
        self.cors = CORS(self.app)
        # 通过装饰器定义URL
        # 然后定义处理对该URL的请求的视图函数，并返回json格式数据
        role_route(self.app)
        product_route(self.app)
        purchase_route(self.app)
        sales_route(self.app)
        inventory_route(self.app)
        print("Successfully create an app!")

    # 指定self.app在特定端口运行
    def run(self, host, port):
        self.app.run(host=host, port=port)

    def __del__(self) -> None:
        print("Successfully destroy the app!")