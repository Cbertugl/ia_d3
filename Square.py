from math import ceil
import tkinter as tk

class Square:

  # ================================================================================================
  # CONSTANTS
  # ================================================================================================
  EMPTY = "EMPTY"
  PLAYER = "PLAYER"
  EXIT = "EXIT"
  WIND = "WIND"
  CREVASSE = "CREVASSE"
  MONSTER_POOP = "MONSTER_POOP"
  MONSTER = "MONSTER"


  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self, initialValue = EMPTY):
    self.__value = initialValue


  # ================================================================================================
  # STATIC METHOS
  # ================================================================================================
  @staticmethod
  def getPhotoImage(value, size):
    IMG_SIZE = 200

    if(value == Square.PLAYER):
      filename = "player"
    elif(value == Square.EXIT):
      filename = "portal"
    elif(value == Square.WIND):
      filename = "wind"
    elif(value == Square.CREVASSE):
      filename = "crevasse"
    elif(value == Square.MONSTER_POOP):
      filename = "monster-poop"
    elif(value == Square.MONSTER):
      filename = "monster"

    dezoom = 1
    if(size < IMG_SIZE and size > 0):
      dezoom = ceil(IMG_SIZE / size)

    return tk.PhotoImage(file="img/"+filename+".gif").subsample(dezoom)


  # ================================================================================================
  # PUBLIC METHODS
  # ================================================================================================
  def hasValue(self):
    return self.__value != self.EMPTY

  def getValue(self):
    return self.__value

  def setValue(self, value):
    self.__value = value