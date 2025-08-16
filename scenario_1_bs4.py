import requests
from bs4 import BeautifulSoup
import time
import psutil
import os

processo = psutil.Process(os.getpid())
ram_iniziale = processo.memory_info().rss / 1024 / 1024  # in MB
# rss è la resident set size, ovvero la RAM effettivamente usata dal processo nella RAM fisica

tempo_iniz_cpu = processo.cpu_times()
tempo_iniz_esec = time.time()
URL = "https://webscraper.io/test-sites/e-commerce/allinone"
response = requests.get(URL)

tempo_iniz_parsing = time.time()
soup = BeautifulSoup(response.content, "html.parser")
tempo_fin_parsing = time.time()
prodotti = soup.find_all(class_ = "product-wrapper card-body")
for prodotto in prodotti:
    nome_prodotto = prodotto.find("a", class_ = "title")["title"]
    print(nome_prodotto)

tempo_fin_esec = time.time()
tempo_esec = (tempo_fin_esec - tempo_iniz_esec)
tempo_parsing = (tempo_fin_parsing - tempo_iniz_parsing)

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
print("TEMPO DI PARSING in s: ", tempo_parsing)
print("USO MEDIO DELLA CPU IN %: ", cpu_percent)
print("RAM USATA IN MB: ", ram_usata)