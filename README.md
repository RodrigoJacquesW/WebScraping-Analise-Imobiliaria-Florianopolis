# 🏨 Web Scraping Análise Imobiliária De Florianópolis
![Mapa de Calor](https://github.com/RodrigoJacquesW/WebScraping-Analise-Imobiliaria-Florianopolis/blob/main/Gráficos/Mapa%20de%20calor%20R%24%20por%20M²%20Apartamentos%20Florianópolis.PNG)
## 💻 Sobre o Projeto
Este projeto coleta informações de sites sobre imóveis em Florianópolis para desenvolver análises de valorização imobiliária. Utilizei web scraping para extrair dados do site Gralha Imóveis, gerei coordenadas geográficas a partir dos endereços e obtive a localização das praias da cidade. Com essas informações, calculei a distância de cada imóvel até a praia mais próxima e criei visualizações para identificar padrões de valorização. Além disso, desenvolvi um gráfico para analisar quais regiões possuem o metro quadrado mais caro da cidade. Vale ressaltar que o projeto coleta informações de diferentes tipologias de imóveis, como terrenos, coberturas e hotéis. No entanto, para esta análise, consideramos apenas os imóveis classificados como apartamentos.

## 📊 Web Scrapping
Para coletar as informações dos imóveis, foi desenvolvido um código em Python utilizando as bibliotecas Pandas e Requests. Esse código extrai dados como ID, tipo, valor de venda, bairro, cidade, estado, número de quartos, suítes, vagas, banheiros, área construída, endereço completo e URL. Como o web scraping não retorna coordenadas geográficas, utilizei a API do Geocode para obter a latitude e longitude dos imóveis, informações essenciais para as análises posteriores. 

Para obter a localização exata das praias de Florianópolis, foi gerada uma lista com auxílio de inteligência artificial e utilizada a biblioteca geopy.geocoders do Python para obter suas coordenadas geográficas.

## 📈 Preço Médio x Distância até as praias
Para calcular a distância entre os imóveis e a praia mais próxima, foi utilizado o método de Haversine, que mede a distância entre duas coordenadas geográficas. Primeiramente, os dados dos imóveis e das praias foram carregados e tratados, removendo inconsistências, como valores inválidos de latitude e longitude. Em seguida, foi aplicada uma função que calcula a menor distância entre cada imóvel e todas as praias registradas. O resultado foi salvo em um novo arquivo CSV, adicionando a coluna "distancia_praia" ao dataset original.

Para analisar a relação entre o preço médio do metro quadrado e a distância até a praia, foi criado um gráfico de dispersão, onde cada ponto representa um imóvel. Além disso, foi adicionada uma linha de regressão para identificar a tendência geral dos preços. O resultado mostra uma relação negativa, indicando que, em média, imóveis mais próximos da praia tendem a ter um valor por metro quadrado mais alto, enquanto os mais distantes apresentam preços menores. Essa análise ajuda a visualizar o impacto da proximidade com o mar na valorização imobiliária em Florianópolis.
![Gráfico Preço Médio x Distância](https://github.com/RodrigoJacquesW/WebScraping-Analise-Imobiliaria-Florianopolis/blob/main/Gráficos/Gráfico%20de%20Preço%20médio%20x%20distância%20Praia%20com%20linha%20de%20regressão%20Linear.png)

Embora a amostra não seja extremamente extensa, a linha de tendência reforça que, naturalmente, os imóveis localizados mais próximos das praias possuem um valor de metro quadrado mais elevado. Essa valorização pode ser explicada por diversos fatores, como:
-Valorização da Vista e Localização: Imóveis próximos ao mar oferecem vistas privilegiadas, fator que agrega valor significativo.
-Turismo e Demanda: Florianópolis é um destino turístico, aumentando a procura por imóveis perto das praias.
-Infraestrutura e Serviços: Áreas litorâneas costumam ter boa infraestrutura, como restaurantes, comércios e lazer.
-Oferta Limitada de Terrenos: A proximidade com o mar reduz a disponibilidade de terrenos, elevando os preços.
-Status e Exclusividade: Morar perto da praia é um diferencial desejado por muitas pessoas, aumentando a demanda.
-Acessibilidade e Transporte: Regiões valorizadas geralmente possuem melhor acesso a transporte público e vias estruturadas.

## 🌆 Preço Médio por Bairros
![Gráfico Preço Médio por Bairro](https://github.com/RodrigoJacquesW/WebScraping-Analise-Imobiliaria-Florianopolis/blob/main/Gráficos/Gráfio%20de%20R%24%20por%20M²%20Florianópolis.PNG)
Para aprofundar a análise imobiliária, foi criado um painel no Power BI que exibe o preço médio por metro quadrado em cada bairro de Florianópolis. Através desse painel, é possível visualizar e comparar os valores médios das diferentes regiões da cidade, identificando quais bairros possuem imóveis mais valorizados. Além disso, o usuário pode filtrar por tipologia, como apartamentos, coberturas e terrenos, permitindo uma análise mais segmentada. Outra funcionalidade do painel é a exibição do número de unidades avaliadas por bairro, o que ajuda a entender o volume de dados considerados em cada região, tornando a análise mais transparente e informativa.

É importante ressaltar que esta é uma análise preliminar e que pode ser aprimorada com a inclusão de mais variáveis, considerando que o mercado imobiliário de Florianópolis é bastante complexo.

# Sobre os arquivos

## Ferramentas Utilizadas
Power BI
Python com as bibliotecas: 
  geopy.geocoders
  Pandas
  Requests
  matplotlib.pyplot
  seaborn
  haversine
## Ideias de complementações
Incluir fatores que influenciam o mercado imobiliário: Incorporar dados como IDH dos bairros, acessibilidade e transporte público para entender melhor a valorização dos imóveis.
Analisar outras tipologias: Expandir a análise para coberturas, terrenos e casas, verificando se o comportamento dos preços segue o mesmo padrão dos apartamentos.
Relacionar padrões construtivos com os preços: Investigar se características como padrão de acabamento, idade do imóvel e infraestrutura influenciam os valores em diferentes regiões.

