from cs1graphics import *
from time import sleep
import random


class Elephant(Layer):
    
    def __init__(self, color='light grey'):
        """ Creates a instance of Elephant
        color: the base color of the entire Elephant(default light grey)
        """
        self._color=color
        super().__init__()
        # Body sits at the point of origin of the Elephant
        self._Body=Rectangle(200,100 ,Point(400,400))
        self._Body.setFillColor(color)
        # Head sits on the top left of the body, on the opposite end of the tail
        self._Head=Circle(40, Point(310,365))
        self._Head.setFillColor(color)
        # leftLeg attaches to the bottom of the body, below and slightly right of the of the head
        self._leftLeg=Rectangle(30,50 ,Point(340,450))
        self._leftLeg.setFillColor(color)
        # rightLeg attaches to the bottom of the body, below and slightly left of the of the tail
        self._rightLeg=Rectangle(30,50 ,Point(460,450))
        self._rightLeg.setFillColor(color)
        # Ear attatches to the middle of the head, slightly to the right of the eyes
        self._Ear=Polygon(Point(420,385),Point(460,385),Point(440,440))
        self._Ear.move(-120,-40)
        self._Ear.setFillColor(color)
        # Tail attaches to the far right side of the main body, right and slightly up from the point of origin
        self._Tail=Rectangle(50,5,Point(500,365))
        self._Tail.rotate(30)
        self._Tail.setFillColor(color)
        # Eye is slightly left and up from the center of the head, and left of the ear
        self._Eye=Circle(5, Point(290,350))
        self._Eye.setFillColor('black')
        # Trunk is attached to the front of the head, and the furthest left object on the Elephant
        self._Trunk=Rectangle(80,20,Point(280,398))
        self._Trunk.rotate(-60)
        self._Trunk.setBorderWidth(1)
        self._Trunk.setFillColor(color)

    def _draw(self):
        self._leftLeg._draw()
        self._rightLeg._draw()
        self._Tail._draw()
        self._Body._draw()
        self._Trunk._draw()
        self._Head._draw()
        self._Ear._draw()
        self._Eye._draw()

    def setColor(self,color):
        """
        Changes the color Body,Head,leftLeg,rightLeg,Ear,Tail,Trunk
        Eye was the only thing that was unchanged
        """
        self._color=color
        self._Body.setFillColor(color)
        self._Head.setFillColor(color)
        self._leftLeg.setFillColor(color)
        self._rightLeg.setFillColor(color)
        self._Ear.setFillColor(color)
        self._Tail.setFillColor(color)
        self._Trunk.setFillColor(color)

    def changeTrunk(self):
        """
        Changes the size of the trunk to a random length to add varity to Elephants
        """
        a=random.randint(60,100)
        b=random.randint(1,7)
        self._Trunk=Rectangle(a,20,Point(280,398))
        self._Trunk.setBorderWidth(b)
        self._Trunk.rotate(-60)
        self._Trunk.setFillColor(self._color)
        
    def tailUp(self):
        """
        Rotates the tail to a random degree, so that each one is different
        """
        rotation=random.randint(-60,20)
        width=random.randint(1,7)
        self._Tail.setBorderWidth(width)
        self._Tail.rotate(rotation)

if __name__ == '__main__':
    can=Canvas(800,800,'light green','Elephant')

    dan=Elephant()
    dan.tailUp()
    dan.setColor("blue")
    dan.changeTrunk()
    dan.move(350,100)
    can.add(dan)

    rick=Elephant()
    rick.tailUp()
    rick.changeTrunk()
    rick.setColor("yellow")
    rick.move(400,-250)
    can.add(rick)

    dave=Elephant()
    dave.tailUp()
    dave.changeTrunk()
    dave.move(400,250)
    can.add(dave)

    daisy=Elephant()
    daisy.tailUp()
    daisy.changeTrunk()
    daisy.setColor("pink")
    daisy.move(350,-100)
    can.add(daisy)

    for c in range(50):
        rick.move(-40,0)
        sleep(0.20)
        dave.move(-40,0)
        sleep(0.20)
        daisy.move(-40,0)
        sleep(0.20)
        dan.move(-40,0)
        sleep(0.20)

