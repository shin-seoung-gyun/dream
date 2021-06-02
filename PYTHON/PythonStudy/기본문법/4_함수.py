def calculate_rectangle_area(x,y):
    return x*y

rectangel_x = 10
rectangel_y = 20

print("사각형 x의 길이 :",rectangel_x)
print("사각형 y의 길이 :",rectangel_y)


print("사각형의 넓이:",calculate_rectangle_area(rectangel_x,rectangel_y))
#함수만드는 키워드 def

def spam(eggs):
    eggs.append(1)

    eggs=[2,3]
ham = [0]
spam(ham)
print(ham)

def f():
    global s
    s = "i love london"
    print(s)

s = "i love paris"
f()
print(s)

(1) 키워드 인수 - 가장 기본적인형태
def printSomething(name,age):
    print(f"Hello {name}, age is {age}")

printSomething("홍길동",30)
printSomething(name ="홍길동",age=30)
printSomething(age=30,name ="홍길동")

#(2) default인수
def printSomething2(name,age=20):
    print(f"Hello {name}, age is {age}")
printSomething2("홍길동")
printSomething2("홍길동",30)

(3)가변인수
def sumNumbers(a,b,*args):
    total =0
    for num in args :
        total += num
    return a+b+total

print(sumNumbers(3,4))
print(sumNumbers(3,4,5,6,7,7))
# print(sumNumbers(3,4,[1,2,3,4]))


가변인수2

def getAtgs(*args) :
    x,y,*z = args
    return x,y,z

print(getAtgs(3,4,10,20,30,50))
print(getAtgs(3,4))
print(getAtgs(3))


키워드가변인수

def kwargsTest(**kwargs):
    print(kwargs)
    print("First value:{first}".format(**kwargs))
    print("Second value:{second}".format(**kwargs))
    print("Thrid value:{third}".format(**kwargs))

kwargsTest(first=3,second=4,third=5)
kwargsTest(3,4,5)







#반지름을입력받고 원의 넓이를 출력하는 함수 r*r*3.14
def circleArea (r):
    return r*r*3.14

R = int(input("반지름을 입력하세요."))

result = circleArea(R)
print(result)

#반지름과 높이를 입력받고 실린더의 부피를 출력하는 함수 r*r*3.14*h
def cilinder(r,h):
    return circleArea(r)*h


R = int(input("반지름을 입력하세요."))
height = int(input("높이를 입력하세요."))

result = cilinder(R,height)
print(result)
#list를 입력받고 리스트의 모든 요소의 합을 출력하는 함수
def sumList(ulist):
    result = 0
    for i in ulist:
        result += i
    return result

userList = [31,2,5,4,6]

result = sumList(userList)
print(result)

#list변수를 입력받고 리스트의 모든 요소의 평균값을 출력하는 함수
def avgList(ulist):
    result = 0
    for i in ulist:
        result += i
    return result/len(ulist)

userList = [31,2,5,4,6]
result = avgList(userList)
print(result)

#list변수를 입력받고 리스트의 모든 요소의 표준편차값을 출력하는 함수

def stdAvgList(ulist):
    avg = avgList(ulist)
    stdAvg[]
    for i in ulist:
        stdAvg.append((i-avg)**2)
    return avgList(stdAvg)**(0.5)

userList = [31,2,5,4,6]
result = stdAvgList(userList)
print(result)


def getTotalResis(numList, serial=True) :
    if serial :
        return sum(numList)
    else :
        total = 0
        for i in numList :
            total += 1/i
        return 1/total

getTotalResis([1,2,3,4])
getTotalResis([1,2,3,4],True)
getTotalResis([1,2,3,4],False)





