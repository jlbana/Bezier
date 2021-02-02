class Point:
	def __init__(self, x, y):
		'''
		Point(2D)
		^
		| * (X, Y)
		|
		*-------->
		'''
		self.x, self.y = x, y

	def __str__(self):
		return "(%d, %d)" % (self.x, self.y)
