import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.interpolate import *
#from matplotlib.pyplot import *
df = pd.read_csv(r'C:\\Users\\HP\\Desktop\\New folder\\dust.csv')
df = df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]

x_matrix=df.iloc[:,4:9]
y_matrix=df.iloc[:,9:10]


from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(x_matrix, y_matrix, test_size = 0.2, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
x = sc_X.fit_transform(X_Train)
y = sc_y.fit_transform(Y_Train)

# Fitting SVR to the dataset
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
#regressor = SVR(kernel = 'rbf')

#regressor = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
#regressor = SVR(kernel='linear', C=100, gamma='auto')
#regressor = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,coef0=1)
regressor = DecisionTreeRegressor()

#rbf = Gaussian Radial Basis Function Kernel
regressor.fit(x, y)

# Predicting a new result

Y_Pred = regressor.predict(X_Test)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

print(mean_absolute_error(Y_Pred,Y_Test))
print(mean_squared_error(Y_Test,Y_Pred))
print(np.sqrt(mean_squared_error(Y_Test,Y_Pred)))

print( np.mean(np.abs(( Y_Pred-Y_Test) / Y_Test)) * 100)
