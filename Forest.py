from Square import Square
import tkinter as tk
import utils

class Forest:

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self, gridSize, canvas):
    # Forest
    if(gridSize < 2):
      raise ValueError("Minimum forest size is 2")

    self.__size = gridSize
    # Grid defined like that: __grid[line][column]
    # So line and column from 0 to (__size - 1)
    self.__grid = [ [ Square() for i in range(self.__size) ] for j in range(self.__size) ]

    self.__playerPosition = (0, 0)

    # GUI
    self.__pieces = []
    self.__canvas = canvas
    self.__canvas.bind("<Configure>", self.__refresh)


  # ================================================================================================
  # STATIC METHODS
  # ================================================================================================
  @staticmethod
  def generateRandom(gridSize, canvas):
    forest = Forest(gridSize, canvas)

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
  def __placePiece(self, value, line, column, tag = None):
    if(value == Square.EMPTY):
      return

    image = Square.getPhotoImage(value, self.__squarePixelSize - 2)
    x = (column * self.__squarePixelSize) + int(self.__squarePixelSize / 2)
    y = (line * self.__squarePixelSize) + int(self.__squarePixelSize / 2)

    if(tag == None):
      tags = ("piece")
    else:
      tags = ("piece", tag)

    self.__canvas.create_image(x, y, image=image, tags=tags, anchor="c")
    self.__pieces.append(image)

  def __refreshPieces(self):
    self.__pieces = []
    self.__canvas.delete("piece")

    # Player
    (line, column) = self.__playerPosition
    self.__placePiece(Square.PLAYER, line, column, "player")

    # Pieces
    for line in range(self.__size):
      for column in range(self.__size):
        value = self.getSquareValue(line, column)
        self.__placePiece(value, line, column)

    self.__canvas.tag_raise("piece")
    self.__canvas.tag_raise("player")
    self.__canvas.tag_lower("square")

  def __refresh(self, event = None):
    if(event == None):
      width = self.__canvas.winfo_width()
      height = self.__canvas.winfo_height()
    else:
      width = event.width
      height = event.height

    x = int((width - 1) / self.__size)
    y = int((height - 1) / self.__size)

    self.__squarePixelSize = min(x, y)
    self.__canvas.delete("square")

    for line in range(self.__size):
      for column in range(self.__size):
        x1 = (column * self.__squarePixelSize)
        y1 = (line * self.__squarePixelSize)
        x2 = x1 + self.__squarePixelSize
        y2 = y1 + self.__squarePixelSize
        self.__canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white", tags="square")

    self.__refreshPieces()

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

  # Return False if can't move in this direction, the new position value otherwise
  def __playerMove(self, lineDif, columnDif):
    (line, column) = self.__playerPosition
    newLine = line + lineDif
    newColumn = column + columnDif
    if(not self.__checkPosition(newLine, newColumn)):
      return False

    self.__playerPosition = (newLine, newColumn)
    x = (newColumn * self.__squarePixelSize) + int(self.__squarePixelSize / 2)
    y = (newLine * self.__squarePixelSize) + int(self.__squarePixelSize / 2)
    self.__canvas.coords("player", x, y)

    return(self.getSquareValue(newLine, newColumn))

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

  def getPlayerPosition(self):
    return self.__playerPosition

  def getPlayerPositionValue(self):
    (line, column) = self.getPlayerPosition()
    return self.getSquareValue(line, column)

  # See __playerMove doc
  def playerMoveUp(self):
    return self.__playerMove(-1, 0)

  # See __playerMove doc
  def playerMoveDown(self):
    return self.__playerMove(1, 0)

  # See __playerMove doc
  def playerMoveLeft(self):
    return self.__playerMove(0, -1)

  # See __playerMove doc
  def playerMoveRight(self):
    return self.__playerMove(0, 1)

  # See __playerMove doc
  def display(self):
    self.__refresh()

  def displayConsole(self):
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
