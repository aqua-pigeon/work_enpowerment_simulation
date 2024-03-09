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
    width = int(os.getenv("SCREEN_WIDTH"))
    height = int(os.getenv("SCREEN_HEIGHT"))
    screen = pygame.display.set_mode((width, height))
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

def main():
    screen = screen_init()   # screenの取得

    wait_count = 0  # 待ち人数
    font = pygame.font.Font(None, 40)  # デフォルトフォント、サイズ40

    # 待ち人数を増やすボタン
    increase_button = pygame.Rect(50, 50, 200, 100)
    increase_text = font.render("decrease", True, BLACK)
    increase_text_rect = increase_text.get_rect(center=increase_button.center)

    # カウントアップのイベント
    INCREASE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(INCREASE_EVENT, 3000)  # 3000ミリ秒ごとに増加する

    # 画像の読み込み
    image1 = Img("img/barista.png", 80, 60)
    image2 = Img("img/barista2.png", 80, 60)

    # ゲームループ
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pygameの終了
                pygame.quit()
                sys.exit()
            elif event.type == INCREASE_EVENT:
                wait_count += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左クリック
                    if increase_button.collidepoint(event.pos):  # ボタンがクリックされたか確認
                        wait_count -= 1
                

        # 画面を白で塗りつぶす
        screen.fill(WHITE)

        # 矩形を描画
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

        # 画像を描画
        image1.draw(screen, 280, 360)
        image2.draw(screen, 650, 370)

        # ボタンを描画
        pygame.draw.rect(screen, BLACK, increase_button)
        screen.blit(increase_text, increase_text_rect)

        # 待ち人数を表示
        count_text = font.render(f"Wait Count: {wait_count}", True, BLACK)
        screen.blit(count_text, (50, 200))

        # 画面を更新
        pygame.display.flip()

if __name__ == "__main__":
    main()