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

#2-3) 검증데이터 생성
from sklearn.model_selection import train_test_split
X_train, X_val, Y_train, Y_val = train_test_split(
        X_train_scaled, Y_train, test_size=0.2, random_state=42)


def model_fn(a_layer=None):
    model = keras.Sequential()
    model.add(keras.layers.Flatten(input_shape=(28,28)))#입력편하게 해주는케라스 함수
    model.add(keras.layers.Dense(100, activation='relu'))
    model.add(keras.layers.Dense(100, activation='relu'))
    model.add(keras.layers.Dense(100, activation='relu'))
    model.add(keras.layers.Dense(100, activation='relu'))
    model.add(keras.layers.Dense(100, activation='relu'))
    model.add(keras.layers.Dense(100, activation='relu'))
  
    if a_layer :
        model.add(a_layer)
    model.add(keras.layers.Dense(10, activation='softmax'))
    return model

model = model_fn()
model.summary()

model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
hist = model.fit(X_train, Y_train, epochs=20, verbose=0)

#에포크에 따른 loss 시각화
import matplotlib.pyplot as plt
plt.plot(hist.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid(True)
plt.show()

plt.plot(hist.history['accuracy'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid(True)
plt.show()

model = model_fn()
model.summary()

model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
hist = model.fit(X_train, Y_train, epochs=20, verbose=1, validation_data=(X_val,Y_val))


plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid(True)
plt.legend(['train','val'])
plt.show()

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid(True)
plt.legend(['train','val'])
plt.show()

#옵티마이저 변경 adam사용

model = model_fn()
model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
hist = model.fit(X_train, Y_train, epochs=20, verbose=1, validation_data=(X_val,Y_val))


plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid(True)
plt.legend(['train','val'])
plt.show()

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid(True)
plt.legend(['train','val'])
plt.show()

#드롭아웃
#대표적인 규제방법(과대적합 방지)
#어떤 샘플을 처리할때 랜덤하게 은닉층의 뉴런의 출력을 끈다.
#(출력을 0으로 만듬)
#뉴런이 랜덤하게 꺼시면 특정 뉴런에 과대하게 의존하는 것을 
#줄일 수 있고, 모든 입력에 대해 주의를 기울여야 한다.
model = model_fn(keras.layers.Dropout(0.3))
model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
hist = model.fit(X_train, Y_train, epochs=20, verbose=1, validation_data=(X_val,Y_val))


plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid(True)
plt.legend(['train','val'])
plt.show()

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid(True)
plt.legend(['train','val'])
plt.show()

#훈련이 끝난 뒤에는 드롭아웃을 적용하지 말아야한다.
#모델 평가와 예측에 사용할때는 자동으로 드롭아웃을 적용하지 않음.

#--------------------------------------------------------------------------------------------------------
#모델 저장과 복원
model.save_weights('./model-weights.h5')
model.save('./model-whole.h5')

model = model_fn(keras.layers.Dropout(0.3))
model.load_weights('./model-weights.h5')

model.predict(X_val)[0]
# array([4.2037307e-10, 3.4817689e-16, 8.3225722e-13, 3.1046402e-15,
#        4.2533557e-10, 2.4128651e-06, 4.1153873e-12, 9.7544250e-11,
#        9.9999762e-01, 2.8633682e-13], dtype=float32)

import numpy as np
val_labels = np.argmax(model.predict(X_val), axis=-1)
val_labels[100]#8
Y_val[100]#8


plt.imshow(X_val[100], cmap='gray_r')
plt.show()

#성능측정 및 모델 훈련 안됨 (가중치만 불러와서)
# model.evaluate(X_test_scaled, Y_test)

model = keras.models.load_model("./model-whole.h5")
model.evaluate(X_test_scaled, Y_test)
# [0.3622871935367584, 0.8770999908447266]
#모델평가및 훈련 가능
hist = model.fit(X_train, Y_train, epochs=5, verbose=1, validation_data=(X_val,Y_val))

#---------------------------------------------------------------------------------------------------------------
#미니배치학습
#배치 크기:모델 학습시 한번에 모델에 전달하는 입력데이터 수
#한번에 여러 데이터를 전달했을때 모델은 각 데이터의 손실과
#손실함수의 기울기를 구하지만, 가중치 갱신은 구해진 기울기의 
# 평균값으로 한번만 실시된다. (배치크기가 클수록 훈련 속도가 빠르다.)

#장점 : 복수의 데이터를 이용하여 가중치를 갱신하면 편향시 심한 데이터의 영향을 덜 받게 된다.

#편향된 데이터가 많을때는 배치크기를 크게하고, 유사한 데이터가 많을때는 배치크기를 작게하는등 조정이 필요
#
#확률적 경사하강법 : 배치크기 1
#배치학습 (경사하강법) : 배치크기 전체데이터수
#미니배치 : 배치크기 1이상 전체 데이터수 이하

model1 = model_fn(keras.layers.Dropout(0.3))
model1.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
hist1 = model1.fit(X_train, Y_train, epochs=20, verbose=1, validation_data=(X_val,Y_val), batch_size=16)

model2 = model_fn(keras.layers.Dropout(0.3))
model2.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
hist2 = model2.fit(X_train, Y_train, epochs=20, verbose=1, validation_data=(X_val,Y_val), batch_size=64)

model3 = model_fn(keras.layers.Dropout(0.3))
model3.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
hist3 = model3.fit(X_train, Y_train, epochs=20, verbose=1, validation_data=(X_val,Y_val), batch_size=128)


plt.plot(hist1.history['loss'])
plt.plot(hist2.history['loss'])
plt.plot(hist3.history['loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['hist1','hist2','hist3'])
plt.grid(True)
plt.show()

plt.plot(hist1.history['accuracy'])
plt.plot(hist2.history['accuracy'])
plt.plot(hist3.history['accuracy'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid(True)
plt.legend(['hist1','hist2','hist3'])
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------
#콜백 : 훈련과정 중간에 어떤 작업을 수행할수 있게 하는 객체
#콜백 활용 : 훈련 조기 종료 , 최적의 점수를 내는 모델 저장
#EX) 100번의 에포크를 설정했을때 최적의 점수를 내는 지점을 확인후 에포크 다 실행하지 않고 종료
model1 = model_fn(keras.layers.Dropout(0.3))
model1.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#베스트 훈련모델을 저장
checkpoint_cb = keras.callbacks.ModelCheckpoint('./best-model.h5', save_best_only=True)

hist1 = model1.fit(X_train, Y_train, epochs=20, verbose=1, validation_data=(X_val,Y_val), batch_size=16 , callbacks=[checkpoint_cb])

#베스트 모델 부르기
best_model = keras.models.load_model('./best-model.h5')
best_model.evaluate(X_test_scaled,Y_test)

#조기종료 콜백함수 : 검증 점수(손실값)이 상승하기 시작하면 훈련을 중지
#과대적합이 커지면 훈련모델 종료
#patience 파라미터 : 연속 검증 점수가 낮아지지 않으면 훈련 중지
#ex) patience=2, 2번 연속 검증 점수(loss값)가 높아지면 훈련 중지

model1 = model_fn(keras.layers.Dropout(0.3))
model1.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#베스트 훈련모델을 저장
checkpoint_cb = keras.callbacks.ModelCheckpoint('./best-model.h5', save_best_only=True)

#조기 종료 조건
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

hist1 = model1.fit(X_train, Y_train, epochs=20, verbose=1, validation_data=(X_val,Y_val), batch_size=16 , callbacks=[checkpoint_cb, early_stopping_cb])

#최상의 모델은 에포크 11번째
early_stopping_cb.stopped_epoch #13(14)

model1.evaluate(X_test_scaled, Y_test)
# [0.3606129586696625, 0.8776999711990356]



model1 = model_fn(keras.layers.Dropout(0.3))
model1.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#조기 종료 조건
early_stopping_cb = keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)

hist1 = model1.fit(X_train, Y_train, epochs=20, verbose=1, validation_data=(X_val,Y_val), batch_size=16 , callbacks=[checkpoint_cb, early_stopping_cb])

model1.evaluate(X_test_scaled, Y_test)







































