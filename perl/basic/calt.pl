=cut字符串的加减法
1、从字符串的第1个元素开始遇到非数字直接去掉非数字内容


使用内建警告来帮助调试程序use warnings
=cut

use warnings;

$num1 = "12sdsd";
$num2 = "1sdasd";
$ret = $num1 + $num2;
printf("$ret\n");  #结果为 13

print "hello"."world";
