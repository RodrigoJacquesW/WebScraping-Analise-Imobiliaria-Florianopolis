import requests
import pandas as pd
import time

# API de geocodificação
API_URL = "https://geocode.maps.co/search"
API_KEY = "SUA KEY"

# Carregar o CSV gerado
df = pd.read_csv("25_03_19_imoveis.csv")

# Criar colunas para latitude e longitude
df["Latitude"] = None
df["Longitude"] = None

# Loop para buscar coordenadas
for i, endereco in enumerate(df["endereco_completo"]):
    if pd.isna(endereco):  # Ignorar células vazias
        continue

    # Montar URL da API
    url = f"{API_URL}?q={endereco}&api_key={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # Se houver resultados, pega a primeira opção
        if data and isinstance(data, list) and "lat" in data[0] and "lon" in data[0]:
            df.at[i, "Latitude"] = data[0]["lat"]
            df.at[i, "Longitude"] = data[0]["lon"]
        else:
            df.at[i, "Latitude"] = "Erro"
            df.at[i, "Longitude"] = "Erro"

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar {endereco}: {e}")
        df.at[i, "Latitude"] = "Falha"
        df.at[i, "Longitude"] = "Falha"

    # Pausa de 1 segundo para evitar bloqueios
    time.sleep(1)

# Salvar no CSV atualizado
df.to_csv("imoveis_com_coordenadas.csv", index=False, encoding="utf-8-sig")

print("✅ Dados com coordenadas salvos em 'imoveis_com_coordenadas.csv'!")
