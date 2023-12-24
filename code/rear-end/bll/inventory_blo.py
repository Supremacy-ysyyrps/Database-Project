import dal.inventory_dao as dao


# 预警函数，检查数据，查看是否达到预警线
# 如果商品的库存量过多或过少，发出预警信息，否则返回字符串"\n"
def warning():
    rst = dao.select_all()
    warning_info = "\n"
    for tup in rst:
        if tup[1] > tup[2] - 10:
            warning_info += "商品 %s 库存已超出警戒值, 该商品当前库存: %s, 最大库存: %s.\n" % (tup[0], tup[1], tup[2])
        elif tup[1] < tup[3] + 10:
            warning_info += "商品 %s 库存已低于警戒值, 该商品当前库存: %s, 最小库存: %s.\n" % (tup[0], tup[1], tup[3])
    return warning_info


def add_inventory(P_ID, I_Curstock, I_Maxstock, I_Minstock):
    # 插入操作成功，返回None；失败，返回异常
    rst = dao.insert(P_ID, I_Curstock, I_Maxstock, I_Minstock)
    # 如果失败，返回异常信息，否则返回成功信息
    return rst if rst else "库存信息添加成功！\n"


def del_inventory(P_ID):
    # 删除操作成功，返回None；失败，返回异常
    rst = dao.delete(P_ID)
    # 如果失败，返回异常信息，否则返回成功信息
    return rst if rst else "库存信息删除成功！\n"


def set_inventory(p_id, P_ID, I_Curstock, I_Maxstock, I_Minstock):
    # 更新操作成功，返回None；失败，返回异常
    rst = dao.update(p_id, P_ID, I_Curstock, I_Maxstock, I_Minstock)
    # 如果失败，返回异常信息，否则返回成功信息
    return rst if rst else "库存信息更新成功！\n"


def get_all_inventory():
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_all()
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有库存信息！\n"


def get_by_p_id_inventory(P_ID):
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_by_p_id(P_ID)
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有P_ID为 %s 的库存信息！\n" % (P_ID)
