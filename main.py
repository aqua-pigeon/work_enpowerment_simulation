import os
import sys
import time
<<<<<<< HEAD
=======
import webbrowser

>>>>>>> a63c12abc556bb945fa27f8f7e3890be4b91deac
import pygame
import requests
from dotenv import load_dotenv
import utils.bar as bar
import utils.Button as Button
import utils.drip as drip
import utils.log as log
import utils.regi as regi
import utils.ScreenClass as ScreenClass

load_dotenv()  # .envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから


simulation_start_flag = 0  # シミュレーション開始フラグ


def main():
    # コマンドライン引数を受け取る
    if len(sys.argv) != 3:
        print(
            "使い方: python main.py <シミュレーションタイプ (test か demo).> <APIトークン>"
        )
        sys.exit(1)
    # APIトークンがxoxbから始まるかどうかをチェック
    elif sys.argv[2] == "xoxb-":
        print("APIトークンが不正です。")
        sys.exit(1)
    else:
<<<<<<< HEAD
        print(
            "使い方: python main.py <シミュレーションタイプ (test か demo).> <APIトークン>"
        )
    file_upload = (
        os.getenv("SLACK_UPLOAD") == "True" and sys.argv[1] == "test"
    )  # slackにログファイルをアップロードするかどうか
    # APIトークンがxoxbから始まるかどうかをチェック
    if sys.argv[2] == "xoxb-":
        print("APIトークンが不正です。")
        sys.exit(1)
    screen_instance = ScreenClass.Screen()  # screenClassのインスタンスを生成
=======
        if sys.argv[1] == "test":
            limit_time = int(
                os.getenv("SIMULATE_TIME")
            )  # シミュレーションの制限時間を取得
        elif sys.argv[1] == "demo":
            limit_time = int(os.getenv("DEMO_TIME"))  # シミュレーションの制限時間を取得
        else:
            print(
                "使い方: python main.py <シミュレーションタイプ (test か demo).> <APIトークン>"
            )

    file_upload = (
        os.getenv("SLACK_UPLOAD") == "True" and sys.argv[1] == "test"
    )  # slackにログファイルをアップロードするかどうか
>>>>>>> a63c12abc556bb945fa27f8f7e3890be4b91deac
    # 被験者の名前を入力
    name = input("被験者の名前を入力してください: ")
    log_file_path = (
        f"log/" + time.strftime("%Y%m%d_%H%M%S_", time.localtime()) + name + ".json"
    )  # ログファイル名を生成
    log.set_meta(
        log_file_path,
        name,
        limit_time,
        time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()),
    )  # メタデータを出力
<<<<<<< HEAD
=======

    pygame.init()  # Pygameの初期化
    screen_instance = ScreenClass.Screen()  # screenClassのインスタンスを生成

>>>>>>> a63c12abc556bb945fa27f8f7e3890be4b91deac
    # button設定
    field_object_coordinates = screen_instance.field_object_coordinates
    # フィールドのオブジェクト座標を取得
    drip_cofee_button = Button.TimeLinkedButton(
        field_object_coordinates["drip_coffee"],
        int(os.getenv("DRIP_COFFEE_COOL_TIME")),
    )  # ドリップコーヒーのボタンの設定
    regi2_button = Button.TimeLinkedButton(
        field_object_coordinates["regi2"], int(os.getenv("REGI_COOL_TIME"))
    )  # regi2のボタンの設定
    menu_button = Button.TimeLinkedButton(
        field_object_coordinates["menu"], int(os.getenv("MENU_COOL_TIME"))
    )  # menuのボタンの設定
    bar_button = Button.TimeLinkedButton(
        field_object_coordinates["bar"], int(os.getenv("BAR_COOL_TIME"))
    )  # regi2のボタンの設定
    start_time = time.time()  # ゲームの開始時間を記録
    status = {
        "bar_baristaNum": 1,  # バーのバリスタの数
        "regi_baristaNum": 1,  # レジのバリスタの数
        "drip_baristaNum": 0,  # ドリップのバリスタの数
        "regi1_time": 0,  # 接客時間
        "regi2_time": 0,  # 接客時間
        "regi1_start_time": 0,  # 接客開始時間
        "regi2_start_time": 0,  # 接客開始時間
        "bar_start_time": 0,  # ドリンク作成開始時間
        "waiting_regi_queue": [],  # 待ち行列の人数
        "waiting_bar": 0,  # 待ち行列の人数
        "served": 0,  # サービスされた人数=作成されたドリンクの数
        "drip_coffee_sup_count": 0,  # ドリップコーヒーの補充回数
        "drip_meter": 5,  # ドリップの残量
        "arrive_1_flag": True,  # 到着を受理していいか否か
        "arrive_2_flag": True,  # 到着を受理していいか否か
        "regi1_customer": 0,  # レジ1が空いている=0, 1or2=空いていない
        "regi2_customer": 0,  # レジ2が空いている=0, 1or2=空いていない
        "is_bar_free": True,  # バーが空いているか
        "elapsed_time": 0,  # 経過時間（秒）
        "regi_serviced_time": 0,  # 何人めのお客さんか
        "click": 0,  # OSクリックの回数
        "menued": 0,
    }
    # ゲームループ
    running = True
<<<<<<< HEAD
    while running:
        status["elapsed_time"] = time.time() - start_time  # 経過時間を計算（秒）
        events = pygame.event.get()  # pygame画面でのイベントを取得
        log.dump_log(log_file_path, status)  # ログを出力
