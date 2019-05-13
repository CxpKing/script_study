import math

class Apple(object):
	def __init__(self,color='red',weight='50',kind='红富士'):
		self.color = color
		self.weight = weight
		self.kind = kind

a = Apple()
print(a.color)

'''Circle

calculate area
'''
class Circle(object):
	def __init__(self,r):
		if not isinstance(r, int):
			print("您的圆半径不合理！")
		else:
			self.r = r
	def area(self):
		return (math.pi)*(self.r)**2
	
c = Circle(5)
print(c.area())

'''Triangle

calculate area
'''
class Triangle(object):
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def area(self):
		return self.a*self.b
t = Triangle(3,5)
print(t.a,t.b,t.area())

'''Hexagon

calculate perimeter
'''
class Hexagon(object):
	def __init__(self,r):
		self.r = r
	def perimeter(self):
		return 6*self.r
h = Hexagon(6)
print(h.r,h.perimeter())




