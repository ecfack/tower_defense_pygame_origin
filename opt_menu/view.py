import pygame
import math
from settings import WIN_WIDTH, WIN_HEIGHT, HP_IMAGE, HP_GRAY_IMAGE,singleton_vol_controller
from color_settings import *

class OptMenuView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.SysFont("comicsans", 30)

    def draw_bg(self):
        self.win.fill(BROWN)
    
    def draw_btn(self,buttonList):
        for btn in buttonList:
            self.win.blit(btn.image, btn.rect)

    def draw_sound_volume(self):
        volume = math.ceil(singleton_vol_controller.sound_volume*100)
        volume = math.ceil(volume/5)*5
        text = self.font.render(f"Sound volume: {volume}%", True, (255, 255, 255))
        self.win.blit(text, (455,320))

    def draw_music_volume(self):
        volume = math.ceil(singleton_vol_controller.music_volume*100)
        volume = math.ceil(volume/5)*5
        text = self.font.render(f"Music volume: {volume}%", True, (255, 255, 255))
        self.win.blit(text, (455,395))

    def draw_map_preview(self, map_img):
        self.win.blit(map_img, (262,5))