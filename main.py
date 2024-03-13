import math
import sys
import time

import pygame

import utils.bar as bar
import utils.log as log
import utils.regi as regi
import utils.ScreenClass as ScreenClass

pygame.init()  # Pygameの初期化

def main():
    screen_instance = ScreenClass.Screen()  # screenClassのインスタンスを生成
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
        "drip_meter": 0,  # ドリップの残量
        "arrive_1_flag": True,  # 到着を受理していいか否か
        "arrive_2_flag": True,  # 到着を受理していいか否か
        "is_reg1_free": True,  # レジ1が空いているか
        "is_reg2_free": True,  # レジ2が空いているか
        "is_bar_free": True,  # バーが空いているか
        "elapsed_time": 0,  # 経過時間
        "regi_serviced_time": 0,  # 何人めのお客さんか
    }

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左クリック
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # レジ2の領域がボタンとして押されたかどうかを確認
                if 350 < mouse_x < 430 and 300 < mouse_y < 350:
                    status["regi_baristaNum"] += 1
                    if event.button == 1:  # 左クリック
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        # レジ2の領域がボタンとして押されたかどうかを確認
                        if 350 < mouse_x < 430 and 300 < mouse_y < 350:
                            status["regi_baristaNum"] -= 1

                if 500 < mouse_x < 800 and 300 < mouse_y < 400:
                    status["bar_baristaNum"] += 1
                    if event.button == 1:  # 左クリック
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        # barの領域がボタンとして押されたかどうかを確認
                        if 500 < mouse_x < 800 and 300 < mouse_y < 400:
                            status["bar_baristaNum"] -= 1

    # ゲームループ
    running = True

    while running:
        status["elapsed_time"] = math.floor(
            time.time() - start_time
        )  # 経過時間を計算（小数点切り捨ての、秒）
        # print(status["elapsed_time"])

        log.dump_log("log/" + log_file_name, status)  # ログを出力

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        

        status = regi.regi_customer_arrive(status)  # お客さんの到着管理
        status = regi.regi_service(status)  # レジの接客管理
        status = bar.bar_service(status)  # バーのドリンク作成管理

        screen_instance.clear()  # 画面を白で塗りつぶす
        screen_instance.draw_field()  # フィールドを描画
        screen_instance.draw_info_bar_frame()  # インフォメーションバーの静的コンテンツを描画
        screen_instance.draw_info_bar_value(
            status["waiting_regi"],
            status["waiting_bar"],
            status["served"],
            status["drip_coffee"],
        )  # インフォメーションバーの動的コンテンツを描画
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
