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

### R3 · Fonctions

| Notion | Formule |
|---|---|
| droite par deux points | $m = \frac{y_2 - y_1}{x_2 - x_1}$ ($x_1 \ne x_2$) ; $c = y_1 - m x_1$ |
| normalisation min-max | $N(x) = \frac{x - \min}{\max - \min}$ ; réciproque $x = (\max - \min)N + \min$ |
| fonctions de référence | $x^2$ et $\lvert x \rvert$ : décroissantes sur $]-\infty \;;\; 0]$, croissantes sur $[0 \;;\; +\infty[$ ; $\frac{1}{x}$ : décroissante sur chaque morceau ; $\sqrt{x}$ : croissante |
| par morceaux | $\max(0, x)$ ; marche $H(x) = 0$ si $x < 0$, 1 si $x \ge 0$ (convention en 0) ; $\lvert x \rvert = \max(x, -x)$ |
| forme canonique | $ax^2 + bx + c = a(x - \alpha)^2 + \beta$, $\alpha = -\frac{b}{2a}$, $\beta = c - \frac{b^2}{4a}$ |
| discriminant | $\Delta = b^2 - 4ac$ ; $\Delta > 0$ : $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$ ; $\Delta = 0$ : $x_0 = -\frac{b}{2a}$ ; $\Delta < 0$ : aucune racine |
| factorisation | $a(x - x_1)(x - x_2)$ ; somme $x_1 + x_2 = -\frac{b}{a}$, produit $x_1 x_2 = \frac{c}{a}$ |
| signe d'un second degré | du signe de $a$, sauf strictement entre les racines |
| composition | $(f \circ g)(x) = f(g(x))$ ; en général $f \circ g \ne g \circ f$ |
| réciproque | $f^{-1}(f(x)) = x$, $f(f^{-1}(y)) = y$ ; courbes symétriques par rapport à $y = x$ |
| Horner | $a_n x^n + \dots + a_0 = (\cdots((a_n x + a_{n-1})x + a_{n-2})\cdots)x + a_0$ |

### R4 · Logique, ensembles, Σ et Π

| Notion | Formule |
|---|---|
| De Morgan | non (P et Q) = (non P) ou (non Q) ; non (P ou Q) = (non P) et (non Q) ; $\overline{A \cup B} = \bar{A} \cap \bar{B}$, $\overline{A \cap B} = \bar{A} \cup \bar{B}$ |
| implication | $P \Rightarrow Q$ fausse seulement si P vraie et Q fausse ; équivalente à (non P) ou Q et à sa contraposée $\text{non } Q \Rightarrow \text{non } P$ ; négation : P et non Q |
| quantificateurs | non ($\forall x$, P(x)) = $\exists x$, non P(x) ; non ($\exists x$, P(x)) = $\forall x$, non P(x) |
| cardinaux | $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert$ ; $\lvert \bar{A} \rvert = \lvert E \rvert - \lvert A \rvert$ ; $\lvert A \times B \rvert = \lvert A \rvert \times \lvert B \rvert$ |
| Σ | $\sum_{k=m}^{n}$ : $n - m + 1$ termes ; $\sum_{k=1}^{n} c = nc$ ; linéarité ; $\sum_{k=m}^{n} = \sum_{k=m}^{p} + \sum_{k=p+1}^{n}$ ; somme vide = 0 |
| sommes connues | $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ ; $\sum_{k=1}^{n} k(k + 1) = \frac{n(n+1)(n+2)}{3}$ ; télescopique $\sum_{k=1}^{n} (b_{k+1} - b_k) = b_{n+1} - b_1$ |
| Π | $\prod_{k=1}^{n} (c\,a_k) = c^n \prod a_k$ ; $n! = \prod_{k=1}^{n} k$ ; produit vide = 1 |
| récurrence | P(n₀) vraie et, pour tout $n \ge n_0$, $P(n) \Rightarrow P(n + 1)$ : P(n) vraie pour tout $n \ge n_0$ |

### R5 · Suites

| Notion | Formule |
|---|---|
| arithmétique | $u_{n+1} = u_n + r$ ; $u_n = u_0 + n\,r = u_p + (n - p)\,r$ |
| géométrique | $u_{n+1} = q\,u_n$ ; $u_n = u_0\,q^n = u_p\,q^{n-p}$ ; une hausse de $t\,\%$ multiplie par $1 + \frac{t}{100}$ |
| somme arithmétique | nombre de termes × $\frac{\text{premier} + \text{dernier}}{2}$ |
| somme géométrique | $n$ termes, raison $q \ne 1$ : premier × $\frac{1 - q^n}{1 - q}$ ; $q = 1$ : $n$ × premier |
| nombre de termes | $\sum_{k=m}^{n}$ : $n - m + 1$ termes |
| limite | $u_n \to \ell$ : $\forall \varepsilon > 0,\ \exists N,\ \forall n \ge N,\ \lvert u_n - \ell \rvert < \varepsilon$ |
| $q^n$ | $\to 0$ si $\lvert q \rvert < 1$ ; $= 1$ si $q = 1$ ; $\to +\infty$ si $q > 1$ ; pas de limite si $q \le -1$ |
| récurrence affine | $u_{n+1} = a\,u_n + b$ ($a \ne 1$) : $\ell = \frac{b}{1 - a}$, $u_n = \ell + (u_0 - \ell)\,a^n$ ; converge vers $\ell$ si $\lvert a \rvert < 1$ |
| somme infinie | $\lvert q \rvert < 1$ : $\sum_{k=0}^{+\infty} u_0\,q^k = \frac{u_0}{1 - q}$ |
| intérêts composés, actualisation | taux $t$ en décimal : $C_n = C_0\,(1 + t)^n$ ; valeur actuelle de $S$ dans $n$ ans : $\frac{S}{(1 + t)^n}$ |
| moyenne mobile | $m_t = \frac{1}{k}\sum_{j=t-k+1}^{t} x_j$ ; $N - k + 1$ moyennes pour $N$ valeurs |
| moyenne exponentielle | $v_0 = 0$, $v_t = \beta\,v_{t-1} + (1 - \beta)\,x_t$ ; poids $(1 - \beta)\,\beta^k$ pour la valeur d'âge $k$ |

### R6 · Exponentielle et logarithmes

| Notion | Formule |
|---|---|
| puissances réelles ($a, b > 0$) | $a^{p/q} = (\sqrt[q]{a})^p$ ; $a^{x+y} = a^x a^y$, $a^{-x} = \frac{1}{a^x}$, $(a^x)^y = a^{xy}$, $(ab)^x = a^x b^x$, $a^x > 0$ |
| nombre e | $e = \lim_{n \to +\infty} (1 + \frac{1}{n})^n \approx 2{,}718$ ; $\exp(x) = e^x$ ; $(1 + \frac{r}{n})^{nt} \to e^{rt}$ |
| ln | pour $x > 0$ : $e^y = x \iff y = \ln x$ ; $\ln(e^y) = y$, $e^{\ln x} = x$, $\ln 1 = 0$, $\ln e = 1$ |
| propriétés de ln ($a, b > 0$) | $\ln(ab) = \ln a + \ln b$, $\ln \frac{a}{b} = \ln a - \ln b$, $\ln(a^k) = k \ln a$, $\ln \sqrt{a} = \frac{1}{2} \ln a$ |
| équations, inéquations | $e^x = c \iff x = \ln c$ ($c > 0$) ; exp et ln gardent le sens des inégalités ; $q^n > c \iff n \ln q > \ln c$ (attention si $\ln q < 0$) |
| doublement, demi-vie | $\frac{\ln 2}{\ln(1 + r)}$ (règle de 70 : $\frac{70}{\text{taux en \%}}$) ; $\frac{\ln 0{,}5}{\ln(1 - r)}$ ; continu : $\frac{\ln 2}{r}$ |
| base b | $\log_b x = \frac{\ln x}{\ln b}$ ; chiffres de $N \ge 1$ : $\lfloor \log_{10} N \rfloor + 1$ |
| information | $-\log_2 p$ bits, $-\ln p$ nats ; 1 bit $= \ln 2 \approx 0{,}693$ nat ; $\lceil \log_2 N \rceil$ questions oui ou non |
| croissances comparées | $\frac{x^k}{a^x} \to 0$ ($a > 1$), $\frac{\ln x}{x^k} \to 0$ ($k > 0$) |
| échelles | position de $x$ sur un axe logarithmique : $\log_{10} x$ ; $C a^t$ droite en semi-log (pente $\log_{10} a$), $C x^k$ droite en log-log (pente $k$) ; décibels : $10 \log_{10} R$ |
| sigmoïde | $\sigma(x) = \frac{1}{1 + e^{-x}}$, $\sigma(0) = \frac{1}{2}$, $\sigma(-x) = 1 - \sigma(x)$ |
| cote, logit | cote $\frac{p}{1 - p}$ ; $\operatorname{logit}(p) = \ln \frac{p}{1 - p}$, réciproque de $\sigma$ |
| tanh | $\tanh x = \frac{e^x - e^{-x}}{e^x + e^{-x}} = 2\sigma(2x) - 1$, impaire, dans $]-1 \;;\; 1[$ |

### R7 · Limites et dérivation

| Notion | Formule |
|---|---|
| limites | formes indéterminées $\infty - \infty$, $\frac{\infty}{\infty}$, $0 \times \infty$, $\frac{0}{0}$ ; fraction de polynômes en $\pm\infty$ : le quotient des termes de plus haut degré |
| asymptotes | $\lim_{x \to \pm\infty} f(x) = L$ : $y = L$ ; $f(x) \to \pm\infty$ quand $x \to a$ : $x = a$ |
| continuité, valeurs intermédiaires | $\lim_{x \to a} f(x) = f(a)$ ; $f$ continue sur $[a ; b]$ et $f(a) f(b) < 0$ : un zéro entre $a$ et $b$ ; dichotomie : longueur $\frac{b - a}{2^n}$ après $n$ coupes |
| nombre dérivé, tangente | $f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$ ; $y = f(a) + f'(a)(x - a)$ ; $f(a + h) \approx f(a) + f'(a)\,h$ |
| dérivées usuelles | $(x^n)' = nx^{n-1}$, $(\frac{1}{x})' = -\frac{1}{x^2}$, $(\sqrt{x})' = \frac{1}{2\sqrt{x}}$, $(e^x)' = e^x$, $(\ln x)' = \frac{1}{x}$, $(a^x)' = a^x \ln a$ |
| règles | $(u + v)' = u' + v'$, $(ku)' = ku'$, $(uv)' = u'v + uv'$, $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$, $(\frac{1}{v})' = -\frac{v'}{v^2}$ |
| règle de la chaîne | $(g(u))' = g'(u) \times u'$ ; $(u^n)' = nu^{n-1}u'$, $(e^u)' = u'e^u$, $(\ln u)' = \frac{u'}{u}$, $(\sqrt{u})' = \frac{u'}{2\sqrt{u}}$ |
| variations, extremums | $f' > 0$ : croissante ; $f' < 0$ : décroissante ; extremum intérieur : $f' = 0$ et $f'$ change de signe ; comparer aussi les bords |
| approximations en 0 | $e^h \approx 1 + h$, $\ln(1 + h) \approx h$ |
| grand O | $f = O(g)$ : $\lvert f \rvert \le C \lvert g \rvert$ pour $n$ assez grand ; $1 \ll \log n \ll n \ll n \log n \ll n^2 \ll 2^n$ |

### R8 · Probabilités de base

| Notion | Formules |
|---|---|
| événements | contraire $\bar{A}$, « et » $A \cap B$, « ou » $A \cup B$ ; incompatibles : $A \cap B = \varnothing$ ; « ni $A$ ni $B$ » $= \overline{A \cup B}$ |
| probabilité | $P(A) = \sum_{\omega \in A} p(\omega)$ ; équiprobabilité : $P(A) = \frac{\lvert A \rvert}{\lvert \Omega \rvert}$ ; $P(\bar{A}) = 1 - P(A)$ |
| réunion | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ($= P(A) + P(B)$ si incompatibles) |
| dénombrer | principe multiplicatif ; $n^k$ suites avec répétition ; $\frac{n!}{(n - k)!}$ arrangements ; $n!$ rangements ; $\binom{n}{k} = \frac{n!}{k!\,(n - k)!}$ choix sans ordre |
| coefficients binomiaux | $\binom{n}{k} = \binom{n}{n - k}$, $\binom{n}{2} = \frac{n(n - 1)}{2}$, $\binom{n}{k} = \binom{n - 1}{k - 1} + \binom{n - 1}{k}$, $\sum_k \binom{n}{k} = 2^n$ |
| arbre pondéré | branches d'un nœud de somme 1 ; chemin : produit ; événement : somme des chemins ; $P(A \cap B) = P(A)\,P(B \mid A)$ |
| indépendance | $P(A \cap B) = P(A)\,P(B)$ ; au moins une réussite en $n$ essais indépendants : $1 - (1 - p)^n$ |
| espérance | $\mathbb{E}[X] = \sum x\,P(X = x)$ ; $\mathbb{E}[aX + b] = a\,\mathbb{E}[X] + b$ ; $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ |
| variance | $\mathbb{V}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - \mathbb{E}[X]^2$ ; $\sigma = \sqrt{\mathbb{V}(X)}$ ; $\mathbb{V}(aX + b) = a^2\,\mathbb{V}(X)$ |
| loi des grands nombres | la fréquence se rapproche de la probabilité ; écarts en $\frac{1}{\sqrt{n}}$ |

### R9 · Géométrie du plan, vecteurs et trigonométrie

| Notion | Formules |
|---|---|
| distance et milieu | $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$ ; milieu $\left(\frac{x_A + x_B}{2} ; \frac{y_A + y_B}{2}\right)$ |
| vecteurs | $\overrightarrow{AB} = (x_B - x_A ; y_B - y_A)$ ; $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ ; $ABCD$ parallélogramme $\iff \overrightarrow{AB} = \overrightarrow{DC}$ ; colinéaires $\iff xy' - x'y = 0$ |
| norme | $\lVert \vec{u} \rVert = \sqrt{x^2 + y^2}$ ; $\lVert k\vec{u} \rVert = \lvert k \rvert\,\lVert \vec{u} \rVert$ ; $\lVert \vec{u} + \vec{v} \rVert \le \lVert \vec{u} \rVert + \lVert \vec{v} \rVert$ ; unitaire $\frac{\vec{u}}{\lVert \vec{u} \rVert}$ ; $\lVert \vec{u} \rVert_1 = \sum \lvert x_i \rvert$, $\lVert \vec{u} \rVert_\infty = \max \lvert x_i \rvert$ |
| droites | $y = mx + p$, $m = \frac{y_B - y_A}{x_B - x_A}$ ; $ax + by + c = 0$ : $(-b ; a)$ directeur, $(a ; b)$ normal ; points $A + t\,\vec{d}$ |
| produit scalaire | $\vec{u} \cdot \vec{v} = xx' + yy' = \lVert \vec{u} \rVert\,\lVert \vec{v} \rVert\cos\theta$ ; $\vec{u} \cdot \vec{u} = \lVert \vec{u} \rVert^2$ ; $\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0$ ; projection $\frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert^2}\vec{u}$ |
| radians | $180° = \pi$ rad ; $\theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180}$ |
| cosinus et sinus | $M(\theta) = (\cos\theta ; \sin\theta)$ ; $\cos^2\theta + \sin^2\theta = 1$ ; $\cos 0, \frac{\pi}{6}, \frac{\pi}{4}, \frac{\pi}{3}, \frac{\pi}{2}$ : $1, \frac{\sqrt{3}}{2}, \frac{\sqrt{2}}{2}, \frac{1}{2}, 0$ (sinus : à l'envers) |
| symétries, période | $\cos(-\theta) = \cos\theta$, $\sin(-\theta) = -\sin\theta$ ; $\cos(\pi - \theta) = -\cos\theta$, $\sin(\pi - \theta) = \sin\theta$ ; période $2\pi$, et $\frac{2\pi}{\omega}$ pour $\cos(\omega t)$ ; $\sin' = \cos$, $\cos' = -\sin$ |
| angle | $\cos\theta = \frac{\vec{u} \cdot \vec{v}}{\lVert \vec{u} \rVert\,\lVert \vec{v} \rVert}$ (similarité cosinus), $\theta = \arccos(\ldots) \in [0 ; \pi]$ ; Al-Kashi : $c^2 = a^2 + b^2 - 2ab\cos\hat{C}$ |
| dimension $n$ | $\lVert \mathbf{x} \rVert = \sqrt{\sum x_i^2}$, $\mathbf{x} \cdot \mathbf{y} = \sum x_i y_i$, $d(\mathbf{x}, \mathbf{y}) = \lVert \mathbf{x} - \mathbf{y} \rVert$ |

## Partie I · Fondations

### M02a · Intégrales et densités

| Notion | Formules |
|---|---|
| sommes de Riemann | $h = \frac{b - a}{n}$, $x_i = a + ih$ ; $L_n = h\sum_{i=0}^{n-1} f(x_i)$, $R_n = h\sum_{i=1}^{n} f(x_i)$, $M_n = h\sum_{i=0}^{n-1} f\big(x_i + \frac{h}{2}\big)$ ; $\int_a^b f = \lim L_n$ |
| primitives | $x^n \to \frac{x^{n+1}}{n+1}$ ($n \ne -1$) ; $\frac{1}{x} \to \ln\lvert x \rvert$ ; $e^{ax} \to \frac{e^{ax}}{a}$ ; $\cos \to \sin$ ; $\sin \to -\cos$ ; $f(ax + b) \to \frac{1}{a}F(ax + b)$ |
| théorème fondamental | $\int_a^b f(x)\,dx = \big[F(x)\big]_a^b = F(b) - F(a)$ ; $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$ |
| règles | linéarité ; Chasles $\int_a^b + \int_b^c = \int_a^c$ ; $\int_b^a = -\int_a^b$ ; aire entre deux courbes $\int_a^b (g - f)$ si $f \le g$ |
| par parties | $\int_a^b u\,v' = \big[uv\big]_a^b - \int_a^b u'\,v$ |
| changement de variable | $\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$ |
| intégrales impropres | $\int_1^{+\infty} \frac{dx}{x^p}$ converge $\iff p > 1$ (et vaut $\frac{1}{p - 1}$) ; $\int_0^1 \frac{dx}{x^p}$ converge $\iff p < 1$ ; $\int_0^{+\infty} e^{-\lambda x}\,dx = \frac{1}{\lambda}$ |
| Gauss | $\int_{-\infty}^{+\infty} e^{-x^2}\,dx = \sqrt{\pi}$ ; $\int_{-\infty}^{+\infty} e^{-t^2/2}\,dt = \sqrt{2\pi}$ |
| méthodes numériques | trapèzes $h\big(\frac{f_0}{2} + f_1 + \cdots + f_{n-1} + \frac{f_n}{2}\big)$ ; Simpson ($n$ pair) $\frac{h}{3}(f_0 + 4f_1 + 2f_2 + \cdots + 4f_{n-1} + f_n)$ ; erreurs en $h$, $h^2$ (milieu, trapèzes), $h^4$ (Simpson) |
| densité | $f \ge 0$, $\int_{-\infty}^{+\infty} f = 1$, $P(a \le X \le b) = \int_a^b f$ ; $P(X = a) = 0$ ; $P(x \le X \le x + h) \approx f(x)\,h$ |
| fonction de répartition | $F(x) = P(X \le x) = \int_{-\infty}^x f$ ; $F' = f$ ; $P(a < X \le b) = F(b) - F(a)$ |
| quantiles | $q_p$ : le plus petit $x$ tel que $F(x) \ge p$ ; médiane $q_{0{,}5}$ ; percentile $k$ : $q_{k/100}$ ; densité $\lambda e^{-\lambda t}$ : $F(t) = 1 - e^{-\lambda t}$, $q_p = -\frac{\ln(1 - p)}{\lambda}$ |
| AUC, valeur moyenne | $\text{AUC} = \int_0^1 \text{TPR}\,d(\text{FPR})$ ; $\bar{f} = \frac{1}{b - a}\int_a^b f$ |

### M02b · Variables aléatoires et lois usuelles

| Notion | Formules |
|---|---|
| variable aléatoire, loi | $X : \Omega \to \mathbb{R}$ ; loi : $P(X \in B)$ ; $F(x) = P(X \le x)$ (escalier pour une loi discrète, continue pour une densité) |
| lois discrètes | Bernoulli $P(X = 1) = p$ ; binomiale $\binom{n}{k}p^k(1-p)^{n-k}$ ; géométrique $(1-p)^{k-1}p$, $P(X > k) = (1-p)^k$ ; Poisson $e^{-\lambda}\frac{\lambda^k}{k!}$ ; catégorielle $p_1, \ldots, p_K$ de somme 1 |
| lois continues | uniforme $\frac{1}{b - a}$ sur $[a ; b]$ ; exponentielle $\lambda e^{-\lambda t}$, $P(T > t) = e^{-\lambda t}$ ; normale $\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ |
| loi normale | $Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1)$ ; $P(X \le x) = \Phi\big(\frac{x - \mu}{\sigma}\big)$ ; $\Phi(-z) = 1 - \Phi(z)$ ; $\Phi(z) = \frac{1}{2}\big(1 + \operatorname{erf}\frac{z}{\sqrt{2}}\big)$ ; $\Phi(1{,}96) \approx 0{,}975$ |
| espérance, transfert | $\mathbb{E}[X] = \sum x\,P(X = x)$ ou $\int x\,f(x)\,dx$ ; $\mathbb{E}[g(X)] = \sum g(x)\,P(X = x)$ ou $\int g(x)\,f(x)\,dx$ |
| variance | $\mathbb{V}(X) = \mathbb{E}[(X - \mu)^2] = \mathbb{E}[X^2] - \mu^2$ ; $\mathbb{V}(aX + b) = a^2\,\mathbb{V}(X)$ ; $\sigma(X) = \sqrt{\mathbb{V}(X)}$ |
| espérances et variances usuelles | Bernoulli $p$, $p(1-p)$ ; binomiale $np$, $np(1-p)$ ; géométrique $\frac{1}{p}$, $\frac{1-p}{p^2}$ ; Poisson $\lambda$, $\lambda$ ; uniforme $\frac{a+b}{2}$, $\frac{(b-a)^2}{12}$ ; exponentielle $\frac{1}{\lambda}$, $\frac{1}{\lambda^2}$ ; normale $\mu$, $\sigma^2$ |
| couples | marginale $P(X = x) = \sum_y P(X = x, Y = y)$, $f_X(x) = \int f(x, y)\,dy$ ; indépendance : $P(X = x, Y = y) = P(X = x)P(Y = y)$, et alors $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$ |
| sommes | $\mathbb{E}[aX + bY + c] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y] + c$ ; $\mathbb{V}(X + Y) = \mathbb{V}(X) + \mathbb{V}(Y) + 2\operatorname{Cov}(X, Y)$ ; indépendantes : $\mathbb{V}(X \pm Y) = \mathbb{V}(X) + \mathbb{V}(Y)$ ; moyenne i.i.d. : $\mathbb{V}(\bar{X}) = \frac{\sigma^2}{n}$ |
| sommes de lois | $\mathcal{P}(\lambda) + \mathcal{P}(\mu) = \mathcal{P}(\lambda + \mu)$ ; $\mathcal{N}(\mu_1, \sigma_1^2) + \mathcal{N}(\mu_2, \sigma_2^2) = \mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ (indépendantes) ; $\mathcal{B}(n, \frac{\lambda}{n}) \to \mathcal{P}(\lambda)$ |
| intégrale double | $\iint_{[a ; b] \times [c ; d]} f = \int_a^b \big(\int_c^d f(x, y)\,dy\big)dx$ ; produit : $\iint g(x)h(y) = \int g \times \int h$ ; polaires : $dx\,dy = r\,dr\,d\theta$ |
| changement de variable | $Y = aX + b$ : $f_Y(y) = \frac{1}{\lvert a \rvert}f_X\big(\frac{y - b}{a}\big)$ ; $g$ monotone : $f_Y(y) = f_X(g^{-1}(y))\,\lvert (g^{-1})'(y) \rvert$ ; $X = \mu + \sigma Z$ |
| simulation | $U \sim \mathcal{U}([0 ; 1])$ : $F^{-1}(U)$ suit la loi de $F$ ; exponentielle $-\frac{\ln(1 - U)}{\lambda}$ ; discrète : segments de longueurs $p_k$, bornes aux sommes cumulées |

