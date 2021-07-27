from keras_preprocessing.text import tokenizer_from_json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from konlpy.tag import Okt
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#1.데이터 불러오기
train_data = pd.read_table('./data/ratings_train.txt')
test_data = pd.read_table('./data/ratings_test.txt')
train_data.head()
test_data.head()
train_data.info()
test_data.info()

#2.데이터 전처리
#2-1 ) 결측치 제거
train_data.dropna(how='any', inplace=True)
test_data.dropna(how='any', inplace=True)

#2-2)중복데이터 제거
train_data.info()
test_data.info()
train_data['document'].nunique()
test_data['document'].nunique()

train_data.drop_duplicates(subset=['document'],inplace=True)
test_data.drop_duplicates(subset=['document'],inplace=True)

#2-3) 한글이외의 문자들 제거
train_data['document'] = train_data['document'].str.replace('[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ]+', " ")
test_data['document'] = test_data['document'].str.replace('[^ㄱ-ㅎ|가-힣|ㅏ-ㅣ]+', " ")
train_data.head()
test_data.head()

#2-4) target분포 확인
train_data.groupby('label').size()
# 0    73342
# 1    72841
test_data.groupby('label').size()
# 0    24446
# 1    24712

train_data = train_data.iloc[:int(len(train_data)*0.1)]
test_data = test_data.iloc[:int(len(test_data)*0.1)]




#2-5) 문장 토큰화
okt = Okt()
okt.morphs("이것은 샘플 문장입니다.", stem=True)#단어 원형
# ['이', '것', '은', '샘플', '문장', '이다', '.']
stopwords=['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

X_train =[]
for words in train_data['document']:
    temp_x = okt.morphs(words, stem=True)
    #불용어 제거
    temp_x = [x for x in temp_x if x not in stopwords]
    X_train.append(temp_x)
X_train[:3]

X_test =[]
for words in test_data['document']:
    temp_x = okt.morphs(words, stem=True)
    #불용어 제거
    temp_x = [x for x in temp_x if x not in stopwords]
    X_test.append(temp_x)
X_test[:3]

#2-6) 정수 토큰화
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
tokenizer.word_index

#2-7) 등장빈도 낮은 단어 제거
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

vocab_size = total_cnt - rare_cnt+1
tokenizer = Tokenizer(num_words=total_cnt - rare_cnt+1)
tokenizer.fit_on_texts(X_train)
tokenizer.word_index
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)


#2-7) 문장 길이 정하기
#문장들의 길이 분포 확인 - 히스토그램
X_seq = X_train_seq
len_list = [len(x) for x in X_seq]
np.mean(len_list)
plt.hist(len_list)
plt.xlabel('length')
plt.ylabel("freq")
plt.show()

max_len =45 #길이 분포가 45이하에 대부분 분포
X_train_seq_pad = pad_sequences(X_train_seq, maxlen=max_len)
X_test_seq_pad = pad_sequences(X_test_seq, maxlen=max_len)

X_train_seq_pad[0]
X_test_seq_pad[0]

#데이터 전처리 /

#3.분석모델 구축
from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=max_len))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))

es = EarlyStopping(monitor='val_loss', patience=3)
mc = ModelCheckpoint('./best_영화감정분석모델.h5', monitor='val_accuracy', verbose=1,
                    save_best_only=True)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
Y_train = np.array(train_data['label'])
Y_test = np.array(test_data['label'])

hist = model.fit(X_train_seq_pad, Y_train, epochs=15, callbacks=[es,mc], batch_size=32, 
                validation_split=0.2)

model.evaluate(X_test_seq_pad, Y_test)

def emotion_predict(sentence) :
    sentence = okt.morphs(sentence, stem = True)
    sentence = [x for x in sentence if not x in stopwords]
    token = tokenizer.texts_to_sequences([sentence])
    pad = pad_sequences(token, maxlen=max_len)
    score = float(model.predict(pad))
    if(score > 0.5) :
        print(f'{score*100:.1f}% 확률로 긍정 리뷰 입니다.')
    else :
        print(f'{(1-score)*100:.1f}% 확률로 부정 리뷰 입니다.')
emotion_predict("너무 참신하고 재밌어요~!")
emotion_predict("감독 뭐하는 놈이냐?")
emotion_predict("와 정말 세계관 최강자들의 영화다")





























