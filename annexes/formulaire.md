# Formulaire

Toutes les formules du workbook, rangées dans l'ordre des chapitres. Chaque chapitre ajoute les siennes à sa publication ; les notations suivent `docs/BIBLE.md` §6.

## Conventions de notation

- Scalaires en italique ($x$), vecteurs en gras minuscule ($\mathbf{x}$, en colonne), matrices en gras majuscule ($\mathbf{A}$).
- $n$ exemples, $p$ features : $\mathbf{X}$ de forme $(n, p)$ ; MML écrit $N$ et $D$.
- $\log$ = logarithme népérien ($\ln$) sauf mention contraire ($\log_2$, $\log_{10}$).
- Gradient : de la forme de $\mathbf{x}$ pour l'optimisation ; vecteur ligne (convention jacobienne de MML) pour le calcul matriciel ; chaque fiche dit laquelle.
- Pour lire les symboles : [`symboles.md`](symboles.md).

## Partie 0 · Remise à niveau

### R1 · Nombres et calcul

| Notion | Formule |
|---|---|
| ensembles de nombres | $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{D} \subset \mathbb{Q} \subset \mathbb{R}$ |
| distributivité | $k(a + b) = ka + kb$ ; $-(a - b) = -a + b$ |
| fractions | $\frac{a}{b} + \frac{c}{d} = \frac{ad + cb}{bd}$ ; $\frac{a}{b} \times \frac{c}{d} = \frac{ac}{bd}$ ; $\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c}$ |
| PGCD (Euclide) | $\operatorname{PGCD}(a, b) = \operatorname{PGCD}(b, r)$ si $a = bq + r$ ; le dernier reste non nul |
| puissances | $a^m a^n = a^{m+n}$ ; $\frac{a^m}{a^n} = a^{m-n}$ ; $(a^m)^n = a^{mn}$ ; $(ab)^n = a^n b^n$ ; $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ |
| exposants nul et négatifs | $a^0 = 1$ ; $a^{-n} = \frac{1}{a^n}$ ($a \ne 0$) |
| racines carrées | $\sqrt{ab} = \sqrt{a}\sqrt{b}$ ; $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$ ; $(\sqrt{a})^2 = a$ ; $\sqrt{a^2} = a$ si $a \ge 0$ ; $\sqrt{a} = a^{1/2}$ |
| notation scientifique | $x = m \times 10^k$, $1 \le \lvert m \rvert < 10$ |
| ordre de grandeur | $10^k$ si $\lvert m \rvert < \sqrt{10} \approx 3{,}16$, sinon $10^{k+1}$ |
| plancher, plafond | $\lfloor x \rfloor \le x < \lfloor x \rfloor + 1$ ; $\lceil x \rceil - 1 < x \le \lceil x \rceil$ |
| taux d'évolution | $t = \frac{V_a - V_d}{V_d}$ ; coefficient $1 + t$ |
| évolutions successives | coefficient global $(1 + t_1)(1 + t_2)\cdots(1 + t_n)$ |
| évolution réciproque | coefficient $\frac{1}{1 + t}$ |
| moyenne, moyenne pondérée | $\bar{x} = \frac{1}{n}\sum_i x_i$ ; $\bar{x}_w = \frac{\sum_i w_i x_i}{\sum_i w_i}$ |
| somme pondérée (neurone) | $z = \sum_i w_i x_i + b$ |
| moyenne harmonique | $H = \frac{n}{\sum_i \frac{1}{x_i}}$ |

### R2 · Calcul littéral et équations

| Notion | Formule |
|---|---|
| double distributivité | $(a + b)(c + d) = ac + ad + bc + bd$ |
| identités remarquables | $(a + b)^2 = a^2 + 2ab + b^2$ ; $(a - b)^2 = a^2 - 2ab + b^2$ ; $(a + b)(a - b) = a^2 - b^2$ |
| équation $ax + b = 0$ | $a \ne 0$ : $x = -\frac{b}{a}$ ; $a = 0$, $b \ne 0$ : aucune solution ; $a = b = 0$ : tous les réels |
| produit nul | $AB = 0 \iff A = 0$ ou $B = 0$ |
| inéquations | multiplier ou diviser par $k < 0$ retourne le sens : $a < b \iff ka > kb$ |
| valeur absolue | $\lvert x \rvert = x$ si $x \ge 0$, $-x$ sinon ; $\sqrt{x^2} = \lvert x \rvert$ ; distance $\lvert a - b \rvert$ |
| $\lvert x - a \rvert = c$ | $c > 0$ : $x = a \pm c$ ; $c = 0$ : $x = a$ ; $c < 0$ : aucune solution |
| $\lvert x - a \rvert \le r$, $\lvert x - a \rvert > r$ | $[a - r \;;\; a + r]$ ; $]-\infty \;;\; a - r[ \,\cup\, ]a + r \;;\; +\infty[$ |
| fonction signe | $\operatorname{sign}(x) \in \{-1, 0, 1\}$ ; $x = \operatorname{sign}(x)\,\lvert x \rvert$ |
| système 2 × 2 | $ax + by = e$, $cx + dy = f$ ; déterminant $D = ad - bc$ |
| formule de Cramer ($D \ne 0$) | $x = \frac{ed - bf}{D}$ ; $y = \frac{af - ec}{D}$ |
| déterminant nul | aucune solution ou une infinité (droites parallèles ou confondues) |

*(R3 à R9 ajoutés avec leurs chapitres)*

## Partie I · Fondations

*(ajouté avec les chapitres M02a à M06)*

## Partie II · Concepts

*(ajouté avec les chapitres M07 à M11)*

## Partie III · ML classique

*(ajouté avec les chapitres M12a à M14)*

## Partie IV · Réseaux

*(ajouté avec les chapitres M16 à M20)*

## Partie V · Architectures

*(ajouté avec les chapitres M21 et M22)*

## Partie VI · Génératif et RL

*(ajouté avec les chapitres M25a à M28)*

## Partie VII · Bonus

*(ajouté avec les chapitres MB2 à MB8)*
