#추측 통계는 추정과 검정이 있다.
#추정 : 값을 추정하는 것이고
#검정 : 값이 맞는지 확인 하는 것
#1. 점추정 : 추정하고 싶은 모수(모평균,모분산)을 하나의 수치로 추정
# 2. 구간추정 : 폭(구간)으로 모수를 추정하는 방법

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
#ex)전고생 400명의 모집단, 모평균과 모분산 추정
# a 학생이 가지고 있는 데이터는 20명의 데이터만 있다.
# 데이터 준비
df = pd.read_csv('./data/ch4_scores400.csv')
df.head()
scores = np.array(df['score']) 

#모수 구하기
p_mean= np.mean(scores)
p_var=np.var(scores)
p_mean, p_var

#모집단의 분포 히스토 그램 시각화
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
xs = np.arange(101)
ax.hist(scores, bins=100, range=(0,100), density=True)
rv = stats.norm(p_mean, np.sqrt(p_var))
ax.plot(xs, rv.pdf(xs), color='gray')
plt.show()
#응시자가 많을 수록 시험점수는 정규분포를 따르는 것으로 근사화 할수 있음.

#A학생이 무작위 추출 - 20개 표본 데이터
np.random.seed(0)
n=20
sample = np.random.choice(scores, n)
sample

#A학생과는 별도로 표본크기 20일때 어느정도 정확도로
#모수를 추정하는지 시뮬레이션
#표본크기 20, 표본데이터 1만개 준비
np.random.seed(1111)
n_samples = 10000
samples = np.random.choice(scores, (n_samples,n))
samples.shape #행(10000)데이터수, 열(20)표본수

#1.점추정
#무작위 추출로 얻은 20명의 시험점수는 기댓값이 p_mean 이고
#분산이 p_var인 확률분포를 따르고, 점수는 서로 독립인 확률변수라 생각할수있다.

#p_mean 을 추정하기 위해 표본평균 Xbar  가 확률변수가 되고
#Xbar의 기댓값은 p_mean, 분산 p_var/20

#(1) 모평균의 점추정
#추정량의 기댓값이 추측하려는 모수가 되는 성질을 불편성이라 한다.
#불편성(unbiasedness) 을 가진 추정량을 분편추정량이라고 한다.

for i in range(5):
    s_mean = np.mean(samples)
    print(f'{i+1}번째의 표본평균 : {s_mean:.3f}')
sample_means = np.mean(samples, axis=1)
p_mean, np.mean(sample_means)

#일치성 : 표본 크기 n을 증가시키면 추측하기 원하는 모수에 수렴하는 성질
np.mean(np.random.choice(scores, 100))

##표본평균은 불편성과 일치성 모두 가지고 있어서 모평균을 잘 추정한다고 말할수 있다.

















































































































