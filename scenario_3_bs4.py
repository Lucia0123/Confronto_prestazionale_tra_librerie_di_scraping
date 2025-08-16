import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import psutil
import os

processo = psutil.Process(os.getpid())
ram_iniziale = processo.memory_info().rss / 1024 / 1024  # in MB
# rss è la resident set size, ovvero la RAM effettivamente usata dal processo nella RAM fisica

tempo_iniz_cpu = processo.cpu_times()
tempo_iniz_esec = time.time()
base_url = "https://books.toscrape.com/catalogue/"
current_url = "https://books.toscrape.com/catalogue/page-1.html"
while current_url:
    # visito la pagina corrente
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # qui estraggo i dati dalla pagina corrente
    libri = soup.find("ol", class_ = "row").find_all("li")
    for l in libri:
        libro = {
            "titolo" : l.find("h3").find("a")["title"],
            "prezzo" : l.find(class_ = "price_color").text
        }
        print(libro)

    # trovo il link alla prossima pagina
    bottone_next = soup.find("li", class_ = "next")
    if bottone_next:
        current_url = urljoin(base_url, bottone_next.find("a")["href"])
    else:
        current_url = None

tempo_fin_esec = time.time()
tempo_esec = (tempo_fin_esec - tempo_iniz_esec)

# Misura CPU e RAM finali
tempo_fin_cpu = processo.cpu_times()
ram_finale = processo.memory_info().rss / 1024 / 1024  # in MB

# Calcolo uso CPU utente + sistema
tempo_cpu_utente = tempo_fin_cpu.user - tempo_iniz_cpu.user
tempo_cpu_sistema = tempo_fin_cpu.system - tempo_iniz_cpu.system
cpu_time_total = tempo_cpu_utente + tempo_cpu_sistema

# Uso medio di CPU in %
cpu_percent = (cpu_time_total / (tempo_fin_esec - tempo_iniz_esec)) * 100
ram_usata = ram_finale - ram_iniziale

# stampa delle misurazioni
print("TEMPO DI ESECUZIONE in s: ", tempo_esec)
print("USO MEDIO DELLA CPU IN %: ", cpu_percent)
print("RAM USATA IN MB: ", ram_usata)