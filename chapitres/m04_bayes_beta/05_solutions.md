# M04 · Bayes, vraisemblance et loi Beta — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🗣️ Pont, lecture et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M04.Q1 — Les quatre termes de la formule de Bayes
1. $P(H) = 0{,}03$ : l'**a priori** (ce qu'on croit avant de voir l'alerte).
2. $P(O \mid H) = 0{,}98$ : la **vraisemblance** de l'hypothèse $H$ pour l'observation $O$.
3. $P(O) = 0{,}05$ : l'**évidence** (la probabilité de l'observation, toutes hypothèses confondues).
4. $P(H \mid O) = 0{,}59$ : l'**a posteriori**.
5. $\frac{P(O \mid H)\,P(H)}{P(O)} = \frac{0{,}98 \times 0{,}03}{0{,}05} = 0{,}588 \approx 0{,}59$ : cohérents. On en déduit même $P(O \mid \text{non } H) = \frac{0{,}05 - 0{,}0294}{0{,}97} \approx 0{,}021$.
6. **Faux** : l'évidence est la même, $P(O)$ ; d'ailleurs $P(\text{non } H \mid O) = 1 - P(H \mid O) = 0{,}41$.

### M04.Q2 — Mettre à jour deux fois
1. Produits $0{,}5 \times 0{,}6 = 0{,}3$ et $0{,}5 \times 0{,}2 = 0{,}1$ : $P(H_1 \mid O) = \frac{0{,}3}{0{,}4} = $ **0,75**.
2. Avec l'a priori 0,75 : $\frac{0{,}75 \times 0{,}6}{0{,}75 \times 0{,}6 + 0{,}25 \times 0{,}2} = \frac{0{,}45}{0{,}5} = $ **0,9**.
3. **Faux** : l'a priori de la deuxième mise à jour est l'a posteriori de la première, 0,75.
4. $\frac{0{,}5 \times 0{,}6 \times 0{,}4}{0{,}5 \times 0{,}6 \times 0{,}4 + 0{,}5 \times 0{,}2 \times 0{,}8} = \frac{0{,}12}{0{,}2} = $ **0,6**.
5. Chaque $O$ multiplie le rapport par $\frac{0{,}6}{0{,}2} = 3$, et le rapport a priori vaut 1 : **$3^n$**.
6. Il faut $3^n > 99$ : $3^4 = 81$ ne suffit pas ($\frac{81}{82} \approx 0{,}988$), $3^5 = 243$ suffit ($\frac{243}{244} \approx 0{,}996$) : **5**.

### M04.Q3 — La vraisemblance, une fonction du paramètre
1. $L(\theta) = \theta^4(1 - \theta)^6$.
2. En $\theta = \frac{4}{10} = $ **0,4**.
3. **Faux** : $L$ n'est pas une densité en $\theta$ ; ici $\int_0^1 L = B(5, 7) = \frac{1}{2310}$.
4. **Vrai** : $c\,L$ a les mêmes variations que $L$ si $c > 0$.
5. Le logarithme change le produit en somme ($4\ln\theta + 6\ln(1 - \theta)$), plus simple à dériver, et il évite l'underflow d'un produit de nombreuses probabilités (fiche §7). Comme $\ln$ est croissante, $\ln L$ a le même maximum que $L$.
6. En $\theta = 0$ : $L(\theta) = (1 - \theta)^6$ décroît. Ce n'est pas raisonnable : après 6 essais, on affirmerait que le succès est **impossible**. C'est ce que corrige un a priori (le lissage de Laplace donne $\frac{1}{8}$, fiche §5).

### M04.Q4 — La loi Beta : forme et paramètres
1. La loi **uniforme** sur $[0, 1]$ (densité 1).
2. $\frac{3}{10} = $ **0,3**.
3. **$\mathrm{Beta}(30, 70)$** : même moyenne, mais variance $\frac{0{,}21}{101} \approx 0{,}0021$ contre $\frac{0{,}21}{11} \approx 0{,}019$.
4. Une forme en **U** : elle tend vers l'infini en 0 et en 1, avec un minimum en $\frac{1}{2}$.
5. $\Gamma(5) = 4! = $ **24**.
6. **Faux** : la densité de $\mathrm{Beta}(2, 2)$ vaut 1,5 en $\frac{1}{2}$, celle de $\mathrm{Beta}(30, 70)$ dépasse 8. Seule son aire vaut 1.

### M04.Q5 — Conjuguée, Laplace, MAP
1. $\mathrm{Beta}(2 + 4,\ 3 + 1) = $ **$\mathrm{Beta}(6, 4)$**.
2. $\frac{6 - 1}{6 + 4 - 2} = \frac{5}{8} = $ **0,625**.
3. $\frac{6}{10} = $ **0,6**.
4. $\frac{0 + 1}{8 + 2} = $ **0,1**.
5. **Vrai** : l'a posteriori est $\mathrm{Beta}(k + 1,\ n - k + 1)$, de mode $\frac{k}{n}$ (fiche §6).
6. $6 + 14 = $ **20** pseudo-observations, dont 6 succès.

### M04.Q6 — Logarithmes et underflow
1. $400 \ln 0{,}1 \approx $ **$-921{,}03$**.
2. **0.0** : $0{,}1^{400} = 10^{-400}$ est plus petit que le plus petit `float64` positif (environ $5 \times 10^{-324}$) ; c'est l'underflow.
3. Pour que le plus grand terme devienne $e^0 = 1$ : aucune exponentielle ne déborde, et elles ne valent pas toutes 0. L'identité $\ln\sum_j e^{\ell_j} = m + \ln\sum_j e^{\ell_j - m}$ est exacte.
4. $\ln 2 \approx $ **0,693**.
5. $-500 + \ln 2 \approx $ **$-499{,}307$** (alors que `math.exp(-500)` est déjà minuscule, et `math.exp(-800)` vaut 0).
6. **Vrai** : la log-vraisemblance d'observations indépendantes est la somme de leurs log-probabilités.

### M04.Q7 — Fréquentiste ou bayésien ?
1. **Bayésien** : une probabilité sur le paramètre, sachant les données (un intervalle de crédibilité).
2. **Fréquentiste** : une fréquence sur des études répétées (un intervalle de confiance).
3. **Bayésien** : un a priori sur un paramètre.
4. **Les deux** : une fréquence limite pour l'un, un degré de certitude pour l'autre, et la même valeur.
5. **Vrai** : l'a priori pèse de moins en moins (fiche §6 et §8).
6. Il tire un taux au hasard dans l'a posteriori de chaque titre et affiche celui dont le tirage est le plus grand. Tant que les a posteriori se chevauchent, le titre qui semble le moins bon a une chance d'obtenir le plus grand tirage : il est encore essayé, en proportion de sa probabilité d'être le meilleur. Ces essais s'espacent à mesure que les a posteriori se resserrent.

<a id="rappels"></a>

## 🔁 Rappels

### M04.R1 — Probabilités conditionnelles (M03)
1. $\frac{30 + 24}{200} = $ **0,27**.
2. $\frac{24}{80} = $ **0,3**.
3. $\frac{24}{54} = \frac{4}{9} \approx$ **0,444**.
4. $\frac{24}{200} = $ **0,12**.
5. **Non** : $P(\text{achat} \mid \text{iOS}) = 0{,}3 \ne P(\text{achat}) = 0{,}27$ (et $P(\text{achat} \mid \text{Android}) = 0{,}25$).

