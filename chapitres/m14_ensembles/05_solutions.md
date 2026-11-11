# M14 · Les maths des ensembles — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M14.Q1 — La queue d'une loi binomiale et ses bornes : vrai ou faux
1. **Faux** : $P(X \ge k) = 1 - P(X \le k - 1) = 1 - P(X < k)$. La formule de l'énoncé enlève aussi $P(X = k)$.
2. **Faux** : $\frac{p}{a}$ ne dépend pas de $n$. Markov ne voit pas que la queue diminue.
3. **Vrai** : $\mathrm{KL}(a \Vert p) \ge 2(a - p)^2$ (Pinsker, ∂ M14.8, question 5), donc $e^{-n\,\mathrm{KL}(a \Vert p)} \le e^{-2n(a - p)^2}$.
4. Rien : la méthode ne donne que la borne triviale 1. Pour $a \le p$ et tout $\lambda > 0$, $\ln(1 - p + pe^\lambda) \ge p\lambda$ (concavité du logarithme), donc l'exposant $n(-\lambda a + \ln(1 - p + pe^\lambda))$ est positif ou nul, et le meilleur choix est $\lambda \to 0$. Attention : pour $a < p$, la formule $e^{-n\,\mathrm{KL}(a \Vert p)}$ serait **fausse** (pour $p = 0{,}4$, $a = 0{,}2$ et $n = 50$, elle donne $\approx 0{,}010$ alors que $P(X \ge 10) \approx 0{,}999$). C'est normal : la proportion de succès tend vers $p \ge a$, l'événement $X \ge na$ n'est pas rare.
5. Elle est élevée au carré : $e^{-2n\,\mathrm{KL}} = \big(e^{-n\,\mathrm{KL}}\big)^2$. Doubler $n$ double l'exposant.
6. **Faux** : $\mathrm{KL}(0{,}25 \Vert 0{,}1) \approx 0{,}0923$ et $\mathrm{KL}(0{,}1 \Vert 0{,}25) \approx 0{,}0725$ (R1).

### M14.Q2 — Corrélation et variance d'une moyenne
1. $5 + 3 + 2 \times (-2) = 4$.
2. **Faux** : $\mathbb{V}\big(\sum_i w_iX_i\big) = \sum_{i,j}w_iw_j\operatorname{Cov}(X_i, X_j)$. Même sans covariances, ce serait $\sum_i w_i^2\,\mathbb{V}(X_i)$, avec des poids **au carré**.
3. $\frac{\sigma^2}{M}$.
4. **Vrai** : $\mathbb{V}\big(\frac{X + Y}{2}\big) = \frac{1}{4}\big(\mathbb{V}(X) + \mathbb{V}(Y) + 2\operatorname{Cov}(X, Y)\big)$ ; une covariance négative retranche au cas non corrélé, $\frac{1}{4}\big(\mathbb{V}(X) + \mathbb{V}(Y)\big)$.
5. La moyenne vaut $\frac{2X_1 + X_2}{3}$, de variance $\frac{4\sigma^2 + \sigma^2}{9} = \frac{5\sigma^2}{9}$, plus que $\frac{\sigma^2}{3} = \frac{3\sigma^2}{9}$. La copie double le poids de $X_1$ sans ajouter de mesure : c'est la moyenne pondérée $\left(\frac{2}{3}, \frac{1}{3}\right)$ de deux variables indépendantes, moins bonne que leur moyenne simple ($\frac{\sigma^2}{2} = \frac{4{,}5\,\sigma^2}{9}$) et que $\frac{\sigma^2}{3}$.
6. **Faux** : la variance est au plus $\big(\sum_i w_i\sigma_i\big)^2 \le \sigma^2$ (∂ M14.7).

### M14.Q3 — Des limites remarquables
1. $e^3$.
2. $e^{-1/2}$.
3. $e^2$ : c'est $\left(\left(1 + \frac{1}{n}\right)^n\right)^2$.
4. 1 : $n\ln\left(1 + \frac{5}{n^2}\right) \approx \frac{5}{n} \to 0$. L'exposant ne grandit pas assez vite.
5. 7.
6. **Faux** : l'erreur relative vaut environ $-\frac{x^2}{2n} = -\frac{16}{200} = -8\,\%$ (exactement $\approx -7{,}5\,\%$ : $1{,}04^{100} \approx 50{,}50$ contre $e^4 \approx 54{,}60$).

### M14.Q4 — Des poids exponentiels
1. Proportionnels à $(5^{-1}, 5^0) = \left(\frac{1}{5}, 1\right)$ : $\left(\frac{1}{6}, \frac{5}{6}\right)$.
2. **Faux** : chaque poids est multiplié par le même facteur $e^{-0{,}7\eta}$, qui s'annule à la normalisation. Seuls les **écarts** de losses cumulées comptent.
3. $\eta \to 0$ : les poids tendent vers l'uniforme, Hedge ignore les losses. $\eta \to +\infty$ : tout le poids va à l'expert de plus petite loss cumulée (partagé à égalité en cas d'ex æquo) : Hedge suit le meneur.
4. Comme $\sqrt{T}$ : $R_T \le \sqrt{\frac{T\ln K}{2}}$. Le regret moyen $\frac{R_T}{T}$ décroît comme $\frac{1}{\sqrt{T}}$, vers 0.
5. Pour de grandes losses cumulées, $e^{-\eta L}$ vaut 0 en flottants (dès que $\eta L$ dépasse environ 745), et la normalisation calcule $\frac{0}{0}$. Retrancher le minimum multiplie tous les termes par le même facteur, qui s'annule à la normalisation, et laisse un exposant nul au meilleur expert.
6. **Faux** : à un tour donné, ta loss est une moyenne des losses des experts, plus grande que la plus petite d'entre elles dès que des experts moins bons ont du poids. La garantie porte sur la **somme** des tours, comparée au meilleur expert sur l'ensemble des tours, à un regret près.

<a id="rappels"></a>

## 🔁 Rappels

### M14.R1 — La log-loss et la divergence KL (M13a, M06)
1. $0{,}25\ln\frac{0{,}25}{0{,}1} + 0{,}75\ln\frac{0{,}75}{0{,}9} \approx 0{,}2291 - 0{,}1367 = 0{,}0923$.
2. $0{,}1\ln\frac{0{,}1}{0{,}25} + 0{,}9\ln\frac{0{,}9}{0{,}75} \approx -0{,}0916 + 0{,}1641 = 0{,}0725$ : la divergence n'est pas symétrique.
3. $-\big(0{,}1\ln 0{,}25 + 0{,}9\ln 0{,}75\big) \approx 0{,}1386 + 0{,}2589 = 0{,}3975$.
4. $H(0{,}1) \approx 0{,}3251$, et $0{,}3975 - 0{,}3251 = 0{,}0725 = \mathrm{KL}(0{,}1 \Vert 0{,}25)$ : la loi des données d'abord, celle du modèle ensuite (M13a §2).
5. Si et seulement si $a = p$ : c'est l'inégalité de Gibbs (M06), $\mathrm{KL} \ge 0$ avec égalité seulement pour deux lois égales.

### M14.R2 — La variance d'une somme et la matrice de covariance (M02c)
1. $\mathbb{V}(aX + bY) = a^2\,\mathbb{V}(X) + b^2\,\mathbb{V}(Y) + 2ab\operatorname{Cov}(X, Y)$ ; $\mathbb{V}(3X - 2Y) = 18 + 12 - 6 = 24$.
2. $\frac{2 + 3 + 2 \times 0{,}5}{4} = 1{,}5$, moins que la moyenne des variances, $2{,}5$.
3. $\mathbb{V}(X) - \mathbb{V}(Y) = -1$ : par bilinéarité, $\operatorname{Cov}(X, Y)$ et $-\operatorname{Cov}(Y, X)$ s'annulent.
4. $\begin{pmatrix} 2 & 0{,}5 \\ 0{,}5 & 3 \end{pmatrix}$. Symétrique, car $\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X)$ ; semi-définie positive, car $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w} = \mathbb{V}(w_1X + w_2Y) \ge 0$ pour tout $\mathbf{w}$.
5. $\frac{0{,}5}{\sqrt{2 \times 3}} \approx 0{,}2041$.

