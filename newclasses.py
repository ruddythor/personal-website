#!usr/bin/env


class Circle():
	def __init__(self, filename):
		Name="Circle"
		self.filename=filename
	def circling(self, cx, cy, r, stroke_width):
		self.cx=cx
		self.cy=cy
		self.r=r
		self.stroke_width=stroke_width
		circle = open(self.filename, "w")
		circle.writelines("<circle cx=\"%d\" cy=\"%d\" r=\"%d\" stroke=\"black\" stroke-width=\"%d\" fill=\"none\"/>" % (self.cx, self.cy, self.r, self.stroke_width))
		circle.close()

circle=Circle("newxml.xml")
circle.circling(100, 100, 100, 2)



