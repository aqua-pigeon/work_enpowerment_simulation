import os

from dotenv import load_dotenv

load_dotenv()  # .envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから

DRIP_DECREASE = int(os.getenv("DRIP_DECREASE"))
DRIP_TIME = int(os.getenv("DRIP_TIME"))

drip_decrease_flag = True


def drip_decrease(status):
    global drip_decrease_flag
    if (
        int(status["elapsed_time"]) % DRIP_DECREASE == 0
    ):  # 10秒経過するごとにドリップの残量を減らす. ただし、前回の減少から10秒経過していない場合は減少しない
        if drip_decrease_flag == False:
            if status["drip_meter"] > 0:
                status["drip_meter"] -= 1
            drip_decrease_flag = True
    else:
        drip_decrease_flag = False
    return status