### M14.R3 — Taylor et ln(1 + u) (M05a)
1. $\ln(1 + u) = u - \frac{u^2}{2} + o(u^2)$.
2. $-0{,}03 - \frac{0{,}0009}{2} = -0{,}030450$, contre $\ln 0{,}97 \approx -0{,}030459$. L'approximation est **au-dessus** : pour $u < 0$, tous les termes suivants ($\frac{u^3}{3}$, $-\frac{u^4}{4}$…) sont négatifs ; le premier oublié, $\frac{u^3}{3} = -9 \times 10^{-6}$, donne presque tout l'écart.
3. Pour $-1 < u \le 1$.
4. 1 : pour $u$ petit, $\ln(1 + u) \approx u$, avec une erreur relative qui tend vers 0.
5. $e^x = \sum_{k \ge 0}\frac{x^k}{k!} = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots$, pour tout réel $x$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M14.1 — La fiabilité d'un système « k parmi n » : au moins k composants qui marchent

**Réponses** : a) `0.9470` · b) `0.1722` · c) `0.9` · d) `0.0530` · e) `1.8113` · f) `0.3753` · g) `0.3` · h) `0.8891`.

**Démarche.** $P(X = 7) = 36 \times 0{,}9^7 \times 0{,}1^2 \approx 0{,}1722$, $P(X = 8) = 9 \times 0{,}9^8 \times 0{,}1 = 0{,}9^9 \approx 0{,}3874$ et $P(X = 9) = 0{,}9^9 \approx 0{,}3874$ : a) $\approx 0{,}9470$. Chaque machine tombe en panne avec la probabilité $0{,}1$, indépendamment : $F$ compte les « succès » d'une panne, de loi $\mathcal{B}(9 ;\ 0{,}1)$, d'espérance $0{,}9$, et $P(F \ge 3) = P(X \le 6) = 1 - $ a). Les bornes portent sur $P(F \ge 9a)$ avec $a = \frac{3}{9} = \frac{1}{3}$ et $p = 0{,}1$ : $\mathrm{KL}\left(\frac{1}{3} \Vert 0{,}1\right) = \frac{1}{3}\ln\frac{10}{3} + \frac{2}{3}\ln\frac{20}{27} \approx 0{,}20125$, d'où e) $\approx 1{,}8113$ et la borne de Chernoff $e^{-1{,}8113} \approx 0{,}1634$ ; f) $= e^{-18 \times 49/900} = e^{-0{,}98}$ ; g) $= \frac{\mathbb{E}[F]}{3}$.

Pour la copie : Chernoff (0,163), puis Markov (0,3), puis Hoeffding (0,375). Hoeffding ne sait pas que $p$ est petit : il ne voit que l'intervalle $[0, 1]$. Toutes restent loin de 0,053 : pour $n = 9$, les bornes exponentielles n'ont pas encore « décollé », et Chernoff perd un facteur qui ne décroît que comme une puissance de $n$ (fiche §1). Avec 12 machines dont 10 nécessaires, la fiabilité baisse (0,889) : il y a plus de machines qui peuvent tomber ($\mathbb{E}[F] = 1{,}2$) pour la même tolérance de 2 pannes. Avec M08 : `testing.binomial_test(7, 9, 0.9, alternative="greater")` rend a).

**Erreurs fréquentes.** $P(X > 7) \approx 0{,}7748$ au lieu de $P(X \ge 7)$ ; $\mathbb{E}[F] = 8{,}1$ (le paramètre des succès) ; $P(F > 3) \approx 0{,}0083$ ; $\mathrm{KL}(0{,}1 \Vert \frac13)$ au lieu de $\mathrm{KL}(\frac13 \Vert 0{,}1)$ (exposant $\approx 1{,}3473$) ; oublier le facteur $n = 9$ ($0{,}2013$) ; Markov avec $\mathbb{E}[X]$, qui donne $2{,}7$, une « borne » plus grande que 1.

**Variante.** Avec $p = 0{,}95$, 9 machines dont 7 nécessaires ? *Réponse* : $\approx 0{,}9916$.

### Ex M14.2 — La variance de la moyenne de trois mesures corrélées, par la matrice de covariance

**Réponses** : a) `"8/9"` · b) `"10/9"` · c) `"5/8"` · d) `["6/19", "3/19", "10/19"]` · e) `"11/19"` · f) `0.2582`.

**Démarche.** a) $\frac{1}{9}$ fois la somme des neuf cases : $3 + 5 + 2 + 2(1 - 1 - 1) = 8$. b) $\frac{3 + 5 + 2}{9}$. c) $\frac{3}{16} + \frac{5}{16} + \frac{2}{4} + 2\left(\frac{1}{16} - \frac{1}{8} - \frac{1}{8}\right) = 1 - \frac{3}{8}$. d) On résout $\boldsymbol{\Sigma}\mathbf{v} = \mathbf{1}$ : $\boldsymbol{\Sigma}\,(6, 3, 10)^\top = (11, 11, 11)^\top$, donc $\mathbf{v} = \frac{1}{11}(6, 3, 10)$, de somme $\frac{19}{11}$, et $\mathbf{w}^* = \frac{1}{19}(6, 3, 10)$. e) $\frac{1}{\mathbf{1}^\top\boldsymbol{\Sigma}^{-1}\mathbf{1}} = \frac{11}{19}$ ; on le retrouve par $\mathbf{w}^{*\top}\boldsymbol{\Sigma}\mathbf{w}^* = \mathbf{w}^{*\top}\frac{11}{19}\mathbf{1} = \frac{11}{19}$. f) $\frac{1}{\sqrt{3 \times 5}}$.

