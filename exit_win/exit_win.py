import pygame
import os
from settings import WIN_WIDTH,WIN_HEIGHT,FPS,game_status

class ExitWin:
    def __init__(self,win):
        self.bg_win = win
        
        self.menu_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "exit_menu.png")), (350,250))

        self.yes_btn = pygame.Rect(430, 350, 100, 50)
        self.no_btn = pygame.Rect(580, 350, 100, 50)

        self.buttons = [self.yes_btn,
                        self.no_btn]
    def draw(self):
        self.bg_win.blit(self.menu_img, (380,210))

        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        transparency = 50
        for btn in self.buttons:
            pygame.draw.rect(surface,(255,255,255,transparency),btn)
        
        self.bg_win.blit(surface,(0,0))
        
    def run(self):
        is_menu_exit=False
        clock = pygame.time.Clock()
        self.draw()
        while not is_menu_exit:
            clock.tick(FPS)
            x, y = pygame.mouse.get_pos()

            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    game_status["run"] = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.yes_btn.collidepoint(x, y):
                        game_status["run"]=False
                        is_menu_exit=True
                    if self.no_btn.collidepoint(x, y):
                        game_status["run"]=True
                        is_menu_exit=True
            pygame.display.update()
