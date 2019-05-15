for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {'one':1, 'two':2}:
    print(key)

for char in "123":
    print(char)

for line in open("a.txt"):
	print(line,end='')

'''迭代器的实现过程

在for语句中调用it = iter(迭代对象),然后调用next(it)方法迭代该对象的元素。
'''
s = "asdhgjg"
it = iter(s)
print(next(it))

'''自定义迭代器

通过上述实现过程，可以自定义类，并且在该类中自定义自己的迭代器。
定义一个 __iter__() 方法来返回一个带有 __next__() 方法的对象。 如果类已定义了 __next__()，则 __iter__() 可以简单地返回 self:
'''
class C:
	def __init__(self,data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		return self
	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

c = C("sdsf")
for i in c:
	print(i)

'''生成器

Generator是用于创建迭代器的简单而强大的工具。他们的写法类似标准的函数	，但当他们要返回数据时会使用yield语句。每次对生成器调用next()方法时
他会从上次	离开的位置恢复执行（他会记住上次执行语句时的所有数值）。
'''				
'''自定义生成器

相较于迭代器来说简单得多，因为它会自动创建__iter__ __next__方法，且当生成器输出最后一个元素后，会自动引发StopIteration
'''
def reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]

for i in reverse("cxp"):
	print(i)

'''有趣的生成器表达式

'''
x = [i*i for i in [1,2,3]]
print(x)

a = [1,2,3]
b = [4,5,6]
l = [x*y for x,y in zip(a,b)]
print(l)

from math import pi,sin
sin_table = {x:sin(x*pi/180) for x in range(0,91)}
print(sin_table)

'''九九乘法
'''
table = [x*y for x in range(1,10) for y in range(1,10) if x >= y ]
print(table)



