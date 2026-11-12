# Cheatsheet SymPy : vérifier un calcul à la main

SymPy fait du **calcul symbolique** : il manipule les expressions exactement, comme sur une feuille. Dans ce workbook, il **vérifie** tes calculs ; il ne les fait pas à ta place.

```python
import sympy as sp

x, y = sp.symbols("x y")                 # des symboles (variables)
a = sp.Symbol("a", positive=True)        # avec une hypothèse (utile pour simplifier racines et logs)
```

| Je veux… | Code | Résultat |
|---|---|---|
| un nombre exact | `sp.Rational(1, 3)`, `sp.sqrt(8)`, `sp.pi`, `sp.E` | $\frac{1}{3}$, $2\sqrt{2}$, $\pi$, $e$ |
| une valeur décimale | `sp.N(sp.pi, 10)` ou `expr.evalf()` | `3.141592654` |
| développer | `sp.expand((x + 1)**2)` | $x^2 + 2x + 1$ |
| factoriser | `sp.factor(x**2 - 1)` | $(x - 1)(x + 1)$ |
| simplifier | `sp.simplify(expr)` | une forme plus simple |
| vérifier une égalité | `sp.simplify(gauche - droite) == 0` | `True` si elles sont égales |
| remplacer une variable | `expr.subs(x, 2)` | la valeur en $x = 2$ |
| résoudre une équation | `sp.solve(x**2 - 4, x)` | `[-2, 2]` |
| résoudre une inéquation | `sp.solve_univariate_inequality(x**2 <= 4, x, relational=False)` | `Interval(-2, 2)` |
| dériver | `sp.diff(x**3, x)`, `sp.diff(f, x, 2)` (dérivée seconde) | $3x^2$ |
| dérivée partielle | `sp.diff(x * y**2, y)` | $2xy$ |
| limite | `sp.limit(sp.sin(x) / x, x, 0)` | `1` |
| intégrer | `sp.integrate(x**2, x)`, `sp.integrate(x**2, (x, 0, 1))` | $\frac{x^3}{3}$, $\frac{1}{3}$ |
| une somme | `sp.summation(1 / 2**sp.Symbol("k"), (sp.Symbol("k"), 0, sp.oo))` | `2` |
| un développement de Taylor | `sp.series(sp.exp(x), x, 0, 4)` | $1 + x + \frac{x^2}{2} + \frac{x^3}{6} + O(x^4)$ |
| une matrice | `M = sp.Matrix([[1, 2], [3, 4]])` ; `M.det()`, `M.inv()`, `M.eigenvals()` | calcul exact |
| valeurs et vecteurs propres exacts | `M.charpoly(lam)`, `M.eigenvects()`, `P, D = M.diagonalize()`, `M.is_diagonalizable()` | `eigenvects()` rend des triplets (valeur, multiplicité, base de l'espace propre) ; réservé aux petites matrices |
| une jacobienne exacte (M17) | `F = sp.Matrix([r * sp.cos(t), r * sp.sin(t)])` ; `J = F.jacobian([r, t])` ; `sp.simplify(J.det())` | la matrice des dérivées partielles, une ligne par sortie ; ici le déterminant $r$ |
| évaluer une matrice en un point | `np.array(J.subs({r: 2, t: 0}).evalf(), dtype=float)` | un tableau NumPy de flottants |
| écrire en LaTeX | `sp.latex(expr)` | le code LaTeX de l'expression |

> ⚠️ **Piège classique — `1/3` en Python** — `x + 1/3` donne `x + 0.333333333333333` : Python divise avant SymPy. Écris `x + sp.Rational(1, 3)`, ou `sp.S(1) / 3`.

> ⚠️ **Piège classique — `^` n'est pas la puissance** — en Python, la puissance s'écrit `**` (`x**2`). `wbm.check` accepte `^` dans une réponse tapée entre guillemets, mais pas SymPy dans du code.
