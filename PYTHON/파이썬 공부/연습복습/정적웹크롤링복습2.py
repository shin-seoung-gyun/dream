import pandas as pd

##판다스라이브러리 데이터를 다루는 라이브러리
#데이터들을 데이터 프레임으로 만들어서 다룬다 칼럼(열)과 인덱스(행)로 만들어지고 데이터 베이스와 유사한 형태. 

##ex)
# finanDF = pd.DataFrame(financeList, columns=financeList[0].keys())
#데이터프레임을 csv형식으로 저장
# finanDF.to_csv("./웹크롤링/정적웹크롤링/코스피상장회사.csv",encoding='utf8',mode='w',index=False) 
#데이터 끼리 병합도 가능하고 불러오기 저장하기 등등 apply로 공급해서 람다로 다른 칼럼을 만들수도 있음 여러기능 가지고있음








