import pygame
from fps import *
from snake import *



#tutorial
if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()
    fps = FPS()

    dis = pygame.display.set_mode((360,240))
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
        if(snek.snake_head_pos == apple.apple_pos):
            print('ham')
            apple.apple_eaten()
        snek.update_snek()
        apple.updt_apple()

        pygame.display.update()
        snek.move_body_in_direction()

        fps.render(dis)



        fps.clock.tick(10)
    pygame.quit()
    quit()


