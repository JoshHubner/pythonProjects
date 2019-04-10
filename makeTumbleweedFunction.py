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