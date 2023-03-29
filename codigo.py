import pandas as pd

df_gasolina = pd.read_csv('gasolina.csv')
df_gasolina.head(10)

# código de geração do gráfico

import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(data=df_gasolina, x='dia', y='venda')
plt.grid()
plt.savefig('grafico_gasolina.png')
plt.show()