### M04.R2 — Intégrales et densités (M02a)
1. $\frac{1}{3}$.
2. $\frac{1}{2} - \frac{1}{3} = \frac{1}{6}$.
3. $c = 6$ (l'intégrale de $c\,x(1 - x)$ doit valoir 1).
4. $\int_0^1 6x^2(1 - x)\,dx = 6\big(\frac{1}{3} - \frac{1}{4}\big) = \frac{1}{2}$ (la densité est symétrique autour de $\frac{1}{2}$).
5. $\big[-\frac{(1 - x)^5}{5}\big]_0^1 = \frac{1}{5}$.

### M04.R3 — Loi binomiale (M02b)
1. $0{,}7^{10} \approx$ **0,0282**.
2. $10 \times 0{,}3 = $ **3**.
3. $10 \times 0{,}3 \times 0{,}7 = $ **2,1**.
4. $\binom{10}{2} \times 0{,}3^2 \times 0{,}7^8 = 45 \times 0{,}09 \times 0{,}0576 \approx$ **0,2335**.
5. $\binom{10}{2}$ ne dépend pas de $p$ : multiplier une fonction de $p$ par une constante positive ne déplace pas son maximum (fiche §3). On peut maximiser $p^2(1 - p)^8$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M04.1 — Bayes avec deux hypothèses : un capteur de fuite d'eau

**Réponses** : a) `0.0392` · b) `0.242` · c) `5.2` · d) `39.2` · e) `29.7` · f) `0.91` · g) `"19/1980"` · h) `0.625`.

**Démarche.**

| hypothèse | a priori | vraisemblance de « sonne » | produit |
|---|---|---|---|
| fuite | 0,01 | 0,95 | 0,0095 |
| pas de fuite | 0,99 | 0,03 | 0,0297 |
| | | **évidence** | 0,0392 |

- a) La somme des produits. b) $\frac{0{,}0095}{0{,}0392} \approx 0{,}242$.
- c) Avec « ne sonne pas » : produits $0{,}01 \times 0{,}05 = 0{,}0005$ et $0{,}99 \times 0{,}97$, évidence $1 - 0{,}0392 = 0{,}9608$ ; $\frac{0{,}0005}{0{,}9608} \approx 0{,}00052$, soit 5,2 pour 10 000.
- d) $1000 \times 0{,}0392$. e) $1000 \times 0{,}99 \times 0{,}03$.
- f) Les deux capteurs sonnent : vraisemblances $0{,}95^2 = 0{,}9025$ et $0{,}03^2 = 0{,}0009$ ; $\frac{0{,}009025}{0{,}009025 + 0{,}000891} \approx 0{,}910$. On obtient la même chose en reprenant b) comme a priori pour le second capteur.
- g) Avec $x = P(\text{sonne} \mid \text{pas de fuite})$ : $\frac{0{,}0095}{0{,}0095 + 0{,}99\,x} \ge 0{,}5 \iff 0{,}99\,x \le 0{,}0095 \iff x \le \frac{0{,}0095}{0{,}99} = \frac{19}{1980} \approx 0{,}0096$ (arrondir par excès franchirait la limite : d'où la fraction).
- h) $\frac{0{,}05 \times 0{,}95}{0{,}05 \times 0{,}95 + 0{,}95 \times 0{,}03} = \frac{0{,}0475}{0{,}076} = 0{,}625$.

Pour la copie : sur 1 000 nuits, 10 fuites, dont 9,5 font sonner le capteur, et 29,7 fausses alertes : parmi les 39,2 alertes, $\frac{9{,}5}{39{,}2} \approx 0{,}242$. Les fuites sont si rares que les fausses alertes, même à 3 %, sont trois fois plus nombreuses que les vraies. Une détection parfaite (1 au lieu de 0,95) ne donnerait que $\frac{0{,}01}{0{,}0397} \approx 0{,}252$ ; des fausses alertes dix fois plus rares (0,003) donneraient $\frac{0{,}0095}{0{,}0095 + 0{,}00297} \approx 0{,}762$ : c'est elles qu'il faut améliorer.

**Erreurs fréquentes.** Répondre 0,95 en b) (confondre $P(\text{fuite} \mid \text{sonne})$ et $P(\text{sonne} \mid \text{fuite})$) ; oublier la part « sans fuite » de l'évidence (0,0095) ; en c), ne pas diviser par l'évidence de « ne sonne pas » ; en g), oublier le facteur 0,99 ($\frac{19}{2000}$).

**Variante.** Trois capteurs identiques et indépendants sonnent tous : $P(\text{fuite} \mid \ldots)$ ? *Réponse* : $\frac{0{,}01 \times 0{,}95^3}{0{,}01 \times 0{,}95^3 + 0{,}99 \times 0{,}03^3} \approx 0{,}997$.

### Ex M04.2 — Trois hypothèses et un tableau de mise à jour

**Réponses** : a) `0.48` · b) `[0.5625, 0.4167, 0.0208]` · c) `[0.1725, 0.7668, 0.0607]` · d) `[0.3339, 0.6596, 0.0065]` · e) `0.0728` · f) `"O"` · g) `0.565` · h) `11`.

**Démarche.**

| type | a priori | V : vraisemblance, produit | après V | N : vraisemblance, produit | après V, N | V : produit | après V, N, V |
|---|---|---|---|---|---|---|---|
| R | 0,3 | 0,9 ; 0,27 | 0,5625 | 0,1 ; 0,05625 | 0,1725 | 0,15525 | 0,3339 |
| O | 0,5 | 0,4 ; 0,20 | 0,4167 | 0,6 ; 0,25 | 0,7668 | 0,30671 | 0,6596 |
| I | 0,2 | 0,05 ; 0,01 | 0,0208 | 0,95 ; 0,01979 | 0,0607 | 0,00304 | 0,0065 |
| évidence | | 0,48 | | 0,3260 | | 0,4650 | |

- e) $0{,}48 \times 0{,}3260 \times 0{,}4650 \approx 0{,}0728$, ou d'un coup : $0{,}3 \times 0{,}9 \times 0{,}1 \times 0{,}9 + 0{,}5 \times 0{,}4 \times 0{,}6 \times 0{,}4 + 0{,}2 \times 0{,}05 \times 0{,}95 \times 0{,}05 = 0{,}0243 + 0{,}048 + 0{,}000475 = 0{,}072775$.
- f) O. g) $0{,}3339 \times 0{,}9 + 0{,}6596 \times 0{,}4 + 0{,}0065 \times 0{,}05 \approx 0{,}565$.
- h) Après $m$ semaines sans venir, les poids (non normalisés) sont $0{,}0243 \times 0{,}1^m$, $0{,}048 \times 0{,}6^m$ et $0{,}000475 \times 0{,}95^m$. I dépasse O quand $\big(\frac{0{,}95}{0{,}6}\big)^m > \frac{0{,}048}{0{,}000475} \approx 101$, soit $m > \frac{\ln 101}{\ln 1{,}583} \approx 10{,}05$ : $m = 11$. (I dépasse R dès $m = 2$.)

Pour la copie : un régulier ne manque une semaine qu'avec la probabilité 0,1, contre 0,6 pour un occasionnel : la semaine N divise le rapport R/O par 6.

**Erreurs fréquentes.** Repartir de l'a priori à chaque étape ; oublier de normaliser ; utiliser la probabilité de venir pour la semaine N ; calculer l'évidence de la suite avec l'a priori à chaque étape ($0{,}48 \times 0{,}52 \times 0{,}48$).

**Variante.** Après V, V, V, l'a posteriori du type R ? *Réponse* : $\frac{0{,}3 \times 0{,}9^3}{0{,}3 \times 0{,}9^3 + 0{,}5 \times 0{,}4^3 + 0{,}2 \times 0{,}05^3} \approx 0{,}872$.

### Ex M04.3 — La vraisemblance d'un taux de clic

**Réponses** : a) `0.15` · b) `1.277` · c) `-8.454` · d) `0.2428` · e) `0.295` · f) `0.1429` · g) `0.1` · h) `True`.

**Démarche.**
- a) La fréquence : $\frac{3}{20}$.
- b) $\frac{L(0{,}15)}{L(0{,}10)} = 1{,}5^3 \times \big(\frac{0{,}85}{0{,}9}\big)^{17} \approx 3{,}375 \times 0{,}378 \approx 1{,}277$.
- c) $3\ln 0{,}15 + 17\ln 0{,}85 \approx -5{,}691 - 2{,}763 = -8{,}454$.
- d) $\binom{20}{3}\,L(0{,}15) = 1140 \times e^{-8{,}454} \approx 0{,}2428$.
- e) $2^3 \times \big(\frac{0{,}7}{0{,}85}\big)^{17} \approx 8 \times 0{,}0369 \approx 0{,}295$.
- f) 3 clics sur 21 : $\frac{1}{7} \approx 0{,}1429$. g) $\frac{3 + 2}{20 + 30}$ : la vraisemblance des deux jours est le produit $\theta^5(1 - \theta)^{45}$.
- h) Vrai : chaque suite a la vraisemblance $\theta^3(1 - \theta)^{17}$.

