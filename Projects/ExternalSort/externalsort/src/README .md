#文件生成部分


----------
##**编译**
*开发环境: Windows 10 + Eclipse*
*Java 1.8*
在Windows Power Shell下，切换目录到java文件所在位置，运行javac filesort_testgen.java生成class文件
![Compile](http://img.blog.csdn.net/20161107194304557)
##**运行**
在class文件目录下运行java filesort_testgen FILE_COUNT LINES_PER_FILE PREFIX
其中

 - filesort_testgen为可执行文件名
 - FILE_COUNT为需要生成的待排序文件的个数
 - LINES_PER_FILE：每个待排序文件的行数
 - PREFIX为生成文件的前缀
执行结果:
![执行结果](http://img.blog.csdn.net/20161107194553834)
在这里生成了6个文件，大小不一，均超过1G。
![文件](http://img.blog.csdn.net/20161107194926058)


----------
#排序部分


----------
思路：先把几个大文件合并成一个文件，对其进行外排序输出。以时间换空间。

##**编译**

> 依赖org.apache.commons.io.jar包

打开powershell或者cmd，切换到filesort.java所在目录，键入

```
javac -cp [path of jar] filesort.java
```
##**运行**
生成class文件，在当前目录键入

```
这里写代码片
```
在PowerShell下编译成功后一直运行有错误。前前后后折腾了快两个小时，最后在cmd下运行成功了。 PowerShell会把分号识别为语句的结束。。。。
运行结果
![结果](http://img.blog.csdn.net/20161109014953398)

5个文件
