import pygame
import PIL
from Board import Board as Board
from TickCode import Tick 


refrence = Board.getRefrence()
board = Board(refrence)

#init window
(width, height) = (1000, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption('Monitor Window')


running = True

while running:
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
  

