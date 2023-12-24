import dal.product_dao as dao


def add_product(P_ID, P_Name, P_Type):
    # 插入操作成功，返回None；失败，返回异常
    # 设置了触发器，在添加新商品信息后追加初始库存信息
    rst = dao.insert(P_ID, P_Name, P_Type)
    # 如果添加新商品信息时出现异常，返回异常，否则返回成功添加信息
    return rst if rst else "商品信息添加成功! 当前库存为0.\n"


def del_product(P_ID):
    # 删除操作成功，返回None；失败，返回异常
    # 其余表设置了级联删除，删除商品信息后对应元组也会删除
    rst = dao.delete(P_ID)
    # 如果删除商品信息时出现异常，返回异常，否则返回成功删除信息
    return rst if rst else "商品信息删除成功！\n"


def set_product(p_id, P_ID, P_Name, P_Type):
    # 更新操作成功，返回None；失败，返回异常
    rst = dao.update(p_id, P_ID, P_Name, P_Type)
    # 如果更新商品信息时出现异常，返回异常，否则返回成功更新信息
    return rst if rst else "商品信息更新成功！\n"


def get_all_product():
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_all()
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有商品信息！\n"


def get_by_p_id_product(P_ID):
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_by_p_id(P_ID)
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有P_ID为 %s 的商品信息！\n" % (P_ID)


def get_by_p_name_product(P_Name):
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_by_p_name(P_Name)
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有P_Name为 %s 的商品信息！\n" % (P_Name)


def get_by_p_type_product(P_Type):
    # 查询操作成功，返回查询结果或空结果；失败，返回异常
    rst = dao.select_by_p_type(P_Type)
    # 如果查询到元组或失败，返回对应结果，否则查询结果为空，返回信息
    return rst if rst else "没有P_Type为 %s 的商品信息！\n" % (P_Type)