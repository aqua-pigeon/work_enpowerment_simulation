import os

import pygame
from dotenv import load_dotenv

import utils.ImgClass as ImgClass

load_dotenv()  # .envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから

# 色の定義 (RGB)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Screen:
    def __init__(self):
        # ウィンドウの設定
        screen_width = int(os.getenv("SCREEN_WIDTH"))
        screen_height = int(os.getenv("SCREEN_HEIGHT"))
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("WORK_ENVIRONMENT_SIMULATION")

    def clear(self):
        self.screen.fill(WHITE)

    def draw_text(self, text, x, y, font_size=40, color=BLACK):
        # フォントの設定
        font = pygame.font.Font(None, font_size)  # デフォルトフォント、サイズ40
        text = font.render(text, True, color)  # テキストの作成
        text_rect = text.get_rect()  # テキストの矩形を取得
        text_rect.center = (x, y)  # テキストをウィンドウの中央に配置
        self.screen.blit(text, text_rect)  # テキストを描画

    def draw_field(self):
        # 座標=(x, y , 幅, 高さ)
        pygame.draw.rect(self.screen, GREEN, (200, 300, 650, 250), 3)  # field
        pygame.draw.rect(self.screen, RED, (250, 300, 80, 50), 0)  # regi1
        pygame.draw.rect(self.screen, RED, (350, 300, 80, 50), 0)  # regi2
        pygame.draw.rect(self.screen, GRAY, (500, 300, 300, 100), 0)  # bar
        pygame.draw.rect(self.screen, BLACK, (420, 480, 80, 70), 0)  # drip coffee
        # テキストを描画
        self.draw_text(text="regi 1", x=290, y=325, font_size=40, color=WHITE)
        self.draw_text(text="regi 2", x=390, y=325, font_size=40, color=WHITE)
        self.draw_text(text="Bar", x=650, y=350, font_size=40, color=BLACK)
        self.draw_text(text="Drip", x=460, y=515, font_size=40, color=WHITE)

    def draw_regi_barista(self, regi_num):
        img_height = 60
        img_width = 80
        img1_x = 290
        img2_x = 390
        height_offset = int(img_height * 3 / 4)
        img_y = 325 + height_offset
        img_regi_barista = ImgClass.Img("img/barista.png", img_width, img_height)
        if regi_num == 1:
            img_regi_barista.draw(self.screen, img1_x, img_y)
        elif regi_num == 2:
            img_regi_barista.draw(self.screen, img2_x, img_y)

    def draw_bar_barista(self, barista_num):
        img_height = 60
        img_width = 80
        img1_x = 600
        img2_x = 700
        height_offset = int(img_height * 3 / 4)
        img_y = 350 + height_offset
        img_bar_barista = ImgClass.Img("img/barista2.png", img_width, img_height)
        if barista_num == 1:
            img_bar_barista.draw(self.screen, img1_x, img_y)
        elif barista_num == 2:
            img_bar_barista.draw(self.screen, img2_x, img_y)

    def draw_drip_barista(self):
        img_height = 60
        img_width = 80
        img1_x = 420
        height_offset = int(img_height * 3 / 4)
        img_y = 515 - height_offset
        img_drip_barista = ImgClass.Img("img/barista.png", img_width, img_height)
        img_drip_barista.draw(self.screen, img1_x, img_y)

    def draw_info_bar_frame(self):  # information barの静的な部分を描画
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        info_bar_height = int(screen_height / 10)  # インフォメーションバーの高さ
        info_bar_width = int(screen_width / 4)  # インフォメーションバーの幅
        img_width = int(info_bar_height * 4 / 5)  # イメージアイコンの幅
        img_height = int(info_bar_height * 4 / 5)  # イメージアイコンの高さ
        # インフォメーションバーを描画
        pygame.draw.rect(
            self.screen, BLACK, (0, 0, screen_width, info_bar_height), 1
        )  # 黒い矩形
        # インフォメーションバーを横4つに分割
        pygame.draw.line(
            self.screen,
            BLACK,
            (info_bar_width * 1, 0),
            (info_bar_width * 1, info_bar_height - 1),
            1,
        )
        pygame.draw.line(
            self.screen,
            BLACK,
            (info_bar_width * 2, 0),
            (info_bar_width * 2, info_bar_height - 1),
            1,
        )
        pygame.draw.line(
            self.screen,
            BLACK,
            (info_bar_width * 3, 0),
            (info_bar_width * 3, info_bar_height - 1),
            1,
        )
        # イメージアイコンを取得
        img_waiting_bar = ImgClass.Img(
            "img/figure_waiting.png", img_width * 2, img_height
        )
        img_waiting_regi = ImgClass.Img(
            "img/waiting_regi.png", img_width * 2, img_height
        )
        img_codee_cup = ImgClass.Img("img/coffee_cup.png", img_width, img_height)
        img_espresso_maker = ImgClass.Img(
            "img/espresso_maker.png", img_width, img_height
        )
        # イメージアイコンを描画
        img_waiting_regi.draw(
            self.screen, info_bar_width * 0 + info_bar_height, info_bar_height / 2
        )
        img_waiting_bar.draw(
            self.screen, info_bar_width * 1 + info_bar_height, info_bar_height / 2
        )
        img_codee_cup.draw(
            self.screen, info_bar_width * 2 + info_bar_height, info_bar_height / 2
        )
        img_espresso_maker.draw(
            self.screen, info_bar_width * 3 + info_bar_height, info_bar_height / 2
        )
        # テキストを描画
        self.draw_text(
            text="Waiting regi",
            x=int(info_bar_width * 3 / 4),
            y=int(info_bar_height / 4),
            font_size=int(info_bar_height / 3),
            color=BLACK,
        )
        self.draw_text(
            text="Waiting bar",
            x=int(info_bar_width * 7 / 4),
            y=int(info_bar_height / 4),
            font_size=int(info_bar_height / 3),
            color=BLACK,
        )
        self.draw_text(
            text="Served",
            x=int(info_bar_width * 11 / 4),
            y=int(info_bar_height / 4),
            font_size=int(info_bar_height / 3),
            color=BLACK,
        )
        self.draw_text(
            text="Drip Cofee",
            x=int(info_bar_width * 15 / 4),
            y=int(info_bar_height / 4),
            font_size=int(info_bar_height / 3),
            color=BLACK,
        )

    def draw_info_bar_value(
        self, waiting_regi, waiting_bar, served, drip_coffee
    ):  # information barの動的な部分を描画
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        info_bar_height = int(screen_height / 10)  # インフォメーションバーの高さ
        info_bar_width = int(screen_width / 4)  # インフォメーションバーの幅
        # フォントの設定
        font = pygame.font.Font(
            None, int(info_bar_height / 3)
        )  # デフォルトフォント、サイズ40
        # テキストを描画
        self.draw_text(
            text=f"{waiting_regi}",
            x=int(info_bar_width * 3 / 4),
            y=int(info_bar_height * 3 / 4),
            font_size=int(info_bar_height / 3),
            color=BLACK,
        )
        self.draw_text(
            text=f"{waiting_bar}",
            x=int(info_bar_width * 7 / 4),
            y=int(info_bar_height * 3 / 4),
            font_size=int(info_bar_height / 3),
            color=BLACK,
        )
        self.draw_text(
            text=f"{served}",
            x=int(info_bar_width * 11 / 4),
            y=int(info_bar_height * 3 / 4),
            font_size=int(info_bar_height / 3),
            color=BLACK,
        )
        self.draw_text(
            text=f"{drip_coffee}",
            x=int(info_bar_width * 15 / 4),
            y=int(info_bar_height * 3 / 4),
            font_size=int(info_bar_height / 3),
            color=BLACK,
        )
