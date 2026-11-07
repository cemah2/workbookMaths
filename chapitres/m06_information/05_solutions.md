# M06 · Théorie de l'information — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté. Sauf mention contraire, les entropies sont en bits.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🧮 🗣️ Pont, estimation et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M06.Q1 — La surprise et la probabilité
1. $-\log_2 \frac{1}{256} = \log_2 256 = 8$ bits.
2. $-\log_2 p = 11$, donc $p = 2^{-11} = \frac{1}{2048}$.
3. $1{,}5 + 2 = 3{,}5$ bits : les informations d'événements indépendants s'additionnent.
4. **Faux** : $0 < p \le 1$, donc $\log_2 p \le 0$ et $-\log_2 p \ge 0$. Elle est nulle pour un événement certain.
5. $2 \ln 2 \approx 1{,}39$ nat (1 bit vaut $\ln 2 \approx 0{,}693$ nat).
6. Pour que les informations d'événements indépendants **s'additionnent** : la probabilité des deux est le produit $p\,q$, et le logarithme change un produit en somme, $-\log(p\,q) = -\log p - \log q$. Avec $\frac{1}{p}$, elles se multiplieraient, et un événement certain apporterait 1 au lieu de 0.

### M06.Q2 — L'entropie : vrai ou faux
1. **Faux** : c'est une moyenne de termes $-\log_2 p \ge 0$.
2. **Vrai** : $H \le \log_2 8 = 3$, avec égalité pour la loi uniforme.
3. **Faux** : une issue de probabilité 0 ajoute $0 \log 0 = 0$.
4. **Faux** : l'entropie ne dépend que des probabilités, pas des valeurs. Multiplier les valeurs par 2 ne change aucune probabilité.
5. **Faux** : $(0{,}97 ;\ 0{,}03)$ est presque certaine, son entropie est petite (environ 0,19 bit) ; $(0{,}53 ;\ 0{,}47)$ est presque équilibrée, son entropie est proche de 1 bit.
6. **Vrai** : $H(X) = \sum p(x)\,\big(-\log_2 p(x)\big) = \mathbb{E}[-\log_2 p(X)]$, la surprise moyenne.

### M06.Q3 — Conjointe et conditionnelle
1. $H(X, Y) = H(X) + H(Y \mid X) = H(Y) + H(X \mid Y)$.
2. $H(Y \mid X) = 0$ : connaître $X$, c'est connaître $Y$.
3. $H(X, Y) = H(X) + H(Y)$.
4. **Faux** en général : avec la règle de la chaîne, $H(Y \mid X) - H(X \mid Y) = H(Y) - H(X)$, qui n'est nul que si $H(X) = H(Y)$.
5. **Vrai** : $H(X, Y) = H(X) + H(Y \mid X)$ et $H(Y \mid X) \ge 0$.
6. $H(Y \mid X) = 2{,}5 - 1 = 1{,}5$ et $H(X \mid Y) = 2{,}5 - 2 = 0{,}5$.

### M06.Q4 — L'information mutuelle
1. $I(X ; Y) = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X) = H(X) + H(Y) - H(X, Y)$.
2. **Vrai** : la troisième écriture est symétrique.
3. $X$ et $Y$ sont **indépendantes** (et réciproquement).
4. $I = 2 - 0{,}5 = 1{,}5$ bit.
5. **Faux** : $I(X ; Y) = H(X) - H(X \mid Y) \le H(X)$, et de même $I \le H(Y)$.
6. **Faux** : la corrélation ne voit que les liens linéaires. Pour $X$ symétrique et $Y = X^2$, la corrélation est nulle, mais $I(X ; Y) = H(Y) > 0$ (M06.21).

### M06.Q5 — La KL n'est pas une distance
1. $\mathrm{KL}(p \,\|\, q) = H(p, q) - H(p)$.
2. 0.
3. $\mathrm{KL}(p \,\|\, q) = 2 \times \frac{1}{2}\log_2 \frac{1/2}{1/3} = \log_2 1{,}5 \approx 0{,}585$ bit : **finie** (la troisième issue, de probabilité 0 sous $p$, ne compte pas). $\mathrm{KL}(q \,\|\, p)$ contient le terme $\frac{1}{3}\log_2 \frac{1/3}{0}$ : elle est **infinie**.
4. La symétrie ($\mathrm{KL}(p \,\|\, q) \ne \mathrm{KL}(q \,\|\, p)$ en général) et l'inégalité triangulaire. (La positivité, elle, est vraie.)
5. **Faux** : c'est l'inégalité de Gibbs (fiche §6, M06.11).
6. Le nombre moyen de bits **perdus** par symbole quand on code les données avec un code fait pour le modèle, au lieu du meilleur code pour les données.

### M06.Q6 — L'inégalité de Jensen
1. $\mathbb{E}[f(X)] \ge f(\mathbb{E}[X])$ : la moyenne des images est au-dessus de l'image de la moyenne.
2. $\mathbb{E}[X^2] = \frac{0 + 16}{2} = 8$ et $(\mathbb{E}[X])^2 = 2^2 = 4$.
3. $\mathbb{E}[\ln X] \le \ln \mathbb{E}[X]$ : $\ln$ est **concave** ($\ln'' x = -\frac{1}{x^2} < 0$), et l'inégalité se retourne.
4. Quand $X$ est constante (elle ne prend qu'une valeur, avec probabilité 1).
5. **Vrai** : $x \mapsto \frac{1}{x}$ est convexe sur $]0, +\infty[$ (dérivée seconde $\frac{2}{x^3} > 0$).
6. La **variance** de $X$ (M02b).

### M06.Q7 — Codes préfixes
1. Aucun mot n'est le début d'un autre. En lisant les bits de gauche à droite, dès que les bits lus forment un mot, c'est ce mot : aucun mot plus long ne peut commencer ainsi.
2. **Préfixe** : ni 01, ni 10, ni 11 n'est le début de 001, et 001 n'est le début d'aucun mot. **Pas complet** : sa somme de Kraft vaut $\frac{3}{4} + \frac{1}{8} = \frac{7}{8} < 1$ ; on pourrait ajouter le mot 000.
3. **Non** : 1 est le début de 10 (la suite « 10 » se lit « 1, 0 » ou « 10 »).
4. **Oui** : $\frac{1}{2} + 3 \times \frac{1}{8} = \frac{7}{8} \le 1$ ; par exemple 0, 100, 101, 110.
5. 6 : $2^5 = 32 < 50 \le 64 = 2^6$.
6. **Vrai** : deux mots de même longueur ne peuvent être le début l'un de l'autre que s'ils sont égaux.

<a id="rappels"></a>

## 🔁 Rappels

### M06.R1 — Logarithmes en base 2 (R6)
1. $\log_2 512 = 9$ ($2^9 = 512$), $\log_2 \frac{1}{4096} = -12$, $\log_2 \sqrt{2} = \frac{1}{2}$.
2. $\log_2 10 = \frac{\ln 10}{\ln 2} \approx \frac{2{,}3026}{0{,}6931} \approx 3{,}322$.
3. $\log_2 24 - \log_2 3 = \log_2 8 = 3$.
4. $x = \log_2 12 = \frac{\ln 12}{\ln 2} \approx 3{,}58$.
5. Négatif : $\log_2 p < 0$ pour $0 < p < 1$. Pour $p = \frac{1}{2}$ : $-\frac{1}{2}\log_2 \frac{1}{2} = \frac{1}{2}$.

### M06.R2 — Probabilités jointes et conditionnelles (M03)
1. En divisant par 100 : 0,12 ; 0,18 ; 0,28 ; 0,42.
2. $P(\text{pluie}) = 0{,}3$, $P(\text{pas de pluie}) = 0{,}7$ ; $P(\text{en retard}) = 0{,}4$, $P(\text{à l'heure}) = 0{,}6$.
3. $\frac{12}{30} = 0{,}4$ et $\frac{28}{70} = 0{,}4$.
4. **Oui** : les deux probabilités conditionnelles de 3. sont égales à $P(\text{en retard})$ ; et chaque case est le produit de ses marges ($0{,}3 \times 0{,}4 = 0{,}12$, $0{,}3 \times 0{,}6 = 0{,}18$, $0{,}7 \times 0{,}4 = 0{,}28$, $0{,}7 \times 0{,}6 = 0{,}42$).
5. $H(Y \mid X) = H(Y)$ : savoir s'il pleut n'apprend rien sur le retard ($I(X ; Y) = 0$).

### M06.R3 — Convexité (M05a)
1. $f$ est convexe si, pour tous $a$, $b$ et tout $t \in [0, 1]$, $f\big(t a + (1 - t) b\big) \le t f(a) + (1 - t) f(b)$ : la corde est au-dessus de la courbe.
2. **Oui** : $f'(x) = -\frac{1}{x}$, $f''(x) = \frac{1}{x^2} > 0$.
3. **Oui** : $g'(x) = \ln x + 1$, $g''(x) = \frac{1}{x} > 0$ sur $]0, +\infty[$.
4. **Oui** : l'inégalité des cordes s'additionne (ou : $(f + g)'' = f'' + g'' \ge 0$).
5. **Au-dessous** : une fonction concave a ses cordes sous sa courbe.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M06.1 — L'information d'événements et l'entropie d'une loi à quatre issues

**Réponses** : a) `4` · b) `1` · c) `2.415` · d) `2.773` · e) `5` · f) `1.703` · g) `1.180` · h) `1.5`.

