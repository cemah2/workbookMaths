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
2. $\ln 5 = \ln 2 + \ln 3$.
3. $\ln(a^{3}) = 3 \ln a$.
4. $\ln \frac{1}{a} = -\ln a$.
5. $(\ln a)^{2} = 2 \ln a$.
6. $\ln \frac{a}{b} = \frac{\ln a}{\ln b}$.
7. $\ln x < 0$ pour tout $x$ compris entre 0 et 1 (exclus).

### R6.Q3 — Combien de bits ? 🧠 ★ ⏱️ 4 min
*Fiche §4 · parcours C, E*

1. Combien de questions oui ou non faut-il, au minimum, pour être sûr de trouver un nombre choisi entre 1 et 16 ?
2. Et un nombre choisi entre 1 et 1 000 000 ?
3. Combien de bits apporte un événement de probabilité $\frac{1}{32}$ ?
4. Combien de bits apporte un événement certain ?
5. Combien de possibilités différentes peut-on distinguer avec 7 réponses oui ou non ?
6. Vrai ou faux : exprimée en nats, une quantité d'information est un nombre plus petit qu'exprimée en bits.

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

Vrai ou faux ?
1. $\sigma(0) = 0$.
2. Il existe un réel $x$ tel que $\sigma(x) = 1$.
3. $\sigma(-x) = -\sigma(x)$ pour tout réel $x$.
4. $\sigma(x) > \frac{1}{2}$ si et seulement si $x > 0$.
5. La sigmoïde et la tangente hyperbolique sont toutes deux impaires.
6. $\tanh x$ peut prendre n'importe quelle valeur strictement comprise entre −1 et 1.

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
2. Calcule $(4{,}8 \times 10^{5}) \div (1{,}6 \times 10^{-3})$, en notation scientifique.
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

Pour a, b, c, d et g, chaque expression s'écrit $e^{k}$ ou $2^{k}$ : donne l'exposant $k$. Pour e, f et h, donne la valeur du nombre.

| | Question | Réponse attendue |
|---|---|---|
| a | $e^{4} \times e^{-1{,}5} = e^{k}$ | un nombre |
| b | $\dfrac{e^{7}}{\left(e^{2}\right)^{3}} = e^{k}$ | un nombre |
| c | $e^{3x} \times e^{2 - 5x} = e^{k}$, en fonction de $x$ | une expression en `x` |
| d | $2^{x} \times 2^{x + 3} = 2^{k}$, en fonction de $x$ | une expression en `x` |
| e | $16^{3/4}$ | un nombre entier |
| f | $125^{-1/3}$ | une fraction |
| g | $\dfrac{\left(e^{x}\right)^{3}}{e^{x - 2}}$ s'écrit $e^{k}$ : l'exposant $k$ en fonction de $x$ | une expression en `x` |
| h | la valeur de $\left(\sqrt{e}\right)^{4} \times e^{-2}$ | un nombre entier |

### Ex R6.2 — Simplifier avec les propriétés de ln ✏️ ★ ⏱️ 15 min
**Objectif :** simplifier des expressions qui contiennent des logarithmes, et écrire un logarithme à partir de $\ln 2$ et $\ln 3$.
**Prérequis :** fiche §3 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $3\ln\left(e^{2}\right) - \ln\left(e^{4}\right)$ | un nombre entier |
| b | l'entier $k$ tel que $\ln 60 - \ln 4 - \ln 3 = \ln k$ | un nombre entier |
| c | l'entier $k$ tel que $2 \ln 3 + \ln 4 = \ln k$ | un nombre entier |
| d | $\ln \dfrac{\sqrt{e}}{e^{3}}$ | une fraction |
| e | $e^{\ln 4 + \ln 5}$ | un nombre entier |
| f | $e^{3 \ln 2 - \ln 4}$ | un nombre entier |
| g | $\ln 18$, en fonction de $a = \ln 2$ et $b = \ln 3$ | une expression en `a` et `b` (sans `ln`) |
| h | $\ln 0{,}75$, en fonction de $a = \ln 2$ et $b = \ln 3$ | une expression en `a` et `b` (sans `ln`) |

