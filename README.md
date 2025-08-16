### Confronto_prestazionale_tra_librerie_di_scraping

Per confrontare le prestazioni di bs4 e parsel vengono proposti 4 scenari, ognuno con un proprio obiettivo di scraping. Questi scenari sono pensati per essere diversificati in modo da rappresentare diverse situazioni che si incontrano in scenari reali di scraping di pagine web. In ogni scenario viene prefissato un obiettivo di scraping su una certa pagina HTML. Questo obiettivo viene raggiunto da 4 programmi equivalenti: due programmi scritti con bs4 (di cui uno che estrae dati con l'uso di filtri specifici messi a disposizione da bs4 e l'altro con l'uso di selettori CSS) e due programmi scritti con parsel (uno che fa uso dei selettori CSS, l'altro dei selettori XPATH).
In ogni soluzione/versione di ogni scenario vengono stampati in output: tempo totale di esecuzione, tempo di parsing della pagina HTML, uso di CPU e uso di RAM.

## Chi è la migliore?

5 test eseguiti per ogni versione di ogni scenario.

# Scenario 1:

<img width="638" height="562" alt="image" src="https://github.com/user-attachments/assets/e4801cbd-f46f-4f26-acfb-5bef4a7f9d84" />

<img width="647" height="227" alt="image" src="https://github.com/user-attachments/assets/041f99a0-b753-4a97-be66-51f278bd4476" />

# Scenario 2:

<img width="635" height="561" alt="image" src="https://github.com/user-attachments/assets/806b089b-7b03-477d-8357-ea611c398748" />

<img width="628" height="216" alt="image" src="https://github.com/user-attachments/assets/73526e10-9b5d-436f-a987-6d2ec2b99f3e" />

# Scenario 3

<img width="627" height="517" alt="image" src="https://github.com/user-attachments/assets/bdb5b56c-d976-408f-8cd3-71b35ae0d8d3" />

<img width="632" height="178" alt="image" src="https://github.com/user-attachments/assets/7305fcec-a6a9-48b8-856b-9610a3141d8b" />

# Scenario 4

<img width="637" height="521" alt="image" src="https://github.com/user-attachments/assets/65053752-89c5-42e6-8d3a-6d1dfa178a1f" />

<img width="632" height="177" alt="image" src="https://github.com/user-attachments/assets/72886ca8-3c4d-4b93-8220-5fc032586e6c" />


--- English ---

### Performance comparison between scraping libraries BeautifulSoup (bs4) and parsel in Python. Parsel wins, obviously.

To compare the performance of bs4 and parsel, four scenarios are proposed, each with its own scraping objective. These scenarios are designed to be diverse in order to represent different situations encountered in real-world web page scraping scenarios. In each scenario, a scraping objective is set for a specific HTML page. This objective is achieved by four equivalent programs: two programs written with bs4 (one of which extracts data using specific filters provided by bs4 and the other using CSS selectors) and two programs written with parsel (one using CSS selectors and the other using XPATH selectors).
In each solution for each scenario, the following are printed in the output: total execution time, HTML page parsing time, CPU usage, and RAM usage.
