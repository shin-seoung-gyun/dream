import re

def getRobotData(section,dataName,fileText):
    p = re.compile(r"#\d+\s*"+section+r'\n([\w\W)]+?)(?:#|$)')
    m=p.search(fileText)
    if m :
        sectionData = m.group(1)
    else :
        sectionData = ""
    
    m = re.search(r'-\s*'+ dataName + r'=([\w\., ]*)', sectionData)
    if m :
        data = m.group(1)
    else :
        data = ""
    print(data)
    if "," in data:##결과값이 여러개인지 확인하기 위한 조건
        dataList = data.split(",")
        for i,val in enumerate(dataList):
            if val.isdigit() :##결과값이 숫자일때 .이 포함되면 실수로 아니면 정수로 변환
                if "." in val :
                    dataList[i] = float(val)
                else :
                    dataList[i] = int(val)
    else : ## 결과 값이 한개일때
        if data.isdigit() :
            if "." in data :##결과값이 숫자일때 .이 포함되면 실수로 아니면 정수로 변환
                dataList = [float(data)]
            else :
                dataList = [int(data)]
        else :
             dataList = [data]## 그대로 출력
    return dataList


with open('ROBOT.CON','r',encoding='utf-8') as f:
    fileText = f.read()

section = "Control environment setting"
dataName = "Program end signal output time[sec]"

data = getRobotData(section,dataName,fileText)
print(data)
