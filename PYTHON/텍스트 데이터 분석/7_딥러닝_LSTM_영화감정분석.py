import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#1) 데이터 불러오기
train_data = pd.read_table('./data/ratings_train.txt')
test_data = pd.read_table('./data/ratings_test.txt')
train_data.head()
train_data.info()
test_data.head()
test_data.info()

#2) 데이터 전처리
#2-1) 결측치 제거
train_data.isna().sum() #document    5
train_data.dropna(how='any', inplace=True)
test_data.isna().sum() #document    5
test_data.dropna(how='any', inplace=True)

#2-2) 중복데이터 제거
train_data.info()#149995
train_data['document'].nunique()#146182
train_data.drop_duplicates(subset=['document'], inplace=True)

test_data.info()#49999
test_data['document'].nunique()#49157
test_data.drop_duplicates(subset=['document'], inplace=True)

#2-3) 한글 이외의 문자들 제거
train_data['document']=train_data['document'].str.replace("[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ ]+"," ")
train_data.head()

test_data['document']=train_data['document'].str.replace("[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ ]+"," ")
test_data.head()

#2-4) label개수 분포 확인
train_data.groupby('label').size()
#0    73342
#1    72840

train_data['label'].value_counts().plot(kind='bar')
plt.show()

#2-5) 문장 토큰화
okt = Okt()
okt.morphs("이것은 샘플 데이터 입니다.", stem=True)
# ['이', '것', '은', '샘플', '데이터', '이다', '.'] 표제어
# ['이', '것', '은', '샘플', '데이터', '입니다', '.'] 원형

stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

X_train = []
for words in train_data['document']:
    print(words)
    temp_x = okt.morphs(words, stem=True)
    #불용어 제거
    tempList = []
    for word in temp_x :
        if not word in stopwords :
            tempList.append(word)
    X_train.append(tempList)
X_train[:3]




X_test = []
for words in train_data['document']:
    temp_x = okt.morphs(words, stem=True)
    #불용어 제거
    tempList = []
    for word in temp_x :
        if not word in stopwords :
            tempList.append(word)
    X_test.append(tempList)
X_test [:3]

#2-6) 정수 인코딩
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
tokenizer.word_index



#등장 빈도수가 2이하인 단어 제외

#2-7) 빈도수가 1회인 단어들 전체단어 집합에 대한 비율확인
threshold = 3
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

#단어집합의 크기
vocab_size = total_cnt -rare_cnt+1
tokenizer = Tokenizer(vocab_size)
X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)
X_train[0]

#패딩
lengths = [len(x) for x in X_train]
np.mean(lengths)

plt.hist(lengths)
plt.show()

max_len = 35
X_train = pad_sequences(X_train, maxlen=max_len)
X_test = pad_sequences(X_test, maxlen=max_len)

#3) 분석 모델 구축
from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

model = Sequential()
model.add(Embedding(vocab_size, 100,input_length=max_len))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=3)
mc = ModelCheckpoint('./best_영화감정분석모델.h5', monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

Y_train = np.array(train_data['label'])
Y_test = np.array(test_data['label'])

hist = model.fit(X_train, Y_train, epochs=15, callbacks=[es, mc], batch_size=64, validation_split=0.2)











































































