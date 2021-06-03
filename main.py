import cv2 as cv
import numpy as np
import pyautogui as pg
import win32gui
import win32ui
import win32con
import time
from bot import BotClient
from gamebot import GameBot
from windowcapture import WindowCapture
from findclick import Vision

gamebot = GameBot()
bot = BotClient()

'''
TEST ZONE
'''
azerbot.launch_coopvsia()
gamebot.play()

while True:
    bot.replay_coopvsia()
    gamebot.play()

exit()
'''
END ZONEazer
'''

bot = BotClient()
gamebot = GameBot()

bot.launch_coopvsia()
gamebot.run_down()

while True:
    print("début boucle")
    bot.replay_coopvsia()
    gamebot.run_down()

exit()

while True:

    bot.click("lol_play_button.png", 0.8)
    time.sleep(5)
    print("FPS : " + str(1 / (time.time() - loop_time)))
    loop_time = time.time()
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break


print("Fin")