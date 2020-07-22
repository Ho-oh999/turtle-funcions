import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("red")
turtle.setup(600,600)
turtle.shape("turtle")

screen = turtle.Screen()
bob = turtle.Turtle()

def triangle(length, color):
  bob.fillcolor(color)
  bob.begin_fill()
  x = 0
  while x <3:
    bob.forward(int(length))
    bob.right(120)
    x = 0
  bob.end_fill()
def circle(length, color):
  bob.fillcolor(color)
  bob.begin_fill()
  x = 0
  while x <100:
    bob.forward(int(length))
    bob.right(2)
    x = 0
    bob.end_fill()

input_shape = input("what shape do you want to draw?")
input_length = input("choose how big: ")
input_color = input("choose color: ")

if input_shape.lower() == "triangle":
  triangle(input_length, input_color)

elif input_shape.lower() =="star":
  print ("star")

elif input_shape.lower() == "circle":
  print ("circle")

 
