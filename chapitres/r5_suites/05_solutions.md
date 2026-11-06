# R5 · Suites — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R5.Q1 — Explicite ou par récurrence ?
1. **Explicite** : la formule donne $u_n$ à partir de $n$ seul.
2. **Par récurrence** : $u_{n+1}$ se calcule à partir de $u_n$ (et de $n$), en partant de $u_0$.
3. $u_{20} = 400 + 1 = $ **401**.
4. **Non** : la règle ne donne $u_{20}$ qu'à partir de $u_{19}$, qui demande $u_{18}$, et ainsi de suite (le §5 de la fiche donne un raccourci pour ce type de règle, mais la règle seule n'en donne pas).
5. **Faux** : il manque le premier terme. Avec $u_0 = 2$, on obtient 2, 4, 16, 256… ; avec $u_0 = 1$, la suite constante 1.
6. $1, -1, 1, -1$ : **ni croissante ni décroissante**, elle monte et descend à chaque pas.

### R5.Q2 — Arithmétique, géométrique, ou ni l'une ni l'autre ?
1. **Arithmétique**, de raison 5.
2. **Géométrique**, de raison 2.
3. **Aucune** : différences 3, 5, 7 ; quotients 4, 2,25, 1,78 (ce sont les carrés $(n + 1)^2$).
4. **Arithmétique**, de raison −3.
5. **Géométrique**, de raison −3.
6. **Les deux** : arithmétique de raison 0 et géométrique de raison 1.
7. **Géométrique**, de raison 0,9 : $u_{n+1} = 7 \times 0{,}9^{n+1} = 0{,}9\,u_n$.

### R5.Q3 — Formules de somme : vrai ou faux
1. **Vrai** : $100 \times \frac{1 + 100}{2} = 5\,050$.
2. **Faux** : de 0 à $n$, il y a $n + 1$ termes.
3. **Faux** : seulement pour $q \ne 1$ (pour $q = 1$, la formule divise par zéro).
4. **Vrai** : $n$ termes égaux à 1.
5. **Vrai** : c'est la règle « nombre de termes × (premier + dernier) / 2 ».
6. **Vrai** : $1 + 5 + 25 + 125 = 156 = \frac{625 - 1}{4}$ (4 termes, raison 5 : $\frac{5^4 - 1}{5 - 1}$).
7. **Faux** : la somme commence à $3^1 = 3$ et a 5 termes : $3 \times \frac{1 - 3^5}{1 - 3} = 363$. La formule proposée, $\frac{1 - 3^5}{1 - 3} = 121$, est celle de $\sum_{k=0}^{4} 3^k$.

### R5.Q4 — Converge ou diverge ?
1. **Converge vers 0** ($-1 < 0{,}8 < 1$).
2. **Tend vers $+\infty$** ($1{,}02 > 1$), lentement : $1{,}02^{100} \approx 7{,}2$.
3. **Pas de limite** : elle oscille entre 1 et −1.
4. **Converge vers 3** : $\frac{1}{n} \to 0$.
5. **Converge vers 0**, en changeant de signe : $\lvert -0{,}5 \rvert < 1$.
6. **Tend vers $+\infty$** : $n(n - 10)$, produit de deux facteurs qui tendent vers $+\infty$ (elle est négative au début, mais pas pour $n > 10$).
7. **Faux** : $(-1)^n$ ne tend pas vers $+\infty$ et ne converge pas.

### R5.Q5 — Moyenne mobile ou moyenne exponentielle ?
1. **La moyenne exponentielle** : $v_t = \beta\,v_{t-1} + (1 - \beta)\,x_t$.
2. **La moyenne mobile** : chaque valeur de la fenêtre pèse $\frac{1}{k}$.
3. **La moyenne mobile** : pas de moyenne tant que la fenêtre n'est pas pleine.
4. $10 - 4 + 1 = $ **7**.
5. **Trop bas** : $v_1 = (1 - \beta) \times 50$, bien en dessous de 50.
6. **Augmenter** $\beta$ : la moyenne garde plus de passé.

### R5.Q6 — Les poids d'une moyenne exponentielle
1. **0,3**.
2. **Vrai** : $v_t = 0{,}3\,x_t + 0{,}7\,v_{t-1}$, et $x_{t-1}$ entre dans $v_{t-1}$ avec le poids 0,3, donc dans $v_t$ avec $0{,}7 \times 0{,}3 = 0{,}21$.
3. **Géométrique**, de raison **0,7** : 0,3 ; 0,21 ; 0,147…
4. **La plus récente** (poids 0,3, les autres sont plus petits).
5. **Vrai** : $\frac{1}{5} = 0{,}2$.
6. $v_t = x_t$ : aucun lissage.

<a id="rappels"></a>

## 🔁 Rappels

### R5.R1 — Σ et changement d'indice (R4)
1. $1 + 3 + 5 + 7 = 16$.
2. **$n$ termes** pour chacune : de 0 à $n - 1$, et de 1 à $n$.
3. $\sum_{j=0}^{5} 5^j$ : quand $k$ va de 1 à 6, $j = k - 1$ va de 0 à 5.
4. $\frac{30 \times 31}{2} = 465$.

