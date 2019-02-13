
import pyautogui
import PIL
import time
from Board import Board

refrence = Board.getRefrence()
board = Board(refrence)

board.clickStart()
for i in range(60):
    time.sleep(2)
    board.captureGameData()
    board.printBoard()




while True:
  board.captureGameData()
  for i in range(200):
    pass
