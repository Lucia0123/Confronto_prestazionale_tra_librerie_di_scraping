### Confronto_prestazionale_tra_librerie_di_scraping

Per confrontare le prestazioni di bs4 e parsel vengono proposti 4 scenari, ognuno con un proprio obiettivo di scraping. Questi scenari sono pensati per essere diversificati in modo da rappresentare diverse situazioni che si incontrano in scenari reali di scraping di pagine web. In ogni scenario viene prefissato un obiettivo di scraping su una certa pagina HTML. Questo obiettivo viene raggiunto da 4 programmi equivalenti: due programmi scritti con bs4 (di cui uno che estrae dati con l'uso di filtri specifici messi a disposizione da bs4 e l'altro con l'uso di selettori CSS) e due programmi scritti con parsel (uno che fa uso dei selettori CSS, l'altro dei selettori XPATH).
In ogni soluzione/versione di ogni scenario vengono stampati in output: tempo totale di esecuzione, tempo di parsing della pagina HTML, uso di CPU e uso di RAM.

## Chi è la migliore?

20 test eseguiti per ogni versione di ogni scenario.


--- English ---

### Performance comparison between scraping libraries BeautifulSoup (bs4) and parsel in Python. Parsel wins, obviously.

To compare the performance of bs4 and parsel, four scenarios are proposed, each with its own scraping objective. These scenarios are designed to be diverse in order to represent different situations encountered in real-world web page scraping scenarios. In each scenario, a scraping objective is set for a specific HTML page. This objective is achieved by four equivalent programs: two programs written with bs4 (one of which extracts data using specific filters provided by bs4 and the other using CSS selectors) and two programs written with parsel (one using CSS selectors and the other using XPATH selectors).
In each solution for each scenario, the following are printed in the output: total execution time, HTML page parsing time, CPU usage, and RAM usage.