### R5.R2 — Raisonnement par récurrence (R4)
1. $u_1 = 4$, $u_2 = 10$, $u_3 = 28$.
2. $4 = 3 + 1$, $10 = 9 + 1$, $28 = 27 + 1$ (et $u_0 = 2 = 3^0 + 1$) : on conjecture $u_n = 3^n + 1$.
3. Pour $n \ge 0$, notons $P(n)$ : « $u_n = 3^n + 1$ ». *Initialisation* : $u_0 = 2 = 3^0 + 1$. *Hérédité* : soit $n \ge 0$ tel que $u_n = 3^n + 1$ ; alors $u_{n+1} = 3u_n - 2 = 3(3^n + 1) - 2 = 3^{n+1} + 1$, c'est $P(n + 1)$. *Conclusion* : par récurrence, $u_n = 3^n + 1$ pour tout $n \ge 0$. ∎

### R5.R3 — Évolutions successives (R1)
1. $80 \times 1{,}05 = 84$ €.
2. Par $1 - 0{,}12 = 0{,}88$.
3. **Non** : $1{,}1 \times 0{,}9 = 0{,}99$, une **baisse de 1 %**.
4. $1{,}2^3 = 1{,}728$ : une hausse de 72,8 %, **pas** de 60 % (chaque hausse porte sur un prix déjà augmenté).

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R5.1 — Calculer des termes : explicite et récurrence

**Réponses** : a) `11` · b) `71` · c) `[2, 0, -4]` · d) `16` · e) `"n**2"` · f) `"2*n - 2"` · g) `1`.

**Démarche.**
- a) $u_5 = 25 - 15 + 1 = 11$ ; b) $u_{10} = 100 - 30 + 1 = 71$.
- c) $v_1 = 2 \times 3 - 4 = 2$, $v_2 = 2 \times 2 - 4 = 0$, $v_3 = 2 \times 0 - 4 = -4$.
- d) La règle part de $n = 1$ : $w_2 = w_1 + 2 \times 1 + 1 = 4$, $w_3 = 4 + 2 \times 2 + 1 = 9$, $w_4 = 9 + 2 \times 3 + 1 = 16$.
- e) 1, 4, 9, 16 : les carrés, $w_n = n^2$. (On le démontrerait par récurrence : $n^2 + 2n + 1 = (n + 1)^2$.)
- f) $u_{n+1} - u_n = (n + 1)^2 - 3(n + 1) + 1 - (n^2 - 3n + 1) = n^2 + 2n + 1 - 3n - 3 + 1 - n^2 + 3n - 1 = 2n - 2$.
- g) $2n - 2 \ge 0 \iff n \ge 1$ : $u_1 = u_2 = -1$, puis la suite croît. Pour $n = 0$, $u_1 - u_0 = -2 < 0$.

**Erreurs fréquentes.** Calculer $u_4$ pour « $u_5$ » (en comptant les termes à partir de 1) ; écrire $2(v_n - 4)$ au lieu de $2v_n - 4$ ; prendre $n = 2$ dans la règle pour calculer $w_2$ ; oublier le double produit de $(n + 1)^2$.

**Variante.** $u_n = 2n^2 - 5n$ : la différence $u_{n+1} - u_n$, et le rang à partir duquel la suite croît ? *Réponse* : $4n - 3$, positive pour $n \ge 1$ ; la suite croît à partir du rang 1 ($u_1 = -3$, $u_2 = -2$).

### Ex R5.2 — Terme général d'une suite arithmétique

**Réponses** : a) `"7 + 4*n"` · b) `107` · c) `-13` · d) `6` · e) `504` · f) `False` · g) `16`.

**Démarche.**
- a) $u_n = u_0 + n\,r = 7 + 4n$ ; b) $u_{25} = 7 + 100 = 107$.
- c) $(a_n)$ commence au rang 1 : $a_n = 12 - 2{,}5(n - 1)$, donc $a_{11} = 12 - 25 = -13$.
- d) $12 - 2{,}5(n - 1) < 0 \iff n - 1 > 4{,}8 \iff n > 5{,}8$ : le premier rang est 6 ($a_5 = 2$, $a_6 = -0{,}5$).
- e) $7 + 4n = 2\,023 \iff n = 504$.
- f) $7 + 4n = 2\,026 \iff n = 504{,}75$, qui n'est pas un entier : 2 026 n'est pas un terme.
- g) $h_n = 24 - 1{,}5\,n = 0 \iff n = 16$.

**Erreurs fréquentes.** Écrire $a_n = a_1 + n\,r$ pour une suite qui commence au rang 1 (c donne alors −15,5) ; s'arrêter à 5,8 en d (un rang est un entier) ; répondre 505 en e, en comptant le premier terme comme rang 1.

**Variante.** $b_1 = 3$ et raison 0,4 : $b_{21}$, et le rang $n$ tel que $b_n = 11$ ? *Réponse* : $b_{21} = 3 + 20 \times 0{,}4 = 11$, donc $n = 21$.

### Ex R5.3 — Terme général d'une suite géométrique

