import json
import os

last_dump_time = -1


def dump_log(file_path, status):
    global last_dump_time
    if status["elapsed_time"] - last_dump_time < 1:
        return
    last_dump_time = status["elapsed_time"]
    # ファイルが存在しない場合は新規作成
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)
    # ファイルの読み込み
    with open(file_path, "r") as f:
        data = json.load(f)
    # データの追加
    data.append(status)
    # ファイルの書き込み
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    return data
