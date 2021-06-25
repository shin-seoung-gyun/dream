#13_딥러닝_인공신경망.py
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.datasets import mnist
from keras.layers import Activation, Dense, Dropout
from keras.models import Sequential, load_model
from keras import optimizers
from keras.utils.np_utils import to_categorical

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

fig, axs = plt.subplots(1, 10, figsize=(10,10))
for i in range(10):
    axs[i].imshow(X_train[i], cmap='gray')
    axs[i].axis('off')
plt.show()


X_train.shape #(60000, 28, 28)
X_train = X_train.reshape(-1, 28*28)
X_train.shape #(60000, 784)
X_test = X_test.reshape(-1, 28*28)
X_test.shape #(10000, 784)

# X_train=X_train.reshape(X_train.shape[0],784)[:6000]
X_train
Y_train
#원핫인코딩

Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)
Y_train

model = Sequential()
model.add(Dense(256, input_shape=[X_train.shape[1]]))
model.add(Activation('sigmoid'))
model.add(Dense(128))
model.add(Activation('sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))

sgd = optimizers.gradient_descent_v2.SGD(learning_rate=0.1)
model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, Y_train, batch_size=500, epochs=30, verbose=1, validation_data=(X_test, Y_test))
history.history
plt.plot(history.history['accuracy'], label='acc', ls='-', marker='o')
plt.plot(history.history['val_accuracy'], label='val_acc', ls='-', marker='x')
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(loc='best')
plt.show()






