**Réponses** : a) `"5*3**n"` · b) `405` · c) `27` · d) `"729/64"` · e) `864` · f) `-486` · g) `8`.

**Démarche.**
- a) $v_n = 5 \times 3^n$ ; b) $v_4 = 5 \times 81 = 405$.
- c) $w_4 = 64 \times \left(\frac{3}{4}\right)^3 = 64 \times \frac{27}{64} = 27$ ; d) $w_7 = 64 \times \left(\frac{3}{4}\right)^6 = 64 \times \frac{729}{4\,096} = \frac{729}{64}$.
- e) $p_3 = 500 \times 1{,}2^3 = 500 \times 1{,}728 = 864$.
- f) $t_5 = 2 \times (-3)^5 = 2 \times (-243) = -486$ (puissance impaire : négatif).
- g) $p_7 = 500 \times 1{,}2^7 \approx 1\,792 < 2\,000$ et $p_8 \approx 2\,150 > 2\,000$ : $n = 8$.

**Erreurs fréquentes.** $3 \times 5^n$ ou $15^n$ au lieu de $5 \times 3^n$ ; la puissance $n$ au lieu de $n - 1$ pour une suite qui commence au rang 1 ; ajouter 100 bactéries par heure (hausse simple) au lieu de multiplier par 1,2.

**Variante.** Une voiture de 18 000 € perd 15 % de sa valeur chaque année : sa valeur au bout de 3 ans ? *Réponse* : $18\,000 \times 0{,}85^3 = 11\,054{,}25$ €.

### Ex R5.4 — Sommes arithmétiques et géométriques

**Réponses** : a) `16` · b) `440` · c) `135` · d) `1365` · e) `211` · f) `504` · g) `-341` · h) `"n**2 + 2*n"`.

**Démarche.**
- a) $\frac{50 - 5}{3} = 15$ écarts, donc 16 termes. b) $16 \times \frac{5 + 50}{2} = 440$.
- c) 20 termes, de $2$ à $2 + 0{,}5 \times 19 = 11{,}5$ : $20 \times \frac{2 + 11{,}5}{2} = 135$.
- d) Premier terme 1, raison 4, 6 termes : $\frac{4^6 - 1}{4 - 1} = \frac{4\,095}{3} = 1\,365$.
- e) Premier terme 81, raison $\frac{54}{81} = \frac{2}{3}$, 5 termes : $81 \times \frac{1 - (2/3)^5}{1 - 2/3} = 243 \times \left(1 - \frac{32}{243}\right) = 243 - 32 = 211$.
- f) Premier terme $2^3 = 8$, 6 termes : $8 \times \frac{2^6 - 1}{2 - 1} = 8 \times 63 = 504$.
- g) Premier terme 1, raison −2, 10 termes : $\frac{1 - (-2)^{10}}{1 - (-2)} = \frac{1 - 1\,024}{3} = -341$.
- h) $3n + 2 \times \frac{(n - 1)n}{2} = 3n + n^2 - n = n^2 + 2n$ ; ou $n \times \frac{3 + (2n + 1)}{2} = n(n + 2)$. Contrôle : pour $n = 3$, $3 + 5 + 7 = 15 = 9 + 6$.

**Erreurs fréquentes.** Compter 15 termes en a (les écarts, pas les termes) ; mettre l'exposant du dernier terme au lieu du nombre de termes (d, f, g) ; partir de 1 au lieu de $2^3$ en f ; se tromper de signe sur $(-2)^{10}$ ou sur $1 - (-2)$ en g.

**Variante.** $\sum_{k=1}^{6} 5 \times 3^{k-1}$ ? *Réponse* : premier terme 5, raison 3, 6 termes : $5 \times \frac{3^6 - 1}{2} = 1\,820$.

### Ex R5.5 — Sommes infinies d'une suite géométrique

**Réponses** : a) `4` · b) `"5/2"` · c) `"27/5"` · d) `"3/7"` · e) `False` · f) `13`.

**Démarche.**
- a) $\frac{1}{1 - 3/4} = 4$.
- b) Premier terme 2, raison $\frac{1}{5}$ : $\frac{2}{1 - 1/5} = \frac{2}{4/5} = \frac{5}{2}$.
- c) Premier terme 9, raison $-\frac{6}{9} = -\frac{2}{3}$ : $\frac{9}{1 + 2/3} = \frac{9}{5/3} = \frac{27}{5}$.
- d) Premier terme 0,3, raison 0,3 : $\frac{0{,}3}{0{,}7} = \frac{3}{7}$.
- e) **Faux** : la raison 1,1 est supérieure à 1, les sommes partielles tendent vers $+\infty$.
- f) L'écart vaut $\frac{0{,}75^n}{1 - 0{,}75} = 4 \times 0{,}75^n$ : $4 \times 0{,}75^{12} \approx 0{,}127$ et $4 \times 0{,}75^{13} \approx 0{,}095 < 0{,}1$, donc 13 termes.

**Erreurs fréquentes.** Prendre le deuxième terme pour la raison (b : $\frac{2}{5}$ au lieu de $\frac{1}{5}$) ; oublier le signe de la raison (c donne alors 27) ; utiliser $\frac{1}{1 - q}$ alors que la somme commence au rang 1 (d donne $\frac{10}{7}$) ; regarder $0{,}75^n < 0{,}1$ au lieu de l'écart (f donne 9).

