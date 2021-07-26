import pandas as pd
from sklearn import svm
result = pd.read_csv("http://javaspecialist.co.kr/pds/382")
result
result.info()
result['y_true'].value_counts()
# 0    1635
# 1     158
result['y_pred'].value_counts()
# 0    1694
# 1      99
pd.crosstab(result.y_true, result.y_pred)

#(1) 정확도
from sklearn.metrics import accuracy_score
accuracy_score(result['y_true'], result['y_pred'])
accuracy_score(result.y_true, result.y_pred)
# 0.9425543781372002


#(2) 정밀도
from sklearn.metrics import precision_score
precision_score(result.y_true, result.y_pred)
# 0.7777777777777778

#(3) 민감도
from sklearn.metrics import recall_score
recall_score(result.y_true, result.y_pred)
# 0.4873417721518987
recall_score(result.y_true, result.y_pred, pos_label=1)

#(4) 특이도
recall_score(result.y_true, result.y_pred, pos_label=0)
# 0.9865443425076452

#(5) 오류율
1-recall_score(result.y_true, result.y_pred, pos_label=0)
# 0.013455657492354778

#(6) f1-score
from sklearn.metrics import f1_score
f1_score(result.y_true, result.y_pred)
# 0.5992217898832685

#Roc-auc 이용한 성능비교
#auc값이 1에 가까울 수록 좋다.
#두 모델이 비슷한 경우에 어떤 모델이 더 좋은 지 알아보기 위한 지표로 활용

from sklearn.datasets import make_classification #가상으로 분류데이터 만들어줄때 쓴다. 연구원 - 알고리즘 테스트
X,Y=make_classification(n_samples=1000, weights=[0.95, 0.05], random_state=5)
X.shape# 피쳐개수 20
X
Y.shape# 이진분류 0,1
Y

#모델생성
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
lr_model = LogisticRegression().fit(X,Y)
svm_model = SVC(gamma = 0.0001, C=3000, probability=True).fit(X,Y)

lr_pred_y = lr_model.predict(X)
svm_pred_y = svm_model.predict(X)

pd.crosstab(Y, lr_pred_y)
# col_0    0   1
# row_0
# 0      940   3
# 1       30  27
pd.crosstab(Y, svm_pred_y)
# col_0    0   1
# row_0
# 0      940   3
# 1       30  27

#roc커브
from sklearn.metrics import roc_curve
fpr1, tpr1, thr1 = roc_curve(Y, lr_model.decision_function(X))
fpr2, tpr2, thr2 = roc_curve(Y, svm_model.decision_function(X))
import matplotlib.pyplot as plt
plt.plot(fpr1, tpr1, label='logistic')
plt.plot(fpr2, tpr2, label='svm')
plt.legend()
plt.show()

from sklearn.metrics import auc
auc(fpr1, tpr1), auc(fpr2, tpr2)
# (0.9112202563673234, 0.9037227214377407)
#fpr = false positive rate
#trp = true positive rate







