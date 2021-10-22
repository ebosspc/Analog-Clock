#PLTW Lesson 1.1.9 Project

#Author: Ethan Francolla

#This program will attempt to use the features in python and the turtle library to draw a working clock on the screen
#Due to the limitations of python turtle this program will not be perfectly accurate
#However, all hands should function as intended

#Import turtle library for drawing functions and objects
import turtle as trtl

#Define lists of fillcolors, pencolors, and shapes for painter objects to be used later on down the line
painter_shapes = ['classic', 'classic', 'classic', 'classic']
painter_fillcolors = ['black', 'red', 'black', 'black']
painter_pencolors = ['black', 'red', 'black', 'black']

#Define the object that will draw the clock body and define its initial properties
clock_painter = trtl.Turtle()
clock_painter.penup()
clock_painter.fillcolor(painter_fillcolors.pop(0))
clock_painter.pencolor(painter_pencolors.pop(0))
clock_painter.shape(painter_shapes.pop(0))
clock_painter.speed(0)
clock_painter.pensize(6)
clock_painter.goto(0,-250)

#Draw the outside body of the clock
clock_painter.pendown()
clock_painter.circle(250)
clock_painter.penup()

#Draw the center of the clock
clock_painter.penup()
clock_painter.goto(0,-6)
clock_painter.pendown()
clock_painter.pensize(13)
clock_painter.circle(6)

#Draw every major tick on the edges of the clock for each hour or every 5 minutes

#Define initial values for major ticks drawing
clock_painter.penup()
clock_painter.pensize(5)
clock_painter.goto(0,0)
tick_heading = 0

#For loop to draw 12 major ticks for each hour
for major_ticks in range(12):
    clock_painter.penup()
    clock_painter.goto(0,0) #Reset painter back to zero every tick
    clock_painter.setheading(tick_heading) #Set heading for each tick
    clock_painter.forward(205) #Position painter to proper starting spot for each tick
    clock_painter.pendown()
    clock_painter.forward(45) #Draw the actual tick
    tick_heading = tick_heading + 30 #Increase heading by 30 to get 12 evenly spaced ticks total

#Define initital values for 48 minor ticks 
clock_painter.penup()
clock_painter.pensize(3)
clock_painter.goto(0,0)
tick_heading = 0

#For loop to draw each of the 48 minor ticks on the clock, skipping the major oens already drawn
for minor_ticks in range(60):
    #Ensure no minor and major ticks overlap by not drawing a minor tick every 5 iterations
    if (minor_ticks % 5) == 0:
        clock_painter.penup()
        clock_painter.goto(0,0)

    #Draw minor ticks like normal if no problems
    else: 
        clock_painter.penup()
        clock_painter.goto(0,0)
        clock_painter.setheading(tick_heading) #Set heading for each tick
        clock_painter.forward(220) #Position painter to proper starting spot for each tick
        clock_painter.pendown()
        clock_painter.forward(30) #Draw the actual tick

    #Increase heading by 6 to get 60 evenly spaced ticks minus the 12 major ticks for a total of 48
    tick_heading = tick_heading + 6

#Write the number 12 on the upper-most major tick
clock_painter.penup()
clock_painter.goto(0,0)
clock_painter.setheading(90)
clock_painter.forward(165)
clock_painter.write(12, move = False, align = 'center', font = ('Arial', 25, 'normal'))

#Write the number 9 on the left-most major tick
clock_painter.penup()
clock_painter.goto(0,-18)
clock_painter.setheading(180)
clock_painter.forward(185)
clock_painter.write(9, move = False, align = 'center', font = ('Arial', 25, 'normal'))

#Write the number 6 on the lower-most major tick
clock_painter.penup()
clock_painter.goto(2,0)
clock_painter.setheading(270)
clock_painter.forward(200)
clock_painter.write(6, move = False, align = 'center', font = ('Arial', 25, 'normal'))

