import pandas as pd
import pygame
from Bird import *
from Pipes import *
import warnings
warnings.filterwarnings("ignore")

import math
if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()

    boardH = 640
    boardW = 360

    df_trace = pd.DataFrame(columns=['Birdx','Birdy','dis1','dis2', 'space_pressed'])
    dis = pygame.display.set_mode((boardW,boardH))

    floppy = Bird(boardH= boardH, boardW=boardW)
    #pipe = Pipes(boardH,boardW)

    Pipes_container = Pipes(dis=dis,boardH=boardH, boardW=boardW)

    Pipes_container.addPipe()
    pygame.display.update()
    game_over = False
    framecounter = 0
    while not game_over:
        space_pressed = False
        floppy.gravity()
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                game_over = True
                df_trace.to_csv('./output.csv')
            if event.type == pygame.KEYDOWN:
                space_pressed = True
                floppy.jump()

        if(framecounter % 5 == 0):
            Pipes_container.addPipe()



        #empty passed pipes
        first_pipe = Pipes_container.pipe_array[0]
        if(first_pipe.pipex < floppy.x):
            Pipes_container.removeFirstPipe()

        dist_top_pipe = math.dist([floppy.x,floppy.y],[first_pipe.pipex, first_pipe.pipeH])
        dist_bot_pipe = math.dist([floppy.x,floppy.y],[first_pipe.pipex,500])



        print(f'bird pos: {floppy.x,floppy.y} , pipes : {Pipes_container.getPipes()}, distances : {dist_top_pipe}, {dist_bot_pipe}')

        row_to_append = pd.DataFrame([{'Birdx' : floppy.x, 'Birdy' : floppy.y, 'dis1': dist_top_pipe, 'dis2': dist_bot_pipe, 'space_pressed': space_pressed}])

        df_trace = pd.concat([df_trace,row_to_append],ignore_index=True)

        #must run on each frame
        framecounter += 1
        dis.fill((135, 206, 235))

        pygame.draw.line(dis,(255,0,0),(floppy.x, floppy.y),(first_pipe.pipex,first_pipe.pipeH),10)
        pygame.draw.line(dis, (255, 0, 0), (floppy.x, floppy.y), (first_pipe.pipex,500),10)

        floppy.update(dis)
        Pipes_container.drawPipes()
        pygame.display.update()
        Pipes_container.movePipes()
        clock.tick(10)
    pygame.quit()