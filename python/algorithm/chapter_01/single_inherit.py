#单继承实例

class Point():
	x = 0.0
	y = 0.0

	def __init__(self,x,y):
		self.x = x
		self.y = y
		print("Point constructor")

	def Tostring(self):
		return "{X:"+str(self.x)+",Y:"+str(self.y)+"}"

class Circle(Point):
	radius = 0.0

	def __init__(self,x,y,radius):
		super.__init__(x,y)
		self.radius = radius
		print("Circle constructor")

	def Tostring(self):
		return super().Tostring()+\
		",{RADIUS="+str(self.radius)+"}"


p = Point(20,20)

print(p.Tostring())

c = Circle(100,100,50)
print(c.Tostring())


# Point constructor
# {X:20,Y:20}
# Point constructor
# Circle constructor
# {X:100,Y:100},{RADIUS=50}
