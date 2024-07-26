# bibliotecas
import pandas as pandas
import numpy as npp
from sklearn.linerar_model import LinearRegression
import matplotlib.pyplot as plt 

# Dados fictícios para previsão 
dias = np.array([1, 2, 3, 4, 5, 6, 7])
temperaturas = np.array([20, 23, 25, 26, 28, 29])

# DataFrame
df = pd.DataFrame({'Dia': dias, 'Temperatura': temperaturas})

# Modelo de regressão 
modelo = LinearRegression()
modelo.fit(df[['Dia']], df[['Temperatura']])

# Previsão do proximo dia 
dia_seguinte = pd.DataFrame({'Dia': [8]})
previsao = modelo.predict(dia_seguinte)

print("Previsão da temperatura do próximo dia:", previsao[0][0])

plt.scatter(dias, temperaturas, color='b')
plt.plot(df['Dia'], modelo.predict(df[['Dia']], color='g', label='Linha de tendência'))
plt.scatter(dia_seguinte, previsao, color='r', label='Previsão')
plt.xlabel('Dia')
plt.xlabel('Temperatura')
plt.legend()
plt.show()
