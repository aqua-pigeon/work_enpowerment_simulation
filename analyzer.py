import json
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv

load_dotenv()


def get_log_file_path() -> str:  # コマンドライン引数からlogファイルのパスを取得
    # コマンドライン引数を受け取る
    args = sys.argv
    if len(args) != 2:
        print("Usage: python analyze.py <log_file_path>")
        sys.exit(1)
    log_file_path = args[1]
    return log_file_path


class analyzer:
    meta: dict = None  # log/metaデータ
    body: list = None  # log/bodyデータ
    result: list = None  # log/resultデータ
    analyzed: dict = {}  # 解析結果

    def __init__(self, log_file_path: str) -> None:
        # jsonファイルを開く
        with open(log_file_path, "r") as f:
            log = json.load(f)
        self.meta = log["meta"]  # logデータ内のmetaデータを取得
        self.body = log["body"]  # logデータ内
        self.result = log["result"]  # logデータ内のresultデータを取得

    def analyze(self):  # logファイルを解析
        self.analyze_meta()  # metaを解析
        self.analyze_body()  # bodyを解析
        self.analyze_result()  # resultを解析
        self.get_waiting_people()  # resultから、ある時点での待ち人数を取得

    def analyze_meta(self):  # metaを解析
        self.analyzed["name"] = self.meta["name"]  # 被験者の名前を出力

    def analyze_body(self):  # bodyを解析
        self.analyzed["body_length"] = len(self.body)  # bodyの長さを出力
        self.analyzed["drip_coffee_sup_count"] = self.body[-1][
            "drip_coffee_sup_count"
        ]  # ドリップコーヒー供給回数を出力
        self.analyzed["click"] = self.body[-1]["click"]  # クリック回数を出力
        self.analyzed["average_bar_baristaNum"] = np.mean(
            [i["bar_baristaNum"] for i in self.body]
        )  # バーのバリスタ数の平均を出力
        self.analyzed["average_regi_baristaNum"] = np.mean(
            [i["regi_baristaNum"] for i in self.body]
        )  # レジのバリスタ数の平均を出力
        self.analyzed["average_drip_baristaNum"] = np.mean(
            [i["drip_baristaNum"] for i in self.body]
        )  # ドリップのバリスタ数の平均を出力
        self.analyzed["average_drip_meter"] = np.mean(
            [i["drip_meter"] for i in self.body]
        )  # ドリップメーターの平均を出力
        self.analyzed["drip_meter_zero_count"] = len(
            [i for i in self.body if i["drip_meter"] == 0]
        )  # ドリップメーターが0の回数を出力

    def analyze_result(self):  # resultを解析
        self.analyzed["regi_waiting_times"] = [
            i["regi_time"] - i["arrive_time"] for i in self.result
        ]  # レジ待ち時間を出力
        self.analyzed["bar_waiting_times"] = [
            i["leave_time"] - i["regi_time"] for i in self.result
        ]  # バー待ち時間を出力
        self.analyzed["all_waiting_times"] = [
            i["leave_time"] - i["arrive_time"] for i in self.result
        ]  # 全待ち時間を出力
        self.analyzed["average_regi_time"] = np.mean(
            self.analyzed["regi_waiting_times"]
        )  # レジ待ち時間の平均を出力
        self.analyzed["average_bar_time"] = np.mean(
            self.analyzed["bar_waiting_times"]
        )  # バー待ち時間の平均を出力
        self.analyzed["average_all_waiting_time"] = np.mean(
            self.analyzed["all_waiting_times"]
        )  # 全待ち時間の平均を出力
        self.analyzed["max_waiting_regi_time"] = np.max(
            self.analyzed["regi_waiting_times"]
        )  # レジ待ち時間の最大値を出力
        self.analyzed["max_waiting_bar_time"] = np.max(
            self.analyzed["bar_waiting_times"]
        )  # バー待ち時間の最大値を出力
        self.analyzed["max_waiting_all_time"] = np.max(
            self.analyzed["all_waiting_times"]
        )  # 全待ち時間の最大値を出力
        self.analyzed["num_of_people"] = np.sum(
            [i["num"] for i in self.result]
        )  # 接客終了した人数の合計を出力
        self.analyzed["num_of_menued"] = np.sum(
            [i["num"] for i in self.result if i["menued"]]
        )  # メニューを選択した人数を出力

    def get_waiting_people(self):  # resultから、ある時点での待ち人数を取得
        simulation_time = int(os.getenv("SIMULATE_TIME"))  # シミュレーション時間
        start_time = int(
            self.result[0]["arrive_time"]
        )  # 最初の人が到着する時間が0秒だから、それをスタート時間とする
        self.analyzed["regi_waiting_people"] = [
            0
        ] * simulation_time  # 0秒からsimulation_time秒までのレジ待ち人数変化を格納するリスト
        self.analyzed["bar_waiting_people"] = [
            0
        ] * simulation_time  # 0秒からsimulation_time秒までのバー待ち人数変化を格納するリスト

        # i+start_time秒がregi_timeとleave_timeの間にある人数を数える
        for i in range(simulation_time):  # 0秒からsimulation_time秒までの各秒について
            for j in self.result:  # resultの各要素について
                if j["arrive_time"] <= i + start_time <= j["leave_time"]:
                    self.analyzed["regi_waiting_people"][i] += j["num"]
                if j["regi_time"] <= i + start_time <= j["leave_time"]:
                    self.analyzed["bar_waiting_people"][i] += j["num"]
        self.analyzed["average_regi_waiting_people"] = np.mean(
            self.analyzed["regi_waiting_people"]
        )  # レジ待ち人数の平均を出力
        self.analyzed["average_bar_waiting_people"] = np.mean(
            self.analyzed["bar_waiting_people"]
        )  # バー待ち人数の平均を出力
        self.analyzed["max_regi_waiting_people"] = np.max(
            self.analyzed["regi_waiting_people"]
        )  # レジ待ち人数の最大値を出力
        self.analyzed["max_bar_waiting_people"] = np.max(
            self.analyzed["bar_waiting_people"]
        )  # バー待ち人数の最大値を出力


def draw_regi_waiting_time_histogram(list):
    plt.hist(list, bins=20)
    plt.xlabel("waiting time")
    plt.ylabel("frequency")
    plt.show()


def main():
    log_file_path = get_log_file_path()  # コマンドライン引数からlogファイルのパスを取得
    analyzer1 = analyzer(log_file_path)  # logファイルを解析
    analyzer1.analyze()  # 解析

    # dict, list以外のデータを出力, dict, listのデータは型とshapeを出力
    for key, value in analyzer1.analyzed.items():
        if type(value) not in [dict, list]:
            print(f"{key}: {value}")
        else:
            print(f"{key}: {type(value)}, {np.shape(value)}")

    # ヒストグラムを描画
    draw_regi_waiting_time_histogram(analyzer1.analyzed["regi_waiting_times"])


if __name__ == "__main__":
    main()
