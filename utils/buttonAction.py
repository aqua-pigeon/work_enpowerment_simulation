import time

import pygame

regi_rect = (350, 300, 80, 50)
bar_rect = (500, 300, 300, 100)
drip_coffee_rect = (420, 480, 80, 70)
menu_rect = (40, 200, 110, 90)


#ドリップコーヒーのメーターが回復するのに5秒かかる

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
        # カウントダウンの残り時間を計算git pull
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
    

    def menu_serve(status):
        if status[click]==True:
              if menu_rect.collidepoint(mouse_pos):
         # クリックを無効にするフラグを立てる
                status["click_disabled"] = True #クリックの無効をオンにする
                status["menu_start_time"] = time.time()  # メニュー配布開始時間を現在時刻にする
                status["countdown_time"] = 5  # カウントダウンをリセット
        if status["click_disabled"] == True :#クリックの無効をオンのとき
             if math.floor(time.time() - status["menu_start_time"])<6:# メニュー配布開始からの経過時刻が5秒経っていないとき
                  status["countdown_time"] -= 1#カウントダウンの表示を-1する
             else:# メニュー配布開始からの経過時刻が5秒経ったとき
                  status["waiting_regi_unserviced"] -=1 # メニューが配布されてない人を一人減らす
                  status["click_disabled"] = False #クリックの無効を解除する
                  status[click]=False #クリックを押されていないようにする
        return status
                 