Pour la copie : a) < b) parce que la somme des covariances, $2(1 - 1 - 1) = -2$, est négative. Le lagrangien $\mathbf{w}^\top\boldsymbol{\Sigma}\mathbf{w} - \lambda(\mathbf{1}^\top\mathbf{w} - 1)$ a pour gradient $2\boldsymbol{\Sigma}\mathbf{w} - \lambda\mathbf{1}$ ; il s'annule pour $\mathbf{w} = \frac{\lambda}{2}\boldsymbol{\Sigma}^{-1}\mathbf{1}$, et la contrainte fixe $\lambda$. Le meilleur instrument seul (variance 2) correspond aux poids $(0, 0, 1)$, admissibles : le minimum fait au moins aussi bien, et strictement mieux puisque $(0, 0, 1)$ n'est pas proportionnel à $\boldsymbol{\Sigma}^{-1}\mathbf{1}$.

**Erreurs fréquentes.** Oublier les covariances (a et c) ; la somme au lieu de la moyenne (8) ; ne pas normaliser $\boldsymbol{\Sigma}^{-1}\mathbf{1}$.

**Variante.** Avec les instruments 1 et 3 seulement ? *Réponse* : $\mathbf{w}^* = \left(\frac{3}{7}, \frac{4}{7}\right)$, variance $\frac{5}{7}$.

### Ex M14.3 — (1 + x/n)ⁿ pour quelques n, et des intérêts composés en continu

**Réponses** : a) `1.459142` · b) `1.472358` · c) `1.476621` · d) `1.476981` · e) `-0.003130` · f) `-0.003169` · g) `-0.131` · h) `563`.

**Démarche.** $\left(1 + \frac{0{,}065}{m}\right)^{6m} = \left(1 + \frac{0{,}39}{N}\right)^N$ avec $x = 0{,}065 \times 6 = 0{,}39$ et $N = 6m$ : $N = 6$, 24, 312, puis $N \to \infty$, d'où d) $= e^{0{,}39}$. e) $\frac{1{,}472358}{1{,}476981} - 1 \approx -0{,}003130$. f) $-\frac{0{,}39^2}{2 \times 24} = -0{,}00316875$. g) $1{,}1^{30} \approx 17{,}4494$ et $e^3 \approx 20{,}0855$. h) $\frac{9}{2n} < 0{,}008$ demande $n > 562{,}5$.

Pour la copie : $n \mapsto \left(1 + \frac{x}{n}\right)^n$ est croissante pour $x > 0$ (∂ M14.6, question 5) et tend vers $e^x$ : a) < b) < c) < d). e) et f) sont très proches, parce que $\frac{x^2}{N} \approx 0{,}006$ est petit : les termes suivants du développement sont de l'ordre de $\frac{1}{N^2}$. En g), $\frac{x^2}{n} = 0{,}3$ n'est pas petit : les termes suivants, $\frac{x^3}{3n^2} = 0{,}01$ et $\frac{1}{2}\left(\frac{x^2}{2n}\right)^2 \approx 0{,}011$, ramènent $-0{,}15$ vers $-0{,}129$, déjà près de $-0{,}131$. La vraie erreur passe sous 0,8 % dès $n = 559$ : l'approximation surestime un peu l'erreur.

**Erreurs fréquentes.** $1{,}065$ (une seule année) ; $e^{0{,}065}$ pour d) ; une erreur relative positive ; $N = 4$ au lieu de 24 en f) ($-0{,}019013$) ; $n = 562$ (l'arrondi dans le mauvais sens).

**Variante.** Avec un versement par mois ? *Réponse* : $\left(1 + \frac{0{,}065}{12}\right)^{72} \approx 1{,}475427$.

### Ex M14.4 — Les poids exponentiels de cinq experts après trois tours

**Réponses** : a) `["1/3", "1/9", "1/9", "1/3", "1/9"]` · b) `["3/19", "3/19", "1/19", "9/19", "3/19"]` · c) `["3/11", "1/11", "1/11", "3/11", "3/11"]` · d) `"1433/855"` · e) `1` · f) `0.6760` · g) `1.877` · h) `2.0717`.

**Démarche.** Avant le tour 1, les poids sont uniformes et la loss de l'algorithme vaut $\frac{3}{5}$. Avant le tour 2, les losses cumulées $(0, 1, 1, 0, 1)$ donnent $3^{-L} = \left(1, \frac{1}{3}, \frac{1}{3}, 1, \frac{1}{3}\right)$, de somme 3 ; la loss du tour vaut $\frac{1}{3} + \frac{1}{9} = \frac{4}{9}$. Avant le tour 3 : $(1, 1, 2, 0, 1)$, soit $9 \times 3^{-L} = (3, 3, 1, 9, 3)$, de somme 19 ; loss $\frac{3 + 9}{19} = \frac{12}{19}$. Après le tour 3 : $(1, 2, 2, 1, 1)$, soit $(3, 1, 1, 3, 3)$, de somme 11. d) $\frac{3}{5} + \frac{4}{9} + \frac{12}{19} = \frac{513 + 380 + 540}{855}$. e) Les experts 1, 4 et 5 finissent avec 1. f) $\frac{1433}{855} - 1 = \frac{578}{855}$. g) $\frac{\ln 5}{\ln 3} + \frac{3\ln 3}{8} \approx 1{,}4650 + 0{,}4120$. h) $\sqrt{\frac{8\ln 5}{3}}$.

Pour la copie : la borne vaut pour **toutes** les suites de losses, même choisies contre l'algorithme ; ici, rien n'est adverse, et $T = 3$ est petit. Avec $\eta \approx 2{,}07$ au lieu de $\ln 3 \approx 1{,}10$, un point de loss divise le poids par $e^{2{,}07} \approx 7{,}9$ au lieu de 3 : après trois tours, les poids seraient $\approx (0{,}31 ;\ 0{,}04 ;\ 0{,}04 ;\ 0{,}31 ;\ 0{,}31)$, plus concentrés sur les trois meilleurs.

**Erreurs fréquentes.** Ne pas normaliser ($(1, \frac{1}{3}, \frac{1}{3}, 1, \frac{1}{3})$ en a) ; utiliser la loss du tour au lieu de la loss cumulée ; $3^{+L}$, qui récompense les losses ; le regret mesuré contre le pire expert.

**Variante.** Et si l'expert 4 avait eu 0 au tour 3 ? *Réponse* : poids après le tour 3 $= \frac{1}{17}(3, 1, 1, 9, 3)$.

### Ex M14.5 — Le gradient de la loss exponentielle e^(−yF) et de la loss de Huber par rapport aux prédictions, et les poids exponentiels qu'il fait apparaître

**Réponses** : a) `[2, -0.5, 1.5, -0.3, 0]` · b) `4.357` · c) `[-0.135, -1.649, 0.223, 1.35, -1]` · d) `[0.0311, 0.3784, 0.0512, 0.3098, 0.2295]` · e) `2` · f) `[-0.5, 0.8, 0.3, -0.8]` · g) `2.5700`.

