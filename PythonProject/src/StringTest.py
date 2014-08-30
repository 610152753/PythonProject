StringStr = "a"

print (StringStr.capitalize())

StringB = "BBDB";

print (StringB.isalpha())

print (StringB.center(20))

print (StringB.count("B",0,len(StringB)));

#以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace

print (StringB.encode(encoding='UTF-16', errors='strict'))

#检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
print (StringB.endswith('B',0,len(StringB)-1))

#如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
print ("IsLower :") 
print (StringB.islower())
print (StringStr.islower())

#Merges (concatenates)以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

StringC = "back"
print ('b'.partition(StringC))
print ("\n".join(StringC))
    