**Démarche.**
- a) $-\log_2 \frac{1}{16} = 4$ ; b) $-\log_2 \frac{1}{2} = 1$.
- c) $-\log_2 \frac{3}{16} = 4 - \log_2 3 \approx 4 - 1{,}585 = 2{,}415$.
- d) En nats : $-\ln \frac{1}{16} = \ln 16 \approx 2{,}773$ (ou $4 \times \ln 2$).
- e) $1 + 4 = 5$ bits (la probabilité des deux est $\frac{1}{32}$).
- f) $H = \frac{1}{2} \times 1 + \frac{1}{4} \times 2 + \frac{3}{16}\,(4 - \log_2 3) + \frac{1}{16} \times 4 = 2 - \frac{3}{16}\log_2 3 \approx 1{,}703$.
- g) $1{,}7028 \times \ln 2 \approx 1{,}180$ nat.
- h) La loi $(\frac{1}{2}, \frac{1}{4}, \frac{1}{4})$ : $\frac{1}{2} + \frac{1}{4} \times 2 + \frac{1}{4} \times 2 = 1{,}5$.

Pour la copie : f) est plus petite que $\log_2 4 = 2$ bits, l'entropie de la loi uniforme sur quatre issues, car la loi n'est pas uniforme. En regroupant les deux erreurs, on perd l'information « laquelle des deux erreurs » : $f) - h) = \frac{1}{4}\,H\big(\frac{3}{4}, \frac{1}{4}\big)$, la probabilité $\frac{1}{4}$ d'une erreur fois l'incertitude qui reste sur son type, de loi $(\frac{3}{4}, \frac{1}{4})$ une fois qu'on sait qu'il y a une erreur (c'est la règle de la chaîne, §3).

**Erreurs fréquentes.** Oublier le signe moins (a : $-4$) ; utiliser $\ln$ au lieu de $\log_2$ (c : 1,674) ; multiplier les informations au lieu de les additionner (e : 4) ; additionner les informations sans les pondérer (f : 11,415) ; diviser par $\ln 2$ au lieu de multiplier (g : 2,457).

**Variante.** Combien de bits apporte un événement de probabilité $\frac{3}{8}$ ? Quelle est l'entropie de $(\frac{3}{4}, \frac{1}{8}, \frac{1}{8})$ ? *Réponse* : $3 - \log_2 3 \approx 1{,}415$ bit ; $\frac{3}{4}\log_2 \frac{4}{3} + \frac{1}{4} \times 3 \approx 1{,}061$ bit.

### Ex M06.2 — L'entropie maximale : comparer trois lois à trois issues

**Réponses** : a) `1.585` · b) `1` · c) `1.157` · d) `"A"` · e) `1.513` · f) `1.353` · g) `1.099`.

**Démarche.**
- a) $3 \times \frac{1}{3}\log_2 3 = \log_2 3 \approx 1{,}585$.
- b) $2 \times \frac{1}{2} \times 1 + 0 = 1$ ($0 \log 0 = 0$).
- c) $0{,}7 \times 0{,}515 + 0{,}2 \times 2{,}322 + 0{,}1 \times 3{,}322 \approx 0{,}360 + 0{,}464 + 0{,}332 = 1{,}157$.
- d) La loi uniforme $A$ : sur trois issues, l'entropie est au plus $\log_2 3$, atteinte seulement par la loi uniforme.
- e) $0{,}45 \times 1{,}152 + 0{,}35 \times 1{,}515 + 0{,}2 \times 2{,}322 \approx 0{,}518 + 0{,}530 + 0{,}464 = 1{,}513$.
- f) $0{,}6 \times 0{,}737 + 0{,}25 \times 2 + 0{,}15 \times 2{,}737 \approx 0{,}442 + 0{,}5 + 0{,}411 = 1{,}353$.
- g) $\ln 3 \approx 1{,}099$ nat.

Pour la copie : $B$ (1) $< C$ (1,157) $<$ f) (1,353) $<$ e) (1,513) $< A$ (1,585). Rapprocher les probabilités les unes des autres fait monter l'entropie, jusqu'à la loi uniforme. La plus petite entropie possible est 0, pour les trois lois certaines $(1, 0, 0)$, $(0, 1, 0)$ et $(0, 0, 1)$.

**Erreurs fréquentes.** Répondre `"B"` en d) parce que deux issues sont à égalité (une issue impossible fait baisser l'entropie : $B$ n'a que deux issues possibles) ; calculer en nats en a) (1,099) ou en bits en g) (1,585).

**Variante.** Quelle est la plus grande entropie possible sur 7 issues ? *Réponse* : $\log_2 7 \approx 2{,}807$ bits, pour la loi uniforme.

### Ex M06.3 — Entropies conjointe et conditionnelle d'un tableau 2 × 3

**Réponses** : a) `1.75` · b) `1.5` · c) `0.75` · d) `1.299` · e) `0.451` · f) `True`.

**Démarche.**
- a) Les cases non nulles : $\frac{1}{2} \times 1 + 2 \times \frac{1}{8} \times 3 + \frac{1}{4} \times 2 = 0{,}5 + 0{,}75 + 0{,}5 = 1{,}75$.
- b) La ligne « payant », divisée par $P(\text{payant}) = \frac{1}{2}$, donne la loi $(\frac{1}{4}, \frac{1}{4}, \frac{1}{2})$, d'entropie $\frac{1}{4} \times 2 \times 2 + \frac{1}{2} \times 1 = 1{,}5$.
- c) $H(Y \mid X) = \frac{1}{2} \times 0 + \frac{1}{2} \times 1{,}5 = 0{,}75$ (la ligne « gratuit » a l'entropie 0).
- d) La loi de $Y$ (les sommes des colonnes) : $(\frac{5}{8}, \frac{1}{8}, \frac{1}{4})$, d'entropie $\frac{5}{8}\log_2 \frac{8}{5} + \frac{3}{8} + \frac{1}{2} \approx 0{,}424 + 0{,}375 + 0{,}5 = 1{,}299$.
- e) $H(X \mid Y) = H(X, Y) - H(Y) \approx 1{,}75 - 1{,}299 = 0{,}451$.
- f) **Vrai** : $H(Y \mid X = \text{payant}) = 1{,}5 > H(Y) \approx 1{,}299$.

Pour la copie : $H(X) + H(Y \mid X) = 1 + 0{,}75 = 1{,}75$ et $H(Y) + H(X \mid Y) \approx 1{,}299 + 0{,}451 = 1{,}75$. $H(Y \mid X = \text{gratuit}) = 0$ : tous les gratuits ont un usage faible. Savoir qu'un utilisateur est payant augmente l'incertitude sur son usage, mais savoir qu'il est gratuit la supprime : **en moyenne**, $H(Y \mid X) = 0{,}75 \le H(Y)$. Le théorème « savoir ne rend pas moins sûr » porte sur la moyenne, pas sur chaque valeur (M06.10, question 6).

**Erreurs fréquentes.** Calculer l'entropie de la ligne sans la diviser par $P(\text{payant})$ (b : 1,25) ; oublier de pondérer, ou oublier la ligne « gratuit » (c : 1,5) ; répondre $H(Y \mid X)$ en e) ; répondre `False` en f) en confondant une valeur de $X$ et la moyenne.

