#!usr/bin/env


#The purpose of the program is to examine object-oriented programming and its features, like classes.


class SVG:
	def __init__(self):
		Name="woeijf"
# HAVE A WRITE FILE
	def createfile(self, filename):
		svgfile = open(filename, "w")
		svgfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">")
		svgfile.close()

#HAVE AN ADD SHAPE
#have svg keep array of circles.

class Shape(SVG):
	def __init__(self):
		Name="Something"
	def circling(self, filename):
		circle = open(filename, "a")
		circle.writelines("<circle cx=\"100\" cy=\"100\" r=\"100\" stroke=\"black\" stroke-width=\"2\" fill=\"none\" />")
		circle.close()
	def rectangling(self):
		rectangle = open(filename, "a")
		rectangle.writelines("<rect width=\"300\" height=\"100\" style=\"fill:rgb(0,0,255);stroke-width:1;stroke:rgb(0,0,0)\"/>")
		rectangle.close()
	def triangling(self):
		triangle = open(filename, "a")
		triangle.writelines("<polygon points=\"200,10 250,190 160,210\" style=\"stroke:purple;stroke-width:1\"/>")
		triangle.close()


class Endsvg():
	def __init__(self):
		Name="something"
	def closesvg(self, filename):
		append = open(filename, "a")
		append.writelines("</svg>")
		append.close()

#A=Shape(circle, 10, 10)
#a.function

#svg=SVG()
#svg.createfile("myxml.xml")

circle=Shape()
circle.createfile("myxml.xml")
circle.circling("myxml.xml")

closed=Endsvg()
closed.closesvg("myxml.xml")
