from cs1graphics import *
numSquares = 8
unitSize = 30
screen = unitSize * numSquares
paper = Canvas(screen,screen)
X = screen - unitSize/2
Y = unitSize/2
for level in range(numSquares):
    block = Square(unitSize, Point(X,Y))
    block.setFillColor('gray')
    paper.add(block)
    X -= unitSize
    Y += unitSize
