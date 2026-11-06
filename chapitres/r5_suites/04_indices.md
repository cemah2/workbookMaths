# R5 · Suites — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R5.Q1 — Explicite ou par récurrence ?

<details><summary>Indice 1</summary>

Relis « Définition explicite » et « Définition par récurrence » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Explicite : une formule en $n$ donne le terme directement. Par récurrence : un premier terme et une règle qui part du terme précédent ; sans premier terme, pas de suite.

</details>
<details><summary>Indice 3</summary>

1 : la formule ne contient que $n$, la suite est **explicite**. Pour 3, remplace $n$ par 20. Pour 6, écris les quatre termes, puis compare chacun au précédent.

</details>

### R5.Q2 — Arithmétique, géométrique, ou ni l'une ni l'autre ?

<details><summary>Indice 1</summary>

Relis « Reconnaître une suite arithmétique » (fiche §2) et « Reconnaître une suite géométrique » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Calcule les différences entre termes consécutifs (constantes : arithmétique), puis les quotients (constants : géométrique).

</details>
<details><summary>Indice 3</summary>

1 : les différences valent toutes 5, la suite est **arithmétique** de raison 5. Pour 6, calcule les différences **et** les quotients. Pour 7, que fait-on pour passer de $u_n$ à $u_{n+1}$ ?

</details>

### R5.Q3 — Formules de somme : vrai ou faux

<details><summary>Indice 1</summary>

Relis le §4 de la fiche, et surtout « Écrire la somme et compter ses termes ».

</details>
<details><summary>Indice 2</summary>

Compte les termes avant tout. Dans la formule géométrique, l'exposant est le nombre de termes, et la formule demande $q \ne 1$.

</details>
<details><summary>Indice 3</summary>

1 : $100 \times \frac{1 + 100}{2} = 5\,050$, **vrai**. Pour 2, compte les rangs de 0 à $n$. Pour 7, quel est le premier terme de la somme, et combien y a-t-il de termes ?

</details>

### R5.Q4 — Converge ou diverge ?

<details><summary>Indice 1</summary>

Relis « Suites qui divergent » et le tableau des limites à connaître (fiche §5).

</details>
<details><summary>Indice 2</summary>

Pour $q^n$, tout dépend de $q$ : entre −1 et 1 (exclus), 0 ; au-dessus de 1, $+\infty$ ; à partir de −1 vers le bas, pas de limite.

</details>
<details><summary>Indice 3</summary>

1 : $0{,}8$ est entre −1 et 1, donc $0{,}8^n \to 0$. Pour 4, que devient $\frac{1}{n}$ ? Pour 6, factorise : $n^2 - 10n = n(n - 10)$. Pour 7, pense à $(-1)^n$.

</details>

### R5.Q5 — Moyenne mobile ou moyenne exponentielle ?

<details><summary>Indice 1</summary>

Relis « La moyenne mobile » et « La moyenne exponentielle » (fiche §6).

</details>
<details><summary>Indice 2</summary>

La moyenne mobile utilise une fenêtre de $k$ valeurs, toutes de même poids ; la moyenne exponentielle est une récurrence qui part de $v_0 = 0$.

</details>
<details><summary>Indice 3</summary>

1 : la moyenne exponentielle ($v_t$ ne dépend que de $v_{t-1}$ et de $x_t$). Pour 4, combien de positions une fenêtre de 4 peut-elle prendre dans 10 valeurs ? Pour 5, calcule $v_1$.

</details>

### R5.Q6 — Les poids d'une moyenne exponentielle

<details><summary>Indice 1</summary>

Relis « Ses poids forment une suite géométrique » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Développe $v_t$ en remplaçant $v_{t-1}$, puis $v_{t-2}$ : chaque pas en arrière multiplie le poids par 0,7.

</details>
<details><summary>Indice 3</summary>

1 : 0,3. Pour 2, développe $v_t = 0{,}3\,x_t + 0{,}7\,v_{t-1}$ et regarde avec quel poids $x_{t-1}$ entre dans $v_{t-1}$. Pour 6, que reste-t-il de $v_{t-1}$ ?

</details>

<a id="rappels"></a>

## 🔁 Rappels

### R5.R1 — Σ et changement d'indice (R4)

<details><summary>Indice 1</summary>

Relis « Lire une somme » et « Calculer avec Σ » (fiche de R4, §5).

</details>
<details><summary>Indice 2</summary>

De $m$ à $n$, il y a $n - m + 1$ termes. Dans un changement d'indice, les bornes bougent avec l'indice.

