# M13a · Vraisemblance et régression logistique — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M13a.Q1 — Vraisemblance, log-vraisemblance, maximum : le vocabulaire

<details><summary>Indice 1</summary>

Relis le §1 de la fiche, et M04 §3.

</details>
<details><summary>Indice 2</summary>

La vraisemblance est la probabilité des **données**, vue comme une fonction du paramètre.

</details>
<details><summary>Indice 3</summary>

5 : une probabilité est au plus 1, une densité peut dépasser 1. 6 : M02c, le biais de la variance en $\frac{1}{n}$.

</details>

### M13a.Q2 — Log-loss et cross-entropy : la même chose ?

<details><summary>Indice 1</summary>

Relis le §2 de la fiche.

</details>
<details><summary>Indice 2</summary>

Log-loss $= -\frac{1}{n}\ell$ ; chaque terme est $-\ln$ de la probabilité du label observé.

</details>
<details><summary>Indice 3</summary>

5 : la log-loss moyenne vaut $H(\pi) + \mathrm{KL}(\pi \,\Vert\, q)$ ; le taux d'erreur ne dépend que du côté de 0,5.

</details>

### M13a.Q3 — Les propriétés de la sigmoïde et de la softplus

<details><summary>Indice 1</summary>

Relis le §3 de la fiche, et R6 §7.

</details>
<details><summary>Indice 2</summary>

Écris $1 + e^z$ et $1 + e^{-z}$ ; leur rapport est $e^z$.

</details>
<details><summary>Indice 3</summary>

4 : $\sigma(z) = \frac{1}{1 + e^{-z}}$, donc $-\ln\sigma(z) = \ln(1 + e^{-z})$. 5 : $e^{709}$ est à peu près le plus grand nombre représentable.

</details>

### M13a.Q4 — Ce que modélise un score w · x + b

<details><summary>Indice 1</summary>

Relis « Le modèle » et « La frontière et les lignes de niveau » (fiche §4).

</details>
<details><summary>Indice 2</summary>

Le score est le logit de la probabilité ; la cote est $e^z$, un produit de facteurs $e^{w_jx_j}$.

</details>
<details><summary>Indice 3</summary>

5 : deux points symétriques par rapport à la frontière ont des scores opposés.

</details>

### M13a.Q5 — Génératif ou discriminant ?

<details><summary>Indice 1</summary>

Relis « Génératif ou discriminant » et « L'hypothèse naïve » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Un modèle génératif modélise les features de chaque classe ; un discriminant, la classe sachant les features.

</details>
<details><summary>Indice 3</summary>

4 : le cas gaussien de même variance, à la fin du §5.

</details>

### M13a.Q6 — Entropie et Gini : leurs propriétés

<details><summary>Indice 1</summary>

Relis le §6 de la fiche.

</details>
<details><summary>Indice 2</summary>

Les deux impuretés sont nulles pour une loi pure, maximales pour la loi uniforme, et concaves.

</details>
<details><summary>Indice 3</summary>

3 : $1 - \sum_k p_k^2$ avec $0{,}81$, $0{,}0025$ et $0{,}0025$.

</details>

### M13a.Q7 — Variance intra et variance inter : les feuilles d'un arbre de régression

<details><summary>Indice 1</summary>

Relis le §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

La variance totale se coupe en une moyenne pondérée des variances des groupes, plus la variance des moyennes des groupes.

</details>
<details><summary>Indice 3</summary>

5 : la dernière partie du §7, « Gini est une variance ».

</details>

### M13a.Q8 — Convexe ou pas ?

<details><summary>Indice 1</summary>

Relis « Log-somme-exp est convexe, et la softplus aussi » (fiche §3) et l'ajustement du §4.

</details>
<details><summary>Indice 2</summary>

La convexité se garde par composition avec une application affine et par somme.

</details>
<details><summary>Indice 3</summary>

2 : regarde la forme en S de la sigmoïde. 6 : une fonction qui fait des sauts n'est pas convexe.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### M13a.R1 — Bayes et le lissage de Laplace (M04)

