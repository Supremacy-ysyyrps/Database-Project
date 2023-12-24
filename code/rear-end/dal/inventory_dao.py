from dal.database import db


# 操作成功，返回None；失败，返回异常
def insert(P_ID, I_Curstock, I_Maxstock, I_Minstock):
    sql = """
    insert into Inventory
    values(%s, %s, %s, %s)
    """ % (P_ID, I_Curstock, I_Maxstock, I_Minstock)
    return db.execute(sql)


# 操作成功，返回None；失败，返回异常
def delete(P_ID):
    sql = """
    delete from Inventory
    where P_ID = %s
    """ % (P_ID)
    return db.execute(sql)


# 操作成功，返回None；失败，返回异常
def update(p_id, P_ID, I_Curstock, I_Maxstock, I_Minstock):
    sql = """
    update Inventory
    set P_ID = %s, I_Curstock = %s, I_Maxstock = %s, I_Minstock = %s
    where P_ID = %s
    """ % (P_ID, I_Curstock, I_Maxstock, I_Minstock, p_id)
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_all():
    sql = """
    select *
    from Inventory
    order by P_ID
    """
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_by_p_id(P_ID):
    sql = """
    select *
    from Inventory
    where P_ID = %s
    """ % (P_ID)
    return db.execute(sql)