# CP6 · Examen blanc de la partie VI (M25a, M25b, M26, M27 et M28)

| | |
|---|---|
| **Durée** | 111 minutes (environ 2 heures), d'une traite |
| **Note** | sur 20 : un point par minute prévue (111 points en tout), puis ton total multiplié par $\frac{20}{111}$ (divisé par 5,55) |
| **Chapitres** | M25a, M25b, M26, M27 et M28 : gaussienne multivariée, conditionnement et divergence KL ; variables latentes, mélanges, EM et ELBO ; chaînes de Markov et équation de Bellman ; jeux à somme nulle et distances entre lois ; matrice de Gram, montée sur l'entrée et lois tronquées |
| **Ta copie** | `04_mes_reponses.md` (dans `mon_travail/checkpoints/partie_6/`), ou une feuille de papier |
| **Après** | le notebook `02_examen_notebook.ipynb` vérifie tes réponses chiffrées ; le quiz CP6.Q1, la démonstration CP6.8, les corrections de CP6.9 b) et les justifications « sur ta copie » se notent avec le corrigé `03_examen_corrige.md`, qui donne aussi le barème et la remédiation |

## Règles

- **Fiches, notes, flashcards, annexes et corrigés fermés.** Pas d'assistant IA, pas de recherche sur le web.
- **Calculatrice autorisée**, ou Python comme simple calculatrice (`+`, `*`, `/`, `**`, `math.sqrt`, `math.exp`, `math.log`, `math.sin`, `math.cos`, `math.acos`, `math.degrees`) ; ni NumPy, ni SciPy, ni SymPy, ni `mymath`, ni les notebooks des chapitres.
- **Décimales.** Quand la colonne « Réponse attendue » dit « valeur exacte », la réponse est un nombre décimal qui n'a que quelques décimales : donne-les toutes, sans arrondir. Quand elle dit « 4 décimales » (ou 3, ou 2), arrondis à ce nombre de décimales, et **à la fin** du calcul seulement : enchaîne les calculs à la calculatrice, ou garde au moins 6 chiffres significatifs dans les résultats intermédiaires (4 décimales ne suffisent pas sous une racine carrée, dans un logarithme, dans une exponentielle ou avant une soustraction).
- Écris ta démarche : une partie des points d'une question de calcul va à la méthode. Quand une question dit « justifie », une réponse sans justification ne rapporte qu'une partie des points.
- Les durées sont indicatives : commence par ce que tu sais faire ; si tu bloques, passe à la question suivante et reviens-y à la fin.

**Barème.** Chaque question vaut autant de points que de minutes prévues, et ces points sont partagés également entre ses sous-questions (ou ses affirmations, ou ses étapes). L'examen compte donc 111 points, et ta note sur 20 est ton total multiplié par $\frac{20}{111}$ (c'est-à-dire divisé par 5,55) : chaque question pèse dans la note en proportion de sa durée. Le poids de chaque sous-question est donné dans le titre de la question (ou entre crochets pour CP6.8 et CP6.9) ; une justification demandée « sur ta copie » compte dans les points de la sous-question à laquelle elle se rattache.

| Question | Type | Sujet | Points | ⏱️ |
|---|---|---|---|---|
| CP6.Q1 | 🧠 | Dix affirmations sur la partie VI, deux par chapitre : vrai ou faux | 10 | 10 min |
| CP6.1 | ✏️ | Un vecteur gaussien de dimension 2 : loi marginale, loi conditionnelle, et la loi de μ + Lε | 10 | 10 min |
| CP6.2 | ✏️ | La divergence KL entre deux gaussiennes de dimension 2, et une interpolation sphérique | 9 | 9 min |
| CP6.3 | ✏️ | Un mélange de deux gaussiennes de variances connues et trois mesures : responsabilités, un pas d'EM sur le poids et les moyennes, et l'écart à l'ELBO d'une affectation dure | 10 | 10 min |
| CP6.4 | ✏️ | Une chaîne de Markov à trois états : loi à deux pas, et la valeur d'une politique fixée par le système de Bellman, quand une ligne finit | 9 | 9 min |
| CP6.5 | ✏️ | Un jeu à somme nulle 2 × 2 en stratégies mixtes, et W₁ entre deux petits échantillons de même taille | 9 | 9 min |
| CP6.6 | ✏️ | Des distances aux positions : double centrage, matrice de Gram, et une configuration à une isométrie près | 8 | 8 min |
| CP6.7 | ✏️ | La distance de Fréchet de deux gaussiennes du plan de covariances proportionnelles, et le biais de la distance entre deux moyennes estimées | 9 | 9 min |
| CP6.8 | ∂ | Une démonstration au choix : l'entropie d'une loi tempérée croît avec la température, ou la loi de Boltzmann minimise l'énergie libre | 12 | 12 min |
| CP6.9 | 🐛 | Corriger une copie : cinq erreurs, une par chapitre | 9 | 9 min |
| CP6.10 | 🔗 | Problème de synthèse : une file d'attente à trois états suivie de façon gloutonne, puis échantillonnée après la troncature top-p de ses transitions : lois conditionnelles, coût en KL et nouvelle loi stationnaire | 16 | 16 min |
| | | **Total** (note sur 20 = total × 20/111) | **111** | **111 min** |

