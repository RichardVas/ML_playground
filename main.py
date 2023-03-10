import pygame
from fps import *
from snake import *



#tutorial
if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()
    fps = FPS()

    dis = pygame.display.set_mode((640,480))
    apple = Apple(dis)
    snek = Snake(dis)

    snek.update_snek()
    pygame.display.update()
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                snek.move_left()
            elif keys[pygame.K_RIGHT]:
                snek.move_right()
            elif keys[pygame.K_UP]:
                snek.move_up()
            elif keys[pygame.K_DOWN]:
                snek.move_down()

        dis.fill((0, 0, 0))
        fps.render(dis)
        snek.update_snek()

        pygame.draw.rect(dis, (255, 0, 0), [200, 100, 10, 10])
        pygame.display.update()

        fps.clock.tick(60)
    pygame.quit()
    quit()


