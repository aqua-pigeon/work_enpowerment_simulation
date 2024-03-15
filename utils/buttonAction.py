import time

import pygame

regi_rect = (350, 300, 80, 50)
bar_rect = (500, 300, 300, 100)
drip_coffee_rect = (420, 480, 80, 70)

# # クリックを無効にするフラグとカウントダウンの時間
# click_disabled = False
# countdown_time = 5
# start_time = None



# def set_event(status):
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
            # if not click_disabled and event.button == 1:  # 左クリック
            #     mouse_x, mouse_y = pygame.mouse.get_pos()
            #     # レジ2の領域がボタンとして押されたかどうかを確認
            #     if 350 < mouse_x < 430 and 300 < mouse_y < 350:
            #         status["regi_baristaNum"] += 1
            #         if event.button == 1:  # 左クリック
            #             mouse_x, mouse_y = pygame.mouse.get_pos()
            #             # レジ2の領域がボタンとして押されたかどうかを確認
            #             if 350 < mouse_x < 430 and 300 < mouse_y < 350:
            #                 status["regi_baristaNum"] -= 1

            #     if event.button == 1:  # 左クリック
            #         mouse_pos = pygame.mouse.get_pos()  # マウスの座標を取得
            #         # マウスの座標がドリップコーヒーの領域内にあるかどうかを確認
            #         if bar_rect.collidepoint(mouse_pos):
            #             status["bar_baristaNum"] += 1

    #             if not click_disabled and event.button == 1:  # 左クリック
    #                 mouse_pos = pygame.mouse.get_pos()  # マウスの座標を取得
    #                 # マウスの座標がドリップコーヒーの領域内にあるかどうかを確認
    #                 if drip_coffee_rect.collidepoint(mouse_pos):
                        
    #                     # クリックを無効にするフラグを立てる
    #                     click_disabled = True
    #                     # カウントダウンの開始時間を記録
    #                     start_time = time.time()
    #                     status["drip_meter"] += 5

    # # クリックが無効な場合、カウントダウンを表示
    # if click_disabled:
    #     # カウントダウンの残り時間を計算
    #     elapse_time = time.time() - start_time
    #     remaining_time = max(0, countdown_time - int(elapse_time))
    #     # カウントダウンのテキストを作成
    #     countdown_text = font.render(f"Remaining: {remaining_time}", True, (0, 0, 0))
    #     screen.blit(countdown_text, (100, 200))

    #     # カウントダウンが終了したらクリックを有効にする
    #     if remaining_time == 0:
    #         click_disabled = False
    #         start_time = None