</details>
<details><summary>Indice 3</summary>

1 : $1 + 3 + 5 + 7$. Pour 3, quand $k$ va de 1 à 6, $j = k - 1$ va de … à … ? Pour 4, la formule $\frac{n(n+1)}{2}$.

</details>

### R5.R2 — Raisonnement par récurrence (R4)

<details><summary>Indice 1</summary>

Relis « La récurrence au service des suites » (fiche §1) et le §7 de R4.

</details>
<details><summary>Indice 2</summary>

Calcule les termes, compare-les aux puissances de 3 : il manque toujours le même nombre. Dans l'hérédité, remplace $u_n$ par la formule supposée.

</details>
<details><summary>Indice 3</summary>

1 : $u_1 = 3 \times 2 - 2 = 4$. Pour 3, dans l'hérédité, remplace $u_n$ par ta formule dans $3u_n - 2$, puis simplifie jusqu'à retrouver la formule au rang $n + 1$.

</details>

### R5.R3 — Évolutions successives (R1)

<details><summary>Indice 1</summary>

Relis les pourcentages et les coefficients multiplicateurs (fiche de R1).

</details>
<details><summary>Indice 2</summary>

Une hausse de $t\,\%$ multiplie par $1 + \frac{t}{100}$, une baisse par $1 - \frac{t}{100}$ ; des évolutions successives multiplient leurs coefficients.

</details>
<details><summary>Indice 3</summary>

1 : $80 \times 1{,}05 = 84$ €. Pour 3, calcule $1{,}1 \times 0{,}9$. Pour 4, calcule $1{,}2^3$.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R5.1 — Calculer des termes : explicite et récurrence

<details><summary>Indice 1</summary>

Relis le §1 de la fiche, en particulier « Sens de variation ».

</details>
<details><summary>Indice 2</summary>

Explicite : remplace $n$. Par récurrence : applique la règle pas à pas, en faisant attention à la valeur de $n$ dans la règle. Pour f, développe $(n + 1)^2 - 3(n + 1) + 1$, puis retire $u_n$.

</details>
<details><summary>Indice 3</summary>

a : $u_5 = 25 - 15 + 1 = 11$. Pour c, $v_1 = 2 \times 3 - 4$. Pour d, $w_2 = w_1 + 2 \times 1 + 1 = 4$ (on prend $n = 1$). Pour g, étudie le signe de la différence trouvée en f.

</details>

### Ex R5.2 — Terme général d'une suite arithmétique

<details><summary>Indice 1</summary>

Relis « On ajoute toujours le même nombre » (fiche §2).

</details>
<details><summary>Indice 2</summary>

$u_n = u_0 + n\,r$ ; pour une suite qui commence au rang 1, $a_n = a_1 + (n - 1)\,r$. Pour savoir si un nombre est un terme, résous l'équation en $n$ et regarde si $n$ est un entier positif.

</details>
<details><summary>Indice 3</summary>

a : $u_n = 7 + 4n$. Pour d, résous $12 - 2{,}5(n - 1) < 0$, puis prends le premier entier qui convient. Pour g, la hauteur après $n$ heures est $24 - 1{,}5\,n$.

</details>

### Ex R5.3 — Terme général d'une suite géométrique

<details><summary>Indice 1</summary>

Relis « On multiplie toujours par le même nombre » et « Pourcentages et intérêts composés » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$v_n = v_0\,q^n$ ; pour une suite qui commence au rang 1, $w_n = w_1\,q^{n-1}$. Une hausse de 20 % multiplie par 1,2.

</details>
<details><summary>Indice 3</summary>

a : $v_n = 5 \times 3^n$. Pour c, $w_4 = 64 \times \left(\frac{3}{4}\right)^3$. Pour g, calcule $500 \times 1{,}2^n$ pour $n = 6, 7, 8$.

</details>

### Ex R5.4 — Sommes arithmétiques et géométriques

<details><summary>Indice 1</summary>

Relis le §4 de la fiche.

</details>
<details><summary>Indice 2</summary>

Pour chaque somme : le premier terme, le nombre de termes (de $m$ à $n$ : $n - m + 1$), la raison, puis la formule. Pour une suite arithmétique, le nombre de termes est le nombre d'écarts plus 1.

</details>
<details><summary>Indice 3</summary>

a : $(50 - 5) / 3 = 15$ écarts, donc 16 termes. Pour f, le premier terme est $2^3 = 8$ et il y a $8 - 3 + 1$ termes. Pour h, le premier terme est 3, le dernier $3 + 2(n - 1)$.

