import pygame
class Pipe:
    def __init__(self, boardH, boardW):
        self.pipeW = 64
        self.pipeH = 360
        self.pipex = boardW-64
        self.pipey = 0



        self.boardH = boardH
    def drawPipe(self,dis):
        pygame.draw.rect(dis,(0,255,0),[self.pipex,0,self.pipeW,self.pipeH])
        pygame.draw.rect(dis, (0, 255, 0), [self.pipex, 500, self.pipeW, self.pipeH])

    def move_pipe(self):
        self.pipex += -48

class Pipes:

    def __init__(self,dis, boardH, boardW):
        self.display = dis
        self.pipe_array = []
        self.b_height = boardH
        self.b_width = boardW
    def drawPipes(self):
        for i in self.pipe_array:
           i.drawPipe(self.display)

    def movePipes(self):
        for i in self.pipe_array:
            i.move_pipe()

    def addPipe(self):
        new_pipe = Pipe(self.b_height, self.b_width)
        self.pipe_array.append(new_pipe)