### M02c · Échantillons et estimation

| Notion | Formules |
|---|---|
| position | $\bar{x} = \frac{1}{n}\sum x_i$ ; médiane : la valeur du milieu de la série triée ; $\sum (x_i - c)^2 = \sum (x_i - \bar{x})^2 + n(\bar{x} - c)^2$ (la moyenne minimise la somme des carrés, la médiane celle des écarts absolus) |
| dispersion | $s_n^2 = \frac{1}{n}\sum (x_i - \bar{x})^2 = \overline{x^2} - \bar{x}^2$ (`ddof=0`) ; $s^2 = \frac{1}{n - 1}\sum (x_i - \bar{x})^2 = \frac{n}{n - 1}s_n^2$ (`ddof=1`) ; $y = ax + b$ : $\bar{y} = a\bar{x} + b$, $s_y = \lvert a \rvert s_x$ |
| quantiles d'une série | série triée $x_{(0)} \le \cdots \le x_{(n-1)}$, position $h = p(n - 1)$, $q_p = x_{(k)} + (h - k)(x_{(k+1)} - x_{(k)})$ avec $k = \lfloor h \rfloor$ ; $\text{EI} = Q_3 - Q_1$ |
| valeurs aberrantes | $z = \frac{x - \bar{x}}{s}$, signal si $\lvert z \rvert > 3$ ; Tukey : hors de $[Q_1 - 1{,}5\,\text{EI} ;\ Q_3 + 1{,}5\,\text{EI}]$ ; avec $n$ valeurs, $\lvert z \rvert \le \sqrt{n - 1}$ (avec $s_n$) |
| échantillon i.i.d. | $\mathbb{E}[\bar{X}_n] = \mu$, $\mathbb{V}(\bar{X}_n) = \frac{\sigma^2}{n}$, $\sigma(\bar{X}_n) = \frac{\sigma}{\sqrt{n}}$ ; sans remise : $\operatorname{Cov}(X_i, X_j) = -\frac{\sigma^2}{N - 1}$, $\mathbb{V}(\bar{X}) = \frac{\sigma^2}{n}\cdot\frac{N - n}{N - 1}$ |
| inégalités | Markov : $P(X \ge a) \le \frac{\mathbb{E}[X]}{a}$ ($X \ge 0$) ; Bienaymé-Tchebychev : $P(\lvert X - \mu \rvert \ge \varepsilon) \le \frac{\sigma^2}{\varepsilon^2}$ ; pour la moyenne : $\le \frac{\sigma^2}{n\varepsilon^2}$ |
| théorème central limite | $\bar{X}_n \approx \mathcal{N}\big(\mu, \frac{\sigma^2}{n}\big)$, $S_n \approx \mathcal{N}(n\mu, n\sigma^2)$ ; proportion : $\hat{p} \approx \mathcal{N}\big(p, \frac{p(1 - p)}{n}\big)$ |
| estimateurs | $\text{biais} = \mathbb{E}[\hat{\theta}] - \theta$ ; $\text{EQM} = \mathbb{E}[(\hat{\theta} - \theta)^2] = \text{biais}^2 + \mathbb{V}(\hat{\theta})$ ; $\mathbb{E}[S_n^2] = \frac{n - 1}{n}\sigma^2$, $\mathbb{E}[S^2] = \sigma^2$ ; données normales : $\mathbb{V}(S^2) = \frac{2\sigma^4}{n - 1}$ |
| erreur type, intervalle | $\text{SE} = \frac{s}{\sqrt{n}}$ ; intervalle à 95 % : $\bar{x} \pm 1{,}96\,\text{SE}$ ($z$ = 1,645 à 90 %, 2,576 à 99 %) ; proportion : $\hat{p} \pm 1{,}96\sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$ ; taille : $n \ge \big(\frac{z\sigma}{E}\big)^2$ |
| bootstrap | $B$ rééchantillons de $n$ valeurs tirées avec remise ; erreur type : l'écart-type des $B$ valeurs ; intervalle à 95 % : leurs percentiles 2,5 et 97,5 |
| covariance, corrélation | $\operatorname{Cov}(x, y) = \frac{1}{n}\sum (x_i - \bar{x})(y_i - \bar{y}) = \overline{xy} - \bar{x}\bar{y}$ ; $r = \frac{\operatorname{Cov}(x, y)}{s_x s_y} \in [-1 ; 1]$ ; $\operatorname{Cov}(aX + b, cY + d) = ac\operatorname{Cov}(X, Y)$ |
| variance d'une combinaison | $\mathbb{V}(aX + bY) = a^2\mathbb{V}(X) + b^2\mathbb{V}(Y) + 2ab\operatorname{Cov}(X, Y)$ ; $\mathbb{V}\big(\sum_i w_iX_i\big) = \sum_i\sum_j w_iw_j\Sigma_{ij}$, $\Sigma_{ij} = \operatorname{Cov}(X_i, X_j)$ |
| imputation | par la moyenne de $m$ valeurs observées sur $n$ : moyenne inchangée, variance multipliée par $\frac{m}{n}$ |
| grande dimension | cube $[-1 ; 1]^d$ : part à moins de $\varepsilon$ du bord $1 - (1 - \varepsilon)^d$ ; boule inscrite $\frac{\pi}{4}$ ($d = 2$), $\frac{\pi}{6}$ ($d = 3$) ; $\mathbf{X} \sim \mathcal{N}(0, 1)^d$ : $\mathbb{E}\lVert \mathbf{X} \rVert^2 = d$ |

