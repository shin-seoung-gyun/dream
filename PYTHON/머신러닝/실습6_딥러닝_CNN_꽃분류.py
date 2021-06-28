from PIL import Image, ImageEnhance, ImageChops #이미지 처리 모듈(사이즈, 색 등 변경)
import glob
from keras.backend import dropout #여러파일을 한꺼번에 처리할수있도록 하는 모듈
from keras.layers.convolutional import Conv2D
from keras.layers.core import Activation, Dense, Dropout, Flatten
import numpy as np
from sklearn.model_selection import train_test_split

#1)데이터 수집
path = './data/flowers'
targets = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
n_class = len(targets)

#이미지 크기 지정
image_w = 100
image_h = 100

#이미지 데이터 읽어들이기
X=[]
Y=[]
for idx, target in enumerate(targets):
    #레이블 - 원핫인코딩으로 지정
    label = [0]*n_class
    label[idx] = 1
    #이미지 경로
    img_dir = path + '/' + target
    files = glob.glob(img_dir + '/*.jpg')
    print(f'{target}:{len(files)}')

    for file in files:
        img = Image.open(file)
        #색상모드변경 : 'L' = 그레이 스케일 (흑백)
        #'1' = 이진화, 'RGB','RGBA','CMYK'
        img = img.convert("RGB")
        img = img.resize((image_w,image_h))
        data = np.asarray(img)
        X.append(data)
        Y.append(label)

        #데이터 부풀리기
        #밝기 증가 이미지
        enhancer = ImageEnhance.Brightness(img)
        bright_img = enhancer.enhance(1.8)
        data = np.asarray(bright_img)
        X.append(data)
        Y.append(label)

        #좌우대칭 이미지
        horizonal_flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        data = np.asarray(horizonal_flip_img)
        X.append(data)
        Y.append(label)

        #상하대칭 이미지
        vertical_flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)
        data = np.asarray(vertical_flip_img)
        X.append(data)
        Y.append(label)

        #회전
        import random
        rotate_img = img.rotate(random.randint(-30, 30))
        data = np.asarray(rotate_img)
        X.append(data)
        Y.append(label)

        #확대 축소
        zoom = random.uniform(0.7,1.3)
        width, height = img.size
        x = width/2
        y = height/2
        crop_img = img.crop((x-(width/2/zoom), y-(height/2/zoom),
            x+(width/2/zoom), y+(height/2/zoom)))
        zoom_img = crop_img.resize((width, height), Image.LANCZOS)
        data = np.asarray(zoom_img)
        X.append(data)
        Y.append(label)




X= np.array(X)
Y= np.array(Y)
X.shape#(4323, 100, 100, 3)
Y.shape#(4323, 5)

#훌련/테스트 데이터 분할
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=32)

#데이터 저장
xyData = (X_train, X_test, Y_train, Y_test)
np.save(path+'/flowerObj.npy', xyData)

#훈련/검증 세트 분할
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.2, random_state=40)

X_train.shape, X_val.shape

#데이터 정규화
X_train = X_train.astype('float')/256
X_val = X_val.astype('float')/256
X_test = X_test.astype('float')/256

#3)모델 구축
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D
from keras.layers import Activation, Dropout, Dense, Flatten
model = Sequential()#100,100,3
model.add(Conv2D(32,kernel_size=3, activation='relu',padding='same',input_shape=X_train.shape[1:]))
#필터(커널)크기 = 3,3,3
#피처맵의 크기 100,100,32
model.add(MaxPool2D(2))
#풀링층의 크기 : 2,2
#풀링층을 거치고 난 후 피처맵의 크기 : 50,50,32
model.add(Dropout(0.3))

model.add(Conv2D(64,kernel_size=3, activation='relu',padding='same',input_shape=X_train.shape[1:]))
model.add(MaxPool2D(2))
model.add(Dropout(0.3))


model.add(Conv2D(128,kernel_size=3, activation='relu',padding='same',input_shape=X_train.shape[1:]))
model.add(MaxPool2D(2))
model.add(Dropout(0.3))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(n_class, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

#모델 훈련 하기
#베스트 훈련모델을 저장
checkpoint_cb = keras.callbacks.ModelCheckpoint('./best-cnn-flower.h5', save_best_only=True)

#조기 종료 조건
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

hist = model.fit(X_train, Y_train, epochs=25, validation_data=(X_val,Y_val),
    callbacks=[checkpoint_cb,early_stopping_cb], batch_size=32)


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

