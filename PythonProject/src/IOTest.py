#coding=gbk
from os.path import os

from pip.backwardcompat import raw_input

straa = raw_input("Enter your input: ");
print ("Received input is : ", straa)

#input([prompt]) 函数和raw_input([prompt]) 函数基本可以互换，但是input会假设你的输入是一个有效的Python表达式，并返回运算结果。
strbb = input("Enter your input: ");
print ("Received input is : ", strbb)
#文件操作
pathfile = "D:" + os.sep + "workspace\\git\\PythonProject\\PythonProject\\src\\foo.txt"
fo = open(pathfile, "a+")
print ("Name of the file: ", fo.name);

'''Write()方法
Write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
Write()方法不在字符串的结尾不添加换行符('\n')：
'''
fo.write( "Python is a great language.\nYeah its great!!\n");

# 关闭打开的文件
fo.close()

fo = open(pathfile, "r+");

strRead = fo.read(30);
print (strRead)

strReada = fo.read();
print (strReada);

fo.close();
#remove()方法删除文件，需要提供要删除的文件名作为参数。
os.remove("foo1.txt");
#rename()方法需要两个参数，当前的文件名和新文件名。
os.renames("foo.txt", "foo1.txt");

#可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数
os.mkdir("test");
#可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
os.chdir("test")
#getcwd()方法显示当前的工作目录。
# 给出当前的目录
print  (os.getcwd());


#os.removedirs("")


