import pygame
import Colors
from FormatConverter import PILtoPYGM


def Tick(screen,board):
  updateModel = False
  
  screen.fill(Colors.white)

  latest_game_img = board.screenGrab()
  
  pygm_preview = PILtoPYGM(latest_game_img)
  pygm_preview = pygame.transform.scale(pygm_preview,(250,500))
  screen.blit(pygm_preview,(0,0))
  
  if updateModel:
    board.captureGameData(latest_game_img)
  
  pygm_model = pygame.image.fromstring(board.renderdata().tobytes("raw","RGB"),(10,20),"RGB")
  pygm_model = pygame.transform.scale(pygm_model,(250,500))

  screen.blit(pygm_model,(300,0))

  pygame.display.update();

