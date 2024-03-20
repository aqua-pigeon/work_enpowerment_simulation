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
    meta = log[0]
    body = log[1:]

    # body中のwaiting_regi_queueだけを取り出す
    waiting_regi_queue = [b["waiting_regi_queue"] for b in body]
    print(waiting_regi_queue)
    # waiting_regi_queueから人数を取得する
    waiting_regi_num = []
    for i in waiting_regi_queue:
        waiting_regi_num.append(regi.get_waiting_regi_num(i))
    print(waiting_regi_num)
    # waiting_regi_numの平均を求める
    waiting_regi_num_average = sum(waiting_regi_num) / len(waiting_regi_num)
    print(waiting_regi_num_average)

    # # bodyの中のbar_baristaNumだけを取り出す
    # bar_baristaNum = [b["bar_baristaNum"] for b in body]
    # print(bar_baristaNum)
    # # bar_baristaNumの平均を求める
    # bar_baristaNum_average = sum(bar_baristaNum) / len(bar_baristaNum)
    # print(bar_baristaNum_average)


if __name__ == "__main__":
    main()
