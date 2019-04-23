'''
类的声明与使用：
class Class_name:
	1、类的声明
	2、类的属性和方法
	3、类的内置属性和方法
	4、类的实例化
'''

class Calculate:
	name = 'Calculate ||'
	def add(self,*args):
		print(self.name)
		sum = 0
		for x in args:
			sum+=x
		return sum
		

c = Calculate()
print(c.add(1,2,3,4))




