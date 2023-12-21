import pygame
class Sounds:
    def __init__(self):
        # Initialize Pygame mixer
        pygame.mixer.init()
        # Load background sound file
        self.background_sound = pygame.mixer.Sound("images and audio/house_lo.wav")

        self.point_sound = pygame.mixer.Sound("images and audio/audio_point.wav")

        # Create a boolean variable to store whether the music is muted or not
        self.music_muted = False
    def play_sound(self):
        # Play background sound on repeat
        self.background_sound.play(-1)

    def play_sound_point(self):
        self.point_sound.play()



    # Create a function to toggle the music mute status
    def toggle_music_mute(self):
        if self.music_muted:
            pygame.mixer.unpause()
            self.music_muted = False
        else:
            pygame.mixer.pause()
            self.music_muted = True
