import pygame

class Bird:
    def __init__(self,boardH,boardW):
        self.x = boardW/8
        self.y = boardH/2
        self.width = 34
        self.height = 24
        self.grav_value = 0

    def update(self,dis):
        pygame.draw.rect(dis,(255,255,0),[self.x, self.y,self.width,self.height] )
    def jump(self):
        self.y -= 30
        self.grav_value=0

    def gravity(self):
        self.grav_value -= 2
        self.y -= self.grav_value