**Variante.** $10 + 4 + 1{,}6 + 0{,}64 + \dots$ ? *Réponse* : premier terme 10, raison 0,4 : $\frac{10}{0{,}6} = \frac{50}{3}$.

### Ex R5.6 — Intérêts composés et actualisation

**Réponses** : a) `3075` · b) `3840.25` · c) `3750` · d) `12` · e) `4311.48` · f) `12.68` · g) `True`.

**Démarche.**
- a) $3\,000 \times 1{,}025 = 3\,075$ €.
- b) $3\,000 \times 1{,}025^{10} \approx 3\,000 \times 1{,}280085 \approx 3\,840{,}25$ €.
- c) $3\,000 + 10 \times 75 = 3\,750$ € : 90,25 € de moins qu'à intérêts composés.
- d) $C_{11} \approx 3\,936{,}26$ et $C_{12} \approx 4\,034{,}67$ : 12 années.
- e) $\frac{5\,000}{1{,}025^6} \approx \frac{5\,000}{1{,}159693} \approx 4\,311{,}48$ €.
- f) $1{,}01^{12} \approx 1{,}126825$ : une hausse de 12,68 % (et pas 12 %, car les intérêts de chaque mois rapportent à leur tour).
- g) **Vrai** : $\frac{1}{1{,}025^n} = \left(\frac{1}{1{,}025}\right)^n$, suite géométrique de raison comprise entre 0 et 1.

**Erreurs fréquentes.** Ajouter $10 \times 75$ en b (c'est l'intérêt simple de c) ; multiplier au lieu de diviser en e ; répondre 12 en f ; répondre 1,1268 en f (c'est le coefficient, pas le pourcentage).

**Variante.** Que vaut aujourd'hui une somme de 10 000 € reçue dans 20 ans, au taux de 3 % par an ? *Réponse* : $\frac{10\,000}{1{,}03^{20}} \approx 5\,536{,}76$ €.

### Ex R5.7 — Une moyenne exponentielle à la main sur cinq valeurs

**Réponses** : a) `[2, 5.6, 7.48, 6.984, 10.5872]` · b) `[15, 13.33, 15]` · c) `15` · d) `True` · e) `0.128` · f) `25`.

**Démarche.**
- a) $v_1 = 0{,}2 \times 10 = 2$ ; $v_2 = 0{,}8 \times 2 + 0{,}2 \times 20 = 5{,}6$ ; $v_3 = 4{,}48 + 3 = 7{,}48$ ; $v_4 = 5{,}984 + 1 = 6{,}984$ ; $v_5 = 5{,}5872 + 5 = 10{,}5872$.
- b) $\frac{10 + 20 + 15}{3} = 15$, $\frac{20 + 15 + 5}{3} \approx 13{,}33$, $\frac{15 + 5 + 25}{3} = 15$.
- c) $\frac{75}{5} = 15$. d) **Vrai** : $10{,}59 < 15$.
- e) $v_3 = 0{,}2\,x_3 + 0{,}8 \times 0{,}2\,x_2 + 0{,}8^2 \times 0{,}2\,x_1$ : le poids de $x_1$ est $0{,}64 \times 0{,}2 = 0{,}128$.
- f) Avec 0 et 1, $v_t = x_t$ : $v_5 = 25$.

Dans ta copie : les premières valeurs sont petites parce que $v_0 = 0$ et que $\beta = 0{,}8$ garde 80 % de cette valeur nulle à chaque pas ; la somme des poids des valeurs déjà vues est encore loin de 1 (à $t = 1$, seulement 0,2).

**Erreurs fréquentes.** Échanger 0,8 et 0,2 ; partir de $v_0 = x_1$ ; donner quatre moyennes mobiles au lieu de trois ($5 - 3 + 1 = 3$) ; oublier le facteur 0,2 dans le poids de e.

**Variante.** Même série, $\beta = 0{,}5$ : $v_3$ ? *Réponse* : $v_1 = 5$, $v_2 = 12{,}5$, $v_3 = 13{,}75$.

### Ex R5.8 — Retrouver le premier terme et la raison à partir de deux termes

**Réponses** : a) `4` · b) `1` · c) `-2` · d) `-6` · e) `0.8` · f) `62.5` · g) `["-2/3", "2/3"]` (ou `[-0.666667, 0.666667]`, dans n'importe quel ordre).

**Démarche.**
- a) $u_{10} - u_4 = 6r = 24$, donc $r = 4$ ; b) $u_0 = u_4 - 4r = 17 - 16 = 1$.
- c) $\frac{v_4}{v_1} = q^3 = \frac{-96}{12} = -8$, donc $q = -2$ ; d) $v_0 = \frac{v_1}{q} = \frac{12}{-2} = -6$.
- e) $q^2 = \frac{32}{50} = 0{,}64$, et les termes sont positifs : $q = 0{,}8$ ; f) $w_0 = \frac{50}{0{,}8} = 62{,}5$.
- g) $q^2 = \frac{8}{18} = \frac{4}{9}$ : $q = \frac{2}{3}$ ou $q = -\frac{2}{3}$, les deux conviennent ($s_3 = \pm 12$).

