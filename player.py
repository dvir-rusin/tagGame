import pygame

class Player():
    def __init__(self, x, y, width, height, color,password):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        if self.color == (255,0,0):#COP
            self.vel = 4
        else:
            self.vel = 3
        self.isReady = False
        self.password = password
        self.connected =False

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