**Conventions de la partie VI.**
- **Gaussiennes.** Les vecteurs sont des colonnes ; $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ a pour second paramètre une **covariance** (une variance en dimension 1, jamais un écart-type). Le facteur de Cholesky $\mathbf{L}$ de $\boldsymbol{\Sigma}$ est triangulaire inférieur, de diagonale positive, avec $\mathbf{L}\mathbf{L}^\top = \boldsymbol{\Sigma}$, et un tirage s'écrit $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ avec $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$. $\ln$ est le logarithme népérien : les KL, les entropies et les informations sont en **nats**, et $\mathrm{KL}(p \,\|\, q) = \mathbb{E}_{p}[\ln p - \ln q]$ (l'espérance sous la **première** loi). $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ; t)$ est l'interpolation sphérique de M25a §8 ($\mathbf{u}$ en $t = 0$, $\mathbf{v}$ en $t = 1$), et $\Omega$ l'angle de $\mathbf{u}$ et $\mathbf{v}$.
- **Mélanges.** Les composantes sont numérotées 1 et 2, de poids $\pi_k$ ; la responsabilité $r_{ik} = P(z_i = k \mid x_i)$ est calculée avec les paramètres du moment ; un pas d'EM est un pas E puis un pas M ; l'ELBO d'une loi $q$ sur les latents est $\mathbb{E}_q[\ln p(\mathbf{x}, \mathbf{z}) - \ln q(\mathbf{z})]$, sommée sur les mesures.
- **Chaînes.** Convention **ligne** : la loi est une ligne, $\boldsymbol{\mu}_{t+1} = \boldsymbol{\mu}_t\mathbf{P}$ ; $p_{ij} = P(S_{t+1} = j \mid S_t = i)$ ; les états sont numérotés à partir de 0 ; une ligne de somme plus petite que 1 dit que le processus peut finir après cet état (la masse manquante est la probabilité de finir). Les récompenses et les valeurs sont des colonnes, $\mathbf{V} = \mathbf{r} + \gamma\mathbf{P}\mathbf{V}$, et $\gamma = 1$ est permis quand la fin est sûre.
- **Jeux.** $\mathbf{G} = (g_{ij})$ donne ce que gagne le joueur des lignes (qui maximise) et ce que paie le joueur des colonnes (qui minimise) ; dans un jeu $2 \times 2$, $p$ et $q$ sont les probabilités de la première ligne et de la première colonne, $p^\star$ et $q^\star$ leurs valeurs optimales. La descente-montée alternée met à jour $x$ d'abord, puis $y$ avec le nouveau $x$ (M27 §4).
- **Distances entre lois.** $W_p$ est la distance de Wasserstein (et $W_p^p$ le coût minimal) ; la distance de Fréchet de deux gaussiennes est leur $W_2$ ; JS est en nats.
- **Matrices de Gram.** Les points sont les lignes de $\mathbf{X}$ et $\mathbf{G} = \mathbf{X}\mathbf{X}^\top$ (la même lettre que la matrice des gains : chaque exercice n'emploie que l'une des deux) ; $\mathbf{D}^{(2)}$ est la matrice des **carrés** des distances et $\mathbf{J} = \mathbf{I} - \frac1n\mathbf{1}\mathbf{1}^\top$.
- **Lois tronquées.** Une loi est un vecteur de probabilités ; entre deux probabilités égales, le plus petit état passe d'abord ; le top-p de seuil $m$ prend les issues par probabilité décroissante, une à une, jusqu'à ce que leur masse $P(S)$ atteigne $m$, et la loi tronquée est la loi conditionnelle sur $S$.
- **Listes.** Une réponse en liste se donne dans l'ordre de la question : les coordonnées ou les états dans l'ordre de leurs numéros, et les éléments annoncés par « puis » dans cet ordre. Quand l'ordre ne compte pas, la question le dit (« dans n'importe quel ordre »).
- Dans le notebook, tu recopies chaque réponse comme sur ta copie, après sa lettre : une matrice comme la liste de ses **lignes**, une fraction irréductible telle quelle, comme `3/8`.
- Dans les tableaux, « données 1 », « données 2 » renvoient aux situations numérotées au-dessus du tableau.

---

### CP6.Q1 — Dix affirmations sur la partie VI, deux par chapitre : vrai ou faux 🧠 ★ ⏱️ 10 min · 10 points (1 par affirmation)

Pour chaque affirmation, réponds **Vrai** ou **Faux**, puis justifie en une phrase : une règle ou un contre-exemple suffit, sans calcul (un calcul juste compte, mais ne rapporte rien de plus). Chaque affirmation vaut 1 point : 0,4 pour le verdict, 0,6 pour la justification. Ce quiz se note avec le corrigé.

