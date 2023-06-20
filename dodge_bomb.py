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


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    rect_kk_img = kk_img.get_rect()
    rect_kk_img.center = 900, 400
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

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()
        total_mv =  [0, 0]
        for k, mv in move_d.items():
            if key_lst[k]:
                total_mv[0] += mv[0]
                total_mv[1] += mv[1]
        """total_move =  [0, 0]
        if move_lst[pg.K_UP]: total_move[1] -= 5
        if move_lst[pg.K_DOWN]: total_move[1] += 5
        if move_lst[pg.K_LEFT]: total_move[0] -= 5
        if move_lst[pg.K_RIGHT]: total_move[0] += 5"""
        rect_kk_img.move_ip(total_mv)
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, rect_kk_img)
        screen.blit(bb_img,rect_bb_img)
        rect_bb_img.move_ip(vx, vy)
        pg.display.update()
        tmr += 1

        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()