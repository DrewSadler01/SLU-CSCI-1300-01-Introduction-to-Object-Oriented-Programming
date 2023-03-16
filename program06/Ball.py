from math import *

class Ball:
    def __init__(self,px,py,vx,vy): #This method assigns input values to class variables
        self._posX=px
        self._posY=py
        self._velX=vx
        self._velY=vy
    def getPositionX(self): #Calls for Position of X and returns X
        return self._posX
    def getVelocityX(self): #Calls for Velocity of X and returnts X
        return self._velX
    def getPositionY(self): #Calls for Position of Y and returns Y
        return self._posY
    def getVelocityY(self): #Calls for Velocity of Y and returnts Y
        return self._velY
    def advance(self,world): #Uses the addition of the Velocity of X&Y to affect the position of the ball
        self._posX=(self._posX + self._velX)
        self._posY=(self._posY + self._velY)
        self._velY=(self._velY + world.getGravity()) #Adds increasing force of Gravity to Y Velocity
        
