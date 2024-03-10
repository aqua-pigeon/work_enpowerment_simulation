import sys

import pygame

import utils.ImgClass as ImgClass
import utils.ScreenClass as ScreenClass

pygame.init()  # Pygameの初期化


def main():
    screen_instance = ScreenClass.Screen()  # screenClassのインスタンスを生成

    wait_count = 0  # 待ち人数

    # # カウントアップのイベント
    # INCREASE_EVENT = pygame.USEREVENT + 1
    # pygame.time.set_timer(INCREASE_EVENT, 3000)  # 3000ミリ秒ごとに増加する

    # レジの状態
    reg1_free = False
    reg2_free = True

    # レジの接客カウントダウン
    reg1_time = 0
    reg2_time = 0

    # お客さんの増加タイマー
    customer_timer = 0

    # レジ2のボタンの状態
    reg2_button_clicked = False

    # 画像の読み込み
    img_people = ImgClass.Img("img/figure_standing.png", 80, 60)

    # ゲームループ
    running = True
    reg1_time = 300
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pygameの終了
                pygame.quit()
                sys.exit()

        screen_instance.clear()  # 画面を白で塗りつぶす
        screen_instance.draw_field()  # フィールドを描画

        screen_instance.draw_info_bar_frame()  # インフォメーションバーの静的コンテンツを描画
        screen_instance.draw_info_bar_value(
            waiting_regi=wait_count, waiting_bar=0, served=0, drip_coffee=0
        )  # インフォメーションバーの動的コンテンツを描画

        screen_instance.draw_regi_barista(regi_num=1)  # レジ1のバリスタを描画
        screen_instance.draw_regi_barista(regi_num=2)  # レジ2のバリスタを描画
        screen_instance.draw_bar_barista(barista_num=1)  # バー1のバリスタを描画
        screen_instance.draw_bar_barista(barista_num=2)  # バー2のバリスタを描画
        screen_instance.draw_drip_barista()

        pygame.display.flip()  # 画面を更新


if __name__ == "__main__":
    main()
