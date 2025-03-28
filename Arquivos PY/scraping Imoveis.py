import requests
import pandas as pd
import time

# URL base da API
BASE_URL = "https://www.gralhaimoveis.com.br/api/anuncios/search"

# Parâmetros fixos para a busca
params = {
    "suggest": "[{\"tipoId\":0,\"tipo\":\"Cidades\",\"titulo\":\"Florianópolis - SC\",\"slug\":\"cidade+sc+florianopolis\",\"bairroId\":0,\"bairro\":null,\"cidadeId\":2,\"cidade\":\"Florianópolis\",\"estadoSigla\":\"SC\",\"empreendimento\":null,\"condominio\":null,\"agrupamentoId\":null,\"agrupamento\":null}]",
    "finalidade": "venda",
    "page": 1
}

# Fazendo a primeira requisição para descobrir o total de páginas
response = requests.get(BASE_URL, params=params)
data = response.json()
total_pages = (data["total"] // data["pagesize"]) + 1

# Lista para armazenar os dados
dados = []

# Loop para percorrer todas as páginas
for page in range(1, total_pages + 1):
    print(f"Coletando dados da página {page}/{total_pages}...")
    params["page"] = page
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        for item in data["items"]:
            url_imovel = f"https://www.gralhaimoveis.com.br/imovel/{item.get('url')}/{item.get('id')}"
            
            # Criando a coluna de endereço completo
            logradouro = item.get("logradouro", "").strip()
            numero = str(item.get("numero", "")).strip()
            bairro = item.get("bairro", "").strip()
            cidade = item.get("cidade", "").strip()
            estado = item.get("estadoSigla", "").strip()
            
            endereco_completo = f"{logradouro}, {numero}, {bairro}, {cidade}, {estado}"

            # Adicionando os dados à lista
            dados.append([
                item.get("id"), item.get("tipo"), item.get("valorVenda"), bairro,
                cidade, estado, item.get("quartos"), item.get("suites"), item.get("vagas"),
                item.get("banheiros"), item.get("areaConstruida"), endereco_completo, url_imovel
            ])
    else:
        print(f"Erro ao coletar dados na página {page}: {response.status_code}")

    time.sleep(1)  # Pequeno delay para evitar bloqueios

# Criando o DataFrame do Pandas
colunas = ["id", "tipo", "valorVenda", "bairro", "cidade", "estado",
           "quartos", "suites", "vagas", "banheiros", "areaConstruida",
           "endereco_completo", "url"]

df = pd.DataFrame(dados, columns=colunas)

# Salvando no CSV
df.to_csv("imoveis.csv", index=False, encoding="utf-8-sig")

print("✅ Dados salvos em 'imoveis.csv'!")