</details>

### Ex R5.5 — Sommes infinies d'une suite géométrique

<details><summary>Indice 1</summary>

Relis « Somme infinie d'une suite géométrique » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Repère le premier terme et la raison (le quotient de deux termes consécutifs), vérifie $\lvert q \rvert < 1$, puis premier terme ÷ (1 − raison).

</details>
<details><summary>Indice 3</summary>

a : $\frac{1}{1 - 3/4} = 4$. Pour c, la raison est $-\frac{6}{9}$. Pour d, le premier terme est $0{,}3$. Pour f, l'écart vaut $4 \times 0{,}75^n$ : essaie quelques valeurs de $n$.

</details>

### Ex R5.6 — Intérêts composés et actualisation

<details><summary>Indice 1</summary>

Relis « Pourcentages et intérêts composés » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Intérêts composés : $C_n = 3\,000 \times 1{,}025^n$ ; simples : $3\,000 + 75\,n$. Actualiser, c'est diviser par $1{,}025^n$. Pour f, le coefficient annuel est $1{,}01^{12}$.

</details>
<details><summary>Indice 3</summary>

a : $3\,000 \times 1{,}025 = 3\,075$ €. Pour d, calcule $C_{11}$ et $C_{12}$. Pour e, résous $x \times 1{,}025^6 = 5\,000$.

</details>

### Ex R5.7 — Une moyenne exponentielle à la main sur cinq valeurs

<details><summary>Indice 1</summary>

Relis « La moyenne exponentielle » et « Ses poids forment une suite géométrique » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Applique la règle pas à pas, en partant de $v_0 = 0$ : $v_t = 0{,}8\,v_{t-1} + 0{,}2\,x_t$. Pour e, développe $v_3$ comme dans la fiche.

</details>
<details><summary>Indice 3</summary>

$v_1 = 0{,}8 \times 0 + 0{,}2 \times 10 = 2$, puis $v_2 = 0{,}8 \times 2 + 0{,}2 \times 20$. Pour b, la première fenêtre est $(10, 20, 15)$.

</details>

### Ex R5.8 — Retrouver le premier terme et la raison à partir de deux termes

<details><summary>Indice 1</summary>

Relis « Retrouver une suite à partir de deux termes » (fiche §2) et « Reconnaître une suite géométrique » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Arithmétique : la différence des deux termes vaut (écart de rang) × $r$. Géométrique : leur quotient vaut $q^{\text{écart de rang}}$. Puis on revient au rang 0.

</details>
<details><summary>Indice 3</summary>

a : $41 - 17 = 6r$. Pour c, $\frac{-96}{12} = q^3$. Pour g, $\frac{8}{18} = q^2$ : combien de solutions ?

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R5.9 — La somme d'une suite géométrique, démontrée par récurrence

<details><summary>Indice 1</summary>

Relis « Un exemple de somme » (fiche de R4, §7) : le geste est le même.

</details>
<details><summary>Indice 2</summary>

Dans l'hérédité, isole le dernier terme : $\sum_{k=0}^{n} q^k = \sum_{k=0}^{n-1} q^k + q^n$, remplace la première somme par $\frac{1 - q^n}{1 - q}$, puis écris $q^n = \frac{q^n(1 - q)}{1 - q}$.

</details>
<details><summary>Indice 3</summary>

$\frac{1 - q^n}{1 - q} + \frac{q^n - q^{n+1}}{1 - q} = \frac{1 - q^{n+1}}{1 - q}$ : c'est $P(n + 1)$. Pour 5, $\sum_{k=m}^{m+n-1} q^k = q^m \sum_{j=0}^{n-1} q^j$ (pose $j = k - m$).

</details>

### Ex R5.10 — La somme d'une suite arithmétique : l'astuce de Gauss

<details><summary>Indice 1</summary>

Relis la somme des premiers entiers (fiche de R4, §5) et la somme arithmétique (fiche §4).

</details>
<details><summary>Indice 2</summary>

Écris $u_k = u_0 + k\,r$ et $u_{n-1-k} = u_0 + (n - 1 - k)\,r$, puis additionne : les $k$ disparaissent.

</details>
<details><summary>Indice 3</summary>

Pour 1, chaque colonne vaut 101 : combien y a-t-il de colonnes ? Pour 3, que vaut chaque colonne, d'après 2 ? Pour 4, le premier terme est 1 et le dernier $2n - 1$.

</details>

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R5.11 — Actualiser : ce que vaut aujourd'hui une somme versée chaque année

