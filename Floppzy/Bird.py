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


class Pipes:
    def __init__(self, boardH, boardW):
        self.pipeW = 64
        self.pipeH = 512
        self.pipex = boardW-64
        self.pipey = 0
        self.pipe_array = []
        self.boardH = boardH
    def drawPipe(self,dis):
        pygame.draw.rect(dis,(0,255,0),[self.pipex,0,self.pipeW,self.pipeH])
        pygame.draw.rect(dis, (0, 255, 0), [self.pipex, 600, self.pipeW, self.pipeH])

    def addPipes(self):
        for i in range(3):
            self.pipe_array.append(Pipes(self.pipex,self.pipey))

    def move_pipes(self):
        self.pipex += -64