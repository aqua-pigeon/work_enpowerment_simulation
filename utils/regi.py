import os

from dotenv import load_dotenv

load_dotenv()  # .envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから

ARRIVE_1_INTERVAL = os.getenv("ARRIVE_1_INTERVAL")
ARRIVE_2_INTERVAL = os.getenv("ARRIVE_2_INTERVAL")


def regi_customer_arrive(status):
    # お客さんの増加
    if status["elapsed_time"] % ARRIVE_1_INTERVAL == 0:
        if status["arrive_1_flag"] == True:
            status["waiting_regi"] += 1
            status["waiting_regi_unserviced"] += 1
            status["arrive_1_flag"] = False
    else:
        status["arrive_1_flag"] = True
    if status["elapsed_time"] % ARRIVE_2_INTERVAL == 0:
        if status["arrive_2_flag"] == True:
            status["waiting_regi"] += 1
            status["waiting_regi_unserviced"] += 1
            status["arrive_2_flag"] = False
    else:
        status["arrive_2_flag"] = True
    return status
