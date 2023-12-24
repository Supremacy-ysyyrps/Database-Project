from flask import Flask, redirect, url_for, request
import controller.return_methods as ret_m
import bll.sales_blo as blo


def sales_route(app: Flask):

    @app.route("/sales/add_sales", methods=["GET", "POST"])
    def add_sales():
        data = request.args
        SR_ID = data.get("SR_ID")
        P_ID = data.get("P_ID")
        SR_Num = data.get("SR_Num")
        SR_UnitPrice = data.get("SR_UnitPrice")
        SR_Date = data.get("SR_Date")
        rst = blo.add_sales(SR_ID, P_ID, SR_Num, SR_UnitPrice, SR_Date)
        return ret_m.return_method_other(rst)

    @app.route("/sales/del_sales", methods=["GET", "POST"])
    def del_sales():
        data = request.args
        Type = data.get("Type")
        ID = data.get("ID")
        rst = blo.del_sales(Type, ID)
        return ret_m.return_method_other(rst)

    # 不实现
    @app.route("/sales/set_sales", methods=["GET", "POST"])
    def set_sales():
        data = request.args
        sr_id = data.get("sr_id")
        P_ID = data.get("P_ID")
        SR_Num = data.get("SR_Num")
        SR_UnitPrice = data.get("SR_UnitPrice")
        SR_Date = data.get("SR_Date")
        rst = blo.set_sales(sr_id, sr_id, P_ID, SR_Num, SR_UnitPrice, SR_Date)
        return ret_m.return_method_other(rst)

    @app.route("/sales/get_all_sales", methods=["GET", "POST"])
    def get_all_sales():
        rst = blo.get_all_sales()
        return ret_m.return_method_select(rst)

    @app.route("/sales/get_by_sr_id_sales", methods=["GET", "POST"])
    def get_by_sr_id_sales():
        data = request.args
        SR_ID = data.get("SR_ID")
        rst = blo.get_by_sr_id_sales(SR_ID)
        return ret_m.return_method_select(rst)

    @app.route("/sales/get_by_p_id_sales", methods=["GET", "POST"])
    def get_by_p_id_sales():
        data = request.args
        P_ID = data.get("P_ID")
        rst = blo.get_by_p_id_sales(P_ID)
        return ret_m.return_method_select(rst)

    @app.route("/sales/get_by_sr_date_sales", methods=["GET", "POST"])
    def get_by_sr_date_sales():
        data = request.args
        SR_Date = data.get("SR_Date")
        rst = blo.get_by_sr_date_sales(SR_Date)
        return ret_m.return_method_select(rst)