import turtle
import time
import random
import math
from ball import Ball
from turtle import *
bgcolor("black")
turtle.colormode(1)
turtle.tracer(0)
turtle.hideturtle()
running = True

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
my_ball = Ball(0,0,5,10,100,"blue")
number_of_balls = 1
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
BALLS = []

for i in range (number_of_balls):
	x = random.randint(-screen_width+maximum_ball_radius,screen_width - maximum_ball_radius)
	y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx , maximum_ball_dx)
	dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	r = random.randint(minimum_ball_radius,maximum_ball_radius)
	color = (random.random(),random.random(),random.random())

	Ball2 = Ball(x,y,dx,dy,r,color)
	BALLS.append(Ball2)

def move_all_balls():
	for ball in BALLS:
		ball.move(screen_width,screen_height)
def collide (ball_a , ball_b):
    if ball_a == ball_b:
        return False
    d = math.sqrt(math.pow(ball_a.xcor() - ball_b.xcor() , 2) + math.pow(ball_a.ycor() - ball_b.ycor() , 2))
    if ball_a.r + ball_b.r >= d:
        return True
    else :
        return False

def check_all_balls_collisions():
	all_balls=[]
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
	for ball_a in all_balls:
		for ball_b in all_balls: 
			if collide(ball_a, ball_b): 
				print("COLLID")
				r1 = ball_a.r
				r2 = ball_b.r
				x = random.randint(-screen_width+maximum_ball_radius,screen_width - maximum_ball_radius)
				y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
				dx = random.randint(minimum_ball_dx , maximum_ball_dx)
				dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				r = random.randint(minimum_ball_radius,maximum_ball_radius)
				color = (random.random(),random.random(),random.random())
				if r1 > r2:
					ball_a.r += 1 
					ball_a.shapesize(ball_a.r/10)
					ball_b.new_Ball(x,y,dx,dy,r,color)
					if my_ball == ball_b:
						running = False
				if r2 > r1:
					ball_b.r += 1
					ball_b.shapesize(ball_b.r/10)
					ball_a.new_Ball(x,y,dx,dy,r,color)
					if my_ball == ball_a:
						running = False

def movearound():
 	my_ball.goto(turtle.getcanvas().winfo_pointerx()-screen_width ,screen_height - turtle.getcanvas().winfo_pointery())


while running == True :
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height =  turtle.getcanvas().winfo_height()/2




	movearound() 
	move_all_balls()
	check_all_balls_collisions()

	turtle.update() 
	time.sleep(0.1)




	





































turtle.mainloop() 