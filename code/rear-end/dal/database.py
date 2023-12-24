import psycopg2


class Database:
    # 构造函数，传入数据库连接参数
    def __init__(self, db, u, pw, h, p) -> None:
        # 使用psycopy2.connect()方法连接到postgresql数据库
        self.con = psycopg2.connect(database=db,
                                    user=u,
                                    password=pw,
                                    host=h,
                                    port=p)
        # 创建游标，用于执行SQL语句，返回查询结果
        self.cur = self.con.cursor()
        print("Successfully connected to database!")

    # 执行函数，输入SQL语句执行查询，返回查询结果、异常或None
    def execute(self, command):
        try:
            # 通过调用cur.execute()方法对数据库进行操作
            self.cur.execute(command)
        # 如果出现执行异常（如违反约束等），回滚事务后返回异常
        except Exception as e:
            # 使用con.rollback()回滚事务，保护数据库一致性
            self.con.rollback()
            # 返回异常
            return e
        # 若没有执行异常，取回查询结果后提交事务
        else:
            try:
                # 如果有查询结果，返回查询结果
                return self.cur.fetchall()
            # 如果没有返回结果（如增删改），则捕捉抛出的异常，返回None
            except Exception as e:
                return None
            finally:
                # 使用con.commit()提交事务，使数据持久化
                self.con.commit()

    # 析构函数，最后使用close()关闭数据库
    def __del__(self) -> None:
        self.con.close()
        print("Successfully disconnected from database!")


# 设置数据库连接参数，指定数据库名，用户名，密码，主机名，端口号
database = "超市库存管理系统"
user = "postgres"
password = "password"
host = "localhost"
port = "5432"
# 设置参数，建立数据库连接
db = Database(database, user, password, host, port)