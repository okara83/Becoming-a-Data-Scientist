import random
import turtle
import math



def drawCircle (drunkard):
    "This function draws the enclosure with a 30 degree opening"
    drunkard.color("black")
    drunkard.pensize(3)
    drunkard.penup()
    drunkard.setpos(0,-100)
    drunkard.pendown()
    drunkard.circle(100, 330)
    drunkard.up()
    drunkard.setpos(0,0)
    drunkard.down()
   

def drunkWalk (n, drunkard):
    """
	This part of the code is the drunkard's random walk. It simulates a random path function with restrictions depending
	on where the particle is. The random walk function makes advances in any direction of a magnitude between 0 and 10 units.

	Parameters:
	n = number of steps for the drunkard to leave the enclosure
	drunkard = the turtle object
	"""
    drunkard.pencolor("dark magenta")
    drunkard.pensize(1)
    x = 0
    y = 0
    for i in range(n+1):
        x = x+1
        if x <=1000:
            drunkard.speed(1000000)
            xlim = (drunkard.xcor())
            ylim = (drunkard.ycor())
            angle = random.uniform(0,360)
            dist = random.uniform(0,10)
            drunkard.setheading(angle)
            drunkard.forward(dist)
            xbound = (drunkard.xcor())
            ybound = (drunkard.ycor())
        
			#setting the bounds for the turtle object to remain within the circle enclosure
            rad = math.sqrt(xbound**2 + ybound**2)
            angle = math.degrees(math.atan(xbound/ybound))

			#all the if statements that follow allow for the random movement to be made with a flashing color
			#just a fun visual effect to go with the simulation

            
            if rad <=100:
                drunkard.goto(xlim, ylim)
                drunkard.color("red")
           
                drunkard.goto(xbound, ybound)

            if rad <=100:
                drunkard.goto(xlim, ylim)
                drunkard.color("yellow")
               
                drunkard.goto(xbound, ybound)

            if rad <=100:
                drunkard.goto(xlim, ylim)
                drunkard.color("green")
                
                drunkard.goto(xbound, ybound)

            if  rad <=100:
                drunkard.goto(xlim, ylim)
                drunkard.color("RoyalBlue")
               
                drunkard.goto(xbound, ybound)

            #when the drunkard finds the opening the path line switches colors to red and prints the result 
            elif (rad > 100) and (0 <= angle <= 30) and (xbound < 0):
                drunkard.goto(xlim, ylim)
                drunkard.color("red")
                drunkard.goto(xbound, ybound)

                print("The drunkard has left the enclosure after hobbling about for " ,x, "steps.")
                break

            else: #keeps the drunkard moving in the direction	
                drunkard.goto(xlim, ylim)
        else:
            print("The drunkard stays trapped in the enclosure even after 1000 steps.")



if __name__ == "__main__":
    atlas = turtle.Turtle()
    atlas.hideturtle()
    atlas.speed(10)
    drawCircle(atlas)
    n = 1000                        #limiting the number of steps
    drunkWalk(n,atlas)
    screen=atlas.getscreen()
    screen.exitonclick()

