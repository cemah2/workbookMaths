# R0 · Prise en main — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [✏️ Papier-crayon](#papier) · [🗣️ 🛠️ Réflexion et outils](#reflexion) · [Notebook, parties A et B](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R0.Q1 — Le notebook : cellules, ordre d'exécution, « Run all »
1. **Faux** : tu écris dans ta copie, dans `mon_travail/r0_prise_en_main/`. Les fichiers de `chapitres/` sont réécrits à chaque mise à jour du dépôt.
2. **Vrai** : elle prépare le dépôt, les bibliothèques et `wbm` ; sans elle, les autres cellules ne connaissent pas `wbm`.
3. **Faux** : ⏳ veut dire « pas encore fait » (la réponse vaut encore `...`, ou la fonction lève encore `NotImplementedError`). Une vraie erreur s'affiche normalement, avec son message.
4. **Vrai** : le noyau repart d'une mémoire vide et exécute les cellules de haut en bas, dans l'ordre de la page.
5. **Faux** : on calcule d'abord sur papier ; le notebook ne fait que vérifier. Taper d'abord, c'est laisser l'ordinateur chercher à ta place.

### R0.Q2 — Python calculatrice : `**` ou `^`, `//` ou `%`
1. `8`, un `int`.
2. `1`, un `int` : `^` est le « ou exclusif » sur les bits ($2 = 10_2$, $3 = 11_2$, et le ou exclusif donne $01_2 = 1$). Retiens surtout que ce n'est pas la puissance.
3. `6`, un `int` : $20 = 3 \times 6 + 2$.
4. `2`, un `int` : c'est le reste de la même division.
5. `5.0`, un `float` : `/` donne toujours un flottant, même quand la division tombe juste.
6. `-4`, un `int` : $-7 / 2 = -3{,}5$, et `//` arrondit vers le bas, vers $-\infty$. Vérification : $-7 = 2 \times (-4) + 1$, avec un reste entre 0 et 1.

### R0.Q3 — Taper une réponse : fraction, expression, intervalle
1. **Non** : sans guillemets, Python calcule `1/3` en flottant, `0.3333333333333333`, une valeur approchée. `wbm.check` répond que c'est une valeur approchée et demande la fraction exacte.
2. **Oui** : entre guillemets, `"1/3"` est lu comme la fraction exacte.
3. **Oui** : dans une chaîne, `wbm.check` accepte `^` pour la puissance et la multiplication sous-entendue (`2x`). En **code** Python, `2x^2` serait faux deux fois.
4. **Non** : du côté de l'infini, le crochet est toujours ouvert : `"[0 ; +oo["`. Le message de `wbm.check` le dit.
5. **Oui** : la notation anglaise `(1, 4]` et la notation française `]1 ; 4]` désignent le même intervalle.

### R0.Q4 — SymPy et LaTeX : vrai ou faux
1. **Vrai.**
2. **Faux** : SymPy calcule exactement et renvoie `2*sqrt(2)`. La valeur approchée se demande avec `.evalf()`.
3. **Vrai** : si la différence se développe en 0, les deux expressions sont égales pour tout $x$.
4. **Faux** : sans accolades, seul le premier caractère monte en exposant ; on voit $x^10$. Il faut écrire `x^{10}`.
5. **Vrai.**

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R0.1 — Calculer avec Python : priorités, division entière et reste

**Réponses** : a) `23` · b) `63` · c) `-16` · d) `16` · e) `4` · f) `5` · g) `-5` · h) `1` · i) `4` · j) `5.0`.

