from dal.database import db


# 操作成功，返回None；失败，返回异常
def insert(P_ID, P_Name, P_Type):
    sql = """
    insert into Product
    values(%s, '%s', '%s')
    """ % (P_ID, P_Name, P_Type)
    return db.execute(sql)


# 操作成功，返回None；失败，返回异常
def delete(P_ID):
    sql = """
    delete from Product
    where P_ID = %s
    """ % (P_ID)
    return db.execute(sql)


# 操作成功，返回None；失败，返回异常
def update(p_id, P_ID, P_Name, P_Type):
    sql = """
    update Product
    set P_ID = %s, P_Name = '%s', P_Type = '%s'
    where P_ID = %s
    """ % (P_ID, P_Name, P_Type, p_id)
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_all():
    sql = """
    select *
    from Product
    order by P_ID
    """
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_by_p_id(P_ID):
    sql = """
    select *
    from Product
    where P_ID = %s
    """ % (P_ID)
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_by_p_name(P_Name):
    sql = """
    select *
    from Product
    where P_Name = '%s'
    order by P_ID
    """ % (P_Name)
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_by_p_type(P_Type):
    sql = """
    select *
    from Product
    where P_Type = '%s'
    order by P_ID
    """ % (P_Type)
    return db.execute(sql)