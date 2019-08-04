s = 'abc'
a = slice(2,4,1)#start,stop,step
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
	print('s',i,'=',s[i])
#slice实现了切片的功能