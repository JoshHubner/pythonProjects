def main():
	import turtle;
	drawSky();
	drawSand();
	drawHorRoad();
	turtle.goto(-75, -300);
	drawVertRoad();
	turtle.goto(225, -300);
	drawVertRoad();
	drawHorRoadLines();
	turtle.goto(-40, -109);
	drawVertRoadLines();
	turtle.goto(260, -109);
	drawVertRoadLines();	
	turtle.goto(-36, -106);
	drawHorStopSignLines();
	turtle.goto(265, -106);
	drawHorStopSignLines();	
	turtle.goto(-5,-65);
	drawVertStopSignLines();
	turtle.goto(295,-65);
	drawVertStopSignLines();
	turtle.goto(223,-105);
	drawVertStopSignLines();
	turtle.goto(-77,-105);
	drawVertStopSignLines();	
	turtle.goto(3, -28);
	drawSideStopSign();
	turtle.goto(303, -28);
	drawSideStopSign();	
	turtle.goto(-87, -113);
	drawSideStopSign();
	turtle.goto(213, -113);
	drawSideStopSign();	
	turtle.goto(14, -50);
	drawStopSign();
	turtle.goto(-8, -38);
	makeStopStop();
	turtle.goto(315, -50);
	drawStopSign();
	turtle.goto(293, -38);
	makeStopStop();
	turtle.goto(-225,-225);
	drawCactus();
	turtle.goto(-145,-265);
	drawCactus();
	turtle.goto(170,-220);
	drawCactus();
	turtle.goto(-285,-5);
	drawSmallCactus();
	turtle.goto(-245,5);
	drawSmallCactus();
	turtle.goto(-145,5);
	drawSmallCactus();
	turtle.goto(-110,-2);
	drawSmallCactus();
	turtle.goto(-70,-10);
	drawSmallCactus();
	turtle.goto(240,0);
	drawSmallCactus();
	makeBlink();
	
	
def drawStopSign():
	import turtle;
	turtle.speed(0);
	turtle.pensize(3);
	turtle.hideturtle();
	turtle.pendown();
	turtle.begin_fill();
	turtle.color("red");
	turtle.setheading(22);
	turtle.circle(20, steps = 8)
	turtle.end_fill();
	turtle.setheading(180);
	turtle.forward(13);
	turtle.setheading(270);
	turtle.penup();
	turtle.setheading(0);
	turtle.forward(5);
	turtle.setheading(270);
	turtle.forward(3);
	turtle.pendown();
	turtle.color("gray");
	turtle.pensize(5);
	turtle.forward(62);
	turtle.color("white");
	turtle.penup();
	
def makeStopStop():
	import turtle;
	turtle.speed(0);
	turtle.pendown();
	turtle.write("STOP", font = ("Times", 9, "bold"));
	turtle.penup();

def drawCactus():
	import turtle;
	turtle.speed(0);
	turtle.pensize(15);
	turtle.hideturtle();
	turtle.pendown();
	turtle.color("green");
	turtle.setheading(90);
	turtle.forward(100);
	turtle.pensize(10);
	turtle.setheading(270);
	turtle.forward(60);
	turtle.setheading(0);
	turtle.forward(30);
	turtle.setheading(90);
	turtle.forward(30);
	turtle.setheading(270);
	turtle.forward(30);
	turtle.setheading(180);
	turtle.forward(30);
	turtle.setheading(90);
	turtle.forward(15);
	turtle.setheading(180);
	turtle.forward(30);
	turtle.setheading(90);
	turtle.forward(15);
	turtle.penup();

def drawSky():
	import turtle;
	turtle.bgcolor("blue");

def drawSand():
	import turtle;
	turtle.speed(0);
	turtle.penup();
	turtle.goto(-500, 25);
	turtle.color("tan");
	turtle.pendown();
	turtle.begin_fill();
	turtle.setheading(0);
	turtle.forward(1000);
	turtle.setheading(270);
	turtle.forward(1000);
	turtle.setheading(180);
	turtle.forward(1000);
	turtle.setheading(90);
	turtle.forward(1000);
	turtle.end_fill();
	turtle.penup();
	
