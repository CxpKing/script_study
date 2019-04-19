'''
关于python的数据类型，元组、列表、字典以及集合四大
数据类型的定义、使用及其各自的特性
'''
#元组
tup1 = ('A','B','C')
print('tup1->',tup1)
#列表
list1 = ['A','B','C']
print('list1->',list1)
#字典
dict1 = {'key1':'value1','key2':'value2'}
print('dict1->',dict1)
#集合
#方式1 使用符号 {}
set1 = {'A','B','C'}
print('set1->',set1)
#方式2 使用 set() 其参数为一个元组，
set2 = set(('A','B','C'))
print('set2->',set2)

'''特性'''

##--------------------start-------------------列表
print('------------------start-------------------list')
#计算元组长度
print('length of list1->',len(list1))
#判断元素是否在元组中
bl = 'A' in list1
print('A in list1->',bl)
#获取元素，下标和切片
print('get list1[2]->',list1[2])
print('list1 chip->',list1[0:2])
#增
list1.append('D')
print('list1 add->',list1)
#删 remove pop
list1.remove('D')
print('list1 delete->',list1)
#改
list1[0] = 'F'
print('change list1[0]->',list1)
#加法
list2 = [1,2]
l = list1+list2
print('list1+list2->',l)
#乘法
l1 = list1*3
print('list1*3->',l1)
print('-------------------end--------------------list')
##---------------------end--------------------列表


##--------------------start-------------------元组
print('------------------start-------------------tuple')
#计算元组长度
print('length of tup1->',len(tup1))
#判断元素是否在元组中
b = 'A' in tup1
print('A in tup1->',b)
#获取元素，下标法以及切片使用
print('get tup1[0]->',tup1[0])
print('chip tup1[0:2]->',tup1[0:2])
#没有增加元素的方法
#改
print('tup1[0] = \'F\' is not allowed')
#元组运算符
#元组的加法
tup2 = (1,2)
t = tup1+tup2
print('tup1+tup2->',t)
#乘法 只能乘数字
t1 = tup1*2
print('tup1*2->',t1)
#删除
del tup1 
#特殊性质
tup2 = (10)
print('type of tup2=(10) ->',type(tup2))
tup3 = (10,)
print('type of tup3=(10,) ->',type(tup3))
print('-------------------end--------------------tuple')
##---------------------end--------------------元组

##--------------------start-------------------字典
print('------------------start-------------------dict')
#获取字典的长度
print('length of dict1->',len(dict1))
#判断字典元素是否存在,只能判断键
bd = 'key1' in dict1
print('key1 in dict1->',bd)
#获取字典的值,通过键去获取对应的值
print('dict1[\'key1\']->',dict1['key1'])
print('-------------------end--------------------dict')
##---------------------end--------------------字典

##--------------------start-------------------集合
print('------------------start-------------------set')
set2 = {'B','C','D'}
print('set1->',set1)
print('set2->',set2)
#获取集合长度
print('length of set1->',len(set1))
#集合的常规运算 交集，并集，差集以及 并集-交集
##交集
s1 = set1 & set2
print('交集 set1 & set2 ->',s1)
##并集
s2 = set1 | set2
print('并集 set1 | set2 ->',s2)
##差集set1对set2
s3 = set1 - set2
print('差集 set1 - set2 ->',s3)
##不同时属于两集合的元素
print('不同时属于两集合的元素 ->')
s4 = s2-s1
print('	方式1：并集-交集 ->',s4)
s5 = s1 ^ s2
print('	方式2：set1^set2 ->',s5)
#增加
set1.add('F')
print('set1.add(\'F\') ->',set1)
set1.update({'M','N'})
print('set1.update({\'M\',\'N\'}) ->',set1)
#移除
set1.remove('A')
print('set1.remove(\'A\') ->',set1)
#随机删除一个元素
set1.pop()
print('返回被删除的元素 set1.pop() ->',set1.pop(),',pop 随机删除一个元素后 set1.pop() ->',set1)
print('-------------------end--------------------set')
##---------------------end--------------------集合