import pygame
class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, (100,100,100))

    def render(self, display):
        self.text = self.font.render(str(round(self.clock.get_fps(), 2)), True, (100,100,100))
        display.blit(self.text, (0, 0))