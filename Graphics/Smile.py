import random
import time
from graphics import *

data = [52, 47, 57, 49, 59, 62, 44, 76, 52, 52, 44, 59, 59, 79, 59, 42, 57, 48, 80, 43, 72, 74, 59, 44, 57, 55, 49, 54, 54]

random = random.choice(data)

window = GraphWin("Visualisation", 500, 500)


#Text and Box
box = Rectangle(Point(200,10),Point(300,40))
box.setOutline(color_rgb(255,0,0))
box.setFill(color_rgb(255,255,0))
box.draw(window)

line = Line(Point(200,32),Point(300,32))
line.setWidth(2)
line.draw(window)

text = Text(Point(250,20),random)
text.draw(window)


#Face
face = Circle(Point(250,250), 100)
face.setFill(color_rgb(255,255,0))
face.setWidth(2)
face.draw(window)


#Eyes
eye = Circle(Point(220,220), 20)
eye.setFill(color_rgb(255,255,0))
eye.setWidth(2)
eye.draw(window)

eye2 = Circle(Point(280,220), 20)
eye2.setFill(color_rgb(255,255,0))
eye2.setWidth(2)
eye2.draw(window)
eyeBall = Circle(Point(220,220), 2)

eyeBall.setWidth(4)
eyeBall.draw(window)

eyeBall2 = Circle(Point(280,220), 2)
eyeBall2.setWidth(4)
eyeBall2.draw(window)


#Brow
brow = Line(Point(200,195),Point(240,195))
brow.setWidth(4)
brow.draw(window)

brow2 = Line(Point(260,195),Point(300,195))
brow2.setWidth(4)
brow2.draw(window)


#Mouth
mouth = Line(Point(220,290),Point(280,290))
mouth.setWidth(4)
mouth.draw(window)


#End
window.getMouse()