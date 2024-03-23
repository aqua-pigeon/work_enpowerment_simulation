import math
import os
import time

from dotenv import load_dotenv

load_dotenv()  # .envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから

BAR_SERVICE_BASE_TIME = int(os.getenv("BAR_SERVICE_BASE_TIME"))

bar_last_checked_time = 0


def bar_service(status):
    global bar_last_checked_time
    # ドリンクの作成
    if (
        status["is_bar_free"] and len(status["waiting_bar_queue"]) > 0
    ):  # バリスタが空いているかつ、待ち行列が0より大きい場合
        status["bar_start_time"] = time.time()  # バリスタの接客開始時間を現在時刻にする
        status["is_bar_free"] = False  # バリスタが空いているか否かをFalseにする
    if status["is_bar_free"] == False:  # ドリンク作成中
        if status["drip_meter"] < 1:
            status["bar_start_time"] += time.time() - bar_last_checked_time
        if (
            math.floor(time.time() - status["bar_start_time"])
            >= BAR_SERVICE_BASE_TIME
            / status["bar_baristaNum"]
            * status["waiting_bar_queue"][0]["num"]
        ):  # ドリンク作成完了時 バリスタ２人の場合はドリンク作成時間が半減
            status["is_bar_free"] = True  # バリスタが空いているか否かをTrueにする
            status["waiting_bar_queue"][0][
                "leave_time"
            ] = time.time()  # ドリンク作成完了時間を記録
            status["served"].append(
                status["waiting_bar_queue"].pop(0)
            )  # 待ち行列から先頭のお客さんを取り出し、接客済みリストに追加

    bar_last_checked_time = time.time()
    return status


def get_waiting_num(waiting_queue):
    result = 0
    for i in waiting_queue:
        result += i["num"]
    return result
