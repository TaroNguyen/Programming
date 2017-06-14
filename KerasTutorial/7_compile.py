# Import `Sequential` from `keras.models`
from keras.models import Sequential

# Import `Dense` from `keras.layers`
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
white = pd.read_csv("../Data/Wine/winequality-white.csv",sep=";")
red = pd.read_csv("../Data/Wine/winequality-red.csv",sep=";")
white['type']=0
red['type']=1
wines=red.append(white,ignore_index='True' )#??
#specify data
X=wines.ix[:,0:11]

#specify target
y=np.ravel( wines.type)

X_train, X_test, y_train, y_test = train_test_split( X,y,test_size=0.33,random_state=42)

#Standarize data

scaler = StandardScaler().fit(X_train)  # ????
X_train= scaler.transform( X_train)
X_test= scaler.transform( X_test)


# Initialize the constructor
model = Sequential()

# Add an input layer 
model.add(Dense(12, activation='relu', input_shape=(11,)))

# Add one hidden layer 
model.add(Dense(8, activation='relu'))

# Add an output layer 
model.add(Dense(1, activation='sigmoid'))   

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
                   
model.fit(X_train, y_train,epochs=20, batch_size=1, verbose=1)
print( type(X_train))