#Write the number 3 on the right-most major tick
clock_painter.penup()
clock_painter.goto(0,-18)
clock_painter.setheading(0)
clock_painter.forward(185)
clock_painter.write(3, move = False, align = 'center', font = ('Arial', 25, 'normal'))

#Hide body drawing turtle after it is done drawing and doesn't get in the way
clock_painter.hideturtle()

#Create second hand on clock
second_hand = trtl.Turtle()
second_hand.penup()
second_hand.goto(0,0)
second_hand.shape(painter_shapes.pop(0))
second_hand.fillcolor(painter_fillcolors.pop(0))
second_hand.pencolor(painter_pencolors.pop(0))
second_hand.pensize(3)
second_hand_heading = 90
second_hand.setheading(second_hand_heading)

#Create minute hand on clock
minute_hand = trtl.Turtle()
minute_hand.penup()
minute_hand.goto(0,0)
minute_hand,trtl.shape(painter_shapes.pop(0))
minute_hand.fillcolor(painter_fillcolors.pop(0))
minute_hand.pencolor(painter_pencolors.pop(0))
minute_hand.pensize(4)
minute_hand_heading = 90
minute_hand.setheading(minute_hand_heading)

#Set minute hand to initial position
minute_hand.penup()
minute_hand.goto(0,0)
minute_hand.pendown()
minute_hand.forward(165)

#Create hour hand on clock
hour_hand = trtl.Turtle()
hour_hand.penup()
hour_hand.goto(0,0)
hour_hand.shape(painter_shapes.pop(0))
hour_hand.fillcolor(painter_fillcolors.pop(0))
hour_hand.pencolor(painter_pencolors.pop(0))
hour_hand.pensize(5)
hour_hand_heading = 90
hour_hand.setheading(hour_hand_heading)

#Set hour hand to initial position
hour_hand.penup()
hour_hand.goto(0,0)
hour_hand.pendown()
hour_hand.forward(128)

#Define second, minute, and hour tracker variables
seconds = 0
minutes = 0
hours = 0

#While loop to keep second, minute, and hour hands running for a full 12 hour cycle
while (hours < 12):
    #If 1 hour has passed, move hour hand
    if (minutes % 60 == 0):
        #Move hour hand over 1 hour
        hour_hand.clear()
        hour_hand.penup()
        hour_hand.goto(0,0)
        hour_hand.setheading(hour_hand_heading)
        hour_hand.pendown()
        hour_hand.forward(128)

        #Incremennt hour hand heading by 30 degrees every iteration to allow it to hit every major tick once in 12 iterations
        hour_hand_heading = hour_hand_heading - 30

        #Set second, minute, and hour trackers to apropriate values
        hours = hours + 1
        minutes = 0
        seconds = 0

    #If 1 minute has passed, move minute hand
    if (seconds % 60 == 0):
        #Move minute hand over 1 minute
        minute_hand.clear()
        minute_hand.penup()
        minute_hand.goto(0,0)
        minute_hand.setheading(minute_hand_heading)
        minute_hand.pendown()
        minute_hand.forward(165)

        #Incremennt minute hand heading by 6 degrees every iteration to allow it to hit every tick once in 60 iterations
        minute_hand_heading = minute_hand_heading - 6

        #Set second and minute trackers to appropriate values
        minutes = minutes + 1
        seconds = 0

    #Move second hand forward every second
    second_hand.penup()
    second_hand.goto(0,0)
    second_hand.setheading(second_hand_heading)
    second_hand.pendown()
    second_hand.forward(200)
    second_hand.clear()
    second_hand.penup()
    
    #Incremennt second hand heading by 6 degrees every iteration to allow it to hit every tick once in 60 iterations
    second_hand_heading = second_hand_heading - 6

    #Incremement seconds counter by 1 after each second
    seconds = seconds + 1

#Keep screen persistent and displayed even after objects are done drawing
window = trtl.Screen()
window.mainloop()
