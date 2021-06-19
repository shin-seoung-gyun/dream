import re

def getRobotData(section,dataName,fileText):
    p = re.compile(r"#\d+\s*"+section+r'\n([\w\W]+?)(?:#|$)')#최소검색
    m=p.search(fileText)
    if m :
        sectionData = m.group(1)
    else :
        sectionData = ""
    
    m = re.search(r'-\s*'+ dataName + r'=([\w\.,]*)', sectionData)
    if m :
        data = m.group(1)
    else :
        data = ""
    
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
    
def setRobotData(section, dataName, fileText, reData) :
    p = re.compile(r"#\d+\s*"+section+r'\n([\w\W]+?)(?:#|$)')#최소검색
    m=p.search(fileText)
    if m :
        sectionData = m.group(1)
        
    else :
        return -1

    reSection = re.sub(r'(-\s*'+ dataName + r'=)[\w\.\,]*', "\g<1>"+reData, sectionData)
    # print(reSection)
    p = re.compile(r"(#\d+\s*"+section+r'\n)([\w\W]+?)(?:#|$)')#최소검색
    newFileText = p.sub("\g<1>"+reSection,fileText)
    return newFileText
    



with open('ROBOT.CON','r',encoding='utf-8') as f:
    fileText = f.read()

section = "Condition set"
dataName = "Playback mode"

# data = getRobotData(section,dataName,fileText)
# print(data)
newFileText = setRobotData(section,dataName,fileText,"reData")
print(newFileText)

with open('ROBOT.CON','w',encoding='utf-8') as f:
    f.write(newFileText)

