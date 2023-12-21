import pygame
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (255, 0, 0)  # Initial color

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        small_font = pygame.font.Font('freesansbold.ttf', 20)
        text_surface = small_font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        win.blit(text_surface, text_rect)

    def set_pressed(self):
        self.color = (0, 255, 0)  # Set the color to green