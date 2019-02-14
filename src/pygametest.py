import PIL
import pygame
import time

from Board import Board as Board
from pygametestMethods import Tick, initPYGM

refrence = Board.getRefrence()
board = Board(refrence)
screen = initPYGM()

running = True

while running:
  time.sleep(1)
  #TODO: Move this coude to the tick fcn
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    #TODO: Move this code out of tick() and onto a pyautogui.
    elif event.type == pygame.KEYDOWN:
      keys = pygame.key.get_pressed()
      if keys[pygame.K_x]:
        updateModel=True

  
  Tick(screen,board)
