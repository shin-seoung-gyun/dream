# colors = ['red','blue','green','yellow']
# result =''
# for val in colors :
#     result += val
# print(result)


##join함수
# result2 = ''.join(colors)
# print(result2)

# result3 = ','.join(colors)
# print(result3)

# result4 = '--'.join(colors)
# print(result4)

##split함수
# items = 'zero one two three'
# itemList = items.split()
# print(itemList)

# items = 'zero,one,two,three'
# itemList = items.split(',')
# print(itemList)

# items = 'zero--one--two--three'
# itemList = items.split('--')
# print(itemList)


##K1KA5CB7->ABCKK13

# strA = 'kkacb'
# stringlist = []
# intlist = []
# for i in range(len(strA)):
#     if strA[i].isalpha() == True:
#         stringlist.append(strA[i])
#     else:
#         intlist.append(strA[i])

# stringlist.sort()
# num =0
# for k in intlist:
#     num += int(k)
# stringlist.append(str(num))
# result = ''.join(stringlist)
# print(result)

##리스트 컴피리헨션

# resultList = [i for i in range(10)]
# resultList

# resultList = [i*2 for i in range(10)]
# resultList

# resultList = [i for i in range(10) if i%2==0]
# resultList

# resultList = [i if i%2==0 else -1 for i in range(10) ]
# resultList
# ##다른언어에 없는 문법

# def getResisTotal(numList) :
#     resultList = [1/x for x in numList]
#     return 1/sum(resultList)

# word1='hello'
# word2='world'
# result=[i+j for i in word1 for j in word2 if i==j]
# result


# word1='hello'
# word2='world'
# result=[i+j if i==j else 'xx' for i in word1 for j in word2 ]
# result

# words = "The quick brown fox jumps over the lazy dog"
# wordList = words.split()
# stuff = [[w.upper(),w.lower(),len(w)] for w in wordList ]
# stuff

# for upStr,lowStr,lenStr in stuff:
#     print(upStr,lowStr,lenStr)


# numList1 = [1,2,3,4,5,6,7,8,9]
# numList2 = [10,20,30,40,50,60,70,80,90]
# numList3 = [10,20,30,40,50,60,70,80,90]
# result = [i+j+k for i,j,k in zip(numList1,numList2,numList3)]
# result

# for i, j in zip(numList1,numList2):
#     print(i,j)

# i=0
# numList1 = [1,2,3,4,5,6,7,8,9]
# for num in numList :
#     print(i,num)
#     i+=1

# for i,num in enumerate(numList1) :#인덱스를 같이 가져옴
#     print(i,num)


# aList = ['a1','a2','a3']
# bList = ['b1','b2','b3']

# for i,(a,b) in enumerate(zip(aList,bList)):
#     print(i,a,b)


# korList = [90,40,30]
# engList = [100,70,80]
# mathList = [30,60,90]

# for i,stScore in enumerate(zip(korList,engList,mathList)) :
#     print(f"{i}번째 학생의 평균값 {sum(stScore)/3:.3}")


###########lambda식

# f=lambda x,y : x+y

# print(f(1,4))
# print((lambda x,y : x+y)(2,5))

# f= lambda x : x**2
# print(f(5))


# numList = [1,2,3,4,5]
# numList1 = [6,7,8,9,10]
# numList2 = [1,2,3,4,5]
# f = lambda x:x**2
# newList = list(map(f,numList))
# print(newList)

# newList = [x**2 for x in numList]
# print(newList)

# for val in map(lambda x:x**2,numList):
#     print(val)

# newList = list(map(lambda x,y:x+y, numList1,numList2))##map은 입력값을 바꿔주는 함수
# print(newList)

fruitList = ['사과','딸기','배']
fruitNumList = [10,8,20]

#->['사과-10','딸기-8','배-20']
##map을 이용한 방법
newList = list(map(lambda x,y:x+'-'+str(y) if y>=10 else '',fruitList,fruitNumList))
print(newList)


newList = [x+'-'+str(y)  for x,y in zip(fruitList,fruitNumList) if y>=10]
print(newList)


###filter
numList = [1,2,3,4,5,6,7,8,9,10]
newList = list(filter(lambda x:x%2==0,numList))##filter함수는 값이 True False로 나와야함.
print(newList)

strList = ["hello","hi","welcome","say"]
newList = list(filter(lambda x:len(x)>=5,strList))
print(newList)



##reduce

from functools import reduce
result = reduce(lambda x,y:x+y,numList)
print(result)

result = reduce(lambda x,y:x*y,numList)
print(result)














