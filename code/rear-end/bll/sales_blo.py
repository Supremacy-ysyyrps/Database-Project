import dal.sales_dao as dao


def add_sales(SR_ID, P_ID, SR_Num, SR_UnitPrice, SR_Date):
    # 插入操作成功，返回None；失败，返回异常
    # 设置了触发器，在添加销售信息后自动更新库存信息
    rst = dao.insert(SR_ID, P_ID, SR_Num, SR_UnitPrice, SR_Date)
    # 有异常返回异常，否则返回成功信息
    return rst if rst else "销售信息添加成功！\n"


def del_sales(Type, ID):
    # 删除操作成功，返回None；失败，返回异常
    # 设置了触发器，在删除销售信息后自动更新库存信息
    rst = dao.delete(Type, ID)
    # 有异常返回异常，否则返回成功信息
    return rst if rst else "销售信息删除成功！\n"


def set_sales(sr_id, SR_ID, P_ID, SR_Num, SR_UnitPrice, SR_Date):
    # 更新操作成功，返回None；失败，返回异常
    rst = dao.update(sr_id, SR_ID, P_ID, SR_Num, SR_UnitPrice, SR_Date)
    # 有异常返回异常，否则返回成功信息
    return rst if rst else "销售信息更新成功！\n"


def get_all_sales():
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_all()
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有销售信息！\n"


def get_by_sr_id_sales(SR_ID):
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_by_sr_id(SR_ID)
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有SR_ID为 %s 的销售信息！\n" % (SR_ID)


def get_by_p_id_sales(P_ID):
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_by_p_id(P_ID)
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有P_ID为 %s 的销售信息！\n" % (P_ID)


def get_by_sr_date_sales(SR_Date):
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_by_sr_date(SR_Date)
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有SR_Date为 %s 的销售信息！\n" % (SR_Date)