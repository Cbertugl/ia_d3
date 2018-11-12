from Square import Square

class Forest:
  def __init__(self, gridSize):
    self.__size = gridSize
    self.__grid = [ [ Square() for i in range(self.__size) ] for j in range(self.__size) ]
  
  @staticmethod
  def generateRandom(gridSize = 3):
    return Forest(gridSize)
  
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
