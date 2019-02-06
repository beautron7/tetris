import pyautogui
import PIL

Tiles = {
  'GRAY':-1,
  'EMPTY':0,
  'i':1,
  '2':2,
  'r':3,
  'l':4,
  '5':5,
  'b':6,
  't':7
}

TileHues = {
  4:23,
  6:41,
  5:90,
  1:198,
  3:228,
  7:316,
  2:348,
}

class Board():
  def encodeColor(self,color):
    if color[2] < 30:
      return 0
    if color[2] < 75:
      return -1
    return 1

  def captureGameData(self):
    img = pyautogui.screenshot(region=(
      self.refrence.left,
      self.refrence.top,
      self.refrence.width,
      self.refrence.width*2
    ))
    img.convert('HSV')
    img.thumbnail((10,20),PIL.Image.NEAREST)
    self.data = map(self.encodeColor,img)


  def constructor(self,refrence):
    self.refrence=refrence
    self.captureGameData()
    
  def printBoard(self):
    charset = ["."," ","@"]
    for i in range(200):
      print(charset[self.data[i]+1])
      if i%10 is 0:
        print('\n')

  def ClickStart(self):
    button = pyautogui.locateOnScreen('img/start.png')
    pyautogui.moveTo(button.left,button.top)
    pyautogui.click()