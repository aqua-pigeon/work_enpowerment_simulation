import time

import pygame


def set_event(status):
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
