# R6 · Exponentielle et logarithmes — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/r6_exp_log/06_mes_reponses.md` (créée par `python tools/start_chapter.py R6`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses des exercices ✏️ et 🔗 se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz, les rappels et les exercices ∂ et 🗣️ se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

**Calculatrice** (ou Python) permise pour les valeurs approchées de $e^x$, de $\ln x$ et des logarithmes ; les simplifications se font à la main, avec les propriétés de la fiche. Écris d'abord le calcul exact, puis sa valeur approchée.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 4 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### R6.Q1 — Propriétés de l'exponentielle : vrai ou faux 🧠 ★ ⏱️ 4 min
*Fiche §1 et §2 · parcours C, E*

Vrai ou faux ?
1. $e^{a} \times e^{b} = e^{a + b}$.
2. $\left(e^{a}\right)^{b} = e^{a + b}$.
3. $e^{-x} < 0$ pour tout $x > 0$.
4. $2^{x} \times 3^{x} = 6^{x}$ pour tout réel $x$.
5. L'équation $e^{x} = 0$ a une solution.
6. $e$ est la limite de la suite $\left(1 + \frac{1}{n}\right)^n$.
7. $4^{1/2} = 2$.

### R6.Q2 — ln d'un produit, d'un quotient, d'une puissance 🧠 ★ ⏱️ 4 min
*Fiche §3 · parcours C, E*

Vrai ou faux, pour tous $a > 0$, $b > 0$ ?
1. $\ln 6 = \ln 2 + \ln 3$.
2. $\ln(a + b) = \ln a + \ln b$.
3. $\ln(a^{3}) = 3 \ln a$.
4. $\ln \frac{1}{a} = -\ln a$.
5. $(\ln a)^{2} = 2 \ln a$.
6. $\ln \frac{a}{b} = \frac{\ln a}{\ln b}$.
7. $\ln x < 0$ pour tout $x$ compris entre 0 et 1 (exclus).

### R6.Q3 — Combien de bits ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Combien de questions oui ou non faut-il, au minimum, pour être sûr de trouver un nombre choisi entre 1 et 16 ?
2. Et un nombre choisi entre 1 et 1 000 000 ?
3. Combien de bits apporte un événement de probabilité $\frac{1}{4}$ ?
4. Combien de bits apporte un événement certain ?
5. Combien de possibilités différentes peut-on distinguer avec 7 réponses oui ou non ?
6. Vrai ou faux : une quantité d'information vaut moins de bits que de nats.

### R6.Q4 — Qui grandit le plus vite ? 🧠 ★ ⏱️ 4 min
*Fiche §5 · parcours C, E*

Pour $x$ très grand, laquelle des deux finit par être la plus grande ?
1. $x^{3}$ ou $1{,}01^{x}$
2. $\ln x$ ou $x^{0{,}1}$
3. $2^{x}$ ou $3^{x}$
4. $x^{100}$ ou $e^{x}$
5. $100 \ln x$ ou $\sqrt{x}$
6. Vrai ou faux : pour $x = 10$, $x^{3}$ est plus grand que $1{,}01^{x}$.

### R6.Q5 — Lire une échelle logarithmique 🧠 ★ ⏱️ 4 min
*Fiche §6 · parcours C*

Un axe logarithmique porte les graduations 1, 10, 100, 1 000.
1. La distance entre 1 et 10 est-elle égale à celle entre 100 et 1 000 ?
2. Le nombre 3 est-il plutôt au quart, à la moitié ou aux trois quarts de la distance entre 1 et 10 ?
3. Peut-on placer 0 sur cet axe ? Et −5 ?
4. Deux points sont séparés de deux décades : quel est le rapport entre leurs valeurs ?
5. Une série de mesures dessine une droite sur un graphique dont l'axe vertical est logarithmique et l'axe horizontal ordinaire. Quel type de croissance a-t-elle ?

### R6.Q6 — Sigmoïde : valeurs remarquables et symétrie 🧠 ★ ⏱️ 4 min
*Fiche §7 · parcours C, E*