<details><summary>Indice 1</summary>

Relis M04 §1, §5 et §7.

</details>
<details><summary>Indice 2</summary>

$P(D \mid S) = \frac{P(S \mid D)P(D)}{P(S \mid D)P(D) + P(S \mid \bar{D})P(\bar{D})}$.

</details>
<details><summary>Indice 3</summary>

2 : $\frac{k + 1}{n + 2}$ avec $k = 0$ échec sur $n = 9$. 5 : $e^{\ln a} = a$.

</details>

### M13a.R2 — Entropie, cross-entropy et information mutuelle (M06)

<details><summary>Indice 1</summary>

Relis M06 §2, §4, §5 et §6.

</details>
<details><summary>Indice 2</summary>

$H(\mathbf{p}, \mathbf{q}) = -\sum p_k\log_2 q_k$, et $\mathrm{KL} = H(\mathbf{p}, \mathbf{q}) - H(\mathbf{p})$.

</details>
<details><summary>Indice 3</summary>

1 : trois termes $0{,}25 \times 2$ et deux termes $0{,}125 \times 3$.

</details>

### M13a.R3 — Fonctions convexes de plusieurs variables (M10)

<details><summary>Indice 1</summary>

Relis M10 §1, « Ensembles convexes et fonctions convexes ».

</details>
<details><summary>Indice 2</summary>

La définition compare $f$ en un point d'un segment à la moyenne des valeurs aux extrémités.

</details>
<details><summary>Indice 3</summary>

4 : l'inégalité triangulaire.

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M13a.1 — Le maximum de vraisemblance d'une loi de Bernoulli et d'une loi catégorielle

<details><summary>Indice 1</summary>

Relis « Un principe, trois lois » (fiche §1).

</details>
<details><summary>Indice 2</summary>

$\ell(p) = k\ln p + (n - k)\ln(1 - p)$, maximum en $\frac{k}{n}$ ; catégorielle : $\frac{n_k}{N}$, lissée : $\frac{n_k + \alpha}{N + K\alpha}$.

</details>
<details><summary>Indice 3</summary>

$k = 7$, $n = 20$ ; f) $\frac{n_k + 1}{24}$ ; g) $\frac{n_k + 0{,}5}{22}$ ; h) $5\ln\frac{5}{20} + 9\ln\frac{9}{20} + 6\ln\frac{6}{20}$.

</details>

### Ex M13a.2 — Le maximum de vraisemblance d'une loi normale : μ̂ et σ̂²

<details><summary>Indice 1</summary>

Relis la loi normale du §1 de la fiche.

</details>
<details><summary>Indice 2</summary>

Les écarts à la moyenne sont $-11, 6, -5, 14, -8, 4$.

</details>
<details><summary>Indice 3</summary>

f) $\ell(\hat{\mu}, \hat{\sigma}^2) = -\frac{n}{2}\big(\ln(2\pi\hat{\sigma}^2) + 1\big)$ ; g) garde la formule générale, avec $v = 91{,}6$.

</details>

### Ex M13a.3 — La log-loss de quatre prédictions, puis la même en cross-entropy

<details><summary>Indice 1</summary>

Relis « Un classifieur probabiliste a une vraisemblance » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Pour un label 0, le terme est $-\ln(1 - \hat{p})$.

</details>
<details><summary>Indice 3</summary>

a) $-\ln 0{,}8$, $-\ln 0{,}45$, $-\ln 0{,}65$, $-\ln 0{,}95$. c) divise par $\ln 2$.

</details>

### Ex M13a.4 — Ce que coûte une prédiction sûre et fausse : la log-loss quand p tend vers 0

<details><summary>Indice 1</summary>

Relis « Une probabilité presque nulle coûte sans limite » (fiche §2).

</details>
<details><summary>Indice 2</summary>

Les 999 exemples valent ensemble $999 \times (-\ln 0{,}98)$ ; le dernier, $-\ln q$ ; on divise le total par 1 000.

</details>
<details><summary>Indice 3</summary>

