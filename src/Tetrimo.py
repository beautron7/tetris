from enum import Enum

class Tetrimo():
  def __init__(self,squares,rotStyle):
    self.squares=[]
    self.squares.push(squares)
    self.rotStyle=rotStyle

  def getRotated():
    pass

class RotStyle(Enum):
  STANDARD = 1
  TRC = 2

class Tetrimoes():
  T = Tetrimo((
    (0,0),
    (1,0),
    (-1,0),
    (0,-1)
  ),RotStyle.STANDARD)
  L = Tetrimo((
    (0,0),
    (1,0),
    (-1,0),
    (1,-1)
  ),RotStyle.STANDARD)
  R = Tetrimo((
    (0,0),
    (1,0),
    (-1,0),
    (-1,-1)
  ),RotStyle.STANDARD)
  _2 = Tetrimo((
    (0,0),
    (1,0),
    (-1,-1),
    (0,-1)
  ),RotStyle.STANDARD)
  _5 = Tetrimo((
    (0,0),
    (-1,0),
    (1,-1),
    (0,-1)
  ),RotStyle.STANDARD)
  Sq = Tetrimo((
    (0,0),
    (0,-1)
    (1,0),
    (1,-1),
  ),RotStyle.TRC)
  I = Tetrimo((
    (-1,0),
    (0,0),
    (1,0)
    (2,0),
  ),RotStyle.TRC)