**Démarche.** Les losses $e^{-y_iF_i}$ valent $e^{-2} \approx 0{,}1353$, $e^{0{,}5} \approx 1{,}6487$, $e^{-1{,}5} \approx 0{,}2231$, $e^{0{,}3} \approx 1{,}3499$ et $e^0 = 1$, de somme $\approx 4{,}3570$ ; le gradient multiplie chacune par $-y_i$ ; les poids les divisent par leur somme. Huber, $\delta = 0{,}8$ : résidus $(0{,}5 ;\ -1{,}1 ;\ -0{,}3 ;\ 2{,}7)$ ; gradient $-\operatorname{clip}(r, -0{,}8, 0{,}8)$ ; losses $\frac{0{,}25}{2} = 0{,}125$, $0{,}8 \times (1{,}1 - 0{,}4) = 0{,}56$, $0{,}045$ et $0{,}8 \times (2{,}7 - 0{,}4) = 1{,}84$.

Pour la copie : $\frac{\partial}{\partial F}e^{-yF} = -y\,e^{-yF}$, et l'exponentielle est positive : le signe est celui de $-y$, et faire un pas **contre** le gradient pousse $F_i$ vers $y_i$. L'exemple 2 pèse le plus : sa marge, $-0{,}5$, est la plus négative (le plus mal classé). Ajouter 1 à toutes les marges multiplie toutes les losses par $e^{-1}$ : les poids ne changent pas. Ajouter $\alpha h$ aux scores multiplie la loss de l'exemple $i$ par $e^{-\alpha y_ih_i}$ : son poids grandit si $h$ se trompe de signe sur lui ($y_ih_i < 0$), diminue sinon (fiche §5). Pour Huber, les exemples 2 et 4 ont un gradient coupé ; le point aberrant (résidu 2,7) tire sa prédiction avec la force 0,8, comme un exemple de résidu 0,8.

**Erreurs fréquentes.** Oublier le signe $-y_i$, ou écrire $+e^{-yF}$ ; prendre $-(y - F)$ sans couper ($[-0{,}5 ;\ 1{,}1 ;\ 0{,}3 ;\ -2{,}7]$) ; le signe opposé (le gradient par rapport au résidu, pas à $F$).

**Variante.** Huber avec $\delta = 2$ ? *Réponse* : gradient $[-0{,}5 ;\ 1{,}1 ;\ 0{,}3 ;\ -2]$, loss totale $4{,}175$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M14.6 — (1 + x/n)ⁿ → eˣ, par le logarithme et ln(1 + u) ≈ u

**Réponse modèle.**
0. Pour $u > -1$, avec $v = \ln(1 + u)$ : $1 + u = e^v \ge 1 + v$ (CP1.9 B), donc $\ln(1 + u) \le u$.
1. $h(u) = \ln(1 + u) - u + \frac{u^2}{2}$ vérifie $h(0) = 0$ et $h'(u) = \frac{1}{1 + u} - 1 + u = \frac{u^2}{1 + u} \ge 0$ pour $u \ge 0$ : $h$ est croissante sur $[0, +\infty[$, donc positive ou nulle.
2. $k(u) = \ln(1 + u) - u + u^2$ vérifie $k(0) = 0$ et $k'(u) = \frac{1}{1 + u} - 1 + 2u = \frac{u(1 + 2u)}{1 + u}$. Pour $-\frac{1}{2} \le u \le 0$ : $u \le 0$, $1 + 2u \ge 0$ et $1 + u > 0$, donc $k' \le 0$ : $k$ décroît sur $\left[-\frac{1}{2}, 0\right]$ et $k(u) \ge k(0) = 0$.
3. $n > 2\lvert x \rvert$ donne $\lvert u \rvert < \frac{1}{2}$, donc $1 + u > 0$. Dans les deux cas ($u \ge 0$ par 1, puisque $u - u^2 \le u - \frac{u^2}{2}$ ; $u < 0$ par 2), $u - u^2 \le \ln(1 + u) \le u$. En multipliant par $n > 0$ : $x - \frac{x^2}{n} \le n\ln\left(1 + \frac{x}{n}\right) \le x$. Par encadrement, $n\ln\left(1 + \frac{x}{n}\right) \to x$, et, l'exponentielle étant **continue**, $\left(1 + \frac{x}{n}\right)^n = \exp\left(n\ln\left(1 + \frac{x}{n}\right)\right) \to e^x$.
4. Pour $x \ge 0$, $u = \frac{x}{n} \ge 0$ : la question 1 et la question 0 donnent $x - \frac{x^2}{2n} \le n\ln\left(1 + \frac{x}{n}\right) \le x$. L'exponentielle est croissante ; en divisant par $e^x$ : $e^{-x^2/(2n)} \le \frac{(1 + x/n)^n}{e^x} \le 1$, et $e^{-v} \ge 1 - v$ donne le résultat. L'erreur relative est négative et au plus $\frac{x^2}{2n}$ en valeur absolue : pour une précision $\varepsilon$, $n \ge \frac{x^2}{2\varepsilon}$ suffit (pour $x = 3$ et 1 %, $n \ge 450$).
5. $\varphi'(t) = \ln\left(1 + \frac{x}{t}\right) + t \times \frac{-x/t^2}{1 + x/t} = \ln(1 + v) - \frac{v}{1 + v}$. Avec $u = -\frac{v}{1 + v} \in\ ]-1, 0[$ : $\ln(1 + u) = \ln\frac{1}{1 + v} = -\ln(1 + v)$, et $\ln(1 + u) \le u$ donne $\ln(1 + v) \ge \frac{v}{1 + v}$, donc $\varphi'(t) \ge 0$. $\varphi$ est croissante, donc $n \mapsto n\ln\left(1 + \frac{x}{n}\right)$ aussi, et, l'exponentielle étant croissante, $n \mapsto \left(1 + \frac{x}{n}\right)^n$ aussi.

**Grille.** (0) $\ln(1 + u) \le u$, cité ; (1) et (2) une différence nulle en 0 et le signe de sa dérivée sur le bon intervalle ; (3) $\lvert u \rvert < \frac{1}{2}$, l'encadrement commun, le passage à $n\ln$, l'encadrement et la continuité de l'exponentielle ; (4) l'encadrement de l'erreur relative et ce qu'il dit du $n$ nécessaire ; (5) la dérivée de $\varphi$ et le choix de $u$.

### Ex M14.7 — Une moyenne pondérée de variables de variance σ² a une variance au plus σ²

