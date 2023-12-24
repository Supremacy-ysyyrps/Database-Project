from flask import Flask, request, jsonify
import controller.return_methods as ret_m
import bll.role_blo as blo


def role_route(app: Flask):

    @app.route("/role", methods=["GET", "POST"])
    def set_role():
        data = request.get_json()
        role = data.get("role")
        username = data.get("username")
        password = data.get("password")
        global now_role
        if role == username == password == "manager":
            now_role = "管理员"
            rst = blo.manager()
        elif role == username == password == "buyer":
            now_role = "进货员"
            rst = blo.buyer()
        elif role == username == password == "seller":
            now_role = "售货员"
            rst = blo.seller()
        else:
            return jsonify({"error": True, "message": "请检查您的输入"})
        return jsonify({"error": False, "message": "登录成功"})
    
    @app.route("/now_role", methods=["GET", "POST"])
    def get_role():
        return jsonify({
            "message": now_role
        })