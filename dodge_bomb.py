import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
move_d = {
    pg.K_UP:(0, -5), 
    pg.K_DOWN:(0, +5), 
    pg.K_LEFT:(-5, 0), 
    pg.K_RIGHT:(+5, 0)
}


def check_bound(rect : pg.rect) -> tuple[bool, bool]:
    """
    こうかとんrect,爆弾rectが画面外、画面内かを判定する関数
    引数：こうかとんrect or 爆弾rect
    戻り値：横方向，縦方向のはみ出し判定結果（画面内：True／画面外：False）
    """
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right:  #横方向判定
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:  #縦方向判定
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    #ここから3行は左向きの三体のSurfaceを作っている
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)  
    kk_img2 = pg.transform.rotozoom(kk_img, 45, 1.0)
    kk_img3 = pg.transform.rotozoom(kk_img, 315, 1.0)
    #ここから6行は右向きの五体のSurfaceを作っている
    kk_img4 = pg.transform.flip(kk_img, True, False)  
    kk_img4 = pg.transform.rotozoom(kk_img4, 0, 1.0)
    kk_img5 = pg.transform.rotozoom(kk_img4, 45, 1.0)
    kk_img6 = pg.transform.rotozoom(kk_img4, 90, 1.0)
    kk_img7 = pg.transform.rotozoom(kk_img4, 315, 1.0)
    kk_img8 = pg.transform.rotozoom(kk_img4, 270, 1.0)
    direction_d = {
        (0, 0):kk_img,
        (-5, 0):kk_img,
        (-5, +5):kk_img2,
        (-5, -5):kk_img3,
        (+5, 0): kk_img4,
        (+5, -5):kk_img5,
        (0, -5):kk_img6,
        (+5, +5):kk_img7,
        (0, +5):kk_img8
    }
    rect_kk_img = kk_img.get_rect()
    rect_kk_img.center = 900, 400
    accs = [a for a in range(1, 11)]  #爆弾の加速度のリスト
    bb_img = pg.Surface((20, 20))  #練習Ⅰ
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_img.set_colorkey((0, 0, 0))
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    rect_bb_img = bb_img.get_rect()
    rect_bb_img.center = x, y  
    #爆弾Rectの位置を表す変数に乱数を設定する
    vx, vy = +5, +5  #練習2 
    clock = pg.time.Clock()
    tmr = 0
    """whileまでの以下のコードは追加課題2の途中
    avx = 0
    avy = 0
    bb_imgs = []
    for r in range(1, 11):
        bb_img = pg.Surface((20*r, 20*r))
        pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r)
        bb_imgs.append(bb_img)
    avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)] """

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        if rect_kk_img.colliderect(rect_bb_img):  #練習5
            print("Game Over")
            return  #ゲーム終了

        key_lst = pg.key.get_pressed()
        total_mv =  [0, 0]
        for k, mv in move_d.items():
            if key_lst[k]:
                total_mv[0] += mv[0]
                total_mv[1] += mv[1]
        rect_kk_img.move_ip(total_mv)
        
        if check_bound(rect_kk_img) != (True, True):
            rect_kk_img.move_ip(-total_mv[0], -total_mv[1])
        
        screen.blit(bg_img, [0, 0])
        #押下されたキーにしたがって，kk_imgをrotozoomしたSurfaceをblitする
        screen.blit(direction_d[tuple(total_mv)], rect_kk_img)  
        #avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]  検討中
        rect_bb_img.move_ip(vx, vy)
        yoko, tate = check_bound(rect_bb_img)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bb_img,rect_bb_img)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()