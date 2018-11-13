from Forest import Forest
import random
from Square import Square
import tkinter as tk
import utils

class MagicForest(tk.Frame):

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self):
    # GUI
    self.__root = tk.Tk()
    self.__root.title("La forêt magique")
    self.__root.configure(background=utils.BACKGROUND_COLOR)
    tk.Frame.__init__(self, self.__root)

    self.__button = tk.Button(
      self.__root,
      text="Bouger",
      command=self.__click
    )
    self.__button.pack(padx=10, pady=10)

    windowWidth = self.__root.winfo_screenwidth()
    windowHeight = self.__root.winfo_screenheight()

    self.__squarePixelSize = 0
    self.__canvas = tk.Canvas(
      self.__root,
      highlightthickness=0,
      width=windowWidth,
      height=windowHeight,
      background=utils.BACKGROUND_COLOR
    )
    self.__canvas.pack(padx=20, pady=20)

    # Forest
    self.__forestSize = 2
    self.__levelUp()


  # ================================================================================================
  # PRIVATE FUNCTIONS
  # ================================================================================================
  def __levelUp(self):
    self.__forestSize += 1
    print("================================")
    print("Entering magic forest of size", self.__forestSize)
    print("================================")
    self.__canvas.delete("all")
    self.__forest = Forest.generateRandom(self.__forestSize, self.__canvas)
    self.__forest.display()

  def __click(self):
    r = random.randint(0, 3)

    if(r == 0):
      v = self.__forest.playerMoveDown()
    elif(r == 1):
      v = self.__forest.playerMoveUp()
    elif(r == 2):
      v = self.__forest.playerMoveLeft()
    elif(r == 3):
      v = self.__forest.playerMoveRight()

    if(v == Square.EXIT):
      print("Level up!")
      print("")
      self.__levelUp()

  # ================================================================================================
  # PUBLIC FUNCTIONS
  # ================================================================================================
  def start(self):
    self.__root.mainloop()
