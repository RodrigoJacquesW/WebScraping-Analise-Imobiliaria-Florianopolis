import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
df = pd.read_csv("imoveis_com_distancia_praia.csv")

# Filtrar apenas os apartamentos
df_apartamentos = df[df["tipo"] == "Apartamento"]

# Calcular o preço por m² (dividindo o valor de venda pela área construída)
df_apartamentos["preco_por_m2"] = df_apartamentos["valorVenda"] / df_apartamentos["areaConstruida"]

# Configuração do estilo do gráfico
sns.set(style="whitegrid")

# Criar o gráfico com a linha de tendência
plt.figure(figsize=(10, 6))
sns.regplot(x="distancia_praia", y="preco_por_m2", data=df_apartamentos, scatter_kws={'alpha':0.5, 'color':'blue'}, line_kws={'color':'red'})

# Adicionar título e rótulos aos eixos
plt.title('Relação entre Distância da Praia e Preço por m² dos Apartamentos', fontsize=16)
plt.xlabel('Distância da Praia (km)', fontsize=12)
plt.ylabel('Preço por m² (R$)', fontsize=12)

# Mostrar o gráfico
plt.tight_layout()
plt.show()