### M03 · Probabilités conditionnelles

| Notion | Formules |
|---|---|
| tableau de contingence | jointe : case / total ; marginale : total de ligne (ou de colonne) / total ; $P(X = x) = \sum_y P(X = x, Y = y)$ (règle de la somme) |
| probabilité conditionnelle | $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ($P(B) > 0$) : une case divisée par le total de sa ligne ou de sa colonne ; $P(A \mid B) \ne P(B \mid A)$ en général |
| règle du produit | $P(A \cap B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A)$ ; $P(A \cap B \cap C) = P(A)\,P(B \mid A)\,P(C \mid A \cap B)$ |
| indépendance | $P(A \cap B) = P(A)\,P(B) \iff P(A \mid B) = P(A)$ ; variables : chaque case $=$ produit des marginales ; effectif attendu $= \frac{\text{ligne} \times \text{colonne}}{\text{total}}$ |
| probabilités totales | $B_1, \ldots, B_K$ partition : $P(A) = \sum_k P(A \mid B_k)\,P(B_k)$ (un taux global est une moyenne pondérée des taux par groupe) |
| matrice de confusion | prévalence $\pi = P(Y = 1)$ ; recall $= P(\hat{Y} = 1 \mid Y = 1) = \frac{TP}{TP + FN}$ ; spécificité $= \frac{TN}{TN + FP}$ ; FPR $= \frac{FP}{FP + TN}$ ; precision $= \frac{TP}{TP + FP}$ ; NPV $= \frac{TN}{TN + FN}$ ; accuracy $= \frac{TP + TN}{n}$ |
| F-beta | $F_\beta = \frac{(1 + \beta^2)PR}{\beta^2 P + R} = \frac{(1 + \beta^2)TP}{(1 + \beta^2)TP + \beta^2 FN + FP}$ ; $F_1 = \frac{2PR}{P + R}$ ; poids du recall $\frac{\beta^2}{1 + \beta^2}$ |
| moyennes multiclasses | macro : moyenne simple des classes ; pondérée : par les effectifs ; micro : sur les comptages additionnés (micro-P $=$ micro-R $=$ accuracy, un seul label par exemple) |
| balanced accuracy, MCC | BA $=$ moyenne des recalls (binaire : $\frac{\text{recall} + \text{spécificité}}{2}$) ; MCC $= \frac{TP \cdot TN - FP \cdot FN}{\sqrt{(TP + FP)(TP + FN)(TN + FP)(TN + FN)}}$ |
| prévalence | precision $= \frac{r\pi}{r\pi + (1 - s)(1 - \pi)}$ ; `class_weight="balanced"` : $w_k = \frac{n}{K\,n_k}$ |
| seuil de décision | probabilités calibrées : positif si $p > \frac{c_{FP}}{c_{FP} + c_{FN}}$ |
| AUC | aire sous la courbe ROC (points (FPR, recall)) $= \frac{\#\{s_+ > s_-\} + \frac{1}{2}\#\{s_+ = s_-\}}{n_+ n_-} = P(S_+ > S_-) + \frac{1}{2}P(S_+ = S_-)$ ; inchangée par une fonction strictement croissante ; $1 - $ AUC pour $-s$ |
| average precision | $\text{AP} = \sum_j (R_j - R_{j-1})\,P_j$, aux seuils décroissants ($R_0 = 0$) ; hasard : la prévalence |
| calibration, Brier | calibré : $P(Y = 1 \mid \text{score} = p) = p$ ; $\text{Brier} = \frac{1}{n}\sum (p_i - y_i)^2$ ; prévision constante $\pi$ : $\pi(1 - \pi)$ |
| taux par groupe | $\text{FPR} = \frac{\pi}{1 - \pi}\cdot\frac{1 - \text{PPV}}{\text{PPV}}\cdot\text{recall}$ : prévalences différentes, impossible d'égaliser PPV, recall et FPR à la fois (sauf cas extrêmes, sans faux positif) |

### M04 · Bayes, vraisemblance et loi Beta

| Notion | Formules |
|---|---|
| formule de Bayes | $P(H \mid O) = \frac{P(O \mid H)\,P(H)}{P(O)}$, évidence $P(O) = \sum_j P(O \mid H_j)\,P(H_j)$ ; a posteriori $\propto$ vraisemblance × a priori |
| mises à jour successives | l'a posteriori devient l'a priori ; observations indépendantes sachant l'hypothèse : $P(H \mid O_1, \ldots, O_m) \propto P(H)\prod_i P(O_i \mid H)$, dans n'importe quel ordre ; rapport de deux hypothèses multiplié par $\frac{P(O \mid H_1)}{P(O \mid H_2)}$ à chaque observation |
| vraisemblance | $L(\theta) = \prod_i p(x_i \mid \theta)$, $\ell(\theta) = \ln L(\theta) = \sum_i \ln p(x_i \mid \theta)$ ; maximum de vraisemblance : $\ell'(\theta) = 0$ et $\ell'' < 0$ |
| maximums de vraisemblance usuels | Bernoulli : $\hat{\theta} = \frac{k}{n}$ ; exponentielle : $\hat{\lambda} = \frac{n}{\sum_i x_i} = \frac{1}{\bar{x}}$ ; Poisson : $\hat{\mu} = \bar{x}$ |
| fonctions Gamma et Beta | $\Gamma(n) = (n - 1)!$, $\Gamma(x + 1) = x\,\Gamma(x)$, $\Gamma(\frac{1}{2}) = \sqrt{\pi}$ ; $B(a, b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a + b)} = \int_0^1 \theta^{a - 1}(1 - \theta)^{b - 1}\,d\theta$ ; $\ln B$ par `math.lgamma` ou `scipy.special.betaln` |
| loi Beta | densité $\frac{\theta^{a - 1}(1 - \theta)^{b - 1}}{B(a, b)}$ sur $[0, 1]$ ; moyenne $\frac{a}{a + b}$ ; variance $\frac{ab}{(a + b)^2(a + b + 1)}$ ; mode $\frac{a - 1}{a + b - 2}$ si $a, b > 1$ (0 si la densité décroît, 1 si elle croît) ; $\mathrm{Beta}(1, 1)$ uniforme |
| conjugaison Beta-binomiale | a priori $\mathrm{Beta}(a, b)$, $k$ succès et $n - k$ échecs : a posteriori $\mathrm{Beta}(a + k,\ b + n - k)$ ; moyenne a posteriori $\frac{a + k}{a + b + n} = \frac{a + b}{a + b + n}\cdot\frac{a}{a + b} + \frac{n}{a + b + n}\cdot\frac{k}{n}$ |
| lissage de Laplace | $\frac{k + 1}{n + 2}$ ; $K$ catégories : $\frac{n_j + 1}{n + K}$ ; additif : $\frac{n_j + \alpha}{n + K\alpha}$ |
| loi prédictive | succès suivant : $\frac{a}{a + b}$ ; $k$ succès dans les $n$ prochains essais : $\binom{n}{k}\frac{B(a + k,\ b + n - k)}{B(a, b)}$ |
| MAP | $\hat{\theta}_{\text{MAP}} = \arg\max_\theta f(\theta \mid \text{données})$ ; Beta-binomial : $\frac{a + k - 1}{a + b + n - 2}$ ; avec $\mathrm{Beta}(1, 1)$, le maximum de vraisemblance |
| intervalle de crédibilité | à 95 % à queues égales : $[F^{-1}(0{,}025) ;\ F^{-1}(0{,}975)]$ de l'a posteriori ; largeur $\approx 2 \times 1{,}96\sqrt{\frac{\hat{\theta}(1 - \hat{\theta})}{n}}$ pour $n$ grand |
| log-sum-exp | $\ln\sum_j e^{\ell_j} = m + \ln\sum_j e^{\ell_j - m}$, $m = \max_j \ell_j$ ; probabilités : $\frac{e^{\ell_j - m}}{\sum_i e^{\ell_i - m}}$ ; plus petit `float64` positif $\approx 5 \times 10^{-324}$ |
| famille exponentielle | $p(x \mid \eta) = h(x)\exp\big(\eta\,T(x) - A(\eta)\big)$ ; Bernoulli : $\eta = \ln\frac{\theta}{1 - \theta}$, $T(x) = x$, $A(\eta) = \ln(1 + e^\eta)$ |

