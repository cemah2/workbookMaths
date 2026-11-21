# Formulaire

Toutes les formules du workbook, rangées dans l'ordre des chapitres. Les notations suivent `docs/BIBLE.md` §6.

Le formulaire est rangé en quatre fichiers, un par groupe de parties (un seul fichier était trop long pour que GitHub l'affiche) :

- [Parties 0, I et II](formulaire_parties_0_a_2.md) : Partie 0 · Remise à niveau, Partie I · Fondations, Partie II · Concepts
- [Parties III, IV et V](formulaire_parties_3_a_5.md) : Partie III · ML classique, Partie IV · Réseaux, Partie V · Architectures
- [Partie VI](formulaire_partie_6.md) : Partie VI · Génératif et RL
- [Partie VII](formulaire_partie_7.md) : Partie VII · Bonus

## Conventions de notation

- Scalaires en italique ($x$), vecteurs en gras minuscule ($\mathbf{x}$, en colonne), matrices en gras majuscule ($\mathbf{A}$).
- $n$ exemples, $p$ features : $\mathbf{X}$ de forme $(n, p)$ ; MML écrit $N$ et $D$.
- $\ln$ = logarithme népérien ; MML et NumPy écrivent $\log$ pour le même logarithme. $\log$ sans base ne sert ici que pour une base quelconque ; sinon $\log_2$, $\log_{10}$.
- Vecteurs du plan et de l'espace : $\vec{u}$ et $\overrightarrow{AB}$, la notation du lycée, en partie 0 (R9) ; en gras à partir de la partie I (M02c §8, M05b, M07).
- Gradient : de la forme de $\mathbf{x}$ pour l'optimisation ; vecteur ligne (convention jacobienne de MML) pour le calcul matriciel ; chaque fiche dit laquelle.
- Pour lire les symboles : [`symboles.md`](symboles.md).
