import sys
argvs = sys.argv
sys.stderr.write('Sorry program is not working!') #警告信息
for arg in argvs:
    print(arg)

#设置默认输入法
sys.setdefautencoding('utf-8')