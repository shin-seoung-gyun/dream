# colors = ['red','green','blue']
# text = '-'.join(colors)

# # numList=[1,2,3,4,5,6,7,8,10]
# # text = '-'.join(numList)

# numList=[1,2,3,4,5,6,7,8,10]
# newList = [str(i) for i in numList]
# text = '-'.join(newList)
# print(text)


# import random
# numList1 = [random.randrange(100) for i in range(10)]
# numList2 = [random.randrange(100) for i in range(10)]
# print(numList1)
# print(numList2)

# ##두 리스트의 요소 중, 같은 인덱스의 값 모두 짝수일때만
# ## 두수의 합을 리스트로 나타내시오
# newList2 = [a+b for a,b in zip(numList1,numList2) if a%2==0 and b%2==0]
# print(newList2)

testMap = {"1":"하나","2":"둘","3":"셋"}
text = ''.join(testMap.keys())
print(text)
















