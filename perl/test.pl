#!/usr/bin/perl
$a = 1;
$b = 2;
$c = $a+$b;
print("a+b=",$c,"\n");
@s = (1,2,3);
#获取数组的长度，将数组赋值给标量，此时标量的值就是数组的长度
$len = @s;
print($len,"\n");
for($i=0;$i<@s.length;$i++){
	print(@s[$i],"\n");
}

%h = ('a','value1','b','value2');
print($h{'a'},"\n");
print($h{'b'},"\n");

#三目运算符 ？:
$name = "Python";
$cap = 80;
$bool = ($cap >= 60)?"cool":"not cool";
print("$name is $bool","\n");
#比较运算符
# == != > < >= <=  <=>
#<=>这个运算符很有意思，如果左边的数大于右边，返回1，左小于右返回-1，左右相等返回0
$x = 10;
$y = 20;
print($x <=> $y);
#比较运算符也可以用以下符号表示
#eq ne gt lt ge le cmp
# **= 平方
#q{} qq{} qx{}
print(qq{Hello world});

sub add{
	
}