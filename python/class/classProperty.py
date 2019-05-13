'''class property

封装、抽象、继承、多态
''' 

'''封装

封装包含两个概念：
1、将变量（状态）和方法（改变状态或执行涉及状态的计算）都集中在一个地方--对象本身
2、隐藏类的内部数据，以避免客户端（client）代码（即外部代码）直接访问对象变量
''' 

class Demo(object):
	def __init__(self):
		self.num = [1,2,3,4,5]
		print(self.num)
	def change(self,index,data):
		self.num[index] = data
d = Demo()
d.change(0,100)
print(d.num)
d.num[1] = 200
print(d.num)

'''抽象

将同一类事物将其共同的特征提取出来进行建模。
'''
'''继承

类似于java等编程语言的继承.创建类时，默认不写父类object时，python默认就是继承的object,所以我们自定义的父类，子类
父类就将object换为自己定义的类名即可，此时我们创建的类就是子类，其拥有了父类的public属性和方法。
% 当然继承也可以像java一样，可以有方法的重写
'''

class Father(object):
	name = ""
	age = 0
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def fun(self):
		print("Father's function!")

	def __unsafe(self):
		print("The fun is that children can't use ")

class Children(Father):
	def fun(self):
		print("Children changed father's fun!")

	def skill(self,*skill):
		self.skill = skill

father = Father("John",40)
children = Children("Bob",5)
print(children.name)  #c.__num is error
print(children.age)
children.skill("打游戏","跑步")
print(children.skill)

class Dog(object):
	def __init__(self,name,breed,owner):
		self.name = name
		self.breed = breed
		self.owner = owner
	def fun(self):
		print("I'm a dog")

class Person(object):
	def __init__(self,name):
		self.name = name

jack = Person("jack")
dog = Dog("coco","TaiDi",jack)
print(dog.owner.name," has a dog named ",dog.name)
f = dog.fun
print(f)
f()


'''私有变量的处理

[description]
'''
class Cat(object):
	__name = "jack"

	def setName(self,name):
		self.__name = name

	def getName(self):
		return self.__name

c = Cat()
print(c.getName())
c.setName("john")
print(c.getName())

class Student(object):
	hobbies = []
	def __init__(self,name):
		self.name = name
	def addHobby(self,hobby):
		self.hobbies.append(hobby)

s = Student("cxp")
s.addHobby("读书")
s2 = Student("sss")
s2.addHobby("打游戏")
print(s.hobbies)

print(issubclass(Student,object))






















