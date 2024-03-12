import math
import sys
import time

import pygame

import utils.regi as regi
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
        "regi1_start_time": 0,  # 接客開始時間
        "regi2_start_time": 0,  # 接客開始時間
        "bar_time": 0,  # ドリンク作成時間
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
        "elapsed_time": 0,  # 経過時間
    }

    # レジでの基本接客時間
    regi_service_base_time = 10

    # serviced_time
    regi_serviced_time = 0
    regi2_serviced_time = 0

    # is_reg_free
    is_reg1_free = True
    is_reg2_free = True
    # is_bar_free
    is_bar_free = True

    # OSの人がレジにいるか
    os_regi = False
    # OSの人がバーにいるか
    os_bar = False

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左クリック
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # レジ2の領域がボタンとして押されたかどうかを確認
                if 350 < mouse_x < 430 and 300 < mouse_y < 350:
                    os_regi == True
                    if event.button == 1:  # 左クリック
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        # レジ2の領域がボタンとして押されたかどうかを確認
                        if 350 < mouse_x < 430 and 300 < mouse_y < 350:
                            os_regi == False

                if 500 < mouse_x < 800 and 300 < mouse_y < 400:
                    os_bar == True
                    if event.button == 1:  # 左クリック
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        # barの領域がボタンとして押されたかどうかを確認
                        if 500 < mouse_x < 800 and 300 < mouse_y < 400:
                            os_bar == False

    # ゲームループ
    running = True

    while running:
        status["elapsed_time"] = math.floor(
            time.time() - start_time
        )  # 経過時間を計算（小数点切り捨ての、秒）
        # print(status["elapsed_time"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # お客さんの増加
        status = regi.regi_customer_arrive(status)

        # レジの接客
        if os_regi == False and is_reg1_free and status["waiting_regi"] > 0:
            regi_serviced_time += 1
            if regi_serviced_time % 3 == 0:
                status["regi1_time"] = regi_service_base_time * 2
            else:
                status["regi1_time"] = regi_service_base_time
            status["regi1_start_time"] = time.time()
            is_reg1_free = False
        if (
            os_regi == False
            and math.floor(time.time() - status["regi1_start_time"])
            >= status["regi1_time"]
        ):
            is_reg1_free = True
            status["waiting_regi"] -= 1
            status["waiting_regi_unserviced"] -= 1
            if status["waiting_regi_unserviced"] < 0:
                status["waiting_regi_unserviced"] = 0
            if status["regi1_time"] == regi_service_base_time:
                status["waiting_bar"] += 1
            else:
                status["waiting_bar"] += 2

        # レジ2の接客

        if (
            os_regi == True
            and is_reg2_free == True
            and is_reg1_free == False
            and status["waiting_regi"] > 0
        ):
            regi2_serviced_time += 1
            if regi2_serviced_time % 3 == 0:
                status["regi2_time"] = regi_service_base_time * 2
            else:
                status["regi2_time"] = regi_service_base_time
                status["regi2_start_time"] = time.time()
                is_reg2_free = False

        if (
            os_regi == True
            and math.floor(time.time() - status["regi2_start_time"])
            >= status["regi2_time"]
        ):
            is_reg2_free = True
            status["waiting_regi"] -= 1
            status["waiting_regi_unserviced"] -= 1
            if status["waiting_regi_unserviced"] < 0:
                status["waiting_regi_unserviced"] = 0
            if status["regi2_time"] == regi_service_base_time:
                status["waiting_bar"] += 1
            else:
                status["waiting_bar"] += 2

        # ドリンクの作成(バリスタ1人)
        if os_bar == False and is_bar_free and status["waiting_bar"] > 0:
            status["bar_time"] += 1
            status["bar_start_time"] = time.time()
            is_bar_free = False
        if os_bar == False and math.floor(time.time() - status["bar_start_time"]) >= 10:
            is_bar_free = True
            status["waiting_bar"] -= 1
            status["served"] += 1
            status["bar_time"] = 0

        # ドリンクの作成(バリスタ２人)
        if os_bar == True and is_bar_free == False and status["waiting_bar"] > 0:
            status["bar_time"] += 1
            status["bar_start_time"] = time.time()
            is_bar_free = False
        if os_bar == True and math.floor(time.time() - status["bar_start_time"]) >= 5:
            is_bar_free = True
            status["waiting_bar"] -= 1
            status["served"] += 1
            status["bar_time"] = 0

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
            status["waiting_regi"], status["regi_baristaNum"]
        )  # レジの待ち人数を描画
        screen_instance.draw_bar_waitingPeople(
            status["waiting_bar"]
        )  # バーの待ち人数を描画
        screen_instance.draw_drip_meter(status["drip_meter"])  # ドリップの残量を描画

        pygame.display.flip()  # 画面を更新


if __name__ == "__main__":
    main()
