from Point import Point
SCALEFACTOR	= 12

class Line:
	def __init__(self, p1, p2):
		'''
		Line Segment(2D)
		Constructed using P1 and P2
		  * (P1)
		   \
		    \  (Line)
		     \
		      * (P2)
		'''
		self.p1, self.p2 = p1, p2

	def __str__(self):
		return "Line (%s, %s)" % (self.p1, self.p2)

	def getat(self, t):
		'''
		Get point at T in the current Line.
		'''
		return Point(
		(1 - t) * self.p1.x + t * self.p2.x,
		(1 - t) * self.p1.y + t * self.p2.y
		)

	def scale(self, factor):
		'''
		Scales P1 and P2 coordinates with a certain factor.
		'''
		self.p1.x *= factor
		self.p2.x *= factor
		self.p1.y *= factor
		self.p2.y *= factor