a) Une chaîne de Markov part de sa loi stationnaire : $S_0$ suit $\boldsymbol{\pi}$. Alors $S_0$ et $S_1$ sont indépendants.
b) $\mathcal{N}(\boldsymbol{\mu}, \operatorname{diag}(6, 1))$ et $\mathcal{N}(\boldsymbol{\mu}, \operatorname{diag}(1, 6))$ ont le même déterminant ; la divergence KL de l'une à l'autre est donc nulle.
c) Tempérer une loi $\mathbf{p}$ à la température $T = 3$, puis tempérer la loi obtenue à la température $T' = 4$, donne la loi $\mathbf{p}$ tempérée à la température 12.
d) Sur $f(x, y) = 10xy$, que $x$ veut petite et $y$ grande, la descente-montée simultanée de pas $\eta = 0{,}04$ multiplie, à chaque pas et depuis tout point, la distance à l'équilibre $(0, 0)$ par 1,16.
e) $p$ est la loi uniforme sur $\{1, 2, 3, 4, 5, 6\}$ et $q$ la loi uniforme sur $\{1, 2\}$. $\mathrm{KL}(q \,\|\, p) = \ln 3$ est finie, alors que $\mathrm{KL}(p \,\|\, q) = +\infty$ : c'est pourquoi la KL inverse, $\mathrm{KL}(q \,\|\, p)$, permet à une loi approchée $q$ d'ignorer une partie de la masse de $p$.
f) Pour une politique fixée et $0 \le \gamma < 1$ : augmenter la récompense moyenne $r(s_0)$ d'un seul état $s_0$ ne fait baisser la valeur d'aucun état, et fait monter $V(s_0)$ d'au moins autant.
g) $\mathbf{x} = (x_1, x_2, x_3)$ est un vecteur gaussien de covariance $\boldsymbol{\Sigma}$ inversible, et $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$. La variance de $x_1$ sachant $x_2$ et $x_3$ vaut $\frac{1}{\Lambda_{11}}$.
h) $p$ et $q$ sont deux lois discrètes de supports disjoints, et $m = \frac12(p + q)$. Alors $\mathrm{JS}(p, m) = \ln 2$, comme $\mathrm{JS}(p, q)$.
i) Sur un signal refermé en anneau, de longueur multiple de 3, une moyenne mobile de trois cases efface tout motif cosinus de période 3 cases, quelle que soit sa phase, et ne multiplie par 0 aucun motif de période plus longue.
j) Une donnée vaut $x_1$ ou $x_2$, avec la probabilité $\frac12$ chacune. Un code stochastique donne $q(z \mid x_1) = (0{,}84 ;\ 0{,}16)$ et $q(z \mid x_2) = (0{,}34 ;\ 0{,}66)$, et le prior est $p(z) = (0{,}59 ;\ 0{,}41)$. Le posterior agrégé est égal au prior ; donc la KL moyenne au prior, $\mathbb{E}_x\,\mathrm{KL}\big(q(z \mid x) \,\|\, p(z)\big)$, est nulle.

### CP6.1 — Un vecteur gaussien de dimension 2 : loi marginale, loi conditionnelle, et la loi de μ + Lε ✏️ ★★ ⏱️ 10 min · 10 points (10/6 ≈ 1,67 par sous-question)

Dans un élevage, la masse d'un veau à la naissance, $x_1$, et à un mois, $x_2$ (en kg), forment un vecteur gaussien $\mathbf{x} = (x_1, x_2) \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, avec
$$\boldsymbol{\mu} = \begin{pmatrix} 40 \\ 55 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 16 & 12 \\ 12 & 13 \end{pmatrix}.$$

| | Question | Réponse attendue |
|---|---|---|
| a | le facteur de Cholesky $\mathbf{L}$ de $\boldsymbol{\Sigma}$ | une matrice $2 \times 2$ (valeurs exactes) |
| b | la loi marginale de $x_2$ : sa moyenne, puis sa variance | une liste de 2 nombres (valeurs exactes) |
| c | la loi de $x_2$ sachant $x_1 = 48$ : sa moyenne, puis sa variance | une liste de 2 nombres (valeurs exactes) |
| d | la loi de $x_1$ sachant $x_2 = 48{,}5$ : sa moyenne, puis sa variance | une liste de 2 nombres (4 décimales) |
| e | le tirage $\boldsymbol{\mu} + \mathbf{L}\boldsymbol{\varepsilon}$ pour $\boldsymbol{\varepsilon} = (1 ;\ -2{,}5)$ | une liste de 2 nombres (valeurs exactes) |
| f | on tire aussi $\boldsymbol{\mu} + \mathbf{M}\boldsymbol{\varepsilon}$, avec $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ et $\mathbf{M} = \begin{pmatrix} 0 & 4 \\ 2 & 3 \end{pmatrix}$ : la matrice de covariance de ces tirages | une matrice $2 \times 2$ (valeurs exactes) |

Sur ta copie : vérifie $\mathbf{L}\mathbf{L}^\top = \boldsymbol{\Sigma}$ ; écris $x_1$ et $x_2$ en fonction de $\varepsilon_1$ et $\varepsilon_2$, et explique avec elles pourquoi la variance de c) est $l_{22}^2$ et ne dépend pas de la valeur lue ; les tirages $\boldsymbol{\mu} + \mathbf{M}\boldsymbol{\varepsilon}$ ont-ils la loi $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, et donnent-ils le point de e) pour le même $\boldsymbol{\varepsilon}$ ?

