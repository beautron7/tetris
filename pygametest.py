import pygame
import PIL
from Board import Board
white = (255,255,255)

refrence = Board.getRefrence()
board = Board(refrence)

#init window
(width, height) = (1000, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption('Monitor Window')


running = True
while running:
  updateModel = False
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      keys = pygame.key.get_pressed()
      if keys[pygame.K_x]:
        updateModel=True
  screen.fill(white)

  latest_img = board.screenGrab()
  latest_img_str = latest_img.tobytes("raw","RGB")
  pygm_preview = pygame.image.fromstring(latest_img_str,(10,20),"RGB")
  pygm_preview = pygame.transform.scale(pygm_preview,(250,500))
  screen.blit(pygm_preview,(0,0))
  
  if updateModel:
    board.captureGameData(latest_img)
  
  pygm_model = pygame.image.fromstring(board.renderdata().tobytes("raw","RGB"),(10,20),"RGB")
  pygm_model = pygame.transform.scale(pygm_model,(250,500))

  screen.blit(pygm_model,(300,0))

  pygame.display.update();

