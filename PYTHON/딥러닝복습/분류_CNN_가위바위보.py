import imp
import os
from keras.backend import dropout
import numpy as np
from PIL import Image
from tensorflow.python.keras.callbacks import EarlyStopping

path ="./data/가위바위보"
targets = os.listdir("./data/가위바위보")
targets #['paper', 'rock', 'scissors']

X=[]
Y=[]

for i, target in enumerate(targets):
    for fileName in os.listdir(path+"/"+target):
        img = Image.open(path+"/"+target+"/"+fileName)
        img = img.convert("RGB")
        img = img.resize((100,100))
        data = np.asarray(img)
        X.append(data)
        Y.append(i)
X = np.array(X)
Y = np.array(Y)
X.shape
Y.shape

#훈련 / 테스트 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y ,test_size=0.2, random_state=3, stratify=Y)

#데이터 정규화
X_train = X_train.astype("float")/256
X_test = X_test.astype("float")/256

#모델 구축
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D
from keras.layers import Dropout, Dense, Flatten

model = Sequential()
model.add(Conv2D(32, kernel_size=3, activation='relu', padding='same',
        input_shape=X_train.shape[1:]))
model.add(MaxPool2D(2))
model.add(dropout(0.3))

model.add(Conv2D(64, kernel_size=3, activation='relu', padding='same'))
model.add(MaxPool2D(2))
model.add(dropout(0.3))

model.add(Conv2D(32, kernel_size=3, activation='relu', padding='same'))
model.add(MaxPool2D(2))
model.add(dropout(0.3))

model.add(Flatten())
model.add(Conv2D(256,activation='relu'))
model.add(dropout(0.3))
model.add(Dense(3, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

#모델훈련
from tensorflow import keras
checkBest = keras.callbacks.ModelCheckpoint('best_cnn_model.h5', save_best_only=True)
EarlyStop = keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
hist = model.fit(X_train, Y_train, epochs=50, batch_size=16, validation_split=0.2,
                callbacks=[checkBest,EarlyStop])

#모델 평가
model.evaluate(X_test, Y_test)
# [7.464894679287681e-06, 1.0]
model.predict(X_test[200:201])
# array([[3.7217188e-16, 1.0000000e+00, 9.4912545e-21]], dtype=float32)
Y_test[200]
# 1

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,10))
plt.imshow(X_test[200])
plt.show()




























