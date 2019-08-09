from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
import matplotlib.pyplot as plt
from keras.applications.resnet50 import ResNet50
from keras.utils import to_categorical 

(x_train,y_train),(x_test,y_test)=ResNet50.load_data()
row,col=x_train.shape
x_train=x_train.reshape(1500,row,col,1)
y_train=y_train.reshape(1500,row,col,1)

y_train=to_categorical(y_train)
y_test=to_categorical(y_test)

model=Sequential()
model.add(Conv2D(64,kernal_size=3,activation='relu',input_shape=(row,col,1)))
model.add(Conv2D(32,kernal_size=3,activation='relu'))
model.add(Flatten())
model.add(Dense(10,activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])