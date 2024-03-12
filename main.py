import random
import sys
import time

import pygame

import utils.ImgClass as ImgClass
import utils.ScreenClass as ScreenClass


def main():
    screen_instance = ScreenClass.Screen()  # screenClassのインスタンスを生成
    start_time = time.time()  # ゲームの開始時間を記録
    status = {
        "bar_baristaNum": 1,  # バーのバリスタの数
        "regi_baristaNum": 1,  # レジのバリスタの数
        "drip_baristaNum": 0,  # ドリップのバリスタの数
        "regi1_time": 0,  # 接客時間
        "regi2_time": 0,  # 接客時間
        "bar_time": 0,  # 接客時間
        "waiting_regi": 0,  # 待ち行列の人数
        "waiting_bar": 0,  # 待ち行列の人数
        "served": 0,  # サービスされた人数=作成されたドリンクの数
        "drip_coffee": 0,  # ドリップコーヒーの補充回数
        "drip_meter": 0,  # ドリップの残量
    }

    # ゲームループ
    running = True
    while running:
        elapsed_time = int(time.time() - start_time)  # 経過時間を計算（秒
        print(elapsed_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # お客さんの増加
        if pygame.time.get_ticks() % 15 == 0:
            status["waiting_regi"] += 1
        if pygame.time.get_ticks() % 30 == 0:
            status["waiting_regi"] += 2

        # レジの接客
        # if status["is_reg1_free"] and status["waiting_regi"] > 0:
        #     status["is_reg1_free"] = False
        #     status["waiting_regi"] -= 1
        #     status["reg1_time"] = 10
        # if status["is_reg2_free"] and status["waiting_regi"] > 0:
        #     status["is_reg2_free"] = False
        #     status["waiting_regi"] -= 1
        #     status["reg2_time"] = random.choice([10, 20])

        # レジのカウントダウン
        if status["regi1_time"] > 0:
            status["regi1_time"] -= 1
            if status["regi1_time"] == 0:
                # バーでドリンクを作成
                status["waiting_bar"] += 1
                # status["is_reg1_free"] = True

        if status["regi2_time"] > 0:
            status["regi2_time"] -= 1
            if status["reg2_time"] == 0:
                # バーでドリンクを作成
                status["waiting_bar"] += 1
                # status["is_regi2_free"] = True

        # ドリンクの作成
        if status["waiting_bar"] > 0:
            if status["bar_time"] == 0:
                status["bar_time"] = 10  # 10秒かかる

            if status["bar_time"] > 0:
                status["bar_time"] -= 1
                status["waiting_bar"] -= 1
                status["served"] += 1
                status["bar_time"] = 10  # ドリンク作成のカウントをリセット

        #    running = True
        #     reg1_time = 300
        #     while running:
        #         for event in pygame.event.get():
        #             if event.type == pygame.QUIT:  # Pygameの終了
        #                 pygame.quit()
        #                 sys.exit()
        # elif event.type == INCREASE_EVENT:
        #     wait_count += 1
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:  # 左クリック
        #         if increase_button.collidepoint(event.pos):  # ボタンがクリックされたか確認
        #             wait_count -= 1

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
            status["waiting_regi"]
        )  # レジの待ち人数を描画
        screen_instance.draw_bar_waitingPeople(
            status["waiting_bar"]
        )  # バーの待ち人数を描画
        screen_instance.draw_drip_meter(status["drip_meter"])  # ドリップの残量を描画

        pygame.display.flip()  # 画面を更新


if __name__ == "__main__":
    main()
