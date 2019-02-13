import PIL
import pygame

def PILtoPYGM(img):
  return pygame.image.fromstring(img.tobytes('raw','RGB'),img.size,'RGB')