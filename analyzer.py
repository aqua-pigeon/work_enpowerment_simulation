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
        return self.analyzed

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


def draw_regi_waiting_time_histogram(
    list, filename
):  # レジ待ち時間のヒストグラムを描画
    plt.hist(list, bins=20)
    plt.xlabel("regi_waiting_times")
    plt.ylabel("frequency")

    # plt.show()
    plt.savefig("analyze_result/" + filename + "_regi_waiting_times.png")


def draw_bar_waiting_time_histogram(list):  # バー待ち時間のヒストグラムを描画
    plt.hist(list, bins=20)
    plt.xlabel("bar_waiting_times")
    plt.ylabel("frequency")
    plt.show()


def draw_all_waiting_time_histogram(list):  # 全待ち時間のヒストグラムを描画
    plt.hist(list, bins=20)
    plt.xlabel("waiting time")
    plt.ylabel("frequency")
    plt.show()


def draw_regi_waiting_people_graph(list):  # レジ待ち人数の時系列グラフを描画
    plt.plot(list)
    plt.xlabel("time")
    plt.ylabel("waiting people")
    plt.show()


def draw_bar_waiting_people_graph(list):  # バー待ち人数の時系列グラフを描画
    plt.plot(list)
    plt.xlabel("time")
    plt.ylabel("waiting people")
    plt.show()


# メニューを渡された人数の時系列変化をレジの待ち人数の時系列変化と比較してグラフに描画
def draw_menued_people_graph(regi_waiting_people, menued_people):
    plt.plot(regi_waiting_people, label="regi_waiting_people")
    plt.plot(menued_people, label="menued_people")
    plt.xlabel("time")
    plt.ylabel("people")
    plt.legend()
    plt.show()


# レジの平均待ち時間と平均待ち人数、バーの平均待ち時間と平均待ち人数、全体の平均待ち時間と平均待ち人数を比較してグラフに描画
def draw_waiting_time_and_people_graph(
    regi_waiting_times,
    regi_waiting_people,
    bar_waiting_times,
    bar_waiting_people,
    all_waiting_times,
    all_waiting_people,
):
    plt.plot(regi_waiting_times, label="regi_waiting_times")
    plt.plot(regi_waiting_people, label="regi_waiting_people")
    plt.plot(bar_waiting_times, label="bar_waiting_times")
    plt.plot(bar_waiting_people, label="bar_waiting_people")
    plt.plot(all_waiting_times, label="all_waiting_times")
    plt.plot(all_waiting_people, label="all_waiting_people")
    plt.xlabel("time")
    plt.ylabel("people")
    plt.legend()
    plt.show()


def draw_num_of_people(num_of_people_dict, filename):
    # num_of_people_dictのキーごとに色分けし、分布図を描画
    # num_of_people_dictのvalueはリスト。
    # xは累積の要素番号、yはその要素番号に対応するリストの要素

    for key, value in num_of_people_dict.items():
        plt.hist(value, bins=10, alpha=0.5, label=key)
    plt.xlabel("num_of_people")
    plt.ylabel("frequency")
    plt.legend()
    plt.savefig("analyze_result/" + filename + "_num_of_people.png")


def main():
    # log_file_path = get_log_file_path()  # コマンドライン引数からlogファイルのパスを取得
    # analyzer1 = analyzer(log_file_path)  # logファイルを解析するためのインスタンスを生成
    log_file_paths = [
        ["OkadaYuro_20240327_224548.json", 1],
        ["aika_kishigami_20240328_151935.json", 1],
        ["aya_nagao_20240328_133350.json", 1],
        ["emi_tokura_20240326_230137.json", 1],
        ["kai_watanabe_20240328_104528.json", 2],
        ["kano_nisimura_20240327_092226.json", 2],
        ["kenta_ano_20240327_182046.json", 2],
        ["mayu_kurozumi_20240327_170252.json", 3],
        ["mina_20240328_121042.json", 3],
        ["miu_furuya_20240327_182046.json", 3],
        ["naoki_akanuma_20240327_153844.json", 3],
        ["tokura_yutaka_20240326_222413.json", 3],
        ["yuta_matusita_20240327_161356.json", 1],
        ["亀田あずさ_20240327_135457.json", 1],
    ]

    num_of_people_dict = {"1": [], "2": [], "3": []}  # 人数のリストを格納する辞書
    regi_waiting_times_dict = {
        "1": [],
        "2": [],
        "3": [],
    }  # レジ待ち時間のリストを格納する辞書

    for i in log_file_paths:
        file_name = i[0]
        discretion_level = i[1]
        target = analyzer(
            "analyze_target/" + file_name
        )  # logファイルを解析するためのインスタンスを生成
        analyzed = target.analyze()
        num_of_people_dict[str(discretion_level)].append(analyzed["num_of_people"])
        regi_waiting_times_dict[str(discretion_level)].extend(
            analyzed["regi_waiting_times"]
        )  # レジ待ち時間のリストを格納
    print(regi_waiting_times_dict)
    # draw_num_of_people(num_of_people_dict, "num_of_people")

    # # dict, list以外のデータを出力, dict, listのデータは型とshapeを出力
    # for key, value in analyzed.items():
    #     if type(value) not in [dict, list]:
    #         print(f"{key}: {value}")  # dict, list以外のデータを出力
    #     else:
    #         print(
    #             f"{key}: {type(value)}, {np.shape(value)}"
    #         )  # dict, listのデータは型とshapeを出力
    # draw_regi_waiting_time_histogram(
    #     analyzed["regi_waiting_times"], analyzed["name"]
    # )

    # ヒストグラムを描画
    # draw_regi_waiting_time_histogram(analyzer1.analyzed["regi_waiting_times"])
    # draw_bar_waiting_time_histogram(analyzer1.analyzed["bar_waiting_times"])
    # draw_all_waiting_time_histogram(analyzer1.analyzed["all_waiting_times"])

    # # 時系列グラフを描画
    # draw_regi_waiting_people_graph(analyzer1.analyzed["regi_waiting_people"])
    # draw_bar_waiting_people_graph(analyzer1.analyzed["bar_waiting_people"])
    # draw_menued_people_graph(analyzer1.analyzed["regi_waiting_people"], analyzer1.analyzed["bar_waiting_people"])
    # draw_waiting_time_and_people_graph(analyzer1.analyzed["regi_waiting_times"], analyzer1.analyzed["regi_waiting_people"], analyzer1.analyzed["bar_waiting_times"], analyzer1.analyzed["bar_waiting_people"], analyzer1.analyzed["all_waiting_times"], analyzer1.analyzed["all_waiting_people"])


if __name__ == "__main__":
    main()
