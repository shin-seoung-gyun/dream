##예외처리

# for i in range(10):
#     try:
#         result =10/i
#     except ZeroDivisionError: #예외가 발생하는 경우
#         print("not divide by 0")
#     else :
#         print(result)       #예외가 발생하지 않는 경우
#     finally :##무조건 끝나면 실행되는 경우
#         print("종료되었습니다.")

# #예외를 발생시키는 방법 raise
# while True :
#     value = input("정수값을 입력하세요")
#     for digit in value :
#         if digit not in "0123456789":
#             raise ValueError("숫자값을 입력하지 않았습니다.")
#     print("정수로 변환된 숫자 - ",int(value))

##예외를 조건에 따라 발생시킬지 말지 선택

def get_binary_number(decimal_number) :
    assert isinstance(decimal_number,int)#타입체크 함수
    return bin(decimal_number)#10진수를 2진수로 변환하는 함수

print(get_binary_number(10))

print(get_binary_number("10"))








