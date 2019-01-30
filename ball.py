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
	def move (self ,screen_width , screen_height):
		print(screen_height,screen_width)
		current_x = self.xcor()
		current_y = self.ycor()
		new_x = current_x + self.dx 
		new_y = current_y + self.dy
		print(self.dx,self.dy)
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		bottom_side_ball = new_y - self.r
		top_side_ball = new_y + self.r
		self.goto(new_x,new_y)
		print("NEW X Y",new_x,new_y)
		if right_side_ball > screen_width:
			self.dx=-self.dx
			print("hit right wall")

		if left_side_ball < -screen_width:
			self.dx=-self.dx
			print("hit left wall")

		if top_side_ball > screen_height:
			self.dy=-self.dy
			print("hit top wall")

		if bottom_side_ball < -screen_height:
			self.dy=-self.dy
			print("hit bottom wall")

	def new_Ball (self, x, y ,dx, dy, r, color) :
		self.penup()
	  	self.goto(x,y) 
	  	self.dx = dx
	  	self.dy = dy
	  	self.r = r
	 	self.shape("circle")
	 	self.shapesize(self.r/10)
	 	self.color(color)    

