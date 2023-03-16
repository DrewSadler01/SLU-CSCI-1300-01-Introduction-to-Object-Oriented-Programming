from cs1graphics import *

color=('light blue')
can=Canvas(800,800,color,'Project A')

sun=Layer()
body=Circle()
body.setRadius(55)
body.setFillColor('yellow')
body.move(650,100)
sun.add(body)
can.add(sun)

ground=Rectangle(800,300, Point(400,650))
ground.setFillColor('green')
can.add(ground)

tree1 = Layer()     ## Tree Start
trunk = Rectangle(20,100,Point(0,-50))
trunk.setFillColor('brown')
trunk.setBorderColor('brown')
tree1.add(trunk)
top = Polygon(Point(0,-100), Point(-50,-50), Point(0,-200), Point(50,-50))
top.setFillColor('forestGreen')
tree1.add(top)
tree1.moveTo(750,500)
can.add(tree1)  ## Tree End

mouse=Layer()   ## Rat Start
rb=Rectangle(60,15 ,Point(400,400))
rb.setFillColor('light grey')
rh=Circle(10, Point(430,395))
rh.setFillColor('light grey')
rlleg=Rectangle(5,20 ,Point(380,405))
rlleg.setFillColor('light grey')
rrleg=Rectangle(5,20 ,Point(420,405))
rrleg.setFillColor('light grey')
nose=Polygon(Point(430,385),Point(430,405),Point(448,395))
nose.setFillColor('light grey')
ear=nose.clone()
ear.rotate(-120)
ear.move(-11,15)
inner=ear.clone()
inner.setFillColor('light pink')
inner.move(2,4)
eye=Circle(1, Point(433,390))
eye.setFillColor('black')
tail=Rectangle(20,3,Point(370,400))
tail.rotate(-25)
tail.setFillColor('light grey')
mouse.add(tail)
mouse.add(ear)
mouse.add(inner)
mouse.add(nose)
mouse.add(rrleg)
mouse.add(rlleg)
mouse.add(rb)
mouse.add(rh)
mouse.add(eye)
can.add(mouse)
mouse.move(-150,155)   ## Rat End

tree3=tree1.clone()
tree3.move(-700,0)
can.add(tree3)
tree2=tree1.clone()
tree2.move(-440,75)
can.add(tree2)

house = Layer() ## House Start
facade = Rectangle(200, 100, Point(400,300))
facade.setFillColor('white')
house.add(facade)
door = Rectangle(37.5, 60, Point(400,320))
door.setFillColor('brown')
door.setBorderWidth(0)
house.add(door)
knob = Circle(2, Point(415,325))
##knob.setFillColor('')
house.add(knob)
roof = Polygon(Point(270,260), Point(530,260), Point(400,180))
roof.setFillColor('grey')
house.add(roof)
house.move(-200,225)
can.add(house)   ## House End

elephant=Layer()   ## Elephant Start
rb1=Rectangle(200,100 ,Point(400,400))
rb1.setFillColor('light grey')
rh1=Circle(40, Point(310,365))
rh1.setFillColor('light grey')
rlleg1=Rectangle(30,50 ,Point(340,450))
rlleg1.setFillColor('light grey')
rrleg1=Rectangle(30,50 ,Point(460,450))
rrleg1.setFillColor('light grey')
ear1=Polygon(Point(420,385),Point(460,385),Point(440,440))
tail1=Rectangle(50,5,Point(500,365))
tail1.setFillColor('light grey')
tail1.rotate(30)
ear1.setFillColor('light grey')
ear1.move(-120,-40)
eye1=Circle(5, Point(290,350))
eye1.setFillColor('black')
trunk=Rectangle(80,20,Point(280,398))
trunk.rotate(-60)
trunk.setBorderWidth(1)
trunk.setFillColor('light grey')
elephant.add(trunk)
elephant.add(rrleg1)
elephant.add(rlleg1)
elephant.add(tail1)
elephant.add(rb1)
elephant.add(rh1)
elephant.add(ear1)
elephant.add(eye1)
can.add(elephant)
elephant.move(550,100)   ## Elephant End
##elephant.move(-50,0)

## message=Text('sample', font size, Point)
from time import sleep

elephant.move(-25,0)
message=Text('What a nice day for a stroll!', 12,Point(652,400))
message.setFontColor('white')
can.add(message)
sleep(0.75)
elephant.move(-30,0)
sleep(0.75)
elephant.move(-30,0)
sleep(0.75)
elephant.move(-30,0)
sleep(0.75)
elephant.move(-30,0)
sleep(0.75)
elephant.move(-30,0)
sleep(0.75)
elephant.move(-30,0)
sleep(0.75)
elephant.move(-30,0)
sleep(0.75)
mouse.move(30,0)
sleep(0.75)
mouse.move(30,0)
message1=Text('Hello There!', 12,Point(355,530))
message1.setFontColor('black')
can.add(message1)
sleep(0.75)
sleep(0.75)
can.remove(message)
can.remove(message1)
message2=Text('EEEEKKK A MOUSE!!!!!',12,Point(652,400))
message2.setFontColor('white')
can.add(message2)
sleep(0.75)
rb1.setFillColor('white')
rh1.setFillColor('white')
trunk.setFillColor('white')
rrleg1.setFillColor('white')
rlleg1.setFillColor('white')
tail1.setFillColor('white')
ear1.setFillColor('white')
dedeye=Ellipse(5,25,Point(290,350))
dedeye.setFillColor('black')
dedeye2=dedeye.clone()
dedeye.rotate(45)
dedeye2.rotate(-45)
elephant.add(dedeye)
elephant.add(dedeye2)
can.remove(message2)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
sleep(0.50)
elephant.move(0,-45)
can.remove(elephant)
mouse.move(50,0)
sleep(0.50)
mouse.move(50,0)
sleep(0.50)
mouse.move(75,0)
message3=Text('Geez what is his deal, I was just saying hi', 12,Point(500,520))
message3.setFontColor('black')
can.add(message3)
sleep(0.75)
mouse.move(50,0)
can.remove(message3)
sleep(0.50)
mouse.move(50,0)
sleep(0.50)
mouse.move(50,0)
sleep(0.50)
mouse.move(50,0)
sleep(0.50)
mouse.move(50,0)
sleep(0.50)
mouse.move(50,0)
sleep(0.50)
mouse.move(50,0)
end=Rectangle(800,800,Point(400,400))
end.setFillColor('black')
can.add(end)
Ending=Text('The End',30,Point(400,400))
Ending.setFontColor('white')
can.add(Ending)
