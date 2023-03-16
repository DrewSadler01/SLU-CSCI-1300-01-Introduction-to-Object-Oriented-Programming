from cs1graphics import *
paper = Canvas(500 , 100)
paper.setBackgroundColor('gray')
numRows = 5
numColumns = 10
triangle = Polygon(Point(25,0) , Point(50,20) , Point(0,20))
triangle.setFillColor('blue')
paper.add(triangle)
for x in range(numColumns):
    new = triangle.clone()
    new.move(50*x,0)
    paper.add(new)
    for y in range(numRows):
        new2 = new.clone()
        new2.move(0,20*y)
        paper.add(new2)
