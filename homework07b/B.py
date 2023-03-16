from cs1graphics import *
numLevels = 8                             
unitSize = 30
screen = unitSize * (1 + numLevels)
paper = Canvas(screen, screen)
for level in range(numLevels):
    Y = unitSize * (numLevels - level)
    X = unitSize
    for count in range(level + 1):
        block = Square(unitSize)
        block.move(X + unitSize * count,Y)
        block.setFillColor('gray')
        paper.add(block)
