import os
import sys
import time

import pygame
from dotenv import load_dotenv

import utils.bar as bar
import utils.Button as Button
import utils.drip as drip
import utils.log as log
import utils.regi as regi
import utils.ScreenClass as ScreenClass

load_dotenv()  # .envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから
pygame.init()  # Pygameの初期化


def main():
    screen_instance = ScreenClass.Screen()  # screenClassのインスタンスを生成

    # button設定
    field_object_coordinates = screen_instance.field_object_coordinates
    # フィールドのオブジェクト座標を取得
    drip_cofee_button = Button.TimeLinkedButton(
        field_object_coordinates["drip_coffee"], int(os.getenv("DRIP_COFFEE_COOL_TIME"))
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
    log_file_name = (
        time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".json"
    )  # ログファイル名を生成
    status = {
        "bar_baristaNum": 1,  # バーのバリスタの数
        "regi_baristaNum": 1,  # レジのバリスタの数
        "drip_baristaNum": 0,  # ドリップのバリスタの数
        "regi1_time": 0,  # 接客時間
        "regi2_time": 0,  # 接客時間
        "regi1_start_time": 0,  # 接客開始時間
        "regi2_start_time": 0,  # 接客開始時間
        "bar_start_time": 0,  # ドリンク作成開始時間
        "waiting_regi": 0,  # 待ち行列の人数
        "waiting_regi_unserviced": 0,  # メニューを渡されてない人
        "waiting_bar": 0,  # 待ち行列の人数
        "served": 0,  # サービスされた人数=作成されたドリンクの数
        "drip_coffee": 0,  # ドリップコーヒーの補充回数
        "drip_meter": 5,  # ドリップの残量
        "arrive_1_flag": True,  # 到着を受理していいか否か
        "arrive_2_flag": True,  # 到着を受理していいか否か
        "is_reg1_free": True,  # レジ1が空いているか
        "is_reg2_free": True,  # レジ2が空いているか
        "is_bar_free": True,  # バーが空いているか
        "elapsed_time": 0,  # 経過時間（秒）
        "regi_serviced_time": 0,  # 何人めのお客さんか
        "os_cool_time": 0,  # osが作業に拘束される時間
        "click_disabled": False,
        "countdown_time": 5,
    }

    # ゲームループ
    running = True

    while running:
        status["elapsed_time"] = time.time() - start_time  # 経過時間を計算（秒）
        events = pygame.event.get()  # pygame画面でのイベントを取得
        log.dump_log("log/" + log_file_name, status)  # ログを出力

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if drip_cofee_button.check_button(
            events
        ):  # ドリップコーヒーのボタンがクリックされた場合
            # print("drip_coffee_button clicked. time: ", status["elapsed_time"])
            status["regi_baristaNum"] = 1
            status["bar_baristaNum"] = 1
            status["drip_meter"] = 5

        if  regi2_button.check_button(
            events
        ):  # regi2のボタンがクリックされた場合
            print("regi2_button clicked. time: ", int(status["elapsed_time"]))

            status["regi_baristaNum"] = 2
            status["bar_baristaNum"] = 1

        if  bar_button.check_button(events):

            status["regi_baristaNum"] = 1
            status["is_reg2_free"]=False
            status["bar_baristaNum"] = 2

        if menu_button.check_button(events):  # menuのボタンがクリックされた場合
            print("menu_button clicked. time: ", int(status["elapsed_time"]))

            status["regi_baristaNum"] = 1
            status["bar_baristaNum"] = 1
            status["waiting_regi_unserviced"] -= 1

        status = regi.regi_customer_arrive(status)  # お客さんの到着管理
        status = regi.regi_service(status)  # レジの接客管理
        status = bar.bar_service(status)  # バーのドリンク作成管理
        status = drip.drip_decrease(status)  # ドリップの残量を減らす
        # status = buttonAction.set_drip(status)  # ボタンの管理

        screen_instance.clear()  # 画面を白で塗りつぶす
        screen_instance.draw_field()  # フィールドを描画
        screen_instance.draw_info_bar_frame()  # インフォメーションバーの静的コンテンツを描画
        screen_instance.draw_info_bar_value(
            status["waiting_regi"],
            status["waiting_bar"],
            status["served"],
            status["drip_coffee"],
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
        screen_instance.draw_regi_waitingPeople(
            status["waiting_regi"], status["is_reg1_free"], status["is_reg2_free"]
        )  # レジの待ち人数を描画
        screen_instance.draw_bar_waitingPeople(
            status["waiting_bar"]
        )  # バーの待ち人数を描画
        screen_instance.draw_drip_meter(status["drip_meter"])  # ドリップの残量を描画

        pygame.display.flip()  # 画面を更新


if __name__ == "__main__":
    main()
