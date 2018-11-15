from Agent import Agent
from Forest import Forest
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

    windowSize = min(
      self.__root.winfo_screenwidth(),
      self.__root.winfo_screenheight()
    )

    self.__squarePixelSize = 0
    self.__canvas = tk.Canvas(
      self.__root,
      highlightthickness=0,
      width=windowSize,
      height=windowSize,
      background=utils.BACKGROUND_COLOR
    )
    self.__canvas.pack(padx=20, pady=20)

    # Agent
    self.__agent = Agent()

    # Forest
    self.__forestSize = 2
    self.__levelUp()

    # Mesure de performance
    self.__performanceMeasure = 0


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

    self.__agent.setEnvironment(self.__forest)

  def __click(self):
    self.__agent.nextAction()
    self.__performanceMeasure -= 1
    

    (line, column) = self.__forest.getPlayerPosition()
    if (self.__forest.getSquareValue(line, column) == Square.CREVASSE or self.__forest.getSquareValue(line, column) == Square.MONSTER ):
      print("t'es mort");
      self.__forest.playerReset()
      self.__performanceMeasure -= 10*(self.__forest.getSize()**2)
    if (self.__forest.getSquareValue(line, column) == Square.MONSTER_POOP or self.__forest.getSquareValue(line, column) == Square.WIND):
      print("Attention")
    if(self.__forest.getSquareValue(line, column) == Square.EXIT):
      self.__performanceMeasure += 10*(self.__forest.getSize()**2)
      print("Level up!")
      print("")
      self.__levelUp()

    print("Mesure de perf : " + str(self.__performanceMeasure))  

  # ================================================================================================
  # PUBLIC FUNCTIONS
  # ================================================================================================
  def start(self):
    self.__root.mainloop()
