import cv2 as cv
import numpy as np
import pyautogui as pg
import win32gui
import win32ui
import win32con
import time


class WindowCapture:
    def __init__(self, w, h, windowname):
        # public
        self.w = w
        self.h = h
        self.windowname = windowname

    @staticmethod
    def window_list():
        def winenumhandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))

        win32gui.EnumWindows(winenumhandler, None)

    def window_position(self):
        hwnd = win32gui.FindWindow(None, self.windowname)
        rect = win32gui.GetWindowRect(hwnd)
        return rect

    def screenshot(self):
        hwnd = win32gui.FindWindow(None, self.windowname)

        # récupère la data de l'image
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (0, 0), win32con.SRCCOPY)

        # sauvgarde le screenshot
        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')

        singnedint = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(singnedint, dtype='uint8')
        img.shape = (self.h, self.w, 4)
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        return img
