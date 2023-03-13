import pygame
import random
class Snake:
    def __init__(self,dis):
        self.snake_head_pos = [100,100,10,10]
        self.snake_color = (0,255,0)
        self.display = dis
        self.snake_body = [[100,90,10,10], [100,80,10,10], [100,70,10,10]]
        self.direction = [0,10]


    def update_snek(self):
        pygame.draw.rect(self.display, self.snake_color, self.snake_head_pos)
        for i in self.snake_body:
            pygame.draw.rect(self.display,self.snake_color,i)

    def move_body_in_direction(self):
        old_head_pos = self.snake_head_pos.copy()
        self.snake_head_pos[0] += self.direction[0]
        self.snake_head_pos[1] += self.direction[1]
        self.push_body(old_head_pos)
    def push_body(self,old_head):
        self.snake_body[2] = self.snake_body[1]
        self.snake_body[1] = self.snake_body[0]
        self.snake_body[0] = old_head
    def move_down(self):

        self.direction = [0,10]
        old_head_pos = self.snake_head_pos.copy()
        self.snake_head_pos[0] += 0
        self.snake_head_pos[1] += 10
        #self.push_body(old_head_pos)

    def move_right(self):
        self.direction = [10,0]
        old_head_pos = self.snake_head_pos.copy()
        self.snake_head_pos[0] += 10
        self.snake_head_pos[1] += 0
        #self.push_body(old_head_pos)
    def move_left(self):
        self.direction = [-10,0]
        old_head_pos = self.snake_head_pos.copy()
        self.snake_head_pos[0] -= 10
        self.snake_head_pos[1] += 0
        #self.push_body(old_head_pos)
    def move_up(self):
        self.direction = [0,-10]
        old_head_pos = self.snake_head_pos.copy()
        self.snake_head_pos[0] += 0
        self.snake_head_pos[1] -= 10
        #self.push_body(old_head_pos)

    def consume(self):
        # by consuming an apple the body of the snake will be extanded by 1 rectangle
        # the tail will be extended by adding the last element of body before it is updated.
        last_tail = self.snake_body[-1].copy()
        old_head_pos = self.snake_head_pos.copy()


        self.snake_body.append(last_tail)
        pass


class Apple:
    def __init__(self,dis):
        self.apple_pos = [50,50,10,10]
        self.apple_color = (255,0,0)
        self.display = dis
        pygame.draw.rect(self.display, self.apple_color, self.apple_pos)

    def updt_apple(self):
        pygame.draw.rect(self.display, self.apple_color, self.apple_pos)
    def apple_eaten(self):
        self.apple_pos = [random.randint(0,36)*10,random.randint(0,24)*10,10,10]