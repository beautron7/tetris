import pyautogui
import PIL

# Tiles = {
#   'GRAY':-1,
#   'EMPTY':0,
#   'i':1,
#   '2':2,
#   'r':3,
#   'l':4,
#   '5':5,
#   'b':6,
#   't':7
# }



class Board():
  @staticmethod
  def getRefrence():
    return pyautogui.locateOnScreen('img/attle2.png')

  @staticmethod
  def encodeColor(color):
    #408-459 
    val = max(color)
    if val < 50:
      return 0
    if val < 160:
      return -1
    return 1

  def screenGrab(self):
    img = pyautogui.screenshot(region=(
      self.refrence.left,
      self.refrence.top,
      self.refrence.width,
      self.refrence.width*2
    ))
    img.thumbnail((10,20),PIL.Image.NEAREST)
    return img

  def captureGameData(self,img=None):
    if img is None:
      img = self.screenGrab();
    self.data = list(map(Board.encodeColor,img.getdata()))


  def __init__(self,refrence):
    self.refrence=refrence
    self.captureGameData()
    
  # def printBoard(self):
  #   charset = ["!"," ","# "]
  #   buf = "";
  #   for i in range(200):
  #     buf+= charset[self.data[i]+1]
  #     if i%10 is 9:
  #       print(buf+"|")
  #       buf*=0
  #   print("\n\n\n")
    
  def renderdata(self):
    pixels = []
    img = PIL.Image.new('RGB',(10,20),"black");
    pixels = img.load()

    for i in range(200):
      data = self.data[i]
      val = None;
      if data is -1:
        val = (0,0,0)
      elif data is 0:
        val = (128,128,128)
      else:
        val = (255,255,255)
      pixels[i%10,int(i/10)] = val
    return img

  def clickStart(self):
    #TODO: Refactor this method to use self.refrence
    button = pyautogui.locateOnScreen('img/start.png')
    pyautogui.moveTo(button.left,button.top)
    pyautogui.click()

  def getBoardState(self):
    raise "Not Implemented"
    pass
    #return UNKNOWN, OPTIONS, MAP, HELP, TITLE, GAME. 

  # def listPiecesAtLocation(self,l):
  #   (
  #     isValid, x,
  #     a,b, c,d,
  #     e,f, g,h,
  #     i,j, k,l
  #   ) = self.fat_t_test(l)
  #   results = set()

  #   if isValid:
  #     if k is not 0:
  #       if g is not 0:
  #         if c is 0:
  #           results.add(Tiles['r'])
  #       else:
  #         if x is 0:
  #           results.add(Tiles['t'])
  #         if c is 0:
  #           results.add(Tiles['2'])
  #           if l is not 0 and h is 0 and d is 0:
  #             results.add(Tiles['l'])
  #     if j is not 0:
  #       if f is not 0:
  #         if b is 0:
  #           results.add(Tiles['l'])
  #       else:
  #         if x is 0:
  #           results.add(Tiles['t'])
  #         if b is 0:
  #           results.add(Tiles['5'])
  #           if i is not 0 and e is 0 and a is 0: #laying down, aslo this algorithm isnt great...
  #             results.add(Tiles['r'])
  #   return results
    

  # def fat_t_test(self,l):
  #   isValid = self.data[l] is 0 and self.data[l-10] is 0
    
  #   a = self.data[l-22]
  #   b = self.data[l-21]
  #   c = self.data[l-19]
  #   d = self.data[l-18]

  #   e = self.data[l-12]
  #   f = self.data[l-11]
  #   g = self.data[l-9]
  #   h = self.data[l-8]

  #   i = self.data[l-2]
  #   j = self.data[l-1]
  #   k = self.data[l+1]
  #   l = self.data[l+2]

  #   lp = l%10
  #   lr = int(l/10)
  #   if lr < 2:
  #     a=1
  #     b=1
  #     c=1
  #     d=1
  #     if lr < 1:
  #       isValid = False
  #   if lr > 18:
  #     isValid = False


  #   if lp < 2:
  #     a=1
  #     e=1
  #     h=1
  #     if lp < 1:
  #       b=1
  #       f=1
  #       i=1
  #   elif lp > 8:
  #     d = 1
  #     g = 1
  #     k = 1
  #     if lp > 9:
  #       c = 1
  #       f = 1
  #       j = 1
  #   x=self.data[l-20]
  #   return (isValid,x,a,b,c,d,e,f,g,h,i,j,k,l)