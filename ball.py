from turtle import *

class Ball(Turtle):
	def __init__(self, x, y ,dx, dy, r, color):
	  	Turtle.__init__(self)
	  	self.penup()
	  	self.goto(x,y) 
	  	self.dx = dx
	  	self.dy = dy
	  	self.r = r
	 	self.shape("circle")
	 	self.shapesize(self.r/10)
	 	self.color(color )   
	def move (self ,sceen_width , screen_height):
		current_x = self.xcor()
		current_y = self.ycor()
		new_x = current_x + self.dx 
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		bottom_side_ball = new_y - self.r
		top_side_ball = new_y + self.r
		self.goto(new_y,new_x)
		if right_side_ball 

	def new_Ball (self, x, y ,dx, dy, r, color) :
		self.penup()
	  	self.goto(x,y) 
	  	self.dx = dx
	  	self.dy = dy
	  	self.r = r
	 	self.shape("circle")
	 	self.shapesize(self.r/10)
	 	self.color(color)    

