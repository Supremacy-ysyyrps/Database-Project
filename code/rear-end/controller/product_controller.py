from flask import Flask, request
import controller.return_methods as ret_m
import bll.product_blo as blo


def product_route(app: Flask):

    @app.route("/product/add_product", methods=["GET", "POST"])
    def add_product():
        data = request.args
        P_ID = data.get("P_ID")
        P_Name = data.get("P_Name")
        P_Type = data.get("P_Type")
        rst = blo.add_product(P_ID, P_Name, P_Type)
        return ret_m.return_method_other(rst)

    @app.route("/product/del_product", methods=["GET", "POST"])
    def del_product():
        data = request.args
        P_ID = data.get("P_ID")
        rst = blo.del_product(P_ID)
        return ret_m.return_method_other(rst)

    @app.route("/product/set_product", methods=["GET", "POST"])
    def set_product():
        data = request.args
        p_id = data.get("p_id")
        P_Name = data.get("P_Name")
        P_Type = data.get("P_Type")
        rst = blo.set_product(p_id, p_id, P_Name, P_Type)
        return ret_m.return_method_other(rst)

    @app.route("/product/get_all_product", methods=["GET", "POST"])
    def get_all_product():
        rst = blo.get_all_product()
        return ret_m.return_method_select(rst)

    @app.route("/product/get_by_p_id_product", methods=["GET", "POST"])
    def get_by_p_id_product():
        data = request.args
        P_ID = data.get("P_ID")
        rst = blo.get_by_p_id_product(P_ID)
        return ret_m.return_method_select(rst)

    @app.route("/product/get_by_p_name_product", methods=["GET", "POST"])
    def get_by_p_name_product():
        data = request.args
        P_Name = data.get("P_Name")
        rst = blo.get_by_p_name_product(P_Name)
        return ret_m.return_method_select(rst)

    @app.route("/product/get_by_p_type_product", methods=["GET", "POST"])
    def get_by_p_type_product():
        data = request.args
        P_Type = data.get("P_Type")
        rst = blo.get_by_p_type_product(P_Type)
        return ret_m.return_method_select(rst)