### Ex R6.3 — Équations et inéquations avec exp et ln ✏️ ★★ ⏱️ 20 min
**Objectif :** résoudre des équations et des inéquations avec exp et ln, en surveillant le domaine et le sens des inégalités.
**Prérequis :** fiche §3 ; R2 (inéquations), R3 (second degré) · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | la solution de $4e^{x} + 1 = 21$ | un nombre (2 décimales) |
| b | la solution de $e^{1 - 2x} = 6$ | un nombre (2 décimales) |
| c | la solution de $2\ln x + 1 = 6$ | un nombre (2 décimales) |
| d | la solution de $\ln(x - 1) + \ln(x + 1) = \ln 8$ (vérifie le domaine) | un nombre entier |
| e | le plus petit entier $n$ tel que $5 \times 1{,}04^{n} > 8$ | un nombre entier |
| f | le plus petit entier $n$ tel que $0{,}85^{n} < 0{,}05$ | un nombre entier |
| g | l'ensemble des solutions de $\ln(x - 1) \le 0$ | un intervalle |
| h | les solutions de $e^{2x} - 5e^{x} + 6 = 0$ (pose $X = e^{x}$), dans l'ordre croissant | une liste (4 décimales) |

### Ex R6.4 — Changer de base : log₂, log₁₀, ln ✏️ ★ ⏱️ 15 min
**Objectif :** calculer des logarithmes dans différentes bases, exactement quand c'est possible, sinon avec la formule de changement de base.
**Prérequis :** fiche §4 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | $\log_{2} 512$ | un nombre entier |
| b | $\log_{10} 25 + \log_{10} 4$ | un nombre entier |
| c | $\log_{6} 216$ | un nombre entier |
| d | $\log_{2} \frac{1}{128}$ | un nombre entier |
| e | $\log_{5} 30$ | un nombre (3 décimales) |
| f | $\log_{2} 7$ | un nombre (3 décimales) |
| g | le nombre de chiffres de l'entier $2^{100}$, avec $\log_{10} 2 \approx 0{,}30103$ | un nombre entier |
| h | $\log_{4} 8$ | une fraction |

### Ex R6.5 — Compter en bits et en nats : combien de questions oui ou non ? ✏️ ★★ ⏱️ 15 min
**Objectif :** relier le nombre de questions oui ou non, les bits et les nats, et mesurer l'information d'un code et d'un tirage.
**Prérequis :** fiche §4 · **Parcours :** C, E

| | Question | Réponse attendue |
|---|---|---|
| a | le nombre minimal de questions oui ou non pour être sûr de trouver un nombre choisi entre 1 et 300 | un nombre entier |
| b | $\log_{2} 300$ | un nombre (2 décimales) |
| c | un code de 3 lettres (parmi les 26 de l'alphabet, répétitions permises) est choisi au hasard, tous les codes étant également probables : l'information, en bits, d'apprendre ce code | un nombre (2 décimales) |
| d | le plus petit nombre de lettres d'un tel code pour que l'apprendre apporte au moins 50 bits | un nombre entier |
| e | l'information, en bits, de « tirer une carte précise » dans un jeu de 52 cartes bien mélangé | un nombre (2 décimales) |
| f | dans le même jeu, l'information, en bits, d'apprendre seulement que la carte tirée est une figure (valet, dame ou roi : 12 cartes sur 52) | un nombre (2 décimales) |
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

### Ex R6.7 — La cote et le logit : d'une probabilité à un score, et retour ✏️ ★★ ⏱️ 20 min
**Objectif :** passer d'une probabilité à sa cote et à son logit, d'un score à une probabilité avec la sigmoïde, et voir ce que fait une addition au logit.
**Prérequis :** fiche §7 · **Parcours :** C, E

Un classifieur calcule un **score** $z$ (un nombre réel), puis la probabilité $p = \sigma(z)$ : le score est le logit de la probabilité.

| | Question | Réponse attendue |
|---|---|---|
| a | la cote d'un événement de probabilité 0,95 | un nombre |
| b | le logit de 0,95 | un nombre (3 décimales) |
| c | un événement a la cote « 3 contre 7 » : sa probabilité | un nombre |
| d | le logit de la probabilité de c) | un nombre (3 décimales) |
| e | le classifieur calcule le score $z = 1{,}2$ : la probabilité qu'il donne | un nombre (3 décimales) |
| f | le logit de la probabilité **contraire** de celle de e), sans calculatrice | un nombre |
| g | le logit d'un événement vaut 3 : sa cote | un nombre (2 décimales) |
| h | un événement a la probabilité 0,2 ; on ajoute $\ln 6$ à son logit : sa nouvelle probabilité | un nombre |

