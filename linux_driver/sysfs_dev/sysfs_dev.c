/*
知识储备：
    Linux内核为我们提供了一组函数，可以用来在模块加载的时候自动在/dev目录下创建相应设备节点，并在卸载模块时删除该节点，当然前提条件是用户空间移植了udev。
内核中定义了struct class结构体，顾名思义，一个struct class结构体类型变量对应一个类，内核同时提供了class_create(…)函数，可以用它来创建一个类，这个类存
放于sysfs下面，一旦创建好了这个类，再调用device_create(…)函数来在/dev目录下创建相应的设备节点。这样，加载模块的时候，用户空间中的udev会自动响应
device_create(…)函数，去/sysfs下寻找对应的类从而创建设备节点。
1> device_create():
    struct device *device_create(struct class *class, struct device *parent,dev_t devt, void *drvdata, const char *fmt, ...)
    class   :指向指定所要创建的设备所从属的类的结构体指针
    parent  :这个设备的父设备,如果没有就指定为NULL
    devt    :设备号(该案例中使用MKDEV(major,0)来创建设备号)
    drvdata :要添加到设备中进行回调的数据
    fmt     :设备名称

2> register_chrdev():
    static inline int register_chrdev(unsigned int major, const char *name,const struct file_operations *fops)
    major   :主设备号，当用户设置为0时，内核会动态分配一个设备号。
    name    :设备名称
    fops    :文件系统的接口指针
    linux字符设备注册函数 register_chrdev详解当我们需要注册字符设备的时候，需要module_init()中调用register_chrdev()注册。

3> class_create():
    struct class *class_create(struct module *owner, const char *name)；
    owner   :指向“拥有”这个struct类的模块的指针
    name    :指向该类名称的字符串的指针。

4> sysfs_create_file():
    sysfs_create_file(struct kobject * kobj,const struct attribute * attr)
    创建节点的接口有4个
    sysfs_create_file      通过kobject创建sysfs的节点（其他3个接口最终都会调用此接口，参数attr中没有读写操作的接口，所以不使用此接口）
    device_create_file　　　为设备创建sys的节点。
    bus_create_file 　　　　为总线创建sys的节点。
    driver_create_file　　　为驱动创建sys的节点。
这4个接口中，linux驱动开发中，用户空间操作内核空间多数都是为了控制设备，那么我们选择实际使用最多的device_create_file接口来创建sysfs节点，
并通过创建出来的节点进行读写操作。

    int sysfs_create_group(struct kobject *kobj,const struct attribute_group *grp)  创建一组属性文件，grp.attr是一个struct attribute数组
    int sysfs_create_file(struct kobject * kobj,const struct attribute * attr)  创建一个属性文件

5> 使用DEVICE_ATTR，可以实现驱动在sys目录自动创建文件,我们只需要实现show和store函数即可.然后在应用层就能通过cat和echo命令来对sys创建出来的文件
进行读写驱动设备,实现交互.
#define DEVICE_ATTR(_name, _mode, _show, _store) \
    struct device_attribute dev_attr_##_name = __ATTR(_name, _mode, _show, _store)
函数功能：
    1、使用DEVICE_ATTR()定义一个名为my_device_test的属性文件，并且实现show(cat)和set(echo)方法供上层调用
    2、使用sysfs_create_file创建属性文件节点

6> int sprintf(char *str, const char *format, ...)
    str -- 这是指向一个字符数组的指针，该数组存储了 C 字符串。
    format -- 这是字符串，包含了要被写入到字符串 str 的文本。它可以包含嵌入的 format 标签，format 标签可被随后的附加参数中指定的值替换，
    并按需求进行格式化。format 标签属性是 %[flags][width][.precision][length]specifier，具体见https://www.runoob.com/cprogramming/c-function-sprintf.html

结果：
/sys/devices/virtual/mytest_class/mytest_device/my_device_test
echo xxx > my_device_test
cat my_device_test
*/
#include <linux/module.h>
#include <linux/init.h>
#include <linux/platform_device.h>
#include <linux/gpio.h>
#include <linux/delay.h>
#include <linux/regulator/consumer.h>
#include <sound/soc.h>
#include <sound/jack.h>


static  char mybuf[100]="123";
static ssize_t show_my_device(struct device *dev,struct device_attribute *attr, char *buf)        //cat命令时,将会调用该函数
{
    return sprintf(buf, "%s\n", mybuf);
}

static ssize_t set_my_device(struct device *dev,struct device_attribute *attr,const char *buf, size_t len)        //echo命令时,将会调用该函数
{
    sprintf(mybuf, "%s", buf);
    return len;
}
static DEVICE_ATTR(my_device_test, S_IWUSR|S_IRUSR, show_my_device, set_my_device);//定义一个名字为my_device_test的设备属性文件
/*
展开该宏如下:
struct device_attribute dev_attr_my_device_test ={  
    .attr = {.name = "my_device_test", .mode = S_IWUSR|S_IRUSR },     
    .show    = show_my_device,                 
    .store    = set_my_device,             
}
*/              
struct file_operations mytest_ops={
         .owner  = THIS_MODULE,
};

static int major;
static struct class *cls;
static int mytest_init(void)
{
         struct device *mydev;   
         major=register_chrdev(0,"mytest", &mytest_ops);    //注册一个字符设备mytest
         cls=class_create(THIS_MODULE, "mytest_class");     //创建一个
         mydev = device_create(cls, 0, MKDEV(major,0),NULL,"mytest_device");    //创建mytest_device设备    
    
    if(sysfs_create_file(&(mydev->kobj), &dev_attr_my_device_test.attr)){    //在mytest_device设备目录下创建一个my_device_test属性文件
            return -1;}
            
         return 0;
}

static void mytest_exit(void)
{
         device_destroy(cls, MKDEV(major,0));
         class_destroy(cls);
         unregister_chrdev(major, "mytest");
}

module_init(mytest_init);
module_exit(mytest_exit);
MODULE_LICENSE("GPL");