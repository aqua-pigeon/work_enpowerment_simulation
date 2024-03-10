import random
import sys

import pygame
import random

import utils.ImgClass as ImgClass
import utils.ScreenClass as ScreenClass


def main():
    screen_instance = ScreenClass.Screen()  # screenClassのインスタンスを生成

<<<<<<< HEAD
    
=======
    waiting_regi = 0  # レジで待っている人数
    waiting_bar = 0  # バーで待っている人数
    served = 0  # サーブされた人数
    drip_coffee = 0  # ドリップコーヒーの残量
>>>>>>> 87d270892b3398f2b1be1d3f977a462dd092feae

    # レジの状態
    reg1_free = True
    reg2_free = True
    bar_free = True

    # レジの接客時間
    reg1_time = 0
    reg2_time = 0

    bar_time = 0

    # 待ち行列の人数
    waiting_regi = 0
    waiting_bar = 0

    # サービスされた人数と作成されたドリンクの数
    served = 0
    drip_coffee = 0

# ゲームループ
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

<<<<<<< HEAD
        

=======
>>>>>>> 87d270892b3398f2b1be1d3f977a462dd092feae
        # お客さんの増加
        if pygame.time.get_ticks() % 15 == 0:
            waiting_regi += 1
        if pygame.time.get_ticks() % 30 == 0:
            waiting_regi += 2

        # レジの接客
        if reg1_free and waiting_regi > 0:
            reg1_free = False
            waiting_regi -= 1
            reg1_time = 10
        if reg2_free and waiting_regi > 0:
            reg2_free = False
            waiting_regi -= 1
            reg2_time = random.choice([10, 20])

        # レジのカウントダウン
        if reg1_time > 0:
            reg1_time -= 1
            if reg1_time == 0:
                # バーでドリンクを作成
<<<<<<< HEAD
               waiting_bar += 1
               
               reg1_free = True
=======
                waiting_bar += 1

                reg1_free = True
>>>>>>> 87d270892b3398f2b1be1d3f977a462dd092feae
        if reg2_time > 0:
            reg2_time -= 1
            if reg2_time == 0:
                # バーでドリンクを作成
<<<<<<< HEAD
                waiting_bar += 1    
                reg2_free = True

        # ドリンクの作成
       
      
        if waiting_bar > 0:
            if bar_time == 0:
                bar_time = 10  # 10秒かかる
           
=======
                waiting_bar += 1
                reg2_free = True

        # ドリンクの作成

        if waiting_bar > 0:
            if bar_time == 0:
                bar_time = 10  # 10秒かかる

>>>>>>> 87d270892b3398f2b1be1d3f977a462dd092feae
            if bar_time > 0:
                bar_time -= 1
                waiting_bar -= 1
                served += 1
                bar_time = 10  # ドリンク作成のカウントをリセット
<<<<<<< HEAD
            

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
=======

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
>>>>>>> 87d270892b3398f2b1be1d3f977a462dd092feae

        screen_instance.clear()  # 画面を白で塗りつぶす
        screen_instance.draw_field()  # フィールドを描画

        screen_instance.draw_info_bar_frame()  # インフォメーションバーの静的コンテンツを描画
        screen_instance.draw_info_bar_value(
            waiting_regi, waiting_bar, served, drip_coffee
        )  # インフォメーションバーの動的コンテンツを描画

        screen_instance.draw_regi_barista(regi_num=1)  # レジ1のバリスタを描画
        screen_instance.draw_regi_barista(regi_num=2)  # レジ2のバリスタを描画
        screen_instance.draw_bar_barista(barista_num=1)  # バー1のバリスタを描画
        screen_instance.draw_bar_barista(barista_num=2)  # バー2のバリスタを描画
        screen_instance.draw_drip_barista()  # ドリップの位置にバリスタを描画
        screen_instance.draw_regi_waitingPeople(
            regi_num=1, waitingNum=10
        )  # レジ1の待ち人数を描画
        screen_instance.draw_regi_waitingPeople(
            regi_num=2, waitingNum=3
        )  # レジ2の待ち人数を描画
        screen_instance.draw_bar_waitingPeople(waitingNum=20)  # バーの待ち人数を描画
        screen_instance.draw_drip_meter(dripNum=2)  # ドリップの残量を描画

        pygame.display.flip()  # 画面を更新


if __name__ == "__main__":
    main()
