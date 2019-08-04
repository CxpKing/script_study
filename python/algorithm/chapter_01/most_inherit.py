#多继承实例

class Point():
	x = 0.0
	y = 0.0

	def __init__(self,x,y):
		self.x = x
		self.y = y
		print("Point constructor")

	def Tostring(self):
		return "{X:"+str(self.x)+",Y:"+str(self.y)+"}"

class Size():
	width = 0.0
	height = 0.0

	def __init__(self,width,height):
		self.width = width
		self.height = height
		print("Size constructor")

	def Tostring(self):
		return "{Width:"+str(self.width)+",Height:"+str(self.height)+"}"

class Rectangle(Point,Size):
	def __init__(self,x,y,width,height):
		Point.__init__(self,x,y)
		Size.__init__(self,width,height)
		print("Rectangle constructor")

	def Tostring(self):
		return Point.Tostring(self)+","+Size.Tostring(self)

s = Size(80,90)
print(s.Tostring())

r = Rectangle(200,250,40,50)
print(r.Tostring())

# Size constructor
# {Width:80,Height:90}
# Point constructor
# Size constructor
# Rectangle constructor
# {X:200,Y:250},{Width:40,Height:50}