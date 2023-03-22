import pygame
from Bird import *
from Pipes import *

if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()


    boardH = 640
    boardW = 360


    dis = pygame.display.set_mode((boardW,boardH))

    floppy = Bird(boardH= boardH, boardW=boardW)
    #pipe = Pipes(boardH,boardW)

    Pipes_container = Pipes(dis=dis,boardH=boardH, boardW=boardW)

    Pipes_container.addPipe()
    pygame.display.update()
    game_over = False
    framecounter = 0
    while not game_over:

        floppy.gravity()
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                floppy.jump()
        if(framecounter % 5 == 0):
            Pipes_container.addPipe()
        framecounter += 1
        print(framecounter)
        dis.fill((135, 206, 235))
        floppy.update(dis)
        Pipes_container.drawPipes()
        pygame.display.update()
        Pipes_container.movePipes()
        clock.tick(10)
    pygame.quit()