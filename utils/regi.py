import math
import os
import time

from dotenv import load_dotenv

load_dotenv()

ARRIVE_1_INTERVAL = int(os.getenv("ARRIVE_1_INTERVAL"))
ARRIVE_2_INTERVAL = int(os.getenv("ARRIVE_2_INTERVAL"))
REGI_SERVICE_BASE_TIME = int(os.getenv("REGI_SERVICE_BASE_TIME"))

regi_customer_count = 0


def regi_customer_arrive(status):
    global regi_customer_count
    customer_dict = {
        "num": None,  # 1: お客さん1人, 2: お客さん2人
        "arrive_time": None,
        "menued": False,
        "regi_time": None,
        "leave_time": None,
    }
    if int(status["elapsed_time"]) % ARRIVE_1_INTERVAL == 0:
        if status["arrive_1_flag"]:
            regi_customer_count += 1
            if regi_customer_count % 3 == 0:
                customer_dict["num"] = 2
            else:
                customer_dict["num"] = 1
            customer_dict["arrive_time"] = time.time()
            status["waiting_regi_queue"].append(customer_dict)
            status["arrive_1_flag"] = False
    else:
        status["arrive_1_flag"] = True
    if int(status["elapsed_time"]) % ARRIVE_2_INTERVAL == 0:
        if status["arrive_2_flag"]:
            regi_customer_count += 1
            if regi_customer_count % 3 == 0:
                customer_dict["num"] = 2
            else:
                customer_dict["num"] = 1
            customer_dict["arrive_time"] = time.time()
            status["waiting_regi_queue"].append(customer_dict)
            status["arrive_2_flag"] = False
    else:
        status["arrive_2_flag"] = True
    return status


def regi_service(status):
    queue_length = len(status["waiting_regi_queue"])
    if status["regi1_customer"] == None:
        if queue_length > 0:
            status["regi1_customer"] = status["waiting_regi_queue"].pop(0)
            if status["regi1_customer"]["menued"] == False:
                status["regi1_time"] = (
                    REGI_SERVICE_BASE_TIME * status["regi1_customer"]["num"]
                )
            else:
                status["regi1_time"] = (
                    REGI_SERVICE_BASE_TIME * status["regi1_customer"]["num"] / 2
                )
            status["regi1_start_time"] = time.time()

    elif math.floor(time.time() - status["regi1_start_time"]) >= status["regi1_time"]:
        status["regi1_customer"]["regi_time"] = time.time()
        status["waiting_bar_queue"].append(status["regi1_customer"])
        status["regi1_customer"] = None

    queue_length = len(status["waiting_regi_queue"])
    if status["regi_baristaNum"] > 1:
        if status["regi2_customer"] == None and queue_length > 0:
            status["regi2_customer"] = status["waiting_regi_queue"].pop(0)
            if status["regi2_customer"]["menued"] == False:
                status["regi2_time"] = (
                    REGI_SERVICE_BASE_TIME * status["regi2_customer"]["num"]
                )
            else:
                status["regi2_time"] = (
                    REGI_SERVICE_BASE_TIME * status["regi2_customer"]["num"] / 2
                )
            status["regi2_start_time"] = time.time()

        if (
            status["regi2_customer"] != None
            and math.floor(time.time() - status["regi2_start_time"])
            >= status["regi2_time"]
        ):
            status["regi2_customer"]["regi_time"] = time.time()
            status["waiting_bar_queue"].append(status["regi2_customer"])
            status["regi2_customer"] = None

    return status


def get_waiting_regi_num(waiting_regi_queue):
    result = 0
    for i in waiting_regi_queue:
        result += i["num"]
    return result