**Variante.** Pour la loi jointe $\begin{pmatrix} \frac{1}{4} & 0 \\ \frac{1}{4} & \frac{1}{2} \end{pmatrix}$ (lignes : $X$), que vaut $H(Y \mid X)$ ? *Réponse* : $\frac{1}{4} \times 0 + \frac{3}{4} \times H\big(\frac{1}{3}, \frac{2}{3}\big) \approx 0{,}75 \times 0{,}918 = 0{,}689$.

### Ex M06.4 — La règle de la chaîne de l'entropie, vérifiée

**Réponses** : a) `1` · b) `0.881` · c) `0.971` · d) `0.926` · e) `1.926` · f) `0.993` · g) `0.933`.

**Démarche.**
- a) $X$ vaut e-mail ou SMS une fois sur deux : $H(X) = 1$.
- b) La ligne « e-mail » divisée par 0,5 : $(0{,}7 ;\ 0{,}3)$, d'entropie $0{,}7 \times 0{,}515 + 0{,}3 \times 1{,}737 \approx 0{,}881$.
- c) La ligne « SMS » divisée par 0,5 : $(0{,}4 ;\ 0{,}6)$, d'entropie $0{,}4 \times 1{,}322 + 0{,}6 \times 0{,}737 \approx 0{,}971$.
- d) $0{,}5 \times 0{,}881 + 0{,}5 \times 0{,}971 \approx 0{,}926$.
- e) $-\big(0{,}35 \log_2 0{,}35 + 0{,}15 \log_2 0{,}15 + 0{,}2 \log_2 0{,}2 + 0{,}3 \log_2 0{,}3\big) \approx 0{,}530 + 0{,}411 + 0{,}464 + 0{,}521 = 1{,}926$.
- f) La loi de $Y$ : $(0{,}55 ;\ 0{,}45)$, d'entropie $\approx 0{,}993$.
- g) $H(X \mid Y) = H(X, Y) - H(Y) \approx 1{,}926 - 0{,}993 = 0{,}933$.

Pour la copie : $H(X) + H(Y \mid X) = 1 + 0{,}926 = 1{,}926$ et $H(Y) + H(X \mid Y) = 0{,}993 + 0{,}933 = 1{,}926$ : c'est e). L'ouverture est la plus prévisible pour l'e-mail ($0{,}881 < 0{,}971$) : 70 % des e-mails sont ouverts, contre 40 % des SMS, une proportion plus proche de 50 %.

**Erreurs fréquentes.** Prendre l'entropie des cases de la ligne sans les diviser par $P(X = x)$ (b : 0,941) ; additionner les deux entropies conditionnelles au lieu d'en faire la moyenne (d : 1,852) ; prendre $H(X) + H(Y)$ pour $H(X, Y)$ (e : 1,993 : ce n'est vrai que pour des variables indépendantes).

**Variante.** Si les deux lignes étaient $(0{,}25 ;\ 0{,}25)$, que vaudrait $H(Y \mid X)$ ? *Réponse* : 1, égale à $H(Y)$ : $X$ et $Y$ seraient indépendantes.

### Ex M06.5 — L'information mutuelle de deux variables

**Réponses** : a) `"7/16"` · b) `0.989` · c) `0.544` · d) `0.522` · e) `0.467` · f) `1.5` · g) `1.033` · h) `False`.

**Démarche.**
- a) $\frac{1}{16} + \frac{2}{16} + \frac{4}{16} = \frac{7}{16}$.
- b) $H(\frac{7}{16}, \frac{9}{16}) = \frac{7}{16}\log_2 \frac{16}{7} + \frac{9}{16}\log_2 \frac{16}{9} \approx 0{,}522 + 0{,}467 = 0{,}989$.
- c) La ligne « vert » divisée par $\frac{1}{2}$ : $(\frac{1}{8}, \frac{7}{8})$, d'entropie $\frac{3}{8} + \frac{7}{8}\log_2 \frac{8}{7} \approx 0{,}375 + 0{,}169 = 0{,}544$.
- d) Les lignes « orange » $(\frac{1}{2}, \frac{1}{2})$ et « rouge » $(1, 0)$ ont les entropies 1 et 0 : $H(Y \mid X) = \frac{1}{2} \times 0{,}544 + \frac{1}{4} \times 1 + \frac{1}{4} \times 0 \approx 0{,}522$.
- e) $I = H(Y) - H(Y \mid X) \approx 0{,}989 - 0{,}522 = 0{,}467$ bit.
- f) La loi de $X$ : $(\frac{1}{2}, \frac{1}{4}, \frac{1}{4})$, d'entropie 1,5.
- g) $H(X \mid Y) = H(X) - I \approx 1{,}5 - 0{,}467 = 1{,}033$.
- h) **Non** : $I > 0$ ; par exemple $P(\text{rouge et ne freine pas}) = 0 \ne \frac{1}{4} \times \frac{9}{16}$.

Pour la copie : $H(X, Y) = \frac{1}{4} + \frac{7}{16}\log_2 \frac{16}{7} + \frac{3}{4} + \frac{1}{2} \approx 2{,}022$, et $H(X) + H(Y) - H(X, Y) \approx 1{,}5 + 0{,}989 - 2{,}022 = 0{,}467$. La case (rouge, freine) contribue le plus : $\frac{1}{4}\log_2 \frac{1/4}{(1/4)(7/16)} = \frac{1}{4}\log_2 \frac{16}{7} \approx 0{,}298$. Deux cases contribuent négativement, là où $p(x, y) < p(x)\,p(y)$ : (vert, freine), $\frac{1}{16}\log_2 \frac{2}{7} \approx -0{,}113$, et (orange, ne freine pas), $\frac{1}{8}\log_2 \frac{8}{9} \approx -0{,}021$. Le total, lui, est toujours positif ou nul.

**Erreurs fréquentes.** Additionner la mauvaise colonne (a : `"9/16"`) ; oublier de diviser la ligne par $P(\text{vert})$ (c) ; ne pas pondérer les lignes (d : la moyenne simple 0,515, ou la somme 1,544) ; répondre $H(Y \mid X)$ en g).

**Variante.** Que vaut $I(X ; Y)$ pour la loi jointe $\begin{pmatrix} \frac{1}{2} & \frac{1}{4} \\ 0 & \frac{1}{4} \end{pmatrix}$ ? *Réponse* : $H(Y) = 1$, $H(Y \mid X) = \frac{3}{4}\,H(\frac{2}{3}, \frac{1}{3}) \approx 0{,}689$, donc $I \approx 0{,}311$ bit.

### Ex M06.6 — Cross-entropy et KL en bits perdus : un code fait pour la mauvaise loi

**Réponses** : a) `2.25` · b) `1` · c) `2.5` · d) `0.25` · e) `250` · f) `0.1733` · g) `-0.25` · h) `True`.

**Démarche.**
- a) $3 \times \frac{1}{4} \times 2 + 2 \times \frac{1}{8} \times 3 = 1{,}5 + 0{,}75 = 2{,}25$.
- b) $-\log_2 \frac{1}{2} = 1$ bit.
- c) Les longueurs du compresseur sont $(1, 3, 3, 3, 3)$ : $H(p, q) = \frac{1}{4} \times 1 + \frac{1}{4} \times 3 + \frac{1}{4} \times 3 + \frac{1}{8} \times 3 + \frac{1}{8} \times 3 = 2{,}5$ bits.
- d) $\mathrm{KL}(p \,\|\, q) = H(p, q) - H(p) = 2{,}5 - 2{,}25 = 0{,}25$ bit.
- e) $1\,000 \times 0{,}25 = 250$ bits perdus.
- f) $0{,}25 \times \ln 2 \approx 0{,}1733$ nat.
- g) $\frac{1}{4}\log_2 \frac{1/4}{1/2} = \frac{1}{4} \times (-1) = -0{,}25$.
- h) **Vrai** : $-\log_2 0 = +\infty$ ; un type que le compresseur croit impossible n'a pas de mot de longueur finie, et $H(p, q) = +\infty$.

Pour la copie : le premier type coûte 1 bit au lieu de 2 (moins cher), les deuxième et troisième 3 bits au lieu de 2 (plus cher), les deux derniers 3 bits, comme avec le meilleur code. Les termes de la somme valent $-0{,}25$ ; $+0{,}25$ ; $+0{,}25$ ; 0 ; 0. Un terme est négatif quand $p_i < q_i$, mais le total ne peut pas l'être : c'est l'inégalité de Gibbs (fiche §6, M06.11), aucun code ne fait mieux que l'entropie en moyenne.

