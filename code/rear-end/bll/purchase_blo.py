import dal.purchase_dao as dao


def add_purchase(PR_ID, P_ID, PR_Num, PR_UnitPrice, PR_Date):
    # 插入操作成功，返回None；失败，返回异常
    # 设置了触发器，在添加进货信息后自动更新库存信息
    rst = dao.insert(PR_ID, P_ID, PR_Num, PR_UnitPrice, PR_Date)
    # 有异常返回异常，否则返回成功信息
    return rst if rst else "进货信息添加成功！\n"


def del_purchase(Type, ID):
    # 删除操作成功，返回None；失败，返回异常
    # 设置了触发器，在删除进货信息后自动更新库存信息
    rst = dao.delete(Type, ID)
    # 有异常返回异常，否则返回成功信息
    return rst if rst else "进货信息删除成功！\n"


def set_purchase(pr_id, PR_ID, P_ID, PR_Num, PR_UnitPrice, PR_Date):
    # 更新操作成功，返回None；失败，返回异常
    rst = dao.update(pr_id, PR_ID, P_ID, PR_Num, PR_UnitPrice, PR_Date)
    # 有异常返回异常，否则返回成功信息
    return rst if rst else "进货信息更新成功！\n"


def get_all_purchase():
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_all()
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有进货信息！\n"


def get_by_pr_id_purchase(PR_ID):
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_by_pr_id(PR_ID)
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有PR_ID为 %s 的进货信息！\n" % (PR_ID)


def get_by_p_id_purchase(P_ID):
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_by_p_id(P_ID)
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有P_ID为 %s 的进货信息！\n" % (P_ID)


def get_by_pr_date_purchase(PR_Date):
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_by_pr_date(PR_Date)
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有PR_Date为 %s 的进货信息！\n" % (PR_Date)