from keras.layers.core import Dropout
import pandas as pd

data_df = pd.read_csv('./data/육군신체측정정보.csv', encoding='ANSI')
data_df.head()
data_df.info()

X = data_df.iloc[:,3:-1]
X['허리 둘레 센티미터'] = X['허리 둘레 센티미터'].apply(lambda x : float(str(x).split('(')[0]))
X.head()
X.info()
Y=data_df.iloc[:,-1]
Y.head()

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y ,test_size=0.3, random_state=1)

#데이터 정규화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train)
X_train_scaled = ss.transform(X_train)
X_test_scaled = ss.transform(X_test)


(X.shape[1],)
from tensorflow import keras
from keras.layers import Dense
model = keras.Sequential()
model.add(Dense(100, activation='relu', input_shape=(X.shape[1],)))
model.add(Dropout(0.4))
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(30, activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(1))#출력층

model.compile(optimizer='adam', loss='mse', metrics=['mse'])
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
hist = model.fit(X_train_scaled, Y_train, epochs=30, validation_split=0.25, callbacks=
                    [early_stop])

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,8))
plt.title("loss history")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.plot(hist.history['loss'], 'red')
plt.plot(hist.history['val_loss'], 'blue')
plt.show()

model.evaluate(X_test_scaled, Y_test)#[36.58478546142578, 36.58478546142578]
pred = model.predict(X_test_scaled)
pred[:10]
Y_test[:10]











