**Démarche.**
- a) `**` d'abord : $3^2 = 9$ ; puis `*` : $2 \times 9 = 18$ ; puis `+` : $5 + 18 = 23$.
- b) les parenthèses d'abord : $5 + 2 = 7$ ; puis $3^2 = 9$ ; enfin $7 \times 9 = 63$.
- c) `**` passe avant le signe moins : `-4 ** 2` se lit $-(4^2) = -16$.
- d) avec les parenthèses, c'est $-4$ qui est élevé au carré : $(-4)^2 = 16$.
- e) et f) $29 = 6 \times 4 + 5$, avec $0 \le 5 < 6$ : le quotient vaut 4 et le reste 5.
- g) et h) $-29 / 6 \approx -4{,}83$ ; `//` arrondit vers le bas, donc $q = -5$. Le reste : $-29 = 6 \times (-5) + 1$, donc $r = 1$, bien entre 0 et 5. Avec $q = -4$, on aurait $r = -29 + 24 = -5$, négatif : interdit.
- i) les puissances se calculent de droite à gauche : `3 ** 0` d'abord, qui vaut 1, puis $4^1 = 4$. De gauche à droite, on aurait trouvé $(4^3)^0 = 1$.
- j) `/` et `*` ont la même priorité et se calculent de gauche à droite : $10 / 4 = 2{,}5$, puis $2{,}5 \times 2 = 5$, et `/` donne un flottant : `5.0`.

**Erreurs fréquentes.**
- Calculer $(5 + 2) \times 9$ en a) : l'addition passe **après** la multiplication.
- Répondre 16 en c) : c'est l'erreur la plus fréquente, en Python comme sur papier ($-4^2 = -16$ aussi en maths).
- Arrondir vers zéro en g) (réponse $-4$) : `//` arrondit vers $-\infty$.
- Donner un reste négatif en h) : avec un diviseur positif, le reste est toujours entre 0 et le diviseur moins 1.
- Calculer $10 / 8$ en j) : il n'y a pas de parenthèses autour de `4 * 2`.

**Variante.** Prévois `-2 ** 4`, `-17 // 4` et `-17 % 4`. *Réponses* : `-16` ; `-5` et `3`, car $-17 = 4 \times (-5) + 3$ avec $0 \le 3 < 4$.

<a id="reflexion"></a>

## 🗣️ 🛠️ Réflexion et outils

### Ex R0.2 — Expliquer à quoi sert `wbm.check`, et pourquoi il ne montre jamais la réponse

**Réponse modèle** (cinq lignes) :
> Le notebook ne connaît pas la bonne réponse : le dépôt ne garde que son **empreinte**, un long code calculé à partir d'elle, d'où l'on ne peut pas la retrouver (comme une empreinte digitale ne permet pas de reconstruire la personne). Quand tu tapes ta réponse, `wbm.check` calcule l'empreinte de **ta** réponse de la même façon et compare les deux codes : s'ils sont égaux, ta réponse est juste. Les messages d'erreur viennent des empreintes de quelques erreurs classiques, enregistrées avec la bonne réponse. Et ne pas afficher la réponse t'oblige à chercher : c'est en cherchant qu'on apprend.

**Ce qu'une bonne réponse contient** : l'empreinte (on ne stocke pas la réponse), la comparaison des empreintes, la raison pédagogique. Une réponse qui dit « la réponse est cachée dans un fichier » est fausse : elle n'y est pas.

**Nuance honnête** (pour aller plus loin) : pour une réponse très simple, comme un petit entier, on pourrait essayer toutes les valeurs une par une jusqu'à retrouver la bonne empreinte. L'empreinte est une protection pédagogique, pas un coffre-fort : la discipline reste la tienne.

**Variante.** Explique en deux lignes pourquoi `wbm.check` peut dire « le signe est faux » sans connaître la réponse. *Réponse* : avec la bonne réponse, on a aussi enregistré l'empreinte de son opposé ; si ta réponse a cette empreinte-là, c'est le signe qui est faux.

### Ex R0.8 — Écrire trois formules en LaTeX dans ta feuille de réponses

**Une écriture possible** :

```latex
$$\frac{a + b}{2}$$

$$\sum_{i=1}^{n} x_i^2$$

$$\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
```

