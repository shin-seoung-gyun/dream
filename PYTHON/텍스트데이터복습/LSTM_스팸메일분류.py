import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras_preprocessing import sequence
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from tensorflow import keras

#1) 데이터 불러오기
data_df = pd.read_csv('./data/spam.csv')
data_df.head()
data_df.info()

#2) 데이터 전처리
#2-1) 데이터 칼럼 삭제
del data_df['Unnamed: 2']
del data_df['Unnamed: 3']
del data_df['Unnamed: 4']
data_df

#2-2) 티켓 테이터 값 변경 (0:일반, 1:스팸)
data_df['v1'] = data_df['v1'].replace(['ham','spam'], [0,1])
data_df.head()
data_df.info()

#2-3) 중복 데이터 확인
data_df['v2'].nunique()
data_df.drop_duplicates(subset=['v2'], inplace=True)
data_df.info()


#2-4) 타겟, 피쳐데이터 생성
X= data_df['v2']
Y= data_df['v1']

#2-5)피쳐 데이터(문자열() -> 정수 토큰화(각 단어마다 고유한 숫자값 매김)
#정수 토큰화는 일반저그로 빈도수가 높은 단어가 정수값이 작다
tokenizer=Tokenizer()
tokenizer.fit_on_texts(X)

#단어를 숫자값으로 변환하여 저장
sequences = tokenizer.texts_to_sequences(X)
X[0]
sequences[0]

#각 단어마다의 정수값
tokenizer.word_index
#단어의 총 빈도값
tokenizer.word_counts

#2-6) 빈도수가 threshold 이하인 단어들 전체 단어 집합에 대한 비율 확인
threshold = 3# 3미안 , 단어빈도수 1~2인 단어들 확인
total_cnt = len(tokenizer.word_index)
total_cnt #8916, 전체 단어수
rare_cnt = 0 #빈도수가 threshold 미만인 단어의 개수
rare_freq = 0 #빈도수가 threshold 미만인 단어의 총 빈도수
total_feq = 0 #훈련 데이터의 총 빈도수

for key, val in tokenizer.word_counts.items():
    total_feq += val
    #단어 빈도수가 threshold 보다 작은 경우
    if val < threshold :
        rare_cnt +=1
        rare_freq += val

print(f'등장빈도가 {threshold-1}번이하인 드문 단어수 :{rare_cnt}')
print(f'드문단어비율 : {(rare_cnt/total_cnt*100)}')
print(f'전체단어빈도에서 드문단어 등장 빈도의 비율 : {(rare_freq/total_feq)*100}')

tokenizer = Tokenizer(num_words=total_cnt - rare_cnt+1)
tokenizer.fit_on_texts(X)
tokenizer.word_index
sequences = tokenizer.texts_to_sequences(X)
len(tokenizer.word_index)
sequences[0]

sorted(tokenizer.word_index.items(), key=lambda x: x[1], reverse=True)

#2-7) sms의 길이 제한, 모든 문장의 길이를 통일
#문장들의 길이 분포 확인 - 히스토그램
X_seq = sequences
len_list = [len(x) for x in X_seq]
np.mean(len_list)
plt.hist(len_list)
plt.xlabel('length')
plt.ylabel("freq")
plt.show()

max_len =50 #길이 분포가 50이하에 대부분 분포
data = pad_sequences(X_seq, maxlen=max_len)
data.shape
data[0]

#2-8) 훈련/테스트 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(data,Y,
                                     random_state=32, test_size=0.3, stratify=Y )


#3)분석모델 구축
from tensorflow.keras.layers import LSTM, Embedding, Dense
from tensorflow.keras.models import Sequential
model = Sequential()

#단어를 딥러닝에 쓸값으로 변환
#(1) 원핫인코딩 벡터화
#총 단어수 100, 모든 단어마다 벡터 사이즈를 100, [0,0,0,0,0,0,0,1,0,0,0,0,0,0,,0,0,0.....]
#(2) 워드임베딩 벡터화(딥러닝 모델)
#총단어수 100, 벡터크기를 지정 100 보다 작음

vocabSize = total_cnt - rare_cnt+1 #총단어수
model.add(Embedding(vocabSize,32,input_length=max_len))
model.add(LSTM(32, dropout=0.4))
model.add(LSTM(16, dropout=0.3))
model.add(Dense(1, activation='sigmoid'))#출력층
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
hist = model.fit(X_train, Y_train, epochs=3, batch_size=8, validation_split=0.2)

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train','val'])
plt.show()

model.evaluate(X_test, Y_test)# 0.98

#스팸 예측
text = ["Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive "]
text_seq=tokenizer.texts_to_sequences(text)
text_seq[0]
text_seq_pad = pad_sequences(text_seq, maxlen=max_len)
text_seq_pad[0]
model.predict(text_seq_pad)


