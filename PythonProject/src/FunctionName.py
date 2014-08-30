# Function definition is here
def printmsg(strparameter):
    print (strparameter);
    return;
# Now you can call printmsg function
printmsg("function Test");

def changList(listp):
    listp.append([1,2,3]);
    return

def printinfo(Name,Age):
    print ("Name:" ,Name);
    print ("Age:" , Age);
    return
#缺省参数
def printinfoA(Name,Age = 0):
    print ("Name:" ,Name);
    print ("Age:" , Age);
    return

listA = ["aa","ccc"]
#必备参数
changList(listA);
print (listA);
#命名参数
changList(listp = (listA));
printinfo(Name= "John",Age= 22);
#缺省参数
printinfoA(Name= "John");


#加了星号（*）的变量名会存放所有未命名的变量参数。选择不多传参数也可。如下实例：
# 可写函数说明
def printinfob( arg1, *vartuple ):
    "打印任何传入的参数"
    print ("out Print ");
    print (arg1);
    for var in vartuple:
        print (var);
    return;
 
# 调用printinfob 函数
printinfob( 10 );
printinfob( 70, 60, 50 );

def sumAll(arg1,arg2):
    #求和
    totala = arg1 + arg2;
    return totala;

sumAfter = sumAll(10, 30);
print ("Sum is :" ,sumAfter);



