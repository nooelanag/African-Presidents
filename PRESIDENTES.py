import requests
from bs4 import BeautifulSoup

def obtener_presidente(pais):
    url = f"https://es.wikipedia.org/wiki/{pais.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        infobox = soup.find('table', {'class': 'infobox'})
        if infobox:
            rows = infobox.find_all('tr')
            for row in rows:
                header = row.find('th')
                if header and ('Presidente' in header.text or 'Presidencia' in header.text):
                    presidente = row.find('td')
                    if presidente:
                        return presidente.text.strip()
    return "No se encontró información!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

paises = [
    "Argelia", "Angola", "Benín", "Botsuana", "Burkina Faso", "Burundi",
    "Cabo Verde", "Camerún", "Chad", "Comoras", "Costa de Marfil", "Egipto",
    "Eritrea", "Esuatini", "Etiopía", "Gabón", "Gambia", "Ghana", "Guinea",
    "Guinea-Bisáu", "Guinea Ecuatorial", "Kenia", "Lesoto", "Liberia", "Libia",
    "Madagascar", "Malaui", "Malí", "Marruecos", "Mauricio", "Mauritania",
    "Mozambique", "Namibia", "Níger", "Nigeria", "República Centroafricana",
    "República del Congo", "República Democrática del Congo", "Ruanda",
    "Santo Tomé y Príncipe", "Senegal", "Seychelles", "Sierra Leona", "Somalia",
    "Sudáfrica", "Sudán", "Sudán del Sur", "Tanzania", "Togo", "Túnez",
    "Uganda", "Yibuti", "Zambia", "Zimbabue"
]

# Abre el archivo en modo escritura ('w'). Si el archivo no existe, se crea.
with open('resultados_presidentes.txt', 'w',encoding="utf-8") as file:
	file.write(f"-----------------------------------------------\n")
	for pais in paises:
		presidente = obtener_presidente(pais)		
		file.write(f"El presidente de {pais} es {presidente}.\n")
