import pygame
class Timer:
    def __init__(self):
        self.counter = 30
        self.text = '30'.rjust(3)

    def star_Timer(self):
        pygame.time.set_timer(pygame.USEREVENT,1000)

    def change_Timer(self, event):
        if event.type == pygame.USEREVENT:
            self.counter -=1
            self.text =str(self.counter).rjust(3)

    def set_Timer(self):
        self.counter = 30
        self.text = '30'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT,1000)

    def time_Up(self):
        return self.counter<=0