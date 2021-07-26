import seaborn  as sns
from sklearn.decomposition import PCA
iris = sns.load_dataset("iris")
X,Y = iris.iloc[:,:-1], iris.species
X.shape #(150, 4) 독립변수 4개
pca = PCA(n_components=2)# n_components 주성분 개수
iris_pca = pca.fit_transform(X)

iris_pca.shape#(150, 2)
pca.components_#독립변수 4개로 주성분 2개를 만듦.
# array([[ 0.36138659, -0.08452251,  0.85667061,  0.3582892 ],
#        [ 0.65658877,  0.73016143, -0.17337266, -0.07548102]])
pca.explained_variance_#array([4.22824171, 0.24267075]) 주성분별 분산값

pca.explained_variance_ratio_#array([0.92461872, 0.05306648]) 분산 비율

# 꽃의 너비,     꽃의 길이,    꽃받침의 너비, 꽃받침의 길이
# [ 0.36138659, -0.08452251,  0.85667061,  0.3582892 ]


#중요변수 추리는 방법 정리
#의자결정 나무의 feature_importance
#랜덤 포레스트 feature_importance
#주성분 분석
#독립변수들 간의 상관계수가 큰경우 (독립 변수 제거 할수있다.)
#종속변수와 상관계수가 큰 독립변수들은 중요변수

#정규화(표준화) 필요
#회귀 분석의 회귀 계수값이 큰경우 중요 변수

