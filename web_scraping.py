import requests
from bs4 import BeautifulSoup

URL = "https://old.reddit.com/r/Python/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

try:
    # Solicitamos la página con el encabezado adecuado para evitar ser bloqueados por el sitio web
    page = requests.get(URL, headers=headers, timeout=5)
    
    # Verificamos que la petición fue exitosa
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Buscamos todos los títulos de los posts. La clase puede variar, así que asegúrate de que 'title' es correcta.
        # En Reddit, las clases cambian con frecuencia. Revisa si 'title' sigue siendo válido o encuentra la clase correcta.
        titles = soup.findAll('a', class_='title')
        
        # Imprimimos los títulos encontrados, si existen
        if titles:
            for title in titles:
                print(title.text)
        else:
            print("No se encontraron títulos. Por favor, verifica si la clase 'title' sigue siendo válida.")
    else:
        print(f"Error al acceder al sitio: Estado {page.status_code}")

except requests.RequestException as e:
    print(f"Error en la solicitud: {e}")