d) le dernier pèse autant que les autres quand $-\ln q = 999 \times (-\ln 0{,}98)$. f) $\log_2 10^4$.

</details>

### Ex M13a.5 — La sigmoïde : valeurs, logit, cote et symétrie σ(−z) = 1 − σ(z)

<details><summary>Indice 1</summary>

Relis R6 §7 et le §3 de la fiche.

</details>
<details><summary>Indice 2</summary>

Cote $= \frac{p}{1 - p}$, logit $= \ln$(cote), et $p = \frac{\text{cote}}{1 + \text{cote}}$.

</details>
<details><summary>Indice 3</summary>

f) le logit de 0,95. h) ajouter $\ln 2$ au score double la **cote**.

</details>

### Ex M13a.6 — La softplus : valeurs, asymptotes et comportement pour |z| grand

<details><summary>Indice 1</summary>

Relis « La softplus » (fiche §3).

</details>
<details><summary>Indice 2</summary>

$s(z) - s(-z) = z$ et $s(z) - z = \ln(1 + e^{-z})$.

</details>
<details><summary>Indice 3</summary>

d) $\ln(1 + e^{-6})$. f) $-\ln(1 - \sigma(z)) = s(z)$. h) l'écart est $\ln(1 + e^{-\lvert z \rvert})$.

</details>

### Ex M13a.7 — Un modèle logistique à deux features : probabilités, cote et frontière de décision

<details><summary>Indice 1</summary>

Relis le §4 de la fiche.

</details>
<details><summary>Indice 2</summary>

Le score $z = 0{,}7\,x_1 + 1{,}1\,x_2 - 3{,}2$ ; la cote est $e^z$ ; la frontière, $z = 0$.

</details>
<details><summary>Indice 3</summary>

f) $z = \ln\frac{0{,}85}{0{,}15}$ en $x_1 = 2$. g) $\frac{z_B}{\lVert \mathbf{w} \rVert}$ (M07).

</details>

### Ex M13a.8 — L'hypothèse naïve à la main : une loi jointe factorisée, comparée à la vraie

<details><summary>Indice 1</summary>

Relis « L'hypothèse naïve » et « Estimer, puis décider » (fiche §5).

</details>
<details><summary>Indice 2</summary>

Calcule les marginales de $x_1$ et $x_2$ dans chaque classe, puis les produits.

</details>
<details><summary>Indice 3</summary>

Classe 1 : $P(x_1 = 1) = P(x_2 = 1) = 0{,}7$ ; classe 0 : $0{,}38$ et $0{,}38$. a posteriori : $\frac{0{,}4\,P(\mathbf{x} \mid 1)}{0{,}4\,P(\mathbf{x} \mid 1) + 0{,}6\,P(\mathbf{x} \mid 0)}$.

</details>

### Ex M13a.9 — Deux classes gaussiennes de même variance : l'a posteriori est une sigmoïde d'un score affine

<details><summary>Indice 1</summary>

Relis la fin du §5 de la fiche.

</details>
<details><summary>Indice 2</summary>

$w = \frac{\mu_1 - \mu_0}{\sigma^2}$, $b = \frac{\mu_0^2 - \mu_1^2}{2\sigma^2} + \ln\frac{\pi_1}{\pi_0}$.

</details>
<details><summary>Indice 3</summary>

h) le coefficient de $x^2$ vaut $-\frac{1}{2\sigma_1^2} + \frac{1}{2\sigma_0^2}$.

</details>

### Ex M13a.10 — L'entropie et l'indice de Gini de quelques distributions

<details><summary>Indice 1</summary>

Relis « Mesurer le mélange d'une distribution » (fiche §6).

</details>
<details><summary>Indice 2</summary>

$H = \sum_k p_k\log_2\frac{1}{p_k}$, $G = 1 - \sum_k p_k^2$.

</details>
<details><summary>Indice 3</summary>

e) $\log_2 2 = 1$, $\log_2 4 = 2$, $\log_2 8 = 3$. g) et h) : $\log_2 K$ et $1 - \frac{1}{K}$.

</details>