**Erreurs fréquentes.** Prendre $-\log_2 p$ pour la longueur du compresseur (b : 2) ; pondérer les longueurs par $q$ (c : 2, l'entropie de $q$) ; compter la longueur totale au lieu des bits perdus (e : 2 500) ; un signe faux en g).

**Variante.** $\mathrm{KL}(p \,\|\, q)$ pour $p = (\frac{1}{2}, \frac{1}{2})$ et $q = (\frac{3}{4}, \frac{1}{4})$ ? *Réponse* : $\frac{1}{2}\log_2 \frac{2}{3} + \frac{1}{2}\log_2 2 \approx -0{,}292 + 0{,}5 = 0{,}208$ bit.

### Ex M06.7 — L'inégalité de Jensen sur trois exemples

**Réponses** : a) `3` · b) `11` · c) `2` · d) `0.2104` · e) `1.0` · f) `1.3219` · g) `-0.3219` · h) `True`.

**Démarche.**
- a) $\frac{1}{4} + \frac{3}{2} + \frac{5}{4} = 3$ ; b) $\frac{1}{4} + \frac{9}{2} + \frac{25}{4} = 11$ ; c) $11 - 3^2 = 2$.
- d) $\frac{e^0 + e^1}{2} - e^{0{,}5} \approx 1{,}8591 - 1{,}6487 = 0{,}2104$.
- e) $\frac{\log_2 1 + \log_2 4}{2} = \frac{0 + 2}{2} = 1$.
- f) $\mathbb{E}[X_3] = 2{,}5$ et $\log_2 2{,}5 \approx 1{,}3219$.
- g) $1 - 1{,}3219 = -0{,}3219$.
- h) **Vrai** : pour $f(x) = x^2$, l'écart de Jensen est $\mathbb{E}[X^2] - (\mathbb{E}[X])^2$, la formule de la variance (M02b).

Pour la copie : $x^2$ et $e^x$ sont convexes (écarts positifs : 2 et 0,2104) ; $\log_2$ est concave (écart négatif : $-0{,}3219$). C'est bien ce qu'annonce Jensen.

**Erreurs fréquentes.** Calculer $(\mathbb{E}[X])^2$ au lieu de $\mathbb{E}[X^2]$ (b : 9) ; l'écart dans le mauvais ordre (c : $-2$) ; $\ln$ au lieu de $\log_2$ (f : 0,9163).

**Variante.** $X$ vaut 2 ou 8, une fois sur deux, et $f = \sqrt{\,\cdot\,}$ : l'écart de Jensen ? *Réponse* : $\frac{\sqrt{2} + \sqrt{8}}{2} - \sqrt{5} = \frac{3\sqrt{2}}{2} - \sqrt{5} \approx -0{,}115$ (négatif : $\sqrt{\,\cdot\,}$ est concave).

### Ex M06.8 — Kraft : ces longueurs de code sont-elles possibles ?

**Réponses** : a) `"15/16"` · b) `"9/8"` · c) `"19/16"` · d) `1` · e) `1` · f) `2` · g) `False` · h) `1`.

**Démarche.**
- a) $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} = \frac{15}{16}$.
- b) $4 \times \frac{1}{4} + \frac{1}{8} = \frac{9}{8}$.
- c) $\frac{1}{2} + 2 \times \frac{1}{4} + \frac{1}{8} + \frac{1}{16} = \frac{19}{16}$.
- d) $\frac{1}{2} + 3 \times \frac{1}{8} + 2 \times \frac{1}{16} = 1$.
- e) $2 \times \frac{1}{3} + 3 \times \frac{1}{9} = 1$.
- f) Il reste $1 - \frac{1}{2} - \frac{1}{4} = \frac{1}{4}$, soit deux parts de $\frac{1}{8}$ : 2 mots de longueur 3 (par exemple 0, 10, puis 110 et 111).
- g) **Non** : 1 est le début de 10.
- h) $\frac{1}{2} + \frac{1}{4} + \frac{1}{4} = 1$.

Pour la copie : a) oui (0, 10, 110, 1110, avec de la place libre) ; b) et c) non (somme $> 1$) ; d) oui, et le code est complet (0, 100, 101, 110, 1110, 1111) ; e) oui, en ternaire (0, 1, 20, 21, 22). h) ne contredit pas g) : l'inégalité de Kraft dit qu'**il existe** un code préfixe de longueurs $(1, 2, 2)$ (0, 10, 11), pas que **ce** code-là l'est.

**Erreurs fréquentes.** Compter $\frac{1}{\ell}$ au lieu de $2^{-\ell}$ (a : `"25/12"`) ; garder la base 2 pour l'alphabet ternaire (e) ; oublier le mot de longueur 2 en f) (4) ; croire qu'une somme de Kraft $\le 1$ rend tout code préfixe (g).

**Variante.** Les longueurs $(2, 2, 2, 3, 4, 4)$ sont-elles possibles ? *Réponse* : oui, $\frac{3}{4} + \frac{1}{8} + \frac{2}{16} = 1$ : 00, 01, 10, 110, 1110, 1111.

### Ex M06.9 — La longueur moyenne d'un code, comparée à l'entropie

**Réponses** : a) `1.977` · b) `2.0` · c) `1` · d) `[2, 2, 3, 4, 5]` · e) `"23/32"` · f) `2.5` · g) `True` · h) `0.023`.

**Démarche.**
- a) $0{,}45 \times 1{,}152 + 0{,}25 \times 2 + 0{,}15 \times 2{,}737 + 0{,}1 \times 3{,}322 + 0{,}05 \times 4{,}322 \approx 0{,}518 + 0{,}5 + 0{,}411 + 0{,}332 + 0{,}216 = 1{,}977$.
- b) $0{,}45 + 0{,}5 + 0{,}45 + 0{,}4 + 0{,}2 = 2{,}0$.
- c) $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{2}{16} = 1$.
- d) $-\log_2 p_i \approx 1{,}15$ ; 2 ; 2,74 ; 3,32 ; 4,32, arrondis à l'entier supérieur : $(2, 2, 3, 4, 5)$.
- e) $\frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \frac{1}{32} = \frac{23}{32}$.
- f) $0{,}9 + 0{,}5 + 0{,}45 + 0{,}4 + 0{,}25 = 2{,}5$.
- g) **Vrai** : $1{,}977 \le 2{,}5 < 2{,}977$.
- h) $2 - 1{,}977 \approx 0{,}023$ bit.

Pour la copie : un code préfixe de longueurs $(2, 2, 3, 4, 5)$ : 00, 01, 100, 1010, 10110. Le code donné est meilleur (2 bits contre 2,5) : il n'est qu'à 0,023 bit de l'entropie. Les longueurs de Shannon arrondissent toujours vers le haut, et laissent $1 - \frac{23}{32} = \frac{9}{32}$ de la somme de Kraft inutilisés : on aurait pu raccourcir des mots.

**Erreurs fréquentes.** Faire la moyenne simple des longueurs (b : 2,8) ; arrondir $-\log_2 p_i$ à l'entier le plus proche (d : `[1, 2, 3, 3, 4]`, dont la somme de Kraft vaut $\frac{17}{16} > 1$ : aucun code préfixe ne les a) ; l'écart dans le mauvais ordre (h).

**Variante.** Pour $p = (0{,}7 ;\ 0{,}2 ;\ 0{,}1)$, quelles sont les longueurs de Shannon et leur longueur moyenne ? *Réponse* : $(1, 3, 4)$, $\bar{L} = 1{,}7$ ; le code 0, 10, 11 fait mieux, $\bar{L} = 1{,}3$, pour $H \approx 1{,}157$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M06.10 — I(X ; Y) = H(X) − H(X | Y), et l'information mutuelle est positive