**Réponse modèle.**
1. Le produit scalaire est $\operatorname{Cov}(X, Y)$, la norme l'écart-type $\sqrt{\mathbb{V}(X)}$. La covariance n'est que **semi**-définie positive : $\mathbb{V}(Y) = 0$ dit seulement que $Y$ est constante, pas nulle. La preuve de M07.14 tient quand même : $t \mapsto \mathbb{V}(X - tY) = \mathbb{V}(X) - 2t\operatorname{Cov}(X, Y) + t^2\,\mathbb{V}(Y)$ est positive pour tout $t$ ; si $\mathbb{V}(Y) > 0$, son discriminant est négatif ou nul ; si $\mathbb{V}(Y) = 0$, elle est affine et positive sur $\mathbb{R}$, donc de pente $-2\operatorname{Cov}(X, Y)$ nulle.
2. $\operatorname{Cov}(X_i, X_j) \le \sqrt{\mathbb{V}(X_i)\,\mathbb{V}(X_j)} \le \sqrt{\sigma^2\sigma^2} = \sigma^2$.
3. $\mathbb{V}\big(\sum_i w_iX_i\big) = \sum_{i,j}w_iw_j\operatorname{Cov}(X_i, X_j) \le \sum_{i,j}w_iw_j\sigma_i\sigma_j = \big(\sum_i w_i\sigma_i\big)^2$, car $w_iw_j \ge 0$ ; puis $\sum_i w_i\sigma_i \le \sigma\sum_i w_i = \sigma$.
4. Il faut $\operatorname{Cov}(X_i, X_j) = \sigma_i\sigma_j$ (corrélation 1) pour tous $i, j$ de poids non nuls, et $\sigma_i = \sigma$ pour chacun. Exemple : $X_2 = X_1$ (ou $X_1 + 3$), de variance $\sigma^2$, et les poids $\left(\frac{1}{2}, \frac{1}{2}\right)$.
5. $X_1$ et $X_2$ indépendantes de variance $\sigma^2$, et les poids $(2, -1)$, de somme 1 : la variance vaut $4\sigma^2 + \sigma^2 = 5\sigma^2$.

**Grille.** (1) la citation de Cauchy-Schwarz, les deux rôles, et le cas $\mathbb{V}(Y) = 0$ ; (2) la majoration de chaque covariance ; (3) la positivité des $w_iw_j$, qui autorise la majoration terme à terme ; (4) la corrélation 1 et un exemple ; (5) un contre-exemple chiffré.

### Ex M14.8 — La borne de Chernoff d'une queue binomiale : le meilleur λ donne exp(−n KL(a ‖ p))

**Réponse modèle.**
1. Seule change l'espérance d'une variable de Bernoulli : $\mathbb{E}[e^{\lambda X_i}] = (1 - p)e^0 + pe^\lambda$ au lieu de $\frac{1 + e^\lambda}{2}$ ; Markov et l'indépendance servent de la même façon. Puis $e^{-\lambda na}(1 - p + pe^\lambda)^n = \exp\big(n(-\lambda a + \ln(1 - p + pe^\lambda))\big) = e^{n\,g(\lambda)}$.
2. $g'(\lambda) = -a + \frac{pe^\lambda}{1 - p + pe^\lambda}$ s'annule quand $pe^\lambda(1 - a) = a(1 - p)$, soit $e^\lambda = \frac{a(1 - p)}{p(1 - a)}$. $g''(\lambda) = \frac{p(1 - p)e^\lambda}{(1 - p + pe^\lambda)^2} > 0$ : $g$ est convexe, et ce point critique est son minimum. Enfin $a(1 - p) > p(1 - a)$ équivaut à $a > p$ : $e^{\lambda^*} > 1$, donc $\lambda^* > 0$.
3. En $\lambda^*$ : $pe^{\lambda^*} = \frac{a(1 - p)}{1 - a}$, donc $1 - p + pe^{\lambda^*} = \frac{1 - p}{1 - a}$, et
$g(\lambda^*) = -a\ln\frac{a(1 - p)}{p(1 - a)} + \ln\frac{1 - p}{1 - a} = -a\ln\frac{a}{p} + (1 - a)\ln\frac{1 - p}{1 - a} = -\mathrm{KL}(a \Vert p)$. La question 1 donne $P(X \ge na) \le e^{n\,g(\lambda)}$ pour tout $\lambda > 0$, en particulier pour $\lambda^*$.
4. $X \ge n$ signifie $X = n$ : $P = p^n$. Et $\mathrm{KL}(1 \Vert p) = 1 \times \ln\frac{1}{p} + 0 = -\ln p$, d'où $e^{-n\,\mathrm{KL}(1 \Vert p)} = p^n$.
5. $f(p) = 0$ ; $f'(a) = \ln\frac{a}{p} - \ln\frac{1 - a}{1 - p} - 4(a - p)$, donc $f'(p) = 0$ ; $f''(a) = \frac{1}{a} + \frac{1}{1 - a} - 4 = \frac{1}{a(1 - a)} - 4 \ge 0$, car $a(1 - a) \le \frac{1}{4}$. $f$ est convexe, sa dérivée s'annule en $p$ : $p$ est son minimum, et $f \ge f(p) = 0$. Donc $e^{-n\,\mathrm{KL}(a \Vert p)} \le e^{-2n(a - p)^2}$ : la borne de Chernoff est toujours au moins aussi bonne que celle de Hoeffding.

**Grille.** (1) le cas $p = \frac{1}{2}$ cité, le facteur $1 - p + pe^\lambda$, la forme $e^{n\,g(\lambda)}$ ; (2) la dérivée, la convexité et $\lambda^* > 0$ ; (3) le calcul de $g(\lambda^*)$ et la conclusion ; (4) le cas $a = 1$ et la convention $0\ln 0 = 0$ ; (5) $f(p)$, $f'(p)$, le signe de $f''$ et la comparaison des bornes.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex M14.9 — Pont : ajouter des modèles très corrélés ne sert presque à rien, un plancher de variance sur deux groupes de modèles

**Réponses** : a) `"4/5"` · b) `"11/20"` · c) `"11/16"` · d) `"7/10"` · e) `"3/5"` · f) `"27/50"` · g) `"19/20"` · h) `"1593/2420"`.

**Démarche.** La moyenne de $m$ modèles de chaque groupe vaut $\frac{Z_A + Z_B}{2} + \frac{1}{2m}\sum_i E_i$ ; les deux termes sont indépendants, de variances $\frac{0{,}7 + 0{,}9 + 2 \times 0{,}3}{4} = 0{,}55$ et $\frac{2m \times 2{,}5}{(2m)^2} = \frac{2{,}5}{2m}$. a) $0{,}55 + 0{,}25$. b) $0{,}55$. c) $\frac{0{,}55}{0{,}8}$. d) Avec le seul groupe A, la moyenne vaut $Z_A + \frac{1}{m}\sum E_i$, de plancher $0{,}7$. e) Avec une proportion $\alpha$ de modèles A, le plancher vaut $\alpha^2 \times 0{,}7 + (1 - \alpha)^2 \times 0{,}9 + 2\alpha(1 - \alpha) \times 0{,}3$, de dérivée $2\alpha - 1{,}2$ : $\alpha^* = 0{,}6$. f) $0{,}36 \times 0{,}7 + 0{,}16 \times 0{,}9 + 0{,}48 \times 0{,}3 = 0{,}54$. g) $0{,}7 + \frac{2{,}5}{10}$. h) $\frac{100^2 \times 0{,}7 + 10^2 \times 0{,}9 + 2 \times 100 \times 10 \times 0{,}3}{110^2} + \frac{2{,}5}{110} = \frac{7\,690 + 275}{12\,100}$.

