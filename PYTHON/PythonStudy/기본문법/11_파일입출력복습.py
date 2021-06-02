# regionDic = {}#키값이 구이름 value는 리스트[동네1,동네2]
# with open('C:/Users/USER/Desktop/수원행정구역.csv','r',encoding='utf8') as f :
#     strList = f.readlines()
#     print(strList)
#     keyList = [i.replace(' ','').replace('\n','') for i in strList[0].split(',')]
#     print(keyList)
#     for key in keyList :
#         regionDic[key] =[]
#     for dongStr in strList[1:]:
#         valueList = [i.replace(' ','').replace('\n','').replace('?','') for i in dongStr.split(',')]
#         print(valueList)
#         for i, j in zip(keyList,valueList):
#             regionDic[i] +=[j]
    

    
# import os
# path = 'C:/Users/USER/Desktop/수원'
# if not os.path.exists(path) :
#     os.mkdir(path)

# # for i,j in regionDic.items() :
# #     if j == '':
# #         continue
# #     path = f'C:/Users/USER/Desktop/수원/{i}/{j}'
# #     if not os.path.exists(path) :
# #         os.mkdir(path)
        
# for gu,dongList in regionDic.items():
#     guPath = path +"/"+gu
#     if not os.path.exists(guPath):
#         os.mkdir(guPath)
#     for dong in dongList :
#         dongPath = guPath +"/"+dong
#         if not os.path.exists(dongPath):
#             os.mkdir(dongPath)
    
# import csv
# with open('C:/Users/USER/Desktop/수원행정구역.csv','r',encoding='utf8') as f :
#     csv_data = csv.reader(f)

#     for row in csv_data :
#         print(row)

# with open('C:/Users/USER/Desktop/수원행정구역2.csv','w',encoding='utf8') as f :
#     writer = csv.writer(f,delimiter ='\t',quotechar="'",quoting=csv.QUOTE_ALL)
#     #delimiter 구분자'\t'
#     #quotechar 데이터를 묶는 문자
#     #quoting 묶는 범위

#     writer.writerow(regionDic.keys())
#     dongList1 = regionDic['장안구']
#     dongList2 = regionDic['권선구']
#     dongList3 = regionDic['팔달구']
#     dongList4 = regionDic['영통구']

#     for data in zip(dongList1,dongList2,dongList3,dongList4):
#         writer.writerow(data)
        
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
print(config.sections())

for key in config['SectionOne']:
    print(key)

print(config['SectionOne']['status'])
print(config['SectionOne']['name'])
print(config['SectionOne']['age'])

config['SectionOne']['age'] = '32'
config['SectionOne']['name'] = '신승균'

with open('config.ini','w',encoding='utf8') as f:
    config.write(f)