### Ex R6.8 — Placer des valeurs sur une échelle logarithmique ✏️ ★ ⏱️ 10 min
**Objectif :** passer d'une valeur à sa position sur un axe logarithmique, et inversement.
**Prérequis :** fiche §6 · **Parcours :** C

Un axe logarithmique va de 1 à 10 000 ; il mesure 20 cm, et chaque décade y occupe donc 5 cm. La position d'une valeur est mesurée en centimètres depuis la graduation 1.

| | Question | Réponse attendue |
|---|---|---|
| a | la position de 100 | un nombre (1 décimale) |
| b | la position de 2 000 | un nombre (1 décimale) |
| c | la position de 5 | un nombre (1 décimale) |
| d | la valeur placée à 7,5 cm | un nombre (2 décimales) |
| e | deux valeurs sont à 3 cm l'une de l'autre : le rapport de la plus grande à la plus petite | un nombre (2 décimales) |

<a id="demonstrations"></a>

## ∂ Démonstrations

Une démonstration se rédige en phrases : ce qu'on suppose, chaque étape et sa justification, ce qu'on conclut (R4 §8). La solution donne une **grille de relecture** pour juger la tienne.

### Ex R6.9 — Démontrer ln(ab) = ln a + ln b à partir de exp ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer les propriétés du logarithme à partir de la définition de ln et des propriétés de exp.
**Prérequis :** fiche §2 et §3 ; R4 §7 (récurrence) · **Parcours :** C, E

On utilise seulement : pour $x > 0$, $\ln x$ est l'unique réel $y$ tel que $e^{y} = x$ ; $e^{0} = 1$ ; et $e^{u + v} = e^{u}\,e^{v}$ pour tous réels $u$, $v$.
1. Soient $a > 0$ et $b > 0$. Que valent $e^{\ln a}$ et $e^{\ln b}$ ? Calcule $e^{\ln a + \ln b}$.
2. Déduis-en que $\ln(ab) = \ln a + \ln b$ (en citant le mot « unique » de la définition).
3. Montre que $\ln \frac{1}{b} = -\ln b$ (applique 2 à $b$ et $\frac{1}{b}$), puis que $\ln \frac{a}{b} = \ln a - \ln b$.
4. Démontre par récurrence que $\ln(a^{n}) = n \ln a$ pour tout entier $n \ge 0$, puis déduis-en $\ln \sqrt{a} = \frac{1}{2} \ln a$ (écris $a = \sqrt{a} \times \sqrt{a}$).
5. Donne un contre-exemple qui montre que $\ln(a + b) = \ln a + \ln b$ est faux en général.

### Ex R6.10 — Les propriétés de tanh, démontrées avec exp ∂ ★★ ⏱️ 25 min
**Objectif :** démontrer, avec les seules règles de l'exponentielle, que tanh est impaire, comprise entre −1 et 1, strictement croissante, et sa formule d'addition.
**Prérequis :** fiche §2 et §7 · **Parcours :** C

