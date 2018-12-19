import math
from trutle import *
import random
 
class Ball(Turtle):
	def__init__(self,radius,color,speed)
	Turtle.___init__(self)
	self.self('circle')
	self.shapesize(radius/10)
	self.radius = radius
	self.color(color)
	self.speed(speed)

ball1 = Ball(5, 'blue', 5)
ball2 = Ball(7, 'yellow', 5)

 
def check_collision(ball1,ball2):
	d = math.sqrt(math.pow((ball1.xcor()- ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2)))
	return(d)