Pour la copie : $L$ monte jusqu'à 0,15 puis redescend, presque nulle au-delà de 0,45. b) La suite observée est 1,28 fois plus probable si $\theta = 0{,}15$ que si $\theta = 0{,}10$. d) additionne les 1 140 suites qui ont 3 clics, chacune de probabilité $L(0{,}15)$ ; le facteur 1 140 ne dépend pas de $\theta$, donc le maximum ne bouge pas.

**Erreurs fréquentes.** $\hat{\theta} = \frac{17}{20}$ ; inverser les rapports ; prendre $\log_{10}$ ; faire en g) la moyenne des deux fréquences (0,108).

**Variante.** $\frac{L(0{,}15)}{L(0{,}05)}$ ? *Réponse* : $27 \times \big(\frac{0{,}85}{0{,}95}\big)^{17} \approx 4{,}08$.

### Ex M04.4 — Maximiser une vraisemblance : dériver son logarithme

**Réponses** : a) `-8.0` · b) `-3.0` · c) `0.625` · d) `-7.35` · e) `-12.8` · f) `1.6` · g) `2.0` · h) `0.28`.

**Démarche.** $\ell(\lambda) = 5\ln\lambda - 8\lambda$, $\ell'(\lambda) = \frac{5}{\lambda} - 8$, $\ell''(\lambda) = -\frac{5}{\lambda^2}$.
- a) $0 - 8$. b) $5 - 8$. c) $\ell'(\lambda) = 0 \iff \lambda = \frac{5}{8}$. d) $5\ln 0{,}625 - 5 \approx -7{,}350$. e) $-\frac{5}{0{,}625^2} = -12{,}8$. f) $\frac{8}{5} = 1{,}6$ s, la moyenne des durées.
- g) $\ell(\mu) = -5\mu + 10\ln\mu - \sum_i \ln(x_i!)$, $\ell'(\mu) = -5 + \frac{10}{\mu} = 0 \iff \mu = 2$, la moyenne des comptages. h) $\frac{7}{25}$.

Pour la copie : $\ell(\lambda) = n\ln\lambda - \lambda\sum_i x_i$, $\ell'(\lambda) = \frac{n}{\lambda} - \sum_i x_i$, donc $\hat{\lambda} = \frac{n}{\sum_i x_i} = \frac{1}{\bar{x}}$ ; pour la loi de Poisson, $\hat{\mu} = \bar{x}$. $\ell''$ est négative partout : $\ell$ est concave, et son unique point critique est son maximum.

**Erreurs fréquentes.** $\hat{\lambda} = \bar{x}$ (la durée moyenne, pas le taux) ; une erreur de signe dans $\ell''$ ; oublier le terme $5\ln\lambda$.

**Variante.** Une sixième durée de 4 s : $\hat{\lambda}$ ? *Réponse* : $\frac{6}{12} = 0{,}5$.

### Ex M04.5 — La loi Beta : normalisation, moyenne, mode, variance

**Réponses** : a) `"1/30"` · b) `2.4576` · c) `"2/7"` · d) `0.2` · e) `"5/196"` · f) `0.8906` · g) `12` · h) `[2, 6]`.

**Démarche.**
- a) $B(2, 5) = \frac{\Gamma(2)\Gamma(5)}{\Gamma(7)} = \frac{1 \times 24}{720} = \frac{1}{30}$. Par le changement de variable $u = 1 - \theta$ : $\int_0^1 \theta(1 - \theta)^4\,d\theta = \int_0^1 (1 - u)u^4\,du = \frac{1}{5} - \frac{1}{6} = \frac{1}{30}$.
- b) $30 \times 0{,}2 \times 0{,}8^4 = 2{,}4576$. c) $\frac{2}{7}$. d) $\frac{2 - 1}{2 + 5 - 2} = \frac{1}{5}$.
- e) $\frac{2 \times 5}{7^2 \times 8} = \frac{10}{392} = \frac{5}{196}$.
- f) $30\int_{0{,}5}^1 (1 - u)u^4\,du = 30\Big[\frac{u^5}{5} - \frac{u^6}{6}\Big]_{0{,}5}^1 = 1 - 30\Big(\frac{0{,}5^5}{5} - \frac{0{,}5^6}{6}\Big) = 1 - \frac{7}{64} = \frac{57}{64} \approx 0{,}8906$.
- g) $\int_0^1 \theta^2(1 - \theta)\,d\theta = \frac{1}{3} - \frac{1}{4} = \frac{1}{12}$ : $c = 12 = \frac{1}{B(3, 2)}$.
- h) $\frac{a}{8} = 0{,}25$ : $a = 2$, $b = 6$.

**Erreurs fréquentes.** $B(a, b) = \frac{a!\,b!}{(a + b)!}$ ($\frac{1}{21}$) au lieu de $\frac{(a - 1)!\,(b - 1)!}{(a + b - 1)!}$ ; les exposants $a$ et $b$ au lieu de $a - 1$ et $b - 1$ ; échanger mode et moyenne ; f) calculé comme la densité en 0,5.

**Variante.** Pour $\mathrm{Beta}(3, 4)$ : $B(3, 4)$, la moyenne et le mode ? *Réponse* : $\frac{1}{60}$, $\frac{3}{7}$ et $\frac{2}{5}$.

### Ex M04.6 — Conjugaison : de Beta(a, b) à Beta(a + k, b + n − k)

**Réponses** : a) `[11, 69]` · b) `0.1375` · c) `0.625` · d) `[17, 113]` · e) `0.1308` · f) `0.0383` · g) `0.1462` · h) `270`.

**Démarche.**
- a) Les retours sont les « succès » pour $\theta$ : $\mathrm{Beta}(3 + 8,\ 27 + 42)$. b) $\frac{11}{80}$. c) $\frac{50}{30 + 50}$.
- d) $\mathrm{Beta}(11 + 6,\ 69 + 44)$. e) $\frac{17}{130} \approx 0{,}1308$.
- f) $\sqrt{\frac{11 \times 69}{80^2 \times 81}} = \sqrt{0{,}001464} \approx 0{,}0383$.
- g) $\mathrm{Beta}(9{,}5 ;\ 55{,}5)$, de moyenne $\frac{9{,}5}{65} \approx 0{,}1462$. h) $\frac{n}{30 + n} \ge 0{,}9 \iff n \ge 270$.

Pour la copie : $\frac{11}{80} = \frac{30}{80} \times \frac{3}{30} + \frac{50}{80} \times \frac{8}{50} = 0{,}0375 + 0{,}1 = 0{,}1375$. L'a priori moins sûr ($a + b = 15$) laisse aux données le poids $\frac{50}{65} \approx 0{,}77$ : la moyenne se rapproche de la fréquence 0,16.

**Erreurs fréquentes.** Ajouter 50 à $b$ (toutes les ventes, au lieu des 42 gardées) ; échanger $a$ et $b$ ; repartir de l'a priori en d) ; donner la variance au lieu de l'écart-type.

**Variante.** Avec l'a priori de départ, 30 retours sur 200 ventes en tout : la moyenne a posteriori ? *Réponse* : $\frac{33}{230} \approx 0{,}1435$.

### Ex M04.7 — Lissage de Laplace : la prédictive avec Beta(1, 1)

**Réponses** : a) `"1/6"` · b) `"6/7"` · c) `0.1` · d) `"1/12"` · e) `"1/21"` · f) `"2/7"`.