Pour la copie : le plancher fait déjà $\frac{11}{16} \approx 69\,\%$ de a) avec 10 modèles ; dix de plus, répartis de même, ne pourraient gagner que sur les $31\,\%$ restants (ils les diviseraient par deux : la variance passerait de $0{,}8$ à $0{,}675$). $Z_A$ et $Z_B$ ne sont corrélées qu'à $\frac{0{,}3}{\sqrt{0{,}63}} \approx 0{,}38$ : les moyenner en compense une partie, même si $Z_B$ seul a plus de variance ; d'où b) $< $ d). h) $\approx 0{,}6583$, contre $0{,}7 + \frac{2{,}5}{110} = \frac{159}{220} \approx 0{,}7227$ avec 110 modèles du groupe A : dix modèles d'un autre groupe valent mieux que dix de plus du même, parce qu'ils baissent le plancher, que des modèles du groupe A ne touchent pas. Deux modèles du groupe A ont la covariance $\mathbb{V}(Z_A) = 0{,}7$ et la variance $3{,}2$ : corrélation $\frac{7}{32} \approx 0{,}22$.

**Erreurs fréquentes.** Oublier $\operatorname{Cov}(Z_A, Z_B)$ (a : $\frac{13}{20}$ ; b : $\frac{2}{5}$ ; h : $\frac{1473}{2420}$) ; diviser la part propre par $m$ au lieu de $2m$ (a : $\frac{21}{20}$) ; c) inversé ($\frac{16}{11}$).

**Variante.** Si $\operatorname{Cov}(Z_A, Z_B) = 0$ ? *Réponse* : $\alpha^* = \frac{0{,}9}{0{,}7 + 0{,}9} = \frac{9}{16}$ et le plus petit plancher vaut $\frac{0{,}7 \times 0{,}9}{1{,}6} = \frac{63}{160} \approx 0{,}39$.

### Ex M14.10 — Expliquer pourquoi une moyenne réduit la variance, et quand elle ne la réduit plus

**Réponse modèle** (6 à 10 phrases).
> Pas tout à fait : diviser l'écart-type par six, c'est-à-dire la variance par 36, suppose que les 36 erreurs sont indépendantes. L'erreur de chaque thermomètre a deux parts. Il y a un bruit propre à chaque appareil, tantôt vers le haut, tantôt vers le bas : sur 36 appareils, ces bruits se compensent, et la variance de cette part-là est bien divisée par 36. Mais il y a aussi des erreurs que tous partagent : s'ils sortent de la même usine avec le même défaut d'étalonnage, ou s'ils sont tous sous la même bouche de ventilation, ils se trompent dans le même sens, et la moyenne garde cette erreur entière, qu'il y ait dix appareils ou mille. Ce reste baisse quand les appareils se trompent différemment : d'autres marques, d'autres emplacements ; deux appareils dont les erreurs partent souvent en sens opposés se corrigent même mieux que deux appareils indépendants. Et si certains sont plus fiables, leur donner plus de poids réduit encore la variance. Un ensemble de modèles obéit au même calcul : la part de leurs erreurs qui leur est commune joue le rôle de l'étalonnage d'usine, et c'est elle qui fixe le plancher ; seule la part qui diffère d'un modèle à l'autre se compense.

En 3 phrases : « Moyenner 36 thermomètres divise par 36 la variance du bruit propre à chacun, pas l'erreur qu'ils partagent (le même étalonnage, le même emplacement). La variance de la moyenne garde donc un plancher, d'autant plus haut que les appareils se trompent ensemble. On l'abaisse avec des appareils qui se trompent différemment, voire en sens opposés, et en pondérant davantage les plus fiables. »

**Grille.** (1) l'hypothèse d'indépendance derrière la division ; (2) la part propre, qui se compense ; (3) la part partagée, qui reste ; (4) des appareils différents, et la corrélation négative ; (5) des poids inégaux ; (6) le lien avec un ensemble de modèles (la part commune) ; (7) une version en 3 phrases.

<a id="entretien"></a>

## 💼 Entretien

### M14.E1 — « Comment combiner les avis de plusieurs experts quand on ne sait pas lequel est le meilleur ? »

**Réponse modèle (60 secondes).**

> Le cadre : à chaque tour, $K$ experts donnent un avis, je les combine, puis je découvre la loss de chacun, sans rien supposer sur la façon dont elles sont produites. Suivre simplement l'expert en tête est fragile : si deux experts alternent, le meneur change à chaque tour, je peux me tromper à chaque fois, et mon regret grandit comme $T$. L'algorithme des poids exponentiels, Hedge, garde plutôt une loi sur les experts : le poids de chacun est proportionnel à $e^{-\eta L}$, où $L$ est sa loss cumulée, donc chaque tour multiplie son poids par $e^{-\eta\ell}$ avant de renormaliser, et je prédis la moyenne pondérée des avis. Le regret compare ma loss totale à celle du meilleur expert choisi après coup ; Hedge garantit un regret au plus $\frac{\ln K}{\eta} + \frac{\eta T}{8}$, soit $\sqrt{T\ln K/2}$ avec le bon $\eta$ : il croît comme $\sqrt{T}$, le regret moyen tend vers 0, et $K$ n'intervient que par $\ln K$. Le learning rate règle le compromis : trop petit, on apprend lentement ; trop grand, on suit les à-coups. Sans connaître l'horizon, on prend $\eta_t = \sqrt{8\ln K/t}$, et l'on perd moins d'un facteur 2. À la différence d'un bandit, je vois la loss de **tous** les experts, pas seulement celle de l'expert suivi : je n'ai pas besoin d'explorer. Usage : combiner plusieurs modèles de prévision de la demande dont le meilleur change avec le temps. Freund et Schapire ont présenté Hedge et AdaBoost dans le même article, en 1997 : AdaBoost applique la même mise à jour multiplicative à des poids d'exemples.

**Grille.** (1) le cadre (experts, losses révélées, aucune hypothèse) ; (2) l'échec de « suivre le meneur » ; (3) les poids exponentiels et la mise à jour multiplicative ; (4) le regret et la garantie en $\sqrt{T\ln K}$ ; (5) le learning rate et l'horizon inconnu ; (6) la différence avec un bandit ; (7) un usage, et le lien avec AdaBoost en une phrase.

<a id="notebook"></a>

## Notebook

Le code complet de chaque exercice est dans `05_solutions.ipynb`, exécuté ; voici les réponses, l'essentiel de la démarche et les réponses aux questions de copie.