1. Que vaut $\sigma(0)$ ?
2. Vrai ou faux : il existe un réel $x$ tel que $\sigma(x) = 1$.
3. Si $\sigma(a) = 0{,}7$, que vaut $\sigma(-a)$ ?
4. Vrai ou faux : $\sigma(x) > \frac{1}{2}$ si et seulement si $x > 0$.
5. Que vaut $\tanh 0$ ? La fonction tanh est-elle paire ou impaire ?
6. Dans quel intervalle tanh prend-elle ses valeurs ?

<a id="rappels"></a>

## 🔁 Rappels

### R6.R1 — Suites géométriques (R5) 🔁 ★ ⏱️ 5 min
*Fiche §1 · parcours C, E*

1. $(u_n)$ est géométrique, $u_0 = 5$ et de raison 2 : calcule $u_6$.
2. Une quantité est multipliée par 1,5 chaque heure : par combien est-elle multipliée en 4 heures ?
3. En essayant des valeurs, trouve le plus petit entier $n$ tel que $1{,}5^{n} > 10$.

### R6.R2 — Fonction réciproque (R3) 🔁 ★ ⏱️ 5 min
*Fiche §3 · parcours C, E*

1. On pose $f(x) = 2x + 3$. Donne l'expression de $f^{-1}(y)$.
2. Quelle est la réciproque de la fonction carré sur $[0 \;;\; +\infty[$ ?
3. Comment se placent l'une par rapport à l'autre les courbes de $f$ et de $f^{-1}$ ?
4. Que vaut $f^{-1}(f(5))$ ?

### R6.R3 — Notation scientifique (R1) 🔁 ★ ⏱️ 5 min
*Fiche §6 · parcours C*

1. Écris 0,00042 et 7 300 000 en notation scientifique.
2. Calcule $(3{,}5 \times 10^{6}) \times (2 \times 10^{-2})$, en notation scientifique.
3. Combien de chiffres a l'entier $10^{12}$ ?

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-les **à la main** (calculatrice permise pour les valeurs approchées), en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, sous la forme demandée :
- un nombre avec un point décimal, comme `-1.5`, arrondi comme le demande la question ;
- une fraction exacte entre guillemets, comme `"5/7"` ;
- une expression entre guillemets, comme `"3*x - 1"` (`*` pour multiplier, `**` pour la puissance) ;
- un intervalle entre guillemets, comme `"[-2 ; 4["` (`-oo` et `+oo` pour l'infini) ;
- une liste de nombres entre crochets ; vrai ou faux par `True` ou `False` ; un numéro de réponse proposée par un nombre entier.

### Ex R6.1 — Simplifier avec les propriétés de exp ✏️ ★ ⏱️ 15 min
**Objectif :** simplifier des produits, des quotients et des puissances d'exponentielles, en base $e$ et dans d'autres bases.
**Prérequis :** fiche §1 et §2 · **Parcours :** C, E

Pour a, b, c et d, chaque expression s'écrit $e^{k}$ ou $2^{k}$ : donne l'exposant $k$.

| | Question | Réponse attendue |
|---|---|---|
| a | $e^{4} \times e^{-1{,}5} = e^{k}$ | un nombre |
| b | $\dfrac{\left(e^{3}\right)^{2}}{e^{4}} = e^{k}$ | un nombre |
| c | $e^{2x} \times e^{1 - x} = e^{k}$, en fonction de $x$ | une expression en `x` |
| d | $2^{x} \times 2^{x + 3} = 2^{k}$, en fonction de $x$ | une expression en `x` |
| e | $8^{2/3}$ | un nombre entier |
| f | $27^{-1/3}$ | une fraction |
| g | $\dfrac{\left(e^{x}\right)^{3}}{e^{x - 2}}$ s'écrit $e^{k}$ : l'exposant $k$ en fonction de $x$ | une expression en `x` |
| h | $\left(\sqrt{e}\right)^{4} \times e^{-2}$ | un nombre entier |

### Ex R6.2 — Simplifier avec les propriétés de ln ✏️ ★ ⏱️ 15 min
**Objectif :** simplifier des expressions qui contiennent des logarithmes, et écrire un logarithme à partir de $\ln 2$ et $\ln 3$.
**Prérequis :** fiche §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\ln\left(e^{5}\right) - \ln\left(e^{2}\right)$ | un nombre entier |
| b | l'entier $k$ tel que $\ln 50 - \ln 2 = \ln k$ | un nombre entier |
| c | l'entier $k$ tel que $2 \ln 3 + \ln 4 = \ln k$ | un nombre entier |
| d | $\ln \dfrac{e^{3}}{\sqrt{e}}$ | une fraction |
| e | $e^{\ln 4 + \ln 5}$ | un nombre entier |
| f | $e^{2 \ln 3}$ | un nombre entier |
| g | $\ln 18$, en fonction de $a = \ln 2$ et $b = \ln 3$ | une expression en `a` et `b` |
| h | $\ln 0{,}75$, en fonction de $a = \ln 2$ et $b = \ln 3$ | une expression en `a` et `b` |

### Ex R6.3 — Équations et inéquations avec exp et ln ✏️ ★★ ⏱️ 20 min
**Objectif :** résoudre des équations et des inéquations avec exp et ln, en surveillant le domaine et le sens des inégalités.
**Prérequis :** fiche §3 ; R2 (inéquations), R3 (second degré) · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | la solution de $e^{x} = 15$ | un nombre (2 décimales) |
| b | la solution de $e^{2x - 1} = 6$ | un nombre (2 décimales) |
| c | la solution de $\ln x = 2{,}5$ | un nombre (2 décimales) |
| d | la solution de $\ln(3x - 2) = 0$ | un nombre |
| e | le plus petit entier $n$ tel que $5 \times 1{,}04^{n} > 8$ | un nombre entier |
| f | le plus petit entier $n$ tel que $0{,}85^{n} < 0{,}05$ | un nombre entier |
| g | l'ensemble des solutions de $\ln(x - 1) \le 0$ | un intervalle |
| h | les solutions de $e^{2x} - 5e^{x} + 6 = 0$ (pose $X = e^{x}$) | une liste (4 décimales) |

### Ex R6.4 — Changer de base : log₂, log₁₀, ln ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des logarithmes dans différentes bases, exactement quand c'est possible, sinon avec la formule de changement de base.
**Prérequis :** fiche §4 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\log_{2} 512$ | un nombre entier |
| b | $\log_{10} 0{,}0001$ | un nombre entier |
| c | $\log_{3} 81$ | un nombre entier |
| d | $\log_{2} \frac{1}{128}$ | un nombre entier |
| e | $\log_{5} 30$ | un nombre (3 décimales) |
| f | $\log_{2} 10$ | un nombre (3 décimales) |
| g | le nombre de chiffres de l'entier $2^{100}$, avec $\log_{10} 2 \approx 0{,}30103$ | un nombre entier |
| h | $\log_{4} 8$ | une fraction |

### Ex R6.5 — Compter en bits et en nats : combien de questions oui ou non ? ✏️ ★★ ⏱️ 15 min
**Objectif :** relier le nombre de questions oui ou non, les bits et les nats, et additionner l'information d'événements indépendants.
**Prérequis :** fiche §4 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre minimal de questions oui ou non pour être sûr de trouver un nombre choisi entre 1 et 300 | un nombre entier |
| b | $\log_{2} 300$ | un nombre (2 décimales) |
| c | l'information, en bits, d'un événement de probabilité $\frac{1}{512}$ | un nombre entier |
| d | la même information, en nats | un nombre (3 décimales) |
| e | l'information, en bits, de « tirer une carte précise » dans un jeu de 52 cartes bien mélangé | un nombre (2 décimales) |
| f | on tire une carte, puis on choisit un nombre entre 1 et 300, indépendamment : l'information totale, en bits | un nombre (2 décimales) |
| g | la probabilité d'un événement qui apporte 3 nats | un nombre (4 décimales) |
| h | 10 bits, convertis en nats | un nombre (2 décimales) |

### Ex R6.6 — Temps de doublement et demi-vie ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer un temps de doublement, une demi-vie et un facteur par période avec les logarithmes et les exposants fractionnaires.
**Prérequis :** fiche §1 et §3 ; R5 §3 · **Parcours :** C

| | Question | Réponse attendue |
|---|---|---|
| a | une grandeur augmente de 3 % par an : son temps de doublement, en années | un nombre (2 décimales) |
| b | la même estimation avec la règle de 70 | un nombre (2 décimales) |
| c | une substance perd 10 % de sa masse chaque année : sa demi-vie, en années | un nombre (2 décimales) |
| d | une population de bactéries double toutes les 5 heures : par quel nombre est-elle multipliée en une heure ? | un nombre (4 décimales) |
| e | la même population : par quel nombre est-elle multipliée en 12 heures ? | un nombre (2 décimales) |
| f | une croissance continue $N(t) = N_{0}\,e^{0{,}04\,t}$ : son temps de doublement | un nombre (2 décimales) |
| g | un médicament a une demi-vie de 6 heures dans le sang : quelle part de la dose reste-t-il au bout de 24 heures ? | une fraction |

### Ex R6.7 — Sigmoïde et logit : la symétrie σ(−x) = 1 − σ(x), la cote et la log-cote ✏️ ★★ ⏱️ 20 min
**Objectif :** calculer des valeurs de la sigmoïde, utiliser sa symétrie, et passer d'une probabilité à sa cote et à son logit.
**Prérequis :** fiche §7 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\sigma(\ln 3)$, valeur exacte (écris $e^{-\ln 3}$ autrement) | une fraction |
| b | $\sigma(-\ln 3)$ | une fraction |
| c | $\sigma(1{,}2)$ | un nombre (3 décimales) |
| d | $\sigma(-1{,}2)$, avec la symétrie et c) | un nombre (3 décimales) |
| e | la cote d'un événement de probabilité 0,95 | un nombre |
| f | le logit de 0,95 | un nombre (3 décimales) |
| g | le réel $x$ tel que $\sigma(x) = 0{,}2$ | un nombre (3 décimales) |
| h | un événement a la probabilité 0,2 ; on ajoute $\ln 6$ à son logit : sa nouvelle probabilité | un nombre |

### Ex R6.8 — Placer des valeurs sur une échelle logarithmique ✏️ ★ ⏱️ 10 min
**Objectif :** passer d'une valeur à sa position sur un axe logarithmique, et inversement.
**Prérequis :** fiche §6 · **Parcours :** C

Un axe logarithmique va de 1 à 10 000 ; il mesure 20 cm, et chaque décade y occupe donc 5 cm. La position d'une valeur est mesurée en centimètres depuis la graduation 1.

| | Question | Réponse attendue |
|---|---|---|
| a | la position de 100 | un nombre |
| b | la position de 2 000 | un nombre (2 décimales) |
| c | la position de 5 | un nombre (2 décimales) |
| d | la valeur placée à 7,5 cm | un nombre (2 décimales) |
| e | deux valeurs sont à 3 cm l'une de l'autre : le rapport de la plus grande à la plus petite | un nombre (2 décimales) |

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex R6.9 — Démontrer ln(ab) = ln a + ln b à partir de exp ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer les propriétés du logarithme à partir de la définition de ln et des propriétés de exp.
**Prérequis :** fiche §2 et §3 ; R4 §7 (récurrence) · **Parcours :** C, E

On utilise seulement : pour $x > 0$, $\ln x$ est l'unique réel $y$ tel que $e^{y} = x$ ; et $e^{u + v} = e^{u}\,e^{v}$ pour tous réels $u$, $v$.
1. Soient $a > 0$ et $b > 0$. Que valent $e^{\ln a}$ et $e^{\ln b}$ ? Calcule $e^{\ln a + \ln b}$.
2. Déduis-en que $\ln(ab) = \ln a + \ln b$ (en citant le mot « unique » de la définition).
3. Montre que $\ln \frac{1}{b} = -\ln b$ (applique 2 à $b$ et $\frac{1}{b}$), puis que $\ln \frac{a}{b} = \ln a - \ln b$.
4. Démontre par récurrence que $\ln(a^{n}) = n \ln a$ pour tout entier $n \ge 0$, puis déduis-en $\ln \sqrt{a} = \frac{1}{2} \ln a$ (écris $a = \sqrt{a} \times \sqrt{a}$).
5. Donne un contre-exemple qui montre que $\ln(a + b) = \ln a + \ln b$ est faux en général.

### Ex R6.10 — tanh(x) = 2σ(2x) − 1 ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer le lien entre la sigmoïde et la tangente hyperbolique, et en déduire leurs propriétés l'une par l'autre.
**Prérequis :** fiche §7 · **Parcours :** C

On rappelle $\sigma(x) = \frac{1}{1 + e^{-x}}$ et $\tanh x = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$.
1. Écris $2\,\sigma(2x) - 1$ comme une seule fraction, de dénominateur $1 + e^{-2x}$.
2. Multiplie le numérateur et le dénominateur par $e^{x}$, et conclus : $\tanh x = 2\,\sigma(2x) - 1$ pour tout réel $x$.
3. Déduis de la symétrie $\sigma(-u) = 1 - \sigma(u)$ (fiche §7) que tanh est impaire.
4. Déduis de $0 < \sigma(u) < 1$ que $-1 < \tanh x < 1$.
5. Inverse la relation : exprime $\sigma(x)$ à l'aide de $\tanh \frac{x}{2}$.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R6.11 — Des produits de probabilités aux sommes de logarithmes 🔗 ★★ ⏱️ 20 min
**Objectif :** calculer une vraisemblance et sa log-vraisemblance, et voir pourquoi on compare des modèles sur des sommes de logarithmes.
**Prérequis :** fiche §3 et §5 · **Parcours :** C, E

Un modèle prédit le résultat de cinq expériences indépendantes ; il avait donné aux résultats observés les probabilités 0,9 ; 0,6 ; 0,3 ; 0,8 ; 0,5. La **vraisemblance** du modèle est le produit de ces probabilités ; sa **log-vraisemblance**, le logarithme népérien de ce produit.

| | Question | Réponse attendue |
|---|---|---|
| a | la vraisemblance | un nombre (4 décimales) |
| b | la log-vraisemblance, calculée comme une somme de logarithmes | un nombre (4 décimales) |
| c | la log-vraisemblance moyenne par expérience | un nombre (4 décimales) |
| d | un second modèle avait donné 0,7 à chacun des cinq résultats observés : sa vraisemblance | un nombre (4 décimales) |
| e | le meilleur des deux modèles : 1 pour le premier, 2 pour le second | 1 ou 2 |
| f | un modèle donne la probabilité 0,4 à chacun de 1 000 résultats observés : $\log_{10}$ de sa vraisemblance | un nombre (2 décimales) |
| g | un `float64` peut-il représenter cette vraisemblance autrement que par 0 ? | vrai ou faux |
| h | sa log-vraisemblance | un nombre (1 décimale) |

Dans ta copie : pourquoi le modèle qui a la plus grande vraisemblance est-il aussi celui qui a la plus grande log-vraisemblance ? Et que mesure $-\ln p$ quand $p$ est la probabilité donnée à ce qui s'est réellement produit (pense aux nats du §4) ?

### Ex R6.12 — Des logarithmes au travail : TF-IDF et PSNR 🔗 ★ ⏱️ 15 min
**Objectif :** calculer deux mesures du ML qui utilisent un logarithme, et voir ce que le logarithme y fait.
**Prérequis :** fiche §3, §4 et §6 · **Parcours :** C

**TF-IDF.** Dans une collection de $N = 2\,000$ documents, le poids d'un mot $t$ dans un document est $\mathrm{tf}(t) \times \mathrm{idf}(t)$, où $\mathrm{tf}(t)$ est le nombre de fois qu'il y apparaît et $\mathrm{idf}(t) = \ln \frac{N}{\mathrm{df}(t)}$, avec $\mathrm{df}(t)$ le nombre de documents qui contiennent le mot (la version la plus simple de l'idf ; scikit-learn y ajoute des 1).

**PSNR.** Pour des images dont les pixels vont de 0 à 255, on mesure la qualité d'une image reconstruite par le PSNR, en décibels : $\mathrm{PSNR} = 10 \log_{10} \frac{255^{2}}{\mathrm{MSE}}$, où MSE est la moyenne des carrés des écarts entre les pixels de l'image reconstruite et ceux de l'originale.

| | Question | Réponse attendue |
|---|---|---|
| a | l'idf d'un mot présent dans les 2 000 documents | un nombre |
| b | l'idf d'un mot présent dans 20 documents | un nombre (3 décimales) |
| c | l'idf d'un mot présent dans 200 documents | un nombre (3 décimales) |
| d | dans un document, le mot de b) apparaît 2 fois et celui de c) 5 fois : la liste de leurs poids tf-idf, dans cet ordre | une liste (3 décimales) |
| e | le PSNR d'une reconstruction dont la MSE vaut 65,025 | un nombre |
| f | de combien de décibels le PSNR augmente-t-il quand on divise la MSE par 2 ? | un nombre (2 décimales) |
| g | la MSE qui donne un PSNR de 40 dB | un nombre (4 décimales) |

Dans ta copie : pourquoi un mot présent dans tous les documents a-t-il un poids nul ? Et pourquoi mesure-t-on la qualité d'une image avec un logarithme plutôt qu'avec la MSE elle-même ?

### Ex R6.13 — Expliquer ce que compte un logarithme : des chiffres, des doublements, des bits 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement à quoi sert un logarithme, avec trois exemples concrets.
**Prérequis :** fiche §3 et §4 · **Parcours :** C, E

Un ami te dit : « Le logarithme, c'est un bouton de la calculatrice, mais je n'ai jamais compris ce qu'il calcule. »

Réponds-lui **en huit lignes au plus**. Ta réponse doit contenir : la question à laquelle répond $\log_{b} x$ (avec un exemple), ce que compte $\log_{10}$ (avec un exemple), ce que compte $\log_{2}$ (des doublements, puis des réponses oui ou non), et pourquoi un logarithme transforme une multiplication en addition.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/r6_exp_log/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses aux exercices ✏️ et 🔗 ci-dessus.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| R6.14 | Un logarithme dans n'importe quelle base · `log_base` | 🔨 | ★ | 15 | C, E |
| R6.15 | Sigmoïde et tanh à partir de exp · `sigmoid`, `tanh` | 🔨 | ★★ | 20 | C, E |
| R6.16 | Temps de doublement · `doubling_time` | 🔨 | ★ | 15 | C |
| R6.17 | Sur tout un tableau : `np.exp`, `np.log2` et `scipy.special.expit` | 📦 | ★ | 15 | C |
| R6.18 | Prédire : exp(800) avec math et NumPy, et le produit de 600 probabilités de 0,25 | 🔮 | ★★ | 15 | C, E |
| R6.19 | Croissances comparées : x¹⁰, 2ˣ et ln x de plus en plus loin | 🔬 | ★★ | 20 | C |
| R6.20 | Les mêmes données en échelle linéaire et en échelle logarithmique | 🎨 | ★ | 15 | C, E |
| R6.21 | Chasse à l'erreur : ln(a + b), e^(a + b) et log(0) | 🐛 | ★★ | 15 | C, E |
| R6.22 | Lire la documentation de `numpy.log`, `log2`, `log10`, `log1p` | 🛠️ | ★ | 15 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
