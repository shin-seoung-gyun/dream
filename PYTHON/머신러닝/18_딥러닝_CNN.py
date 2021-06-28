from tensorflow import keras
import numpy as np

#1) 데이터 수집 - 패션 MINIST 이미지 크기 28*28
#10가지 패션 아이템

(X_train, Y_train), (X_test, Y_test) = \
        keras.datasets.fashion_mnist.load_data()

#2) 데이터 전처리 및 탐색
#2-1) 데이터 정규화
#0~255 => 0~1
#(data-min(data))/(max(data)-min(data))
#(123-0)/(255-0) =  123/255
X_train_scaled = X_train/255
X_test_scaled = X_test/255

X_train_scaled=X_train_scaled.reshape(-1,28,28,1)
X_test_scaled=X_test_scaled.reshape(-1,28,28,1)
X_train_scaled.shape
X_test_scaled.shape

#2-3) 검증데이터 생성
from sklearn.model_selection import train_test_split
X_train, X_val, Y_train, Y_val = train_test_split(
        X_train_scaled, Y_train, test_size=0.2, random_state=42)
X_train.shape

#3)CNN 모델 생성
model = keras.Sequential()
model.add(keras.layers.Conv2D(32,kernel_size=3,activation='relu', padding='same',#32=필터개수
    input_shape=X_train.shape[1:]))
X_train.shape[1:]#(28, 28, 1)

model.add(keras.layers.MaxPooling2D(2))#풀링크기
#특성맵의 크기 (14*14)*32

model.add(keras.layers.Conv2D(64,kernel_size=3,activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))
#특성맵의 크기 (7*7)*64

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100,activation='relu'))
model.add(keras.layers.Dropout(0.3))
#출력층
model.add(keras.layers.Dense(10,activation='softmax'))

model.summary()

#모델 플롯 시각화 - 저장
keras.utils.plot_model(model, to_file='cnn-model.png')

#모델 컴파일과 훈련
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


#베스트 훈련모델을 저장
checkpoint_cb = keras.callbacks.ModelCheckpoint('./best-cnn-model.h5', save_best_only=True)

#조기 종료 조건
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

hist = model.fit(X_train, Y_train, epochs=20, validation_data=(X_val,Y_val),
callbacks=[checkpoint_cb,early_stopping_cb], batch_size=64)

import matplotlib.pyplot as plt
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.xlabel('accuracy')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

model.evaluate(X_test_scaled, Y_test)
# [0.23556013405323029, 0.9176999926567078]

#예측
preds = model.predict(X_test_scaled[0:1])
X_test_scaled[0].shape#(28, 28, 1)
X_test_scaled[0:1].shape#(1, 28, 28, 1)
X_test_scaled.shape#(10000, 28, 28, 1)
preds
import numpy as np
np.argmax(preds)#9

plt.imshow(X_test_scaled[0],cmap='gray_r')
plt.show()

plt.bar(range(1,11),preds[0])
plt.xticks(range(1,11))
plt.xlabel('class')
plt.ylabel('prod')
plt.show()

