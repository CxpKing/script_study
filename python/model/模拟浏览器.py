import urllib.request
url = "http://www.baidu.com"
#设置一个浏览器请求头
headers = {
    "User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
#设置一个请求体
req = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)
