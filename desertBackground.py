#PROGRAMMERS:      JOSH HUBNER, JACOB ROMEO, MATTHEW DIELMAN, KATELYNN SILVANO
#PROGRAM NAME:     DESERT BACKGROUND
#DATE:             4/9/2019
#PROGRAM PURPOSE:  TO DRAW A DESERT BACKGROUND USING TURTLE GRAPHICS
################################################################################
# DEFINING THE MAIN FUNCTION
# THIS CALLS ALL THE OTHER FUNCTIONS AS WELL AS POSITIONING EACH FUNCTION
def main():
	import turtle;
	import random;
	drawSky();
	turtle.goto(-200, 200);
	drawCloud();
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
	turtle.goto(-108,-2);
	drawSmallCactus();
	turtle.goto(-70,-10);
	drawSmallCactus();			
	turtle.goto(240,0);
	drawSmallCactus();
	turtle.goto(50, -120);
	makeTumbleweed();
	turtle.goto(-275, -275);
	makeTumbleweed();
	makeBlink();
################################################################################
# DEFINING THE "drawStopSign" FUNCTION THAT DRAWS THE OUTLINE OF A STOP SIGN
def drawStopSign():
	import turtle;
	turtle.speed(0);
	turtle.pensize(3);
	turtle.hideturtle();
	turtle.pendown();
	turtle.begin_fill();
	turtle.color("white");
	turtle.setheading(22);
	turtle.circle(22, steps = 8)
	turtle.end_fill();
	turtle.begin_fill();	
	turtle.setheading(180);
	turtle.forward(1);
	turtle.setheading(90);
	turtle.forward(2);	
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
################################################################################
# DEFINING THE "makeStopStop" FUNCTION THAT WRITES STOP ON A STOP SIGN
def makeStopStop():
	import turtle;
	turtle.speed(0);
	turtle.pendown();
	turtle.write("STOP", font = ("Times", 9, "bold"));
	turtle.penup();
################################################################################
# DEFINING THE "drawCactus" FUNCTION THAT DRAWS A CACTUS
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
################################################################################
# DEFINING THE "drawSky" FUNCTION THAT SETS THE BACKGROUND AS BLUE AND SIZES THE DISPLAY
def drawSky():
	import turtle;
	#ESTABLISHING SCREEN SIZE
	turtle.setup(700, 600);
	turtle.bgcolor("#7e6fde");
	turtle.penup();
	turtle.hideturtle();
################################################################################
# DEFINING THE "drawSand" FUNCTION THAT DRAWS THE SAND
def drawSand():
	import turtle;
	turtle.speed(0);
	turtle.penup();
	turtle.goto(-500, 25);
	turtle.color("#d9bb43");
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
################################################################################	
# DEFINING THE "drawHorRoad" FUNCTION THAT DRAWS THE HORIZONTAL ROAD
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
################################################################################
# DEFINING THE "drawHorRoadLines" FUNCTION THAT DRAWS THE HORIZONTAL ROAD LINES
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
################################################################################
# DEFINING THE "drawVertRoad" FUNCTION THAT DRAWS A VERTICAL ROAD
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
################################################################################
# DEFINING THE "drawVertRoadLines" FUNCTION THAT DRAWS THE VERTICAL ROAD LINES
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
################################################################################	
# DEFINING THE "drawSmallCactus" FUNCTION THAT DRAWS A SMALL CACTUS
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
################################################################################	
# DEFINING THE "drawHorStopSignLines" FUNCTION THAT DRAWS THE LINES ON THE ROAD FOR EACH HORIZONTAL STOP SIGN
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
################################################################################	
# DEFINING THE "drawVertStopSignLines" FUNCTION THAT DRAWS THE LINES ON THE ROAD FOR EACH VERTICAL STOP SIGN
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
################################################################################
# DEFINING THE "drawSideStopSign" FUNCTION THAT DRAWS A SIDEWAYS STOP SIGN
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
################################################################################
# DEFINING THE "makeBlink" FUNCTION THAT MAKES THE STOP SIGNS BLINK
def makeBlink():
	for num in range (9999):
		import turtle;
		turtle.goto(14, -50);
		turtle.setheading(180);
		turtle.forward(1);
		turtle.setheading(90);
		turtle.forward(2);
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
		turtle.setheading(180);
		turtle.forward(1);
		turtle.setheading(90);
		turtle.forward(2);
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
		turtle.penup();
################################################################################		
def drawCloud():
        import turtle;
        turtle.setheading(0);
        turtle.pendown();
        turtle.fillcolor("white");
        turtle.begin_fill();
        turtle.pensize(1);
        turtle.circle(15, 180);
        turtle.rt(100);
        turtle.circle(20, 150);
        turtle.rt(100);
        turtle.circle(30, 180);
        turtle.rt(100);
        turtle.circle(25, 200);
        turtle.rt(70);
        turtle.circle(30, 70);
        turtle.rt(70);
        turtle.circle(12, 120);
        turtle.rt(30);
        turtle.circle(7, 90);
        turtle.end_fill();
        turtle.penup();
################################################################################	
def makeTumbleweed():
	import turtle
	import random
	turtle.speed(0);
	turtle.pendown();
	turtle.pensize(1);
	turtle.begin_fill();
	turtle.color("#52430a");
	turtle.end_fill();
	for num in range(30):
		turtle.circle(random.randint(1, 8));
		turtle.rt(random.randint(1, 5));
		turtle.circle(random.randint(1, 10));
		turtle.rt(random.randint(1, 5));
		turtle.circle(random.randint(1, 8));
		turtle.rt(random.randint(1, 5));
		turtle.circle(random.randint(1, 7));
		turtle.rt(random.randint(1, 5));
		turtle.circle(random.randint(1, 8));
		turtle.rt(random.randint(1, 8));
		turtle.circle(random.randint(1, 5));
	turtle.penup();
################################################################################
# CALLS THE MAIN FUNCTION	main();


input("blahblH");