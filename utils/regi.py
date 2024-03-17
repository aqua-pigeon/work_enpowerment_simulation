import math
import os
import time

from dotenv import load_dotenv

load_dotenv()  # .envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから

ARRIVE_1_INTERVAL = int(os.getenv("ARRIVE_1_INTERVAL"))
ARRIVE_2_INTERVAL = int(os.getenv("ARRIVE_2_INTERVAL"))
REGI_SERVICE_BASE_TIME = int(os.getenv("REGI_SERVICE_BASE_TIME"))


def regi_customer_arrive(status):
    # お客さんの増加
    if int(status["elapsed_time"]) % ARRIVE_1_INTERVAL == 0:
        if status["arrive_1_flag"] == True:
            status["waiting_regi"] += 1
            status["waiting_regi_unserviced"] += 1
            status["arrive_1_flag"] = False
    else:
        status["arrive_1_flag"] = True
    if int(status["elapsed_time"]) % ARRIVE_2_INTERVAL == 0:
        if status["arrive_2_flag"] == True:
            status["waiting_regi"] += 1
            status["waiting_regi_unserviced"] += 1
            status["arrive_2_flag"] = False
    else:
        status["arrive_2_flag"] = True
    return status


def regi_service(status):
    # レジの接客
    if (
        status["is_reg1_free"]
        and (status["waiting_regi"] - 1 + status["is_reg2_free"]) > 0
    ):  # レジ1が空いているかつ、待ち行列からレジ2の人数を引いた数が0より大きい場合
        status["regi_serviced_time"] += 1  # 何人目の処理中お客さんか
        if status["regi_serviced_time"] % 3 == 0:  # 3の倍数の場合
            status["regi1_time"] = (
                REGI_SERVICE_BASE_TIME * 2
            )  # レジ1の接客時間を2倍にする
        else:
            status["regi1_time"] = REGI_SERVICE_BASE_TIME
        status["regi1_start_time"] = time.time()  # レジ1の接客開始時間を現在時刻にする
        status["is_reg1_free"] = False  # レジ1が空いているか否かをFalseにする

    if (
        status["is_reg1_free"] == False
        and math.floor(time.time() - status["regi1_start_time"]) >= status["regi1_time"]
    ):  # レジ1の接客時間が経過した場合
        status["is_reg1_free"] = True  # レジ1が空いているか否かをTrueにする
        status["waiting_regi"] -= 1  # 待ち行列の人数を1減らす
        status["waiting_regi_unserviced"] -= 1  # メニューを渡されてない人を1減らす
        # メニューを渡されてない人が0より小さい場合,それ以上減らさないようにする
        if status["waiting_regi_unserviced"] < 0:
            status["waiting_regi_unserviced"] = 0
        if (
            status["regi1_time"] == REGI_SERVICE_BASE_TIME
        ):  # レジ1の接客時間が基本接客時間の場合
            status["waiting_bar"] += 1
        else:  # レジ1の接客時間が基本接客時間でない場合
            status["waiting_bar"] += 2

    # レジ2の接客
    if status["regi_baristaNum"] > 1:  # OSサポートが入っている場合
        if (
            status["is_reg2_free"] == True  # レジ2が空いている場合
            and (status["waiting_regi"] - 1 + status["is_reg1_free"])
            > 0  # 待ち行列からレジ1の人数を引いた数が0より大きい場合
        ):
            status["regi_serviced_time"] += 1  # 何人目の処理中お客さんか
            if status["regi_serviced_time"] % 3 == 0:
                status["regi2_time"] = REGI_SERVICE_BASE_TIME * 2
            else:
                status["regi2_time"] = REGI_SERVICE_BASE_TIME
                status["regi2_start_time"] = time.time()
                status["is_reg2_free"] = False

        if (
            status["is_reg2_free"] == False
            and math.floor(time.time() - status["regi2_start_time"])
            >= status["regi2_time"]
        ):  # レジ2の接客時間が経過した場合
            status["is_reg2_free"] = True  # レジ2が空いているか否かをTrueにする
            status["waiting_regi"] -= 1  # 待ち行列の人数を1減らす
            status["waiting_regi_unserviced"] -= 1
            # メニューを渡されてない人が0より小さい場合,それ以上減らさないようにする
            if status["waiting_regi_unserviced"] < 0:
                status["waiting_regi_unserviced"] = 0
            if status["regi2_time"] == REGI_SERVICE_BASE_TIME:
                status["waiting_bar"] += 1  # レジ2の接客時間が基本接客時間の場合
            else:
                status["waiting_bar"] += 2  # レジ2の接客時間が基本接客時間でない場合

    return status
