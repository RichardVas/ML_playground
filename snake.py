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


class Apple:
    def __init__(self,dis):
        self.apple_pos = [50,50,10,10]
        self.apple_color = (255,0,0)
        self.display = dis
        pygame.draw.rect(self.display, self.apple_color, self.apple_pos)