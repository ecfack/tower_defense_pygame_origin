import pygame
import os
from tower.towers import Tower, Vacancy
from settings import singleton_vol_controller,singleton_map_controller,game_status

"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""


class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add new enemy"""
        if user_request == "start new wave":
            if model.enemies.is_empty():
                model.enemies.add(10)
                model.wave += 1


class TowerSeller:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """sell tower"""
        if user_request == "sell":
            x, y = model.selected_tower.rect.center
            model.money += model.selected_tower.get_cost()
            model.plots.append(Vacancy(x, y))
            model.towers.remove(model.selected_tower)
            model.selected_tower = None


class TowerDeveloper:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "upgrade" and model.selected_tower.level < 5:
            if model.money >= model.selected_tower.get_cost():
                model.money -= model.selected_tower.get_cost()
                model.selected_tower.level += 1
            # if the money > upgrade cost of the selected tower , level+1
            # use model.selected_tower to access the selected tower data
            # use model.money to access to money data


class TowerFactory:
    def __init__(self, subject):
        subject.register(self)
        self.tower_name = ["moon_tower", "red_fire_tower", "blue_fire_tower", "obelisk_tower"]

    def update(self, user_request: str, model):
        """add new tower"""
        for name in self.tower_name:
            if user_request == name:
                x, y = model.selected_plot.rect.center
                tower_dict = {"moon_tower": Tower.moon_tower(x, y), "red_fire_tower": Tower.red_fire_tower(x, y),
                              "blue_fire_tower": Tower.blue_fire_tower(x, y), "obelisk_tower":Tower.obelisk_tower(x, y)}
                new_tower = tower_dict[user_request]
                if model.money > new_tower.get_cost():
                    model.money -= new_tower.get_cost()
                    model.towers.append(new_tower)
                    model.plots.remove(model.selected_plot)
                    model.selected_plot = None


class Music:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            model.sound.play()


class Muse:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            model.sound.play()

class MinusVolume:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """minusSound"""
        if user_request == "minusSound":
            singleton_vol_controller.minusVol(model.sound,0.05)
            model.sound.play()
        elif user_request == "minusMusic":
            singleton_vol_controller.minusVol(pygame.mixer.music,0.05)
            model.sound.play()

class AddVolume:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """addSound"""
        if user_request == "addSound":
            singleton_vol_controller.addVol(model.sound,0.05)
            model.sound.play()
        elif user_request == "addMusic":
            singleton_vol_controller.addVol(pygame.mixer.music,0.05)
            model.sound.play()

class Back:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """back"""
        if user_request == "back":
            model.back_game=True
            model.sound.play()

class Pause:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """pause"""
        if user_request == "pause":
            model.sound.play()
            model.opt_menu.run()
            model.sound.set_volume(singleton_vol_controller.sound_volume)

class MinusMapIndex:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """minusMapIndex"""
        if user_request == "minusMapIndex":
            singleton_map_controller.map_index-=1
            model.map_preview_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(singleton_map_controller.map_index)+".png")), (500, 300))

class AddMapIndex:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """AddMapIndex"""
        if user_request == "addMapIndex":
            singleton_map_controller.map_index+=1
            model.map_preview_img=pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(singleton_map_controller.map_index)+".png")), (500, 300))

class GoStartMenu:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """Change var game_status["go_start_menu"] in settings.py"""
        if user_request == "goStartMenu":
            game_status["go_start_menu"] = True
