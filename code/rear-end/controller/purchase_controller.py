from flask import Flask, request
import controller.return_methods as ret_m
import bll.purchase_blo as blo


def purchase_route(app: Flask):

    @app.route("/purchase/add_purchase", methods=["GET", "POST"])
    def add_purchase():
        data = request.args
        PR_ID = data.get("PR_ID")
        P_ID = data.get("P_ID")
        PR_Num = data.get("PR_Num")
        PR_UnitPrice = data.get("PR_UnitPrice")
        PR_Date = data.get("PR_Date")
        rst = blo.add_purchase(PR_ID, P_ID, PR_Num, PR_UnitPrice, PR_Date)
        return ret_m.return_method_other(rst)

    @app.route("/purchase/del_purchase", methods=["GET", "POST"])
    def del_purchase():
        data = request.args
        Type = data.get("Type")
        ID = data.get("ID")
        rst = blo.del_purchase(Type, ID)
        return ret_m.return_method_other(rst)

    # 不实现
    @app.route("/purchase/set_purchase", methods=["GET", "POST"])
    def set_purchase():
        data = request.args
        pr_id = data.get("pr_id")
        P_ID = data.get("P_ID")
        PR_Num = data.get("PR_Num")
        PR_UnitPrice = data.get("PR_UnitPrice")
        PR_Date = data.get("PR_Date")
        rst = blo.set_purchase(pr_id, pr_id, P_ID, PR_Num, PR_UnitPrice, PR_Date)
        return ret_m.return_method_other(rst)

    @app.route("/purchase/get_all_purchase", methods=["GET", "POST"])
    def get_all_purchase():
        rst = blo.get_all_purchase()
        return ret_m.return_method_select(rst)

    @app.route("/purchase/get_by_pr_id_purchase", methods=["GET", "POST"])
    def get_by_pr_id_purchase():
        data = request.args
        PR_ID = data.get("PR_ID")
        rst = blo.get_by_pr_id_purchase(PR_ID)
        return ret_m.return_method_select(rst)

    @app.route("/purchase/get_by_p_id_purchase", methods=["GET", "POST"])
    def get_by_p_id_purchase():
        data = request.args
        P_ID = data.get("P_ID")
        rst = blo.get_by_p_id_purchase(P_ID)
        return ret_m.return_method_select(rst)

    @app.route("/purchase/get_by_pr_date_purchase", methods=["GET", "POST"])
    def get_by_pr_date_purchase():
        data = request.args
        PR_Date = data.get("PR_Date")
        rst = blo.get_by_pr_date_purchase(PR_Date)
        return ret_m.return_method_select(rst)