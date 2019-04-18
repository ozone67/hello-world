#Produce 4 nested equilateral triangles.
#Space of 7 units between horizontal base lines.
#Each triangle larger than previous.
#initial triangle side = 20

#import the turtle functions
from turtle import *

#Initialize variables
line_size=20 #Initial line size
number_of_shapes=4 #Change this to draw more triangles
line_spacing=7

#Create outer(main) loop for number of triangles
for triangles in range(4):
    #Draw triangle of size line_size
    for triangle_sides in range(3):
        pendown()
        forward(line_size)
        left(120)
        penup()
    #Move to start of next triangle
    line_size=line_size+20
    right(90)
    forward(7)
    right(90)
    forward(10)
    right(180)
        
    
