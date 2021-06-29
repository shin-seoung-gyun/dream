#로이터 뉴스 데이터
#총 11,259개 뉴스기사 46개의 카테고리 텍스트 데이터
from keras.engine import sequential
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
#로티어 뉴스 데이터셋 불러오기
from keras.datasets import reuters
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
from keras.preprocessing import sequence
from tensorflow.keras import callbacks

#1)데이터셋 불러오기
(X_train, Y_train), (X_test, Y_test) = reuters.load_data(num_words=1000, test_split=0.2)
#1000개의 가장 빈도가 높은 단어만 가져옴

#2) 데이터 탐색
X_train.shape#(8982,)
Y_train.shape#(8982,)
X_train[0]#[1, 2, 2, 8, 43, 10, 447, 5, 25, 207, 270, 5, 2, 111, 16, 369, 186, 90, 67, 7, 89, 5, 19, 102, 6, 19, 124, 15, 90, 67, 84, 22, 482, 26, 7, 48, 4, 49,
#  8, 864, 39, 209, 154, 6, 151, 6, 83, 11, 15, 22, 155, 11, 15, 7, 48, 9, 2, 2, 504, 6, 258, 6, 272, 11, 15, 22, 134, 44, 11, 15, 16, 8, 197, 2, 90, 67, 52, 29,
#   209, 30, 32, 132, 6, 109, 15, 17, 12]
Y_train[0]#3

#3) 데이터 전처리
#3-1) 뉴스 기사 토큰 길이 평균, 중앙값 구하기
lengths = np.array([len(x) for x in X_train])
np.mean(lengths), np.median(lengths)
# (145.5398574927633, 95.0)

plt.hist(lengths)
plt.xlabel('length')
plt.ylabel('freq')
plt.show()

X_train = sequence.pad_sequences(X_train, maxlen=100)
X_test = sequence.pad_sequences(X_test, maxlen=100)

#4) 모델구축
model = Sequential()
model.add(Embedding(1000,64,input_length=100))
model.add(LSTM(100,dropout=0.35))
model.add(Dense(46,activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


#모델훈련

checkpoint_cb = keras.callbacks.ModelCheckpoint('./best-lstm_뉴스카테고리-model.h5', save_best_only=True)

#조기 종료 조건
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

hist = model.fit(X_train, Y_train, epochs=30, batch_size=16, validation_data=(X_test,Y_test), callbacks=[checkpoint_cb,early_stopping_cb])

# word_to_index = reuters.get_word_index()
# print(word_to_index)
# np.unique(Y_train, return_counts=True)[0] #0~45 라벨
# np.unique(Y_train, return_counts=True)[1] #각 라벨별 개수

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



























































































































