**Démarche.**
- a) $\mathrm{Beta}(1, 5)$ : $\frac{0 + 1}{4 + 2} = \frac{1}{6}$. b) $\mathrm{Beta}(6, 1)$ : $\frac{6}{7}$. c) $\frac{0 + 0{,}5}{4 + 1} = 0{,}1$. d) $\frac{0 + 1}{9 + 3} = \frac{1}{12}$.
- e) Le premier achat a la probabilité $\frac{1}{6}$ ; après lui, la loi devient $\mathrm{Beta}(2, 5)$ et le second a la probabilité $\frac{2}{7}$ : $\frac{1}{6} \times \frac{2}{7} = \frac{1}{21}$ (c'est aussi $\frac{B(3, 5)}{B(1, 5)}$).
- f) Aucun achat : $\frac{5}{6} \times \frac{6}{7} = \frac{5}{7}$, donc au moins un : $\frac{2}{7}$.

Pour la copie : le maximum de vraisemblance donnerait 0 et 1, « jamais d'achat » et « toujours un achat » après 4 ou 5 visites : une page notée 0 ne serait plus jamais montrée, et un $\ln 0$ ferait exploser une log-loss. e) n'est pas $\big(\frac{1}{6}\big)^2$ : un achat rend le suivant plus probable, parce qu'il renseigne sur $\theta$ ($P(\text{deux achats}) = \mathbb{E}[\theta^2] > \mathbb{E}[\theta]^2$).

**Erreurs fréquentes.** $\frac{k + 1}{n + 1}$ ; oublier la mise à jour entre les deux visites ($\frac{1}{36}$) ; ajouter 2 au lieu de $K = 3$ en d).

**Variante.** En d) avec $\alpha = 0{,}5$ ? *Réponse* : $\frac{0{,}5}{9 + 1{,}5} = \frac{1}{21} \approx 0{,}048$.

### Ex M04.8 — MAP, maximum de vraisemblance et moyenne a posteriori

**Réponses** : a) `0.9` · b) `0.7222` · c) `0.7` · d) `0.9` · e) `0.8333` · f) `0.7` · g) `0.2` · h) `13`.

**Démarche.**
- a) $\frac{9}{10}$. b) $\mathrm{Beta}(14, 6)$ : $\frac{13}{18} \approx 0{,}7222$. c) $\frac{14}{20}$. d) $\mathrm{Beta}(10, 2)$ : $\frac{9}{10}$. e) $\frac{10}{12}$. f) $0{,}7 < 0{,}722 < 0{,}9$.
- g) $\mathrm{Beta}(2, 5)$ : $\frac{1}{5}$ (le maximum de vraisemblance vaudrait 0).
- h) $\mathrm{Beta}(5 + n, 5)$ : $\frac{4 + n}{8 + n} > 0{,}8 \iff 4 + n > 6{,}4 + 0{,}8\,n \iff n > 12$, donc 13 ($n = 12$ donne exactement $\frac{16}{20} = 0{,}8$).

Pour la copie : moyenne $<$ MAP $<$ maximum de vraisemblance. L'a priori tire vers 0,5 ; la moyenne $\frac{5 + 9}{10 + 10}$ se comporte comme 10 pseudo-observations, le MAP $\frac{4 + 9}{8 + 10}$ comme 8 : la moyenne est tirée un peu plus fort. Avec 900 adoptions sur 1 000 : 0,9 ; $\frac{904}{1008} \approx 0{,}897$ ; $\frac{905}{1010} \approx 0{,}896$ : l'a priori ne compte presque plus.

**Erreurs fréquentes.** Confondre le MAP et la moyenne ; oublier « strictement » en h).

**Variante.** Avec l'a priori $\mathrm{Beta}(2, 8)$ et 9 adoptions sur 10 : le MAP et la moyenne ? *Réponse* : $\frac{10}{18} \approx 0{,}556$ et $\frac{11}{20} = 0{,}55$.

### Ex M04.9 — Un intervalle de crédibilité d'une loi Beta

**Réponses** : a) `[1, 9]` · b) `0.6126` · c) `0.00281` · d) `0.3363` · e) `0.2831` · f) `0.0741` · g) `[0.2924, 0.9916]`.

**Démarche.**
- a) 0 défaut, 8 fabrications sans défaut : $\mathrm{Beta}(1 + 0,\ 1 + 8)$. b) $F(0{,}1) = 1 - 0{,}9^9 \approx 0{,}6126$.
- c) $1 - (1 - x)^9 = 0{,}025 \iff x = 1 - 0{,}975^{1/9} \approx 0{,}00281$. d) $x = 1 - 0{,}025^{1/9} \approx 0{,}3363$.
- e) $x = 1 - 0{,}05^{1/9} \approx 0{,}2831$. f) $x = 1 - 0{,}5^{1/9} \approx 0{,}0741$.
- g) $x^3 = 0{,}025$ et $x^3 = 0{,}975$ : $0{,}2924$ et $0{,}9916$.

Pour la copie : $F(x) = \int_0^x 9(1 - t)^8\,dt = \big[-(1 - t)^9\big]_0^x = 1 - (1 - x)^9$. La densité $9(1 - \theta)^8$ décroît : la masse est tassée près de 0, avec une longue queue à droite ; la médiane (0,074) est sous la moyenne $\frac{1}{10}$, et l'intervalle s'étend bien plus à droite. Le maximum de vraisemblance dirait 0, « jamais de défaut » ; l'intervalle dit qu'un taux jusqu'à 34 % reste plausible après 8 fabrications seulement.

**Erreurs fréquentes.** Échanger les bornes basse et haute (résoudre $F(x) = 0{,}975$ pour la borne basse) ; écrire $F(x) = (1 - x)^b$ ; donner la moyenne pour la médiane.

**Variante.** Après 18 fabrications sans défaut, la borne supérieure à 95 % ? *Réponse* : $1 - 0{,}05^{1/19} \approx 0{,}146$.

### Ex M04.10 — Log-probabilités : additionner au lieu de multiplier, normaliser par log-sum-exp

**Réponses** : a) `-804.72` · b) `-349.485` · c) `True` · d) `-999.651` · e) `[0.7054, 0.2595, 0.0351]` · f) `[0.5014, 0.4611, 0.0374]`.

**Démarche.**
- a) $500\ln 0{,}2 \approx 500 \times (-1{,}60944)$. b) $500\log_{10} 0{,}2 \approx 500 \times (-0{,}69897)$.
- c) $0{,}2^{500} \approx 10^{-349{,}5}$, bien moins que $5 \times 10^{-324}$ : oui, 0.0 en `float64`.
- d) $-1000 + \ln(1 + e^{-1} + e^{-3}) = -1000 + \ln 1{,}41767 \approx -1000 + 0{,}349$.
- e) $\frac{(1 ;\ e^{-1} ;\ e^{-3})}{1{,}41767} = (1 ;\ 0{,}36788 ;\ 0{,}04979) / 1{,}41767$.
- f) Log-produits : $\ln 0{,}2 - 1000 \approx -1001{,}609$, $\ln 0{,}5 - 1001 \approx -1001{,}693$, $\ln 0{,}3 - 1003 \approx -1004{,}204$ ; moins le maximum : $(0 ;\ -0{,}084 ;\ -2{,}595)$ ; exponentielles : $(1 ;\ 0{,}920 ;\ 0{,}075)$, de somme 1,994 ; d'où $(0{,}5014 ;\ 0{,}4611 ;\ 0{,}0374)$.

Pour la copie : $e^{-1000} \approx 10^{-434}$ vaut 0 en `float64` : le calcul direct normaliserait $\frac{0}{0}$ et donnerait `nan`.

**Erreurs fréquentes.** $\log_{10}$ au lieu de $\ln$ ; écrire $\ln(e^x + e^y) = x + y$ ; oublier l'a priori en f).

**Variante.** $\ln\big(e^{-700} + e^{-700} + e^{-700}\big)$ ? *Réponse* : $-700 + \ln 3 \approx -698{,}901$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M04.11 — La conjugaison Beta-binomiale, démontrée

