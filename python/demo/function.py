i=1
def test(var=i):
	print(var)

test()
test(23)

def f(a,l=[]):
	l.append(a)
	print(l)
f(1)
f(2)
f(3)
f(4,[5])

def ff(a,l=None):
	if l is None:
		l = []
	l.append(a)
	print(l)
ff(1)
ff(2)
ff(3)
#关键字参数
def p(a,b='x',c='y',d='z'):
	print(a,b,c,d)
p(10)
p(5.0,'A')
p(10,c='A')
p(10,'A',d='C')
p(10,'A','B','C')

#可变参数
'''
动态生成目录结构
'''
def b(*a,k='/'):
	return k.join(a)
print(b('a','b','c'))

#参数拆分
# 在参数列表[]前加一个*可以实现参数的拆分
print(list(range(3,6))) # 3 4 5
print(list(range(*[3,6]))) # 3 4 5
print(list(range(*[0,10,2])))  # 0 2 4 8

#在字典参数前加两个*可以实现字典拆分
def dict(a,b='x',c='y'):
	print(a,b,c)
d = {'a':10,'b':'B','c':'C'}
dict(**d)

#文档字符串,将文档注释写在一个fun方法中，当调用fun的变量__doc__时，就可以将fun中的文档注释打印出来。
def doc():
	'''
	Your name is Sum,
	and you are so nice!
	'''
	pass
print(doc.__doc__)

