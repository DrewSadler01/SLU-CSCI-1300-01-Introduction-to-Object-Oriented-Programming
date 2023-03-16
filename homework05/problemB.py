from cs1graphics import *
paper=Canvas(500, 300,'lightgray','The Zoo')

animal = Layer()
body = Rectangle(200, 100)
body.setFillColor('white')
body.move(250, 200)
body.setBorderWidth(5)
animal.add(body)

head = Circle(50)
head.setFillColor('brown')
head.move(350, 150)
animal.add(head)
animal.adjustReference(250,200)
animal.rotate(-30)

paper.add(animal)
