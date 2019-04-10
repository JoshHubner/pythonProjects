# ====================================================================================================
# PROGRAMMER:               Josh Hubner
# PROGRAM NAME:             Assignment 7
# DATE WRITTEN:/REVISED:    3/21/2019
#
# PURPOSE:  To draw a checkerboard
# ====================================================================================================
#Importing turtle program.
import turtle;
# ====================================================================================================
#Establishing variables
north = 90;
south = 270;
east = 0;
west = 180;
tileSize = 30;
boardSize = 240;
# ====================================================================================================
#Defining main function.
def main():
	turtle.speed(0);
	turtle.penup();
	turtle.goto(-boardSize, boardSize);
	drawBoard(boardSize);
	drawOddRow(tileSize);
	drawEvenRow(tileSize);
	drawOddRow(tileSize);
	drawEvenRow(tileSize);
	drawOddRow(tileSize);
	drawEvenRow(tileSize);
	drawOddRow(tileSize);
	drawEvenRow(tileSize);
	gotcha(boardSize);
	
	
# ====================================================================================================
#Defining drawBoard function... this draws the board outline.
def drawBoard(boardSize):
	turtle.pendown();
	turtle.hideturtle();
	turtle.setheading(east);
	turtle.forward(boardSize);
	turtle.setheading(south);
	turtle.forward(boardSize);
	turtle.setheading(west);
	turtle.forward(boardSize);
	turtle.setheading(north);
	turtle.forward(boardSize);
	turtle.penup();
	
# ====================================================================================================
#Defining drawOddRow function... this draws an odd row.
def drawOddRow(tileSize):
	turtle.pendown();
	turtle.hideturtle();
	drawTile(tileSize);
	skipTile(tileSize);
	drawTile(tileSize);
	skipTile(tileSize);
	drawTile(tileSize);
	skipTile(tileSize);
	drawTile(tileSize);
	turtle.penup();
	turtle.setheading(south);
	turtle.forward(tileSize);
	turtle.setheading(west);
	turtle.forward(boardSize);
	turtle.setheading(east);

	# ====================================================================================================
#Defining drawEvenRow function... this draws an even row.
def drawEvenRow(tileSize):
	turtle.forward(tileSize);
	turtle.pendown();
	turtle.hideturtle();
	skipTile(tileSize);
	drawTile(tileSize);
	skipTile(tileSize);
	drawTile(tileSize);
	skipTile(tileSize);
	drawTile(tileSize);
	skipTile(tileSize);
	drawTile(tileSize);
	turtle.setheading(east);
	turtle.forward(tileSize);
	turtle.penup();
	turtle.setheading(south);
	turtle.forward(tileSize);
	turtle.setheading(west);
	turtle.forward(boardSize);
	turtle.setheading(east);

# ====================================================================================================
def drawTile(tileSize):
	turtle.begin_fill();
	turtle.setheading(east);
	turtle.forward(tileSize);
	turtle.setheading(south);
	turtle.forward(tileSize);
	turtle.setheading(west);
	turtle.forward(tileSize);
	turtle.setheading(north);
	turtle.forward(tileSize);
	turtle.end_fill();
		
# ====================================================================================================	
def skipTile(tileSize):	
	turtle.penup();
	turtle.setheading(east);
	turtle.forward(tileSize);
	turtle.forward(tileSize);	
# ====================================================================================================	
def gotcha(boardSize):
	turtle.setheading(south);
	turtle.forward(40);
	turtle.write("CHECKMATE!!!", font = ("Arial", "25", "bold"));
		
# ====================================================================================================
#Calls the main function.
main();
# ====================================================================================================
#END PROGRAM
input("Press any key to continue...");