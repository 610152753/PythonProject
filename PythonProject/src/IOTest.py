#coding=gbk
from os.path import os

from pip.backwardcompat import raw_input

straa = raw_input("Enter your input: ");
print ("Received input is : ", straa)

#input([prompt]) ������raw_input([prompt]) �����������Ի���������input��������������һ����Ч��Python���ʽ����������������
strbb = input("Enter your input: ");
print ("Received input is : ", strbb)
#�ļ�����
pathfile = "D:" + os.sep + "workspace\\git\\PythonProject\\PythonProject\\src\\foo.txt"
fo = open(pathfile, "a+")
print ("Name of the file: ", fo.name);

'''Write()����
Write()�����ɽ��κ��ַ���д��һ���򿪵��ļ�����Ҫ�ص�ע����ǣ�Python�ַ��������Ƕ��������ݣ������ǽ��������֡�
Write()���������ַ����Ľ�β����ӻ��з�('\n')��
'''
fo.write( "Python is a great language.\nYeah its great!!\n");

# �رմ򿪵��ļ�
fo.close()

fo = open(pathfile, "r+");

strRead = fo.read(30);
print (strRead)

strReada = fo.read();
print (strReada);

fo.close();
#remove()����ɾ���ļ�����Ҫ�ṩҪɾ�����ļ�����Ϊ������
os.remove("foo1.txt");
#rename()������Ҫ������������ǰ���ļ��������ļ�����
os.renames("foo.txt", "foo1.txt");

#����ʹ��osģ���mkdir()�����ڵ�ǰĿ¼�´����µ�Ŀ¼�ǡ�����Ҫ�ṩһ��������Ҫ������Ŀ¼���ƵĲ���
os.mkdir("test");
#������chdir()�������ı䵱ǰ��Ŀ¼��chdir()������Ҫ��һ��������������ɵ�ǰĿ¼��Ŀ¼���ơ�
os.chdir("test")
#getcwd()������ʾ��ǰ�Ĺ���Ŀ¼��
# ������ǰ��Ŀ¼
print  (os.getcwd());


#os.removedirs("")


