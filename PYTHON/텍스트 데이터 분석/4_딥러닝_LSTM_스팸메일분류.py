from typing import Sequence
from keras_preprocessing import sequence
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.layers import embeddings

#1) 데이터 불러오기
data = pd.read_csv('./data/spam.csv')
data.head()
data.info()


#2) 데이터 탐샘 및 전처리
#2-1) 칼럼 삭제
del data['Unnamed: 2']
del data['Unnamed: 3']
del data['Unnamed: 4']
#2-2) 타겟 데이터를 0,1로 변경 (0은 일반 1은 스팸)
data['v1'] = data['v1'].replace(['ham', 'spam'], [0,1])
data.head()

#2-3) 널데이터 확인 후 삭제
data.isnull().sum()

#2-4) 중복데이터 확인 후 삭제
data['v2'].nunique()#5169 유니크한 개수 표시
data.drop_duplicates(subset=['v2'], inplace=True)
data.info()

#2-5) 타겟, 피쳐 데이터 생성
X_data = data['v2']
Y_data = data['v1']

#2-6) 피쳐 데이터 정수 토큰화
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_data)
#단어를 숫자값, 인덱스로 변환하여 저장
sequences  = tokenizer.texts_to_sequences(X_data)
sequences[0]
# [47, 433, 4011, 779, 705, 662, 64, 8, 1201, 94, 121, 434, 1202, 142, 2710, 1203, 68, 57, 4012, 137]

#각 정수 숫자가 어떤 단어 인지 확인
tokenizer.word_index

#2-7) 빈도수가 1회인 단어들 전체단어 집합에 대한 비율확인
threshold = 2
total_cnt = len(tokenizer.word_index) # 전체 단어수
rare_cnt =0#등장 빈도수가 threshold보다 작은 단어 개수 카운트
total_freq = 0 # 훈련 데이터 전체 단어 빈도수 총 합
rare_freq = 0 #등장 빈도수가 threshold보다 작은 단어의 빈도수 총합

tokenizer.word_counts#각 단어의 빈도수 확인
for key, val in tokenizer.word_counts.items():
    total_freq = total_freq+val

    #단어의 빈도수가 threshold보다 작은 경우
    if val < threshold :
        rare_cnt +=1
        rare_freq +=val

print(f'등장빈도가 {threshold-1}번 이하인 드문 단어수 : {rare_cnt}')
print(f'드문 단어의 비율 : {(rare_cnt/total_cnt)*100}')
print(f'전체 단어에서 드문 단어의 등장 빈도 비율: {(rare_freq/total_freq)*100}')

tokenizer = Tokenizer(num_words=100+1)
tokenizer.fit_on_texts(X_data)
tokenizer.word_index
sequences = tokenizer.texts_to_sequences(X_data)
sequences[0]

sorted(tokenizer.word_index.items(), key=lambda x:x[1], reverse=True)

tokenizer = Tokenizer(num_words=total_cnt-rare_cnt+1)
tokenizer.fit_on_texts(X_data)
tokenizer.word_index
sequences = tokenizer.texts_to_sequences(X_data)
sequences[0]

#2-8) sms의 평균 길이
X_data = sequences
lengths = [len(x) for x in X_data]
np.mean(lengths)

plt.hist(lengths)
plt.xlabel('lenght')
plt.ylabel('freq')
plt.show()

max_len = 50#길이 분포가 대략 50이하에서 대부분 있으므로 50으로 선정
data = pad_sequences(X_data, maxlen=max_len)
data.shape #(5169, 50)

#훈련/테스트 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(data, Y_data, random_state=32)
X_train.shape #(3876, 50)
X_test.shape #(1293, 50)

#3) 모델 구축
from tensorflow.keras.layers import LSTM, Embedding, Dense
from tensorflow.keras.models import Sequential
model= Sequential()
vocabSize = total_cnt-rare_cnt+1
model.add(Embedding(vocabSize, 32, input_length=max_len))
model.add(LSTM(32,dropout=0.4))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
hist = model.fit(X_train, Y_train, epochs=20, batch_size=16, validation_split=0.2 )



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
model.evaluate(X_test,Y_test)

#스팸 예측
text = ["WINNER!! As a valued network customer you have been selected to receivea"]
text_encoded = tokenizer.texts_to_sequences(text)
text_encoded
text_encoded_pad = pad_sequences(text_encoded, maxlen= max_len)
text_encoded_pad[0]
model.predict(text_encoded_pad)
# array([[0.99989533]], dtype=float32)
#0.5이상은 스팸
#0.5미만은 일반

#스팸 예측
text = ["As per your request 'Melle Melle (Oru Minnaminunginte Nurungu Vettam)' has been set as your callertune for all Callers. Press *9 to copy your"]
text_encoded = tokenizer.texts_to_sequences(text)
text_encoded
text_encoded_pad = pad_sequences(text_encoded, maxlen= max_len)
text_encoded_pad[0]
model.predict(text_encoded_pad)
# array([[3.0639752e-05]], dtype=float32)

