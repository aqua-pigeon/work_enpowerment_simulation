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
    result = log["result"]

    for i in result:
        num = i["num"]
        menued = i["menued"]
        arrive = i["arrive_time"]
        regiEnd = i["regi_time"]
        leave = i["leave_time"]

        time1 = leave - arrive
        regi_time = regiEnd - arrive
        bar_time = leave - regiEnd
        print(time1, regi_time, bar_time)


if __name__ == "__main__":
    main()
