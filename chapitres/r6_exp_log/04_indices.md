# R6 · Exponentielle et logarithmes — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R6.Q1 — Propriétés de l'exponentielle : vrai ou faux

<details><summary>Indice 1</summary>

Relis « Ses propriétés : celles des puissances » (fiche §1) et « La fonction exponentielle » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Multiplier deux puissances de même base additionne les exposants ; une puissance de puissance les multiplie ; une exponentielle est toujours strictement positive.

</details>
<details><summary>Indice 3</summary>

1 : $e^{a} e^{b} = e^{a+b}$, **vrai**. Pour 2, $(e^{a})^{b}$ : additionne-t-on ou multiplie-t-on ? Pour 5, une exponentielle peut-elle valoir 0 ?

</details>

### R6.Q2 — ln d'un produit, d'un quotient, d'une puissance

<details><summary>Indice 1</summary>

Relis « Des produits aux sommes » et son encadré ⚠️ (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\ln$ transforme un produit en somme et une puissance en multiplication. Une somme, un carré de logarithme ou un quotient de logarithmes ne se simplifient pas.

</details>
<details><summary>Indice 3</summary>

1 : $6 = 2 \times 3$, donc **vrai**. Pour 5, compare $(\ln a)^{2}$ et $\ln(a^{2})$ avec $a = e$. Pour 7, regarde la courbe de ln entre 0 et 1.

</details>

### R6.Q3 — Combien de bits ?

<details><summary>Indice 1</summary>

Relis « Combien de questions oui ou non ? Les bits » (fiche §4).

</details>
<details><summary>Indice 2</summary>

$k$ réponses oui ou non distinguent $2^{k}$ possibilités ; un événement de probabilité $p$ apporte $-\log_{2} p$ bits ; 1 bit ≈ 0,693 nat.

</details>
<details><summary>Indice 3</summary>

1 : $2^{4} = 16$, donc 4 questions. Pour 2, cherche la plus petite puissance de 2 au-dessus d'un million. Pour 6, une quantité en bits multipliée par 0,693 donne des nats.

</details>

### R6.Q4 — Qui grandit le plus vite ?

<details><summary>Indice 1</summary>

Relis l'encadré « Croissances comparées » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Pour $x$ très grand : un logarithme est plus lent que toute puissance, une exponentielle de base plus grande que 1 plus rapide que toute puissance.

</details>
<details><summary>Indice 3</summary>

1 : $1{,}01^{x}$, une exponentielle, finit par gagner. Pour 6, calcule les deux nombres en $x = 10$ : « finir par » ne dit rien des petites valeurs.

</details>

### R6.Q5 — Lire une échelle logarithmique

<details><summary>Indice 1</summary>

Relis « Des écarts égaux pour des rapports égaux » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Un nombre $x$ est placé à la position $\log_{10} x$ ; une décade est un facteur 10.

</details>
<details><summary>Indice 3</summary>

1 : chaque intervalle est un facteur 10, donc **oui**. Pour 2, calcule $\log_{10} 3$. Pour 5, relis « Une exponentielle devient une droite ».

</details>

### R6.Q6 — Sigmoïde : valeurs remarquables et symétrie

<details><summary>Indice 1</summary>

Relis « La sigmoïde » et « La tangente hyperbolique » (fiche §7).

</details>
<details><summary>Indice 2</summary>

$\sigma(0) = \frac{1}{2}$, $0 < \sigma(x) < 1$, $\sigma(-x) = 1 - \sigma(x)$ ; tanh est impaire, entre −1 et 1.

</details>
<details><summary>Indice 3</summary>

1 : $\frac{1}{1 + e^{0}} = \frac{1}{2}$. Pour 3, utilise la symétrie. Pour 4, σ est croissante : compare $\sigma(x)$ à $\sigma(0)$.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### R6.R1 — Suites géométriques (R5)

<details><summary>Indice 1</summary>

Relis le terme général d'une suite géométrique (fiche de R5, §3).

</details>
<details><summary>Indice 2</summary>

$u_{n} = u_{0}\,q^{n}$ ; des multiplications successives se composent en une puissance.

</details>
<details><summary>Indice 3</summary>

1 : $u_{6} = 5 \times 2^{6}$. Pour 3, calcule $1{,}5^{4}$, $1{,}5^{5}$, $1{,}5^{6}$.

</details>

### R6.R2 — Fonction réciproque (R3)

<details><summary>Indice 1</summary>

Relis le §8 de la fiche de R3, « Fonction réciproque ».

</details>
<details><summary>Indice 2</summary>

Pour trouver $f^{-1}(y)$, résous $f(x) = y$ en $x$. Les courbes de $f$ et $f^{-1}$ sont symétriques par rapport à une droite.

</details>
<details><summary>Indice 3</summary>

1 : $2x + 3 = y \iff x = \frac{y - 3}{2}$. Pour 4, $f^{-1}$ défait ce que $f$ a fait.

</details>

### R6.R3 — Notation scientifique (R1)

<details><summary>Indice 1</summary>

Relis « Notation scientifique » (fiche de R1, §6).

</details>
<details><summary>Indice 2</summary>

$a \times 10^{k}$ avec $1 \le a < 10$ ; on multiplie les mantisses et on additionne les exposants.

</details>
<details><summary>Indice 3</summary>

1 : $0{,}00042 = 4{,}2 \times 10^{-4}$. Pour 3, écris $10^{12}$ en entier : un 1 suivi de combien de zéros ?

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R6.1 — Simplifier avec les propriétés de exp

<details><summary>Indice 1</summary>

Relis « Ses propriétés : celles des puissances » (fiche §1) et les exemples du §2.

</details>
<details><summary>Indice 2</summary>

Produit : on additionne les exposants ; quotient : on les soustrait ; puissance de puissance : on les multiplie. $a^{p/q}$ : la racine $q$-ième, puis la puissance $p$.

</details>
<details><summary>Indice 3</summary>

a : $4 + (-1{,}5) = 2{,}5$. Pour e, la racine cubique de 8 est 2. Pour g, $(e^{x})^{3} = e^{3x}$, puis soustrais tout l'exposant $x - 2$.

</details>

### Ex R6.2 — Simplifier avec les propriétés de ln

<details><summary>Indice 1</summary>

Relis « La réciproque de l'exponentielle » et « Des produits aux sommes » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$\ln(e^{y}) = y$, $e^{\ln x} = x$ ; $\ln a + \ln b = \ln(ab)$, $k \ln a = \ln(a^{k})$. Pour g et h, décompose le nombre en produit de puissances de 2 et de 3.

</details>
<details><summary>Indice 3</summary>

a : $5 - 2 = 3$. Pour c, $2 \ln 3 = \ln 9$. Pour h, $0{,}75 = \frac{3}{4} = \frac{3}{2^{2}}$.

</details>

### Ex R6.3 — Équations et inéquations avec exp et ln

<details><summary>Indice 1</summary>

Relis « Résoudre des équations et des inéquations » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Isole l'exponentielle, puis prends ln (ou isole ln, puis prends exp). Pour $a^{n} > c$, prends ln des deux membres, et change le sens si tu divises par un nombre négatif. Pense au domaine de ln.

</details>
<details><summary>Indice 3</summary>

a : $x = \ln 15$. Pour f, $\ln 0{,}85 < 0$. Pour g, il faut $x - 1 > 0$ et $x - 1 \le 1$. Pour h, $X^{2} - 5X + 6 = 0$ a deux racines positives.

</details>

### Ex R6.4 — Changer de base : log₂, log₁₀, ln

<details><summary>Indice 1</summary>

Relis « Le logarithme en base b » et « Changer de base » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Cherche d'abord un exposant entier ($b^{y} = x$) ; sinon, $\log_{b} x = \frac{\ln x}{\ln b}$. Le nombre de chiffres de $N$ est $\lfloor \log_{10} N \rfloor + 1$.

</details>
<details><summary>Indice 3</summary>

a : $2^{9} = 512$. Pour e, $\frac{\ln 30}{\ln 5}$. Pour h, écris 4 et 8 comme des puissances de 2.

</details>

### Ex R6.5 — Compter en bits et en nats : combien de questions oui ou non ?

<details><summary>Indice 1</summary>

Relis « Combien de questions oui ou non ? Les bits » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Questions : le plus petit $k$ tel que $2^{k} \ge N$. Information : $-\log_{2} p$ bits, ou $-\ln p$ nats ; les informations d'événements indépendants s'additionnent ; bits × ln 2 = nats.

</details>
<details><summary>Indice 3</summary>

a : $2^{8} = 256 < 300 \le 2^{9}$. Pour d, multiplie par $\ln 2$. Pour g, $-\ln p = 3$.

</details>

### Ex R6.6 — Temps de doublement et demi-vie

<details><summary>Indice 1</summary>

Relis « Temps de doublement et demi-vie » (fiche §3) et « La croissance exponentielle » (fiche §1).

</details>
<details><summary>Indice 2</summary>

Doublement : $(1 + r)^{n} = 2$ ; demi-vie : $(1 - r)^{n} = \frac{1}{2}$ ; un facteur $m$ par heure, si 5 heures doublent, vérifie $m^{5} = 2$.

</details>
<details><summary>Indice 3</summary>

a : $\frac{\ln 2}{\ln 1{,}03}$. Pour d, $m = 2^{1/5}$. Pour g, combien de demi-vies tiennent dans 24 heures ?

</details>

### Ex R6.7 — Sigmoïde et logit : la symétrie σ(−x) = 1 − σ(x), la cote et la log-cote

<details><summary>Indice 1</summary>

Relis le §7, de « La sigmoïde » à « La cote, le logit ».

</details>
<details><summary>Indice 2</summary>

$e^{-\ln 3} = \frac{1}{3}$ ; $\sigma(-x) = 1 - \sigma(x)$ ; cote $\frac{p}{1 - p}$, logit $\ln \frac{p}{1 - p}$ ; ajouter $\ln k$ au logit multiplie la cote par $k$.

</details>
<details><summary>Indice 3</summary>

a : $\sigma(\ln 3) = \frac{1}{1 + \frac{1}{3}}$. Pour g, le logit de 0,2. Pour h, la cote de 0,2 est $\frac{1}{4}$ : multiplie-la par 6, puis repasse en probabilité.

</details>

### Ex R6.8 — Placer des valeurs sur une échelle logarithmique

<details><summary>Indice 1</summary>

Relis « Des écarts égaux pour des rapports égaux » (fiche §6).

</details>
<details><summary>Indice 2</summary>

Position (en cm) = 5 × $\log_{10}$ (valeur) ; valeur = $10^{\text{position} / 5}$.

</details>
<details><summary>Indice 3</summary>

a : $5 \times \log_{10} 100 = 10$ cm. Pour d, $7{,}5$ cm font 1,5 décade. Pour e, 3 cm font 0,6 décade.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R6.9 — Démontrer ln(ab) = ln a + ln b à partir de exp

<details><summary>Indice 1</summary>

Relis la définition de ln (fiche §3) : « l'unique réel $y$ tel que $e^{y} = x$ ».

</details>
<details><summary>Indice 2</summary>

Montre que le nombre $\ln a + \ln b$ a la propriété qui définit $\ln(ab)$ : son exponentielle vaut $ab$. L'unicité fait le reste.

</details>
<details><summary>Indice 3</summary>

$e^{\ln a + \ln b} = e^{\ln a} \times e^{\ln b} = a b$ : donc $\ln a + \ln b$ est un réel dont l'exponentielle vaut $ab$. Pour 4, l'hérédité écrit $a^{n+1} = a^{n} \times a$.

</details>

### Ex R6.10 — tanh(x) = 2σ(2x) − 1

<details><summary>Indice 1</summary>

Relis les définitions de σ et de tanh (fiche §7).

</details>
<details><summary>Indice 2</summary>

$2\sigma(2x) - 1 = \frac{2}{1 + e^{-2x}} - 1$ : réduis au même dénominateur, puis multiplie en haut et en bas par $e^{x}$.

</details>
<details><summary>Indice 3</summary>

$\frac{2 - (1 + e^{-2x})}{1 + e^{-2x}} = \frac{1 - e^{-2x}}{1 + e^{-2x}}$ ; et $e^{x} \times e^{-2x} = e^{-x}$. Pour 3, écris $\tanh(-x) = 2\sigma(-2x) - 1$ et utilise la symétrie.

</details>

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R6.11 — Des produits de probabilités aux sommes de logarithmes

<details><summary>Indice 1</summary>

Relis « Les log-probabilités » (fiche §3) et les limites des flottants (fiche §5).

</details>
<details><summary>Indice 2</summary>

Vraisemblance : un produit ; log-vraisemblance : la somme des logarithmes ; pour f, $\log_{10}(0{,}4^{1000}) = 1000 \log_{10} 0{,}4$.

</details>
<details><summary>Indice 3</summary>

a : $0{,}9 \times 0{,}6 \times 0{,}3 \times 0{,}8 \times 0{,}5$. Pour d, $0{,}7^{5}$. Pour g, compare f à l'exposant du plus petit flottant positif.

</details>

### Ex R6.12 — Des logarithmes au travail : TF-IDF et PSNR

<details><summary>Indice 1</summary>

Relis l'énoncé (les deux formules), puis « Les décibels » (fiche §6).

</details>
<details><summary>Indice 2</summary>

idf $= \ln \frac{2000}{\mathrm{df}}$ ; tf-idf $=$ tf × idf ; PSNR $= 10 \log_{10} \frac{255^{2}}{\mathrm{MSE}}$. Diviser la MSE par 2 multiplie le rapport par 2.

</details>
<details><summary>Indice 3</summary>

a : $\ln 1 = 0$. Pour e, $\frac{255^{2}}{65{,}025} = 1\,000$. Pour g, résous $10 \log_{10} R = 40$, puis $\mathrm{MSE} = \frac{255^{2}}{R}$.

</details>

### Ex R6.13 — Expliquer ce que compte un logarithme : des chiffres, des doublements, des bits

<details><summary>Indice 1</summary>

Relis les débuts du §3 et du §4.

</details>
<details><summary>Indice 2</summary>

Pars de la question « à quelle puissance faut-il élever 10 (ou 2) pour obtenir ce nombre ? », puis donne un exemple pour chaque usage.

</details>
<details><summary>Indice 3</summary>

Par exemple : $\log_{10} 1\,000 = 3$ (trois zéros) ; $\log_{2} 4\,096 = 12$ (douze doublements depuis 1, ou douze questions oui ou non pour trouver un nombre parmi 4 096).

</details>

<a id="notebook"></a>

## Notebook

### Ex R6.14 — Un logarithme dans n'importe quelle base · `log_base`

<details><summary>Indice 1</summary>

Relis « Changer de base » (fiche §4).

</details>
<details><summary>Indice 2</summary>

D'abord les vérifications (`x <= 0`, puis `base <= 0 or base == 1`), chacune avec `raise ValueError(...)` ; puis une ligne : le quotient de deux `math.log`.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
if x <= 0:
    raise ValueError("...")
if base <= 0 or base == 1:
    raise ValueError("...")
return ...
```

</details>

### Ex R6.15 — Sigmoïde et tanh à partir de exp · `sigmoid`, `tanh`

<details><summary>Indice 1</summary>

Relis les définitions de σ et de tanh (fiche §7), et R6.10.

</details>
<details><summary>Indice 2</summary>

`sigmoid` : une ligne avec `math.exp(-x)`. `tanh` : soit la formule avec $e^{x}$ et $e^{-x}$, soit la relation $\tanh x = 2\sigma(2x) - 1$ avec ta sigmoïde.

</details>
<details><summary>Indice 3</summary>

`sigmoid` : `return 1 / (1 + math.exp(-x))`. Pour `tanh`, calcule d'abord `a = math.exp(x)` et `b = math.exp(-x)`, puis le quotient.

</details>

### Ex R6.16 — Temps de doublement · `doubling_time`

<details><summary>Indice 1</summary>

Relis « Temps de doublement et demi-vie » (fiche §3).

</details>
<details><summary>Indice 2</summary>

La `ValueError` si `rate <= 0`, puis $n = \frac{\ln 2}{\ln(1 + \text{rate})}$, sans arrondi.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
if rate <= 0:
    raise ValueError("...")
return math.log(2) / ...
```

</details>

### Ex R6.17 — Sur tout un tableau : `np.exp`, `np.log2` et `scipy.special.expit`

<details><summary>Indice 1</summary>

Relis l'énoncé : chaque fonction y est nommée.

</details>
<details><summary>Indice 2</summary>

Chaque réponse est un appel de fonction sur le tableau entier, sans boucle. Pour b, le nombre de chiffres vient de $\log_{10}$ (fiche §4).

</details>
<details><summary>Indice 3</summary>

a : `np.log2(values_a)`. Pour b, `np.floor(np.log10(values_b)) + 1`. Pour d, `np.logspace(-4, 0, 5)`.

</details>

### Ex R6.18 — Prédire : exp(800) avec math et NumPy, et le produit de 600 probabilités de 0,25

<details><summary>Indice 1</summary>

Relis les limites des flottants (fiche §5) et « Les log-probabilités » (fiche §3).

</details>
<details><summary>Indice 2</summary>

Pour chaque calcul, demande-toi d'abord si le résultat existe en flottant ; puis, s'il n'existe pas, si l'outil préfère s'arrêter ou continuer avec une valeur spéciale.

</details>
<details><summary>Indice 3</summary>

Pour d, calcule $\ln 0{,}25$ : est-ce un nombre ordinaire ? Et 600 fois ce nombre ?

</details>

### Ex R6.19 — Croissances comparées : x¹⁰, 2ˣ et ln x de plus en plus loin

<details><summary>Indice 1</summary>

Relis « Qui gagne à la fin ? » (fiche §5).

</details>
<details><summary>Indice 2</summary>

`gap` et `race` s'écrivent chacun en une ligne de NumPy (`np.log` sur tout le tableau). Pour a, compte les éléments où `gap <= 0` ; pour b, le premier `n` après le dernier où `gap <= 0`.

</details>
<details><summary>Indice 3</summary>

`gap = n * math.log(2) - 10 * np.log(n)`. Pour a, `(gap <= 0).sum()`. Pour e, $\ln k > 15 \iff k > e^{15}$.

</details>

### Ex R6.20 — Les mêmes données en échelle linéaire et en échelle logarithmique

<details><summary>Indice 1</summary>

Relis « Une exponentielle devient une droite » (fiche §6), et le tracé de R3.

</details>
<details><summary>Indice 2</summary>

Un `axes[k].plot(steps, counts, "o")` par axe, `axes[1].set_yscale("log")`, un titre par axe. Pour a, la pente d'une droite semi-logarithmique est $\log_{10}$ du facteur par pas.

</details>
<details><summary>Indice 3</summary>

Squelette :
```python
axes[0].plot(steps, counts, "o")
axes[0].set_title("...")
axes[1].plot(steps, counts, "o")
axes[1].set_yscale("log")
```

</details>

### Ex R6.21 — Chasse à l'erreur : ln(a + b), e^(a + b) et log(0)

<details><summary>Indice 1</summary>

Relis l'encadré ⚠️ « Le logarithme d'une somme ne se simplifie pas » (fiche §3) et les propriétés de exp (fiche §2).

</details>
<details><summary>Indice 2</summary>

Teste chaque fonction à la main sur un cas simple : `total_log_prob([1.0])`, `log_of_sum(1, 1)`, `grow(1, 1, 1, 1)`. Compare avec la valeur exacte.

</details>
<details><summary>Indice 3</summary>

`total_log_prob([1.0])` devrait rendre $\ln 1 = 0$ : que rend le code ? Pour b, exécute `math.log(0)` seul et lis le nom de l'erreur.

</details>

### Ex R6.22 — Lire la documentation de `numpy.log`, `log2`, `log10`, `log1p`

<details><summary>Indice 1</summary>

Relis le §3 et le §4, puis la documentation affichée par la cellule.

</details>
<details><summary>Indice 2</summary>

Compare `np.log(1 + 1e-12)` et `np.log1p(1e-12)` à la valeur attendue, $\approx 10^{-12}$ ; puis calcule `1 + 1e-12 - 1` pour voir ce qu'il reste de `1e-12`.

</details>
<details><summary>Indice 3</summary>

Pour la question 2, entoure les appels de `with np.errstate(all="ignore"):` pour faire taire les alertes, et lis les valeurs rendues.

</details>
