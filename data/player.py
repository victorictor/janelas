import pygame as pg

class PLAYER:
    def __init__(self):
        self.surf = pg.image.load('data/palito.png')
        self.pos = [200,200]
        self.vel = 5

    def move(self, k):
            if k[pg.K_w]:
                self.pos[1] -= self.vel
            if k[pg.K_s]:
                 self.pos[1] += self.vel

            if k[pg.K_a]:
                self.pos[0] -= self.vel
            if k[pg.K_d]:
                 self.pos[0] += self.vel 

    def update(self, tela,x,y):
        tela.blit(self.surf, (self.pos[0]-x, self.pos[1]-y))