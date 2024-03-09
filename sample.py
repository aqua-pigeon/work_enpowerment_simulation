import pygame
import sys
pygame.init()

# ウィンドウの設定
width, height = 1000, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Window")

# 色の定義 (RGB)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# フォントの読み込み
font = pygame.font.Font(None, 40)  # デフォルトフォント、サイズ36
# フォントの読み込み

# 待ち人数
wait_count = 0

# 待ち人数を増やすボタン
increase_button = pygame.Rect(50, 50, 200, 100)
increase_text = font.render("decrease", True, BLACK)
increase_text_rect = increase_text.get_rect(center=increase_button.center)

# カウントアップのイベント
INCREASE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_EVENT, 3000)  # 3000ミリ秒ごとに増加する


# テキストの作成
text1 = font.render("reji 1", True, WHITE)  # 白色のテキスト
text2 = font.render("reji 2", True, WHITE) 
text3 = font.render("Bar", True, BLACK) 
text4 = font.render("coffee", True, WHITE) 


# テキストの位置
text_rect1 = text1.get_rect()
text_rect1.center = (290,320)
text_rect2 = text2.get_rect()
text_rect2.center = (390,320)
text_rect3 = text3.get_rect()
text_rect3.center = (720,370)
text_rect4 = text4.get_rect()
text_rect4.center = (460,500)


# 画像の読み込み
image1 = pygame.image.load("barista.png")  # 任意の画像ファイル名
image2 = pygame.image.load("barista2.png")

# 画像の新しいサイズ
new_width, new_height = 80, 60

# 画像のサイズ変更
resized_image1 = pygame.transform.scale(image1, (new_width, new_height))
resized_image2 = pygame.transform.scale(image2, (new_width, new_height))

# 画像の位置
image_rect1 = resized_image1.get_rect()
image_rect1.center = (280,360)  # 画像をウィンドウの中央に配置
image_rect2 = resized_image2.get_rect()
image_rect2.center = (650,370)  # 画像をウィンドウの中央に配置

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)
    screen.blit(text3, text_rect3)
    screen.blit(text4, text_rect4)

    # 画像を描画
    screen.blit(resized_image1, image_rect1)
    screen.blit(resized_image2, image_rect2)

    # ボタンを描画
    pygame.draw.rect(screen, BLACK, increase_button)
    screen.blit(increase_text, increase_text_rect)

    # 待ち人数を表示
    count_text = font.render(f"Wait Count: {wait_count}", True, BLACK)
    screen.blit(count_text, (50, 200))

    # 画面を更新
    pygame.display.flip()

# Pygameの終了
pygame.quit()
sys.exit()

