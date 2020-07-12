import pygame as pg
pg.init()

size = width, height = 300, 300
work, domove  = True, False
x,y,x1,y1 = 0,0,0,0
BLACK = pg.Color(0, 0, 0)

screen = pg.display.set_mode(size)
screen.fill(BLACK)
pg.draw.rect(screen, pg.color.Color('red'), (0,0,70,70))
pg.display.flip()

while work:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            work = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            work = False
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y = event.pos
            r1,r2 = x - x1,y - y1
            if abs(r1)> 70 or abs(r2)> 70:
                status = False
            status = True
            if status:
                domove = True
        if event.type == pg.MOUSEMOTION and domove:
            x, y = event.pos
            x1,y1 = x,y
            screen.fill(BLACK)
            pg.draw.rect(screen, pg.color.Color('red'), (x,y,70,70))
        if event.type == pg.MOUSEBUTTONUP: 
            domove = False
    pg.display.flip()

pg.quit()