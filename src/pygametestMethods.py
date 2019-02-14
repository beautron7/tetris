import pygame
import Colors
from FormatConverter import PILtoPYGM

def displayPIL(screen, PILimg,pos,size):
  PYGMimg = PILtoPYGM(PILimg)
  PYGMimg = pygame.transform.scale(PYGMimg,size)
  screen.blit(PYGMimg,pos)

def Tick(screen,board):
  updateModel = False
  screen.fill(Colors.white)

  latest_game_img = board.screenGrab()
  displayPIL(screen,latest_game_img,(0,0),(250,500))
  displayPIL(screen,board.renderdata(),(300,0),(250,500))
  pygame.display.update();

def initPYGM():
  (width, height) = (1000, 500)
  screen = pygame.display.set_mode((width, height))
  pygame.display.flip()
  pygame.display.set_caption('Monitor Window')
  return screen
