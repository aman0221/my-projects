import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.interpolate import *
#from matplotlib.pyplot import *
df = pd.read_csv(r'C:\\Users\\HP\\Desktop\\New folder\\dust.csv')
df = df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]

x_matrix=df.iloc[:,4:9]
x_matrix['Temp         (Deg C)']=x_matrix['Temp         (Deg C)']-np.mean(x_matrix['Temp         (Deg C)'])
x_matrix['R Humidity      (%)']=x_matrix['R Humidity      (%)']-np.mean(x_matrix['R Humidity      (%)'])
x_matrix['B Pressure       (milli bar)']=x_matrix['B Pressure       (milli bar)']-np.mean(x_matrix['B Pressure       (milli bar)'])
x_matrix['W Direction       (Deg)']=x_matrix['W Direction       (Deg)']-np.mean(x_matrix['W Direction       (Deg)'])
x_matrix['Wind Spd      (m/s)']=x_matrix['Wind Spd      (m/s)']-np.mean(x_matrix['Wind Spd      (m/s)'])
y_matrix=df.iloc[:,9:10]


from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(x_matrix, y_matrix, test_size = 0.2, random_state = 0)

reg = LinearRegression()
reg.fit(X_Train,Y_Train)
print(reg.coef_,reg.intercept_)

Y_Pred = reg.predict(X_Test)

#accuracy = reg.score(X_Test,Y_Test)
#print(accuracy,'%')
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

print(mean_absolute_error(Y_Pred,Y_Test))
print(mean_squared_error(Y_Test,Y_Pred))
print(np.sqrt(mean_squared_error(Y_Test,Y_Pred)))

print( np.mean(np.abs(( Y_Pred-Y_Test) / Y_Test)) * 100)