<details><summary>Indice 1</summary>

Relis la fin de « Pourcentages et intérêts composés » (fiche §3) et la somme géométrique (fiche §4).

</details>
<details><summary>Indice 2</summary>

Le versement de l'année $k$ vaut aujourd'hui $\frac{1\,000}{1{,}04^k}$. Ces valeurs forment une suite géométrique : son premier terme (année 1), sa raison, son nombre de termes.

</details>
<details><summary>Indice 3</summary>

a : $\frac{1\,000}{1{,}04} \approx 961{,}54$. Pour c, le premier terme est la réponse de a, la raison celle de b, et il y a 8 termes. Pour e, refais c) avec 1,06.

</details>

### Ex R5.12 — Une moyenne mobile qui glisse : la mettre à jour sans tout recalculer

<details><summary>Indice 1</summary>

Relis « La moyenne mobile » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Écris $m_{t+1}$ et $m_t$ l'une sous l'autre, valeur par valeur : lesquelles apparaissent dans les deux ? Laquelle entre, laquelle sort ?

</details>
<details><summary>Indice 3</summary>

a : $\frac{12 + 18 + 15 + 9}{4}$. Pour d, la valeur qui entre est $x_6$, celle qui sort $x_2$. Pour e, combien d'additions pour additionner 100 nombres ?

</details>

### Ex R5.13 — Expliquer pourquoi une somme infinie peut être finie

<details><summary>Indice 1</summary>

Relis « Somme infinie d'une suite géométrique » et le dernier encadré ⚠️ du §5.

</details>
<details><summary>Indice 2</summary>

Prends un exemple concret (une distance parcourue par moitiés, une tablette partagée en parts de plus en plus petites) et écris quelques sommes partielles.

</details>
<details><summary>Indice 3</summary>

Avec $1 + \frac{1}{4} + \frac{1}{16} + \dots$ : les sommes partielles valent 1 ; 1,25 ; 1,3125 ; 1,328… et s'approchent de $\frac{4}{3}$ sans le dépasser. Pour le piège, pense à $1 + \frac{1}{2} + \frac{1}{3} + \dots$

</details>

<a id="notebook"></a>

## Notebook

### Ex R5.14 — Terme d'une suite arithmétique et somme géométrique · `arithmetic_term`, `geometric_sum`

<details><summary>Indice 1</summary>

Relis le terme général (fiche §2) et la somme géométrique (fiche §4).

</details>
<details><summary>Indice 2</summary>

`arithmetic_term` : une ligne, la formule $u_0 + n\,r$. `geometric_sum` : traite d'abord le cas `q == 1` (la somme vaut `n` fois `u0`), puis applique la formule ; `n` est le nombre de termes.

</details>
<details><summary>Indice 3</summary>

Squelette de `geometric_sum` :
```python
if q == 1:
    return float(...)
return u0 * (1 - q**n) / ...
```
Pour `n = 0`, la formule donne bien 0 : vérifie-le.

</details>

### Ex R5.15 — Itérer une récurrence · `iterate`

<details><summary>Indice 1</summary>

Relis « Définition par récurrence » et sa cellule Python (fiche §1).

</details>
<details><summary>Indice 2</summary>

Une liste qui commence par `u0`, puis une boucle de `n` tours qui ajoute `f(dernier terme)`. Le dernier terme d'une liste est `terms[-1]`.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
terms = [u0]
for _ in range(n):
    terms.append(...)
return terms
```
Pour la copie : si $u_k \to \ell$, alors $\ell = 1 + \frac{1}{\ell}$, soit $\ell^2 - \ell - 1 = 0$.

</details>

### Ex R5.16 — Moyennes mobile et exponentielle · `moving_average`, `exponential_moving_average`

<details><summary>Indice 1</summary>

Relis le §6 de la fiche, et tes calculs de R5.7 et R5.12.

</details>
<details><summary>Indice 2</summary>

`moving_average` : la `ValueError` d'abord, puis une moyenne par position de départ `start` de 0 à `len(values) - window`. `exponential_moving_average` : la `ValueError`, puis `v = 0.0` et une boucle sur les valeurs qui met `v` à jour et l'ajoute à la liste.

</details>
<details><summary>Indice 3</summary>

Squelette de `moving_average` :
```python
if not 1 <= window <= len(values):
    raise ValueError("...")
