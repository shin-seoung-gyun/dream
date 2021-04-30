
# f = open("회원정보.txt",'r',encoding='utf-8')##꼭닫아야함
# text = f.read()#모든정보를 읽어서 문자열로 반환
# print(text)
# f.close()

# with open("회원정보.txt",'r',encoding='utf-8') as f :## 닫아줄필요 없음.
#     strList = f.readlines()#한줄씩 읽어와서, 리스트로 반환
#     for str in strList :
#         if '\n' in str:
#            str=str.replace('\n','')
#         print(str)

# ##회원 정보를 diction객체 저장
# resultList = []
# with open("회원정보.txt",'r',encoding='utf-8') as f :## 닫아줄필요 없음.
#     strList = f.readlines()#한줄씩 읽어와서, 리스트로 반환
#     keyList = strList[0].replace('\n','').split(',')
#     for val in strList[1:]:
#         if '\n' in val:
#             val = val.replace('\n','')
#         valList = val.split(',')
#         memberDic={}
#         for key, value in zip(keyList,valList):
#             memberDic[key] = value
#         resultList.append(memberDic)
# print(resultList)

# for member in resultList :
#     if "수원시" in member["Address"]:
#         print(member)


# for member in resultList:
#     if member["Address"].find("수원시") >=0:
#         print(member)

# import pickle##객체를 저장하는 

# with open("memberList.pickle",'wb') as f:
# #     pickle.dump(resultList,f)
# import pickle##객체를 저장하는 
# with open("memberList.pickle",'rb') as f:
#     resultList = pickle.load(f)

# for member in resultList :
#     print(member)


# ####파일쓰기

# with open("파일쓰기.txt",'w',encoding='utf-8') as f:##기존데이터 삭제하고 씀
#     for i in range(1,11):
#         data = f"{i}번째 줄입니다.\n"
#         f.write(data)


with open("파일쓰기.txt",'a',encoding='utf-8') as f:##기존데이터 이어서 씀
    for i in range(1,11):
        data = f"{i}번째 줄입니다.\n"
        f.write(data)









