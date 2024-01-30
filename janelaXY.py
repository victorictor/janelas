import pygame as pg
from sys import exit 
import pygetwindow as gw
from data.player import PLAYER

pl = PLAYER()
pg.init()
pg.display.set_caption('Meu jogo foda')

lar, alt = 320, 320
x, y = 100,100
tela = pg.display.set_mode((lar, alt))
janela = gw.getWindowsWithTitle('Meu jogo foda')[0]

clock = pg.time.Clock()
img = pg.image.load('data/palito.png')
pg.transform.scale_by(img, 50)
janela.moveTo(x, y)

tamanho_mudou = False
while True:
    mx, my = pg.mouse.get_pos()
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            exit()

    print(mx, x, y)
    
    k_press = pg.key.get_pressed()
    if k_press[pg.K_SPACE]:
        if mx <= x - 20:
            x -= 2
            janela.moveTo(x, y)
        if mx >= x + 20:
            x += 2
            janela.moveTo(x, y)

        if my <= y - 20:
            y -= 2
            janela.moveTo(x, y)
        if my >= y + 20:
            y += 2
            janela.moveTo(x, y)

    if tamanho_mudou:
        tela = pg.display.set_mode((lar, alt))
        tamanho_mudou = False

    tela.fill((248, 252, 3))
    tela.blit(img, (10 - x, 10 - y))

    pl.update(tela, x,y)
    pl.move(k_press)
    pg.display.flip()
    clock.tick(60)
    