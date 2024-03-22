import json
import utils.regi as regi
import sys


def main():
    # コマンドライン引数を受け取る
    args = sys.argv
    if len(args) != 2:
        print("Usage: python analyze.py <log_folder_path>")
        sys.exit(1)
    log_folder_path = args[1]
    # jsonファイルを開く
    with open(log_folder_path, "r") as f:
        log = json.load(f)
    meta = log["meta"]
    body = log["body"]

    # body中のwaiting_regi_queueだけを取り出す
    waiting_regi_queue = [b["waiting_regi_queue"] for b in body]
    # print(waiting_regi_queue)
    # waiting_regi_queueから人数を取得する
    waiting_regi_num = []
    for i in waiting_regi_queue:
        waiting_regi_num.append(regi.get_waiting_regi_num(i))
    # print(waiting_regi_num)
    # waiting_regi_numの平均を求める
    waiting_regi_num_average = sum(waiting_regi_num) / len(waiting_regi_num)
    print("待ち人数平均",waiting_regi_num_average)

    # bodyの中のbar_baristaNumだけを取り出す
    bar_baristaNum = [b["bar_baristaNum"] for b in body]
    # print(bar_baristaNum)
    # bar_baristaNumの平均を求める
    bar_baristaNum_average = sum(bar_baristaNum) / len(bar_baristaNum)
    print("barバリスタ平均", bar_baristaNum_average)

    #waiting_barの平均を求める
    waiting_bar = [b["waiting_bar"] for b in body]
    waiting_bar_average = sum(waiting_bar) / len(waiting_bar)
    print("waiting_bar平均", waiting_bar_average)

    #最終的なservedを出力
    served = body[-1]["served"]
    print("served", served)

    #regi_baristaNumの平均を求める
    regi_baristaNum = [b["regi_baristaNum"] for b in body]
    regi_baristaNum_average = sum(regi_baristaNum) / len(regi_baristaNum)
    print("regi_baristaNum平均", regi_baristaNum_average)

    #drip_meterの平均を求める
    drip_meter = [b["drip_meter"] for b in body]
    drip_meter_average = sum(drip_meter) / len(drip_meter)
    print("drip_meter平均", drip_meter_average)

    #drip_coffee_sup_countを出力
    drip_coffee_sup_count = body[-1]["drip_coffee_sup_count"]
    print("drip補充回数", drip_coffee_sup_count)

    #drip_meterが0になった回数を出力
    drip_meter_zero_count = 0
    for i in drip_meter:
        if i == 0:
            drip_meter_zero_count += 1
    print("drip_meterが0になった回数", drip_meter_zero_count)

    #clickの回数を出力
    click = body[-1]["click"]
    print("click回数", click)

    #最大の待ち時間を出力
    max_waiting_time = max(waiting_regi_queue)
    







if __name__ == "__main__":
    main()