**Erreurs fréquentes.** Diviser par 10 au lieu de 6 en a ; oublier que la racine cubique d'un négatif est négative (c) ; multiplier au lieu de diviser pour revenir à $v_0$ ; ne garder que la racine positive en g.

**Variante.** $(u_n)$ géométrique, $u_2 = 3$ et $u_5 = 81$ : $q$ et $u_0$ ? *Réponse* : $q^3 = 27$, $q = 3$, $u_0 = \frac{3}{9} = \frac{1}{3}$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R5.9 — La somme d'une suite géométrique, démontrée par récurrence

**Démonstration.**
1. $P(1)$ : « $1 = \frac{1 - q}{1 - q}$ », vraie. $P(2)$ : « $1 + q = \frac{1 - q^2}{1 - q}$ », vraie car $1 - q^2 = (1 - q)(1 + q)$.
2. *Initialisation.* Pour $n = 1$, la somme n'a qu'un terme, $q^0 = 1$, et $\frac{1 - q^1}{1 - q} = 1$ (car $q \ne 1$) : $P(1)$ est vraie.
3. *Hérédité.* Soit $n \ge 1$ tel que $P(n)$ est vraie. En isolant le dernier terme, puis en utilisant $P(n)$ :
$$\sum_{k=0}^{n} q^k = \sum_{k=0}^{n-1} q^k + q^n = \frac{1 - q^n}{1 - q} + \frac{q^n(1 - q)}{1 - q} = \frac{1 - q^n + q^n - q^{n+1}}{1 - q} = \frac{1 - q^{n+1}}{1 - q}.$$
C'est $P(n + 1)$.
4. *Conclusion.* $P(1)$ est vraie et, pour tout $n \ge 1$, $P(n) \Rightarrow P(n + 1)$ : par récurrence, $P(n)$ est vraie pour tout $n \ge 1$. ∎
5. Par linéarité, $\sum_{k=0}^{n-1} u_0\,q^k = u_0 \sum_{k=0}^{n-1} q^k = u_0\,\frac{1 - q^n}{1 - q}$. Et avec $j = k - m$ : $\sum_{k=m}^{m+n-1} q^k = \sum_{j=0}^{n-1} q^{m+j} = q^m\,\frac{1 - q^n}{1 - q}$ : premier terme $q^m$, $n$ termes, comme dans la règle de la fiche.
6. Pour $q = 1$, on divise par $1 - q = 0$ : la formule n'a pas de sens, et l'initialisation comme l'hérédité tombent. Tous les termes valent $1^k = 1$, et la somme de $n$ termes vaut $n$.

**Grille de relecture.**
- $q \ne 1$ est dit, et sert (on divise par $1 - q$).
- L'initialisation calcule les **deux** membres en $n = 1$.
- L'hérédité isole le dernier terme $q^n$, dit où $P(n)$ sert, réduit au même dénominateur et aboutit exactement à $\frac{1 - q^{n+1}}{1 - q}$.
- La conclusion cite le principe de récurrence.
- En 5, le facteur $u_0$ ou $q^m$ sort par linéarité ; en 6, la division par zéro est nommée.

**Erreurs fréquentes.** Isoler $q^{n+1}$ au lieu de $q^n$ (le dernier terme de $\sum_{k=0}^{n}$ est $q^n$) ; supposer $P(n)$ « pour tout $n$ » ; oublier de réduire au même dénominateur.

**Variante.** Démontre de même, par récurrence, que $\sum_{k=1}^{n} 2^k = 2^{n+1} - 2$ pour tout $n \ge 1$. *Réponse* : initialisation $2 = 4 - 2$ ; hérédité $2^{n+1} - 2 + 2^{n+1} = 2^{n+2} - 2$.

### Ex R5.10 — La somme d'une suite arithmétique : l'astuce de Gauss

**Démonstration.**
1. Chaque colonne vaut $1 + 100 = 2 + 99 = \dots = 101$, et il y a 100 colonnes : $2S = 100 \times 101 = 10\,100$, donc $S = 5\,050$.
2. $u_k = u_0 + k\,r$ et $u_{n-1-k} = u_0 + (n - 1 - k)\,r$, donc $u_k + u_{n-1-k} = 2u_0 + (n - 1)\,r = u_0 + \big(u_0 + (n - 1)\,r\big) = u_0 + u_{n-1}$.
3. On écrit $S = u_0 + u_1 + \dots + u_{n-1}$ et $S = u_{n-1} + u_{n-2} + \dots + u_0$. La colonne $k$ contient $u_k + u_{n-1-k}$, qui vaut $u_0 + u_{n-1}$ d'après 2 ; il y a $n$ colonnes : $2S = n(u_0 + u_{n-1})$, d'où $S = n \times \frac{u_0 + u_{n-1}}{2}$. ∎
4. Premier terme 1, dernier $2n - 1$, $n$ termes : $n \times \frac{1 + 2n - 1}{2} = n^2$. Vérification : $1 = 1$, $1 + 3 = 4$, $1 + 3 + 5 = 9$, $1 + 3 + 5 + 7 = 16$.
5. Réponse libre. Par exemple : celle de Gauss montre pourquoi on prend la moyenne du premier et du dernier ; celle de la fiche n'utilise que des règles déjà connues (linéarité, somme des entiers).

