import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split


X, y = load_boston(return_X_y=True)
X = pd.DataFrame(X, columns=load_boston().feature_names)


x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.1)

model = LinearRegression()
model.fit(x_train, y_train)


accuracy = round( model.score(x_test, y_test ) * 100, 2)
print( 'The accuracy of the model is '+ str(accuracy)+'%')

