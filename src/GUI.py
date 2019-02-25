import pygame
from Board import Board as Board
import time

class GUI():
  class Colors():
    white = (255,255,255)
    black = (0,0,0)
  
  @staticmethod
  def PILtoPYGM(img):
    return pygame.image.fromstring(img.tobytes('raw','RGB'),img.size,'RGB')

  @staticmethod
  def initPYGM():
    (width, height) = (1000, 500)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    pygame.display.set_caption('Monitor Window')
    return screen

  def displayPIL(self,PILimg,pos,size):
    PYGMimg = GUI.PILtoPYGM(PILimg)
    PYGMimg = pygame.transform.scale(PYGMimg,size)
    self.screen.blit(PYGMimg,pos)

  def tick(self):
    updateModel = False
    self.screen.fill(GUI.Colors.white)

    latest_game_img = self.board.screenGrab()
    self.displayPIL(latest_game_img,(0,0),(250,500))
    self.displayPIL(self.board.renderdata(),(300,0),(250,500))
    pygame.display.update();  

  def __init__(self,board):
    self.board = board
    self.screen = GUI.initPYGM()

if __name__ == "__main__":
  running = True
  
  ref = Board.getReference()
  board = Board(ref)
  mygui = GUI(board)
  
  running = True
  while running:
    mygui.tick()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False