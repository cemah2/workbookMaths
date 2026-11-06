# R0 · Prise en main — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [✏️ Papier-crayon](#papier) · [🗣️ 🛠️ Réflexion et outils](#reflexion) · [Notebook, parties A et B](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R0.Q1 — Le notebook : cellules, ordre d'exécution, « Run all »

<details><summary>Indice 1</summary>

Relis la fiche §1 : « Où tu travailles », puis « La routine d'un exercice papier », puis « Exécuter un notebook ».

</details>
<details><summary>Indice 2</summary>

Pour 1 : quel dossier Claude ne touche-t-il jamais ? Pour 3 : ⏳ est-il une erreur ou un état ? Pour 5 : à quoi sert le notebook dans la routine, vérifier ou calculer ?

</details>
<details><summary>Indice 3</summary>

1 est **faux** : les fichiers de `chapitres/` sont réécrits par les mises à jour ; tu travailles dans ta copie, dans `mon_travail/`. Juge les autres avec la même question : « que dit la fiche, mot pour mot ? ». Pour 4, demande-toi avec quelle mémoire repart le noyau.

</details>

### R0.Q2 — Python calculatrice : `**` ou `^`, `//` ou `%`

<details><summary>Indice 1</summary>

Relis le tableau des opérateurs de la fiche §2, et les deux encadrés ⚠️ qui le suivent.

</details>
<details><summary>Indice 2</summary>

Quelle opération donne toujours un flottant ? Pour 6, `//` arrondit vers le bas, c'est-à-dire vers $-\infty$.

</details>
<details><summary>Indice 3</summary>