**Grille de relecture.**
- En 2, les deux termes sont écrits avec $u_0$ et $r$, et le calcul montre que $k$ disparaît.
- En 3, les deux écritures de $S$ sont alignées, le nombre de colonnes ($n$) est justifié, et l'on divise par 2 à la fin.
- En 4, le dernier terme $2n - 1$ et le nombre de termes $n$ sont justifiés.

**Erreurs fréquentes.** Compter 101 colonnes ou 50 colonnes en 1 ; écrire $u_{n-k}$ au lieu de $u_{n-1-k}$ (le dernier terme est $u_{n-1}$) ; oublier de diviser par 2.

**Variante.** La somme des multiples de 3 de 3 à 300 ? *Réponse* : 100 termes, $100 \times \frac{3 + 300}{2} = 15\,150$.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R5.11 — Actualiser : ce que vaut aujourd'hui une somme versée chaque année

**Réponses** : a) `961.54` · b) `0.9615` · c) `6732.74` · d) `1` · e) `6209.79`.

**Démarche.**
- a) $\frac{1\,000}{1{,}04} \approx 961{,}54$ €.
- b) Le versement de l'année $k$ vaut aujourd'hui $\frac{1\,000}{1{,}04^k}$ : chaque année de plus multiplie par $\frac{1}{1{,}04} \approx 0{,}9615$.
- c) Premier terme $\frac{1\,000}{1{,}04}$, raison $q = \frac{1}{1{,}04}$, 8 termes : $\frac{1\,000}{1{,}04} \times \frac{1 - q^8}{1 - q} = 1\,000 \times \frac{1 - 1{,}04^{-8}}{0{,}04} \approx 6\,732{,}74$ €.
- d) $7\,000 > 6\,732{,}74$ : les 7 000 € tout de suite valent plus.
- e) Le même calcul avec 1,06 : $\approx 6\,209{,}79$ € (un taux plus élevé rend l'argent futur moins précieux).

Dans ta copie : $\gamma$ joue le rôle de $\frac{1}{1{,}04}$, le facteur qui multiplie la valeur d'une somme à chaque année d'attente. Un $\gamma$ proche de 0 : l'agent ne compte presque que la récompense immédiate (il est « impatient ») ; un $\gamma$ proche de 1 : il donne presque autant de poids aux récompenses lointaines qu'aux proches.

**Erreurs fréquentes.** Additionner les 8 000 € sans actualiser ; actualiser le premier versement d'une puissance 0 (il arrive dans un an) ; multiplier par $1{,}04^k$ (c'est la valeur **future** d'un placement, pas la valeur actuelle).

**Variante.** 500 € à la fin de chaque année pendant 3 ans, au taux de 5 % : la valeur actuelle ? *Réponse* : $\frac{500}{1{,}05} + \frac{500}{1{,}05^2} + \frac{500}{1{,}05^3} \approx 1\,361{,}62$ €.

### Ex R5.12 — Une moyenne mobile qui glisse : la mettre à jour sans tout recalculer

**Réponses** : a) `13.5` · b) `15.75` · c) `1` · d) `17.25` · e) `[99, 2]` · f) `16.5`.

**Démarche.**
- a) $\frac{12 + 18 + 15 + 9}{4} = \frac{54}{4} = 13{,}5$ ; b) $\frac{18 + 15 + 9 + 21}{4} = 15{,}75$.
- c) $m_{t+1} - m_t = \frac{(x_{t-2} + x_{t-1} + x_t + x_{t+1}) - (x_{t-3} + x_{t-2} + x_{t-1} + x_t)}{4} = \frac{x_{t+1} - x_{t-3}}{4}$ : la formule 1.
- d) $m_6 = m_5 + \frac{x_6 - x_2}{4} = 15{,}75 + \frac{24 - 18}{4} = 17{,}25$.
- e) Au minimum 99 additions pour additionner 100 nombres (on part du premier, pas de 0) ; une soustraction et une addition pour la mise à jour (et une division dans les deux cas, qu'on ne compte pas).
- f) $m_7 = 17{,}25 + \frac{6 - 15}{4} = 15$, puis $m_8 = 15 + \frac{15 - 9}{4} = 16{,}5$.

