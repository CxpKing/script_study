import urllib.request
urllib.request.urlretrieve("http://www.baidu.com",r"F:\file\file2.html")
#这个方法会生成缓存一般需要清除缓存
#清除缓存
urllib.request.urlcleanup()