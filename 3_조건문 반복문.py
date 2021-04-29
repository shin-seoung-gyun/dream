# print("Tell me your age?")
# myage = int(input())
# if myage <30:
#     print("Wellcom to the club.")
# else:
#     print("oh! No. You are not accepted.")


# pocket = ["키","지갑","잔돈"]
# item = input("소지품을 입력하세요.")

# if item in pocket:
#     print(item,"이 포켓안에 있습니다.")
# else:
#     print(item,"이 포켓안에 없습니다.")


# score = int(input("Enter your score: "))

# if score >=90: grade ='A'
# elif score >=80: grade = 'B'
# elif score >=70: grade = 'C'
# elif score >=60: grade = 'D'
# else: grade = 'F'

# print(grade)

# for _ in [1,2,3,4,5]:
#     print("hello")

# for a in range(1,10,2):
#     print("hello",a)

# for ch in "hello":
#     print(ch)

# for item in ['americano','latte','coffe']:
#     for ch in item:
#         print(ch, end = ',')
#     print("-----------------------")




# i = 1
# while i < 10:
#     print(i)
#     i+=1


# num = int(input("구구단 몇단을 출력할까?"))/
# for a in range(1,10):
#     for b in range(1,10):
#         print(a,"*",b,"=",a*b)
#     print("********************")


# num = int(input("n을입력하시오."))
# result = 0
# for i in range(1,num+1):
#     if i%7==0:
#         result += i

# print(result)

##높이가 n인 삼각형
# num = int(input("n을입력하시오."))
# for i in range (1,num+1):
#     print("*"*i)


##높이가 n인 오른쪽 정렬 삼각형

# num = int(input("n을입력하시오."))
# cnt = 1
# for i in range (num+1,0,-1):
#     print(" "*(i-1),"*"*cnt)
#     cnt += 1

##높이가 n인 이등변 삼각형

# num = int(input("n을입력하시오."))
# cnt = 1
# for i in range (num+1,0,-1):
#     print(" "*(i-1),"*"*cnt)
#     cnt += 2

#다이아 몬드 형태
# num = int(input("n을입력하시오."))
# cnt = 1
# for i in range (num,0,-1):
#     print(" "*(i-1),"*"*cnt)
#     cnt += 2
# cnt -= 4  
# for i in range (2,num+1):
#     print(" "*(i-1),"*"*cnt)
#     cnt -= 2


##임의의 숫자가 주어졌을때 소수인지 아닌지 판별하기
# num = int(input("n을입력하시오."))

# for i in range(2,num):
#     if num%i==0:
#         print("정수")
#         break
#     if i == num-1 :
#         print("소수")

##369 출력

# num = int(input("n을입력하시오."))
# for i in range(1,num+1):
#     a = str(i)
#     for j in range(0,len(a)):
#         if  '3'in a[j] or'6'in a[j] or'9'in a[j] :
#             print("짝",end='')
#         else :
#             print(a[j],end='')
#         if j==len(a)-1:
#             if i != num:
#                 print(",",end='')


##달력출력
#         
# month = [31,28,31,20,31,30,31,31,30,31,30,31]
# for i in range(0,len(month)):
#     print(i+1,"월 - ",end='')
#     for j in range(1,month[i]+1):
#         if j != month[i]:
#             print(j,"일",end=', ')
#         elif j == month[i]:
#             print(j,"일",end='')
#     print()    
   
##출력해보기 너비와 높이 받아서 출력
# width = int(input("너비를 입력하세요"))
# height = int(input("높이를 입력하세요"))
# maxNum = width*height
# for i in range(1,maxNum+1):
#     print(i," ",end='')
#     if i%width==0:
#         print()
##패킹 언패킹 사용.
kor_score = [49,80,20,100,80]
math_score = [43,60,85,30,90]
eng_score = [49,82,48,50,100]
midterm_score = [kor_score,math_score,eng_score]

student_score = [0,0,0,0,0]
i=0
for subject in midterm_score:
    for score in subject:
        student_score[i]+=score
        i += 1
    i=0

a,b,c,d,e = student_score
student_average = [a/3,b/3,c/3,d/3,e/3]
print(student_average)









    

    









