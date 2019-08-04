from collections import deque
#--------------------
#实现记录符合的搜索行最近的搜索记录
#--------------------
def search(lines,pattern,history=5):
	previous_lines = deque(maxlen=history)	#使用deque(len)创建一个固定长度为len的队列
	for line in lines:	#遍历文本行
		if pattern in line:	#如果查找的内容在改行出现，就然返回改行内容以及deque队列对象
			previous_lines.append(line)
			yield line,previous_lines
if __name__ == '__main__':
	with open('test.txt') as file:
		for line,prevlines in search(file,'python',3):
			# print(prevlines)
			for pline in prevlines:
				print(pline)
			# print(line)
			print('-'*20)

# pythonpythonpythonpy1

# --------------------
# pythonpythonpythonpy1

# pythonpythonpythonpy3

# --------------------
# pythonpythonpythonpy1

# pythonpythonpythonpy3

# pythonpythonpythonpy5

# --------------------
# pythonpythonpythonpy3

# pythonpythonpythonpy5

# pythonpythonpythonpy8

# --------------------
# pythonpythonpythonpy5

# pythonpythonpythonpy8

# pythonpythonpythonpy10

# --------------------
# pythonpythonpythonpy8

# pythonpythonpythonpy10

# pythonpythonpythonpy12
# --------------------
#--------------------
#实现记录符合的搜索行最新的搜索记录以及其附近的行
#--------------------

def search1(lines,pattern,history=5):
	previous_lines = deque(maxlen=history)	#使用deque(len)创建一个固定长度为len的队列
	for line in lines:	#遍历文本行
		previous_lines.append(line)	#将本次搜索行的内容添加到deque队列中
		if pattern in line:	#如果查找的内容在改行出现，就然返回改行内容以及deque队列对象
			# previous_lines.append(line)
			yield line,previous_lines
if __name__ == '__main__':
	with open('test.txt') as file:
		for line,prevlines in search1(file,'python',3):
			# print(prevlines)
			for pline in prevlines:
				print(pline)
			print('当前行--',line)
			print('-'*20)
# pythonpythonpythonpy1

# 当前行-- pythonpythonpythonpy1

# --------------------
# pythonpythonpythonpy1

# 3434-2

# pythonpythonpythonpy3

# 当前行-- pythonpythonpythonpy3

# --------------------
# pythonpythonpythonpy3

# 132324-4

# pythonpythonpythonpy5

# 当前行-- pythonpythonpythonpy5

# --------------------
# 453465-6

# 56546-7

# pythonpythonpythonpy8

# 当前行-- pythonpythonpythonpy8

# --------------------
# pythonpythonpythonpy8

# 56546-9

# pythonpythonpythonpy10

# 当前行-- pythonpythonpythonpy10

# --------------------
# pythonpythonpythonpy10

# 6758-11

# pythonpythonpythonpy12
# 当前行-- pythonpythonpythonpy12
# --------------------