### Ex M14.11 — La borne de Chernoff et la variance d'une moyenne pondérée · `chernoff_bound, variance_of_average`

**Réponses** : a) `0.034731` · b) `1.0` · c) `0.8625` · d) `0.85525` · e) `True` · f) `"ValueError"`.

**Démarche.** `chernoff_bound` : les contrôles, puis `1.0` si $a \le p$, `0.0` si $p = 0$, sinon `math.exp(-n * kl)` avec le terme en $1 - a$ seulement si $a < 1$. `variance_of_average` : les contrôles de forme, de symétrie et de poids, puis `float(w @ c @ w)`. Pour la copie : $\mathrm{KL}(0{,}45 \Vert 0{,}24) \approx 0{,}2829 - 0{,}1779 = 0{,}1050$, d'où $e^{-32 \times 0{,}1050} \approx 0{,}0347$ ; Hoeffding donne $e^{-64 \times 0{,}21^2} \approx 0{,}0595$ et la queue exacte $P(X \ge 15) \approx 0{,}00395$ : Chernoff est près de deux fois meilleure que Hoeffding et reste neuf fois au-dessus de la vraie valeur. b) Pour $a \le p$, la formule donnerait $0{,}45$, alors que $P(X \ge 5) \approx 0{,}91$ : la borne doit valoir 1. c) La somme des 16 cases vaut $13{,}8$ ; sans les covariances, on aurait $\frac{10{,}4}{16} = 0{,}65$ : les covariances positives l'emportent. d) Les meilleurs poids, $\propto \boldsymbol{\Sigma}^{-1}\mathbf{1} \approx (0{,}276 ;\ 0{,}133 ;\ 0{,}434 ;\ 0{,}157)$, donneraient $\approx 0{,}7967$. e) `25 * 0.6000000000000001` vaut `15.000000000000002` : sans le `- 1e-9`, `math.ceil` donnerait 16 et l'on calculerait $P(X \ge 16)$, une queue trop petite qui laisserait passer une borne fausse. f) Une somme de 1,1 trahit presque toujours une erreur en amont : la renormaliser en silence la cacherait.

**Erreurs fréquentes.** $\mathrm{KL}(p \Vert a)$ ($0{,}047961$) ; la KL en bits ($0{,}007847$) ; oublier le cas $a \le p$ ($0{,}454685$) ; la variance sans les covariances ($0{,}65$) ou la somme des cases sans la diviser par $M^2$ ($13{,}8$).

### Ex M14.12 — Les poids de l'algorithme Hedge · `hedge_weights`

**Réponses** : a) `[0.240663, 0.20714, 0.438516, 0.113681]` · b) `True` · c) `True` · d) `2.742313` · e) `0.642313` · f) `"ValueError"`.

**Démarche.** Une ligne de zéros puis `np.cumsum(losses, axis=0)` : $T + 1$ lignes de losses cumulées ; on retranche le minimum de chaque ligne, puis `np.exp(-eta * shifted)` et la normalisation par ligne. d) `np.sum(W[:-1] * losses)` : les poids **avant** chaque tour. Pour la copie : les losses cumulées valent $(2{,}5 ;\ 2{,}6 ;\ 2{,}1 ;\ 3)$ ; après avoir retranché $2{,}1$, les poids sont $\propto (e^{-0{,}6} ;\ e^{-0{,}75} ;\ 1 ;\ e^{-1{,}35})$. L'expert 3 a le plus de poids alors qu'il n'a gagné qu'un tour, le dernier (les gagnants sont les experts 4, 2, 1, 2, 4, 3) : Hedge suit la loss cumulée, pas les victoires. c) Sans retrancher le minimum, $e^{-1{,}5 \times 42\,000}$ vaut 0 en flottants pour les quatre experts, et la normalisation divise 0 par 0 ; retrancher la même quantité multiplie chaque $e^{-\eta L}$ par le même facteur, que la normalisation annule. e) Le regret, $\approx 0{,}64$, est sous la borne $\frac{\ln 4}{1{,}5} + \frac{1{,}5 \times 6}{8} \approx 2{,}05$.

**Erreurs fréquentes.** Les poids d'après la loss du dernier tour seulement ; le signe $+$ dans l'exponentielle ; oublier de normaliser ; d) avec les poids **après** chaque tour ($2{,}221089$) ; e) contre le pire expert ($-0{,}257687$) ou la moyenne des experts ($0{,}192313$).

### Ex M14.13 — Simuler la moyenne de deux groupes de modèles corrélés, et retrouver aᵀΣa et son plancher

**Réponses** : a) `0.933333` · b) `0.75` · c) `True` · d) `0.9562`.

**Démarche.** Une paire $(Z_A, Z_B)$ par tirage (`rng.multivariate_normal`, `size=n_draws`), les $2m$ parts propres par `rng.normal(0, np.sqrt(2.2), size=(n_draws, 2 * m))`, les erreurs des deux groupes, leur moyenne par ligne, puis `np.var`. La matrice $2m \times 2m$ : des blocs pleins de $0{,}6$, $0{,}5$, $0{,}5$ et $1{,}4$, plus $2{,}2$ sur la diagonale. Pour la copie : la moyenne vaut $\frac{Z_A + Z_B}{2} + \frac{1}{2m}\sum_i E_i$, de variance $\frac{0{,}6 + 1{,}4 + 2 \times 0{,}5}{4} + \frac{2{,}2}{2m} = 0{,}75 + \frac{1{,}1}{m}$ : a) $\frac{14}{15}$ et b) $\frac{3}{4}$. Une variance empirique sur 20 000 tirages fluctue d'environ $\sqrt{2/20\,000} \approx 1\,\%$ : les écarts mesurés restent sous 1,2 %. d) Pour $m = 32$, la variance vaut $0{,}784375$, dont le plancher fait $\frac{240}{251}$ : doubler encore le nombre de modèles ne gagnerait qu'environ $0{,}017$. Deux modèles du groupe B ont la corrélation $\frac{1{,}4}{1{,}4 + 2{,}2} \approx 0{,}389$. Avec $\operatorname{Cov}(Z_A, Z_B) < 0$, les deux parts communes se compenseraient en partie et le plancher baisserait.

**Erreurs fréquentes.** Tirer une paire $(Z_A, Z_B)$ par modèle au lieu d'une par tirage (les parts communes deviennent propres, et le plancher disparaît) ; passer une variance à `rng.normal`, qui attend un écart-type ; oublier la covariance croisée (a : $0{,}683333$) ; diviser la part propre par $m$ au lieu de $2m$ (a : $1{,}116667$).

### Ex M14.14 — Les poids exponentiels au fil des tours : quel expert domine, selon le learning rate

**Vérification manuelle** : ✅ quand les dessins sont dans les axes reçus, avec une courbe (ou une aire) par expert, les bons poids et la valeur de $\eta$ dans chaque titre.

