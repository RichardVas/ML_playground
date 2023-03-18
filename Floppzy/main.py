import pygame
from Bird import *


if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()


    boardH = 640
    boardW = 360


    dis = pygame.display.set_mode((boardW,boardH))

    floppy = Bird(boardH= boardH, boardW=boardW)
    pipe = Pipes(boardH,boardW)
    pipe.addPipes()
    pygame.display.update()
    game_over = False
    while not game_over:

        floppy.gravity()
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                floppy.jump()


        dis.fill((135, 206, 235))
        floppy.update(dis)
        pipe.drawPipe(dis)
        pygame.display.update()
        pipe.move_pipes()
        clock.tick(10)
    pygame.quit()