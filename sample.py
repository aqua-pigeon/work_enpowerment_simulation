import pygame
import sys
import os
from dotenv import load_dotenv

pygame.init()  # Pygameの初期化
load_dotenv() #.envから環境変数を取得する。定数値の設定は別ファイルにしたほうが管理しやすいから

# 色の定義 (RGB)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def screen_init():
    # ウィンドウの設定
    screen_width = int(os.getenv("SCREEN_WIDTH"))
    screen_height = int(os.getenv("SCREEN_HEIGHT"))
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("WORK_ENVIRONMENT_SIMULATION")
    return screen 

class Img:
    # self.???はclass内でしか見えない変数=class変数
    # class変数はclassのインスタンス内でしか参照できない。
    # 同じImgクラスをもとにしていても、それぞれのインスタンスで別々の値を持つことができる。
    def __init__(self, path, w, h): #初期化関数. 画像のパスとサイズを受け取る
        img = pygame.image.load(path) #とりあえず画像を読み込む
        self.img = pygame.transform.scale(img, (w, h)) #画像のサイズを変更.結果はclassの中でしか見えないself.imgに保存

    def draw(self,screen,x,y): #画像を描画する関数
        image_rect=self.img.get_rect() # 画像の矩形を取得
        image_rect.center = (x,y)  # 画像をウィンドウの中央に配置
        screen.blit(self.img, image_rect) # 画像を描画

def draw_text(screen, text, x, y, font_size=40, color=BLACK):
    # フォントの設定
    font = pygame.font.Font(None, font_size)  # デフォルトフォント、サイズ40
    text = font.render(text, True, color)  # テキストの作成
    text_rect = text.get_rect()  # テキストの矩形を取得
    text_rect.center = (x, y)  # テキストをウィンドウの中央に配置
    screen.blit(text, text_rect)  # テキストを描画

def draw_field(screen):
    pygame.draw.rect(screen, GREEN, (200, 300, 650, 250), 3)  # 緑の矩形、枠線の太さ3
    pygame.draw.rect(screen, RED, (250, 300, 80, 50), 0)  # 青い矩形、塗りつぶし
    pygame.draw.rect(screen, RED, (350, 300, 80, 50), 0)  # 赤い矩形
    pygame.draw.rect(screen, GRAY, (500, 300, 300, 100), 0)  # 緑の矩形、枠線の太さ3
    pygame.draw.rect(screen, BLACK, (420, 480, 80, 70), 0)  # 緑の矩形、枠線の太さ3
    # テキストを描画
    draw_text(screen=screen, text="reji 1", x=290, y=320, font_size=40, color=WHITE)
    draw_text(screen=screen, text="reji 2", x=390, y=320, font_size=40, color=WHITE)
    draw_text(screen=screen, text="Bar", x=720, y=370, font_size=40, color=BLACK)
    draw_text(screen=screen, text="coffee", x=460, y=500, font_size=40, color=WHITE)

def draw_info_bar_frame(screen): #information barの静的な部分を描画
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    info_bar_height = int(screen_height/10)  # インフォメーションバーの高さ
    info_bar_width = int(screen_width/4)  # インフォメーションバーの幅
    img_width = int(info_bar_height*4/5)  # イメージアイコンの幅
    img_height = int(info_bar_height*4/5)  # イメージアイコンの高さ
    # インフォメーションバーを描画
    pygame.draw.rect(screen, BLACK, (0, 0, screen_width, info_bar_height), 1)  # 黒い矩形
    # インフォメーションバーを横4つに分割
    pygame.draw.line(screen, BLACK, (info_bar_width*1, 0), (info_bar_width*1, info_bar_height-1), 1)
    pygame.draw.line(screen, BLACK, (info_bar_width*2, 0), (info_bar_width*2, info_bar_height-1), 1)
    pygame.draw.line(screen, BLACK, (info_bar_width*3, 0), (info_bar_width*3, info_bar_height-1), 1)
    # イメージアイコンを取得
    img_waiting_bar=Img("img/figure_waiting.png", img_width*2, img_height)
    img_waiting_regi=Img("img/waiting_regi.png", img_width*2, img_height)
    img_codee_cup=Img("img/coffee_cup.png", img_width, img_height)
    img_espresso_maker=Img("img/espresso_maker.png", img_width, img_height)
    # イメージアイコンを描画
    img_waiting_regi.draw(screen, info_bar_width*0+info_bar_height, info_bar_height/2)
    img_waiting_bar.draw(screen, info_bar_width*1+info_bar_height, info_bar_height/2)
    img_codee_cup.draw(screen, info_bar_width*2+info_bar_height, info_bar_height/2)
    img_espresso_maker.draw(screen, info_bar_width*3+info_bar_height, info_bar_height/2)
    # テキストを描画
    draw_text(screen=screen, text="Waiting regi", x=int(info_bar_width*3/4), y=int(info_bar_height/4), font_size=int(info_bar_height/3), color=BLACK)
    draw_text(screen=screen, text="Waiting bar", x=int(info_bar_width*7/4), y=int(info_bar_height/4), font_size=int(info_bar_height/3), color=BLACK)
    draw_text(screen=screen, text="Served", x=int(info_bar_width*11/4), y=int(info_bar_height/4), font_size=int(info_bar_height/3), color=BLACK)
    draw_text(screen=screen, text="Drip Cofee", x=int(info_bar_width*15/4), y=int(info_bar_height/4), font_size=int(info_bar_height/3), color=BLACK)

