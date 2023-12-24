from point import Point, Line
from tkinter import Tk, BOTH, Canvas

class Window:
  def __init__(self, width: int, height: int):
    self.__width=width
    self.__height=height
    self.__root = Tk()
    self.__root.title = "Maze Solver"
    self.__canvas = Canvas()
    self.__canvas.pack()
    self.__running = False
    self.__root.protocol("WM_DELETE_WINDOW", self.close)

  def draw_line(self, line: Line, fill_color: str):
    line.draw(self.__canvas, fill_color)
  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()
  
  def wait_for_close(self):
    self.__running = True
    while(self.__running):
      self.redraw()
  
  def close(self):
    self.__running = False
