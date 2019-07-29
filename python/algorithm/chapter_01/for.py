#for循环本质 Python的for循环本质上就是通过不断调用next()函数实现
# for item in [1,2,3]:
# 	print(item)
#这里的for循环等同于下面的方法

for item in [1,2,3]:
 	print(item)

# 等价于不断调用next()函数
it = iter([1,2,3])
while True:
	try:
		# 迭代器的next()方法
		x = next(it)
		print(x)
	except StopIteration:
		# 遇到StopIteration退出
		break