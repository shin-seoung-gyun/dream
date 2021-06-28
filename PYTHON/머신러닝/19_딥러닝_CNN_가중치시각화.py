#합성곱층은 여러개의 필터를 사용해 이미지에서 특징을 학습
#각 필터는 커널이라 부르는 카중치와 절편을 가지고 있다.
#크게 두드러지게 표현하는 역할을 한다.

#필터 시각화 - 가중치의 시각화
from tensorflow import keras
model = keras.models.load_model('./best-cnn-model.h5')
model.summary()

conv = model.layers[0]#첫번째 층을 가져옴 Conv2d
conv.weights
# [<tf.Variable 'conv2d/kernel:0' 
# shape=(3, 3, 1, 32) dtype=float32, numpy=

conv.weights[0].shape#TensorShape([3, 3, 1, 32]) 커널크기(3,3) 깊이1(채널수) 필터개수
conv.weights[1].shape#TensorShape([32]) 필터마다의 절편값

#가중치들의 평균값과 표준편차값
conv_weights = conv.weights[0].numpy()
conv_weights.mean(), conv_weights.std()
# (-0.003912815, 0.20979364)

#모든 가중치 - 히스토그램 시각화
import matplotlib.pyplot as plt
plt.hist(conv_weights.reshape(-1,1))
plt.xlabel(('weights'))
plt.ylabel('count')
plt.show()
#종모양

##훈련하지 않은 모델과 비교
no_training_model = keras.Sequential()
no_training_model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same', input_shape=(28,28,1)))

no_training_conv = no_training_model.layers[0]
no_training_conv.weights[0].shape#가중치
no_training_conv.weights[1].shape#절편
no_training_weights= no_training_conv.weights[0].numpy()
no_training_weights.mean(), no_training_weights.std()
# (-0.005335096, 0.08483233)

plt.hist(no_training_weights.reshape(-1,1))
plt.xlabel(('weights'))
plt.ylabel('count')
plt.show()

#텐서플로가 신경망의 가중치를 초기화 할때 균일분포에서 랜덤하게 값을 선택

#---------------------------------------------------------------------------------------------------------------------
#커널 시각화-훈련한 모델
fig, axs = plt.subplots(2,16, figsize=(15,2))
for i in range(2):
    for j in range(16):
        axs[i,j].imshow(conv_weights[:,:,0,i*16+j], vmin=-0.5, vmax=0.5)
        axs[i,j].axis('off')
plt.show()

#커널 시각화-훈련하지 않은 모델
fig, axs = plt.subplots(2,16, figsize=(15,2))
for i in range(2):
    for j in range(16):
        axs[i,j].imshow(no_training_weights[:,:,0,i*16+j], vmin=-0.5, vmax=0.5)
        axs[i,j].axis('off')
plt.show()

#---------------------------------------------------------------------------------------------------------------------
#특성맵 시각화
model.input #인풋 데이터의 크기가 보여짐

#layer0의 출력 결과 얻기
conv_acti = keras.Model(model.input, model.layers[0].output)
(X_train, Y_train), (X_test, Y_test) = keras.datasets.fashion_mnist.load_data()
plt.imshow(X_train[0], cmap='gray_r')
plt.show()#첫데이터 나이키 신발

inputData = X_train[0:1]
inputData.shape#(1, 28, 28)
inputData=inputData.reshape(-1,28,28,1)/255.0
inputData.shape#(1, 28, 28, 1)
feature_maps = conv_acti.predict(inputData)
feature_maps.shape#(1, 28, 28, 32)


fig, axs = plt.subplots(4,8, figsize=(15,8))
for i in range(4):
    for j in range(8):
        axs[i,j].imshow(feature_maps[0,:,:,i*8+j])
        axs[i,j].axis('off')
plt.show()

#두번째 합성 곱 층의 시각화
conv2_acti = keras.Model(model.input, model.layers[2].output)
feature_maps = conv2_acti.predict(inputData)
feature_maps.shape#(1, 14, 14, 64)

fig, axs = plt.subplots(8,8, figsize=(12,12))
for i in range(8):
    for j in range(8):
        axs[i,j].imshow(feature_maps[0,:,:,i*8+j])
        axs[i,j].axis('off')
plt.show()

#첫번째 층은 시각적인 정보(대각선, 곡선, 형태등)를 감지하고 두번째 층이상은 시각적인 정보를 바탕으로 추상적인 정보 학습.




