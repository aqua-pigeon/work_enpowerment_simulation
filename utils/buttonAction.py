import time

import pygame


class ButtonAction:
    last_click_time = 0  # 最後にクリックされた時間
    click_time = 0  # クリックされた時間
    disable_set_time = 0  # クリックが無効になった時間
    click_disable = False  # クリックが無効かどうか
    disable_limit_time = None  # クリックが無効になる時間

    def __init__(self, area_coordinate):
        self.area_coordinate = area_coordinate  # ボタンの領域を表すRectオブジェクト
        self.area_rect = pygame.Rect(
            area_coordinate
        )  # ボタンの領域を表すRectオブジェクト

    def check_button(self, events):  # ボタンがクリックされたかどうかを確認
        if (
            self.click_disable  # クリックが無効になっている場合
            and not self.disable_limit_time
            == None  # カウントダウン時間が設定されている場合
            and time.time() - self.disable_set_time
            > self.countdown_time  # カウントダウン時間が経過した場合
        ):
            self.click_disable = False  # クリックを有効にするフラグを立てる

        if not self.click_disable:  # クリックが有効な場合
            for event in events:  # pygame画面でのイベントを取得
                if event.type == pygame.MOUSEBUTTONDOWN:  # クリックされた場合
                    mouse_pos = pygame.mouse.get_pos()  # マウスの座標を取得
                    if self.area_rect.collidepoint(
                        mouse_pos
                    ):  # マウスの座標がボタンの領域内にあるかどうかを確認
                        self.click_time = time.time()  # クリックされた時間を記録
                        return True

        return False  # ボタンクリックが無効 または ボタンクリックが有効だがクリックされていない場合

    def set_disabled(self, limit_time=None):
        self.click_disable = True  # クリックを無効にするフラグを立てる
        self.disable_set_time = time.time()
        self.countdown_time = limit_time  # カウントダウン時間を設定(秒)


# def set_drip(status):
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if status["click_disable"] and event.button == 1:  # 左クリック
#                 mouse_pos = pygame.mouse.get_pos()  # マウスの座標を取得
#                 # マウスの座標がドリップコーヒーの領域内にあるかどうかを確認
#                 if drip_coffee_rect.collidepoint(mouse_pos):
#                     # クリックを無効にするフラグを立てる
#                     status["click_disable"] = True
#                     # カウントダウンが終了したらクリックを有効にする

#         if status["elapsed_time"] % 1 == 0:
#             if status["click_disable"] == True:
#                 # カウントダウンの残り時間を計算
#                 if status["countdown_time"] > 0:
#                     status["countdown_time"] -= 1
#                     # カウントダウンが終了したらクリックを有効にする
#                 status["click_disable"] = False
#                 if status["countdown"] <= 0:
#                     status["drip_meter"] = 5
#                     status["countdown_time"] = 5  # カウントダウン時間をリセット
#                     status["click_disable"] = False
#         else:
#             status["click_disable"] = False
#     return status

# def menu_serve(status):
#     if status[click]==True:
#           if menu_rect.collidepoint(mouse_pos):
#      # クリックを無効にするフラグを立てる
#             status["click_disabled"] = True #クリックの無効をオンにする
#             status["menu_start_time"] = time.time()  # メニュー配布開始時間を現在時刻にする
#             status["countdown_time"] = 5  # カウントダウンをリセット
#     if status["click_disabled"] == True :#クリックの無効をオンのとき
#          if math.floor(time.time() - status["menu_start_time"])<6:# メニュー配布開始からの経過時刻が5秒経っていないとき
#               status["countdown_time"] -= 1#カウントダウンの表示を-1する
#          else:# メニュー配布開始からの経過時刻が5秒経ったとき
#               status["waiting_regi_unserviced"] -=1 # メニューが配布されてない人を一人減らす
#               status["click_disabled"] = False #クリックの無効を解除する
#               status[click]=False #クリックを押されていないようにする
#     return status