=======
    Button.TimeLinkedButton.set_disabled(
        int(os.getenv("START_COOL_TIME"))
    )  # シミュレーション開始までのクールタイムを設定

    while running:
        status["elapsed_time"] = time.time() - start_time  # 経過時間を計算（秒）
        events = pygame.event.get()  # pygame画面でのイベントを取得

>>>>>>> a63c12abc556bb945fa27f8f7e3890be4b91deac
        for event in events:
            if event.type == pygame.QUIT:  # ウィンドウの×ボタンが押された場合
                pygame.quit()
        if status["elapsed_time"] > limit_time:  # 制限時間を超えた場合
            break  # ゲームを終了
        if drip_cofee_button.check_button(
            events
        ):  # ドリップコーヒーのボタンがクリックされた場合
            # print("drip_coffee_button clicked. time: ", status["elapsed_time"])
            if status["regi2_customer"] != 0:
                status["waiting_regi_queue"].insert(0, status["regi2_customer"])
                status["regi2_customer"] = 0
            status["regi_baristaNum"] = 1
            status["bar_baristaNum"] = 1
            status["drip_coffee_sup_count"] += 1
            status["drip_meter"] = 5
            status["click"] += 1
        if regi2_button.check_button(events):  # regi2のボタンがクリックされた場合
            print("regi2_button clicked. time: ", int(status["elapsed_time"]))
            status["regi_baristaNum"] = 2
            status["bar_baristaNum"] = 1
            status["click"] += 1
        if bar_button.check_button(events):
            if status["regi2_customer"] != 0:
                status["waiting_regi_queue"].insert(0, status["regi2_customer"])
                status["regi2_customer"] = 0
            status["regi_baristaNum"] = 1
            status["bar_baristaNum"] = 2
            status["click"] += 1
        if menu_button.check_button(events):  # menuのボタンがクリックされた場合
            print("menu_button clicked. time: ", status["elapsed_time"])
            if status["regi2_customer"] != 0:
                status["waiting_regi_queue"].insert(0, status["regi2_customer"])
                status["regi2_customer"] = 0
                status["regi_baristaNum"] = 1
                status["bar_baristaNum"] = 1
            status["regi_baristaNum"] = 1
            status["bar_baristaNum"] = 1
            for i in range(len(status["waiting_regi_queue"])):
                if status["waiting_regi_queue"][i] < 3:
                    status["waiting_regi_queue"][i] += 3
                    break
            status["click"] += 1
            status["menued"] += 1
        status = regi.regi_customer_arrive(status)  # お客さんの到着管理
        status = regi.regi_service(status)  # レジの接客管理
        status = bar.bar_service(status)  # バーのドリンク作成管理
        status = drip.drip_decrease(status)  # ドリップの残量を減らす
        # status = buttonAction.set_drip(status)  # ボタンの管理
        screen_instance.clear()  # 画面を白で塗りつぶす
        screen_instance.draw_field()  # フィールドを描画
        screen_instance.draw_info_bar_frame()  # インフォメーションバーの静的コンテンツを描画
        screen_instance.draw_info_bar_value(
            regi.get_waiting_regi_num(status["waiting_regi_queue"]),
            status["waiting_bar"],
            status["served"],
            status["drip_coffee_sup_count"],
        )  # インフォメーションバーの動的コンテンツを描画
        screen_instance.draw_cool_time(  # クールタイムを描画
            int(
                Button.TimeLinkedButton.get_last_cool_time()
            )  # TimeLinkedButtonが保存するクールタイムを取得
        )
        # regi1_buttonなどから取得しないのは、regi1_buttonなどのインスタンスが存在しない場合も踏まえ、プログラムとしての汎用性を上げるため
        if status["regi_baristaNum"] > 0:
            screen_instance.draw_regi_barista(regi_num=1)  # レジ1のバリスタを描画
        if status["regi_baristaNum"] > 1:
            screen_instance.draw_regi_barista(regi_num=2)  # レジ2のバリスタを描画
        if status["bar_baristaNum"] > 0:
            screen_instance.draw_bar_barista(barista_num=1)  # バー1のバリスタを描画
        if status["bar_baristaNum"] > 1:
            screen_instance.draw_bar_barista(barista_num=2)  # バー2のバリスタを描画
        if status["drip_baristaNum"] > 0:
            screen_instance.draw_drip_barista()  # ドリップの位置にバリスタを描画
        screen_instance.draw_regi_waitingPeople(status)  # レジの待ち人数を描画
        screen_instance.draw_bar_waitingPeople(
            status["waiting_bar"]
        )  # バーの待ち人数を描画
        screen_instance.draw_drip_meter(status["drip_meter"])  # ドリップの残量を描画
        pygame.display.flip()  # 画面を更新
<<<<<<< HEAD
=======
        log.dump_log(log_file_path, status)  # ログを出力

>>>>>>> a63c12abc556bb945fa27f8f7e3890be4b91deac
    # ゲーム終了後の処理
    if file_upload:
        # logファイルを開いてslackにアップロード
        with open(log_file_path, "rb") as file:
            response = requests.post(
                url="https://slack.com/api/files.upload",
                headers={"Authorization": f"Bearer {sys.argv[2]}"},
                data={"channels": os.getenv("SLACK_CHANNEL")},
                files={"file": file},
            )
        if response.json()["ok"] is not True:
            print("logファイルのアップロードに失敗しました")
            print(response.json())
            sys.exit(1)
        print("logファイルをアップロードしました。")
    print("実験お疲れ様でした。引き続きアンケートのご協力をお願いします")
    webbrowser.open(os.getenv("QUESTIONNAIRE_URL"))  # アンケートページを開く


if __name__ == "__main__":
    main()
