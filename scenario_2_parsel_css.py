import requests
from parsel import Selector
import time
import psutil
import os

def ottieni_e_pulisci_stringa(s: Selector):
    stringa = s.css("::text").get().replace("\n", "").replace("\xa0", "")
    return stringa

processo = psutil.Process(os.getpid())
ram_iniziale = processo.memory_info().rss / 1024 / 1024  # in MB
# rss è la resident set size, ovvero la RAM effettivamente usata dal processo nella RAM fisica

tempo_iniz_cpu = processo.cpu_times()
tempo_iniz_esec = time.time()
URL = "https://it.wikipedia.org/wiki/Citt%C3%A0_del_mondo_per_popolazione"
response = requests.get(URL)

tempo_iniz_parsing = time.time()
selector = Selector(response.text)
tempo_fin_parsing = time.time()

corpo_tabella = selector.css("tbody")[0]
righe = corpo_tabella.css("tr")
righe.pop(0)    # la prima riga è quella che contiene i titoli, non mi serve quindi la rimuovo dalla lista di righe
for riga in righe:
    tds = riga.css("td")
    dati = {
        "citta": ottieni_e_pulisci_stringa(tds[1]),
        "popolazione": ottieni_e_pulisci_stringa(tds[2]),
        "paese": ottieni_e_pulisci_stringa(tds[6].css("a"))
        }
    print(dati)

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