### CP6.2 — La divergence KL entre deux gaussiennes de dimension 2, et une interpolation sphérique ✏️ ★★ ⏱️ 9 min · 9 points (1,5 par sous-question)

1. Une station mesure deux polluants de l'air. Leurs écarts à une valeur de référence, en µg/m³, suivent la loi $p_0 = \mathcal{N}(\boldsymbol{\mu}_0, \boldsymbol{\Sigma}_0)$ ; un modèle les décrit par $p_1 = \mathcal{N}(\boldsymbol{\mu}_1, \boldsymbol{\Sigma}_1)$, avec
$$\boldsymbol{\mu}_0 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \boldsymbol{\Sigma}_0 = \begin{pmatrix} 5 & 3 \\ 3 & 4 \end{pmatrix}, \qquad \boldsymbol{\mu}_1 = \begin{pmatrix} 3 \\ 1 \end{pmatrix}, \quad \boldsymbol{\Sigma}_1 = \begin{pmatrix} 4 & 2 \\ 2 & 2 \end{pmatrix}, \qquad \boldsymbol{\delta} = \boldsymbol{\mu}_1 - \boldsymbol{\mu}_0 .$$
2. Deux vecteurs de même norme, $\mathbf{u} = (2, 2, 1)$ et $\mathbf{v} = (0, 3, 0)$, d'angle $\Omega$.

| | Question | Réponse attendue |
|---|---|---|
| a | données 1 : $\operatorname{tr}(\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\Sigma}_0)$ | un nombre (valeur exacte) |
| b | données 1 : $\boldsymbol{\delta}^\top\boldsymbol{\Sigma}_1^{-1}\boldsymbol{\delta}$ | un nombre (valeur exacte) |
| c | données 1 : $\mathrm{KL}(p_0 \,\Vert\, p_1)$, en nats | un nombre (4 décimales) |
| d | données 2 : l'angle $\Omega$, en degrés | un nombre (2 décimales) |
| e | données 2 : $\operatorname{slerp}(\mathbf{u}, \mathbf{v} ;\ \frac14)$ | une liste de 3 nombres (4 décimales) |
| f | données 2 : la norme du point $(1 - t)\,\mathbf{u} + t\,\mathbf{v}$ de la ligne droite, pour $t = \frac14$ | un nombre (3 décimales) |

Sur ta copie : les trois termes de la KL, et ce que chacun compare ; sans calcul, l'angle de $\mathbf{u}$ avec le point de e), et sa norme.

### CP6.3 — Un mélange de deux gaussiennes de variances connues et trois mesures : responsabilités, un pas d'EM sur le poids et les moyennes, et l'écart à l'ELBO d'une affectation dure ✏️ ★★ ⏱️ 10 min · 10 points (2,5 par sous-question)

Une coopérative a mélangé par erreur les graines de deux sacs, sans savoir de quel sac vient chaque graine. Le temps de germination d'une graine, en heures, suit le mélange $\pi_1\,\mathcal{N}(\mu_1, \sigma^2) + \pi_2\,\mathcal{N}(\mu_2, \sigma^2)$ : la composante 1 est le sac de graines fraîches, la composante 2 le sac de graines anciennes, plus lentes à germer. La variance est connue, $\sigma^2 = 16$ h² pour les deux, et l'EM ne met à jour que le poids et les moyennes. On part de $\boldsymbol{\pi} = (0{,}62 ;\ 0{,}38)$ et $\boldsymbol{\mu} = (24 ;\ 32)$. Trois graines ont germé en $x = 22$, $27$ et $36$ heures.

| | Question | Réponse attendue |
|---|---|---|
| a | les responsabilités $r_{i1}$ de la composante 1 pour les trois graines, dans l'ordre des mesures | une liste de 3 nombres (4 décimales) |
| b | le poids $\pi_1$ après le pas M | un nombre (4 décimales) |
| c | les moyennes $(\mu_1, \mu_2)$ après le pas M (h) | une liste de 2 nombres (3 décimales) |
| d | avec les paramètres de départ : l'écart $\ln p(x_1, x_2, x_3) - \operatorname{ELBO}(q)$ pour l'**affectation dure** $q$, qui met chaque graine, avec certitude, dans la composante de plus grande responsabilité | un nombre (4 décimales) |

Sur ta copie : les trois nombres $\frac{(x - \mu_2)^2 - (x - \mu_1)^2}{2\sigma^2}$, avant d'y ajouter $\ln\frac{\pi_1}{\pi_2}$ ; pourquoi l'écart de d) est une somme de KL, et pourquoi chacune vaut $-\ln r$ ; pour quelle loi $q$ cet écart serait nul.

### CP6.4 — Une chaîne de Markov à trois états : loi à deux pas, et la valeur d'une politique fixée par le système de Bellman, quand une ligne finit ✏️ ★★ ⏱️ 9 min · 9 points (2,25 par sous-question)