Dans ta copie : chaque nouvelle mesure coûte deux opérations au lieu de $k$, quelle que soit la largeur de la fenêtre ; il faut quand même garder en mémoire les $k$ dernières valeurs, pour savoir laquelle sort. (Et, sur des millions de mises à jour, les arrondis des flottants s'accumulent : on recalcule de temps en temps la moyenne en entier.)

**Erreurs fréquentes.** Retirer $x_t$ au lieu de la plus ancienne valeur ; oublier de diviser la différence par 4 ; compter 100 additions.

**Variante.** Fenêtre de 3 sur 4, 10, 7, 13 : $m_3$, puis $m_4$ par la mise à jour ? *Réponse* : $m_3 = 7$, $m_4 = 7 + \frac{13 - 4}{3} = 10$.

### Ex R5.13 — Expliquer pourquoi une somme infinie peut être finie

**Exemple de réponse.**

> Non ! Une randonneuse marche 10 km le premier jour, puis chaque jour 80 % de la distance de la veille : 10, puis 8, puis 6,4… Elle marche une infinité de jours, mais ses distances totales (les sommes partielles) valent 10 ; 18 ; 24,4 ; 29,52… et se rapprochent de 50 km sans jamais les dépasser : la somme infinie, c'est cette limite, $\frac{10}{1 - 0{,}8} = 50$. Ça marche parce que chaque étape est une part fixe de la précédente (ici 80 %) : ce qui reste à parcourir jusqu'à 50 km fond aussi vite que les étapes. Si les étapes étaient toutes égales, ou de plus en plus longues, le total grandirait sans fin. Attention : il ne suffit pas que les étapes deviennent minuscules. $1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dots$ finit par dépasser n'importe quel nombre, très lentement.

**Grille.** Une bonne réponse : (1) un exemple concret de somme infinie finie ; (2) les sommes partielles et leur limite ; (3) la raison (une part fixe, plus petite que 1, du terme précédent), opposée à des termes constants ou croissants ; (4) le piège $1 + \frac{1}{2} + \frac{1}{3} + \dots$ ; (5) huit lignes au plus.

<a id="notebook"></a>

## Notebook

### Ex R5.14 — Terme d'une suite arithmétique et somme géométrique · `arithmetic_term`, `geometric_sum`

**Réponses** : a) `[80, -2.0]` · b) `62.34375` · c) `[35.0, 0]` · d) `8.0` (à $10^{-24}$ près).

**Démarche.** `arithmetic_term` tient en une ligne : `return u0 + n * r`. `geometric_sum` traite d'abord `q == 1` (`float(n * u0)`), puis applique `u0 * (1 - q**n) / (1 - q)`, qui donne bien 0 pour `n = 0`.

**Erreurs fréquentes.** `(n - 1) * r` (le rang 0 est `u0`) ; `q**(n - 1)` ou `q**(n + 1)` dans la somme ; oublier le cas `q == 1` (division par zéro) ; rendre `u0` pour une somme vide.

### Ex R5.15 — Itérer une récurrence · `iterate`

**Réponses** : a) `[0, 10.0, 5.0, 7.5, 6.25]` · b) `11` · c) `[-3]` · d) `1.618` ($\frac{144}{89} \approx 1{,}6180$).

**Démarche.** `terms = [u0]`, puis `for _ in range(n): terms.append(f(terms[-1]))`, et `return terms`. Pour la copie : si $u_k \to \ell$, alors $\ell = 1 + \frac{1}{\ell}$, soit $\ell^2 - \ell - 1 = 0$ ; la solution positive est $\frac{1 + \sqrt{5}}{2} \approx 1{,}618$, le nombre d'or, très proche de d).

**Erreurs fréquentes.** Oublier `u0` dans la liste ; `range(n + 1)` (un terme de trop) ; appliquer `f` à `u0` à chaque tour (`f(u0)`) au lieu du dernier terme.

### Ex R5.16 — Moyennes mobile et exponentielle · `moving_average`, `exponential_moving_average`

**Réponses** : a) `[6.0, 8.0, 6.0, 8.0]` · b) `44` · c) `"ValueError"` · d) `"ValueError"` · e) `[10.0, 7.5, 10.625, 12.96875]` · f) `[3.0, 1.0, 4.0]` · g) `"ValueError"`.

**Démarche.** `moving_average` : `if not 1 <= window <= len(values): raise ValueError(...)`, puis une moyenne par position de départ, de 0 à `len(values) - window` inclus. `exponential_moving_average` : la `ValueError` si `not 0 <= beta < 1`, puis `v = 0.0` et, pour chaque valeur, `v = beta * v + (1 - beta) * x`, ajouté à la liste.

**Erreurs fréquentes.** `range(len(values) - window)` (la dernière moyenne manque) ; diviser par `len(values)` ; tester la fenêtre après le calcul (une fenêtre de 0 donne une division par zéro) ; partir de `v = values[0]` ; échanger `beta` et `1 - beta`.

### Ex R5.17 — Les mêmes calculs avec NumPy : `np.cumsum`, `np.cumprod`, `np.convolve`

**Réponses** : a) `[4, 11, 21, 34, 50, 69, 91, 116, 144, 175]` · b) `[5, 11, 18.2, 26.84, 37.208, 49.6496]` · c) `[1020, 1071, 1038.87, 1080.42]` · d) `[6, 5, 6, 10, 6, 4.5]`.

**Démarche.** a) `np.cumsum(4 + 3 * np.arange(10))` ; b) `np.cumsum(5 * 1.2 ** np.arange(6))` ; c) `1000 * np.cumprod(1 + rates)` ; d) `np.convolve(x, np.ones(2) / 2, mode="valid")`. Pour la copie : le coefficient change chaque année (1,02 ; 1,05 ; 0,97 ; 1,04), il n'y a pas de raison commune.

