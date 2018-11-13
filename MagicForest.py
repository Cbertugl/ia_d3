from Forest import Forest
import tkinter as tk
import utils

class MagicForest(tk.Frame):

  # ================================================================================================
  # CONSTRUCTOR
  # ================================================================================================
  def __init__(self):
    # GUI
    self.__root = tk.Tk()
    self.__root.configure(background=utils.BACKGROUND_COLOR)
    tk.Frame.__init__(self, self.__root)

    self.winfo_toplevel().title("La forêt magique")

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
    self.__forestSize = 3
    self.__click(True)


  # ================================================================================================
  # PRIVATE FUNCTIONS
  # ================================================================================================
  def __click(self, firstUse = False):
    if(not firstUse):
      self.__forestSize += 1

    self.__canvas.delete("all")
    self.__forest = Forest.generateRandom(self.__forestSize, self.__canvas)
    self.__forest.display()
    self.pack()


  # ================================================================================================
  # PUBLIC FUNCTIONS
  # ================================================================================================
  def start(self):
    self.__root.mainloop()