Un domaine viticole suit chaque année l'état de ses parcelles de vigne : jeune plantation (état 0), en production (état 1), vieille (état 2). Sous la règle fixe du vigneron (une politique fixée), d'une année à la suivante :
- une jeune plantation reste jeune avec la probabilité 0,6, entre en production avec 0,33, et meurt (gel, maladie) avec 0,07 ;
- une parcelle en production y reste avec 0,7, vieillit avec 0,2, et est arrachée avec 0,1 ;
- une vieille parcelle reste vieille avec 0,4 ; sinon, le vigneron l'arrache.

Une parcelle morte ou arrachée sort du domaine : c'est la fin, codée par la masse qui manque à chaque ligne de $\mathbf{P}$, la matrice $3 \times 3$ des états 0, 1 et 2. La récolte moyenne d'une année, en hectolitres de vin, est $\mathbf{r} = (0 ;\ 22 ;\ 6)$ selon l'état de la parcelle cette année-là. On compte la récolte de l'année en cours (l'année 0) et de toutes les suivantes, sans actualisation ($\gamma = 1$).

| | Question | Réponse attendue |
|---|---|---|
| a | la loi $\boldsymbol{\mu}_2$ de l'état, dans deux ans, d'une parcelle jeune cette année (états 0, 1, 2) | une liste de 3 nombres (valeurs exactes) |
| b | la probabilité que cette parcelle soit sortie du domaine dans deux ans | un nombre (valeur exacte) |
| c | les valeurs $V(0)$, $V(1)$, $V(2)$ : la récolte totale moyenne d'une parcelle, depuis chaque état (hl) | une liste de 3 nombres (valeurs exactes) |
| d | la récolte moyenne de l'année 2 (la troisième récolte) d'une parcelle jeune cette année, une parcelle sortie du domaine comptant 0 hl (hl) | un nombre (valeur exacte) |

Sur ta copie : $\mathbf{P}$ et la somme de chacune de ses lignes ; le système $\mathbf{V} = \mathbf{r} + \mathbf{P}\mathbf{V}$, et pourquoi il se résout en commençant par $V(2)$ ; pourquoi $\gamma = 1$ est permis ici.

### CP6.5 — Un jeu à somme nulle 2 × 2 en stratégies mixtes, et W₁ entre deux petits échantillons de même taille ✏️ ★★ ⏱️ 9 min · 9 points (1,5 par sous-question)

1. Chaque nuit, un braconnier chasse dans la zone nord ou dans la zone sud d'une réserve, et un garde surveille l'une des deux, sans connaître le choix de l'autre. Ce que gagne le braconnier, en centaines d'euros (ce que perd la réserve) :

| | garde au nord | garde au sud |
|---|---|---|
| **braconnier au nord** | −4 | 6 |
| **braconnier au sud** | 3 | −2 |

Le braconnier maximise, le garde minimise ; $p$ est la probabilité que le braconnier aille au nord, $q$ celle que le garde surveille le nord.

2. Deux pépinières vendent la même variété d'arbuste. On mesure la hauteur, en cm, de cinq plants pris au hasard dans chacune : pépinière A, 26 ; 19 ; 34 ; 21 ; 32 ; pépinière B, 29 ; 37 ; 14 ; 22 ; 18.

| | Question | Réponse attendue |
|---|---|---|
| a | données 1 : le maximin, puis le minimax, en stratégies pures | une liste de 2 entiers |
| b | données 1 : $p^\star$ | une fraction irréductible |
| c | données 1 : $q^\star$ | une fraction irréductible |
| d | données 1 : la valeur du jeu (en centaines d'euros) | une fraction irréductible |
| e | données 2 : $W_1$ entre les deux échantillons (cm) | un nombre (valeur exacte) |
| f | données 2 : $W_2$ entre les deux échantillons (cm) | un nombre (4 décimales) |

Sur ta copie : pourquoi le jeu n'a pas de point selle ; vérifie $W_1 \le W_2$.

### CP6.6 — Des distances aux positions : double centrage, matrice de Gram, et une configuration à une isométrie près ✏️ ★★ ⏱️ 8 min · 8 points (2 par sous-question)

Trois bouées A, B et C sont ancrées dans une baie. Un bateau ne mesure que leurs distances ; leurs carrés, en hm² (1 hm = 100 m), valent $\mathrm{AB}^2 = 16$, $\mathrm{AC}^2 = 121$ et $\mathrm{BC}^2 = 49$. Les bouées sont rangées dans l'ordre A, B, C ; $\mathbf{D}^{(2)}$ est la matrice $3 \times 3$ des carrés de leurs distances, et $\mathbf{G} = -\frac12\mathbf{J}\mathbf{D}^{(2)}\mathbf{J}$ la matrice de Gram des bouées centrées. La carte se construit comme dans la fiche M28 : $\mathbf{G} = \mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top$ avec $\lambda_1 \ge \lambda_2 \ge \cdots$, la colonne $k$ de la carte est $\sqrt{\lambda_k}\,\mathbf{q}_k$ avec $\mathbf{q}_k$ unitaire, on garde autant de colonnes que de valeurs propres non nulles, et, dans chaque colonne, la première coordonnée non nulle (en lisant de A vers C) est positive.

| | Question | Réponse attendue |
|---|---|---|
| a | $s$, la moyenne des neuf coefficients de $\mathbf{D}^{(2)}$ (hm²) | une fraction irréductible |
| b | la matrice $\mathbf{G}$, lignes et colonnes dans l'ordre A, B, C (hm²) | une matrice $3 \times 3$ (valeurs exactes) |
| c | les trois valeurs propres de $\mathbf{G}$, de la plus grande à la plus petite (compare les lignes de $\mathbf{G}$) | une liste de 3 nombres (valeurs exactes) |
| d | la carte : une colonne par valeur propre non nulle, une ligne par bouée (A, B, C), en hm | une matrice à 3 lignes (valeurs exactes) |

Sur ta copie : les moyennes $r_i$ des lignes de $\mathbf{D}^{(2)}$, puis $G_{ij} = -\frac12\big(D^{(2)}_{ij} - r_i - r_j + s\big)$ ; vérifie $\mathbf{G}\mathbf{1} = \mathbf{0}$ ; que dit le nombre de valeurs propres non nulles de la disposition des bouées ? quelle sorte d'isométrie peut séparer ta carte de la vraie position des bouées ?

### CP6.7 — La distance de Fréchet de deux gaussiennes du plan de covariances proportionnelles, et le biais de la distance entre deux moyennes estimées ✏️ ★★ ⏱️ 9 min · 9 points (1,8 par sous-question)

Deux fermes solaires ont chacune deux rangées de panneaux. La production journalière des deux rangées, en MWh, suit $\mathcal{N}(\boldsymbol{\mu}_A, \boldsymbol{\Sigma}_A)$ dans la ferme A et $\mathcal{N}(\boldsymbol{\mu}_B, \boldsymbol{\Sigma}_B)$ dans la ferme B, plus exposée aux nuages :
$$\boldsymbol{\mu}_A = \begin{pmatrix} 18 \\ 12 \end{pmatrix}, \quad \boldsymbol{\Sigma}_A = \begin{pmatrix} 12 & 2 \\ 2 & 9 \end{pmatrix}, \qquad \boldsymbol{\mu}_B = \begin{pmatrix} 21 \\ 13 \end{pmatrix}, \quad \boldsymbol{\Sigma}_B = 4\,\boldsymbol{\Sigma}_A = \begin{pmatrix} 48 & 8 \\ 8 & 36 \end{pmatrix}.$$
On compare d'abord les deux lois par leur distance de Fréchet $W_2$. Puis on suppose les moyennes inconnues : on les estime par les moyennes $\bar{\mathbf{x}}$ de relevés de jours indépendants.

| | Question | Réponse attendue |
|---|---|---|
| a | les valeurs propres de $\boldsymbol{\Sigma}_A\boldsymbol{\Sigma}_B$, de la plus grande à la plus petite | une liste de 2 nombres (valeurs exactes) |
| b | la part des covariances dans $W_2^2$, $\operatorname{tr}\boldsymbol{\Sigma}_A + \operatorname{tr}\boldsymbol{\Sigma}_B - 2\sum_i\sqrt{\lambda_i(\boldsymbol{\Sigma}_A\boldsymbol{\Sigma}_B)}$ (MWh²) | un nombre (valeur exacte) |
| c | la distance de Fréchet $W_2$ entre les deux lois (MWh) | un nombre (4 décimales) |
| d | $\mathbb{E}\lVert\bar{\mathbf{x}}_A - \bar{\mathbf{x}}_B\rVert^2$, pour 20 jours de la ferme A et 40 jours de la ferme B (MWh²) | un nombre (valeur exacte) |
| e | $\mathbb{E}\lVert\bar{\mathbf{x}}_A - \bar{\mathbf{x}}_B\rVert^2$, pour 25 jours de la ferme A et 25 jours de la ferme B (MWh²) | un nombre (valeur exacte) |

Sur ta copie : les valeurs propres de $\boldsymbol{\Sigma}_A$, et pourquoi celles de $\boldsymbol{\Sigma}_A\boldsymbol{\Sigma}_B$ s'en déduisent ; écris la part des covariances de b) en fonction de $\operatorname{tr}\boldsymbol{\Sigma}_A$ seulement ; compare d) et e) : que faut-il en conclure quand on compare des distances estimées ?

### CP6.8 — Une démonstration au choix ∂ ★★★ ⏱️ 12 min · 12 points (3 par étape)

Traite **un seul** des deux sujets. Rédige en phrases : ce que tu supposes, chaque étape et la règle qui la justifie, ce que tu conclus. Cette question se note avec le corrigé.

**Sujet A — L'entropie d'une loi tempérée croît avec la température.** $\mathbf{p}$ est une loi sur $n$ issues, toutes de probabilité $p_i > 0$, et, pour $T > 0$, sa loi tempérée est $p_i^{(T)} = \frac{p_i^{1/T}}{\sum_j p_j^{1/T}}$. On note $E_i = -\ln p_i$ les énergies, $\beta = \frac1T$, $Z = \sum_j e^{-\beta E_j}$, $\langle g\rangle = \sum_i p_i^{(T)}g_i$ la moyenne d'une grandeur $g$ sous $\mathbf{p}^{(T)}$, $\mathbb{V}(E) = \langle E^2\rangle - \langle E\rangle^2$ la variance des énergies sous $\mathbf{p}^{(T)}$, et $H(T) = -\sum_i p_i^{(T)}\ln p_i^{(T)}$ l'entropie de $\mathbf{p}^{(T)}$.
1. Montre que $p_i^{(T)} = \frac{e^{-\beta E_i}}{Z}$, puis que $H(T) = \beta\langle E\rangle + \ln Z$. **[3]**
2. En dérivant par rapport à $\beta$, montre que $\frac{\mathrm{d}p_i^{(T)}}{\mathrm{d}\beta} = p_i^{(T)}\big(\langle E\rangle - E_i\big)$, puis que $\frac{\mathrm{d}\ln Z}{\mathrm{d}\beta} = -\langle E\rangle$ et $\frac{\mathrm{d}\langle E\rangle}{\mathrm{d}\beta} = -\mathbb{V}(E)$. **[3]**
3. Déduis-en $\frac{\mathrm{d}H}{\mathrm{d}\beta} = -\beta\,\mathbb{V}(E)$, puis $\frac{\mathrm{d}H}{\mathrm{d}T} = \frac{\mathbb{V}(E)}{T^3} \ge 0$. Quand cette dérivée est-elle nulle ? Conclus. **[3]**
4. Pour $\mathbf{p} = (0{,}6 ;\ 0{,}1 ;\ 0{,}1 ;\ 0{,}1 ;\ 0{,}1)$ : calcule $H(1)$ et la dérivée $\frac{\mathrm{d}H}{\mathrm{d}T}$ en $T = 1$ (4 décimales). **[3]**

**Sujet B — La loi de Boltzmann minimise l'énergie libre.** Des issues $1, \ldots, n$ ont des énergies $E_i$, et $T > 0$ est une température. La loi de Boltzmann est $p^\star_i = \frac{e^{-E_i/T}}{Z}$, avec $Z = \sum_j e^{-E_j/T}$. Pour une loi $q$ sur les mêmes issues, l'**énergie libre** est $F(q) = \mathbb{E}_q[E] - T\,H(q)$, où $H(q) = -\sum_i q_i\ln q_i$ (avec $0\ln 0 = 0$).
1. Montre que, pour chaque issue, $E_i = -T\ln p^\star_i - T\ln Z$. **[3]**
2. Montre que, pour toute loi $q$, $F(q) = T\,\mathrm{KL}(q \,\|\, p^\star) - T\ln Z$. **[3]**
3. Conclus : $F(q) \ge -T\ln Z$, avec égalité si et seulement si $q = p^\star$. Réécris l'identité de la question 2 sous la forme $\ln Z = -\frac{F(q)}{T} + \mathrm{KL}(q \,\|\, p^\star)$, et dis à quelle identité de M25b elle ressemble, terme à terme. **[3]**
4. Pour les énergies $(0,\ \ln 3,\ 2\ln 3)$ et $T = 1$ : calcule $Z$ (valeur exacte, une fraction), puis $p^\star$ et $F(p^\star)$ (4 décimales), puis $F(q)$ pour $q$ uniforme et pour $q = (1, 0, 0)$. Pourquoi la loi qui met toute la masse sur l'énergie la plus basse ne minimise-t-elle pas $F$ ? **[3]**

### CP6.9 — Corriger une copie : cinq erreurs, une par chapitre 🐛 ★★ ⏱️ 9 min · 9 points

Voici huit lignes extraites de la copie d'un élève. **Cinq** sont fausses, une par chapitre de la partie VI.

- **(A)** La chaîne de matrice $\begin{pmatrix} 0{,}05 & 0{,}95 \\ 0{,}65 & 0{,}35 \end{pmatrix}$ a pour valeurs propres 1 et $-0{,}6$ ; la seconde étant négative, la loi $\boldsymbol{\mu}_n$ de la chaîne ne converge pas vers sa loi stationnaire : elle oscille sans fin.
- **(B)** Pour 50 points de $\mathbb{R}^3$ rangés en lignes de $\mathbf{X}$, la matrice de Gram $\mathbf{X}\mathbf{X}^\top$, de taille $50 \times 50$, a au plus trois valeurs propres non nulles : les mêmes que celles de $\mathbf{X}^\top\mathbf{X}$.
- **(C)** En dimension 2, l'ellipse de Mahalanobis de niveau $c = 2{,}5$ contient 98,8 % des tirages, comme l'intervalle $[\mu - 2{,}5\sigma ;\ \mu + 2{,}5\sigma]$ en dimension 1.
- **(D)** Sur $f(x, y) = xy$, la descente-montée alternée de pas $\eta = 0{,}4$ garde $x^2 + y^2 - 0{,}4\,xy$ constant : ses itérés restent sur une ellipse.
- **(E)** Pour approcher le mélange $\frac13\,\mathcal{N}(0, 2) + \frac23\,\mathcal{N}(9, 2)$ par une gaussienne $q$ au sens de $\mathrm{KL}(p \,\|\, q)$, on prend $q = \mathcal{N}(6, 2)$ : la moyenne du mélange, et la variance commune des deux composantes.
- **(F)** L'entropie différentielle de $\mathcal{N}(0 ;\ 0{,}03)$ vaut $\frac12\ln(2\pi e \times 0{,}03)$, un nombre négatif : ce n'est pas une erreur de calcul, une entropie différentielle peut être négative.
- **(G)** Le motif $x_{ij} = \cos\big(2\pi(0{,}24\,i + 0{,}07\,j)\big)$ a pour période $\frac{1}{0{,}24} + \frac{1}{0{,}07} \approx 18{,}5$ cases.
- **(H)** Pour $\mathbf{a} = \mathbf{b} = (\frac12 ;\ \frac12)$ sur les points 0 et 1 de la droite, le couplage indépendant $\boldsymbol{\Gamma} = \mathbf{a}\mathbf{b}^\top$ coûte $\frac12$ : c'est $W_1(\mathbf{a}, \mathbf{b})$.

a) Les lettres des cinq lignes fausses, dans n'importe quel ordre (comme `ABCDE`). **[4,5]**
b) Pour chaque ligne fausse, écris le résultat juste et le nom de la règle oubliée, en quelques mots. **[4,5]** (0,9 par ligne ; se note avec le corrigé)

