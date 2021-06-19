import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
print(titanic)
print(titanic.shape)
print(titanic.info())

#데이터 결측치 확인
print(titanic.isnull().sum())

##age 결측치 중앙값으로 치환 하기 (fillna 메서드 이용)
titanic['age'] = titanic['age'].fillna(titanic['age'].median())
print(titanic.isnull().sum())

#embarked 최빈치로 치환하기
# print(titanic['embarked'].value_counts())
titanic['embarked'] = titanic['embarked'].fillna('S')

#embark_town 최빈치로 치환하기
# print(titanic['embark_town'].value_counts())
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')
##deck 최빈치로 지환하기
# print(titanic['deck'].value_counts())
titanic['deck'] = titanic['deck'].fillna('C')

print(titanic.info())
print(titanic.survived.value_counts())#0:549, 1:342

# #남녀 성별에 따른 생존률 파이차트로 그리기

import matplotlib.pyplot as plt

# # 캔버스 및 프레임 생성
# f, ax = plt.subplots(1,2, figsize=(10,5))
# #남자 생존자 파이차트
# titanic['survived'][titanic['sex']=='male'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f%%',ax=ax[0],shadow=True)
# #여자 생존자 파이차트
# titanic['survived'][titanic['sex']=='female'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f%%',ax=ax[1],shadow=True)

# ax[0].set_title("Survived (Male)")
# ax[1].set_title("Survived (Female)")
# plt.show()

# ##막대 차트 : pclass 등급별 생존자수
# sns.countplot(x='pclass', hue='survived',data= titanic)
# plt.title("Pclass Vs Survived")
# plt.show()

# ##데이터 분석 : 상관분석 모델링
# titanic_corr = titanic.corr(method='pearson')
# print(titanic_corr)

# titanic_corr.to_csv("./데이터분석/titanic_corr.csv", index = False)

# ##결과의 시각화
# #(1) 산점도로 상관분석 시각화 하기

# sns.pairplot(titanic, hue='survived')
# plt.show()

# #(2) 두 변수의 상관관계 시각화
# sns.catplot(x='pclass',y='survived',hue='sex',data=titanic, kind='point')
# plt.show()

# (3) 변수 사이의 상관계수를 히트맵으로 시각화 하기
def category_age(x):
    return x//10

def category_sex(x):
    if x == 'male' :
        return 1
    else :
        return 0
titanic['age2']=titanic['age'].apply(category_age)

titanic['sex2']=titanic['sex'].apply(category_sex)
print(titanic)
titanic['family']=titanic['sibsp']+titanic['parch']+1

#히트맵에 사용할 데이터를 추출
heatmap_data = titanic[['survived','sex2','age2','family','pclass','fare']]
#히트맵에 사용할 색상맵 지정
colorMap = plt.cm.RdBu
#corr() 함수로구한 상관 계수로 히트맵 생성
sns.heatmap(heatmap_data.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap = colorMap, linecolor='white', annot = True, annot_kws={'size':10})
plt.show()
