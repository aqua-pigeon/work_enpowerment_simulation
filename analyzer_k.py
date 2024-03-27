import json
import sys

import utils.regi as regi


def get_log_file_path():
    # コマンドライン引数を受け取る
    args = sys.argv
    if len(args) != 2:
        print("Usage: python analyze.py <log_file_path>")
        sys.exit(1)
    log_file_path = args[1]
    return log_file_path


def get_log_data(log_file_path):
    # jsonファイルを開く
    with open(log_file_path, "r") as f:
        log = json.load(f)
    meta = log["meta"]  # logデータ内のmetaデータを取得
    body = log["body"]  # logデータ内のbodyデータを取得
    result = log["result"]  # logデータ内のresultデータを取得
    return meta, body, result


def analyze_body(analyzed, body):
    analyzed["body_length"] = len(body)  # bodyの長さを出力
    ave_bar_baristaNum = 0
    ave_regi_baristaNum = 0
    ave_drip_baristaNum = 0
    ave_waiting_regi = 0
    ave_waiting_bar = 0
    ave_drip_meter = 0
    ave_arrive_1_flag = 0
    ave_arrive_2_flag = 0
    analyzed["drip_coffee_sup_count"] = body[-1]["drip_coffee_sup_count"]
    analyzed["click"] = body[-1]["click"]
    drip_zero_count = 0

    # 各要素の処理
    for i in body:
        ave_bar_baristaNum += i["bar_baristaNum"]
        ave_regi_baristaNum += i["regi_baristaNum"]
        ave_drip_baristaNum += i["drip_baristaNum"]
        ave_waiting_regi += regi.get_waiting_regi_num(i["waiting_regi_queue"])
        ave_waiting_bar += regi.get_waiting_regi_num(i["waiting_bar_queue"])
        ave_drip_meter += i["drip_meter"]
        ave_arrive_1_flag += i["arrive_1_flag"]
        ave_arrive_2_flag += i["arrive_2_flag"]
        if i["drip_meter"] == 0:
            drip_zero_count += 1

    # 各要素の平均を求める
    analyzed["ave_bar_baristaNum"] = ave_bar_baristaNum / len(body)
    analyzed["ave_regi_baristaNum"] = ave_regi_baristaNum / len(body)
    analyzed["ave_drip_baristaNum"] = ave_drip_baristaNum / len(body)
    analyzed["ave_waiting_regi"] = ave_waiting_regi / len(body)
    analyzed["ave_waiting_bar"] = ave_waiting_bar / len(body)
    analyzed["ave_drip_meter"] = ave_drip_meter / len(body)
    analyzed["ave_arrive_1_flag"] = ave_arrive_1_flag / len(body)
    analyzed["ave_arrive_2_flag"] = ave_arrive_2_flag / len(body)

    return analyzed


def analyze_result(analyzed, result):
    ave_regi_time = 0  # レジ時間の平均
    ave_bar_time = 0  # バー時間の平均
    ave_all_waiting_time = 0  # 全待ち時間の平均
    serve_count = 0  # サーブ回数
    num_of_people = 0  # 人数
    num_of_menued = 0  # メニューを受け取った人数

    # 各要素の処理
    for i in result:
        ave_regi_time += i["regi_time"] - i["arrive_time"]
        ave_bar_time += i["leave_time"] - i["regi_time"]
        ave_all_waiting_time += i["leave_time"] - i["arrive_time"]
        serve_count += 1
        num_of_people += i["num"]
        if i["menued"]:
            num_of_menued += 1 * i["num"]

    # 各要素の平均を求める
    analyzed["ave_regi_time"] = ave_regi_time / len(result)
    analyzed["ave_bar_time"] = ave_bar_time / len(result)
    analyzed["ave_all_waiting_time"] = ave_all_waiting_time / len(result)
    analyzed["serve_count"] = serve_count
    analyzed["num_of_people"] = num_of_people
    analyzed["num_of_menued"] = num_of_menued

    return analyzed


def main():
    log_file_path = get_log_file_path()  # コマンドライン引数からlogファイルのパスを取得
    meta, body, result = get_log_data(
        log_file_path
    )  # logファイルからmeta, body, resultを取得
    analyzed = {}
    analyzed = analyze_body(analyzed, body)  # bodyを解析
    analyzed = analyze_result(analyzed, result)  # resultを解析

    # 解析結果を出力
    for key, value in analyzed.items():
        print(key, value)


if __name__ == "__main__":
    main()
