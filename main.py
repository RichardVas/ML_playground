import pygame

class Snake:
    def __init__(self,dis):
        self.snake_head_pos = [100,100,10,10]
        self.snake_color = (0,255,0)
        self.display = dis
        self.snake_body = [[100,90,10,10], [100,80,10,10], [100,70,10,10]]

    def update_snek(self):
        pygame.draw.rect(self.display, self.snake_color, self.snake_head_pos)
        for i in self.snake_body:
            pygame.draw.rect(self.display,self.snake_color,i)

    def push_body(self,old_head):
        self.snake_body[2] = self.snake_body[1]
        self.snake_body[1] = self.snake_body[0]
        self.snake_body[0] = old_head
    def move_down(self):

        old_head_pos = self.snake_head_pos.copy()
        self.snake_head_pos[0] += 0
        self.snake_head_pos[1] += 10
        self.push_body(old_head_pos)
    def move_right(self):
        old_head_pos = self.snake_head_pos.copy()
        self.snake_head_pos[0] += 10
        self.snake_head_pos[1] += 0
        self.push_body(old_head_pos)
    def move_left(self):
        old_head_pos = self.snake_head_pos.copy()
        self.snake_head_pos[0] -= 10
        self.snake_head_pos[1] += 0
        self.push_body(old_head_pos)
    def move_up(self):
        old_head_pos = self.snake_head_pos.copy()
        self.snake_head_pos[0] += 0
        self.snake_head_pos[1] -= 10
        self.push_body(old_head_pos)

#tutorial
if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()


    dis = pygame.display.set_mode((640,480))
    apple = pygame.draw.rect(dis, (255, 0, 0), [200, 100, 10, 10])
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
        snek.update_snek()

        pygame.draw.rect(dis, (255, 0, 0), [200, 100, 10, 10])
        pygame.display.update()



        clock.tick(30)
    pygame.quit()
    quit()


