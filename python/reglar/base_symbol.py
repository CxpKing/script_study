'''reglar

正则表达式：
常用的symbol
1> . 表示所有字符包括它本身
2> + 表示前面一个字符或子表达式可以重复一次或多次,比如说"ab+"能匹配"abbbbb",但不能匹配"a"
3> * 表示前面一个字符或子表达式可以重复0次或多次，比如说"ab+"能匹配"a"以及"abbb"
4> ? 表示匹配一个字符或子表达式可以重复0到1次，
4> \ 转义符号，比如像让匹配规则自匹配一星号*，"\*"
5> [] 表示中括号内的字符任意一个
6> [^...] 表示除了其后面的字符，其他都匹配。
7> () 表示一个子表达式的起始位置如：(sd)* 同时也用来表示需要提取的字符内容
''' 
import re
'''方法一

[description]
'''
def generalMatch(strs,partern):
	res = (re.compile(partern)).findall(strs)
	print(res)


def match(strs,p):
	partern = re.compile(p)
	res = re.search(partern,strs)
	print(res)


generalMatch("http://sdsd","http*://")

s = r"whar? sdsd sd?"
p = r"((sd)+)"
generalMatch(s,p)


html = r'<form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=ç\x99¾åº¦ä¸\x80ä¸\x8b class="bg s_btn"></span> </form><form >123</form>'
p1 = r'<form .*?>(.*?)</form>'
p2 = r'<input .*?>'
#generalMatch(html,p1)
#generalMatch(html,p2)
res1 = re.findall(r"[0-9]+","adg6sd")
print(res1)
