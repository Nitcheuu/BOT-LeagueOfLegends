import pyautogui as pg
import numpy as np
import cv2 as cv
import time
from windowcapture import WindowCapture
from findclick import Vision
import keyboard as kb


class GameBot:
    def __init__(self):
        self.__is_loading = False
        self.__loaded = False
        self.__ended = False
        self.__game_window = WindowCapture(1980, 1080, "0xde0ac4 League of Legends (TM) Clien")
        self.__can_walk = True

    '''def get_window_posiiton(self):
        window = Vision("lol_window.PNG")'''

    def __reset(self):
        self.__is_loading = False
        self.__loaded = False
        self.__ended = False

    def __send_spells(self, ulti):
        kb.send('a')
        kb.send('z')
        kb.send('e')
        if ulti:
            kb.send('r')

    def __verif(self, list):
        if list:
            return False
        else:
            return True

    def run_down_game(self):
        load = Vision("lol_loading_screen.PNG")
        run_down = Vision("lol_run_down.PNG")
        end = Vision("lol_victory_button.PNG")
        while not self.__is_loading:
            s = self.__game_window.screenshot()
            test = load.find(s, 0.9)
            if test:
                self.__is_loading = True
                print("en chargement")
        while not self.__loaded:
            s = self.__game_window.screenshot()
            point = load.find(s, 0.9)
            if not point:
                self.__loaded = True
                print("en jeu")

        while not self.__ended:
            s = self.__game_window.screenshot()
            end_point = end.find(s, 0.9)
            if end_point:
                pg.click(x=end_point[0][0], y=end_point[0][1])
                self.__ended = True
                print("fin de la partie")
            point = run_down.find(s, 0.6)
            if point:
                print(point)
                pg.moveTo(point[0][0], point[0][1])
                pg.mouseDown(button='right')
                pg.mouseUp(button='right')
                pg.moveTo(0, 0)
                print("run down")
            time.sleep(10)

        print("end")
        self.__reset()

    def run_down(self):
        run_down = Vision("lol_run_down.PNG")
        point = run_down.find(self.__game_window.screenshot(), 0.6)
        if point:
            print(point)
            pg.moveTo(point[0][0], point[0][1])
            pg.mouseDown(button='right')
            pg.mouseUp(button='right')
            pg.moveTo(0, 0)
            print("run down")

    def attack_tower_test(self):
        tower_plate = Vision("model/turret/lol_turret.PNG")
        tower_points = tower_plate.find(self.__game_window.screenshot(), 0.6)
        self.__can_walk = self.__verif(tower_points)
        if tower_points:
            pg.moveTo(tower_points[0][0], tower_points[0][1])
            pg.mouseDown(button='right')
            pg.mouseUp(button='right')
            pg.moveTo(0, 0)
            print("j'attaque la tourelle")
            time.sleep(10)
        else:
            print("pas de tours")

    def attack_tower2_test(self):
        tower2 = Vision("model/turret/lol_turret_2.PNG")
        tower_points = tower2.find(self.__game_window.screenshot(), 0.6)
        self.__can_walk = self.__verif(tower_points)
        if tower_points:
            pg.moveTo(tower_points[0][0], tower_points[0][1])
            pg.mouseDown(button='right')
            pg.mouseUp(button='right')
            pg.moveTo(0, 0)
            print("j'attaque la tourelle 2")

    def attack_creep_test(self):
        creep = Vision("model/creep/lol_creep.PNG")
        creep_points = creep.find(self.__game_window.screenshot(), 0.9)
        self.__can_walk = self.__verif(creep_points)
        if creep_points:
            pg.moveTo(creep_points[0][0] + 20, creep_points[0][1] + 20)
            pg.mouseDown(button='right')
            pg.mouseUp(button='right')
            self.__send_spells(ulti=False)
            print("j'attaque un caster")

    def attack_enemy_test(self):
        isEnemy = True
        while isEnemy:
            enemy = Vision("model/enemy/lol_enemy.PNG")
            enemy_points = enemy.find(self.__game_window.screenshot(), 0.75)
            self.__can_walk = self.__verif(enemy_points)
            if enemy_points:
                pg.moveTo(enemy_points[0][0] + 50, enemy_points[0][1] + 50)
                self.__send_spells(ulti=True)
                pg.mouseDown(button='right')
                pg.mouseUp(button='right')
                print("j'attaque un ennemi")
            else:
                isEnemy = False
                print("sortie de la boucle")

    def lvl_up_spell(self):
        lvl_up_button = Vision("model/lvl_up_spell/lol_lvl_up_spell.PNG")
        lvl_points = lvl_up_button.find(self.__game_window.screenshot(), 0.8)
        self.__can_walk = self.__verif(lvl_points)
        if lvl_points:
            pg.moveTo(lvl_points[0][0], lvl_points[0][1])
            pg.mouseDown()
            pg.mouseUp()
            pg.moveTo(0, 0)
            print("j'augmente mon sort")

    def walk_front(self):
        myself = Vision("model/self/self.PNG")
        self_points = myself.find(self.__game_window.screenshot(), 0.8)
        if self_points and self.__can_walk:
            pg.moveTo(self_points[0][0] + 400, self_points[0][1] - 150)
            pg.mouseDown(button='right')
            pg.mouseUp(button='right')
            print("je me déplace")

    def play(self):
        load = Vision("lol_loading_screen.PNG")
        end = Vision("lol_victory_button.PNG")
        while not self.__is_loading:
            s = self.__game_window.screenshot()
            test = load.find(s, 0.9)
            if test:
                self.__is_loading = True
                print("en chargement")
        while not self.__loaded:
            s = self.__game_window.screenshot()
            point = load.find(s, 0.9)
            if not point:
                self.__loaded = True
                print("en jeu")
        while not self.__ended:
            self.lvl_up_spell()
            self.attack_enemy_test()
            self.attack_tower_test()
            self.attack_creep_test()
            self.walk_front()
            is_end = end.find(self.__game_window.screenshot(), 0.9)
            if is_end:
                pg.click(x=is_end[0][0], y=is_end[0][1])
                self.__ended = True
                print("fin de la partie")

        self.__reset()