**Réponse modèle.**
1. Sur les cases où $p(x, y) > 0$, $\frac{p(x, y)}{p(x)\,p(y)} = \frac{p(y)\,p(x \mid y)}{p(x)\,p(y)} = \frac{p(x \mid y)}{p(x)}$. Donc $I(X ; Y) = \sum p(x, y) \log_2 p(x \mid y) - \sum p(x, y) \log_2 p(x)$. La première somme vaut $-H(X \mid Y)$ (fiche §3). Dans la seconde, on regroupe les cases d'une même valeur $x$ : $\sum_y p(x, y) = p(x)$, et elle vaut $\sum_x p(x) \log_2 p(x) = -H(X)$. D'où $I(X ; Y) = H(X) - H(X \mid Y)$.
2. En écrivant $p(x, y) = p(x)\,p(y \mid x)$, le même calcul donne $I(X ; Y) = H(Y) - H(Y \mid X)$. Avec la règle de la chaîne, $H(X \mid Y) = H(X, Y) - H(Y)$, donc $I(X ; Y) = H(X) + H(Y) - H(X, Y)$.
3. $\mathrm{KL}\big(p_{XY} \,\|\, p_X\,p_Y\big) = \sum p(x, y) \log_2 \frac{p(x, y)}{p(x)\,p(y)}$ sur les cases où $p(x, y) > 0$ : c'est la définition de $I(X ; Y)$. Elle est finie, car $p(x) \ge p(x, y) > 0$ et $p(y) \ge p(x, y) > 0$ sur ces cases. Par l'inégalité de Gibbs, $I(X ; Y) \ge 0$, avec égalité si et seulement si $p(x, y) = p(x)\,p(y)$ pour tous $x$ et $y$, c'est-à-dire si $X$ et $Y$ sont indépendantes.
4. $H(X \mid Y) = H(X) - I(X ; Y) \le H(X)$, et $H(X, Y) = H(X) + H(Y) - I(X ; Y) \le H(X) + H(Y)$ ; égalité dans les deux cas si et seulement si $I = 0$, donc pour des variables indépendantes.
5. $H(X \mid X) = 0$ (connaître $X$, c'est connaître $X$), donc $I(X ; X) = H(X) - 0 = H(X)$.
6. Par exemple la loi jointe $\begin{pmatrix} 0{,}6 & 0{,}1 \\ 0{,}2 & 0{,}1 \end{pmatrix}$ (lignes : $X$, colonnes : $Y$). $X$ a la loi $(0{,}7 ;\ 0{,}3)$, d'entropie environ 0,881. Sachant $Y = $ deuxième colonne, $X$ a la loi $(\frac{1}{2}, \frac{1}{2})$, d'entropie 1, plus grande. Pas de contradiction : la question 4 porte sur la **moyenne** $H(X \mid Y)$, pondérée par les probabilités des colonnes ; la première colonne, de probabilité 0,8, laisse beaucoup moins d'incertitude, et la moyenne reste au-dessous de $H(X)$.

**Grille.** (1) la factorisation $p(x, y) = p(y)\,p(x \mid y)$, puis le regroupement $\sum_y p(x, y) = p(x)$ ; (2) la symétrie et la règle de la chaîne ; (3) $I = \mathrm{KL}(p_{XY} \,\|\, p_X p_Y)$, sa finitude, Gibbs et le cas d'égalité, traduit en indépendance ; (4) les deux inégalités et leur cas d'égalité ; (5) $H(X \mid X) = 0$ ; (6) un tableau qui marche, et la distinction entre une valeur et la moyenne.

### Ex M06.11 — La KL est positive : la preuve par l'inégalité de Jensen

**Réponse modèle.**
1. $\log_2 x = \frac{\ln x}{\ln 2}$, de dérivée seconde $-\frac{1}{x^2 \ln 2} < 0$ sur $]0, +\infty[$ : $\log_2$ est strictement concave.
2. $\mathbb{E}[\log_2 Z] = \sum_{x \in S} p(x) \log_2 \frac{q(x)}{p(x)} = -\mathrm{KL}(p \,\|\, q)$ (la somme qui définit la KL porte sur $S$) ; $\mathbb{E}[Z] = \sum_{x \in S} p(x)\,\frac{q(x)}{p(x)} = \sum_{x \in S} q(x)$, donc $\log_2 \mathbb{E}[Z] = \log_2 \sum_{x \in S} q(x)$.
3. Pour une fonction concave, l'inégalité de Jensen s'écrit $\mathbb{E}[\log_2 Z] \le \log_2 \mathbb{E}[Z]$ : $-\mathrm{KL}(p \,\|\, q) \le \log_2 \sum_{x \in S} q(x)$. Et $\sum_{x \in S} q(x) \le \sum_x q(x) = 1$, donc $\log_2 \sum_{x \in S} q(x) \le 0$. D'où $\mathrm{KL}(p \,\|\, q) \ge 0$.
4. Si $p = q$, chaque terme vaut $p(x) \log_2 1 = 0$. Réciproquement, si $\mathrm{KL}(p \,\|\, q) = 0$, les deux inégalités de 3. sont des égalités. Celle de Jensen, pour une fonction strictement concave, impose que $Z$ soit constante : $q(x) = c\,p(x)$ pour tout $x \in S$. La seconde impose $\sum_{x \in S} q(x) = 1$, donc $c \sum_{x \in S} p(x) = c = 1$ : $q = p$ sur $S$, et $q$ est nulle hors de $S$ (toute sa masse est sur $S$), comme $p$. Donc $q = p$.
5. Avec $m = \frac{p + q}{2}$, $\mathrm{JS}(p, q) = \frac{1}{2}\mathrm{KL}(p \,\|\, m) + \frac{1}{2}\mathrm{KL}(q \,\|\, m)$. Là où $p(x) > 0$, $m(x) \ge \frac{p(x)}{2} > 0$ : la question 3 s'applique, et de même pour $q$. Les deux termes sont positifs ou nuls, donc $\mathrm{JS} \ge 0$. Si $\mathrm{JS} = 0$, les deux KL sont nulles, donc $p = m$ et $q = m$ (question 4) : $p = q$.
6. Si $q(x) = 0$ pour un $x$ de $S$, le terme $p(x) \log_2 \frac{p(x)}{0}$ vaut $+\infty$ : $\mathrm{KL}(p \,\|\, q) = +\infty$, et l'inégalité $\mathrm{KL} \ge 0$ reste vraie, sans démonstration. (La variable $Z$ prendrait la valeur 0, où $\log_2$ n'est pas définie : la preuve de 3. ne s'applique plus.)

**Grille.** (1) la dérivée seconde négative ; (2) les deux espérances écrites sur $S$, et le lien avec la KL ; (3) Jensen dans le bon sens (concave), puis $\sum_S q \le 1$ ; (4) les deux sens de l'équivalence, avec les **deux** cas d'égalité (Jensen : $Z$ constante ; et $\sum_S q = 1$) ; (5) $m > 0$ là où il faut, la somme de deux termes positifs, et le cas d'égalité ; (6) la KL infinie, et pourquoi la preuve ne s'applique plus.

<a id="reflexion"></a>

## 🔗 🧮 🗣️ Pont, estimation et explication

### Ex M06.12 — La log loss d'un classifieur, une cross-entropy moyenne

**Réponses** : a) `1.3863` · b) `0.602` · c) `0.8685` · d) `1.0986` · e) `True` · f) `1.8257`.

**Démarche.** La cross-entropy d'une image entre la loi « vraie » (toute la probabilité sur sa vraie classe) et la prédiction ne garde qu'un terme : $-\ln(\text{probabilité donnée à la vraie classe})$.
- a) L'image 3 est de classe C, prédite avec 0,25 : $-\ln 0{,}25 = \ln 4 \approx 1{,}3863$.
- b) $\frac{-\ln 0{,}5 - \ln 0{,}8 - \ln 0{,}25 - \ln 0{,}9}{4} \approx \frac{0{,}6931 + 0{,}2231 + 1{,}3863 + 0{,}1054}{4} \approx 0{,}6020$ nat.
- c) $\frac{0{,}6020}{\ln 2} \approx 0{,}8685$ bit.
- d) Chaque image coûte $-\ln \frac{1}{3} = \ln 3 \approx 1{,}0986$ nat.
- e) **Vrai** : $0{,}602 < 1{,}099$.
- f) $e^{0{,}6020} \approx 1{,}8257$.

Pour la copie : l'image 3 coûte le plus cher : le classifieur y donne 0,6 à la mauvaise classe A et seulement 0,25 à la bonne. f) se lit comme une perplexité : le classifieur hésite en moyenne comme s'il choisissait au hasard entre 1,83 classes également probables (le modèle uniforme, lui, hésite entre 3). Avec la probabilité 0 pour la classe C, la cross-entropy de l'image 3 serait $-\ln 0 = +\infty$ : une seule erreur certaine rend la log loss infinie (d'où les probabilités jamais tout à fait nulles en pratique).