**Démarche.** Chaque commande prend ses arguments entre accolades : `\frac{numérateur}{dénominateur}`, `\sum_{début}^{fin}`, `\sqrt{tout ce qui est sous la racine}`. Dans `x_i^2`, l'indice et l'exposant s'appliquent tous les deux à `x`. D'autres écritures sont justes : `\dfrac{a+b}{2}` (une fraction plus grande), `\left( x_2 - x_1 \right)^2` (des parenthèses qui s'adaptent), les espaces n'ont aucun effet.

**Erreurs fréquentes.**
- `\frac{a + b}2` marche par chance (un seul caractère), mais `\frac{a + b}{10}` demande des accolades : prends l'habitude de toujours en mettre.
- `x_i2` affiche $x_{i}2$ : l'exposant s'écrit `^`.
- Oublier les `$$` : le texte s'affiche tel quel, sans mise en forme.

**Variante.** Écris en LaTeX la moyenne $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$. *Réponse* : `$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$`.

<a id="notebook"></a>

## Notebook, parties A et B

### Ex R0.3 — Taper une fraction exacte, une expression et un intervalle

**Réponses** : a) `"7/12"` · b) `"(x + 3)**2 - 1"` (ou toute écriture équivalente, comme `"x**2 + 6*x + 8"`) · c) `"]-2 ; 5]"` · d) `"]-oo ; 0]"` · e) `3.142`.

**Démarche.**
- a) Au même dénominateur, 12 : $\frac{3}{4} = \frac{9}{12}$ et $\frac{1}{6} = \frac{2}{12}$, donc $\frac{9}{12} - \frac{2}{12} = \frac{7}{12}$, déjà irréductible (7 est premier et ne divise pas 12).
- b) « La somme de $x$ et de 3 » est $(x + 3)$ ; son carré est $(x + 3)^2$ ; « moins 1 » vient après : $(x + 3)^2 - 1$. `wbm.check` accepte toutes les écritures équivalentes : la forme développée $x^2 + 6x + 8$ passe aussi.
- c) « strictement supérieurs à $-2$ » : $-2$ est exclu, crochet ouvert `]-2` ; « inférieurs ou égaux à 5 » : 5 est inclus, crochet fermé `5]`.
- d) « négatifs ou nuls » : tous les nombres inférieurs ou égaux à 0 ; 0 est inclus (`0]`), et du côté de l'infini le crochet est ouvert (`]-oo`).
- e) $\pi = 3{,}14159\ldots$ ; la quatrième décimale est 5, donc la troisième monte : $3{,}142$.

**Erreurs fréquentes.**
- a) Soustraire « en haut et en bas » ; ou écrire $\frac{1}{6} = \frac{1}{12}$ en oubliant de multiplier le numérateur (on trouve alors $\frac{8}{12} = \frac{2}{3}$).
- b) Écrire `x + 3**2 - 1` : sans parenthèses, seul le 3 est élevé au carré.
- c) Inverser les crochets : `[-2 ; 5[`.
- e) Tronquer au lieu d'arrondir : $3{,}141$.

**Variante.** Tape $\frac{2}{3} - \frac{1}{5}$ et l'intervalle des réels supérieurs ou égaux à 1. *Réponses* : `"7/15"` (car $\frac{10}{15} - \frac{3}{15}$) et `"[1 ; +oo["`.

### Ex R0.4 — Prédire : 0,1 + 0,2 vaut-il 0,3 pour Python ?

**Réponses** : a) `False` · b) `-17` · c) `"3/10"`.

**Démarche.** `0.1 + 0.2` s'affiche `0.30000000000000004` : l'écart avec `0.3` vaut environ $5{,}55 \times 10^{-17}$, affiché `5.551115123125783e-17` ; la puissance de 10 est $-17$. Il vient de ce que 0,1 et 0,2 ne s'écrivent pas exactement en binaire : l'ordinateur garde les flottants les plus proches, et leur somme tombe sur le voisin du flottant appelé `0.3` (fiche §2, figure de la grille). `math.isclose` compare avec une tolérance et répond `True`. Avec `Fraction`, le calcul est exact : $\frac{1}{10} + \frac{2}{10} = \frac{3}{10}$.

