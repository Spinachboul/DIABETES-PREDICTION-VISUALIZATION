import matplotlib
matplotlib.use("TkAgg")
from utils import preprocess
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from keras.layers import Dense
from keras.models import Sequential
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(16)

try:
    df = pd.read_csv("diabetes.csv")
except:
    print("Dataset not found in the computer")
    quit()


## Preprocessing and feature engineering
df = preprocess(df)


# Splitting the data into training and testing sets
X = df.loc[:, df.columns != 'Outcome']
y = df.loc[:, 'Outcome']
X_train, X_test, y_train, y_test = tts(X, y, test_size=0.25, random_state=0)


# Building the neural network
model = Sequential()
model.add(Dense(32, activation='relu', input_dim = 8))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer = 'adam', loss = 'binary_crossentropy',metrics = ['accuracy'])
model.fit(X_train, y_train, epochs=200, verbose= False)


# Results (Accuracy)
scores = model.evaluate(X_train, y_train, verbose = False)
print("Training Accuracy: %.2f%%\n" % (scores[1]*100))
scores = model.evaluate(X_test, y_test, verbose = False)
print("Training Accuracy: %.2f%%\n" % (scores[1]*100))



## Results in the form of confusion matrix
y_test_pred = model.predict_classes(X_test)
c_matrix = confusion_matrix(y_test, y_test_pred)
ax = sns.heatmap(c_matrix, annot=True, xticklabels=["No Diabetes", "Diabetes"], yticklabels= ["No Diabetes", "Diabetes"], cbar = False, cmap = "Blues")

ax.set_xlabel("Prediction")
ax.set_ylabel("Actual")
plt.show()
plt.clf()


# Results - ROC Curve
y_test_pred_probs = model.predict(X_test)
FPR, TPR, _ = roc_curve(y_test, y_test_pred_probs)
plt.plot(FPR, TPR)
plt.plot([0,1],[0,1],'--', color='black') #diagonal line
plt.title('ROC Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()
plt.clf()

