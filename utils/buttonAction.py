import time

import pygame

regi_rect = (350, 300, 80, 50)
bar_rect = (500, 300, 300, 100)
drip_coffee_rect = (420, 480, 80, 70)



def set_drip(status):

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if status["click_disabled"] and event.button == 1:  # 左クリック
                mouse_pos = pygame.mouse.get_pos()  # マウスの座標を取得
                # マウスの座標がドリップコーヒーの領域内にあるかどうかを確認
                if  drip_coffee_rect.collidepoint(mouse_pos):
                    # クリックを無効にするフラグを立てる
                    status["click_disabled"] = True
                    # カウントダウンが終了したらクリックを有効にする
                   
        if status["elapsed_time"] % 1 == 0:
                if status["click_disabled"]==True:
        # カウントダウンの残り時間を計算
                        if status["countdown_time"] > 0:
                             status["countdown_time"] -= 1
                                # カウントダウンが終了したらクリックを有効にする
                        status["click_disabled"] = False
                        if status["countdown"]<=0:
                             status["drip_meter"] = 5
                             status["countdown_time"] = 5  # カウントダウン時間をリセット
                             status["click_disabled"] = False
        else:
                status["click_disabled"] = False
    return status
    

