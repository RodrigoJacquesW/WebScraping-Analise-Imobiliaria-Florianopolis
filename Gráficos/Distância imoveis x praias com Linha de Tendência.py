import pandas as pd
from haversine import haversine

# 📌 Carregar os dados
df_imoveis = pd.read_csv("imoveis_com_coordenadas.csv")
df_praias = pd.read_csv("25_03_11_praias_floripa.csv")

# 📌 Renomear a coluna "Nome da Praia" para evitar problemas
df_praias.rename(columns={"Nome da Praia": "nome_praia"}, inplace=True)

# 📌 Remover espaços extras e converter para string
df_imoveis["Latitude"] = df_imoveis["Latitude"].astype(str).str.strip()
df_imoveis["Longitude"] = df_imoveis["Longitude"].astype(str).str.strip()
df_praias["Latitude"] = df_praias["Latitude"].astype(str).str.strip()
df_praias["Longitude"] = df_praias["Longitude"].astype(str).str.strip()

# 📌 Remover linhas com "Erro" na Latitude ou Longitude
df_imoveis = df_imoveis[(df_imoveis["Latitude"] != "Erro") & (df_imoveis["Longitude"] != "Erro")]

# 📌 Remover linhas onde a Latitude ou Longitude não são números válidos
df_imoveis = df_imoveis[pd.to_numeric(df_imoveis["Latitude"], errors="coerce").notna()]
df_imoveis = df_imoveis[pd.to_numeric(df_imoveis["Longitude"], errors="coerce").notna()]
df_praias = df_praias[pd.to_numeric(df_praias["Latitude"], errors="coerce").notna()]
df_praias = df_praias[pd.to_numeric(df_praias["Longitude"], errors="coerce").notna()]

# 📌 Converter para float
df_imoveis["Latitude"] = df_imoveis["Latitude"].astype(float)
df_imoveis["Longitude"] = df_imoveis["Longitude"].astype(float)
df_praias["Latitude"] = df_praias["Latitude"].astype(float)
df_praias["Longitude"] = df_praias["Longitude"].astype(float)

# 📌 Função para calcular a menor distância de um imóvel até uma praia
def distancia_mais_proxima(lat, lon, praias):
    distancias = [haversine((lat, lon), (p_lat, p_lon)) for p_lat, p_lon in zip(praias["Latitude"], praias["Longitude"])]
    return min(distancias) if distancias else None  # Retorna None se não houver praias

# 📌 Criar uma cópia do dataframe original para evitar sobrescrita
df_imoveis_com_distancia = df_imoveis.copy()

# 📌 Aplicar a função para calcular a distância para cada imóvel
df_imoveis_com_distancia["distancia_praia"] = df_imoveis.apply(
    lambda row: distancia_mais_proxima(row["Latitude"], row["Longitude"], df_praias), axis=1
)

# 📌 Salvar o novo CSV sem sobrescrever o original
novo_arquivo = "imoveis_com_distancia_praia.csv"
df_imoveis_com_distancia.to_csv(novo_arquivo, index=False)

print(f"✅ Distâncias calculadas e CSV salvo como '{novo_arquivo}'!")