**Erreurs fréquentes.** Prendre la plus grande probabilité prédite au lieu de celle de la vraie classe (a : 0,5108) ; faire la somme au lieu de la moyenne (b : 2,4079) ; $\log_2$ au lieu de $\ln$ (a : 2 ; b : 0,8685) ; $2^{0{,}602}$ au lieu de $e^{0{,}602}$ (f).

**Variante.** Un modèle qui donne toujours 0,9 à la vraie classe : sa log loss ? *Réponse* : $-\ln 0{,}9 \approx 0{,}105$ nat.

### Ex M06.13 — Choisir une feature par l'information mutuelle

**Réponses** : a) `0.1187` · b) `0.029` · c) `0.239` · d) `"F3"` · e) `0.761` · f) `0.0823` · g) `True`.

**Démarche.** Dans les trois tableaux, $Y$ a la loi $(\frac{1}{2}, \frac{1}{2})$ : $H(Y) = 1$, et $I(F ; Y) = 1 - H(Y \mid F)$.
- a) Chaque ligne de $F_1$, divisée par 10, a la loi $(0{,}7 ;\ 0{,}3)$, d'entropie 0,8813 : $I = 1 - 0{,}8813 \approx 0{,}1187$.
- b) Chaque ligne de $F_2$ a la loi $(0{,}6 ;\ 0{,}4)$, d'entropie 0,9710 : $I \approx 0{,}0290$.
- c) $H(Y \mid F_3) = \frac{4}{20} \times 0 + \frac{6}{20}\,H\big(\frac{1}{3}, \frac{2}{3}\big) + \frac{10}{20}\,H(0{,}4 ;\ 0{,}6) \approx 0{,}2755 + 0{,}4855 = 0{,}7610$, donc $I \approx 0{,}2390$.
- d) $F_3$.
- e) $H(Y \mid F_3) \approx 0{,}7610$ (calculée en c)).
- f) $0{,}1187 \times \ln 2 \approx 0{,}0823$ nat.
- g) **Vrai** : chaque valeur ne concerne qu'un client, donc $H(Y \mid F) = 0$ sur ces données, et $I(F ; Y) = H(Y) = 1$, le maximum.

Pour la copie : le numéro de client « explique » parfaitement les 20 achats observés, mais un nouveau client a un numéro jamais vu : la feature n'apprend rien de général, elle ne fait que mémoriser. $F_3$ part avec un avantage : avec plus de valeurs, donc plus de cases, ses fréquences ont plus de liberté pour s'écarter de l'indépendance, et l'information mutuelle estimée sur peu de données augmente (M06.20 e)). Ici, $F_3$ est aussi réellement informative (les jeunes achètent tous), mais 20 clients ne suffisent pas pour en être sûr.

**Erreurs fréquentes.** Oublier de diviser les comptages par 20, ou chaque ligne par son total ; prendre $I$ pour $H(Y \mid F_3)$ en e) ; donner f) en bits.

**Variante.** Une feature égale à $Y$ (un tableau diagonal $\begin{pmatrix} 10 & 0 \\ 0 & 10 \end{pmatrix}$) : son information mutuelle avec $Y$ ? *Réponse* : $H(Y) = 1$ bit.

### Ex M06.14 — Fermi : combien de bits pour un génome humain ?

**Réponse modèle.**
1. Quatre lettres : 2 bits par base (00, 01, 10, 11). $3 \times 10^9 \times 2 = 6 \times 10^9$ bits, soit $\frac{6 \times 10^9}{8} = 7{,}5 \times 10^8$ octets, environ **750 Mo**.
2. $H = 2 \times 0{,}3 \log_2 \frac{1}{0{,}3} + 2 \times 0{,}2 \log_2 5 \approx 1{,}042 + 0{,}929 = 1{,}971$ bit par base. On gagnerait moins de 1,5 %, environ 11 Mo : presque rien.
3. Les bases voisines ne sont pas indépendantes : des motifs se répètent (de longues répétitions, des paires CG rares…). Un compresseur qui regarde le **contexte** code chaque base avec l'incertitude qui reste sachant les précédentes, une entropie conditionnelle, plus petite que l'entropie de 2., qui traite chaque base comme tirée au hasard, indépendamment des autres.
4. $0{,}1\,\% \times 3 \times 10^9 = 3 \times 10^6$ différences ; à $32 + 2 = 34$ bits chacune, environ $10^8$ bits, soit **13 Mo** environ.
5. Quelques photos de téléphone : près de 60 fois moins qu'en 1.
6. Ce qu'il faut décrire, c'est l'incertitude qui reste **sachant** la référence, une entropie conditionnelle : deux génomes humains ont une information mutuelle énorme. Plus un message connu est lié à celui qu'on veut transmettre, moins il reste de bits à envoyer.

**Grille.** (1) 2 bits par base et la conversion en octets ; (2) l'entropie de la loi donnée et un gain minuscule ; (3) la dépendance entre bases voisines, et ce que l'entropie de 2. ignore ; (4) le nombre de différences et la taille ; (5) une comparaison parlante ; (6) le lien avec l'entropie conditionnelle ou l'information mutuelle.

### Ex M06.15 — Expliquer l'information mutuelle avec deux capteurs

**Réponse modèle.**

> L'incertitude sur un capteur, c'est à quel point sa prochaine mesure est difficile à deviner. L'information mutuelle mesure combien cette incertitude baisse quand on lit l'autre capteur. Elle est la même dans les deux sens : c'est la part d'incertitude que les deux capteurs ont en commun, ce que l'un « sait » de l'autre. Tes deux thermomètres, dans des pièces voisines, montent et descendent ensemble : lire l'un permet de bien deviner l'autre, leur information mutuelle est grande. Le détecteur de porte et le thermomètre du salon n'ont presque rien en commun : lire l'un ne change pas ce qu'on prévoit pour l'autre, leur information mutuelle est proche de zéro. Elle est exactement nulle quand les deux mesures sont indépendantes, et seulement dans ce cas : elle voit n'importe quel lien, pas seulement les liens en ligne droite.

**Grille.** (1) l'incertitude sur un capteur comme difficulté à deviner sa mesure ; (2) l'information mutuelle comme baisse de cette incertitude quand on lit l'autre ; (3) la symétrie (une part commune) ; (4) les deux thermomètres voisins : grande ; (5) nulle exactement pour des capteurs indépendants, et n'importe quel lien détecté ; (6) huit lignes au plus, sans formule.

<a id="entretien"></a>

## 💼 Entretien

### M06.E1 — Information mutuelle ou corrélation : laquelle détecte quoi ?

**Réponse modèle (60 secondes).**

> La corrélation de Pearson mesure un lien **linéaire** entre deux variables numériques : elle vaut plus ou moins 1 si les points sont alignés, et elle peut être nulle alors que la dépendance est totale. L'exemple classique : une feature symétrique autour de zéro et une cible égale à son carré ; la corrélation est nulle, et pourtant connaître la feature donne exactement la cible. L'information mutuelle, elle, mesure de combien l'incertitude sur la cible baisse quand on connaît la feature, en bits ou en nats ; elle est nulle si et seulement si les deux sont indépendantes, et elle voit n'importe quel lien, y compris pour des variables catégorielles. La corrélation garde des avantages : elle se calcule directement, sans découper les valeurs en classes ni estimer une densité, elle a un signe qui dit le sens du lien, et elle est fiable même sur peu de données, alors que l'information mutuelle estimée est biaisée vers le haut sur un petit échantillon, surtout pour une feature à beaucoup de valeurs. En pratique, je regarde les deux, et je préfère l'information mutuelle pour classer des features quand je soupçonne des liens non linéaires.

**Grille.** (1) la corrélation : lien linéaire, et son signe ; (2) un exemple de corrélation nulle avec une dépendance forte ($Y = X^2$) ; (3) l'information mutuelle : baisse d'incertitude, nulle seulement pour l'indépendance, tout type de lien ; (4) au moins un avantage de la corrélation (simple, signée, fiable sur peu de données) ; (5) le biais de l'information mutuelle estimée.

<a id="notebook"></a>

## Notebook

### Ex M06.16 — Entropies conjointe et conditionnelle d'un tableau · `joint_entropy, conditional_entropy`

**Réponses** : a) `2.366` · b) `1.395` · c) `0.8071` · d) `1.64` · e) `"ValueError"` · f) `"ValueError"` · g) `0.6098` · h) `"float"`.

