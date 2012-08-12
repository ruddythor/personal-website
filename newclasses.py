#!usr/bin/env


class Circle():
	def __init__(self, cx, cy, r, stroke_width):
		self.cx=cx
		self.cy=cy
		self.r=r
		self.stroke_width=stroke_width

	def draw(self):
		return "<circle cx=\"%d\" cy=\"%d\" r=\"%d\" stroke=\"black\" stroke-width=\"%d\" fill=\"none\"/>" % (self.cx, self.cy, self.r, self.stroke_width)


class Rectangle():
	def __init__(self, rx, ry, width, height, stroke_width):
		self.rx=rx
		self.ry=ry
		self.width=width
		self.height=height
		self.stroke_width=stroke_width

	def draw(self):
		return "<rect x=\"%d\" y=\"%d\" width=\"%d\" height=\"%d\" style=\"fill:none;%d:1;stroke:rgb(0,0,0)\"/>" % (self.rx, self.ry, self.width, self.height, self.stroke_width)


#class Triangle():
#	return "<polygon points=\"200,10 250,190 160,210\" style=\"stroke:purple;stroke-width:1\"/>"




class SVG:
	def __init__(self, filename):
		self.filename=filename
		self.mylist=[]

	def addshape(self, shape):
		self.mylist.append(shape)

	def writefile(self):
		header="<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">"
		footer="</svg>"
		thefile=open(self.filename, "w")
		thefile.write(header)
		thefile.write("\n")
		for x in self.mylist:
			thefile.write(x.draw())
			thefile.write("\n")
		thefile.write(footer)
		thefile.close()



#print
#print
circle=Circle(200, 200, 200, 2)
rect=Rectangle(150, 150, 50, 50, 2)
mysvg=SVG("mysvgfile.xml")
for x in range(1,18):
	cx=35*x
	cy=2**(float(x/2.0))
	circle=Circle(cx, cy, 50, 2)
	mysvg.addshape(circle)
for x in range(18,36):
	cx=35*x
	y=abs(36-x)
	cy=2**(float(y/2.0))
	circle=Circle(cx, cy, 50, 2)
	mysvg.addshape(circle)


#mysvg.addshape(circle)

#rect2=Rectangle(50, 150, 50, 50, 2)
#mysvg.addshape(rect2)
mysvg.writefile()