### CP6.10 — Problème de synthèse : une file d'attente à trois états suivie de façon gloutonne, puis échantillonnée après la troncature top-p de ses transitions : lois conditionnelles, coût en KL et nouvelle loi stationnaire 🔗 ★★ ⏱️ 16 min · 16 points (16/7 ≈ 2,29 par sous-question)

Une borne de recharge pour voitures électriques a deux places d'attente. Toutes les cinq minutes, on note le nombre de voitures qui attendent : 0, 1 ou 2, les trois états. Ce nombre suit une chaîne de Markov de matrice
$$\mathbf{P} = \begin{pmatrix} 0{,}32 & 0{,}60 & 0{,}08 \\ 0{,}21 & 0{,}33 & 0{,}46 \\ 0{,}05 & 0{,}60 & 0{,}35 \end{pmatrix}.$$
1. Un simulateur **glouton** suit la file en passant toujours à l'état suivant le plus probable, $u_{t+1} = f(u_t)$ (entre deux probabilités égales, le plus petit état), depuis $u_0 = 0$.
2. Un simulateur **aléatoire** tire l'état suivant, mais après avoir tronqué chaque ligne de $\mathbf{P}$ par un top-p de seuil $m = 0{,}68$ : dans la ligne de l'état présent, il garde les états suivants par probabilité décroissante, un à un, jusqu'à ce que leur masse $P(S)$ atteigne $m$, puis tire selon la loi conditionnelle sur l'ensemble $S$ gardé. On note $\mathbf{P}'$ la matrice de la chaîne ainsi simulée, $\mathbf{p}_1$ la ligne 1 de $\mathbf{P}$, $S_1$ l'ensemble des états gardés dans cette ligne (un ensemble d'états, pas l'état $S_t$ au pas 1) et $\mathbf{p}_{S_1}$ la ligne 1 de $\mathbf{P}'$.

