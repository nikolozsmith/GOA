from turtle import *


#we want to paint a house 

#step one draw a sqare

shape("turtle")

speed(5)
color("purple")

width(5)

forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)
#end of squaer 

#drawing a door

left(90)

begin_fill()

forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

end_fill()

penup()
goto(200,200)
pendown()

color("red")

begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
exitonclick()

#we want to make windows 

penup()

#end