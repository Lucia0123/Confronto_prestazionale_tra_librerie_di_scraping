from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options   # per usare webdriver.ChromeOp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import psutil
import os

processo = psutil.Process(os.getpid())
ram_iniziale = processo.memory_info().rss / 1024 / 1024  # in MB
# rss è la resident set size, ovvero la RAM effettivamente usata dal processo nella RAM fisica

tempo_iniz_cpu = processo.cpu_times()

tempo_iniz_esec = time.time()
URL = "https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops"

s = Service("C:/Users/lucia/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# con questa opzione, il browser rimane aperto finché non lo si chiude manualmente
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # per evitare la chiusura automatica
driver = webdriver.Chrome(service = s, options = chrome_options)
driver.get(URL)
accetta_cookies = driver.find_element(By.CLASS_NAME, "acceptCookies")
accetta_cookies.click()

bottoni = driver.find_elements(By.CLASS_NAME, "page-link")
bottoni.pop(0)
actions = ActionChains(driver)

for bottone in bottoni:
    time.sleep(3)
    # scraping delle informazioni di interesse
    pagina_html = driver.page_source
    soup = BeautifulSoup(pagina_html, "html.parser")
    laptops = soup.select(".product-wrapper.card-body")
    for l in laptops:
        laptop = {
            "nome" : l.select_one(".title")["title"],
            "prezzo" : l.select_one(".price.float-end.pull-right").text
        }
        print(laptop)

    # vado alla prossima pagina
    actions.move_to_element(bottone).perform()
    bottone.click()

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