**Réponse modèle.**
1. $P(K = k \mid \theta) = \binom{n}{k}\theta^k(1 - \theta)^{n - k}$ et $f(\theta) = \frac{\theta^{a - 1}(1 - \theta)^{b - 1}}{B(a, b)}$, donc $P(K = k \mid \theta)\,f(\theta) = \frac{\binom{n}{k}}{B(a, b)}\,\theta^{a + k - 1}(1 - \theta)^{b + n - k - 1}$.
2. $P(K = k)$ est une intégrale sur $\theta$ : elle ne dépend pas de $\theta$. Donc $f(\theta \mid k) = c\,\theta^{a + k - 1}(1 - \theta)^{b + n - k - 1}$, avec $c = \frac{\binom{n}{k}}{B(a, b)\,P(K = k)}$, une constante.
3. $f(\theta \mid k)$ est une densité sur $[0, 1]$ : son intégrale vaut 1. Or $\int_0^1 \theta^{a + k - 1}(1 - \theta)^{b + n - k - 1}\,d\theta = B(a + k,\ b + n - k)$, donc $c = \frac{1}{B(a + k,\ b + n - k)}$ : c'est la densité de $\mathrm{Beta}(a + k,\ b + n - k)$. L'argument : une densité est déterminée par sa forme, la constante est fixée par l'aire 1.
4. En égalant les deux expressions de $c$ : $P(K = k) = \binom{n}{k}\frac{B(a + k,\ b + n - k)}{B(a, b)}$, la loi prédictive (bêta-binomiale) de la fiche (§5).
5. $\frac{a + k}{a + b + n} = \frac{a + b}{a + b + n} \cdot \frac{a}{a + b} + \frac{n}{a + b + n} \cdot \frac{k}{n}$ : poids $\frac{a + b}{a + b + n}$ pour la moyenne a priori, $\frac{n}{a + b + n}$ pour la fréquence.
6. Le poids des données tend vers 1 : la moyenne tend vers $p$. La variance $\frac{(a + k)(b + n - k)}{(a + b + n)^2(a + b + n + 1)}$ se comporte comme $\frac{np \cdot n(1 - p)}{n^3} = \frac{p(1 - p)}{n}$ : elle tend vers 0. L'a priori est oublié, et l'a posteriori se concentre autour de la fréquence, avec un écart-type en $\frac{1}{\sqrt{n}}$.
7. $\prod_i e^{-\lambda}\frac{\lambda^{x_i}}{x_i!} \propto \lambda^{\sum_i x_i}e^{-n\lambda}$, donc l'a posteriori est proportionnel à $\lambda^{\alpha + \sum_i x_i - 1}e^{-(\beta + n)\lambda}$ : la loi Gamma de paramètres $\alpha + \sum_i x_i$ et $\beta + n$ (même argument qu'en 3).

**Grille.** (1) le produit, avec les exposants regroupés ; (2) l'évidence ne dépend pas de $\theta$ ; (3) l'argument de la constante fixée par l'aire 1 (sans calculer d'intégrale) ; (4) la loi bêta-binomiale obtenue en égalant les constantes ; (5) la moyenne pondérée, avec ses poids ; (6) les limites de la moyenne et de la variance, et l'interprétation ; (7) Gamma-Poisson : $\alpha + \sum x_i$ et $\beta + n$.

### Ex M04.12 — Le maximum de vraisemblance d'une loi de Bernoulli est la fréquence

**Réponse modèle.**
1. Chaque facteur $\theta^{x_i}(1 - \theta)^{1 - x_i}$ vaut $\theta$ si $x_i = 1$ et $1 - \theta$ si $x_i = 0$ : le produit a $k$ facteurs $\theta$ et $n - k$ facteurs $1 - \theta$. Il suffit de connaître $n$ et $k$ : $k$ est une statistique suffisante.
2. $\ell(\theta) = k\ln\theta + (n - k)\ln(1 - \theta)$ et $\ell'(\theta) = \frac{k}{\theta} - \frac{n - k}{1 - \theta} = \frac{k - n\theta}{\theta(1 - \theta)}$. $\ell'$ s'annule en $\frac{k}{n}$, est positive avant et négative après : $\ell$, donc $L = e^\ell$, croît puis décroît sur $]0, 1[$, avec son maximum en $\frac{k}{n}$. Aux bords, $L(0) = L(1) = 0 < L\big(\frac{k}{n}\big)$ (car $0 < k < n$) : c'est le maximum sur $[0, 1]$.
3. $k = 0$ : $L(\theta) = (1 - \theta)^n$ décroît sur $[0, 1]$, maximum en $0 = \frac{0}{n}$. $k = n$ : $\theta^n$ croît, maximum en $1 = \frac{n}{n}$. Dans tous les cas, $\hat{\theta} = \frac{k}{n}$.
4. $\mathbb{E}[\hat{\theta}] = \frac{1}{n}\sum_i \mathbb{E}[X_i] = \theta$ : sans biais. Par indépendance, $\mathbb{V}(\hat{\theta}) = \frac{1}{n^2}\sum_i \mathbb{V}(X_i) = \frac{\theta(1 - \theta)}{n}$.
5. Son écart-type $\sqrt{\frac{\theta(1 - \theta)}{n}}$, estimé par $\sqrt{\frac{\hat{\theta}(1 - \hat{\theta})}{n}}$, est l'erreur type d'une proportion de M02c.
6. L'a posteriori $\mathrm{Beta}(a + k,\ b + n - k)$ a ses deux paramètres plus grands que 1 : son mode est $\frac{a + k - 1}{a + b + n - 2}$ (fiche §6). À fréquence $p = \frac{k}{n}$ fixée, $\frac{a - 1 + np}{a + b - 2 + n} \to p$, et l'écart au maximum de vraisemblance vaut $\frac{(a - 1) - p(a + b - 2)}{n + a + b - 2}$, qui tend vers 0 comme $\frac{1}{n}$.
7. $\ell(\mu) = -n\mu + \big(\sum_i x_i\big)\ln\mu - \sum_i \ln(x_i!)$, $\ell'(\mu) = -n + \frac{\sum_i x_i}{\mu}$, nulle en $\mu = \bar{x}$ ; $\ell''(\mu) = -\frac{\sum_i x_i}{\mu^2} < 0$ : c'est le maximum.

**Grille.** (1) le produit et la statistique suffisante ; (2) la dérivée, son signe (pas seulement son zéro), et les bords ; (3) les cas $k = 0$ et $k = n$ traités sans $\ln 0$ ; (4) biais et variance, l'indépendance citée ; (5) le lien avec l'erreur type ; (6) la formule du MAP et sa limite ; (7) Poisson : la moyenne.

### Ex M04.13 — Le mode de la loi Beta

**Réponse modèle.**
1. $g'(\theta) = \frac{a - 1}{\theta} - \frac{b - 1}{1 - \theta} = \frac{(a - 1) - (a + b - 2)\theta}{\theta(1 - \theta)}$, nulle en $\theta^* = \frac{a - 1}{a + b - 2} \in\ ]0, 1[$, positive avant, négative après. La densité $\frac{e^{g}}{B(a, b)}$ a les variations de $g$ : maximum en $\theta^*$. Aux bords, $\theta^{a - 1} \to 0$ et $(1 - \theta)^{b - 1} \to 0$ : la densité vaut 0.
2. Les dénominateurs étant positifs : $\frac{a - 1}{a + b - 2} < \frac{a}{a + b} \iff (a - 1)(a + b) < a(a + b - 2) \iff -a - b < -2a \iff a < b$. Si $a = b$, mode et moyenne valent $\frac{1}{2}$.
3. $B(1, b) = \frac{1}{b}$, donc la densité est $b(1 - \theta)^{b - 1}$, décroissante car $b - 1 > 0$ : mode 0.
4. $\theta^{a - 1} \to +\infty$ en $0^+$ (exposant négatif). $g'(\theta) = \frac{a - 1}{\theta} - \frac{b - 1}{1 - \theta}$ est une somme de deux termes négatifs : la densité décroît, et son maximum est au bord 0 (où elle est infinie) : mode 0.
5. $g'$ s'annule en $\theta^* = \frac{1 - a}{2 - a - b} \in\ ]0, 1[$. Son numérateur $(a - 1) - (a + b - 2)\theta$ vaut $a - 1 < 0$ en 0 et croît (le coefficient de $\theta$, $2 - a - b$, est positif) : $g$ décroît puis croît, $\theta^*$ est un **minimum**. La densité tend vers l'infini en 0 et en 1 : deux modes, aux bords.
6. La densité vaut 1 partout : chaque point est un maximum.
7. Si $0 < k < n$, les deux paramètres de $\mathrm{Beta}(k + 1,\ n - k + 1)$ dépassent 1 : mode $\frac{k}{n}$, le maximum de vraisemblance. Si $k = 0$ (et $n \ge 1$) : $a = 1 < b = n + 1$, mode $0 = \frac{0}{n}$ par 3. De même, $k = n$ donne 1.

**Grille.** (1) la dérivée de $g$ mise sous un même dénominateur, son signe, les valeurs aux bords ; (2) l'équivalence démontrée dans les deux sens (par équivalences successives) ; (3) et (4) la monotonie justifiée ; (5) le point critique identifié comme un minimum ; (6) la loi uniforme ; (7) le cas $k = 0$ traité par 3, pas par la formule.

<a id="reflexion"></a>

## 🔗 📖 🗣️ Pont, lecture et explication

### Ex M04.14 — Un test A/B : deux taux de conversion et P(θB > θA) par simulation

**Réponses** : a) `[31, 271]` · b) `0.1523` · c) `0.0206` · d) `0.0174` · e) `0.97` · f) `0.969` · g) `0.0498`.

