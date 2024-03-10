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

    # # 待ち人数を増やすボタン
    # increase_button = pygame.Rect(50, 50, 200, 100)
    # increase_text = font.render("decrease", True, BLACK)
    # increase_text_rect = increase_text.get_rect(center=increase_button.center)

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
    image1 = Img("img/barista.png", 80, 60)
    image2 = Img("img/barista2.png", 80, 60)

    # ゲームループ
    running = True
    reg1_time = 300
    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # マウスの左ボタンがクリックされた場合
                    mouse_x, mouse_y = event.pos
                    if 350 <= mouse_x <= 430 and 300 <= mouse_y <= 350:  # レジ2の矩形がクリックされた場合
                        if reg2_free:  # レジ2が空いている場合
                            reg2_free = False
                            reg2_time = 300  # レジ2の接客時間は10秒とする
                            wait_count -= 1  # 待ち人数を1人減らす
                        # else:  # レジ2が稼働中の場合
                        #     reg1_free = True  # レジ1も稼働する
                        #     reg2_time = 300  # レジ2の接客時間は10秒とする
                        #     wait_count -= 1  # 待ち人数を1人減らす

        # お客さんの増加
        customer_timer += 1
        if customer_timer % 450 == 0:
            wait_count += 1
        if customer_timer % 900 == 0:
            wait_count += 2

        # レジ1の処理
        reg1_time = 300
        if  not reg1_free:
            reg1_time -= 1
            if reg1_time <= 0:
                reg1_free = True
                wait_count -= 1

        # レジ2の処理
        if not reg2_free:
            reg2_time -= 1
            if reg2_time <= 0:
                reg2_free = True
                wait_count -= 1


    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:  # Pygameの終了
    #             pygame.quit()
            #     sys.exit()
            # elif event.type == INCREASE_EVENT:
            #     wait_count += 1
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:  # 左クリック
            #         if increase_button.collidepoint(event.pos):  # ボタンがクリックされたか確認
            #             wait_count -= 1
    

            
                

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

        # 待ち人数を表示
        wait_text = font.render(f"Wait Count: {wait_count}", True, BLACK)
        screen.blit(wait_text, (50, 50))

        # レジの状態を表示
        reg1_text = font.render(f"Register 1: {'Free' if reg1_free else 'Busy'}", True, BLACK)
        screen.blit(reg1_text, (50, 100))

        reg2_text = font.render(f"Register 2: {'Free' if reg2_free else 'Busy'}", True, BLACK)
        screen.blit(reg2_text, (50, 150))

        # レジ2のボタンの状態を表示
        pygame.draw.rect(screen, GREEN if reg2_free else RED, pygame.Rect(350, 300, 80, 50))

        # 接客カウントダウンを表示
        if not reg1_free:
            reg1_timer_text = font.render(f"Reg1: {reg1_time}", True, BLACK)
            screen.blit(reg1_timer_text, (50, 200))

        if not reg2_free:
            reg2_timer_text = font.render(f"Reg2: {reg2_time}", True, BLACK)
            screen.blit(reg2_timer_text, (50, 250))

        # # ボタンを描画
        # pygame.draw.rect(screen, BLACK, increase_button)
        # screen.blit(increase_text, increase_text_rect)

        # # 待ち人数を表示
        # count_text = font.render(f"Wait Count: {wait_count}", True, BLACK)
        # screen.blit(count_text, (50, 200))


        # 画面を更新
        pygame.display.flip()

        # ゲームのフレームレートを設定
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()