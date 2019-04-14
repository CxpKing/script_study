import urllib.request
#指定爬取的网站的地址，返回一个服务器响应的数据
response = urllib.request.urlopen("http://www.baidu.com")
#方式1
#data = response.read()
#print(type(data))
#with open(r"F:\file\file.html","wb") as f:
#    f.write(data)

#方式2 读取一行
#data = response.readline()

#方式3 把读取到的数据赋值给一个列表
data = response.readlines()
print(data)
'''
print(data)
print(type(data))
print(len(data))
print(type(data[100].decode("utf-8")))
'''
#reponse常用属性
'''
print(response.info()) #返回当前环境的有关信息
print(response.getcode()) #放回请求状态码
print(response.geturl()) #返回

'''
#urllib.request.unquote()方法把url中的wd的编码还原回去
url = "https://www.baidu.com/s?wd=%E9%87%8F%E5%AD%90%E7%89%A9%E7%90%86&rsv_spt=1&rsv_iqid=0x900b7fba0025d081&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=24&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&inputT=8214&rsv_sug4=16585"
newUrl = urllib.request.unquote(url)
print(newUrl)
#编码
newUrl2 = urllib.request.quote(newUrl)
print(newUrl2)