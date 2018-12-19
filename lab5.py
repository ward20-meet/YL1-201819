import random
from import turtle *
colormode(255) 
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shape = "square"
		self.size = 5
		self.random_color = (r,g,b)
	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color(r, g, b)





		