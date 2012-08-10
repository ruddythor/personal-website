#!usr/bin/env


class Circle():
	def __init__(self):
		Name="Circle"
	def circling(self, filename, cx, cy, r, stroke_width):
		self.filename=filename
		self.cx=cx
		self.cy=cy
		self.r=r
		self.stroke_width=stroke_width
		circle = open(filename, "w")
		circle.writelines("<circle cx=\"%d\" cy=\"%d\" r=\"%d\" stroke=\"black\" stroke-width=\"%d\" fill=\"none\"/>" % cx, cy, r, stroke_width)
		circle.close()

circle=Circle()
circle.circling("newxml.xml", 100, 100, 100, 2)



