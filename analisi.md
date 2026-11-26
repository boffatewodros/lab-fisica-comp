1.1 Diffusione
la posizione media non è esattamente zero ma oscilla intorno ad esso, perché il numero di camminatori è finito. Le fluttuazioni sono dell'ordine di sqrt(t/nwalks).

Dal grafico in scala log-log si osserva che l'MSD cresce linearmente con il tempo, infatti la pendenza è circa 1. Dal fit lineare ricavo D dividendo la pendenza per 2. valore teorico atteso è 0.5.

1.2 Distribuzione delle posizioni
dopo un numero pari di passi vengono occupate solamente le posizioni pari, mentre dopo un numero dispari di passi quelle dispari.

La distribuzione non coincide esattamente con la gaussiana perché il random walk assume valori discreti invece che continui. dopo 10 passi si ha una buona approssimazione, che migliora aumentando il numero di passi. 

2.1 Dal moto balistico alla diffusione
per tempi piccoli la particella mantiene circa la sua velocità iniziale e l'MSD cresce come t^2, con pendenza 2 nel grafico log-log

Per tempi grandi la particella perde memoria della velocità iniziale e il moto diventa diffusivo, con pendenza circa 1. passaggio tra i due regimi avviene intorno a t = 2.

Dal fit lineare, escludo i tempi iniziali, ricavo i coefficienti di diffusione. I valori teorici sono rispettivamente 1, 0.5, 2 e 2. Aumentando gamma la diffusione diminuisce, mentre aumentando kT la diffusione aumenta.
2.2 Confronto tra i due modelli
nel random walk non è presente il regime balistico perché ogni passo è casuale e indipendente dal precedente.
nel modello di Langevin invece la particella all'inizio mantiene circa la sua velocità. 
Con gamma = 1 e kT = 1 abbiamo D = 1. 