**Démarche.** Une fois `W = hedge_weights(losses, eta)` par axe, puis une courbe par colonne (ou `ax.stackplot`), un titre, une légende, des noms d'axes. Pour la copie : l'expert 3 prend la tête des losses cumulées à la ligne 24 et la garde. Avec $\eta = 3$, son poids passe 0,5 dès la ligne 24 et finit à $\approx 1$, mais pendant les vingt premiers tours le poids saute d'un expert à l'autre (jusqu'à 0,36 en un tour) : chaque saut fait payer la loss d'un expert qui vient de perdre la tête, le terme $\frac{\eta T}{8}$ de la borne. Avec $\eta = 0{,}15$, l'expert 3 ne passe 0,5 qu'à la ligne 68 et finit à $0{,}53$ : trop prudent. $\eta = 0{,}6$ (0,5 dépassé à la ligne 36, $0{,}95$ à la fin) est le plus proche de $\sqrt{8\ln 5/80} \approx 0{,}40$, le $\eta$ qui équilibre les deux termes pour 80 tours.

### Ex M14.15 — Chasse à l'erreur : P(X ≥ k) calculée comme P(X > k), des covariances oubliées, des poids non renormalisés

**Réponses** : a) `"ACDG"` · b) `0.9779` · c) `0.0812` · d) `0.625` · e) `[0.1427, 0.4857, 0.2873, 0.0844]`.

**Démarche.** (A) `binom.sf(k, n, p)` rend $P(X > 13) = P(X \ge 14) \approx 0{,}9031$ : il faut `binom.sf(k - 1, n, p)` ; (B), `binom.sf(15 - 1, n, p)`, est juste. (C) La borne de Chernoff de « au moins 4 serveurs en panne », pour $F = 16 - X$ de loi $\mathcal{B}(16 ;\ 0{,}07)$, est $e^{-16\,\mathrm{KL}(0{,}25 \Vert 0{,}07)}$ : la proportion de l'événement d'abord ; la ligne inverse les arguments et trouve $0{,}1695$. La probabilité exacte vaut $\approx 0{,}0221$ : pour $n = 16$, la borne reste près de quatre fois au-dessus. (D) oublie les covariances : $\frac{7{,}8}{16} = 0{,}4875$ au lieu de $\frac{10}{16}$, un nombre plausible sans aucun signal. (E) $\mathbf{w}^\top\mathbf{S}\mathbf{w}$ est juste ; (F) retranche le minimum, ce qui ne change pas les poids normalisés. (G) ne divise pas par la somme : les « poids » $(0{,}2938 ;\ 1 ;\ 0{,}5916 ;\ 0{,}1738)$ somment à $2{,}06$.

### Ex M14.16 — Un test qui vérifie que la borne de Chernoff majore la queue exacte de `scipy.stats`, sur une grille de n, p et a

**Vérification manuelle** : ✅ quand ton test passe sur la vraie borne avec au moins 100 cas (dont $a = 1$, des $p \le 0{,}05$ et $\ge 0{,}95$) et échoue, par un `assert`, sur chacune des quatre fausses bornes.

**Démarche.** Une grille de $n$ (de 1 à quelques centaines), de $p$ (dont 0,01 et 0,97) et de $a$ (dont 1), et quatre `assert` par cas : dans $[0, 1]$, au-dessus de la queue exacte, sous Hoeffding pour $a > p$, et pas plus grande pour $2n$ que pour $n$. Pour la copie : `bound_half` passe sous la queue exacte pour $a \le p$ (0,5 alors que la queue vaut presque 1) et pour $a = 1$, où la borne est exacte. `bound_squared` passe sous la queue pour $n = 1$, $p = 0{,}01$, $a = 0{,}7$ ($0{,}0053 < 0{,}01$). `bound_fixed_lambda` et `bound_markov` sont de **vraies** bornes (Markov vaut pour tout $\lambda > 0$, et pour $X$ lui-même), mais pas celles du contrat : la première rend $(1 - p + pe)^ne^{-na}$, plus que 1 dès que $a$ est petit (pour $a = 0$, $(1 + p(e - 1))^n > 1$) ; la seconde ne décroît pas avec $n$ et passe au-dessus de Hoeffding, par exemple pour $n = 3$, $p = 0{,}01$, $a = 0{,}9$ : $0{,}0111 > 0{,}0086$. Une grille utile contient les cas extrêmes.

**Erreurs fréquentes.** Une grille sans petits $n$ ni $p$ extrêmes, qui laisse passer `bound_squared` et `bound_markov` ; `math.ceil(n * a)` sans la petite marge, qui calcule parfois la mauvaise queue ; des comparaisons sans tolérance, qui peuvent échouer sur la vraie borne pour $a = 1$, où borne et queue valent toutes deux $p^n$ à un arrondi près.

### Ex M14.17 — Défi : suivre le meilleur de dix experts avec Hedge sans connaître l'horizon, un regret sous la borne théorique sur 1 000 tours

**Vérification** : `True` si ton regret est sous la borne aux tours 50, 200 et 1 000, sur les trois suites.

**Démarche.** Garder les losses cumulées et le numéro $t$ du tour qui vient ; `weights()` rend les poids $\propto e^{-\eta_t(L - \min L)}$ avec $\eta_t = \sqrt{8\ln K/t}$ ; `update` ajoute les losses et incrémente $t$. Pour la copie : les bornes valent $\approx 15{,}7$, $30{,}9$ et $68{,}4$. $\eta = 0{,}01$ réagit trop lentement : regret $\approx 31$ dès le tour 50 sur la suite stochastique. « Suivre le meneur » réussit les deux premières suites, mais la suite piège lui fait perdre 1 à chaque tour pendant que le meilleur expert ne perd qu'un tour sur deux : regret $\approx t/2$, 500 au tour 1 000. Le meilleur $\eta$ constant pour $T = 1\,000$, $\approx 0{,}136$, paie d'emblée $\frac{\ln K}{\eta} \approx 17$ : regret $\approx 17{,}0$ au tour 50, au-dessus de $15{,}7$. $\eta_t$ est grand au début (il suit vite le meilleur expert) et diminue ensuite (il ne suit plus les à-coups) : regrets $\approx 1{,}9$ (stochastique) et $\approx 0{,}8$ (changement) au tour 1 000, et $\approx 6{,}8$, $14{,}4$ et $33{,}1$ aux trois points de contrôle de la suite piège, tous sous la borne. Il ne dépend que du tour courant, jamais de $T$. Une autre solution : recommencer Hedge avec des horizons $1, 2, 4, 8, \ldots$ (le *doubling trick*), au prix d'un facteur constant sur la borne.

**Erreurs fréquentes.** Un $\eta$ qui dépend de $T$ (l'horizon n'est pas connu) ; des poids qui ne somment pas à 1 ; un $\eta_t$ calculé avec le nombre de tours joués, qui vaut 0 au premier appel (division par zéro) ; utiliser `hedge_weights` ou les suites de la vérification, interdits.
