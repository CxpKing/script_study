p = (1,2,3)
one,two,three = p 	#python支持将序列（可迭代对象的元素分解为独立的变量，前提是变量总数需要与p的元素个数吻合）
print(one,two,three)
data = ['Acme',10,67.3,(1992,2,3)]
name,age,wight,birth = data
print(name,age,wight,birth,sep=':\n',end=';\n')

# Acme:
# 10:
# 67.3:
# (1992, 2, 3);

records = [
	('AAA',1,2,3),
	('BBB','hello',1),
	('CCC','E',3,8)
]

def AAA(*arg):
	print('AAA',*arg)
def BBB(*arg):
	print('BBB',*arg)

for tag,*arg in records:
	if tag == 'AAA':
		AAA(*arg)
	elif tag == 'BBB':
		BBB(*arg)

line = 'https://www.baicu.com:80'
prot,*addr,port = line.split(':')
print(prot,*addr,port)

