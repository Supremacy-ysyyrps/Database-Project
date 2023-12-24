from dal.database import db


def manager():
    sql = """
    reset role;
    """
    return db.execute(sql)


def buyer():
    sql = """
    set role buyer;
    """
    return db.execute(sql)


def seller():
    sql = """
    set role seller;
    """
    return db.execute(sql)