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

*(R7 à R9 ajoutés avec leurs chapitres)*

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