return [... for start in range(len(values) - window + 1)]
```
À la place des `...`, la moyenne de `values[start:start + window]`.
Pour la moyenne exponentielle, la ligne clé est `v = beta * v + (1 - beta) * x`.

</details>

### Ex R5.17 — Les mêmes calculs avec NumPy : `np.cumsum`, `np.cumprod`, `np.convolve`

<details><summary>Indice 1</summary>

Relis l'énoncé : chaque fonction y est montrée sur un petit exemple.

</details>
<details><summary>Indice 2</summary>

Fabrique d'abord les termes avec `np.arange` et le calcul vectorisé (`4 + 3 * np.arange(10)`, `5 * 1.2 ** np.arange(6)`), puis cumule-les. Pour c, les coefficients multiplicateurs sont `1 + rates`.

</details>
<details><summary>Indice 3</summary>

a : `np.cumsum(4 + 3 * np.arange(10))`. Pour c, multiplie 1 000 par les produits cumulés des coefficients. Pour d, `np.convolve(x, np.ones(2) / 2, mode="valid")`.

</details>

### Ex R5.18 — Prédire : vers quoi tend u(n + 1) = 0,75 u(n) + 2 ?

<details><summary>Indice 1</summary>

Relis « Une récurrence affine : $u_{n+1} = a\,u_n + b$ » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Deux questions à te poser : quelle est la solution de $\ell = 0{,}75\,\ell + 2$ ? Et par quoi l'écart à cette valeur est-il multiplié à chaque pas ?

</details>
<details><summary>Indice 3</summary>

Pour c, écris l'écart initial (il découle de ta prédiction a), puis calcule de proche en proche $0{,}75^2$, $0{,}75^4$, $0{,}75^8$… : combien de multiplications par 0,75 faut-il pour que l'écart passe sous 0,01 ?

</details>

### Ex R5.19 — Lisser un signal bruité : l'effet de la fenêtre et de β

<details><summary>Indice 1</summary>

Relis « La moyenne mobile » (sa troisième remarque) et « Le choix de β » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Une liste par compréhension suffit pour chacune : une erreur par fenêtre, une erreur par valeur de β, dans l'ordre des listes données.

</details>
<details><summary>Indice 3</summary>

a : `[error(moving(x, k)) for k in windows]`. Pour c et d, cherche la plus petite valeur de chaque liste (`np.argmin` donne son indice : `windows[np.argmin(window_errors)]` donne la fenêtre). Pour e, compare la position des sommets de la courbe rouge et de la courbe noire.

</details>

### Ex R5.20 — Des suites qui convergent, divergent, oscillent

<details><summary>Indice 1</summary>

Relis « Suites qui divergent » et le tableau des limites (fiche §5), puis le tracé de R3.

</details>
<details><summary>Indice 2</summary>

`ns = np.arange(31)`, puis chaque suite en une ligne de NumPy (`5 - 4 * 0.7**ns`…). Pour $(-1)^n$, écris `(-1.0) ** ns` (avec un flottant). Un `ax.plot(ns, values, "o")` par axe.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
ns = np.arange(31)
axes[0].plot(ns, 5 - 4 * 0.7**ns, "o")
axes[0].set_title("(a)")
```
Pour a et b, regarde chaque graphique : les points se stabilisent-ils près d'une valeur ?

</details>

### Ex R5.21 — Chasse à l'erreur : un décalage d'indice dans une somme

<details><summary>Indice 1</summary>

Relis l'encadré ⚠️ « Le nombre de termes, pas le dernier rang » (fiche §4) et les bornes d'un `range` (R4 §5).

</details>
<details><summary>Indice 2</summary>

Fais tourner les deux fonctions à la main avec `years = 1` : le total doit valoir `first`. Combien de tours fait `range(1, 1)` ? Que vaut $q^0$ dans la formule ?

</details>
<details><summary>Indice 3</summary>

Pour `years = 1`, la boucle ne fait aucun tour et rend 0 : la ligne (C) est fausse. Pour la formule, quel exposant faut-il pour `years` termes ?

</details>

### Ex R5.22 — Une boucle ou une formule ? Mesurer le temps de calcul

<details><summary>Indice 1</summary>

Relis le §4 (la fin, sur `sum` et la formule) et l'énoncé, qui montre `time.perf_counter()`.

</details>
<details><summary>Indice 2</summary>

Pour chaque `n` : un `start = time.perf_counter()`, l'appel, un second `time.perf_counter()`, et la différence. Fais de même pour la formule.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
for n in [10**3, 10**4, 10**5, 10**6]:
    start = time.perf_counter()
    by_loop = loop_sum(0.999999, n)
    middle = time.perf_counter()
    ...
```

</details>
