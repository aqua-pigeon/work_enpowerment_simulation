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
    if int(status["elapsed_time"]) % ARRIVE_1_INTERVAL == 0:
        if status["arrive_1_flag"]:
            regi_customer_count += 1
            if regi_customer_count % 3 == 0:
                status["waiting_regi_queue"].append(2)
            else:
                status["waiting_regi_queue"].append(1)
            status["arrive_1_flag"] = False
    else:
        status["arrive_1_flag"] = True
    if int(status["elapsed_time"]) % ARRIVE_2_INTERVAL == 0:
        if status["arrive_2_flag"]:
            regi_customer_count += 1
            if regi_customer_count % 3 == 0:
                status["waiting_regi_queue"].append(2)
            else:
                status["waiting_regi_queue"].append(1)
            status["arrive_2_flag"] = False
    else:
        status["arrive_2_flag"] = True
    return status


def regi_service(status):
    queue_length = len(status["waiting_regi_queue"])
    if status["regi1_customer"] == 0:
        if queue_length > 0:
            status["regi1_customer"] = status["waiting_regi_queue"].pop(0)
            if (
                status["regi1_customer"] == 0
                or status["regi1_customer"] == 1
                or status["regi1_customer"] == 2
            ):
                status["regi1_time"] = REGI_SERVICE_BASE_TIME * (
                    status["regi1_customer"] % 3
                )
            else:
                status["regi1_time"] = REGI_SERVICE_BASE_TIME * (
                    status["regi1_customer"] % 3 * (5 / 10)
                )
            status["regi1_start_time"] = time.time()

    if (
        status["regi1_customer"] > 0
        and math.floor(time.time() - status["regi1_start_time"]) >= status["regi1_time"]
    ):

        status["waiting_bar"] += status["regi1_customer"] % 3
        status["regi1_customer"] = 0

    queue_length = len(status["waiting_regi_queue"])
    if status["regi_baristaNum"] > 1:
        if status["regi2_customer"] == 0 and queue_length > 0:
            status["regi2_customer"] = status["waiting_regi_queue"].pop(0)
            if (
                status["regi2_customer"] == 0
                or status["regi2_customer"] == 1
                or status["regi2_customer"] == 2
            ):
                status["regi2_time"] = REGI_SERVICE_BASE_TIME * (
                    status["regi2_customer"] % 3
                )
            else:
                status["regi2_time"] = REGI_SERVICE_BASE_TIME * (
                    status["regi2_customer"] % 3 * (5 / 10)
                )
            status["regi2_start_time"] = time.time()

        if (
            status["regi2_customer"] > 0
            and math.floor(time.time() - status["regi2_start_time"])
            >= status["regi2_time"]
        ):
            status["waiting_bar"] += status["regi2_customer"] % 3
            status["regi2_customer"] = 0

    return status


def get_waiting_regi_num(waiting_regi_queue):
    result = 0
    for i in waiting_regi_queue:
        result += i % 3
    return result
