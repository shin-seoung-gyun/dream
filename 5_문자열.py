 a="hello"
 print(a[0])
 print(a[-1])
 print(a[1:])
 print(a[::-1])
 print(a[1::2])

 b="world"
 c=a+" "+b
 print(c)
 print(c*2)

for ch in c :
    print(ch)

print(len(a))
print(a.upper())
print(a.lower())
print(c.title())
print(c.capitalize())
print(c.count("l"))
print(c.count("el"))
print(c.find("world"))
print(c.rfind("world"))
print(c.startswith("h"))
print(c.endswith("d"))


a="10,30,40,50"
aList = a.split(",")
print(aList)

a = "4345"
b="31.4"
print(a.isdigit())
print(b.isalpha())

c="           hello"
print(c.lstrip())
print(c.rstrip())
print(c.strip())

num = 10
floatNum = 3.14
str1="hello"
print("%d,%10.2f ,%s"%(num,floatNum,str1))
print("{},{} ,{}".format(num,floatNum,str1))
print("{0:>10},{1:<10.2} ,{2:>10}".format(num,floatNum,str1))
print("{2},{1} ,{0}".format(num,floatNum,str1))
print("{0},{0} ,{1}".format(num,floatNum,str1))
print(f"{num},{floatNum} ,{str1}")


maxNum=50
for i in range(1,maxNum+1) :
    numStr = str(i)
    jjackCnt = numStr.count("3")+numStr.count("6")+numStr.count("9")
    if(jjackCnt>0):
        print("짝"*jjackCnt,end=",")
    else :
        print(numStr,end=",")

str1 = "1231231231321321321'3121'3321"
print(str1)
str2 = '213123"123"132131312313'
print(str2)