### M05a · Dérivées, Taylor et calcul numérique

| Notion | Formules |
|---|---|
| dérivée seconde et convexité | $f'' \ge 0$ sur $I$ $\iff$ $f$ convexe sur $I$ ; alors $f(x) \ge f(c) + f'(c)(x - c)$ (tangente au-dessous) ; point d'inflexion : $f''$ change de signe |
| extrema | intérieur : $f'(c) = 0$ ; $f''(c) > 0$ minimum local, $f''(c) < 0$ maximum local, $f''(c) = 0$ on ne conclut pas ; sur $[a, b]$ : comparer les points critiques et les bords ; $f$ convexe : un point critique est un minimum global |
| polynôme de Taylor | $P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x - a)^k$ ; reste de Lagrange : $\lvert f(x) - P_n(x) \rvert \le \frac{M}{(n+1)!}\lvert x - a \rvert^{n+1}$ si $\lvert f^{(n+1)} \rvert \le M$ entre $a$ et $x$ |
| développements en 0 | $e^x = \sum_k \frac{x^k}{k!}$ ; $\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \cdots$ ; $\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$ ; $\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ ($-1 < x \le 1$) ; $\frac{1}{1 - x} = 1 + x + x^2 + \cdots$ ($\lvert x \rvert < 1$) ; $\sqrt{1 + x} \approx 1 + \frac{x}{2} - \frac{x^2}{8}$ |
| méthode de Newton | $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$ ; racine simple : $e_{k+1} \approx \frac{f''(r)}{2f'(r)}e_k^2$ (quadratique) ; racine double : linéaire ; $\sqrt{c}$ : $x_{k+1} = \frac{1}{2}\big(x_k + \frac{c}{x_k}\big)$ |
| différences finies | avant $\frac{f(x + h) - f(x)}{h}$ : erreur $\approx \frac{h}{2}f''(x)$ ; centrée $\frac{f(x + h) - f(x - h)}{2h}$ : $\approx \frac{h^2}{6}f'''(x)$ ; seconde $\frac{f(x + h) - 2f(x) + f(x - h)}{h^2}$ : $\approx \frac{h^2}{12}f^{(4)}(x)$ ; Richardson $\frac{4D(h/2) - D(h)}{3}$ : ordre 4 |
| flottants | `float64` : $\pm 1{,}b_1 \ldots b_{52} \times 2^e$, $\varepsilon = 2^{-52} \approx 2{,}2 \times 10^{-16}$, $u = \frac{\varepsilon}{2}$ ; `float32` : $\varepsilon = 2^{-23}$ ; `float16` : $2^{-10}$ ; écart entre $2^e$ et $2^{e+1}$ : $2^e\varepsilon$ ; entiers exacts jusqu'à $2^{53}$ ; $\text{fl}(a \circ b) = (a \circ b)(1 + \delta)$, $\lvert \delta \rvert \le u$ |
| meilleur pas | $E(h) \le \frac{M_3}{6}h^2 + \frac{\delta}{h}$ (centrée) : $h^* = \big(\frac{3\delta}{M_3}\big)^{1/3}$, $E^* \propto \delta^{2/3}$ ; $E(h) \le \frac{M_2}{2}h + \frac{2\delta}{h}$ (avant) : $h^* = 2\sqrt{\frac{\delta}{M_2}}$, $E^* = 2\sqrt{M_2\delta}$ |
| overflow, underflow | `float64` : $e^x$ déborde pour $x > 709{,}78$ ; plus grand $\approx 1{,}8 \times 10^{308}$ ; plus petit normal $\approx 2{,}2 \times 10^{-308}$, sous-normal $\approx 5 \times 10^{-324}$ |
| log-sum-exp et softmax | $\text{LSE}(\mathbf{v}) = m + \ln\sum_i e^{v_i - m}$, $m = \max_i v_i$ ; $m \le \text{LSE}(\mathbf{v}) \le m + \ln n$ ; $\text{softmax}(\mathbf{v})_i = \frac{e^{v_i - m}}{\sum_j e^{v_j - m}}$ ; $\ln\text{softmax}(\mathbf{v})_i = v_i - \text{LSE}(\mathbf{v})$ |

### M05b · Fonctions de plusieurs variables et gradient

| Notion | Formules |
|---|---|
| ligne de niveau | $\{(x, y) : f(x, y) = c\}$ ; deux lignes de valeurs différentes ne se croisent pas ; écart entre deux lignes voisines $\approx \frac{\Delta c}{\lVert \nabla f \rVert}$ |
| dérivée partielle | $\frac{\partial f}{\partial x}(a, b)$ : la dérivée de $x \mapsto f(x, b)$ en $a$ ; différence centrée $\frac{f(\mathbf{p} + h\mathbf{e}_i) - f(\mathbf{p} - h\mathbf{e}_i)}{2h}$ |
| gradient | $\nabla f = \big(\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\big)$ (en colonne ici, en ligne dans MML) |
| règle de la chaîne | $\frac{d}{dt} f\big(x(t), y(t)\big) = f_x\,x'(t) + f_y\,y'(t)$ |
| dérivée directionnelle | $D_{\mathbf{u}} f(\mathbf{p}) = \nabla f(\mathbf{p}) \cdot \mathbf{u} = \lVert \nabla f(\mathbf{p}) \rVert \cos\theta$, avec $\lVert \mathbf{u} \rVert = 1$ |
| plus grande pente | montée la plus raide : $\frac{\nabla f}{\lVert \nabla f \rVert}$, de pente $\lVert \nabla f \rVert$ ; descente : $-\nabla f$ ; pente nulle à angle droit du gradient, le long de la ligne de niveau |
| plan tangent | $z = f(a, b) + f_x(a, b)\,(x - a) + f_y(a, b)\,(y - b)$ ; développé : $A = f_x$, $B = f_y$, $C = f(a, b) - Aa - Bb$ ; $f(\mathbf{p} + \mathbf{h}) \approx f(\mathbf{p}) + \nabla f(\mathbf{p}) \cdot \mathbf{h}$, erreur d'ordre 2 |
| dérivées secondes | $f_{xx}$, $f_{yy}$, $f_{xy} = f_{yx}$ (Schwarz) ; courbure dans la direction $\mathbf{u}$ : $f_{xx}u_1^2 + 2f_{xy}u_1u_2 + f_{yy}u_2^2$ |
| test du second ordre | en un point critique ($\nabla f = \mathbf{0}$), $D = f_{xx}f_{yy} - f_{xy}^2$ : $D > 0$ et $f_{xx} > 0$ minimum local ; $D > 0$ et $f_{xx} < 0$ maximum local ; $D < 0$ point selle ; $D = 0$ on ne conclut pas |
| descente de gradient | $\mathbf{x}_{k+1} = \mathbf{x}_k - \eta\,\nabla f(\mathbf{x}_k)$ ; au premier ordre $f(\mathbf{x} - \eta\nabla f) \approx f(\mathbf{x}) - \eta\,\lVert \nabla f(\mathbf{x}) \rVert^2$ ; montée : $\mathbf{x} + \eta\,\nabla f$ |

### M06 · Théorie de l'information

| Notion | Formules |
|---|---|
| information | $-\log_2 p$ bits, ou $-\ln p$ nats ; 1 bit $= \ln 2 \approx 0{,}693$ nat, 1 nat $\approx 1{,}443$ bit ; pour des événements indépendants, les informations s'additionnent |
| entropie | $H(p) = -\sum p_i \log_2 p_i = \mathbb{E}[-\log_2 p(X)]$, avec $0 \log 0 = 0$ ; $0 \le H(p) \le \log_2 n$, le maximum pour la loi uniforme |
| conjointe, conditionnelle | $H(X, Y) = -\sum p(x, y) \log_2 p(x, y)$ ; $H(Y \mid X) = \sum_x p(x)\,H(Y \mid X = x)$, où la loi de $Y$ sachant $X = x$ est la ligne $x$ divisée par $p(x)$ |
| règle de la chaîne | $H(X, Y) = H(X) + H(Y \mid X) = H(Y) + H(X \mid Y)$ ; $H(Y \mid X) \le H(Y)$ et $H(X, Y) \le H(X) + H(Y)$, égalités pour des variables indépendantes |
| regroupement | regrouper des issues en une seule, de probabilité $s$ : $H(X) = H(G) + s\,H(\text{loi des issues regroupées, divisées par } s)$ |
| information mutuelle | $I(X ; Y) = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X) = H(X) + H(Y) - H(X, Y) = D_{\mathrm{KL}}(p_{XY} \parallel p_X\,p_Y) \ge 0$ ; nulle si et seulement si $X$ et $Y$ sont indépendantes ; $I(X ; X) = H(X)$ |
| cross-entropy, KL | $H(p, q) = -\sum p_i \log_2 q_i$ ; $D_{\mathrm{KL}}(p \parallel q) = \sum p_i \log_2 \frac{p_i}{q_i} = H(p, q) - H(p) \ge 0$ (Gibbs), nulle si et seulement si $p = q$ ; pas symétrique ; infinie si $q_i = 0$ là où $p_i > 0$ |
| log loss, perplexité | log loss $= \frac{1}{n}\sum_k -\ln \hat{p}_k$, où $\hat{p}_k$ est la probabilité donnée à la vraie classe de l'exemple $k$ (en nats) ; perplexité $2^{H(p, q)}$ (en bits) |
| inégalité de Jensen | $f$ convexe : $f(\mathbb{E}[X]) \le \mathbb{E}[f(X)]$ ; $f$ concave : l'inverse ; pour $f$ strictement convexe, égalité seulement si $X$ est constante ; $f(x) = x^2$ : l'écart est la variance |
| Jensen-Shannon | $\mathrm{JS}(p, q) = \frac{1}{2}D_{\mathrm{KL}}(p \parallel m) + \frac{1}{2}D_{\mathrm{KL}}(q \parallel m)$, avec $m = \frac{p + q}{2}$ : symétrique, finie, nulle si et seulement si $p = q$ |
| codes | longueur fixe : $\lceil \log_2 N \rceil$ bits pour $N$ issues ; code préfixe : Kraft $\sum_i D^{-\ell_i} \le 1$ ($D = 2$ en binaire), et réciproquement ; $\bar{L} = \sum p_i \ell_i \ge H(p)$ ; longueurs de Shannon $\lceil -\log_2 p_i \rceil$ : $\bar{L} < H(p) + 1$ |
| estimer une entropie | l'estimateur plug-in (les fréquences) a un biais $\approx -\frac{k - 1}{2n\ln 2}$ bit pour $k$ issues et $n$ observations ; correction de Miller-Madow : ajouter $\frac{m - 1}{2n\ln 2}$, où $m$ est le nombre de valeurs différentes observées |

## Partie II · Concepts

### M07 · Vecteurs et géométrie de ℝⁿ

| Notion | Formules |
|---|---|
| opérations | coordonnée par coordonnée : $\mathbf{u} + \mathbf{v} = (u_i + v_i)_i$, $\lambda\mathbf{u} = (\lambda u_i)_i$ ; base canonique : $\mathbf{x} = \sum_i x_i\,\mathbf{e}_i$ ; one-hot de la catégorie $k$ : $\mathbf{e}_k$ |
| produit scalaire | $\mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i = \mathbf{u}^\top\mathbf{v}$ ; symétrique, linéaire par rapport à chaque vecteur ; $\mathbf{u} \cdot \mathbf{u} = \lVert \mathbf{u} \rVert^2 \ge 0$, nul seulement pour $\mathbf{u} = \mathbf{0}$ ; $\mathbf{e}_i \cdot \mathbf{x} = x_i$ |
| développements | $\lVert \mathbf{u} \pm \mathbf{v} \rVert^2 = \lVert \mathbf{u} \rVert^2 \pm 2\,\mathbf{u} \cdot \mathbf{v} + \lVert \mathbf{v} \rVert^2$ ; $\mathbf{u} \cdot \mathbf{v} = \frac{1}{4}\big(\lVert \mathbf{u} + \mathbf{v} \rVert^2 - \lVert \mathbf{u} - \mathbf{v} \rVert^2\big)$ ; Pythagore : $\mathbf{u} \perp \mathbf{v} \Rightarrow \lVert \mathbf{u} + \mathbf{v} \rVert^2 = \lVert \mathbf{u} \rVert^2 + \lVert \mathbf{v} \rVert^2$ |
| neurone | $z = \mathbf{w} \cdot \mathbf{x} + b$ ; augmenter $x_j$ de $\delta$ change $z$ de $w_j\,\delta$ |
| normes | $\lVert \mathbf{x} \rVert_1 = \sum_i \lvert x_i \rvert$, $\lVert \mathbf{x} \rVert_2 = \sqrt{\sum_i x_i^2}$, $\lVert \mathbf{x} \rVert_\infty = \max_i \lvert x_i \rvert$, $\lVert \mathbf{x} \rVert_p = \big(\sum_i \lvert x_i \rvert^p\big)^{1/p}$ ($p \ge 1$) ; positivité, homogénéité $\lVert \lambda\mathbf{x} \rVert = \lvert \lambda \rvert\,\lVert \mathbf{x} \rVert$, inégalité triangulaire ; $\lVert \mathbf{x} \rVert_\infty \le \lVert \mathbf{x} \rVert_2 \le \lVert \mathbf{x} \rVert_1 \le \sqrt{n}\,\lVert \mathbf{x} \rVert_2$ |
| distances | $d_p(\mathbf{x}, \mathbf{y}) = \lVert \mathbf{x} - \mathbf{y} \rVert_p$ ; inégalité triangulaire renversée : $\big\lvert \lVert \mathbf{u} \rVert - \lVert \mathbf{v} \rVert \big\rvert \le \lVert \mathbf{u} - \mathbf{v} \rVert$ |
| Cauchy-Schwarz | $\lvert \mathbf{u} \cdot \mathbf{v} \rvert \le \lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert$, égalité si et seulement si $\mathbf{u}$ et $\mathbf{v}$ sont colinéaires |
| angle, cosinus | $\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert\,\lVert \mathbf{v} \rVert} \in [-1, 1]$, $\theta \in [0, \pi]$ ; distance cosinus $1 - \cos\theta$ ; vecteurs unitaires : $\lVert \mathbf{u} - \mathbf{v} \rVert^2 = 2 - 2\,\mathbf{u} \cdot \mathbf{v} = 2(1 - \cos\theta)$ |
| projection sur une droite | $\mathbf{p} = \frac{\mathbf{x} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\,\mathbf{u}$ (ne dépend que de la droite) ; $\mathbf{x} - \mathbf{p} \perp \mathbf{u}$ ; $\lVert \mathbf{x} \rVert^2 = \lVert \mathbf{p} \rVert^2 + \lVert \mathbf{x} - \mathbf{p} \rVert^2$ ; composante le long de $\mathbf{u}$ : $\frac{\mathbf{x} \cdot \mathbf{u}}{\lVert \mathbf{u} \rVert}$ |
| hyperplan | $H : \mathbf{w} \cdot \mathbf{x} + b = 0$ ($\mathbf{w} \ne \mathbf{0}$, vecteur normal) ; côté : le signe de $\mathbf{w} \cdot \mathbf{x} + b$ ; distance signée $\frac{\mathbf{w} \cdot \mathbf{x} + b}{\lVert \mathbf{w} \rVert}$, distance $\frac{\lvert \mathbf{w} \cdot \mathbf{x} + b \rvert}{\lVert \mathbf{w} \rVert}$ ; point le plus proche $\mathbf{x} - \frac{\mathbf{w} \cdot \mathbf{x} + b}{\lVert \mathbf{w} \rVert^2}\,\mathbf{w}$ ; hyperplans parallèles : $\frac{\lvert b_1 - b_2 \rvert}{\lVert \mathbf{w} \rVert}$ |
| barycentre, inertie | $\bar{\mathbf{x}} = \frac{1}{m}\sum_i \mathbf{x}_i$, pondéré $\frac{\sum_i \omega_i \mathbf{x}_i}{\Omega}$ avec $\Omega = \sum_i \omega_i$ ; König-Huygens : $\sum_i \omega_i \lVert \mathbf{x}_i - \mathbf{c} \rVert^2 = \sum_i \omega_i \lVert \mathbf{x}_i - \bar{\mathbf{x}}_\omega \rVert^2 + \Omega\,\lVert \bar{\mathbf{x}}_\omega - \mathbf{c} \rVert^2$, minimum unique en $\mathbf{c} = \bar{\mathbf{x}}_\omega$ |
| centres et distances | somme des carrés des distances L2 : le barycentre ; somme des distances L1 : la médiane coordonnée par coordonnée ; somme des distances L2 (non au carré) : la médiane géométrique (Weiszfeld : $\mathbf{c} \leftarrow \frac{\sum_i \mathbf{x}_i / d_i}{\sum_i 1 / d_i}$, $d_i = \lVert \mathbf{x}_i - \mathbf{c} \rVert$) |
| k-means | inertie $J = \sum_i \lVert \mathbf{x}_i - \boldsymbol{\mu}_{c_i} \rVert^2$ ; affectation au centre le plus proche, puis chaque centre au barycentre de son cluster : $J$ ne remonte jamais, arrêt en un nombre fini d'étapes, sur un minimum local ; k-means++ : tirer un point avec la probabilité $\frac{D(\mathbf{x})^2}{\sum D^2}$ |
| silhouette | $a(i)$ : distance moyenne aux autres points du cluster ; $b(i)$ : distance moyenne aux points du cluster voisin le plus proche ; $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))} \in [-1, 1]$, 0 pour un point seul dans son cluster |
| grande dimension | $\lVert \mathbf{1} \rVert = \sqrt{n}$ ; $\cos(\mathbf{1}, \mathbf{e}_1) = \frac{1}{\sqrt{n}}$ ; deux directions gaussiennes au hasard : $\cos\theta$ d'écart-type $\approx \frac{1}{\sqrt{n}}$ ; pour $\mathbf{X} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ : $\mathbb{E}\big[\lVert \mathbf{X} \rVert^2\big] = n$, $\mathbb{V}\big(\lVert \mathbf{X} \rVert^2\big) = 2n$ (avec $\mathbb{E}[Z^4] = 3$), donc $\lVert \mathbf{X} \rVert \approx \sqrt{n}$ à environ $\frac{1}{\sqrt{2}} \approx 0{,}71$ près |

### M08 · Tests statistiques

| Notion | Formules |
|---|---|
| p-valeur | $p = P_{H_0}(T \text{ au moins aussi extrême que } t_{\text{obs}})$ ; rejeter $H_0$ si $p \le \alpha$ ; sous $H_0$, une p-valeur continue suit la loi uniforme sur $[0, 1]$ ($P(P \le u) = u$), une p-valeur discrète vérifie $P(P \le u) \le u$ |
| test binomial exact | $K \sim \mathcal{B}(n, p_0)$ sous $H_0$ ; unilatéral : $P(K \ge k)$ ou $P(K \le k)$ ; bilatéral : $\sum_{j : P(K = j) \le P(K = k)} P(K = j)$ (le double de l'unilatéral si $p_0 = \frac{1}{2}$) ; approximation normale : $z = \frac{k - np_0}{\sqrt{np_0(1 - p_0)}}$ |
| test par permutation | $t = \bar{x} - \bar{y}$ ; exact : la part des $\binom{m + n}{m}$ répartitions au moins aussi extrêmes ; tiré au hasard : $\frac{C + 1}{B + 1}$ ; apparié : changer au hasard le signe de chaque différence ; importance par permutation : score − score après mélange de la colonne |
| erreurs et puissance | $\alpha = P_{H_0}(\text{rejeter})$, $\beta = P_{H_1}(\text{ne pas rejeter})$, puissance $1 - \beta$ ; test sur une moyenne : $1 - \beta = \Phi\big(\frac{\delta\sqrt{n}}{\sigma} - z_{1-\alpha}\big)$ et $n \ge \Big(\frac{(z_{1-\alpha} + z_{1-\beta})\,\sigma}{\delta}\Big)^2$ ($z_{1-\alpha/2}$ en bilatéral) ; deux groupes de $n$ : $\delta\sqrt{n/2}$ |
| proportion | Wald : $\hat{p} \pm z\sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$ ; Wilson : $\frac{\hat{p} + \frac{z^2}{2n} \pm z\sqrt{\frac{\hat{p}(1 - \hat{p})}{n} + \frac{z^2}{4n^2}}}{1 + \frac{z^2}{n}}$, pour $k = 0$ : $\big[0 ;\ \frac{z^2}{n + z^2}\big]$ ; $z = z_{(1 + \text{niveau})/2}$ |
| différence appariée | $d_i = a_i - b_i$ : $\bar{d} \pm t_{n-1}\,\frac{s_d}{\sqrt{n}}$ ($s_d$ en $\mathrm{ddof} = 1$) ; il exclut 0 exactement quand le test de Student apparié bilatéral a $p < 1 - \text{niveau}$ |
| comparaisons multiples | $m$ tests vrais au seuil $\alpha$ : $m\alpha$ faux positifs en moyenne, $1 - (1 - \alpha)^m$ d'en avoir au moins un (tests indépendants) ; Boole : $P(\bigcup A_i) \le \sum P(A_i)$ ; Bonferroni : seuil $\frac{\alpha}{m}$, ou $\min(1, m\,p_i) \le \alpha$ |
| sélection de modèle | $\mathrm{AIC} = 2k - 2\ln L$, $\mathrm{BIC} = k\ln n - 2\ln L$ (le plus petit gagne) ; $\mathrm{BF}_{12} = \frac{p(\mathcal{D} \mid M_1)}{p(\mathcal{D} \mid M_2)}$, cote a posteriori = $\mathrm{BF}_{12}$ × cote a priori ; loi a priori uniforme sur $p$ : $p(k \text{ succès sur } n) = \frac{1}{n + 1}$ ; $-\frac{1}{2}\mathrm{BIC} \approx \ln p(\mathcal{D} \mid M)$ pour $n$ grand |

### M09a · Matrices et systèmes linéaires

| Notion | Formules |
|---|---|
| formes | $(n, p) \times (p, m) \to (n, m)$ ; $\mathbf{A}\mathbf{x}$ a autant de coordonnées que $\mathbf{A}$ a de lignes ; un dataset : $(n, p)$, une ligne par exemple |
| produit matrice-vecteur | $(\mathbf{A}\mathbf{x})_i = \sum_j a_{ij}x_j$ (lignes) $= x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n$ (colonnes) ; $\mathbf{A}\mathbf{e}_j = \mathbf{a}_j$ ; prédictions $\hat{\mathbf{y}} = \mathbf{X}\mathbf{w} + b$ |
| produit matriciel | $(\mathbf{A}\mathbf{B})_{ij} = \sum_k a_{ik}b_{kj}$ ; associatif, distributif, pas commutatif ; $\mathbf{I}\mathbf{A} = \mathbf{A}\mathbf{I} = \mathbf{A}$ ; coût $n\,p\,m$ multiplications, $n^3$ pour des carrées |
| Hadamard | $(\mathbf{A} \odot \mathbf{B})_{ij} = a_{ij}b_{ij}$ (même forme) ; `A * B` contre `A @ B` |
| couche, embedding | $\mathbf{Z} = \mathbf{X}\mathbf{W} + \mathbf{b}$, $\mathbf{X}$ $(n, d_{\text{in}})$, $\mathbf{W}$ $(d_{\text{in}}, d_{\text{out}})$, $\mathbf{Z}$ $(n, d_{\text{out}})$, $d_{\text{in}}d_{\text{out}} + d_{\text{out}}$ paramètres ; PyTorch : $\mathbf{X}\mathbf{W}^\top + \mathbf{b}$ ; embedding : $\mathbf{e}_k^\top\mathbf{E}$ = ligne $k$ de $\mathbf{E}$ |
| transposée | $(\mathbf{A}^\top)_{ij} = a_{ji}$ ; $(\mathbf{A}^\top)^\top = \mathbf{A}$, $(\mathbf{A} + \mathbf{B})^\top = \mathbf{A}^\top + \mathbf{B}^\top$, $(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top\mathbf{A}^\top$ ; $\mathbf{X}^\top\mathbf{X}$ $(p, p)$ symétrique, $(\mathbf{X}^\top\mathbf{X})_{ij}$ = produit scalaire des colonnes $i$ et $j$ |
| systèmes | 0, 1 ou une infinité de solutions ; solution générale = solution particulière + solutions de $\mathbf{A}\mathbf{h} = \mathbf{0}$ ; opérations élémentaires : $L_i \leftrightarrow L_j$, $L_i \leftarrow \lambda L_i$ ($\lambda \ne 0$), $L_i \leftarrow L_i + \lambda L_j$ ; pivot de Gauss $\approx \frac{2}{3}n^3$ opérations |
| inverse | $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$ ; $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ ; $(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$, $(\mathbf{A}^\top)^{-1} = (\mathbf{A}^{-1})^\top$, $(\lambda\mathbf{A})^{-1} = \frac{1}{\lambda}\mathbf{A}^{-1}$ ; Gauss-Jordan : $[\mathbf{A} \mid \mathbf{I}] \to [\mathbf{I} \mid \mathbf{A}^{-1}]$ |
| rang | $\operatorname{rg}(\mathbf{A})$ = nombre de pivots $\le \min(m, n)$ ; carrée de taille $n$ : inversible $\iff \operatorname{rg} = n$ ; système : aucune solution si $\operatorname{rg}([\mathbf{A} \mid \mathbf{b}]) > \operatorname{rg}(\mathbf{A})$, sinon $n - \operatorname{rg}(\mathbf{A})$ paramètres libres |

### M09b · Moindres carrés et régularisation

| Notion | Formules |
|---|---|
| losses | $\mathbf{r} = \mathbf{y} - \hat{\mathbf{y}}$ ; $\mathrm{MSE} = \frac{1}{n}\sum r_i^2$, $\mathrm{RMSE} = \sqrt{\mathrm{MSE}}$, $\mathrm{MAE} = \frac{1}{n}\sum \lvert r_i \rvert$ ; Huber : $\frac{r^2}{2}$ si $\lvert r \rvert \le \delta$, $\delta(\lvert r \rvert - \frac{\delta}{2})$ sinon |
| $R^2$ | $\mathrm{SCT} = \sum (y_i - \bar{y})^2$, $\mathrm{SCE} = \sum (\hat{y}_i - \bar{y})^2$, $\mathrm{SCR} = \sum r_i^2$ ; $R^2 = 1 - \frac{\mathrm{SCR}}{\mathrm{SCT}}$ ; $\mathrm{SCT} = \mathrm{SCE} + \mathrm{SCR}$ pour les moindres carrés avec une colonne de 1 |
| gradients | $\nabla(\mathbf{a}^\top\mathbf{w}) = \mathbf{a}$ ; $\nabla(\mathbf{w}^\top\mathbf{A}\mathbf{w}) = (\mathbf{A} + \mathbf{A}^\top)\mathbf{w}$ ($2\mathbf{A}\mathbf{w}$ si symétrique) ; $\nabla\lVert \mathbf{y} - \mathbf{X}\mathbf{w} \rVert^2 = -2\mathbf{X}^\top(\mathbf{y} - \mathbf{X}\mathbf{w})$ ; $\nabla\mathrm{MSE} = -\frac{2}{n}\mathbf{X}^\top\mathbf{r}$ |
| équations normales | $\mathbf{X}^\top\mathbf{X}\,\mathbf{w} = \mathbf{X}^\top\mathbf{y}$ ; unique si $\mathbf{X}$ est de rang $p$ ; $\mathbf{X}^\top\mathbf{r} = \mathbf{0}$ ; colonne de 1 : $\sum r_i = 0$ et la droite passe par $(\bar{x}, \bar{y})$ |
| matrice chapeau | $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top$, $\hat{\mathbf{y}} = \mathbf{H}\mathbf{y}$ ; $\mathbf{H}^\top = \mathbf{H}$, $\mathbf{H}\mathbf{H} = \mathbf{H}$, $\operatorname{tr}\mathbf{H} = p$, $\mathbf{H}\mathbf{X} = \mathbf{X}$ ; $\mathbf{r} = (\mathbf{I} - \mathbf{H})\mathbf{y}$ |
| features polynomiales | $\binom{p + d}{d}$ monômes de degré au plus $d$ en $p$ variables, constante comprise ; $\binom{k + p - 1}{k}$ de degré exactement $k$ |
| ridge | $(\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})\mathbf{w} = \mathbf{X}^\top\mathbf{y}$, inversible pour $\lambda > 0$ ; weight decay : $\mathbf{w} \leftarrow (1 - 2\eta\lambda)\mathbf{w} - \eta\nabla L$ ; MAP : $\lambda = \frac{\sigma^2}{\tau^2}$ ; colonnes orthogonales : facteur $\frac{\lVert \mathbf{x}_j \rVert^2}{\lVert \mathbf{x}_j \rVert^2 + \lambda}$ |
| lasso | pénalité $\lambda\lVert \mathbf{w} \rVert_1$ ; seuillage doux $S(z, \gamma) = \operatorname{signe}(z)\max(\lvert z \rvert - \gamma, 0)$ |
| vraisemblance | $\ln L = -\frac{n}{2}\ln(2\pi\sigma^2) - \frac{\mathrm{SCR}}{2\sigma^2}$ : $\hat{\mathbf{w}}$ = moindres carrés, $\hat{\sigma}^2 = \frac{\mathrm{SCR}}{n}$ (sans biais : $\frac{\mathrm{SCR}}{n - p}$) ; bruit de Laplace : minimiser $\sum \lvert r_i \rvert$ |
| biais et variance | $\mathbb{E}[(\hat{\theta} - \theta)^2] = (\mathbb{E}[\hat{\theta}] - \theta)^2 + \mathbb{V}(\hat{\theta})$ ; $\mathbb{E}[(y - \hat{f}_D(x))^2] = \text{biais}^2 + \text{variance} + \sigma^2$ ; $c\,\bar{x}$ : $c^* = \frac{\mu^2}{\mu^2 + \sigma^2/n}$ |

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