**Démarche.** Une fonction privée qui vérifie la loi jointe : `table = np.asarray(joint, dtype=float)`, puis une `ValueError` si `table.ndim != 2` ou `table.size == 0`, si `not np.all(table >= 0)` (ce test refuse aussi `nan`, pour lequel toute comparaison est fausse) ou si `abs(table.sum() - 1) > 1e-9` ; une autre qui vérifie `base > 1` et renvoie `math.log(base)`. Puis `p = table[table > 0]` et `float(-np.sum(p * np.log(p)) / math.log(base))` pour l'entropie conjointe ; l'entropie conditionnelle par la règle de la chaîne, `joint_entropy(table, base) - ` l'entropie des sommes des lignes `table.sum(axis=1)`, ou par la double somme $\sum p(x, y) \log \frac{p(x)}{p(x, y)}$. Pour la copie : c) est $H(X \mid Y)$, car la fonction conditionne toujours par la variable des lignes ; b) $= 0{,}4 \times 1{,}5 + 0{,}6 \times 1{,}3250 \approx 1{,}3950$. Le tableau de e) somme à 1 mais contient une case négative, qui n'est pas une probabilité. g) est l'entropie de $(0{,}15 ;\ 0{,}85)$ : les cases nulles comptent pour 0.

**Erreurs fréquentes.** `np.log(table)` sur tout le tableau (les cases nulles donnent `nan`, ou `-inf` multiplié par 0) ; conditionner par les colonnes (b : 0,8071) ; tester `np.any(table < 0)`, qui laisse passer `nan` ; renvoyer un `numpy.float64` (h).

### Ex M06.17 — L'information mutuelle · `mutual_information`

**Réponses** : a) `0.1805` · b) `True` · c) `0.0` · d) `1.361` · e) `0.1251` · f) `"ValueError"` · g) `"float"`.

**Démarche.** `product = np.outer(table.sum(axis=1), table.sum(axis=0))` donne $p(x)\,p(y)$ case par case ; sur les cases `table > 0`, `np.sum(p * np.log(p / product[positive])) / math.log(base)`, puis `0.0` si le résultat est entre $-10^{-12}$ et 0. Ou bien $H(Y) - H(Y \mid X)$ avec les fonctions de M06.16. Pour la copie : `np.outer` construit la loi jointe de deux variables **indépendantes**, d'où c) $= 0$ ; le tableau diagonal de d) dit que $Y = X$ : $H(Y \mid X) = 0$ et $I = H(0{,}1 ;\ 0{,}4 ;\ 0{,}5) \approx 1{,}3610$. f) : `nan < 0` est faux, donc `np.any(table < 0)` ne voit pas `nan` ; `np.all(table >= 0)` le refuse.

**Erreurs fréquentes.** Multiplier par la marge de la ligne seulement ; écrire $H(Y) - H(X \mid Y)$ (a : $-0{,}390$) ; oublier un terme dans $H(X) + H(Y) - H(X, Y)$ ; une valeur négative minuscule ($-10^{-17}$) au lieu de 0 en c).

### Ex M06.18 — Codes préfixes et somme de Kraft · `kraft_sum, is_prefix_code`

**Réponses** : a) `0.8125` · b) `0.5926` · c) `"ValueError"` · d) `True` · e) `False` · f) `False` · g) `"ValueError"` · h) `True`.

**Démarche.** `kraft_sum` : les vérifications (liste non vide, `alphabet >= 2`, chaque longueur `>= 1`), puis `float(sum(Fraction(1, alphabet ** length) for length in lengths))` (les fractions évitent les erreurs d'arrondi des grandes longueurs) ou `sum(alphabet ** -length)`. `is_prefix_code` : `words = [str(w) for w in codewords]` (un texte de NumPy devient un `str`), une `ValueError` si un mot est vide, puis soit deux boucles (`words[j].startswith(words[i])` pour $i \ne j$), soit le tri : après `words.sort()`, un mot qui en commence un autre est juste avant un mot qu'il commence, et il suffit de comparer les voisins. Pour la copie : a) $\frac{13}{16} \le 1$ et b) $\frac{16}{27} \le 1$ : des codes préfixes de ces longueurs existent. Le mot vide de g) serait le début de tous les mots.

**Erreurs fréquentes.** Comparer chaque paire dans un seul sens (e : « 10 » est le début de « 101 », placé après lui) ; oublier qu'un mot répété est le début de sa copie (f) ; renvoyer un booléen de NumPy (h) ; ignorer `alphabet` (b : 1,125).

### Ex M06.19 — L'écart de Jensen d'une loi discrète · `jensen_gap`

**Réponses** : a) `3.64` · b) `-0.3751` · c) `0.5431` · d) `2.0` · e) `"ValueError"` · f) `"ValueError"` · g) `"float"`.

**Démarche.** `x = np.asarray(values, dtype=float)`, une `ValueError` si `x.size == 0` ; les poids égaux `np.full(x.size, 1 / x.size)` par défaut, sinon une `ValueError` si leur forme diffère, si `not np.all(w >= 0)` ou si `abs(w.sum() - 1) > 1e-9`. Puis `expected_f = sum(wi * f(float(xi)) for xi, wi in zip(x, w))` (f valeur par valeur : `math.log` refuse un tableau) et `float(expected_f - f(float(np.dot(w, x))))`. Pour la copie : a) est la variance de $X$ (convexe, écart positif) ; b) $\ln$ est concave (négatif) ; c) $\exp$ est convexe (positif) ; d) `abs` est convexe : l'écart vaut 2, et il ne serait nul que si toutes les valeurs avaient le même signe, là où `abs` est affine.

**Erreurs fréquentes.** L'écart dans le mauvais ordre (signes inversés) ; ignorer les poids (a : 4,2222) ; appeler `f` sur tout le tableau (`TypeError` avec `math.log`) ; vérifier la longueur après avoir divisé par elle (f : `ZeroDivisionError`).

### Ex M06.20 — `sklearn.metrics.mutual_info_score` contre ta fonction, en nats

**Réponses** : a) `0.3356` · b) `0.4842` · c) `1.0889` · d) `False` · e) `0.0923`.

**Démarche.** a) `mutual_info_score(x_20, y_20)` ; b) divisé par `math.log(2)` ; c) `mutual_info_score(x_20, x_20)` donne $I(X ; X) = H(X)$, en nats : l'entropie de $(0{,}3 ;\ 0{,}3 ;\ 0{,}4)$ ; d) `mutual_info_score(np.array(["rouge", "vert", "bleu"])[x_20], y_20)` donne la même valeur : seules comptent les observations qui ont la même valeur ; e) `rng = np.random.default_rng(620)` puis `mutual_info_score(x_20, rng.permutation(y_20))`. Pour la copie : après le mélange, les variables sont indépendantes, mais les fréquences de 40 observations, réparties dans 9 cases, s'écartent toujours un peu du produit des marges ; l'information mutuelle estimée, positive ou nulle, ne peut se tromper que vers le haut. Son biais est d'environ $\frac{(3 - 1)(3 - 1)}{2n} = 0{,}05$ nat pour $n = 40$, 100 fois moins pour $n = 4\,000$. Sur peu de données, une feature à beaucoup de valeurs paraît donc informative même quand elle ne l'est pas (M06.13 g)).

**Erreurs fréquentes.** Convertir a) en bits ; oublier que scikit-learn travaille en nats (b et c) ; appeler `rng.permutation` deux fois, ou créer `rng` plus tôt et s'en servir avant (e).

### Ex M06.21 — Prédire : l'information mutuelle de X et 2X, de X et X²

**Réponses** : a) `3` · b) `3` · c) `1` · d) `2`.

**Démarche.** a) $2X$ et $X$ se déterminent l'un l'autre : $H(X \mid 2X) = 0$, donc $I(X ; 2X) = H(X) = \log_2 5 \approx 2{,}322$. b) et d) $X^2$ est une fonction de $X$ : $H(X^2 \mid X) = 0$, donc $I(X ; X^2) = H(X^2) - 0 = H\big(\frac{1}{5}, \frac{2}{5}, \frac{2}{5}\big) \approx 1{,}522$, strictement entre 0 et $H(X)$. Ce qui reste inconnu sur $X$ quand on connaît $X^2$, c'est son signe : $H(X \mid X^2) = \frac{1}{5} \times 0 + \frac{4}{5} \times 1 = 0{,}8$ bit. c) $\mathrm{Cov}(X, X^2) = \mathbb{E}[X^3] - \mathbb{E}[X]\,\mathbb{E}[X^2] = 0 - 0 = 0$ par symétrie : la corrélation, qui ne voit que les liens linéaires, est nulle (la figure du nuage $Y \approx X^2$, fiche §4).

