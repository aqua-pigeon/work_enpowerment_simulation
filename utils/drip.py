import math
import os
import time

from dotenv import load_dotenv

load_dotenv()  # .envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから

DRIP_DECREASE = int(os.getenv("DRIP_DECREASE"))
DRIP_TIME = int(os.getenv("DRIP_TIME"))

def drip(status):
    if status["elapsed_time"]%DRIP_DECREASE==0:
        if status["drip_meter"]>0:
            status["drip_meter"]-=1
    if 
        status["os_cool_time"]=20
        status["drip_coffee"]+=1
        status["drip_meter"]=5