**Démarche.**
- a) $\mathrm{Beta}(1 + 30,\ 1 + 270)$ ; pour B, $\mathrm{Beta}(46, 256)$. b) $\frac{46}{302}$.
- c) $\sqrt{\frac{46 \times 256}{302^2 \times 303}} = \sqrt{0{,}000426} \approx 0{,}0206$. d) $\sqrt{\frac{31 \times 271}{302^2 \times 303}} = \sqrt{0{,}000304} \approx 0{,}0174$.
- e) $\theta_B - \theta_A$ est approchée par une loi normale de moyenne $\frac{46 - 31}{302} \approx 0{,}0497$ et d'écart-type $\sqrt{0{,}000426 + 0{,}000304} \approx 0{,}0270$ ; $P(\theta_B - \theta_A > 0) = \Phi\big(\frac{0{,}0497}{0{,}0270}\big) = \Phi(1{,}84) \approx 0{,}97$.
- f) et g) La simulation : 0,9687 et 0,04976. La valeur exacte, par intégration numérique, est 0,9674 : l'approximation normale (0,9670) en est ici plus proche que la simulation, dont l'erreur type vaut $\sqrt{\frac{0{,}967 \times 0{,}033}{100\,000}} \approx 0{,}0006$ ; l'écart de 0,0013 fait un peu plus de deux erreurs types, ce qui arrive (une fois sur vingt environ).

Pour la copie : la différence de deux variables normales indépendantes est normale (M02b), de variance la somme des variances (M02c, l'indépendance). Une proportion estimée sur 100 000 tirages a une erreur type d'environ 0,0006 : e) et f) diffèrent de 0,0017, de l'ordre de quelques erreurs types, et la simulation n'est pas « plus exacte » par principe. Pour l'équipe : « Sachant ces données, la page B a environ 97 % de chances d'avoir un meilleur taux de conversion que la page A, avec un gain moyen d'environ 5 points. » Tout basculer sur B reste un pari : 3 % de chances qu'elle soit moins bonne, et un gain encore incertain (écart-type de 2,7 points). L'échantillonnage de Thompson montrerait B environ 97 % du temps et A environ 3 % : il exploite déjà B tout en continuant d'apprendre.

**Erreurs fréquentes.** Oublier l'a priori (`[30, 270]`) ; additionner les écarts-types au lieu des variances (0,90) ; taper en f) la valeur de e) ou la valeur exacte au lieu du résultat de la simulation.

**Variante.** Si B avait reçu 400 visites et 60 commandes (A inchangée), l'approximation normale de $P(\theta_B > \theta_A)$ ? *Réponse* : environ 0,975.

### Ex M04.15 — MML §6.3 (relire le théorème de Bayes) et §6.6 : conjugaison et famille exponentielle (lecture guidée)

**Éléments de réponse.**
1. *Prior* (a priori), *likelihood* (vraisemblance, que le livre appelle aussi modèle de mesure), *posterior* (a posteriori) et *marginal likelihood* ou *evidence* (évidence). C'est l'évidence qui est difficile : c'est une intégrale (ou une somme) sur toutes les valeurs du paramètre, souvent impossible à calculer exactement en grande dimension.
2. Le dénominateur ne dépend pas du paramètre : pour comparer des valeurs du paramètre, ou trouver le maximum de l'a posteriori, la proportionnalité suffit ; la constante ne sert qu'à normaliser.
3. Un a priori est conjugué pour une vraisemblance si l'a posteriori appartient à la même famille que l'a priori : la mise à jour ne fait que changer ses paramètres. Dans l'exemple Beta-binomial : a priori $\mathrm{Beta}(\alpha, \beta)$, $h$ succès sur $N$ essais, a posteriori $\mathrm{Beta}(\alpha + h,\ \beta + N - h)$, la règle de la fiche (§5).
4. Par exemple, la vraisemblance gaussienne (moyenne inconnue) avec un a priori gaussien ; la multinomiale avec l'a priori de Dirichlet (la généralisation de la loi Beta à $K$ catégories).
5. Une statistique suffisante contient toute l'information des données sur le paramètre : la vraisemblance ne dépend des données qu'à travers elle. Pour $n$ essais de Bernoulli, le nombre de succès (M04.12).
6. $p(x \mid \boldsymbol{\theta}) = h(x)\exp\big(\langle \boldsymbol{\theta}, \boldsymbol{\phi}(x) \rangle - A(\boldsymbol{\theta})\big)$. Pour la loi de Bernoulli de paramètre $\mu$ : paramètre naturel $\theta = \ln\frac{\mu}{1 - \mu}$ (le logit), statistique $\phi(x) = x$, fonction de normalisation $A(\theta) = \ln(1 + e^{\theta}) = -\ln(1 - \mu)$, et $\mu$ se retrouve par la sigmoïde de $\theta$. C'est l'écriture de la fiche (§7), avec $\eta$ pour le paramètre naturel.
7. Par exemple : *conjugate prior* (a priori conjugué), *closed form* (forme explicite, sans approximation), *sufficient statistic* (statistique suffisante), *log-partition function* (le logarithme de la constante de normalisation).

### Ex M04.16 — MML §8.3 : maximum de vraisemblance et MAP (lecture guidée)

