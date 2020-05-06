@num = (1..5);
@student = qw(name age score);

#pop 取出数组最后一个元素，同时返回该元素 -------------右减
@array1 = (5..9);
$test1 = pop(@array1);  #此时@array = (5,6,7,8) $test1 = 9
$test2 = pop(@array1);  #@array = (5,6,7) $test2 =8

#push 添加一个元素（或者一串元素到数组的尾端）---------右加
@array2 = (5,6);
push(@array2,8);     #@array2 = (5,6,8)
push(@array2,1..5);  #@array2 = (5,6,8,1,2,3,4,5)

#shift 取出数组最左边的元素，同时返回该元素值----------左减
@array3 = (5..9);
$test1 = shift(@array3) ;#@array3 = (6,7,8,9) $test1 = 5
$test2 = shift(@arrat3) ;#@array3 = (7,8,9) $test1 = 6

#unshift 添加一个元素（或者一串元素到数组的最左端）
@array4 = (5,6);
unshift(@array4,4); #@array4 = (4,5,6)
unshift(@array4,1..3); #@array4 = (1,2,3,4,5,6)

#  $#<数组名> 获取数组最后一个元素的索引
@array5 = (1..100);
$end = $#array5;
printf("$end");

#perl 中的地址引用
$a = 1;
@b = (1..4);
$c = \$a;        
printf("$c");