**Erreurs fréquentes.** Cumuler les $3k$ seuls, puis ajouter 4 une fois ; `np.cumprod(rates)` (des taux, pas des coefficients) ; `mode="full"`, qui ajoute les positions où la fenêtre déborde.

### Ex R5.18 — Prédire : vers quoi tend u(n + 1) = 0,75 u(n) + 2 ?

**Réponses** : a) `8` · b) `8` · c) `2` · d) `24`.

**Démarche.** Le point fixe vérifie $\ell = 0{,}75\,\ell + 2$, soit $0{,}25\,\ell = 2$ et $\ell = 8$. L'écart au point fixe est multiplié par 0,75 à chaque pas : $u_n = 8 + (u_0 - 8) \times 0{,}75^n$, et la limite est 8 quel que soit $u_0$. Depuis 0, l'écart vaut $8 \times 0{,}75^n$ ; il passe sous 0,01 quand $0{,}75^n < 0{,}00125$ : $0{,}75^{23} \approx 0{,}0013$ et $0{,}75^{24} \approx 0{,}0010$, donc 24 pas, entre 10 et 50.

**Erreurs fréquentes.** Prédire 2 (le nombre ajouté) ou $u_0$ ; croire que la limite dépend du point de départ ; sous-estimer la lenteur d'un facteur 0,75 ($0{,}75^{10} \approx 0{,}056$ seulement).

### Ex R5.19 — Lisser un signal bruité : l'effet de la fenêtre et de β

**Réponses** : a) environ `[1.621, 1.036, 0.834, 1.776, 3.430]` · b) environ `[1.621, 1.011, 0.796, 1.262, 3.135]` · c) `9` · d) `0.75` · e) `2`.

**Démarche.** `window_errors = [error(moving(x, k)) for k in windows]` et de même pour `betas`. L'erreur commence par baisser (le lissage enlève du bruit), puis remonte : une grande fenêtre moyenne des valeurs trop anciennes, la courbe lissée est en retard d'environ la moitié de la fenêtre et aplatit les sommets. Le meilleur réglage est un compromis entre bruit et retard.

**Erreurs fréquentes.** Choisir la plus grande fenêtre (« plus on lisse, mieux c'est ») ; croire que la courbe lissée anticipe la tendance (elle n'utilise que des valeurs passées).

### Ex R5.20 — Des suites qui convergent, divergent, oscillent

**Réponses** : a) `"ab"` · b) `[5, 2]` · c) `[-1, 1]`.

**Démarche.** `ns = np.arange(31)` et une ligne par suite, tracée en points. (a) converge vers 5 en restant en dessous ($4 \times 0{,}7^n > 0$) ; (b) converge vers 2 en oscillant autour ; (c) n'a pas de limite : ses termes pairs s'approchent de 1, ses termes impairs de −1 ; (d) tend vers $+\infty$, lentement ($\sqrt{30} \approx 5{,}5$).

**Erreurs fréquentes.** Relier les points par des lignes, qui suggèrent des valeurs entre les entiers (une suite n'est définie qu'aux entiers) ; écrire `(-1) ** ns` avec des entiers et `ns / (ns + 1)` (ça marche, mais `(-1.0) ** ns` évite les surprises avec des puissances négatives) ; prendre (c) pour une suite convergente parce que $\frac{n}{n + 1} \to 1$.

### Ex R5.21 — Chasse à l'erreur : un décalage d'indice dans une somme

**Réponses** : a) `"CG"` · b) `9` · c) `[5204.0402, 5204.0402]`.

**Démarche.** (C) `range(1, years)` fait `years − 1` tours et saute le dépôt de rang 0 : il faut `range(years)`. (G) la formule a `years` termes, donc `q**years`. Après correction, les deux fonctions donnent $1\,000 \times \frac{1{,}02^5 - 1}{0{,}02} \approx 5\,204{,}04$.

**Erreurs fréquentes.** Accuser la ligne (D) (elle est juste si la boucle part de 0) ; corriger (C) en `range(1, years + 1)` sans corriger (D) (on additionne alors les dépôts de rang 1 à `years`).

### Ex R5.22 — Une boucle ou une formule ? Mesurer le temps de calcul

**Exemple de résultats** (ils varient d'une machine à l'autre) : la boucle passe de 0,0001 s pour $n = 10^3$ à environ 0,05 s pour $n = 10^6$ ; la formule reste autour de quelques microsecondes. L'écart entre les deux résultats est de l'ordre de $10^{-11}$ à $10^{-8}$.

**Réponses attendues dans la copie.** 1. Le temps de la boucle est (à peu près) multiplié par 10 quand $n$ l'est ; celui de la formule ne change presque pas. 2. Non : les arrondis des flottants ne tombent pas au même endroit (une addition de $n$ termes accumule $n$ petits arrondis). 3. L'ordinateur fait d'autres choses en même temps, et les premières exécutions sont souvent plus lentes : on répète la mesure (`timeit`) et l'on garde l'ordre de grandeur.
