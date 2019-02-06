
import pyautogui
import PIL
import time
from Board import Board

refrence = pyautogui.locateOnScreen('img/attle2.png')
board = Board(refrence)

board.clickStart()
for i in range(100):
    time.sleep(1)
    board.captureGameData()
    board.printBoard()




