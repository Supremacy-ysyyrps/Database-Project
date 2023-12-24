from dal.database import db


# 操作成功，返回None；失败，返回异常
def insert(PR_ID, P_ID, PR_Num, PR_UnitPrice, PR_Date):
    sql = """
    insert into PurchaseRecord
    values(%s, %s, %s, %s, '%s')
    """ % (PR_ID, P_ID, PR_Num, PR_UnitPrice, PR_Date)
    return db.execute(sql)


# 操作成功，返回None；失败，返回异常
def delete(Type, ID):
    if Type == "PR_ID":
        sql = """
        delete from PurchaseRecord
        where PR_ID = %s
        """ % (ID)
    elif Type == "P_ID":
        sql = """
        delete from PurchaseRecord
        where P_ID = %s
        """ % (ID)
    return db.execute(sql)


# 操作成功，返回None；失败，返回异常
def update(pr_id, PR_ID, P_ID, PR_Num, PR_UnitPrice, PR_Date):
    sql = """
    update PurchaseRecord
    set PR_ID = %s, P_ID = %s, PR_Num = %s, PR_UnitPrice = %s, PR_Date = '%s'
    where PR_ID = %s
    """ % (PR_ID, P_ID, PR_Num, PR_UnitPrice, PR_Date, pr_id)
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_all():
    sql = """
    select *
    from PurchaseRecord
    order by P_ID, PR_ID
    """
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_by_pr_id(PR_ID):
    sql = """
    select *
    from PurchaseRecord
    where PR_ID = %s
    """ % (PR_ID)
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_by_p_id(P_ID):
    sql = """
    select *
    from PurchaseRecord
    where P_ID = %s
    order by PR_ID
    """ % (P_ID)
    return db.execute(sql)


# 操作成功，返回查询结果或空结果；失败，返回异常
def select_by_pr_date(PR_Date):
    sql = """
    select *
    from PurchaseRecord
    where PR_Date = '%s'
    order by P_ID, PR_ID
    """ % (PR_Date)
    return db.execute(sql)