| | Question | Réponse attendue |
|---|---|---|
| a | données 1 : $f(0)$, $f(1)$, $f(2)$ | une liste de 3 entiers |
| b | données 1 : la prépériode $\mu$ (un nombre de pas, pas une loi), puis la période $\lambda$ de la suite gloutonne | une liste de 2 entiers |
| c | données 2 : l'ensemble $S_1$, par probabilité décroissante | une liste d'entiers |
| d | données 2 : la loi tronquée $\mathbf{p}_{S_1}$ (états 0, 1, 2) | une liste de 3 nombres (4 décimales) |
| e | données 2 : le coût de la troncature de la ligne 1, $\mathrm{KL}(\mathbf{p}_{S_1} \,\Vert\, \mathbf{p}_1)$, en nats | un nombre (4 décimales) |
| f | données 2 : la matrice $\mathbf{P}'$ | une matrice $3 \times 3$ (4 décimales) |
| g | données 2 : la loi stationnaire $\boldsymbol{\pi}'$ de $\mathbf{P}'$ (états 0, 1, 2) | une liste de 3 nombres (4 décimales) |

Sur ta copie : la borne que la fiche M28 donne à $\mu + \lambda$, comparée à ta réponse b) ; pourquoi $\mathrm{KL}(\mathbf{p}_1 \,\|\, \mathbf{p}_{S_1})$ est infinie ; pourquoi $\pi'_0 = 0$, et ce que cela dit de la file vide dans le simulateur aléatoire.

---

**Fin de l'examen.** Note l'heure, relis ta copie, puis passe à la vérification : le notebook `02_examen_notebook.ipynb` (ta copie), puis le corrigé `03_examen_corrige.md`.