def draw_info_bar_value(screen, waiting_regi, waiting_bar, served, drip_coffee): #information barの動的な部分を描画
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    info_bar_height = int(screen_height/10)  # インフォメーションバーの高さ
    info_bar_width = int(screen_width/4)  # インフォメーションバーの幅
    # フォントの設定
    font = pygame.font.Font(None, int(info_bar_height/3))  # デフォルトフォント、サイズ40
    # テキストを描画
    draw_text(screen=screen, text=f"{waiting_regi}", x=int(info_bar_width*3/4), y=int(info_bar_height*3/4), font_size=int(info_bar_height/3), color=BLACK)
    draw_text(screen=screen, text=f"{waiting_bar}", x=int(info_bar_width*7/4), y=int(info_bar_height*3/4), font_size=int(info_bar_height/3), color=BLACK)
    draw_text(screen=screen, text=f"{served}", x=int(info_bar_width*11/4), y=int(info_bar_height*3/4), font_size=int(info_bar_height/3), color=BLACK)
    draw_text(screen=screen, text=f"{drip_coffee}", x=int(info_bar_width*15/4), y=int(info_bar_height*3/4), font_size=int(info_bar_height/3), color=BLACK)

def main():
    screen = screen_init()   # screenの取得

    wait_count = 0  # 待ち人数
    # font = pygame.font.Font(None, 40)  # デフォルトフォント、サイズ40

    # 待ち人数を増やすボタン
    # increase_button = pygame.Rect(50, 50, 200, 100)
    # increase_text = font.render("decrease", True, BLACK)
    # increase_text_rect = increase_text.get_rect(center=increase_button.center)

    # カウントアップのイベント
    INCREASE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(INCREASE_EVENT, 3000)  # 3000ミリ秒ごとに増加する

    # 画像の読み込み
    img_regi_barista = Img("img/barista.png", 80, 60)
    img_bar_barista = Img("img/barista2.png", 80, 60)
    img_people=Img("img/figure_standing.png", 80, 60)

    # ゲームループ
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pygameの終了
                pygame.quit()
                sys.exit()
            elif event.type == INCREASE_EVENT:
                wait_count += 1
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:  # 左クリック
            #         if increase_button.collidepoint(event.pos):  # ボタンがクリックされたか確認
            #             wait_count -= 1
                

        # 画面を白で塗りつぶす
        screen.fill(WHITE)

        # フィールドを描画
        draw_field(screen)

        # インフォメーションバーを描画
        draw_info_bar_frame(screen)
        draw_info_bar_value(screen, wait_count, 0, 0, 0)

        # 画像を描画
        img_regi_barista.draw(screen, 280, 360)
        img_bar_barista.draw(screen, 650, 370)

        # ボタンを描画
        # pygame.draw.rect(screen, BLACK, increase_button)
        # screen.blit(increase_text, increase_text_rect)

        # 画面を更新
        pygame.display.flip()

if __name__ == "__main__":
    main()