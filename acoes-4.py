import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

dias = np.array([1, 2, 3, 4, 5, 6, 7])
valores = np.array([30, 25, 32, 28, 33, 27, 31])

df =pd.DataFrame({'Dias': dias, 'Valores': valores})

modelo = LinearRegression()
modelo.fit(df[['Dias']], df[['Valores']])

dia_seguite = np.array([[8]])
previsao = modelo.predict(dia_seguite)

print(f'Previsão do valor para o dia seguinte é de: {previsao[0][0]}')

dias = np.append(dias, dia_seguite)
valores = np.append(valores, previsao[0][0])

plt.scatter(dias, valores, color='b')
plt.plot(dias, valores, color='r')
plt.xlabel('Dias')
plt.ylabel('Valores')
plt.show()
