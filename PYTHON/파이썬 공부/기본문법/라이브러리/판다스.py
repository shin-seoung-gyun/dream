##pandas라이브러리
import pandas as pd
import numpy as np
## 시리즈
s = pd.Series([1,3,5,np.nan,6,8])#시리즈를 만드는 법
print(s)
s = pd.Series([1,3,5,np.nan,6,8], index=['하나','둘','셋','넷','다섯','여섯'])
print(s)

data1 = [10,20,30,40,50]
data2 = ['1반','2반','3반','4반','5반']
sr1 = pd.Series(data1)
sr2 = pd.Series(data2)
sr3 = pd.Series(data1,index=data2)
print(sr1)
print(sr2)
print(sr3)

#값얻기
print(sr1[0])
print(sr2[3])
print(sr3['1반'])
#인덱스 리스트 얻기
print(sr3.index)
#값 리스트 얻기
print(sr3.values)

print(sr1+sr1)
print(sr1*sr1)
print(sr1*4)

##데이터 프레임
dates = pd.date_range('20130101',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))#데이터 프레임 만들기
print(df)

df2 = pd.DataFrame({'A':1.,'B':pd.Timestamp('20130102'),'C':pd.Series(1, index=list(range(4)), dtype='float32'), \
    'D':np.array([3]*4,dtype='int32'),'E': pd.Categorical(['test','train','test','train']),'F': 'foo'})
print(df2)

##데이터 프레임 심화
#데이터 프레임의 열별 타입
print(df2.dtypes)
#값 가져오기
print(df2.head())#최대 5개
print(df2.head(3))
print(df2.tail(3))#뒤에서부터

print(df2.index)# 인덱스 값
print(df.index)# 인덱스 값

print(df2.columns)
print(df2.values)

#value들의 요약 통계
print(df.describe())

#데이터를 전치 (행<->열) 바꾼다
print(df.T)

#데이터 정렬
#칼럼 기준으로 내림차순
print(df.sort_index(axis=1, ascending=False))
#인덱스 기준으로 내림차순
print(df.sort_index(axis=0, ascending=False))
#값 별로 정렬 - B열 값 기준 내림차순
print(df.sort_values(by='B'))
#값 별로 정렬 - B열 값 기준 오름차순
print(df.sort_values(by='B',ascending=True))

#값 얻기
#시리즈 데이터 구조로 인덱스와 A열값이 출력
print(df['A'])

#인덱스 기준으로 0~2까지 데이터를 가져온다.
print(df[0:3])#뒤의 인자 미포함

print(df['20130102':'20130104']) #뒤의 인자 포함 #인덱스의 이름으로 가져올때

#라벨을 통해서 값 가져오기
print(df.loc['20130102'])#인덱스 이름
print(df.iloc[1])#인덱스 번호
#범위
print(df.loc[:,['A','B']])#모든 인덱스 열 두개
print(df.loc['20130102':'20130104',['A','B']])#인덱스 두개 열 두개
print(df.loc['20130102',['A','B']])#해당하는 인덱스 열 두개
print(df.loc['20130102','A'])#해당하는 인덱스와 열 하나

#iloc 범위 위의 것과 같은 처리
print(df.iloc[:,0:2])
print(df.iloc[1:4,0:2])
print(df.iloc[1,0:2])#해당하는 인덱스 열 두개
print(df.iloc[1,0])#해당하는 인덱스와 열 하나
print(df.iloc[[0,1,2,3],[0,2]])

#데이터 검색 - boolean indexing
print(df[df.A>0])
print(df[df >0])#0이상의 값만 표시 되고, 0이하의 값은 Nan

df2 = df#주소값을 복사
df2 = df.copy()#값 복사
df2['E']=['one','one','two','three','four','three']

#필터링 함수 isin
print(df2[df2['E'].isin(['two','four'])])

s1= pd.Series([1,2,3,4,5,6],index=pd.date_range('20130102',periods=6))
print(s1)
df['F']=s1
print(df)

#값 수정
df.loc['20130102','A']=3
print(df.loc['20130102','A'])
df.iloc[1,0]=4
print(df.loc['20130102','A'])
df.at['20130102','A']=5
print(df.loc['20130102','A'])

#데이터 행 길이 = 인덱스 개수
print(len(df))
df.loc[:,'D'] = np.array([5]*len(df))
print(df)

df2 = df.copy()
df2[df2>0]=-df2
print(df2)

#결측치 데이터 처리
df1 = df.reindex(index=dates[0:4], columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
print(df1)

#결측치가 있는 행 지우기

print(df1.dropna(how='any'))
print(df1.fillna(value=5))

print(pd.isna(df1))
print(pd.isna(df1).sum())#각열들의 결측치 개수

#통계
#각 열별 평균값
print(df.mean())

#인덱스 기준으로 평균값
print(df.mean(1))

print(df.apply(lambda x:x.max()-x.min()))

s = pd.Series(["A","B","c","Abac","13"])
print(s.str.lower())
print(s.str.count('a'))
print(s.str.isdigit())
print(s.str.len())
print(s.str.strip())

#데이터 프레임 병합
df = pd.DataFrame(np.random.randn(10,4))
pieces = [df[:3],df[3:7],df[7:]]
print(pieces)
print(pd.concat(pieces))

#그룹화
df = pd.DataFrame({'A':['foo','bar','foo','bar','foo','bar'],'B':["one","one","two","three","two","four"],'C':np.random.randn(6),'D':np.random.randn(6)})
print(df)
print(df.groupby('A').sum())
print(df.groupby(['A','B']).sum())


