from dal.database import db
from sql.sql import sql_init, sql_rebuild, sql_insert_all, sql_select_all
from controller.central_control import App


# 新建
def init():
    print(db.execute(sql_init))


# 重置
def rebuild():
    print(db.execute(sql_rebuild))


# 插入测试元组
def init():
    for sql in sql_insert_all:
        print(db.execute(sql))


# 查询所有表
def all():
    for sql in sql_select_all:
        print()
        for tup in db.execute(sql):
            for ele in tup:
                print(ele, end="\t")
            print()


# 运行
# init()
rebuild()
init()
all()
app = App(__name__)
app.run("0.0.0.0", 8888)