'''
在Python中，如果想找出列表中出现次数最多的元素，可以使用collections模块的Counter类，调用Counter类中的
函数most_common()来实现上述功能。
'''

from collections import Counter
words = [
	'loook','into','my','AAA','lock','the','into','AAA','the','AAA'
]

words_list = Counter(words)	#初始化Counter类
print(words_list.most_common())	#调用Counter类的most_common()方法，参数为元素出现的次数(无参数表示列出所有元素出现的次数)
# [('AAA', 3), ('into', 2), ('the', 2), ('loook', 1), ('my', 1), ('lock', 1)]
print(words_list.most_common(3))	#返回出现次数为2以上的字符
# [('into', 2), ('AAA', 3)]
print(words_list['AAA'])	#找到该对象的某个元素出现的次数
#3

c = Counter(a = 4,b = 1)
d = Counter(a = 1,b = 2)
print(c + d)
# Counter({'a': 5, 'b': 3})
print(c-d)
Counter({'a': 3})
print(c & d)
Counter({'a': 1, 'b': 1})
print(c | d)
Counter({'a': 4, 'b': 2})

print(dict(c))#将Counter转化为键值对
print(list(c))#将Counter的键转化列表
