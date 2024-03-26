import json
import os

from dotenv import load_dotenv

load_dotenv()


class JsonLogger:
    last_dump_time = None  # 最後にbodyをセットした時間
    log_template = None  # dumpするlogの形式]
    file_path = None  # 出力logのファイル名

    def __init__(self, file_path: str) -> None:
        self.last_dump_time = -1
        self.log_template = {"meta": {}, "body": [], "result": {}}
        self.file_path = file_path

    def __del__(self):
        self.save()

    def set_body(self, status) -> None:
        if status["elapsed_time"] - self.last_dump_time < int(
            os.getenv("LOG_INTERVAL")
        ):
            return
        self.last_dump_time = status["elapsed_time"]
        # logデータの取得
        log_data = status.copy()
        # logするデータから不要なものを削除
        log_data.pop("served")
        self.log_template["body"].append(log_data)

    def set_result(self, status) -> None:
        # データの追加
        self.log_template["result"] = status["served"]

    def set_meta(self, name: str, limit_time: str, begin_time: str) -> None:
        # データの追加
        self.log_template["meta"] = {
            "name": name,
            "limit_time": limit_time,
            "begin_time": begin_time,
        }

    def save(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump(self.log_template, f, indent=4)
