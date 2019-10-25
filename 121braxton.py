# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random

#-----game configuration----
turtleshape ="turtle"
turtlesize = 5
turtlecolor ="red"



score = 0

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
Kevin=trtl.Turtle(shape=turtleshape)
Kevin.color(turtlecolor)
Kevin.shapesize(turtlesize)
Kevin.speed(0)

scorekeeper = trtl.Turtle()
counter = trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(275,275)

#-----game functions--------
def Turtle_clicked(x,y):
    print("kevin got clicked")
    change_position()
    update_score()

    

def change_position():
    Kevin.penup()
    Kevin.ht()
    Kevinx = random.randint(-400,400)
    Keviny = random.randint(-300,300)
    Kevin.goto(Kevinx,Keviny)
    Kevin.st()

def update_score():
    global score
    score +=1
    print(score)
    scorekeeper.penup()
    scorekeeper.goto(-400,350)
    scorekeeper.clear()
    scorekeeper.write(score, font=font_setup)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        counter.write("GAME OVER", font=font_setup)
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
wn = trtl.Screen()
Kevin.onclick(Turtle_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()