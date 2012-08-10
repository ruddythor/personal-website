#!usr/bin/env


class Circle():
	def __init__(self, cx, cy, r, stroke_width):
		self.cx=cx
		self.cy=cy
		self.r=r
		self.stroke_width=stroke_width

	def draw(self):
		return ("<circle cx='" + str(self.cx) +"'>" )
#		return ("<circle cx=\"%d\" cy=\"%d\" r=\"%d\" stroke=\"black\" stroke-width=\"%d\" fill=\"none\"/>")


circle=Circle(100, 100, 100, 2)
print str(circle.draw())




