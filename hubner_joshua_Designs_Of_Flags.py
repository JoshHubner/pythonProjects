#PROGRAMMER: JOSHUA HUBNER
#PROGRAM: DESIGN
#DATE: 2/10/2019

import turtle;

#CREATING VARIABLES SO THAT THE SCREEN SIZE CAN BE CHANGED
screenWidth = 600;
screenHeight = 600;
#USING THIS METHOD TO ESTABLISH THE COMPASS IS A GREAT IDEA!!!
north = 90;
south = 270;
east = 0;
west = 180;

#ESTABLISHING SCREEN SIZE
turtle.setup(screenWidth, screenHeight);

#ESTABLISHING TURTLE SPEED
turtle.speed(0);

#FIRST FLAG
turtle.hideturtle();
turtle.pendown();
turtle.fillcolor("yellow");
turtle.begin_fill();
turtle.setheading(east);
turtle.forward(150);
turtle.setheading(north);
turtle.forward(33);
turtle.setheading(west);
turtle.forward(150);
turtle.setheading(south);
turtle.forward(33);
turtle.end_fill();
turtle.penup();
turtle.goto(0,33);
turtle.pendown();
turtle.fillcolor("red");
turtle.begin_fill();
turtle.setheading(east);
turtle.forward(150);
turtle.setheading(north);
turtle.forward(33)
turtle.setheading(west);
turtle.forward(150);
turtle.setheading(south);
turtle.forward(33);
turtle.end_fill();
turtle.penup();
turtle.goto(0,67);
turtle.pendown();
turtle.fillcolor("black");
turtle.begin_fill();
turtle.setheading(east);
turtle.forward(150);
turtle.setheading(north);
turtle.forward(33)
turtle.setheading(west);
turtle.forward(150);
turtle.setheading(south);
turtle.forward(33);
turtle.end_fill();
turtle.penup();

#SECOND FLAG
turtle.goto(-200,0);
turtle.pendown();
turtle.setheading(east);
turtle.forward(150);
turtle.setheading(north);
turtle.forward(100);
turtle.setheading(west);
turtle.forward(150);
turtle.setheading(south);
turtle.forward(100);
turtle.penup();
turtle.goto(-150,50);
turtle.pendown();
turtle.fillcolor("red");
turtle.begin_fill();
turtle.circle(25);
turtle.end_fill();
turtle.penup();

#THIRD FLAG
turtle.goto(-200,-150);
turtle.pendown();
turtle.fillcolor("green");
turtle.begin_fill();
turtle.setheading(east);
turtle.forward(50);
turtle.setheading(north);
turtle.forward(100);
turtle.setheading(west);
turtle.forward(50);
turtle.setheading(south);
turtle.forward(100);
turtle.end_fill();
turtle.penup();
turtle.goto(-150,-150);
turtle.pendown();
turtle.fillcolor("white");
turtle.begin_fill();
turtle.setheading(east);
turtle.forward(50);
turtle.setheading(north);
turtle.forward(100);
turtle.setheading(west);
turtle.forward(50);
turtle.setheading(south);
turtle.forward(100);
turtle.end_fill();
turtle.penup();
turtle.goto(-100,-150);
turtle.pendown();
turtle.fillcolor("orange");
turtle.begin_fill();
turtle.setheading(east);
turtle.forward(50);
turtle.setheading(north);
turtle.forward(100);
turtle.setheading(west);
turtle.forward(50);
turtle.setheading(south);
turtle.forward(100);
turtle.end_fill();
turtle.penup();

#FOURTH FLAG
turtle.goto(0,-150);
turtle.pendown();
turtle.setheading(east);
turtle.forward(150);
turtle.setheading(north);
turtle.forward(100);
turtle.setheading(west);
turtle.forward(150);
turtle.setheading(south);
turtle.forward(100);
turtle.penup();
turtle.goto(65,-135);
turtle.pendown();
turtle.fillcolor("red");
turtle.begin_fill();
turtle.setheading(east);
turtle.forward(15);
turtle.setheading(north);
turtle.forward(30);
turtle.setheading(east);
turtle.forward(30);
turtle.setheading(north);
turtle.forward(15);
turtle.setheading(west);
turtle.forward(30);
turtle.setheading(north);
turtle.forward(30);
turtle.setheading(west);
turtle.forward(15);
turtle.setheading(south);
turtle.forward(30);
turtle.setheading(west);
turtle.forward(30);
turtle.setheading(south);
turtle.forward(15);
turtle.setheading(east);
turtle.forward(30);
turtle.setheading(south);
turtle.forward(30);
turtle.end_fill();
turtle.penup();

#REESTABLISHING TURTLE SPEED
turtle.speed(1);

#ADDING LABELS TO THE FLAGS
turtle.goto(25,100);
turtle.write("GERMANY", font = ("Arial", "17", "bold"));
turtle.goto(-130,100);
turtle.write("JAPAN", font = ("Arial", "17", "bold"));
turtle.goto(-160,-50);
turtle.write("IRELAND", font = ("Arial", "17", "bold"));
turtle.goto(0,-50);
turtle.write("SWITZERLAND", font = ("Arial", "17", "bold"));

#END PROGRAM