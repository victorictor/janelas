import pygame 
from sys import exit
import pygetwindow as gw

pygame.init()
l = 320
a = 240
pygame.display.set_caption('Meu jogo foda')
tela = pygame.display.set_mode((l, a))
clock = pygame.time.Clock()
janela = gw.getWindowsWithTitle("Meu jogo foda")[0]

janela.moveTo(100,100)  

img = pygame.image.load('data/palito.png')
while True:
    tela = pygame.display.set_mode((l, a))
    m_x, m_y = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()  

        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_SPACE]:
            l = m_x
            a = m_y
            if m_x >= l or m_y >= a:
                l += m_x
                a += m_y

    '''if l >= 320:
        l -= 15'''
    tela.blit(img, (l/2, a/2))
    pygame.display.flip()
    clock.tick(60)
