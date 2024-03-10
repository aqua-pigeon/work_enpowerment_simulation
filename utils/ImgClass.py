import pygame

class Img:
    # self.???はclass内でしか見えない変数=class変数
    # class変数はclassのインスタンス内でしか参照できない。
    # 同じImgクラスをもとにしていても、それぞれのインスタンスで別々の値を持つことができる。
    def __init__(self, path, w, h):  # 初期化関数. 画像のパスとサイズを受け取る
        img = pygame.image.load(path)  # とりあえず画像を読み込む
        self.img = pygame.transform.scale(
            img, (w, h)
        )  # 画像のサイズを変更.結果はclassの中でしか見えないself.imgに保存

    def draw(self, screen, x, y):  # 画像を描画する関数
        image_rect = self.img.get_rect()  # 画像の矩形を取得
        image_rect.center = (x, y)  # 画像をウィンドウの中央に配置
        screen.blit(self.img, image_rect)  # 画像を描画
