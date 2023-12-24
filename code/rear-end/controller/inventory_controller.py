from flask import Flask, request
import controller.return_methods as ret_m
import bll.inventory_blo as blo


def inventory_route(app: Flask):

    # 不实现
    @app.route("/inventory/add_inventory", methods=["GET", "POST"])
    def add_inventory():
        data = request.args
        P_ID = data.get("P_ID")
        I_Curstock = data.get("I_Curstock")
        I_Maxstock = data.get("I_Maxstock")
        I_Minstock = data.get("I_Minstock")
        rst = blo.add_inventory(P_ID, I_Curstock, I_Maxstock, I_Minstock)
        return ret_m.return_method_other(rst)

    # 不实现
    @app.route("/inventory/del_inventory", methods=["GET", "POST"])
    def del_inventory():
        data = request.args
        P_ID = data.get("P_ID")
        rst = blo.del_inventory(P_ID)
        return ret_m.return_method_other(rst)

    # 不实现
    @app.route("/inventory/set_inventory", methods=["GET", "POST"])
    def set_inventory():
        data = request.args
        p_id = data.get("p_id")
        I_Curstock = data.get("I_Curstock")
        I_Maxstock = data.get("I_Maxstock")
        I_Minstock = data.get("I_Minstock")
        rst = blo.set_inventory(p_id, p_id, I_Curstock, I_Maxstock, I_Minstock)
        return ret_m.return_method_other(rst)

    @app.route("/inventory/get_all_inventory", methods=["GET", "POST"])
    def get_all_inventory():
        rst = blo.get_all_inventory()
        return ret_m.return_method_select(rst)

    @app.route("/inventory/get_by_p_id_inventory", methods=["GET", "POST"])
    def get_by_p_id_inventory():
        data = request.args
        P_ID = data.get("P_ID")
        rst = blo.get_by_p_id_inventory(P_ID)
        return ret_m.return_method_select(rst)