**Éléments de réponse.**
1. Choisir les paramètres qui rendent les données observées les plus probables, c'est-à-dire qui maximisent la vraisemblance. Le livre minimise moins la log-vraisemblance : le logarithme change le produit en somme, et l'habitude de l'optimisation est de **minimiser** une fonction de coût (une loss).
2. Avec un bruit gaussien de variance fixée, moins la log-vraisemblance vaut, à une constante et un facteur près, la somme des carrés des erreurs : la méthode des moindres carrés.
3. Maximiser l'a posteriori, proportionnel à vraisemblance × a priori ; en logarithmes, on minimise moins la log-vraisemblance **plus** moins le logarithme de l'a priori.
4. Avec un a priori gaussien centré, moins son logarithme est proportionnel au carré de la norme des paramètres : c'est la régularisation $\ell_2$ (*weight decay*, la régression *ridge*).
5. A priori $\mathrm{Beta}(2, 8)$, 2 échecs sur 12 ($\theta$ est le taux d'échec) : l'a posteriori est $\mathrm{Beta}(4, 18)$, et $-\ln f(\theta \mid \text{données}) = -3\ln\theta - 17\ln(1 - \theta) + C$. La dérivée $-\frac{3}{\theta} + \frac{17}{1 - \theta}$ s'annule en $\theta = \frac{3}{20} = 0{,}15$ : on retrouve le MAP de la fiche.
6. Avec peu de données, le maximum de vraisemblance peut sur-ajuster (*overfitting*) : il colle aux particularités de l'échantillon (un taux de 0 après quelques essais, des paramètres extrêmes). L'a priori du MAP pénalise ces valeurs et agit comme une régularisation.
7. Par exemple : *negative log-likelihood* (moins la log-vraisemblance), *point estimate* (estimation ponctuelle), *regularizer* (terme de régularisation).

### Ex M04.17 — Expliquer la conjugaison avec des pseudo-observations

**Réponse modèle.**

> Ce calcul est la moyenne a posteriori avec l'a priori $\mathrm{Beta}(2, 8)$ : avant toute donnée, on fait comme si l'on avait déjà vu 10 affichages, dont 2 clics, ce qui dit « un taux autour de 20 % », d'après nos autres publicités. Ce n'est pas truquer, c'est écrire ce qu'on sait déjà. Ces 10 affichages imaginaires pèsent 10 contre $n$ vrais : après 1 000 affichages, ils ne changent presque rien. Ils servent au début : avec 1 clic sur 2 affichages, la fréquence dirait 50 %, alors que $\frac{1 + 2}{2 + 10} = 25\,\%$ est plus raisonnable, et 0 clic sur 3 ne donne pas un taux nul. Si l'on ne sait rien, on prend 1 et 2 (Laplace).

**Grille.** (1) l'a priori $\mathrm{Beta}(2, 8)$ et la lecture « 2 clics sur 10 affichages déjà vus » ; (2) le poids qui diminue quand les données s'accumulent ; (3) l'utilité au début (peu de données, comptages nuls) ; (4) huit lignes au plus, sans formule compliquée.

<a id="entretien"></a>

## 💼 Entretien

### M04.E1 — Qu'est-ce que le lissage de Laplace, et pourquoi l'utiliser ?

**Réponse modèle (60 secondes).**

> Le lissage de Laplace ajoute 1 à chaque comptage avant de calculer une fréquence : pour deux issues, $\frac{k + 1}{n + 2}$ au lieu de $\frac{k}{n}$ ; pour $K$ catégories, $\frac{n_j + 1}{n + K}$. Il évite les probabilités nulles : un mot jamais vu dans les spams d'entraînement aurait une probabilité 0, et dans un classifieur naïf de Bayes, ce seul mot annulerait tout le produit, ou donnerait $\ln 0 = -\infty$. Son interprétation bayésienne : c'est la moyenne a posteriori avec un a priori uniforme, $\mathrm{Beta}(1, 1)$, ou Dirichlet à $K$ catégories, comme si l'on avait vu chaque issue une fois. Variante : ajouter $\alpha$ au lieu de 1, avec $\alpha = 0{,}5$ ou plus petit ; c'est un hyperparamètre qu'on règle sur un jeu de validation. Limite : avec un vocabulaire immense, ajouter 1 à chaque mot donne trop de masse aux mots jamais vus.

**Grille.** (1) les deux formules ; (2) le problème des comptages nuls, avec un exemple (Naïve Bayes, log-loss) ; (3) l'a priori uniforme et la moyenne a posteriori ; (4) une variante ($\alpha$) ou une limite (grand vocabulaire).

<a id="notebook"></a>

## Notebook

### Ex M04.18 — Densité et moments de la loi Beta (avec `math.lgamma`) · `beta_pdf, beta_moments`

**Réponses** : a) `2.1177` · b) `0.0` · c) `6.0` · d) `True` · e) `21.241` · f) `[0.25, 0.0144]` · g) `"ValueError"` · h) `"float"`.

**Démarche.** `_check_parameters(a, b)` lève une `ValueError` sauf si `a > 0 and b > 0` (écrit ainsi, il refuse aussi `nan`). `beta_pdf` : `0.0` hors de $[0, 1]$ ; aux bords, le facteur qui rencontre $0^{\text{exposant}}$ décide (0 si l'exposant est positif, `math.inf` s'il est négatif, $\frac{1}{B(1, \cdot)}$ s'il est nul) ; à l'intérieur, `math.exp((a - 1) * math.log(x) + (b - 1) * math.log1p(-x) - log_beta)` avec `log_beta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)`. `beta_moments` : `float(a / (a + b))` et `float(a * b / ((a + b) ** 2 * (a + b + 1)))`. Pour la copie : a) $42 \times 0{,}3 \times 0{,}7^5$ ; c) $\frac{1}{B(1, 6)} = 6$ ; f) $\frac{27}{1872}$ ; e) une loi très concentrée a une densité haute, son aire reste 1.

**Erreurs fréquentes.** `math.gamma` (une `OverflowError` pour e) ; `x ** (a - 1)` en $x = 0$ avec $a < 1$ (`ZeroDivisionError`), ou `math.log(0)` en $x = 1$ ; oublier les bords ou l'extérieur ; renvoyer un `numpy.float64`, ou l'entier `0` hors de $[0, 1]$ (h).

### Ex M04.19 — Mise à jour conjuguée et loi prédictive des prochains essais · `conjugate_beta_update, posterior_predictive`

**Réponses** : a) `[7, 13]` · b) `True` · c) `0.35` · d) `0.2364` · e) `0.0` · f) `1.0` · g) `"ValueError"` · h) `0.1339`.

**Démarche.** `conjugate_beta_update` : vérifier les paramètres et `successes >= 0 and failures >= 0`, puis `return a + successes, b + failures` (sans `float`). `posterior_predictive` : vérifier `a`, `b` et `n >= 0` ; `0.0` si `k < 0 or k > n` (avant tout `lgamma`, qui refuse 0 et les entiers négatifs) ; puis l'exponentielle de $\ln\binom{n}{k} + \ln B(a + k,\ b + n - k) - \ln B(a, b)$. Pour la copie : c) $\frac{7}{20}$ ; d) $3 \times \frac{7 \times 8 \times 13}{20 \times 21 \times 22} = \frac{13}{55}$, contre $3 \times 0{,}35^2 \times 0{,}65 \approx 0{,}2389$ pour la binomiale : la prédictive tient compte de l'incertitude sur $\theta$, et les essais futurs ne sont pas indépendants sachant les seules données.

**Erreurs fréquentes.** Ajouter $n$ au lieu des échecs à $b$ ; oublier $\binom{n}{k}$ ; calculer $\Gamma$ directement (une `OverflowError` en h) ; tester `k > n` après l'appel à `lgamma`.

### Ex M04.20 — Le MAP d'une loi Beta, cas limites compris · `map_estimate_beta`

**Réponses** : a) `0.3333` · b) `0.0` · c) `1.0` · d) `0.0` · e) `"ValueError"` · f) `0.1885` · g) `"float"` · h) `0.2`.

**Démarche.** Dans cet ordre : vérifier les paramètres ; si `a > 1 and b > 1`, la formule ; si `a == b == 1` ou `a < 1 and b < 1`, une `ValueError` ; sinon `0.0` si `a <= 1 < b` ou `a < 1 == b` (densité décroissante), `1.0` sinon (croissante). Pour la copie : b) et d) décroissent, c) croît, e) est en U ; h) $\frac{4}{20}$, le maximum de vraisemblance (a priori uniforme).

**Erreurs fréquentes.** Appliquer la formule partout ($-0{,}25$ en b), 1 en d), 1,11 en c) ; renvoyer l'entier `0` ; renvoyer la moyenne.

### Ex M04.21 — La fonction Beta avec `scipy.special` : `beta`, `betaln` et l'underflow

**Réponses** : a) `840` · b) `True` · c) `-1011.54` · d) `-439.31` · e) `0.1602` · f) `1.1447`.

**Démarche.** Voir `05_solutions.ipynb`. a) $B(4, 7) = \frac{3!\,6!}{10!} = \frac{1}{840}$. b) $B(600, 900) \approx 10^{-439}$ : 0 en `float64`. c) `special.betaln(600, 900)`. d) c) divisé par $\ln 10$. e) `math.exp(special.betaln(602, 900) - special.betaln(600, 900))` $= \frac{600 \times 601}{1500 \times 1501} \approx 0{,}1602$, comme `posterior_predictive(600, 900, 2, 2)`. f) $\ln \pi$. Pour la copie : le quotient direct vaut $\frac{0}{0}$, donc `nan` ; l'exponentielle de f) vaut $\pi = B(\frac{1}{2}, \frac{1}{2})$.

