import pyautogui as pg
import time
from windowcapture import WindowCapture
from findclick import Vision


class BotClient:

    def __init__(self):
        # Private
        self.__client = WindowCapture(1280, 720, "League of legends")
        self.__window_pos = self.__client.window_position()
        self.__is_game_found = False
        self.__have_champ = False
        self.__skip_honor = False
        self.__champ_points = [(395, 160), (495, 160), (595, 160), (695, 160), (795, 160), (895, 160)]

    def click(self, item_path, threshold):
        screenshot = self.__client.screenshot()
        v = Vision(item_path)
        points = v.find(screenshot, threshold)
        pg.moveTo(points[0][0] + self.__window_pos[0], points[0][1] + self.__window_pos[1])
        pg.click()

    def __reset(self):
        self.__is_game_found = False
        self.__have_champ = False

    def __found_match(self):
        while not self.__is_game_found:
            accept = Vision("lol_accept_button.PNG")
            champselect = Vision("lol_champ_select.PNG")
            isFound = accept.find(self.__client.screenshot(), 0.8)
            if isFound:
                self.click("lol_accept_button.PNG", 0.8)
            isChampSelect = champselect.find(self.__client.screenshot(), 0.8)
            if isChampSelect:
                self.__is_game_found = True
        time.sleep(3)

    def __navigate_client_coopvsia(self):
        time.sleep(10)
        self.click("lol_play_button.PNG", 0.8)
        time.sleep(10)
        self.click("lol_coop_button.PNG", 0.8)
        time.sleep(10)
        self.click("lol_confirm_button.PNG", 0.8)
        time.sleep(20)
        pg.click()
        self.__found_match()

    def __champ_select_coopvsia(self):
        lock = Vision("lol_lock_button.PNG")
        while not self.__have_champ:
            for champ in self.__champ_points:
                if not self.__have_champ:
                    pg.moveTo(champ[0] + self.__window_pos[0], champ[1] + self.__window_pos[1])
                    pg.click()
                    is_lockable = lock.find(self.__client.screenshot(), 0.9)
                    if is_lockable:
                        self.click("lol_lock_button.PNG", 0.9)
                        self.__have_champ = True

        self.__reset()

    def replay_coopvsia(self):
        lvl_button = Vision("lol_lvl_up_ok.PNG")
        honor_button = Vision("lol_skip_honor.PNG")
        time.sleep(15)
        while not self.__skip_honor:
            test = honor_button.find(self.__client.screenshot(), 0.9)
            if test:
                self.click("lol_skip_honor.PNG", 0.9)
                self.__skip_honor = True
        time.sleep(6)
        is_lvl_up = lvl_button.find(self.__client.screenshot(), 0.9)
        if is_lvl_up:
            self.click("lol_lvl_up_ok.PNG", 0.9)
        time.sleep(5)
        is_xp = lvl_button.find(self.__client.screenshot(), 0.9)
        if is_xp:
            self.click("lol_lvl_up_ok.PNG", 0.9)
        time.sleep(5)
        time.sleep(5)
        is_ok = lvl_button.find(self.__client.screenshot(), 0.9)
        if is_ok:
            self.click("lol_lvl_up_ok.PNG", 0.9)
        time.sleep(5)
        self.click("lol_rematch_button.PNG", 0.9)
        time.sleep(5)
        pg.click()
        self.__found_match()
        self.__champ_select_coopvsia()

    def launch_coopvsia(self):
        self.__navigate_client_coopvsia()
        self.__champ_select_coopvsia()
