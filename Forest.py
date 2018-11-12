from Square import Square
import utils

class Forest:

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