### Ex M13a.11 — L'information mutuelle d'un tableau de contingence, et la baisse d'entropie qu'elle mesure

<details><summary>Indice 1</summary>

Relis « Le gain d'information est une information mutuelle » (fiche §6).

</details>
<details><summary>Indice 2</summary>

$H(Y \mid X) = \sum_x P(X = x)\,H(Y \mid X = x)$, avec les lignes du tableau.

</details>
<details><summary>Indice 3</summary>

Lignes : $(0{,}55 ;\ 0{,}45)$, $(\frac{26}{30}, \frac{4}{30})$, $(\frac{17}{30}, \frac{13}{30})$, de poids 0,4, 0,3, 0,3.

</details>

### Ex M13a.12 — La variance d'un groupe coupé en deux : variance intra plus variance inter

<details><summary>Indice 1</summary>

Relis le §7 de la fiche.

</details>
<details><summary>Indice 2</summary>

$m_A = 8$, $m_B = 18$, $m = \frac{96}{7}$.

</details>
<details><summary>Indice 3</summary>

e) $\frac{3}{7}V_A + \frac{4}{7}V_B$ ; f) $\frac{3}{7}(m_A - m)^2 + \frac{4}{7}(m_B - m)^2$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M13a.13 — Le maximum de vraisemblance d'une loi catégorielle, par l'inégalité de Gibbs

<details><summary>Indice 1</summary>

Relis M06 §5 et §6 (cross-entropy, KL, Gibbs).

</details>
<details><summary>Indice 2</summary>

Divise $\ell$ par $N$ : les poids $\frac{n_k}{N}$ sont les $\hat{p}_k$.

</details>
<details><summary>Indice 3</summary>

$\frac{1}{N}\ell(\mathbf{p}) = -H(\hat{\mathbf{p}}, \mathbf{p}) \le -H(\hat{\mathbf{p}})$. 5 : remplace $n_k$ par $n_k + \alpha$.

</details>

### Ex M13a.14 — La log-loss moyenne est moins la log-vraisemblance divisée par n

<details><summary>Indice 1</summary>

Relis le §2 de la fiche.

</details>
<details><summary>Indice 2</summary>

$P(y_i) = \hat{p}_i^{\,y_i}(1 - \hat{p}_i)^{1 - y_i}$.

</details>
<details><summary>Indice 3</summary>

3 : une loi one-hot ne garde qu'un terme de la cross-entropy. 5 : multiplier par une constante positive ne déplace pas le minimum.

</details>

### Ex M13a.15 — Log-somme-exp est convexe : sur une droite, sa dérivée seconde est une variance ; la softplus aussi

<details><summary>Indice 1</summary>

Relis « Log-somme-exp est convexe » (fiche §3) et la variance comme $\mathbb{E}[D^2] - \mathbb{E}[D]^2$ (M02b).

</details>
<details><summary>Indice 2</summary>

$g = \ln S$, $g' = \frac{S'}{S}$ ; dérive $\pi_k = \frac{e^{a_k + td_k}}{S}$ comme un quotient.

</details>
<details><summary>Indice 3</summary>

$\pi_k' = \pi_k(d_k - g')$. 6 : essaie $\mathbf{d} = (1, \ldots, 1)$.

</details>

### Ex M13a.16 — L'indice de Gini est maximal pour la loi uniforme

<details><summary>Indice 1</summary>

Relis le §6 de la fiche et Cauchy-Schwarz (M07).

</details>
<details><summary>Indice 2</summary>

Une somme de carrés est positive ou nulle, et nulle seulement si chaque terme l'est.

</details>
<details><summary>Indice 3</summary>

1 : $\sum_k \frac{1}{K^2} = \frac{1}{K}$ et $\sum_k p_k = 1$. 4 : $p_k^2 \le p_k$ sur $[0, 1]$.

</details>

### Ex M13a.17 — L'entropie est maximale pour la loi uniforme, par l'inégalité de Gibbs

<details><summary>Indice 1</summary>

Relis M06 §6 (la KL est positive).

</details>
<details><summary>Indice 2</summary>

