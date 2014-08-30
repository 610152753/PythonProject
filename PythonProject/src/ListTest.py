import calendar
import time
import FunctionName
from FunctionName import printinfo


listB = ["a", "a", "c", "d"];
print (listB)

seqA = ("a","1111","c","d");

listA = list(seqA);
print (seqA)
print (listA)
print (listA + [879])
print (len(listA))

print (listA.reverse())
print (listA)

print ("Max:" + max(listB))
print ("Min:" + min(listB))

for x in listA: print (x)

ticks = time.localtime()
print ("Number of ticks since 12:00am, January 1, 1970:",(ticks))

cal = calendar.month(2008,2)
print ("Here is the calendar:");
print (cal);

print (time.clock())

FunctionName.changList(listA);
print (listA);

printinfo(Name= "John",Age= 22);
