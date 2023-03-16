"""An implementation of a hierarchy of different ball classes for simulation"""
####################################################################
# Student Names: Drew Sadler

####################################################################




# a world supports methods getWidth() and getHeight() and getBalls()
from world import World

####################################################################

class Ball:
    def __init__(self, r, x, y, vx, vy):
        self._r = r
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getRadius(self):
        return self._r

    def getColor(self):
        return 'black'

    def advance(self, world):
        self._x += self._vx
        self._y += self._vy

####################################################################

# utility method for bouncing along an arbitrary axis
def clip(pos, vel, low, high):
    """Return newPos,newVel that remains in range low to high."""
    if vel > 0:
        if pos > high:
            pos = high - (pos-high)
            vel = -vel
    else:
        if pos < low:
            pos = low + (low-pos)
            vel = -vel
    return pos,vel

class BouncingBall(Ball):
    def getColor(self):
        return 'skyblue'
    def advance(self, world):
        super().advance(world)
        w = world.getWidth()
        h = world.getHeight()
        self._x,self._vx = clip(self._x, self._vx, self._r, w-self._r)
        self._y,self._vy = clip(self._y, self._vy, self._r, h-self._r)

####################################################################

class DampeningBall(BouncingBall):
    def getColor(self):
        return 'orange'
    def advance(self,world):
        super().advance(world)
        VelocityVX=self._vx
        VelocityVY=self._vy
        if (VelocityVX != self._vx):
            self._vx*=(0.5)
            self._vy*=(0.5)
            return self._vx
        if (VelocityVY != self._vy):
            self._vx*=(0.5)
            self._vy*=(0.5)
            return self._vy

####################################################################

class WrappingBall(Ball):
    def getColor(self):
        return 'light green'
    def advance(self, world):
        super().advance(world)
        thickness=world.getWidth()
        tallness=world.getHeight()
        if (self._x<0):
            self._x=(thickness+self._x)
        elif (self._x>thickness):
            self._x=(thickness-self._x)
        elif (self._y<0):
            self._y=(tallness+self._y)
        elif (self._y>tallness):
            self._y=(tallness-self._y) 

####################################################################

#class ExplosiveBall(Ball):
#    def getColor(self):
#        return 'red'

####################################################################

#class ExplosiveWrappingBall(ExplosiveBall, WrappingBall):
#    def getColor(self):
#        return 'darkgreen'

####################################################################

#class ExplosiveBouncingBall(ExplosiveBall, BouncingBall):
#    def getColor(self):
#        return 'blue'

####################################################################