$\log_2\frac{p_k}{1/K} = \log_2 p_k + \log_2 K$.

</details>
<details><summary>Indice 3</summary>

3 : $-p\log_2 p \ge 0$ sur $[0, 1]$, nul en 0 et en 1.

</details>

<a id="reflexion"></a>

## 🔗 📖 🧮 🗣️ Pont, lecture, ordre de grandeur et explication

### Ex M13a.18 — Pont : une sonde linéaire, un modèle logistique en NumPy sur un batch de représentations figées, jusqu'à la log-loss

<details><summary>Indice 1</summary>

Relis « Une sonde linéaire » (fiche §4) et le lien avec la log-loss (fiche §3).

</details>
<details><summary>Indice 2</summary>

Chaque score est le produit scalaire d'une ligne de $\mathbf{H}$ avec $\mathbf{w}$, plus $b$.

</details>
<details><summary>Indice 3</summary>

c) les termes : $s(-1{,}4)$ (label 1), puis $s(-1{,}1)$, $s(0{,}1)$, $s(-0{,}4)$ (labels 0). e) l'entropie, en nats, de la proportion $\frac{1}{4}$.

</details>

### Ex M13a.19 — MML §8.3, relu après M04 : estimer des paramètres, et ce que la régression logistique y ajoute

<details><summary>Indice 1</summary>

Relis le guide de lecture et le 📐 de la fiche avant le livre.

</details>
<details><summary>Indice 2</summary>

MML écrit $L$ pour moins la log-vraisemblance : lis ses formules avec un signe moins.

</details>
<details><summary>Indice 3</summary>

Pour 5, cherche au §8.3.4 la phrase sur les prédicteurs $\varphi(\boldsymbol{\theta}^\top\mathbf{x})$ et la fonction de lien.

</details>

### Ex M13a.20 — Fermi : la loi jointe complète contre l'hypothèse naïve, combien de nombres pour 30 features à 4 valeurs ?

<details><summary>Indice 1</summary>

Relis « L'hypothèse naïve » (fiche §5).

</details>
<details><summary>Indice 2</summary>

La loi complète a $4^{30}$ cases ; Naïve Bayes, 30 lois à 4 valeurs par segment.

</details>
<details><summary>Indice 3</summary>

$4^{30} = 2^{60} \approx 10^{18}$ ; une loi à 4 valeurs a 3 probabilités libres.

</details>

### Ex M13a.21 — Expliquer pourquoi on minimise la log-loss plutôt que le taux d'erreur

<details><summary>Indice 1</summary>

Relis « Pourquoi la log-loss » et la figure de la log-loss contre l'erreur (fiche §2).

</details>
<details><summary>Indice 2</summary>

Trois idées : la confiance, la forme de la courbe, la vraisemblance.

</details>
<details><summary>Indice 3</summary>

Un exemple : un label 1 prédit à 0,6 puis à 0,95, avec la même erreur et deux log-loss différentes.

</details>

<a id="entretien"></a>

## 💼 Entretien

### M13a.E1 — « Pourquoi la cross-entropy est-elle une log-vraisemblance ? »

<details><summary>Indice 1</summary>

Relis le §2 de la fiche.

</details>
<details><summary>Indice 2</summary>

Pars du modèle des labels : indépendants, tirés de la loi prédite.

</details>
<details><summary>Indice 3</summary>

Produit, logarithme, moyenne changée de signe, cross-entropy avec une loi one-hot ; puis une conséquence.

</details>

### M13a.E2 — « Qu'est-ce que le maximum de vraisemblance, et quel lien avec les losses que vous minimisez ? »

<details><summary>Indice 1</summary>

Relis le §1 de la fiche et son « En machine learning ».

</details>
<details><summary>Indice 2</summary>

Définition, logarithme, deux exemples, deux losses.

</details>
<details><summary>Indice 3</summary>

Bruit gaussien ↔ moindres carrés ; labels de Bernoulli ↔ log-loss ; une limite : le biais ou l'overfitting.

</details>

<a id="notebook"></a>

## Notebook

*(à compléter)*
