#!/usr/bin/python3
import turtle
from Point import Point
from Line import Line, SCALEFACTOR

t = 0.005

def Setup():
	turtle.colormode(255)
	turtle.screensize(100, 100)
	turtle.penup()
	turtle.ht()

def Draw(P):
	turtle.pencolor(
	0,
	128,
	0
	)

	turtle.goto(P.x, P.y)
	turtle.pendown()

def Bezier(*L):
	if len(L) == 1:
		# Once we have a single line left,
		# parametrize it and draw at (t).
		C = L[0].getat(t)
		Draw(C)
		return

	R = list()
	# Acquire points in all lines and
	# link them together, before call
	# -ing the function recursively.
	P = [Line.getat(t) for Line in L]
	for i in range(0, len(P) - 1):
		Q = Line(P[i], P[i+1])
		R.append(Q)

	return Bezier(*R)

if __name__ == '__main__':
	# A set of hardcoded lines,
	# first drawn in a sheet of
	# paper.
	L0 = Line(Point(12, -6), Point(0, 0))
	L1 = Line(Point(0,0), Point(6,6))
	L2 = Line(Point(6,6), Point(10, 6))
	L3 = Line(Point(10,6), Point(16, 0))
	L4 = Line(Point(16, 0), Point(22, 6))
	L5 = Line(Point(22, 6), Point(20, 10))
	L6 = Line(Point(20, 10), Point(12, 12))

	# Initiate Turtle and Scale points.
	Setup()
	[L.scale(SCALEFACTOR) for L in (L0, L1, L2, L3, L4, L5, L6)]

	# Loop with small incrementation
	# steps(0.005) that give a good
	# amount of details.
	while t <= 1:
		Bezier(
		L0, L1, L2, L3, L4, L5, L6
		)
		t += 0.005

	# Hang
	input("Press any key to terminate.")
