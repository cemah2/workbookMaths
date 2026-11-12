# Cheatsheet matplotlib pour les maths

```python
import matplotlib.pyplot as plt
import numpy as np
```

| Je veux… | Code |
|---|---|
| tracer une fonction | `x = np.linspace(-3, 3, 300)` ; `fig, ax = plt.subplots()` ; `ax.plot(x, x**2, label="x²")` ; `ax.legend()` ; `plt.show()` |
| les axes passant par 0 | `ax.axhline(0, color="gray", lw=0.5)` ; `ax.axvline(0, color="gray", lw=0.5)` |
| un repère orthonormé (cercles ronds) | `ax.set_aspect("equal")` |
| des points | `ax.scatter(xs, ys)` |
| un vecteur (flèche) depuis l'origine | `ax.quiver(0, 0, vx, vy, angles="xy", scale_units="xy", scale=1)` |
| un histogramme de probabilités | `ax.hist(samples, bins=30, density=True)` (l'aire totale vaut 1) |
| des lignes de niveau | `X, Y = np.meshgrid(x, y)` ; `ax.contour(X, Y, X**2 + Y**2, levels=10)` |
| une surface 3D | `ax = plt.figure().add_subplot(projection="3d")` ; `ax.plot_surface(X, Y, Z)` |
| une échelle logarithmique | `ax.set_yscale("log")` |
| plusieurs graphiques | `fig, axes = plt.subplots(1, 3, figsize=(12, 3.5))` |
| une matrice ou une grille en couleurs | `im = ax.imshow(M)` ; `fig.colorbar(im, ax=ax)` ; la ligne 0 est en haut, comme une matrice s'écrit ; pour des valeurs des deux signes, `cmap="RdBu_r", vmin=-a, vmax=a` centre les couleurs sur 0 |
| une trajectoire du plan | `ax.plot(X[:, 0], X[:, 1], "o-")` (un état par ligne de `X`) ; `ax.set_aspect("equal")` pour voir les cercles ronds |
| des valeurs propres dans le plan complexe | `ax.scatter(lam.real, lam.imag)` ; `ax.add_patch(plt.Circle((0, 0), 1, fill=False))` : les puissances de la matrice tendent vers 0 si tous les points sont strictement à l'intérieur du cercle |
| du LaTeX dans un titre | `ax.set_title(r"$f(x) = e^{-x^2}$")` (le `r` devant la chaîne) |

`wbm.setup()` règle le style des graphiques (taille, couleurs lisibles par les daltoniens) ; termine chaque cellule graphique par `plt.show()`.
