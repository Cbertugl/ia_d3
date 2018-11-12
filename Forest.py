from Square import Square

class Forest:

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self, gridSize):
    self.__size = gridSize
    # Grid defined like that: __grid[line][column]
    # So line and column from 0 to (__size - 1)
    self.__grid = [ [ Square() for i in range(self.__size) ] for j in range(self.__size) ]


  # ================================================================================================
  # STATIC METHODS
  # ================================================================================================
  @staticmethod
  def generateRandom(gridSize = 3):
    return Forest(gridSize)


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


  # ================================================================================================
  # PUBLIC METHODS
  # ================================================================================================
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