def drawHorRoad():
	import turtle;
	turtle.speed(0);
	turtle.penup();
	turtle.hideturtle();
	turtle.goto(-500, -34);
	turtle.color("black");
	turtle.pendown();
	turtle.begin_fill();
	turtle.setheading(0);
	turtle.forward(1000);
	turtle.setheading(270);
	turtle.forward(70);
	turtle.setheading(180);
	turtle.forward(1000);
	turtle.setheading(90);
	turtle.forward(70);
	turtle.end_fill();
	turtle.penup();

def drawHorRoadLines():
	import turtle;
	turtle.speed(0);
	turtle.goto(-315, -69);
	turtle.pendown();
	turtle.color("yellow");
	turtle.setheading(0);
	turtle.pensize(10);
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();

def drawVertRoad():
	import turtle;
	turtle.speed(0);
	turtle.hideturtle();
	turtle.color("black");
	turtle.pendown();
	turtle.begin_fill();
	turtle.setheading(90);
	turtle.forward(200);
	turtle.setheading(0);
	turtle.forward(70);
	turtle.setheading(270);
	turtle.forward(200);
	turtle.setheading(180);
	turtle.forward(70);
	turtle.end_fill();
	turtle.penup();

def drawVertRoadLines():
	import turtle;
	turtle.speed(0);
	turtle.pendown();
	turtle.color("yellow");
	turtle.setheading(270);
	turtle.pensize(10);
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	turtle.forward(25);
	turtle.pendown();
	turtle.forward(25);
	turtle.penup();
	
def drawSmallCactus():
	import turtle;
	turtle.speed(0);
	turtle.pensize(10);
	turtle.hideturtle();
	turtle.pendown();
	turtle.color("green");
	turtle.setheading(90);
	turtle.forward(50);
	turtle.setheading(270);
	turtle.forward(32);
	turtle.pensize(7);
	turtle.setheading(180);
	turtle.forward(15);
	turtle.setheading(90);
	turtle.forward(15);
	turtle.setheading(270);
	turtle.forward(15);
	turtle.setheading(0);
	turtle.forward(15);
	turtle.setheading(90);
	turtle.forward(10);
	turtle.setheading(0);
	turtle.forward(15);
	turtle.setheading(90);
	turtle.forward(10);
	turtle.penup();
	
def drawHorStopSignLines():
	import turtle;
	turtle.speed(0);
	turtle.color("white");
	turtle.setheading(0);
	turtle.pensize(3);
	turtle.hideturtle();
	turtle.pendown();
	turtle.forward(30);
	turtle.penup();
	
def drawVertStopSignLines():
	import turtle;
	turtle.speed(0);
	turtle.color("white");
	turtle.setheading(90);
	turtle.pensize(3);
	turtle.hideturtle();
	turtle.pendown();
	turtle.forward(30);
	turtle.penup();

def drawSideStopSign():
	import turtle;	
	turtle.pendown();
	turtle.setheading(90);
	turtle.color("gray");
	turtle.pensize(5);
	turtle.forward(62);
	turtle.penup();
	turtle.setheading(270);
	turtle.forward(5);
	turtle.pendown();
	turtle.color("red");
	turtle.setheading(90);
	turtle.pensize(2);
	turtle.forward(40);
	turtle.penup();

def makeBlink():
	for num in range (9999):
		import turtle;
		turtle.goto(14, -50);
		turtle.speed(0);
		turtle.pensize(3);
		turtle.hideturtle();
		turtle.pendown();
		turtle.begin_fill();
		turtle.color("red");
		turtle.setheading(22);
		turtle.circle(20, steps = 8)
		turtle.end_fill();	
		turtle.penup();
		turtle.goto(315, -50);
		turtle.pendown();
		turtle.begin_fill();
		turtle.color("red");
		turtle.setheading(22);
		turtle.circle(20, steps = 8)
		turtle.end_fill();	
		turtle.penup();
		turtle.color("white")
		turtle.goto(-8, -38);
		turtle.pendown();
		turtle.write("STOP", font = ("Times", 9, "bold"));
		turtle.penup();
		turtle.goto(293, -38);
		turtle.pendown();
		turtle.write("STOP", font = ("Times", 9, "bold"));
		turtle.penup()
	
	main();


input("blahblH");