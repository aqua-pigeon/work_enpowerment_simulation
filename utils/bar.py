import math
import os
import time

from dotenv import load_dotenv

load_dotenv()  # .envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから

BAR_SERVICE_BASE_TIME = int(os.getenv("BAR_SERVICE_BASE_TIME"))


def bar_service(status):
    # ドリンクの作成
    if (
        status["is_bar_free"] and status["waiting_bar"] > 0
    ):  # バリスタが空いているかつ、待ち行列が0より大きい場合
        status["bar_start_time"] = time.time()  # バリスタの接客開始時間を現在時刻にする
        status["is_bar_free"] = False  # バリスタが空いているか否かをFalseにする
    if (
        status["is_bar_free"] == False
        and math.floor(time.time() - status["bar_start_time"])
        >= BAR_SERVICE_BASE_TIME
        / status["bar_baristaNum"]  # バリスタ２人の場合はドリンク作成時間が半減
    ):  # ドリンク作成完了時
        status["is_bar_free"] = True  # バリスタが空いているか否かをTrueにする
        status["waiting_bar"] -= 1  # 待ち行列の人数を1減らす
        status["served"] += 1  # ドリンクを作成した人数を1増やす

    return status