On rappelle $\tanh x = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$, et que $e^{u} > 0$ pour tout réel $u$. Pas de dérivée : R7 viendra plus tard.
1. Multiplie le numérateur et le dénominateur par $e^{x}$ : montre que $\tanh x = \frac{e^{2x} - 1}{e^{2x} + 1}$ pour tout réel $x$.
2. Montre que tanh est impaire : $\tanh(-x) = -\tanh x$.
3. Montre que $-1 < \tanh x < 1$ pour tout réel $x$ (compare le numérateur et le dénominateur de l'écriture de 1, en sachant que $e^{2x} > 0$).
4. Soient $a < b$ ; pose $A = e^{2a}$ et $B = e^{2b}$. Avec l'écriture de 1, calcule $\tanh b - \tanh a$ comme une seule fraction, et déduis-en que tanh est strictement croissante.
5. Avec les mêmes $A$ et $B$, montre que $\tanh(a + b) = \dfrac{\tanh a + \tanh b}{1 + \tanh a \tanh b}$ pour tous réels $a$, $b$.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R6.11 — Des produits de probabilités aux sommes de logarithmes 🔗 ★★ ⏱️ 20 min
**Objectif :** calculer une vraisemblance et sa log-vraisemblance, et comparer deux modèles par des sommes de logarithmes quand leurs vraisemblances sont trop petites pour être calculées.
**Prérequis :** fiche §3 et §5 · **Parcours :** C, E

Un modèle prédit le résultat de cinq expériences indépendantes ; il avait donné aux résultats observés les probabilités 0,9 ; 0,6 ; 0,3 ; 0,8 ; 0,5. La **vraisemblance** du modèle est le produit de ces probabilités ; sa **log-vraisemblance**, le logarithme népérien de ce produit.

| | Question | Réponse attendue |
|---|---|---|
| a | la vraisemblance | un nombre (4 décimales) |
| b | la log-vraisemblance, calculée comme une somme de logarithmes | un nombre (4 décimales) |
| c | la log-vraisemblance moyenne par expérience | un nombre (4 décimales) |
| d | un second modèle avait donné 0,7 à chacun des cinq résultats observés : sa vraisemblance | un nombre (4 décimales) |
| e | le meilleur des deux modèles : 1 pour le premier, 2 pour le second | 1 ou 2 |

Sur 1 000 nouveaux résultats indépendants, le modèle A avait donné la probabilité 0,4 à chacun des résultats observés ; le modèle B avait donné 0,5 à 600 d'entre eux et 0,3 aux 400 autres. Leurs vraisemblances sont bien trop petites pour un flottant (§5) : calcule seulement avec des logarithmes.

| | Question | Réponse attendue |
|---|---|---|
| f | la log-vraisemblance du modèle B | un nombre (1 décimale) |
| g | de combien la log-vraisemblance de B dépasse-t-elle celle de A ? | un nombre (1 décimale) |
| h | le rapport de la vraisemblance de B à celle de A, en ordres de grandeur : $\log_{10}$ de ce rapport | un nombre (2 décimales) |

Dans ta copie : que mesure $-\ln p$ quand $p$ est la probabilité donnée à ce qui s'est réellement produit (pense aux nats du §4) ? Lequel des cinq premiers résultats a le plus surpris le premier modèle ?

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
| d | dans un document, le mot de b) apparaît 2 fois et celui de c) 5 fois : la liste de leurs poids tf-idf, dans cet ordre (avec les valeurs non arrondies de b et c) | une liste (3 décimales) |
| e | le PSNR d'une reconstruction dont la MSE vaut 65,025 | un nombre |
| f | de combien de décibels le PSNR augmente-t-il quand on divise la MSE par 5 ? | un nombre (2 décimales) |
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
| R6.18 | Prédire : exp(800) et exp(−800), avec math et avec NumPy | 🔮 | ★★ | 15 | C, E |
| R6.19 | Croissances comparées : x¹⁰, 2ˣ et ln x de plus en plus loin | 🔬 | ★★ | 20 | C |
| R6.20 | Les mêmes données en échelle linéaire et en échelle logarithmique | 🎨 | ★ | 15 | C, E |
| R6.21 | Chasse à l'erreur : ln(a + b), e^(a + b) et log(0) | 🐛 | ★★ | 15 | C, E |
| R6.22 | Lire la documentation de `numpy.log`, `log2`, `log10`, `log1p` | 🛠️ | ★ | 15 | C |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
