import PIL
import pygame
import time

from Board import Board
from pygametestMethods import Tick, initPYGM

refrence = Board.getRefrence()
board = Board(refrence)
screen = initPYGM()

running = True

while running:
  time.sleep(1)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  Tick(screen,board)