**Erreurs fréquentes.** Croire `special.beta(600, 900)` positif ; prendre $\log_{10}$ pour c) ; calculer e) par le quotient direct.

### Ex M04.22 — Prédire : le MAP avec Beta(1, 1) après trois échecs

**Réponses** : a) `1` · b) `2` · c) `2` · d) `3` · e) `3`.

**Démarche.** L'a posteriori $\mathrm{Beta}(1, 4)$ a la densité $4(1 - \theta)^3$, décroissante : a) mode 0 ; b) moyenne $\frac{1}{5}$ (Laplace) ; c) $\mathrm{Beta}(2, 5)$ a pour mode $\frac{1}{5}$ ; d) $\frac{1}{5} \times \frac{2}{6} = \frac{1}{15}$ ; e) $1 - 0{,}5^4 = 0{,}9375$. Le MAP avec l'a priori uniforme est le maximum de vraisemblance, ici 0 : une estimation à ne pas annoncer après trois essais.

### Ex M04.23 — Le posterior se resserre : la largeur de l'intervalle en 1/√n

**Réponses** : a) `0.5` · b) `0.0355` · c) `1.95` · d) `-0.48` · e) `1.8` · f) `1290` · g) `0.17`.

**Démarche.** `low, high = stats.beta(a + k, b + n - k).ppf([0.025, 0.975])`, puis `float(high - low)`. Pour la copie : multiplier $n$ par 4 divise la largeur par environ 2 (1,82 ; 1,95 ; 1,99 ; 2,00) ; l'écart-type de l'a posteriori est proche de $\sqrt{\frac{0{,}21}{n}}$, et la largeur de $2 \times 1{,}96 \times \sqrt{\frac{0{,}21}{n}}$, d'où e) $\approx 2 \times 1{,}96 \times \sqrt{0{,}21} \approx 1{,}80$. La pente n'est pas exactement $-0{,}5$ : pour $n = 10$, l'approximation normale est grossière et l'a priori pèse encore. g) L'a priori $\mathrm{Beta}(30, 70)$ vaut 100 essais imaginaires.

**Erreurs fréquentes.** Les quantiles 0,05 et 0,95 (un intervalle à 90 %) ; oublier l'a priori ($\mathrm{Beta}(k, n - k)$) ; une mise à jour à l'envers, invisible avec l'a priori uniforme (les deux lois sont symétriques l'une de l'autre, de même largeur) mais pas en g) ; renvoyer les deux bornes au lieu de la largeur.

### Ex M04.24 — Prior, vraisemblance et posterior sur une même figure

**Démarche.** Une grille `theta = np.linspace(0, 1, 501)` ; trois `ax.plot(theta, stats.beta(...).pdf(theta), label=...)` pour $\mathrm{Beta}(a, b)$, $\mathrm{Beta}(k + 1,\ n - k + 1)$ et $\mathrm{Beta}(a + k,\ b + n - k)$ ; `ax.legend()` et `ax.set_xlabel("θ")`. Pour la copie : l'a posteriori $\mathrm{Beta}(15, 20)$ est entre les deux, plus près de l'a priori (20 pseudo-observations contre 15 visites), et plus étroit qu'eux ; avec 90 sur 150, il se collerait à la vraisemblance.

**Erreurs fréquentes.** Tracer la vraisemblance sans la normaliser (une courbe minuscule, invisible à côté des densités) ; oublier les labels ; ouvrir une nouvelle figure dans la fonction.

### Ex M04.25 — Chasse à l'erreur : évidence oubliée, mise à jour à l'envers, mode et moyenne

**Réponses** : a) `"ABDF"` · b) `[55, 0.5, 0.08, 0.069, 0.083, 0.083]`.

**Démarche.** (A) met la mise à jour à l'envers : les 3 pièces défectueuses vont à $a$, les 37 bonnes à $b$, $b = 18 + 37 = 55$. (B) oublie l'évidence : $\frac{0{,}04}{0{,}08} = 0{,}5$, avec l'évidence de la ligne (C), juste. (D) calcule la moyenne au lieu du mode : $\frac{4}{58} \approx 0{,}069$. (E) est juste : $\frac{5}{60}$. (F) donne le maximum de vraisemblance ; la prédictive est la moyenne a posteriori $\frac{5}{60}$.

**Erreurs fréquentes.** Accuser (C) (c'est bien l'évidence) ou (E) ; en b), donner $\frac{3}{40}$ pour (F).

### Ex M04.26 — Un calcul stable : comparer des vraisemblances en logarithmes (`math.lgamma`)

**Démarche.** Dans cet ordre : `ValueError` si $p$ est hors de $[0, 1]$ ; `-math.inf` si $k < 0$ ou $k > n$ ; les cas $p = 0$ (0.0 si $k = 0$, sinon `-math.inf`) et $p = 1$ (0.0 si $k = n$) ; sinon `math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1) + k * math.log(p) + (n - k) * math.log1p(-p)`. Pour la copie : log-vraisemblances $-23{,}73$, $-6{,}89$ et $-6{,}87$ ; moins le maximum : $(-16{,}86 ;\ -0{,}02 ;\ 0)$ ; exponentielles $(4{,}7 \times 10^{-8} ;\ 0{,}980 ;\ 1)$ ; a posteriori $(2{,}4 \times 10^{-8} ;\ 0{,}495 ;\ 0{,}505)$. Un écart de 16,9 en logarithme est un rapport de $e^{16{,}9} \approx 2 \times 10^7$ : la première hypothèse est écartée ; un écart de 0,02 est un rapport de $e^{0{,}02} \approx 1{,}02$ : les deux autres restent presque à égalité.

**Erreurs fréquentes.** Ne pas vérifier $p$ (`math.log` refuse bien un négatif, mais laisse passer `nan`) ; `k * math.log(p)` avec $p = 0$ (une `ValueError` même pour $k = 0$) ; `math.comb(n, k) * p ** k * ...` (une `OverflowError`) ; renvoyer `0` au lieu de `-math.inf` pour une probabilité nulle.

### Ex M04.27 — Défi : traduire l'avis d'un expert en une loi Beta (moyenne, écart-type, intervalle)

**Réponses** : a) `[12.6, 50.4]` · b) `[6.9, 27.5]` · c) `0.9745` · d) `0.164` · e) `34.3`.

**Démarche.** a) $\frac{m(1 - m)}{s + 1} = 0{,}05^2$ donne $s + 1 = 64$, $s = 63$, puis $a = 0{,}2 \times 63$ et $b = 0{,}8 \times 63$. b) Deux équations, $F^{-1}(0{,}05) = 0{,}10$ et $F^{-1}(0{,}95) = 0{,}32$, résolues par `optimize.fsolve` (sur $\ln a$ et $\ln b$, pour rester positif) : $\mathrm{Beta}(6{,}87 ;\ 27{,}48)$. c) `cdf(0.32) - cdf(0.10)` pour la loi de a). d) $\frac{6{,}87 + 7}{34{,}34 + 50} \approx 0{,}164$. e) $6{,}87 + 27{,}48$. Pour la copie : même centre (0,20), mais le premier expert est plus sûr de lui (97 % dans l'intervalle du second, $a + b = 63$ contre 34) ; après 50 pièces, les données pèsent $\frac{50}{84{,}3} \approx 0{,}59$ face au second avis et $\frac{50}{113} \approx 0{,}44$ face au premier.

**Erreurs fréquentes.** Prendre l'écart-type pour la variance ; les quantiles 0,025 et 0,975 (un intervalle à 95 %) ; partir de la loi de a) en d) ; calculer d) et e) avec les paramètres arrondis de b) (0,165 et 34,4) ; donner à `fsolve` le point de départ $(5, 15)$ pour $(\ln a, \ln b)$ au lieu de $(\ln 5, \ln 15)$.