**Erreurs fréquentes.**
- b) Répondre 17 : `e-17` veut dire « fois $10^{-17}$ », un nombre minuscule, pas énorme.
- Conclure que « Python calcule faux » : il calcule juste, sur des nombres légèrement différents de ceux qu'on a tapés. Toute calculatrice qui travaille en binaire fait de même.

**Variante.** Prédis `0.5 + 0.25 == 0.75`. *Réponse* : `True`, car 0,5, 0,25 et 0,75 s'écrivent exactement en binaire ($\frac{1}{2}$, $\frac{1}{4}$, $\frac{3}{4}$) : il n'y a aucun arrondi.

### Ex R0.5 — Vérifier un développement avec SymPy (expand, simplify)

**Réponses** : 1) `"ac"` · 2) `"9*x**2 - 12*x + 4"` · 3) `"x - 2"`.

**Démarche.** Pour chaque ligne, `sp.expand(depart - resultat)` :
- a) donne `0` : juste ;
- b) donne `8 - 12*x` : faux ; le bon développement est $(3x - 2)^2 = 9x^2 - 12x + 4$, avec le double produit $-2 \times 3x \times 2 = -12x$ que le camarade a oublié ;
- c) donne `0` : juste ;
- d) donne `16` : faux ; $(x + 2)(x^2 - 2x + 4) = x^3 + 8$, et non $x^3 - 8$.

Pour 3, `sp.simplify((x**2 - 4) / (x + 2))` donne `x - 2` : en effet $x^2 - 4 = (x - 2)(x + 2)$, et on simplifie par $x + 2$ (pour $x \ne -2$).

**Erreurs fréquentes.**
- Comparer avec `==` deux expressions écrites différemment : `(x + 3)*(x - 7) == x**2 - 4*x - 21` répond `False`, car `==` compare l'**écriture**, pas la valeur. C'est pour cela qu'on développe la différence.
- Tester avec une seule valeur de $x$ : pour $x = 0$, d) donne $8$ à gauche et $-8$ à droite (faux, bien vu), mais un test en un point peut aussi tomber juste par hasard.

**Variante.** Vérifie avec SymPy que $(x + 1)(x - 1)(x^2 + 1) = x^4 - 1$. *Réponse* : `sp.expand((x + 1)*(x - 1)*(x**2 + 1) - (x**4 - 1))` donne `0` : c'est juste.

### Ex R0.6 — Chasse à l'erreur : `x^2` et `2x` en Python

**Réponses** : 1) `"bcf"` · 2) `y3(2)` vaut `0.125`.

**Démarche.**
- (b) est fausse : `x^3` est un « ou exclusif » sur les bits, pas une puissance ; il faut `x**3`.
- (c) est fausse : `1/4*x` se calcule de gauche à droite, $(1/4) \times x$, c'est-à-dire $\frac{x}{4}$ ; pour $\frac{1}{4x}$, il faut `1/(4*x)`.
- (f) est fausse : `5x` est une erreur de syntaxe ; il faut `5*x + 1`.
- Les autres sont justes : (a) ; (d) ; (e), car `-x**2` vaut $-(x^2)$, exactement comme la formule $-x^2$ ; et (g), car `x**(1/2)` est la racine carrée, pour $x \ge 0$.

La fonction corrigée : `return 1 / (4 * x)`, et `y3(2)` vaut $\frac{1}{8} = 0{,}125$ (la ligne fausse donnait 0,5).

**Erreurs fréquentes.**
- Marquer (e) comme fausse : c'est le piège inverse de R0.1 c ; ici la formule voulue est bien $-(x^2)$.
- Marquer (g) comme fausse : `x**(1/2)` et `x**0.5` sont justes ; `math.sqrt(x)` aussi.
- Ne pas voir (c) : elle ne provoque aucune erreur, elle calcule autre chose. Ce sont les erreurs les plus dangereuses.

**Variante.** Que calcule `1/2/x` ? *Réponse* : $(1/2)/x = \frac{1}{2x}$ : de gauche à droite, on divise par 2 puis par $x$. C'est juste, mais `1/(2*x)` se lit mieux.

