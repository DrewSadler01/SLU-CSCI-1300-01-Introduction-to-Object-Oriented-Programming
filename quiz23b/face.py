############################
# Students: drew.sadler@slu.edu  (Drew Sadler)
############################

from cs1graphics import *
from time import sleep

class Face(Layer):

    def __init__(self, skinTone='lavender'):
        super().__init__()
        self._check = False
        self._disc = Circle(100)
        self._disc.setFillColor(skinTone)
        self.add(self._disc)
        self._leftEye = Circle(5)
        self._leftEye.setFillColor('black')
        self._leftEye.move(-25,-25)
        self.add(self._leftEye)
        self._rightEye = self._leftEye.clone()
        self._rightEye.move(50,0)
        self.add(self._rightEye)

        self._mouth = Spline()
        self._mouth.addPoint(Point(-50,30))
        self._mouth.addPoint(Point(0,50))
        self._mouth.addPoint(Point(50,30))
        self.add(self._mouth)
        
    def setColor(self, color):
        self._disc.setFillColor(color)

    def speak(self,message=('')):
        self._text = Text('',20,Point(-110,25))
        self._text.setMessage(message)
        self.add(self._text)
        sleep(.95)
        self.remove(self._text)

        
    def closeEyes(self):
        self.remove(self._leftEye)
        self.remove(self._rightEye)
        self._leftEye = Path(Point(-20,-25),Point(-30,-25))
        self._leftEye.setBorderWidth(5)
        self._rightEye = self._leftEye.clone()
        self._rightEye.move(50,0)
        self.add(self._leftEye)
        self.add(self._rightEye)
    def openEyes(self):
        self._leftEye = Circle(5)
        self._leftEye.setFillColor('black')
        self._leftEye.move(-25,-25)
        self.add(self._leftEye)
        self._rightEye = self._leftEye.clone()
        self._rightEye.move(50,0)
        self.add(self._rightEye)
        
    def frown(self):
        if(self._check == False):
            self._mouth.flip(90)
        self._check=True
        
    def smile(self):
        if(self._check == True):
            self._mouth.flip(90)
        self._check=False
        
if __name__ == '__main__':
    paper = Canvas(800,300)

    lefty = Face()
    lefty.moveTo(200,150)
    paper.add(lefty)
    righty = Face('orange1')
    righty.moveTo(500,150)
    paper.add(righty)
    sleep(2)
    righty.speak('Hello')
    sleep(2)
    righty.speak('')
    lefty.speak('Hi')
    sleep(2)
    lefty.speak("Don't blink")
    sleep(2)
    righty.closeEyes()
    sleep(1)
    righty.openEyes()
    lefty.speak()
    lefty.frown()
    sleep(2)
    righty.speak('Oops')
    righty.setColor('pink')
    righty.frown()
    sleep(2)
    righty.speak('')
    lefty.smile()
    lefty.speak("It's ok")
