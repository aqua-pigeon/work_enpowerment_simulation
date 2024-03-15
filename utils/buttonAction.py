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
    

# status["drip_meter"] = 5
# status["countdown_time"] = 5  # カウントダウン時間をリセット


#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#         #     if not click_disabled and event.button == 1:  # 左クリック
                # mouse_x, mouse_y = pygame.mouse.get_pos()
                # レジ2の領域がボタンとして押されたかどうかを確認

                # if 350 < mouse_x < 430 and 300 < mouse_y < 350:
                #     status["regi_baristaNum"] += 1
                #     if event.button == 1:  # 左クリック
                #         mouse_x, mouse_y = pygame.mouse.get_pos()
                #         # レジ2の領域がボタンとして押されたかどうかを確認
                #         if 350 < mouse_x < 430 and 300 < mouse_y < 350:
                #             status["regi_baristaNum"] -= 1

                # if event.button == 1:  # 左クリック
                #     mouse_pos = pygame.mouse.get_pos()  # マウスの座標を取得
                #     # マウスの座標がドリップコーヒーの領域内にあるかどうかを確認
                #     if bar_rect.collidepoint(mouse_pos):
                #         status["bar_baristaNum"] += 1

#                 if  status["click_disabled"]==False and event.button == 1:  # 左クリック
#                         mouse_pos = pygame.mouse.get_pos()  # マウスの座標を取得
#                         # マウスの座標がドリップコーヒーの領域内にあるかどうかを確認
#                         if drip_coffee_rect.collidepoint(mouse_pos):
#                                 # クリックを無効にするフラグを立てる
#                                 status["click_disabled"] = True
                               
#     def set_drip(status):             
#         if  status["click_disabled"]==False and event.button == 1:  # 左クリック
#                 mouse_pos = pygame.mouse.get_pos()  # マウスの座標を取得
#                 # マウスの座標がドリップコーヒーの領域内にあるかどうかを確認
#                 if drip_coffee_rect.collidepoint(mouse_pos):
#                         # クリックを無効にするフラグを立てる
#                         status["click_disabled"] = True
#                         # クリックが無効な場合、カウントダウンを表示
#                 if status["click_disabled"] == True:
#                         # カウントダウンの残り時間を計算
#                         if status["countdown_time"] > 0:
#                                 status["countdown_time"]-=1     
#                          # カウントダウンが終了したらクリックを有効にする
#                         if status["countdown_time"] <=0:
#                                 status["drip_meter"] == 5
#                                 status["click_disabled"] = False
        
           
# import os

# from dotenv import load_dotenv

# load_dotenv()  # .envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから

# COUNT_DECREASE = int(os.getenv("COUNT_DECREASE"))
# COUNT_TIME = int(os.getenv("COUNT_TIME"))




def count_decrease(status):
    if (
        status["elapsed_time"] % COUNT_DECREASE == 0
    ):  # 10秒経過するごとにドリップの残量を減らす. ただし、前回の減少から10秒経過していない場合は減少しない
        if drip_decrease_flag == False:
            if status["drip_meter"] > 0:
                status["drip_meter"] -= 1
            drip_decrease_flag = True
    else:
        drip_decrease_flag = False
    return status