"""
Course: CISC108
Assignment: Lab 2:
Section A: Simple Python Data
Section B: Turtles
Author: Dina Dawood
"""

# Put all modules that need to be imported here without indentation

import math
import turtle

# Problem 1.
# Printed 8 to the power of 4
# Printed the value of the arithmetic as a float
def problem1():
    print(math.pow(8, 4))
    print((5+6)*(34/7))

# Problem 2.
#Assigned the variable leftover to the remainder of 87 mod 8 and printed.
def problem2():
    leftover = 87%8
    print("Leftover = ", leftover)

# Problem 3.
def problem3():
    width = 17
    height = 12.0
#1 Evaluating the expression and printing the value and type
    print(width/2)
    print(type(width/2))
#2 Evaluating the expression and printing the value and type
    print(width/2.0)
    print(type(width/2.0))
#3 Evaluating the expression and printing the value and type
    print(height/3)
    print(type(height/3))
#4 Evaluating the expression and printing the value and type
    print(1+2*5)
    print(type(1+2*5))

# Problem 4.
# Made two variables hours and rate, set their type, and input them for the user
# Then printed the result
def problem4():
    hours = int(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    print(hours * rate)

# Problem 5.
#
def problem5():
    t = float(input("Enter Temperature (F): "))
    v = float(input("Enter Wind Speed (mph): "))
    w = 35.74 + (0.6215*t) + (0.4275*t -35.75) * math.pow(v, 0.16)
    print(w)
    
# Problem 6.
def problem6():
    # Asks user to input a cost, inputs that into the total cost equation and displays final cost
    itemCost = input("Enter cost of item: ")
    totalCost = "{:.2f}".format(float(itemCost) * 15)
    print("Total Cost: $ ", totalCost)

# Problem 7.
def problem7():
    # All values already given, asks user to input the years and results in final amount
    P = 10000
    n = 12
    r = 0.08
    t = int(input("Enter number of years: "))
    A = print(P*(1 + r/n)**(n*t))

# Problem 8.
def problem8():
    # Creates a turtle named dina that draws a "L"
    wn = turtle.Screen()
    dina = turtle.Turtle()
    dina.right(90)
    dina.forward(150)
    dina.left(90)
    dina.forward(75)
    
    dina.clear()
    
# Problem 9.
def problem9():
    # Creates a turtle named alex that draws a check mark
    wn = turtle.Screen()
    alex = turtle.Turtle()
    alex.right(45)
    alex.forward(75)
    alex.left(90)
    alex.forward(150)
    
    alex.clear()

# Problem 10.
def problem10():
    # Creates a turtle named tim that turns to face west and draws a straight line
    wn = turtle.Screen()
    tim = turtle.Turtle()
    tim.right(180)
    tim.forward(75)
    
    tim.clear()
    
# Problem 11.
def problem11():
    # Creates a turtle named mark that draws a capital T in white on a green background
    wn = turtle.Screen()
    wn.bgcolor("green")
    mark = turtle.Turtle()
    mark.color("white")
    mark.pensize(10)
    mark.left(90)
    mark.forward(150)
    mark.left(90)
    mark.forward(50)
    mark.right(180)
    mark.forward(100)
    
    mark.clear()

# Problem 12.
def problem12():
    # Creates two turtles, jamal & tina, one draws a "L" and other draws line toward west
    wn = turtle.Screen()
    wn.bgcolor("white")
    
    jamal = turtle.Turtle()
    jamal.color("blue")
    jamal.pensize(10) 
    jamal.right(90)
    jamal.forward(150)
    jamal.left(90)
    jamal.forward(75)
    
    tina = turtle.Turtle()
    tina.color("orange")
    tina.pensize(10)
    tina.right(180)
    tina.forward(75)
    
    tina.clear()
    jamal.clear()

# Problem 13.
def problem13():
    # Creates two turtles, jamal & tina that draw a straight line facing north/west
    wn = turtle.Screen()
    
    jamal = turtle.Turtle()
    jamal.color("blue")
    jamal.pensize(10)
    jamal.left(90)
    jamal.forward(150)
    
    tina = turtle.Turtle()
    tina.color("orange")
    tina.pensize(10)
    tina.forward(150)
    
    tina.clear()
    jamal.clear()

# Problem 14.
def problem14():
    # Blue-filled Triangle 
    wn = turtle.Screen()
    
    triangle = turtle.Turtle()
    triangle.color("black", "blue")
    triangle.pensize(10)
    triangle.begin_fill()
    
    for i in range(3):
        triangle.forward(150)
        triangle.left(120)
        
    triangle.end_fill()
    triangle.clear()

    # Blue-filled Square 
    square = turtle.Turtle()
    square.color("black", "blue")
    square.pensize(10)
    square.begin_fill()
     
    for i in range(4):
        square.forward(150)
        square.left(90)
         
    square.end_fill()
    square.clear()
    
    # Blue-filled Hexagon 
    hexagon = turtle.Turtle()
    hexagon.color("black", "blue")
    hexagon.pensize(10)
    hexagon.begin_fill()
     
    for i in range(6):
        hexagon.forward(150)
        hexagon.left(60)
         
    hexagon.end_fill()
    hexagon.clear()

    # Blue-filled Octagon 
    octagon = turtle.Turtle()
    octagon.color("black", "blue")
    octagon.pensize(10)
    octagon.begin_fill()
     
    for i in range(8):
        octagon.forward(150)
        octagon.left(45)
         
    octagon.end_fill()
    octagon.clear()

# Problem 15.
def problem15():
    # Creates a clock with 12 ticks and 13 turtles
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    moe = turtle.Turtle()
    moe.color("blue")
    moe.shape("turtle")
    move = 30
    moe.pensize(3)
    #moe.up()
    for i in range(12):
        moe.up()
        moe.forward(120)
        moe.down()
        moe.forward(10)
        moe.up()
        moe.forward(15)
        moe.stamp()
        moe.home()
        moe.left(move)
        move = move + 30
                

    wn.exitonclick()
        
if __name__ == "__main__":
    # To test your code, uncomment the relevant problem below, save and hit run. Every comment has a space following the hash - make sure you remove this space so that all indentation are same.
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem6()
    problem7()
    problem8()
    problem9()
    problem10()
    problem11()
    problem12()
    problem13()
    problem14()
    problem15()
