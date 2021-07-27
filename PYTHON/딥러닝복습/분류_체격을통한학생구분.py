# import pandas as pd

# data_df = pd.read_csv('./data/학생건강검사 결과분석 rawdata_서울_2015.csv', encoding='ANSI')
# data_df.head()
# data_df['키']
# data_df.info()

import os
os.listdir('data')
fileName =os.listdir('data')[0]
file = open('./data/'+fileName) 
 
#파일의 첫행 제거
file.readline()

#데이터와 레이블 저장하기 위한 리스트
X = []
Y = []
for line in file :
    strList = line.split(",")
    #학교명 인덱스 9
    school = strList[9]
    #성별 13
    #여 = 0, 남자 = 1
    gender = 1 if strList[13]=='남' else 0
    #키 15
    height = float(strList[15])
    #몸무게 16
    weight = float(strList[16])

    tempData = []
    tempData.append(height)
    tempData.append(weight)
    tempData.append(gender)

    if school.endswith("초등학교"):
        label =0
    elif school.endswith("중학교"):
        label = 1
    elif school.endswith("고등학교"):
        label =2

    X.append(tempData)
    Y.append(label)
import numpy as np
X = np.array(X)
Y = np.array(Y)
X.shape
Y.shape

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y ,test_size=0.3, random_state=1)

from tensorflow import keras
from keras.layers import Dense
model = keras.Sequential()
model.add(Dense(100, activation='relu', input_shape=(3,)))#은닉층
model.add(Dense(50, activation='relu'))#은닉층
model.add(Dense(3, activation='softmax'))#출력층

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=8)
hist = model.fit(X_train, Y_train, epochs=30, validation_data=(X_test,Y_test), callbacks=
                    [early_stop])




















