1 : `2 ** 3` vaut `8`, un `int` (une puissance d'entiers, à exposant positif ou nul, reste un entier). Pour 2, souviens-toi que `^` **n'est pas** la puissance ; la réponse est un entier, mais ce n'est pas 8. Pour 3 et 4, écris $20 = 3q + r$ avec $0 \le r < 3$. Pour 5, quel opérateur est utilisé ? Pour 6, $-9 / 2 = -4{,}5$ : quel est l'entier juste en dessous ?

</details>

### R0.Q3 — Taper une réponse : fraction, expression, intervalle

<details><summary>Indice 1</summary>

Relis la fiche §3, « Comment taper chaque sorte de réponse » : les paragraphes « Les fractions », « Les expressions » et « Les intervalles ».

</details>
<details><summary>Indice 2</summary>

Sans guillemets, Python **calcule** d'abord ce que tu tapes : que devient `1/3` ? Entre guillemets, `wbm.check` lit une expression avec indulgence. Pour l'infini, regarde le sens du crochet.

</details>
<details><summary>Indice 3</summary>

1 : **non**, car `1/3` est calculé en flottant, `0.3333333333333333`, une valeur approchée, alors que l'énoncé demande la fraction exacte. Pour 2, qu'est-ce qui change avec les guillemets ? Pour 3, `^` et la multiplication sous-entendue sont-ils acceptés **dans une chaîne** ? Pour 4, quel crochet met-on du côté de l'infini ? Pour 5, les deux notations sont-elles acceptées ?

</details>

### R0.Q4 — SymPy et LaTeX : vrai ou faux

<details><summary>Indice 1</summary>

Relis la fiche §4 (les exemples avec `>>>` et « Vérifier son propre calcul ») et l'encadré ⚠️ de la fiche §5.

</details>
<details><summary>Indice 2</summary>

SymPy calcule-t-il en valeurs exactes ou approchées ? En LaTeX, que fait l'exposant quand il a plusieurs caractères et pas d'accolades ?

</details>
<details><summary>Indice 3</summary>

1 est **vrai** : c'est exactement ce que fait `expand` (développer). Pour 2, regarde la ligne `sp.sqrt(8)` des exemples de la fiche. Pour 3, c'est la méthode « la différence se simplifie en 0 ». Pour 4, quel caractère monte en exposant sans accolades ? Pour 5, compare au tableau de la fiche §5.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R0.1 — Calculer avec Python : priorités, division entière et reste

<details><summary>Indice 1</summary>

Relis la fiche §2, « Les priorités » et « Division euclidienne avec des nombres négatifs ». L'ordre : parenthèses, puis `**` (avant le signe moins), puis `*`, `/`, `//`, `%` de gauche à droite, puis `+` et `-`.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, souligne l'opération qui passe en premier, calcule-la, et recommence. Pour e à h, écris la division euclidienne $a = 6q + r$ avec $0 \le r < 6$ : `//` donne $q$, `%` donne $r$. Pour i, les puissances se calculent de droite à gauche.

</details>
<details><summary>Indice 3</summary>

a : `3 ** 2` d'abord (9), puis `2 * 9` (18), puis `5 + 18` : **23**. b : les parenthèses d'abord, puis la puissance. c et d : la différence entre les deux est le signe moins, que `**` précède ou non. Pour g et h : $-29 = 6 \times q + r$ avec $0 \le r < 6$ ; essaie $q = -4$ (le reste serait négatif : interdit), puis $q = -5$. Pour i : que vaut `3 ** 0` ? Pour j : de gauche à droite, `12 / 8` d'abord.

</details>

<a id="reflexion"></a>

## 🗣️ 🛠️ Réflexion et outils

### Ex R0.2 — Expliquer à quoi sert `wbm.check`, et pourquoi il ne montre jamais la réponse

<details><summary>Indice 1</summary>

Relis la fiche §3, « Ce que fait `wbm.check` ».

</details>
<details><summary>Indice 2</summary>

Trouve une image de la vie courante pour l'empreinte : quelque chose qu'on peut comparer sans pouvoir revenir en arrière (une empreinte digitale ne permet pas de reconstruire la personne, mais permet de dire si c'est la même).

</details>
<details><summary>Indice 3</summary>

Une structure possible en trois idées : (1) le dépôt ne garde pas la réponse, seulement son empreinte, un code dont on ne peut pas la retrouver ; (2) `wbm.check` calcule l'empreinte de ta réponse et compare les deux codes ; (3) ne pas voir la réponse t'oblige à chercher, et c'est en cherchant qu'on apprend. Écris chaque idée avec tes mots, en une ou deux phrases.

</details>

### Ex R0.8 — Écrire trois formules en LaTeX dans ta feuille de réponses

<details><summary>Indice 1</summary>

Relis le tableau de la fiche §5 : il contient toutes les commandes dont tu as besoin.

</details>
<details><summary>Indice 2</summary>

Il te faut `\frac{...}{...}` pour 1, `\sum_{...}^{...}` et un indice avec un exposant pour 2, `\sqrt{...}` avec des parenthèses et des indices pour 3. N'oublie pas les accolades.

</details>
<details><summary>Indice 3</summary>

La première s'écrit `$$\frac{a + b}{2}$$`. Pour la deuxième, la somme commence comme `\sum_{i=1}^{n}` ; il reste à écrire $x_i^2$ (un indice **et** un exposant sur la même lettre : `x_i^2`). Pour la troisième, tout ce qui est sous la racine va entre les accolades de `\sqrt{...}`.

</details>

<a id="notebook"></a>

## Notebook, parties A et B

### Ex R0.3 — Taper une fraction exacte, une expression et un intervalle

<details><summary>Indice 1</summary>

Relis la fiche §3, le tableau « Comment taper chaque sorte de réponse ». Fais d'abord chaque calcul ou chaque traduction sur papier.

</details>
<details><summary>Indice 2</summary>

a : mets les deux fractions au même dénominateur (12), puis simplifie si possible. b : traduis la phrase de gauche à droite, avec des parenthèses autour de ce qui est élevé au carré. c et d : « strictement » exclut la borne, « ou égal » et « ou nul » l'incluent ; du côté de l'infini, le crochet est ouvert. e : arrondir, c'est regarder la décimale suivante.

</details>
<details><summary>Indice 3</summary>

a : $\frac{3}{4} = \frac{9}{12}$ et $\frac{1}{6} = \frac{2}{12}$ ; termine le calcul et tape le résultat entre guillemets, comme `"2/9"`. b : « la somme de $x$ et de 3 » s'écrit `(x + 3)` ; élève-la au carré, puis retire 1. c : une borne exclue s'écrit avec un crochet tourné vers l'extérieur, `]-2`. d : l'infini du côté des négatifs s'écrit `-oo`. e : $\pi = 3{,}14159\ldots$ : la quatrième décimale est 5.

</details>

### Ex R0.4 — Prédire : 0,5 + 0,25 et dix fois 0,1, exacts ou arrondis ?

<details><summary>Indice 1</summary>

Pour les prédictions, réfléchis seul : il n'y a pas d'indice qui les donne. Relis seulement la fiche §2, « Les flottants » : pourquoi 0,1 est-il arrondi ? Une prédiction ratée t'apprend souvent plus qu'une prédiction réussie.

</details>
<details><summary>Indice 2</summary>

Après l'expérience, pour c : un nombre affiché `3.2e-8` se lit $3{,}2 \times 10^{-8}$, et son exposant est $-8$. Pour d : regarde la dernière ligne affichée.

</details>
<details><summary>Indice 3</summary>

c : dans l'écriture `<m>e<k>`, l'entier demandé est ce qui suit le `e`, avec son signe ; pour un nombre plus petit que 1, il est négatif. d : `Fraction` calcule exactement ; réponds par `True` ou `False` selon la dernière ligne. Ensuite, relis la note de `05_solutions.md` : pourquoi 0,5 et 0,25 ne sont-ils pas arrondis ?

</details>

### Ex R0.5 — Vérifier un développement avec SymPy (expand, simplify)

<details><summary>Indice 1</summary>

Relis la fiche §4, « Vérifier son propre calcul » : on développe la différence entre le départ et le résultat.

</details>
<details><summary>Indice 2</summary>

Pour chaque ligne, une seule instruction suffit : `sp.expand(depart - resultat)`. Si le résultat vaut 0, la ligne est juste ; sinon, ce qui reste montre l'erreur. Pour b, `sp.expand(depart)` donne le bon développement : lis le nombre devant `x`. Pour c, `sp.simplify(...)`, puis lis $a$ et $b$ dans le résultat.

</details>
<details><summary>Indice 3</summary>

La ligne 1 se vérifie avec `sp.expand((x + 3)*(x - 7) - (x**2 - 4*x - 21))`, qui affiche `0` : la ligne 1 est juste. Fais de même pour les lignes 2, 3 et 4, en recopiant le départ et le résultat de chaque ligne du tableau. Pour a, mets les numéros des lignes justes dans une liste. Pour b, un terme `-5*x` aurait pour coefficient $-5$ (avec son signe). Pour c, un résultat comme `x + 7` se lit $a = 1$ et $b = 7$.

</details>

### Ex R0.6 — Chasse à l'erreur : `x^2` et `2x` en Python

<details><summary>Indice 1</summary>

Relis les deux encadrés ⚠️ de la fiche §2 et la ligne « une fraction en Python » du tableau des pièges.

</details>
<details><summary>Indice 2</summary>

Il y a trois sortes de pièges : un symbole qui n'est pas la puissance, une multiplication sous-entendue, et une fraction mal parenthésée. Pour chaque ligne, demande-toi : « Python lit-il la même chose que la formule ? ». Attention, certaines lignes ont l'air suspectes et sont justes.

</details>
<details><summary>Indice 3</summary>

La ligne 2 est fausse : `x^3` n'est pas une puissance en Python. Cherche maintenant les deux autres lignes fausses parmi les lignes 3, 5, 6 et 7 : pour chacune, calcule ce que Python fait avec `x = 2`, et compare à la formule avec $x = 2$. Pour `y3`, la fonction tient en une ligne : `return 1 / (...)`.

</details>

### Ex R0.7 — Tracer une fonction avec matplotlib

<details><summary>Indice 1</summary>

Recopie la recette de la fiche §6 dans le corps de `plot_f` (à la place du `raise`), puis adapte-la.

</details>
<details><summary>Indice 2</summary>

Trois choses changent par rapport à la recette : l'intervalle (`np.linspace(-5, 3, 200)`), la formule des ordonnées, et les textes (titre, légende). Ajoute `ax.axhline(0, linewidth=0.8)` avant `plt.show()`.

</details>
<details><summary>Indice 3</summary>

Le début de la fonction :

```python
xs = np.linspace(-5, 3, 200)
ys = xs**2 + 2*xs - 8
fig, ax = plt.subplots(figsize=(6, 3.6))
```

Ajoute ensuite `ax.plot(xs, ys, label=...)`, la ligne $y = 0$, le titre, les noms d'axes, le quadrillage et la légende, puis `plt.show()`. Pour les lectures, cherche où la courbe traverse la ligne $y = 0$, puis le bas de la cuvette.

</details>

### Ex R0.9 — Ta première fonction : la moyenne (`mean`)

<details><summary>Indice 1</summary>

Relis la docstring de `mean` dans `mon_travail/mymath/_example.py`, puis la fiche §7 et son encadré ⚠️. Deux cas : la suite est vide (on lève une erreur), ou non (on renvoie la moyenne).

</details>
<details><summary>Indice 2</summary>

Python a déjà `sum(values)` et `len(values)`. Pour le cas vide, la recette de la fiche : `raise ValueError("...")`. Le résultat doit être un `float` : la division `/` en donne toujours un. N'oublie pas d'**enregistrer** le fichier avant de relancer la cellule qui recharge `mymath`.

</details>
<details><summary>Indice 3</summary>

Le squelette, à compléter :

```python
def mean(values):
    if len(values) == 0:
        raise ValueError("cannot average an empty sequence")
    return ...
```

Pour `my_tests`, une ligne a la forme `assert mymath._example.mean([...]) == ...` (avec le nom complet : `mean` tout court provoque une `NameError` dans le notebook) : choisis deux nombres dont tu connais la moyenne de tête, puis une liste d'un seul nombre.

</details>
