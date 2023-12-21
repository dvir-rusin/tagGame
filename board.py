import pygame
#brick = pygame.image.load("D:/‏‏הורדות/black brick.jpg")
brick = pygame.image.load("images and audio/the escapist 2 block.jpg")
brick = pygame.transform.scale(brick, (50, 50))
class Board:
    def __init__(self, width, height, board_map):

        self.width = width
        self.height = height
        self.board_map = board_map

    def draw(self, win):
        for i in range(len(self.board_map)):
            for j in range(len(self.board_map[0])):
                if self.board_map[i][j] == 1:
                    rect = pygame.Rect(j*self.width, i*self.height, self.width, self.height)
                    pygame.draw.rect(win, (0, 0, 0), rect)
                    win.blit(brick,rect)

