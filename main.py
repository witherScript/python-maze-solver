from window import Window
from point import Point, Line
def main():
    win = Window(800, 800)
    
    pointA = Point(40, 12)
    pointB = Point(150, 190)
    line = Line(pointA, pointB)
    color = "red"
    win.draw_line(line, color)
    win.wait_for_close()

if __name__ == "__main__":
    main()
