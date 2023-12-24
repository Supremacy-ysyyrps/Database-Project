from dal.database import db


# 操作成功，返回None；失败，返回异常
def insert(SR_ID, P_ID, SR_Num, SR_UnitPrice, SR_Date):
    sql = """
    insert into SalesRecord
    values(%s, %s, %s, %s, '%s')
    """ % (SR_ID, P_ID, SR_Num, SR_UnitPrice, SR_Date)
    return db.execute(sql)


# 操作成功，返回None；失败，返回异常
def delete(Type, ID):
    if Type == "SR_ID":
        sql = """
        delete from SalesRecord
        where SR_ID = %s
        """ % (ID)
    elif Type == "P_ID":
        sql = """
        delete from SalesRecord
        where P_ID = %s
        """ % (ID)
    return db.execute(sql)


# 操作成功，返回None；失败，返回异常
def update(sr_id, SR_ID, P_ID, SR_Num, SR_UnitPrice, SR_Date):
    sql = """
    update SalesRecord
    set SR_ID = %s, P_ID = %s, SR_Num = %s, SR_UnitPrice = %s, SR_Date = '%s'
    where SR_ID = %s
    """ % (SR_ID, P_ID, SR_Num, SR_UnitPrice, SR_Date, sr_id)
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_all():
    sql = """
    select *
    from SalesRecord
    order by P_ID, SR_ID
    """
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_by_sr_id(SR_ID):
    sql = """
    select *
    from SalesRecord
    where SR_ID = %s
    """ % (SR_ID)
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_by_p_id(P_ID):
    sql = """
    select *
    from SalesRecord
    where P_ID = %s
    order by SR_ID
    """ % (P_ID)
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_by_sr_date(SR_Date):
    sql = """
    select *
    from SalesRecord
    where SR_Date = '%s'
    order by P_ID, SR_ID
    """ % (SR_Date)
    return db.execute(sql)
