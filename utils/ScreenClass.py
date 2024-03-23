import os

import cv2
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
BROWN = (165, 42, 42)
CREAM = (255, 238, 205)


class Screen:
    field_object_coordinates = {
        "field": (200, 300, 650, 250),
        "regi1": (250, 300, 80, 50),
        "regi2": (350, 300, 80, 50),
        "bar": (500, 300, 300, 100),
        "drip_coffee": (420, 480, 80, 70),
        "menu": (60, 200, 100, 90),
    }
    frame_count = (
        -1
    )  # 録画時に使用するフレームカウント. record_frame_intervalごとに動画に出力

    def __init__(self, log_file_name):
        # ウィンドウの設定
        pygame.init()  # Pygameの初期化
        self.width = int(os.getenv("SCREEN_WIDTH"))
        self.height = int(os.getenv("SCREEN_HEIGHT"))
        self.record_fps = int(os.getenv("RECORD_FPS"))  # 1秒間に何回画像を保存するか
        self.input_fps = int(
            os.getenv("INPUT_FPS")
        )  # 1秒間に何回ユーザーからの入力を受け付けるか
        self.record_frame_interval = (
            self.input_fps // self.record_fps
        )  # 何フレームごとに画像を保存するか
        self.output_file = log_file_name + ".mp4"
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("WORK_ENVIRONMENT_SIMULATION")
        self.clock = pygame.time.Clock()
        # 動画ファイルの設定
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.video_writer = cv2.VideoWriter(
            self.output_file, fourcc, self.record_fps, (self.width, self.height)
        )

    def record(self):
        self.frame_count += 1
        print(self.frame_count)
        if self.frame_count % self.record_frame_interval == 0:
            # 画面をキャプチャして動画ファイルに保存
            screen = pygame.display.get_surface()
            screen = pygame.surfarray.pixels3d(screen)
            screen = cv2.transpose(screen)
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
            self.video_writer.write(screen)

    def record_stop(self):  # 動画ファイルを閉じる
        self.video_writer.release()

    def quit(self):  # Pygameを終了
        self.record_stop()
        pygame.quit()

    def clear(self):
        self.screen.fill(CREAM)

    def draw_text(self, text, x, y, font_size=40, color=BLACK):
        # フォントの設定
        font = pygame.font.Font(None, font_size)  # デフォルトフォント、サイズ40
        text = font.render(text, True, color)  # テキストの作成
        text_rect = text.get_rect()  # テキストの矩形を取得
        text_rect.center = (x, y)  # テキストをウィンドウの中央に配置
        self.screen.blit(text, text_rect)  # テキストを描画

    def draw_field(self):
        # 座標=(x, y , 幅, 高さ)
        pygame.draw.rect(
            self.screen, GREEN, self.field_object_coordinates["field"], 3
        )  # field
        pygame.draw.rect(
            self.screen, RED, self.field_object_coordinates["regi1"], 0
        )  # regi1
        pygame.draw.rect(
            self.screen, RED, self.field_object_coordinates["regi2"], 0
        )  # regi2
        pygame.draw.rect(
            self.screen, GRAY, self.field_object_coordinates["bar"], 0
        )  # bar
        pygame.draw.rect(
            self.screen, BLACK, self.field_object_coordinates["drip_coffee"], 0
        )
        pygame.draw.rect(
            self.screen, BLUE, self.field_object_coordinates["menu"], 0
        )  # drip coffee
        # テキストを描画
        self.draw_text(text="regi 1", x=290, y=325, font_size=40, color=WHITE)
        self.draw_text(text="regi 2", x=390, y=325, font_size=40, color=WHITE)
        self.draw_text(text="Bar", x=650, y=350, font_size=40, color=BLACK)
        self.draw_text(text="Drip", x=460, y=515, font_size=40, color=WHITE)
        self.draw_text(text="Menu", x=110, y=240, font_size=40, color=WHITE)

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
            self.screen, BLACK, (50, 600, screen_width / 4, info_bar_height), 1
        )  # 黒い矩形

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
        img_menu = ImgClass.Img("img/menu.png", img_width * 2, img_height * 2)
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
        img_menu.draw(self.screen, 110, 150)

        # テキストを描画
        self.draw_text(
            text="Countdown",
            x=100,
            y=620,
            font_size=int(info_bar_height / 3),
            color=BLACK,
        )

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

    def draw_cool_time(
        self, *args
    ):  # クールタイムを描画. 可変長引数をとるので*argsを使う。可変長引数は、0~n個の引数を受け取ることができて、何個引数があるかわからない場合に便利!（print()関数も同じ構造）
        time_sum = sum(args)  # クールタイムの合計を計算
        self.draw_text(
            text=f"{time_sum}",
            x=100,
            y=650,
            font_size=40,
            color=BLACK,
        )

    def draw_regi_waitingPeople(self, status):
        img_width = 80
        img_height = 60
        img_people = ImgClass.Img(
            "img/figure_standing.png", img_width, img_height
        )  # 画像の読み込み
        img_people_served = ImgClass.Img(
            "img/serverd.png", img_width, img_height
        )  # 画像の読み込み
        img_people_double = ImgClass.Img(
            "img/figure_talking.png", img_width, img_height
        )  # 画像の読み込み
        img_people_served_double = ImgClass.Img(
            "img/serverd_double.png", img_width, img_height
        )  # 画像の読み込み

        regi_x_1 = 290
        rigi_x_2 = 390
        regi_x_center = (regi_x_1 + rigi_x_2) // 2
        regi_y = 300
        regi_y_offset = 20
        queue_y_offset = 40
        queue_y_length = 100
        queue_y_end = regi_y - queue_y_offset
        queue_y_start = queue_y_end - queue_y_length

        # 0=いない,1=普通の人,2=VIP,3=メニューを持った普通の人,4=メニューを持ったVIP
        regi1_customer = status["regi1_customer"]
        regi2_customer = status["regi2_customer"]
        if regi1_customer == None:
            pass
        elif regi1_customer["num"] == 1:
            if regi1_customer["menued"] == False:
                img_people.draw(self.screen, regi_x_1, regi_y - regi_y_offset)
            else:
                img_people_served.draw(self.screen, regi_x_1, regi_y - regi_y_offset)
        elif regi1_customer["num"] == 2:
            if regi1_customer["menued"] == False:
                img_people_double.draw(self.screen, regi_x_1, regi_y - regi_y_offset)
            else:
                img_people_served_double.draw(
                    self.screen, regi_x_1, regi_y - regi_y_offset
                )
        if regi2_customer == None:
            pass
        elif regi2_customer["num"] == 1:
            if regi2_customer["menued"] == False:
                img_people.draw(self.screen, rigi_x_2, regi_y - regi_y_offset)
            else:
                img_people_served.draw(self.screen, rigi_x_2, regi_y - regi_y_offset)
        elif regi2_customer["num"] == 2:
            if regi2_customer["menued"] == False:
                img_people_double.draw(self.screen, rigi_x_2, regi_y - regi_y_offset)
            else:
                img_people_served_double.draw(
                    self.screen, rigi_x_2, regi_y - regi_y_offset
                )

        queue_len = len(status["waiting_regi_queue"])
        for index in range(len(status["waiting_regi_queue"])):  # 待ち行列の描画
            i = status["waiting_regi_queue"][queue_len - index - 1]
            queue_y = queue_y_end - queue_y_length / len(
                status["waiting_regi_queue"]
            ) * (queue_len - index)
            if i["num"] == 1:
                if i["menued"] == False:
                    img_people.draw(self.screen, regi_x_center, queue_y)
                else:
                    img_people_served.draw(self.screen, regi_x_center, queue_y)
            elif i["num"] == 2:
                if i["menued"] == False:
                    img_people_double.draw(self.screen, regi_x_center, queue_y)
                else:
                    img_people_served_double.draw(self.screen, regi_x_center, queue_y)

    def draw_bar_waitingPeople(self, waitingNum):
        img_width = 80
        img_height = 60
        img_people = ImgClass.Img(
            "img/coffee_cup_paper.png", img_width * 3 / 4, img_height
        )  # 画像の読み込み
        bar_center_y = 450
        bar_x = 800
        queue_x_length = 200
        for i in range(waitingNum - 1, -1, -1):
            queue_x = bar_x - queue_x_length / waitingNum * i
            img_people.draw(self.screen, queue_x, bar_center_y)

    def draw_drip_meter(self, dripNum):
        gage_num = 5
        meter_x_start = 510
        meter_y_start = 495
        meter_width = 30
        meter_height = 50
        meter_row_height = int(meter_height / gage_num)

        # メーターの中身を描画
        for i in range(dripNum):
            meter_y = meter_y_start + meter_row_height * (gage_num - 1 - i)
            pygame.draw.rect(
                self.screen,
                BROWN,
                (meter_x_start, meter_y, meter_width, meter_row_height),
                0,
            )

        # メーターの枠を描画
        pygame.draw.rect(
            self.screen,
            BLACK,
            (meter_x_start, meter_y_start, meter_width, meter_height),
            1,
        )

        # メーターの仕切りを描画
        for i in range(gage_num):
            meter_y = meter_y_start + meter_row_height * i
            pygame.draw.line(
                self.screen,
                BLACK,
                (meter_x_start, meter_y),
                (meter_x_start + meter_width - 1, meter_y),
                1,
            )
        # テキストを描画(n/gage_num)
        self.draw_text(
            text=f"{dripNum}/{gage_num}",
            x=int(meter_x_start + meter_width / 2),
            y=int(meter_y_start - 10),
            font_size=20,
            color=BLACK,
        )