### Ex R0.7 — Tracer une fonction avec matplotlib

**La figure attendue :**

![La parabole de f(x) = x² − 2x − 3 sur [−2, 4] : elle coupe l'axe en −1 et 3, son point le plus bas est (1 ; −4)](figures/r0_7_parabole.png)

**Lectures** : la courbe coupe l'axe horizontal en $x = -1$ et $x = 3$ ; son point le plus bas est $(1 ; -4)$. Vérification par le calcul : $f(-1) = 1 + 2 - 3 = 0$, $f(3) = 9 - 6 - 3 = 0$, $f(1) = 1 - 2 - 3 = -4$. En R3, tu sauras trouver ces valeurs sans graphique.

**Démarche.** La recette de la fiche §6, avec `np.linspace(-2, 4, 200)`, `ys = xs**2 - 2*xs - 3`, puis `ax.axhline(0, linewidth=0.8)` pour l'axe. Le code complet est dans `05_solutions.ipynb`.

**Erreurs fréquentes.**
- Oublier `plt.show()` : dans certains environnements, la figure ne s'affiche pas.
- Écrire `xs^2` : erreur de type sur un tableau (et ce ne serait pas la puissance).
- Une figure sans titre ni noms d'axes : elle n'est pas fausse, mais elle n'est pas lisible par quelqu'un d'autre.

**Variante.** Trace aussi $g(x) = -f(x)$ sur la même figure (une seconde ligne `ax.plot`, avec sa propre légende). *Réponse* : c'est la même parabole retournée ; elle coupe l'axe aux mêmes points, et son point le plus haut est $(1 ; 4)$.

### Ex R0.9 — Ta première fonction : la moyenne (`mean`)

**Réponse** (une version possible ; la référence est dans `solutions/mymath_ref/_example.py`) :

```python
def mean(values):
    if len(values) == 0:
        raise ValueError("mean() of an empty sequence")
    return sum(values) / len(values)
```

`mean([2, 4, 9])` vaut `5.0`, et les cinq tests de `tests/test_example_mymath.py` passent. Deux `assert` possibles : `assert mymath._example.mean([10, 20]) == 15.0` et `assert mymath._example.mean([7]) == 7.0`.

**Démarche.** La docstring dit tout : la somme divisée par le nombre de valeurs, un `float`, et une `ValueError` pour une suite vide. `/` renvoie toujours un `float`, même pour `[2, 4]` (moyenne `3.0`). Les tests comparent la fonction à `np.mean` sur des données tirées au hasard, puis vérifient une seule valeur, le type `float` et la `ValueError`.

**Erreurs fréquentes.**
- `if not values:` : échoue sur un tableau NumPy (« *truth value of an array is ambiguous* »), et le test `test_mean_matches_numpy` le montre.
- Oublier d'enregistrer le fichier, ou de relancer la cellule qui recharge `mymath` : la vérification teste alors l'ancienne version.
- `return sum(values) // len(values)` : `//` donne un entier arrondi vers le bas ; `mean([2, 4, 9])` donnerait 5 par chance, mais `mean([1, 2])` donnerait 1 au lieu de 1,5.
- Un `assert` qui compare deux flottants calculés, comme `assert mean([0.1, 0.2]) == 0.15` : il peut échouer à cause des arrondis (fiche §2). Choisis des nombres dont la moyenne tombe juste, ou compare avec `math.isclose`.

**Variante.** Écris un troisième `assert` qui vérifie que multiplier toutes les valeurs par 10 multiplie la moyenne par 10, avec des nombres choisis pour que les calculs tombent juste. *Réponse* : `assert mymath._example.mean([10, 30]) == 10 * mymath._example.mean([1, 3])` (20,0 des deux côtés). Avec `[1, 4, 9]`, `==` échouerait : `mean([10, 40, 90])` donne `46.666666666666664` et `10 * mean([1, 4, 9])` donne `46.66666666666667`, à cause des arrondis des flottants (fiche §2) ; on compare alors avec `math.isclose`.
