
#stack
word = input("Input a word")
world_list = list(word)
print(world_list)

result =[]
for _ in range(len(world_list)):
    result.append(world_list.pop())

print(result)
print(word[::-1])
#queue

aList = [1,2,3,4,5]
aList.append(10)
aList.append(20)
print(aList.pop(0))
print(aList)
print(aList.pop(0))
print(aList)
#set
s = set([1,2,3,1,1,1,1])
print(s)
lists = list(s)
print(lists)

s.remove(3)
s.clear()

s.update([1,2,4,5,6,7,4,5,6,4,5])


fruitSet1 ={'사과','딸기','포도'}
fruitSet2 ={'배','딸기','귤'}

#합집합
fruitUnion = fruitSet1.union(fruitSet2)
print(fruitUnion)
fruitUnion2 = fruitSet1|fruitSet2
print(fruitUnion2)

#교집합
fruitInter = fruitSet1.intersection(fruitSet2)
print(fruitInter)
fruitInter2 = fruitSet1&fruitSet2
print(fruitInter2)
#차집합
fruitDiffer = fruitSet1.difference(fruitSet2)
print(fruitDiffer)
fruitDiffer2 = fruitSet1-fruitSet2
print(fruitDiffer2)
fruitDiffer3 = fruitSet2-fruitSet1
print(fruitDiffer3)


#딕셔너리

studentDic = {20140012:"홍길동",20140013:"임꺽정"}
print(studentDic[20140012])
#값수정
studentDic[20140012] = "김하나"
print(studentDic[20140012])
# 값추가
studentDic[20140014] = "김새롬"
print(studentDic[20140014])

print(studentDic.keys())
print(studentDic.values())
print(studentDic.items())

for key in studentDic.keys():
    print(f"key:{key}, Value:{studentDic[key]}")


for key, val in studentDic.items():
    print(f"key:{key}, Value:{val}")


for val in studentDic.values():
    print(f"Value:{val}")


print(20140013 in studentDic.keys())
print('김새롬' in studentDic.values())

#카운터

from collections import Counter #라이브러리 불러올때 쓰는 처리

text = list("hello World")
c = Counter(text)
print(c)

fruitList = ["사과","사과","딸기","딸기","포도"]
c = Counter(fruitList)
print(c)
print(c["사과"])
print(c["딸기"])


fruitList = ["사과","사과","딸기","딸기","포도","포도","포도"]
fruitSet = set(fruitList)#사과 딸기 포도
fruitSet
fruitDic={}
for fruit in fruitSet
    fruitDic[fruit] = fruitList.count(fruit)
fruitDic

from collections import Counter

fruitCnt  = Counter(fruitList)
print(fruitCnt)


# 정수 n이 입력되었을때 00시00분00초 ~ n시 59분 59초 까지 시간중 하나라도 3이 포함되는 경우의 수를 구하는 처리 카운트

num = int(input("시간을 입력하세요."))


cnt = 0
for hour in range(num):
    for min in range(60):
        for sec in range(60):
            if '3' in str(hour)+str(min)+str(sec):
                cnt += 1
print(cnt)

#파이선 삼항연산자
# num = (a>=10)? 10:0##자바 삼항연산자
a = 15
num = 10 if a>= 10 else 0
num
