### Ex M06.22 — Estimer une entropie à partir d'un échantillon : le biais des petits échantillons

**Réponses** : a) `1.955` · b) `-0.405` · c) `-0.034` · d) `0.92` · e) `-0.044`.

**Démarche.** `freq = np.bincount(sample, minlength=k) / len(sample)`, `freq = freq[freq > 0]`, puis `float(-np.sum(freq * np.log2(freq)))`. Pour la copie : le plug-in **sous-estime** l'entropie. Une issue rare (0,05) est absente d'un échantillon de taille 10 environ six fois sur dix ($0{,}95^{10} \approx 0{,}6$) : elle compte alors pour 0 ; et, plus généralement, les fréquences observées sont en moyenne plus inégales que les vraies probabilités. Le biais passe de $-0{,}405$ ($n = 10$) à $-0{,}034$ ($n = 100$) ; l'approximation $-\frac{k - 1}{2n\ln 2}$ donne $-0{,}361$ et $-0{,}036$ : elle est bonne pour les grands échantillons, moins pour $n = 10$, où la correction de Miller-Madow laisse un biais de $-0{,}044$. L'information mutuelle estimée se calcule avec des entropies estimées : sur peu de données, elle est biaisée elle aussi, mais vers le haut (M06.20 e)).

**Erreurs fréquentes.** Oublier `minlength` (pas grave ici, les fréquences nulles ne comptent pas, mais indispensable dès qu'on veut le vecteur des fréquences) ; `np.log` au lieu de `np.log2` (a : 1,355) ; le biais dans le mauvais ordre (b et c positifs).

### Ex M06.23 — Un diagramme de l'information : H(X), H(Y), H(X | Y), I(X ; Y)

**Démarche.** Avec $h_{XY} = H(X, Y)$, $a = H(X \mid Y)$ (la fonction `conditional_entropy` sur le tableau transposé), $I$ et $b = H(Y \mid X)$ : `ax.barh(2, a)`, `ax.barh(2, I, left=a)` ; `ax.barh(1, I, left=a)`, `ax.barh(1, b, left=a + I)` ; `ax.barh(0, h_XY)` ; `ax.set_yticks([2, 1, 0], labels=["H(X)", "H(Y)", "H(X, Y)"])` et `ax.set_xlabel("bits")`. Pour la copie : la première barre dit $H(X) = H(X \mid Y) + I$, la deuxième $H(Y) = I + H(Y \mid X)$, et la troisième $H(X, Y) = H(X \mid Y) + I + H(Y \mid X)$ ; les règles de la chaîne et les trois écritures de $I$ s'y lisent directement. Pour deux variables indépendantes, le morceau commun disparaît : les barres de $H(X)$ et de $H(Y)$ se suivent sans se chevaucher. Si $Y = X$, $H(X \mid Y) = H(Y \mid X) = 0$ et les trois barres ont la même longueur.

**Erreurs fréquentes.** Commencer la barre de $H(Y)$ à 0 (les deux morceaux $I$ ne sont plus alignés) ; `ax.bar` au lieu de `ax.barh` (des barres verticales) ; ouvrir une nouvelle figure dans la fonction.

### Ex M06.24 — Chasse à l'erreur : log en base 10, 0 log 0, KL à l'envers

**Réponses** : a) `"ACD"` · b) `[1.406, 0.974, 1.75, 0.344, 3.0, 3.364]`.

**Démarche.** (A) $0 \times \log_2 0$ vaut `nan` pour NumPy ($0 \times (-\infty)$) : la somme est `nan`. Il faut garder les probabilités non nulles (ou `xlogy`, M06.25) : $H(p) = 0{,}5 + 0{,}375\log_2 \frac{8}{3} + 0{,}375 \approx 1{,}406$. (C) `log10` donne la cross-entropy en base 10, $1{,}75 \log_{10} 2 \approx 0{,}527$ : il faut `log2`, $H(p, q) = 0{,}5 \times 2 + 0{,}375 \times 1 + 0{,}125 \times 3 = 1{,}75$. (D) Les deux lois sont échangées : c'est $\mathrm{KL}(q \,\|\, p)$, infinie ici (`inf`), car $q$ donne une probabilité à la 4ᵉ issue et $p$ non ; $\mathrm{KL}(p \,\|\, q) = 1{,}75 - 1{,}406 \approx 0{,}344$. (B), (E) et (F) sont justes : $1{,}406 \ln 2 \approx 0{,}974$ nat, $-\log_2 0{,}125 = 3$ bits, $2^{1{,}75} \approx 3{,}364$. Pour la copie : `nan` et `inf` se voient, mais (C) renvoie un nombre plausible, et passe inaperçue si l'on ne vérifie pas l'unité.

**Erreurs fréquentes.** Croire (B) fausse (elle convertit bien des bits en nats) ; ne pas voir (A) parce que la formule est celle de la fiche : c'est la probabilité nulle qui la casse ; croire (F) fausse parce qu'elle utilise $H(p, q)$ et pas $H(p)$ : la perplexité d'un modèle se calcule avec sa cross-entropy.

### Ex M06.25 — Calculer 0 log 0 proprement (`scipy.special.xlogy`)

**Réponse** : `1.2192`.

**Démarche.** `p = np.asarray(p, dtype=float)`, puis `return float(-np.sum(xlogy(p, p)) / math.log(base))`. Pour la copie : $x \ln x \to 0$ quand $x \to 0^+$ (R7, M05a) : une issue impossible n'apporte rien à l'entropie, et la convention prolonge $x \ln x$ par continuité. `scipy.special.entr(p)` renvoie directement $-p \ln p$, avec la même convention. L'entropie de chaque ligne d'un tableau `t` dont chaque ligne est une loi : `-xlogy(t, t).sum(axis=1) / math.log(2)`.

**Erreurs fréquentes.** Oublier de diviser par $\ln(\text{base})$ (des nats : 0,8451) ; `np.sum(xlogy(p, p), axis=0)` sur une loi jointe (un vecteur au lieu d'un nombre) ; un filtre `p[p > 0]`, juste, mais que l'exercice remplace justement par `xlogy`.

### Ex M06.26 — Défi : deviner un nombre de 1 à 100 en un minimum de questions

**Réponse** : `5.3102`.

**Démarche.** On garde l'intervalle `lo..hi` des nombres encore possibles, et l'on choisit le seuil `t` qui coupe la **probabilité** restante en deux parts aussi égales que possible : avec les probabilités cumulées `cumulative[k] = P(nombre ≤ k)`, le `t` de `lo..hi − 1` dont `cumulative[t]` est le plus proche de `(cumulative[lo − 1] + cumulative[hi]) / 2`. Pour la loi uniforme, c'est la dichotomie : 7 questions au plus, 6,72 en moyenne. Pour la loi en $\frac{1}{n}$, environ 5,37 questions en moyenne, contre 6,83 pour la dichotomie, et `bound_26` $\approx 5{,}3102$ bits. Pour la copie : avec 6 questions, on distingue au plus $2^6 = 64$ nombres, avec 7, $2^7 = 128$ ; pour 100 nombres, au mieux 28 nombres demandent 6 questions et 72 en demandent 7, soit $\frac{28 \times 6 + 72 \times 7}{100} = 6{,}72$ (pour une entropie de $\log_2 100 \approx 6{,}64$). Pour la seconde loi, couper l'intervalle en deux moitiés de même longueur pose autant de questions pour 1, très probable, que pour 100, très rare ; couper la probabilité en deux donne des réponses courtes aux nombres probables, comme un bon code donne des mots courts aux symboles fréquents. Le score, 5,37, est à moins de 0,06 question de l'entropie.

**Erreurs fréquentes.** Couper l'intervalle en deux moitiés de même longueur (6,83 pour la seconde loi) ; une boucle qui ne réduit pas l'intervalle quand la réponse est « non » (`lo = t` au lieu de `lo = t + 1` : elle tourne en rond) ; calculer `bound_26` en nats (3,6808) ou pour la loi uniforme (6,6439).
