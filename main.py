from turtle import *

speed(0)
move_distance = 20
bgcolor("#D2691E")
penup()
goto(100, 200)
pendown()

color("blue")
begin_fill()
goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)
end_fill()

color("green")
penup()
goto(-200, 0)
shape("turtle")


def move_up():
  setheading(90)
  forward(move_distance)
  check_goal()
 

 
def move_down():
  setheading(270)
  forward(move_distance)
  check_goal()
  
def move_left():
  setheading(180)
  forward(move_distance)
  check_goal()
  
def move_right():
  setheading(0)
  forward(move_distance)
  check_goal()

onkey(move_up, "w")
onkey(move_down, "s")
onkey(move_left, "a")
onkey(move_right, "d")


def check_goal():
  if xcor() > 100:
    hideturtle()
    color("yellow")
    write("YOU WIN!!!!")
    onkey(None, "w")
    onkey(None, "s")
    onkey(None,"a")
    onkey(None, "d")
    
listen()

mainloop()
