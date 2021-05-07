

#회원관리 딕셔너리 활용
#이름으로 회원정보 불러오기

memberDic = {}
memberDic["python"]=["1234","김동현","010-1234-1234","2020-12-23"]
memberDic["apple"]=["abcd","이현수","010-4445-1123","2020-12-21"]
memberDic["java"]=["1q2w3e","강동원","010-5556-3455","2020-12-10"]
memberDic["android"]=["5555","전지현","010-1114-1555","2020-12-09"]
memberDic["Clang"]=["932j","강동원","010-4498-7777","2020-12-01"]

findName = "강동원"

for key, val in memberDic.items():
    if val[1]==findName :
        print(f"id :{key}, pw :{val[0]}, name :{val[1]}, phone :{val[2]}, signDate :{val[3]}")
    












