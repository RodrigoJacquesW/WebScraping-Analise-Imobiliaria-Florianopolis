from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="meu_projeto_praias")  # Nome do app para evitar bloqueios

praias = [
    "Praia Mole, Florianópolis, Brasil",
    "Praia da Joaquina, Florianópolis, Brasil",
    "Praia do Campeche, Florianópolis, Brasil",
    "Praia da Barra da Lagoa, Florianópolis, Brasil",
    "Praia do Moçambique, Florianópolis, Brasil",
    "Praia dos Ingleses, Florianópolis, Brasil",
    "Praia do Santinho, Florianópolis, Brasil",
    "Praia Brava, Florianópolis, Brasil",
    "Praia do Forte, Florianópolis, Brasil",
    "Praia da Galheta, Florianópolis, Brasil",
    "Praia da Armação, Florianópolis, Brasil",
    "Praia do Pântano do Sul, Florianópolis, Brasil",
    "Praia do Matadeiro, Florianópolis, Brasil",
    "Praia da Daniela, Florianópolis, Brasil",
    "Praia do Saquinho, Florianópolis, Brasil",
    "Praia do Rio Tavares, Florianópolis, Brasil",
    "Praia da Cachoeira do Bom Jesus, Florianópolis, Brasil",
    "Praia do Naufragados, Florianópolis, Brasil",
    "Praia da Solidão, Florianópolis, Brasil"
]

coordenadas_praias = {}

for praia in praias:
    try:
        location = geolocator.geocode(praia, timeout=10)
        if location:
            coordenadas_praias[praia] = (location.latitude, location.longitude)
            print(f"{praia}: {location.latitude}, {location.longitude}")
        else:
            print(f"Não foi possível encontrar a localização de {praia}")
        time.sleep(1)  # Evita bloqueios na API gratuita
    except Exception as e:
        print(f"Erro ao buscar {praia}: {e}")

print("\nCoordenadas das praias:")
for praia, coords in coordenadas_praias.items():
    print(f"{praia}: {coords}")

import csv

with open("praias_floripa.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome da Praia", "Latitude", "Longitude"])
    
    for praia, coords in coordenadas_praias.items():
        writer.writerow([praia, coords[0], coords[1]])

print("Arquivo CSV criado com sucesso!")
