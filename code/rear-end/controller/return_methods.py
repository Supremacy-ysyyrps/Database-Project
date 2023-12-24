from flask import jsonify
from bll.inventory_blo import warning


def return_method_select(rst):
    # 进行预警测试，返回值为预警信息或字符串"\n"
    warning_info = warning()
    # 返回字符串(或异常)表示没有查询结果(或失败)
    if isinstance(rst, str) or isinstance(rst, Exception):
        return jsonify({"error": True, "message": str(rst)})
    # 有结果返回结果
    else:
        return jsonify({
            "error": False,
            "message": warning_info,
            "result": rst
        })


def return_method_other(rst):
    # 进行预警测试，返回值为预警信息或字符串"\n"
    warning_info = warning()
    # 返回异常则表示执行失败
    if isinstance(rst, Exception):
        return jsonify({"error": True, "message": str(rst)})
    # 返回字符串表示执行成功
    elif isinstance(rst, str):
        return jsonify({"error": False, "message": rst + warning_info})
    # 这个应该不会有
    else:
        return jsonify({"error": True, "message": "我也不知到发生了什么错误"})