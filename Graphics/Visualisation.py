from graphics import *

data = [52, 47, 57, 49, 59, 62, 44, 76, 52, 52, 44, 59, 59, 79, 59, 42, 57, 48, 80, 43, 72, 74, 59, 44, 57, 55, 49, 54, 54]

window = GraphWin("Visualisation", 500, 500)

#Text and Box
box = Rectangle(Point(200,10),Point(300,40))
box.setOutline(color_rgb(255,0,0))
box.setFill(color_rgb(255,255,0))
box.draw(window)

line = Line(Point(200,32),Point(300,32))
line.setWidth(2)
line.draw(window)

text = Text(Point(250,20),"Stay Happy!")
text.draw(window)


#End
window.getMouse()