class Square:
  EMPTY = " "
  PLAYER = "X"
  EXIT = "E"
  WIND = "W"
  CREVASSE = "C"
  MONSTER_POOP = "P"
  MONSTER = "M"

  def __init__(self, initialValue = EMPTY):
    self.__value = initialValue

  def getValue(self):
    return self.__value

  def setValue(self, value):
    self.__value = value