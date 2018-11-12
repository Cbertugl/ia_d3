from Square import Square
import tkinter as tk
import utils

class Forest(tk.Frame):

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self, gridSize):
    if(gridSize < 2):
      raise ValueError("Minimum forest size is 2")

    self.__size = gridSize
    # Grid defined like that: __grid[line][column]
    # So line and column from 0 to (__size - 1)
    self.__grid = [ [ Square() for i in range(self.__size) ] for j in range(self.__size) ]

    # GUI
    self.__root = tk.Tk()
    self.__root.configure(background="chartreuse4")
    tk.Frame.__init__(self, self.__root)

    windowWidth = self.__root.winfo_screenwidth() - 100
    windowHeight = self.__root.winfo_screenheight() - 100
    self.__squareSize = 0

    self.winfo_toplevel().title("La forêt magique")
    self.__canvas = tk.Canvas(
      self,
      highlightthickness=0,
      width=windowWidth,
      height=windowHeight,
      background="chartreuse4"
    )
    self.__canvas.pack()
    self.__canvas.bind("<Configure>", self.__refresh)
    self.pack(padx=20, pady=20)

  # ================================================================================================
  # STATIC METHODS
  # ================================================================================================
  @staticmethod
  def generateRandom(gridSize = 3):
    forest = Forest(gridSize)

    # Placing player
    forest.setSquareValue(0, 0, Square.PLAYER)

    # Placing exit
    (randomLine, randomColumn) = utils.getRandomPosition(gridSize)
    while(randomLine == 0 and randomColumn == 0):
      (randomLine, randomColumn) = utils.getRandomPosition(gridSize)

    forest.setSquareValue(randomLine, randomColumn, Square.EXIT)

    # Placing random monsters and crevasses
    for line in range(gridSize):
      for column in range(gridSize):
        # Avoid generating a monster or a crevasse near the player
        if(
          (line == 0 and column == 0) or
          (line == 1 and column == 0) or
          (line == 0 and column == 1)
        ):
          continue

        if(not forest.hasSquareValue(line, column)):
          # With this probabilities, there is at least 1 monster and 1 crevasse
          # every 10 square
          monsterChance = (1 / 10) * 100
          crevasseChance = (1 / 10) * 100

          # Monster generation with enough chance
          if(utils.rollDice(monsterChance)):
            forest.__placeDeadlyElement(line, column, Square.MONSTER, Square.MONSTER_POOP)
          # If a monster has not been generated, maybe a crevasse will be
          elif(utils.rollDice(crevasseChance)):
            forest.__placeDeadlyElement(line, column, Square.CREVASSE, Square.WIND)

    return forest


  # ================================================================================================
  # PRIVATE METHODS
  # ================================================================================================
  def __refresh(self, event):
    x = int((event.width - 1) / self.__size)
    y = int((event.height - 1) / self.__size)
    self.__squareSize = min(x, y)
    self.__canvas.delete("square")

    for line in range(self.__size):
      for col in range(self.__size):
        x1 = (col * self.__squareSize)
        y1 = (line * self.__squareSize)
        x2 = x1 + self.__squareSize
        y2 = y1 + self.__squareSize
        self.__canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white", tags="square")

  def __checkPosition(self, line, column):
    if(
      line < 0 or
      column < 0 or
      line >= self.__size or
      column >= self.__size
    ):
      return False

    return True

  def __placeDeadlyElement(self, line, column, deadlyElement, clueElement):
    self.setSquareValue(line, column, deadlyElement)
    
    tmp = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    for pair in tmp:
      (i, j) = pair
      newLine = line + i
      newColumn = column + j

      # If it's not a monster, a crevasse or the exit
      if(
        (not self.getSquareValue(newLine, newColumn) == Square.MONSTER) and
        (not self.getSquareValue(newLine, newColumn) == Square.CREVASSE) and
        (not self.getSquareValue(newLine, newColumn) == Square.EXIT)
      ):
        self.setSquareValue(newLine, newColumn, clueElement)


  # ================================================================================================
  # PUBLIC METHODS
  # ================================================================================================
  def hasSquareValue(self, line, column):
    if(not self.__checkPosition(line, column)):
      return None
    
    return self.__grid[line][column].hasValue()

  def getSquareValue(self, line, column):
    if(not self.__checkPosition(line, column)):
      return None
    
    return self.__grid[line][column].getValue()

  def setSquareValue(self, line, column, value):
    if(not self.__checkPosition(line, column)):
      return
    
    self.__grid[line][column].setValue(value)
  
  def display(self):
    for i in range(2 * self.__size + 3):
      print("=", end = "")

    print()

    for i in range(self.__size):
      print("‖ ", end = "")
      
      for j in range(self.__size):
        print(self.__grid[i][j].getValue(), "", end = "")
      
      print("‖")

    for i in range(2 * self.__size + 3):
      print("=", end = "")

    print()

  def start(self):
    self.__root.mainloop()
