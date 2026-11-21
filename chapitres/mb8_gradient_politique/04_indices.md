# MB8 · Gradient de politique — indices

> **Mode d'emploi.** Cherche d'abord seul pendant 15 minutes. Si tu bloques, ouvre **l'indice 1** (la direction), cherche encore 5 minutes, puis l'indice 2 (la méthode), puis l'indice 3 (presque la solution). Ouvrir un indice n'est pas un échec : c'est ne pas chercher avant qui en est un. Note dans ton journal les exercices où tu as eu besoin de l'indice 3 : ce sont eux qu'il faudra refaire dans une semaine.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 Pont](#pont) · [🗣️ Explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### MB8.Q1 — La fonction score : espérance nulle, information de Fisher, support qui dépend du paramètre, et dériver une espérance par le score ou par le chemin

<details><summary>Indice 1</summary>

Fiche §1 : « Dériver par rapport au paramètre », « Une espérance nulle », « L'information de Fisher » et « La KL de deux lois voisines » ; §2 : « Le score contre le chemin ».

</details>
<details><summary>Indice 2</summary>

Écris $\ln p_\theta(x)$, puis dérive en $\theta$, $x$ restant fixé. $I(\theta) = \mathbb{V}(s_\theta) = -\mathbb{E}[\partial^2_\theta\ln p_\theta]$ ; $\mathrm{KL}(p_\theta \,\|\, p_{\theta'}) \approx \frac12I(\theta)(\theta' - \theta)^2$. L'erreur type d'une moyenne de $n$ tirages indépendants est $\frac{\sigma}{\sqrt n}$. Pour 5, regarde comment $X = F_\theta^{-1}(U)$ varie avec $\theta$, $U$ restant fixé.

</details>
<details><summary>Indice 3</summary>

1. $\ln p_\theta(x) = -\frac{(x - \theta)^2}{8} + \text{constante}$. 3. Où vit le support, et qu'a supposé la fiche pour écrire $\mathbb{E}[s_\theta] = 0$ ? 2. $I(0{,}5) = \frac{10}{0{,}25}$, et $\theta' - \theta = 0{,}02$. 4. Résous $\frac{1{,}44}{n} = 0{,}05^2$. 5. À $U$ fixé, quelles valeurs prend $X$ quand $\theta$ varie un peu ? $\mathbb{E}_\theta[X^2] = \mathbb{V}(X) + \mathbb{E}[X]^2$.

</details>

### MB8.Q2 — Variables de contrôle et baselines : ce qui garde l'espérance, ce qui réduit la variance, ce qui biaise

<details><summary>Indice 1</summary>

Fiche §3 : « Une variable de contrôle », « Une baseline pour l'estimateur score » et « Des baselines tirées de l'échantillon ».

</details>
<details><summary>Indice 2</summary>

$c^\star = \frac{\operatorname{Cov}(f, h)}{\mathbb{V}(h)}$, et la variance devient $(1 - \rho^2)\,\mathbb{V}(f) = \mathbb{V}(f) - \frac{\operatorname{Cov}(f, h)^2}{\mathbb{V}(h)}$. Une baseline constante ne change l'espérance que de $b\,\mathbb{E}[s]$. La moyenne des autres valeurs ne dépend pas du tirage ; la moyenne du batch, si.

</details>
<details><summary>Indice 3</summary>

1. $\frac54$, puis $10 - \frac{25}{4}$. 2. $\rho^2 = 0{,}81$. 3. $\mathbb{E}[s] = 0$ ; la variance est un trinôme en $b$ (fiche §3). 4. Écris $\bar f$ avec $f(x_i)$ et la moyenne $b_i$ des sept autres : $f(x_i) - \bar f = \ ? \times (f(x_i) - b_i)$. 5. Que vaut $\mathbb{E}[f - c\,(h - m)]$ si $m \ne \mathbb{E}[h]$ ?

</details>

### MB8.Q3 — Le gradient de la valeur d'une politique et le λ-retour : la loi d'occupation actualisée, l'avantage d'espérance nulle, le poids de chaque retour à k pas

<details><summary>Indice 1</summary>

Fiche §4 : « Rappel de M26 : une politique et ses valeurs » et « Dériver le système de Bellman » ; §5 : « Le λ-retour » et « Ce que vaut un retour, en moyenne ».

</details>
<details><summary>Indice 2</summary>

$V(s) = \sum_a\pi(a \mid s)\,Q(s, a)$ et $A = Q - V$. $\mathbf{M} = \sum_t\gamma^t\mathbf{P}_\pi^t$, et un état visité au pas $t$ pèse $(1 - \gamma)\gamma^t$ dans $\boldsymbol\nu_{s_0}$. Le retour à $k$ pas pèse $(1 - \lambda)\lambda^{k-1}$ dans le λ-retour. Avec des valeurs fausses de $\mathbf{e}$, le retour à $k$ pas a le biais $\gamma^k(\mathbf{P}_\pi^k\mathbf{e})(s)$.

</details>
<details><summary>Indice 3</summary>

1. $0{,}5 + 0{,}6 + 0{,}6$, puis les trois différences. 2. $\sum_t\gamma^t = \frac{1}{1 - \gamma}$ ; $(1 - 0{,}6) \times 0{,}6^3$. 3. Les retours de plus de $k$ pas pèsent ensemble $\lambda^k$ : calcule les puissances successives de $0{,}6$, puis de $0{,}7$, jusqu'à passer sous $0{,}1$. 4. Quel facteur de la formule de la fiche s'annule ? 5. $\mathbf{e} = \mathbf{0}$.

</details>

### MB8.Q4 — Échantillonnage d'importance et KL estimée : support, taille effective, poids tronqués, k₁ ou k₃

<details><summary>Indice 1</summary>

Fiche §6 : « Changer de loi », « Normaliser, mesurer, tronquer » et « Estimer une KL par échantillons ».

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}_q[wf] = \int_{q > 0}p\,f$. La taille effective vaut $\frac{(\sum_iw_i)^2}{\sum_iw_i^2}$. $\min(w, c) \le w$. $k_1 = -\ln w$ et $k_3 = (w - 1) - \ln w$.

</details>
<details><summary>Indice 3</summary>

1. Les tirages de $q$ tombent-ils dans $[0, 1]$ ? Compare $\int_{q > 0}p\,f$ et $\int p\,f$. 2. $\frac{6^2}{9 + 1 + 1 + 1}$ ; puis un facteur commun au numérateur et au dénominateur. 3. Si un poids dépasse $c$ là où $f > 0$, l'espérance bouge-t-elle ? 4. $\ln 1{,}55 \approx 0{,}438$ ; pour le signe de $k_3$, la tangente de $\ln$ en 1.

</details>

### MB8.Q5 — Bradley-Terry et Elo : ce que les forces identifient, quand elles existent, ce que fait une mise à jour

<details><summary>Indice 1</summary>

Fiche §7 : « Le modèle », « Quand les forces existent » et « La cote Elo ».

</details>
<details><summary>Indice 2</summary>

$\sigma(\beta_i - \beta_j)$ ne dépend que des différences de forces. Les forces existent si et seulement si le graphe des victoires est fortement connexe ; elles vérifient alors « victoires observées = victoires attendues ». Elo : $R_i \leftarrow R_i + k\,(S - E)$, avec $E = \frac{1}{1 + 10^{(R_j - R_i)/400}}$.

</details>
<details><summary>Indice 3</summary>

1. Remplace chaque $\beta_i$ par $\beta_i + t$. 2. Suis les flèches A → B → C → A ; avec des forces égales, chaque joueur attend $2 \times \frac12$ victoire. 3. $S = 0$ et $E = 0{,}64$. 4. $10^{-400/400}$.

</details>

### MB8.Q6 — Le principe de Gibbs : la loi optimale, ses limites en β, et ce que mesure β ln Z

<details><summary>Indice 1</summary>

Fiche §8 : « Un compromis » et « Les deux limites ».

</details>
<details><summary>Indice 2</summary>

$\pi^\star \propto \pi_{\mathrm{ref}}\,e^{r/\beta}$, et le maximum de $F$ vaut $\beta\ln Z$. Quand $\beta \to 0$, $e^{r/\beta}$ est dominé par la plus grande satisfaction ; quand $\beta \to +\infty$, $e^{r/\beta} \to 1$.

</details>
<details><summary>Indice 3</summary>

1. $e^{r/\beta} = e^{r\ln 2} = 2^r$, puis normalise. 3. Un facteur nul reste nul. 4. $F(\pi) = \beta\ln Z - \beta\,\mathrm{KL}(\pi \,\|\, \pi^\star)$ : compare avec $F(\pi_{\mathrm{ref}})$ et avec $F$ d'une loi concentrée sur la meilleure issue.

</details>

<a id="rappels"></a>

## 🔁 Rappels

### MB8.R1 — La jacobienne de la softmax, diag(p) − ppᵀ, lue comme la covariance d'un vecteur one-hot, et la loi de Boltzmann (M17)

<details><summary>Indice 1</summary>

M17 §7 (la loi de Boltzmann et la jacobienne de la softmax) ; fiche §4 : « Une politique softmax tabulaire ».

</details>
<details><summary>Indice 2</summary>

$\frac{\partial p_i}{\partial z_j} = p_i(\mathbf{1}\{i = j\} - p_j)$. Pour un vecteur à une seule coordonnée égale à 1 : $Y_iY_j = 0$ si $i \ne j$, et $Y_i^2 = Y_i$. La loi de Boltzmann : $p_i \propto e^{-E_i/T}$.

</details>
<details><summary>Indice 3</summary>

1. La diagonale $p_i(1 - p_i)$ : $0{,}6 \times 0{,}4 = 0{,}24$ ; hors de la diagonale, $-p_ip_j$ : $-0{,}6 \times 0{,}1 = -0{,}06$ ; complète. 2. Que deviennent les $p_i$ si l'on ajoute un même nombre $t$ à tous les logits ? Dérive en $t$. 3. $\operatorname{Cov}(\mathbf{Y}) = \mathbb{E}[\mathbf{Y}\mathbf{Y}^\top] - \mathbb{E}[\mathbf{Y}]\,\mathbb{E}[\mathbf{Y}]^\top$. 4. $e^0$, $e^{-1{,}5}$, $e^{-3}$, puis divise par leur somme.

</details>

### MB8.R2 — Le système de Bellman d'une politique fixée, la loi d'occupation actualisée et le télescopage des erreurs TD (M26)

<details><summary>Indice 1</summary>

M26 §5 (le système de Bellman, la loi d'occupation actualisée) et §8 (l'erreur TD, le télescopage) ; fiche §4 et §5.

</details>
<details><summary>Indice 2</summary>

$(\mathbf{I} - \gamma\mathbf{P}_\pi)\,\mathbf{V} = \mathbf{r}_\pi$ ; $\boldsymbol\nu_0 = (1 - \gamma) \times$ la ligne 0 de $\mathbf{M}$ ; $\mathbb{E}[\delta_t \mid S_t = 0] = r_\pi(0) + \gamma\,(\mathbf{P}_\pi\mathbf{W})(0) - W(0)$.

</details>
<details><summary>Indice 3</summary>

1. $\mathbf{I} - 0{,}6\,\mathbf{P}_\pi = \begin{pmatrix} 0{,}58 & -0{,}18 \\ -0{,}12 & 0{,}52 \end{pmatrix}$, de déterminant $0{,}28$ ; l'inverse d'une matrice $2 \times 2$. 2. La ligne 0 de $\mathbf{M}$ : $\frac{(0{,}52 ;\ 0{,}18)}{0{,}28}$. 3. $8 + 0{,}6\,(0{,}7 \times 16 + 0{,}3 \times 5) - 16$. 4. Écris chaque $\delta_{t+k}$, multiplie par $\gamma^k$ et somme : les termes en $W$ se compensent deux à deux.

</details>

### MB8.R3 — La dérivée par le chemin, son hypothèse de domination, et l'indicatrice où elle échoue (M25b)

<details><summary>Indice 1</summary>

M25b §7 (la dérivée par le chemin et son hypothèse de domination) ; fiche §2 : « Le score contre le chemin ».

</details>
<details><summary>Indice 2</summary>

Dérive $(\theta + U)^2$ en $\theta$, $U$ restant fixé, puis prends l'espérance. La domination : un majorant intégrable des taux d'accroissement, le même pour tous les $\theta$ voisins de $1{,}5$. $P_\theta(X > 2) = P(U > 2 - \theta)$.

</details>
<details><summary>Indice 3</summary>

1. $\mathbb{E}[2(\theta + U)] = 2\theta + 1$ ; et $\mathbb{E}_\theta[X^2] = \theta^2 + \theta + \frac13$. 3. Pour $1 \le \theta \le 2$, $P(U > 2 - \theta) = \theta - 1$. Que vaut la dérivée en $\theta$ de $\mathbf{1}\{\theta + u > 2\}$, $u$ fixé, hors du saut ?

</details>

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex MB8.1 — Une attente au téléphone de loi exponentielle de taux θ, et une pénalité au-delà de c minutes : d/dθ P(X > c) par la formule fermée, par l'estimateur score (son espérance calculée) et par le chemin X = ξ/θ ; la variance de l'estimateur score à un tirage

<details><summary>Indice 1</summary>

Fiche §2 : « La méthode du score » et « Le score contre le chemin » ; M02b (la loi exponentielle, l'absence de mémoire) ; M25b §7.

</details>
<details><summary>Indice 2</summary>

$s_\theta(x) = \frac1\theta - x$ et $P(X > c) = e^{-\theta c}$. $\mathbb{E}[g(X)] = \frac1\theta P(X > c) - \mathbb{E}[X\,\mathbf{1}\{X > c\}]$ ; sachant $X > c$, $X - c$ suit encore la loi exponentielle de taux $\theta$. Par le chemin, dérive $\frac\xi\theta$ en $\theta$, $\xi$ restant fixé. Pour e), écris $X = c + Y$ sachant $X > c$.

</details>
<details><summary>Indice 3</summary>

a) $e^{-1{,}8}$. b) $-c\,e^{-\theta c}$. c) $\frac1\theta e^{-\theta c}$, puis $(c + \frac1\theta)\,e^{-\theta c}$ ; leur différence doit redonner b). d) $-\frac{\xi}{\theta^2} = -\frac X\theta$, d'espérance $-\frac{1}{\theta^2}$ ; et l'indicatrice ? e) $\mathbb{E}[(\frac1\theta - X)^2 \mid X > c] = c^2 + \mathbb{V}(Y)$, puis $\mathbb{V}(g) = \mathbb{E}[g^2] - (\text{b})^2$.

</details>

### Ex MB8.2 — Deux graines par godet (une loi binomiale B(2, θ)) et un prix selon le nombre de pousses : la dérivée de la recette moyenne, puis l'estimateur score sans baseline, avec b = E[f] et avec la baseline optimale, et leurs variances

<details><summary>Indice 1</summary>

Fiche §1 (le score d'une loi binomiale) et §3 : « Une baseline pour l'estimateur score » ; M02b (la loi binomiale).

</details>
<details><summary>Indice 2</summary>

$\ln p_\theta(x) = \ln\binom2x + x\ln\theta + (2 - x)\ln(1 - \theta)$ ; les probabilités valent $\big(\frac{1}{16} ;\ \frac{6}{16} ;\ \frac{9}{16}\big)$. La variance de $(f - b)\,s$ est $\mathbb{E}[(f - b)^2s^2] - D^2$, avec $D$ la réponse b) ; développe-la en $b$ : $\mathbb{E}[f^2s^2] - 2b\,\mathbb{E}[fs^2] + b^2\,\mathbb{E}[s^2] - D^2$.

</details>
<details><summary>Indice 3</summary>

a) $s_\theta(x) = \frac{x - 2\theta}{\theta(1 - \theta)}$, avec $\theta(1 - \theta) = \frac{3}{16}$. b) Dérive $3{,}5 \times 2\theta(1 - \theta) + 5\theta^2$, ou calcule $\mathbb{E}[fs]$. c) $\mathbb{E}[f^2s^2] - D^2$. d), e) Calcule $\mathbb{E}[s^2]$ et $\mathbb{E}[fs^2]$, puis $b^\star$ et la variance minimale ; pour tout $b$, la variance vaut la variance minimale plus $(b - b^\star)^2\,\mathbb{E}[s^2]$.

</details>

### Ex MB8.3 — Un camion de crêpes entre deux emplacements, une politique softmax dans l'un d'eux : la chaîne induite, les valeurs, la loi d'occupation actualisée, les valeurs et les avantages des deux actions, puis le gradient de la valeur par rapport aux deux logits

<details><summary>Indice 1</summary>

Fiche §4 : « Rappel de M26 : une politique et ses valeurs », « Une politique softmax tabulaire » et « Dériver le système de Bellman » ; MB8.R2.

</details>
<details><summary>Indice 2</summary>

$\pi(\text{rester} \mid \text{marché}) = \frac{e^{\ln 3}}{e^{\ln 3} + 1}$. La ligne du marché de $\mathbf{P}_\pi$ mélange les lignes de rester et de partir avec les probabilités $\pi$ ; celle du parc est fixe ; $\mathbf{r}_\pi$ de même. $\mathbf{V} = \mathbf{M}\,\mathbf{r}_\pi$, avec l'inverse d'une matrice $2 \times 2$. $Q(\text{marché}, a) = r(\text{marché}, a) + \gamma\sum_t\mathbf{P}[a, \text{marché}, t]\,V(t)$ et $A = Q - V(\text{marché})$ ; puis $\frac{\partial V(s_0)}{\partial z(\text{marché}, a)} = \mathbf{M}[s_0, \text{marché}]\,\pi(a \mid \text{marché})\,A(\text{marché}, a)$.

</details>
<details><summary>Indice 3</summary>

a) $0{,}75\,(0{,}86 ;\ 0{,}14) + 0{,}25\,(0 ;\ 1)$. b) $\mathbf{I} - 0{,}7\,\mathbf{P}_\pi = \begin{pmatrix} 0{,}5485 & -0{,}2485 \\ -0{,}21 & 0{,}51 \end{pmatrix}$, son déterminant, puis $\mathbf{M}\,\mathbf{r}_\pi$. c) La colonne du marché de $\mathbf{M}$ : $\frac{(0{,}51 ;\ 0{,}21)}{\det}$. d) $Q(\text{marché}, \text{rester}) = 3 + 0{,}7\,(0{,}86\,V(\text{marché}) + 0{,}14\,V(\text{parc}))$ et $Q(\text{marché}, \text{partir}) = 0{,}7\,V(\text{parc})$. e) Quatre produits ; contrôle : les deux dérivées d'un même départ ont une somme nulle.

</details>

### Ex MB8.4 — L'état d'une route (bonne, usée, en travaux) et des valeurs estimées fausses : le biais des retours à 1 et 2 pas, les poids (1 − λ)λ^{k−1} d'un λ-retour, et son biais quand l'erreur est la même partout

<details><summary>Indice 1</summary>

Fiche §5 : « Des retours qui s'arrêtent », « Le λ-retour » et « Ce que vaut un retour, en moyenne » ; M26 §1 (la loi à $k$ pas) ; R5 (série géométrique).

</details>
<details><summary>Indice 2</summary>

Le biais du retour à $k$ pas depuis $s$ est $\gamma^k(\mathbf{P}_\pi^k\mathbf{e})(s)$ : l'erreur de l'état atteint au pas $k$, en moyenne, actualisée $k$ fois. Le retour à $k$ pas pèse $(1 - \lambda)\lambda^{k-1}$ ; les retours de plus de $k$ pas pèsent ensemble $\lambda^k$. Pour d), une erreur constante vérifie $\mathbf{P}_\pi^k\mathbf{e} = \mathbf{e}$.

</details>
<details><summary>Indice 3</summary>

a) $\mathbf{P}_\pi\mathbf{e} = (0{,}85 \times 3 ;\ 0{,}3 \times 2 ;\ 0{,}85 \times 3 + 0{,}15 \times 2)$, puis $\times\,0{,}6$. b) $\mathbf{P}_\pi(\mathbf{P}_\pi\mathbf{e})$, puis $\times\,0{,}36$. c) $0{,}3 \times 0{,}7^4$ ; cherche le premier $k$ tel que $0{,}7^k < 0{,}05$. d) $\sum_k(1 - \lambda)\lambda^{k-1}\,2\gamma^k$ : une série géométrique de raison $\gamma\lambda$.

</details>

### Ex MB8.5 — Un panel en ligne dont les classes d'âge ne suivent pas le recensement : les poids p/q, la dépense moyenne repondérée, la taille effective de Kish d'un petit échantillon, des poids tronqués (le biais), puis KL(q ‖ p) exacte et ses estimateurs k₁ et k₃ classe par classe

<details><summary>Indice 1</summary>

Fiche §6 : « Changer de loi », « Normaliser, mesurer, tronquer » et « Estimer une KL par échantillons » ; M20 §5 (Horvitz-Thompson) ; M06 (KL).

</details>
<details><summary>Indice 2</summary>

$w = \frac pq$ classe par classe ; $\mathbb{E}_q[wf] = \sum q\,w\,f = \sum p\,f$. Kish : $\frac{(\sum_iw_i)^2}{\sum_iw_i^2}$ sur les six panélistes. Tronquer : $\min(w, c)$ classe par classe ; le biais se compare à la moyenne repondérée exacte. $\mathrm{KL}(q \,\|\, p) = \sum q\ln\frac qp$ ; $k_1 = -\ln w$ ; $k_3 = (w - 1) - \ln w$.

</details>
<details><summary>Indice 3</summary>

a) $\frac{0{,}26}{0{,}50}$, … b) $\sum q\,f$, puis $\sum p\,f$. c) $\sum w_i = 3 \times 0{,}52 + 1{,}64 + 2 \times 1{,}32$. d) $\min(w, 1{,}6) = (0{,}52 ;\ 1{,}6 ;\ 1{,}32)$. e) $0{,}5\ln\frac{0{,}5}{0{,}26} + \cdots$ f), g) Classe par classe ; contrôle : $\sum q\,k_1$ et $\sum q\,k_3$ redonnent e).

</details>

### Ex MB8.6 — Un tournoi de babyfoot entre trois clubs : deux clubs seuls (la différence de forces en forme fermée), puis vérifier les équations du maximum de vraisemblance pour des forces proposées, la probabilité qu'un club batte un autre, une mise à jour Elo, et un club invaincu

<details><summary>Indice 1</summary>

Fiche §7 : « Le modèle », « Quand les forces existent » et « La cote Elo » ; M04 (maximum de vraisemblance) ; M13a (sigmoïde).

</details>
<details><summary>Indice 2</summary>

Deux clubs seuls : l'équation de vraisemblance d'une paire, $n\,\sigma(d) = $ les victoires de A. Avec $p_i = e^{\beta_i}$, $\sigma(\beta_i - \beta_j) = \frac{p_i}{p_i + p_j}$, et les victoires attendues de $i$ contre $j$ valent $n_{ij}\,\sigma(\beta_i - \beta_j)$. Centrer : retrancher la moyenne des $\ln p_i$. Elo : $R_A - R_C = \frac{400}{\ln 10}(\beta_A - \beta_C)$, et C gagne $k\,(1 - E)$.

</details>
<details><summary>Indice 3</summary>

a) $\sigma(d) = \frac27$, donc $d = \ln\frac{2/7}{5/7}$. b) $7 \times \frac47$ ; $10 \times \frac45$ ; $4 \times \frac34$ ; puis somme par club et compare aux totaux du tableau. c) $\ln 4$, $\ln 3$, 0, moins leur moyenne. d) $\frac{1}{1 + 4}$. e) $400\log_{10}4$ ; $32 \times (1 - 0{,}2)$. Pour D : écris son équation du maximum de vraisemblance, $4 = 2\,\sigma(\beta_D - \beta_A) + 2\,\sigma(\beta_D - \beta_C)$ ; une force finie peut-elle la vérifier ?

</details>

### Ex MB8.7 — Trois plats à la cantine : la loi de service qui maximise la satisfaction moyenne moins β fois la KL à la loi actuelle, pour deux valeurs de β, sa valeur β ln Z, comparée à la loi actuelle et au meilleur plat seul

<details><summary>Indice 1</summary>

Fiche §8 : « Un compromis » et « Les deux limites » ; M05a §8 (log-sum-exp) ; M06 (KL).

</details>
<details><summary>Indice 2</summary>

$\pi^\star \propto \pi_{\mathrm{ref}}\,e^{r/\beta}$, $Z = \sum_x\pi_{\mathrm{ref}}(x)\,e^{r(x)/\beta}$, et la valeur maximale est $\beta\ln Z$. $F(\pi_{\mathrm{ref}}) = \mathbb{E}_{\mathrm{ref}}[r]$ (KL nulle) ; pour la loi qui ne sert que le plat $x$, la KL vaut $\ln\frac{1}{\pi_{\mathrm{ref}}(x)}$.

</details>
<details><summary>Indice 3</summary>

a) Les trois produits $\pi_{\mathrm{ref}}(x)\,e^{r(x)}$, divisés par leur somme $Z$. b) $\ln Z$. c) $0{,}45 \times 2 + 0{,}40 \times 4 + 0{,}15 \times 5$ ; puis $5 - \ln\frac{1}{0{,}15}$. d) $e^{r/3}$, la même démarche, et $3\ln Z$. Contrôle : $\mathbb{E}_{\pi^\star}[r] - \beta\,\mathrm{KL}(\pi^\star \,\|\, \pi_{\mathrm{ref}}) = \beta\ln Z$.

</details>

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex MB8.8 — Les deux identités du score, E[s_θ(X)] = 0 et Var(s_θ) = −E[∂²_θ ln p_θ(X)], pour une famille à densité dont le support ne dépend pas de θ ; leur application aux lois de Poisson et exponentielle ; puis la loi uniforme sur [0, θ], où elles tombent

<details><summary>Indice 1</summary>

Fiche §1 : « Une espérance nulle » et « L'information de Fisher » ; M25b §7 (dériver sous l'intégrale) ; M02b (les trois lois).

</details>
<details><summary>Indice 2</summary>

Sur $S$, $\partial_\theta p_\theta = p_\theta\,s_\theta$. Dérive $\int_Sp_\theta = 1$ une fois, puis deux fois. Pour la loi uniforme, calcule $\int_0^\theta\partial_\theta p_\theta(x)\,\mathrm{d}x$ et compare-le à ce que donnerait l'étape 1.

</details>
<details><summary>Indice 3</summary>

1. $0 = \int_S\partial_\theta p_\theta = \int_Sp_\theta\,s_\theta$. 2. $\partial^2_\theta\ln p_\theta = \frac{\partial^2_\theta p_\theta}{p_\theta} - s_\theta^2$, et $\int_S\partial^2_\theta p_\theta = 0$. 3. Poisson : $s_\theta = \frac x\theta - 1$, $-\partial^2_\theta\ln p_\theta = \frac{x}{\theta^2}$ ; exponentielle : $s_\theta = \frac1\theta - x$, et une seule formule, par exemple $-\partial^2_\theta\ln p_\theta = \frac{1}{\theta^2}$. 4. Sur $[0, \theta[$, $\ln p_\theta = -\ln\theta$ ; $\int_0^\theta\partial_\theta p_\theta = -\frac1\theta$ : où l'étape 1 a-t-elle utilisé un support fixe ?

</details>

### Ex MB8.9 — La baseline optimale b* = E[f s²]/E[s²] d'un estimateur score ; sur n tirages, la moyenne des autres est une baseline sans biais, et la moyenne du groupe multiplie l'estimateur par (n − 1)/n

<details><summary>Indice 1</summary>

Fiche §3 : « Une variable de contrôle », « Une baseline pour l'estimateur score » et « Des baselines tirées de l'échantillon » ; M02c (variance, covariance).

</details>
<details><summary>Indice 2</summary>

$\mathbb{E}[s] = 0$ donne l'absence de biais. Développe $\mathbb{E}[(f - b)^2s^2]$ : un trinôme en $b$, comme pour $c^\star$ (fiche §3). Pour 3, $b_i$ dépend des $x_j$, $j \ne i$, mais pas de $x_i$. Pour 4, écris $\bar f$ avec $f(x_i)$ et $b_i$.

</details>
<details><summary>Indice 3</summary>

1. Le trinôme $\mathbb{E}[s^2]\,b^2 - 2\,\mathbb{E}[fs^2]\,b + \mathbb{E}[f^2s^2] - D^2$ est minimal en $b = \frac{\mathbb{E}[fs^2]}{\mathbb{E}[s^2]}$. 2. $\mathbb{E}[fs^2] = \mathbb{E}[f]\,\mathbb{E}[s^2]$ : une covariance nulle. 3. Par indépendance, $\mathbb{E}[b_i\,s(x_i)] = \mathbb{E}[b_i]\,\mathbb{E}[s(x_i)]$. 4. $n\bar f = f(x_i) + (n - 1)\,b_i$ ; remplace dans $f(x_i) - \bar f$.

</details>

### Ex MB8.10 — Le gradient de la valeur d'une politique sous forme matricielle : dériver V = r_π + γP_πV, faire apparaître la loi d'occupation actualisée et la valeur des actions, puis remplacer Q^π par l'avantage

<details><summary>Indice 1</summary>

Fiche §4 : « Rappel de M26 : une politique et ses valeurs » et « Dériver le système de Bellman » ; M18 §7 (règle du produit) ; MB8.R1 (jacobienne de la softmax).

</details>
<details><summary>Indice 2</summary>

Dérive le produit $(\mathbf{I} - \gamma\mathbf{P}_\pi)\,\mathbf{V}$. $\frac{\partial\pi(b \mid s')}{\partial z(s, a)}$ est nul si $s' \ne s$. En $s$, regroupe $r(s, b) + \gamma(\mathbf{P}[b]\mathbf{V})(s) = Q(s, b)$. Pour 5 : $\partial_\theta\pi = \pi\,\partial_\theta\ln\pi$, et $\sum_a\pi(a \mid s) = 1$.

</details>
<details><summary>Indice 3</summary>

1. $-\gamma\,(\partial\mathbf{P}_\pi)\,\mathbf{V} + (\mathbf{I} - \gamma\mathbf{P}_\pi)\,\partial\mathbf{V} = \partial\mathbf{r}_\pi$, puis multiplie par $\mathbf{M}$. 2. $\pi(b \mid s)\big(\mathbf{1}\{b = a\} - \pi(a \mid s)\big)$. 3. $\sum_b\pi(b \mid s)\big(\mathbf{1}\{b = a\} - \pi(a \mid s)\big)\,Q(s, b) = \pi(a \mid s)\big(Q(s, a) - \sum_b\pi(b \mid s)\,Q(s, b)\big)$. 4. $\mathbf{M}$ fois un vecteur qui n'a que la coordonnée $s$ ; $\mathbf{M}[s_0, s] = \frac{\nu_{s_0}(s)}{1 - \gamma}$. 5. $\sum_a\pi(a \mid s)\,\partial_\theta\ln\pi(a \mid s)\,V(s) = V(s)\,\partial_\theta\sum_a\pi(a \mid s)$.

</details>

<a id="pont"></a>

## 🔗 Pont vers workbookIA

### Ex MB8.11 — Pont : la « loss de substitution » −(1/n)Σ(f(x_i) − b) ln p_θ(x_i), dont la dérivée, les f(x_i) et b tenus fixes, est moins l'estimateur score : sur le taux d'une loi de Poisson, puis ce que changent des f standardisés dans le batch

<details><summary>Indice 1</summary>

Fiche §2 : « La méthode du score » ; §3 : « Des baselines tirées de l'échantillon » ; M04 (la log-vraisemblance d'une loi de Poisson).

</details>
<details><summary>Indice 2</summary>

$\ln p_\theta(x) = x\ln\theta - \theta - \ln x!$. Les $f(x_i)$ et $b$ sont des constantes : $\frac{\mathrm{d}L}{\mathrm{d}\theta} = -\frac1n\sum_i(f(x_i) - b)\,s_\theta(x_i)$. Compare $\sum_is_\theta(x_i)$ à 0.

</details>
<details><summary>Indice 3</summary>

a) $\frac{x_i}{2{,}5} - 1$. Les $f(x_i)$ : $(1, 0, 2, 0, 3, 0, 1, 2)$. c) $\sum_if(x_i)\,s_\theta(x_i) = 5{,}8$, donc $-\frac{5{,}8}{8}$. b) $\sum_i(f(x_i) - 1)\,s_\theta(x_i) = \sum_if(x_i)\,s_\theta(x_i) - \sum_is_\theta(x_i)$. Pour la standardisation : le centrage est une baseline (laquelle ? ∂ MB8.9) ; et la division ?

</details>

<a id="reflexion"></a>

## 🗣️ Explication

### Ex MB8.12 — Expliquer avec un club d'échecs pourquoi une cote Elo ne dit que des écarts de niveau, et pourquoi battre plus fort que soi rapporte plus de points

<details><summary>Indice 1</summary>

Fiche §7 : « La cote Elo » (et « Le modèle » : seules les différences de forces comptent).

</details>
<details><summary>Indice 2</summary>

Une cote donne, par son écart avec une autre, une chance de gagner. Après une partie, on regarde le résultat moins ce qui était attendu. Que valait ce qui était attendu contre la meilleure joueuse ? Contre un débutant ?

</details>
<details><summary>Indice 3</summary>

Un plan en cinq phrases : (1) l'écart prédit une chance de gagner ; (2) un même nombre ajouté à toutes les cotes ne change aucun écart ; (3) on compare le résultat à ce qui était attendu ; (4) la surprise rapporte ; (5) les points passent de la perdante à la gagnante.

</details>

<a id="entretien"></a>

## 💼 Entretien

### MB8.E1 — « Comment dériver la probabilité d'un événement par rapport au paramètre d'une loi quand on ne peut pas dériver à travers les tirages, et comment rendre l'estimation moins bruitée ? »

<details><summary>Indice 1</summary>

Fiche §2 : « La méthode du score » et « Le score contre le chemin » ; §3 : « Une baseline pour l'estimateur score » et « Des baselines tirées de l'échantillon ».

</details>
<details><summary>Indice 2</summary>

Quatre temps : pourquoi le chemin échoue (une indicatrice, une loi discrète) ; l'identité du score et son hypothèse ; l'estimateur et la raison de son bruit ; deux réductions de variance sans biais, et un piège.

</details>
<details><summary>Indice 3</summary>

Une phrase par temps : « la dérivée d'une indicatrice est nulle presque partout » ; « la dérivée de $\mathbb{E}_\theta[f]$ est $\mathbb{E}_\theta[f\,s_\theta]$, si le support ne dépend pas de $\theta$ » ; « la moyenne des $f\,s_\theta$, sans biais mais bruitée » ; « une baseline (la meilleure constante, ou la moyenne des autres tirages) ou une variable de contrôle d'espérance connue ; pas la moyenne du batch, tirage compris ».

</details>

<a id="notebook"></a>

## Notebook

### MB8.13 — L'estimateur score d'une dérivée sur un échantillon, avec une baseline constante ou la moyenne des autres tirages, et son erreur type : `score_function_gradient`

<details><summary>Indice 1</summary>

Fiche §2 : « La méthode du score » ; §3 : « Une baseline pour l'estimateur score » et « Des baselines tirées de l'échantillon » ; la docstring de `score_function_gradient`.

</details>
<details><summary>Indice 2</summary>

Les contrôles : `np.asarray(f_values, dtype=float)` à une dimension, au moins deux valeurs finies ; les scores à une ou deux dimensions, avec $n$ lignes ; `isinstance(baseline, bool)` avant tout, puis un nombre fini ou la chaîne `"leave-one-out"`. Les baselines : la constante, ou $\frac{\sum_jf_j - f_i}{n - 1}$. Les termes $g_i = (f_i - b_i)\,s_i$ (pour des scores à deux dimensions, la ligne $i$ fois $f_i - b_i$) ; leur moyenne et leur écart-type (`ddof=1`) sur l'axe 0, divisé par $\sqrt n$. Rends deux `float` pour des scores à une dimension.

</details>
<details><summary>Indice 3</summary>

Les lignes clés :
```python
b = (f.sum() - f) / (n - 1) if loo else float(baseline)
g = (f - b)[:, None] * s if s.ndim == 2 else (f - b) * s
est, se = g.mean(axis=0), g.std(axis=0, ddof=1) / math.sqrt(n)
```
a) La baseline par défaut ; b) `baseline="leave-one-out"` ; c) le rapport des deux estimations, à comparer avec ∂ MB8.9.

</details>

### MB8.14 — Le gradient exact de la valeur d'une politique softmax tabulaire, par le système de Bellman : `policy_gradient_exact`

<details><summary>Indice 1</summary>

Fiche §4 : « Une politique softmax tabulaire » et « Dériver le système de Bellman » ; M26.14 (`P[a, s, t]`, `r[a, s]`) ; la docstring de `policy_gradient_exact`.

</details>
<details><summary>Indice 2</summary>

Les contrôles : les formes $(K, m, m)$, $(K, m)$ et $(m, K)$ ; des $\mathbf{P}[a]$ positifs, de lignes de somme au plus $1 + 10^{-9}$ ; $\gamma$ réel de $[0, 1]$, pas un booléen. $\pi$ : `z - z.max(axis=1, keepdims=True)`, l'exponentielle, divisée par la somme de sa ligne. $\mathbf{P}_\pi$ et $\mathbf{r}_\pi$ par `np.einsum`. $\mathbf{M}$ par `np.linalg.solve(I - gamma * P_pi, I)` ; pour $\gamma = 1$, refuse si `np.linalg.matrix_rank(I - P_pi) < m`. $\mathbf{V} = \mathbf{M}\,\mathbf{r}_\pi$, $Q[s, a] = r[a, s] + \gamma\,(\mathbf{P}[a]\,\mathbf{V})[s]$, $A = Q - V$. a) Au parc, deux actions identiques : `P[0, 1]` et `P[1, 1]` valent $(0{,}3 ;\ 0{,}7)$, `r[0, 1]` et `r[1, 1]` valent 4.

</details>
<details><summary>Indice 3</summary>

Les lignes clés :
```python
P_pi = np.einsum("sa,ast->st", pi, P)
Q = r.T + gamma * np.einsum("ast,t->sa", P, V)
grad = M[:, :, None] * (pi * (Q - V[:, None]))[None, :, :]
```
b) `grad[0].ravel()` ; c) `grad[2].ravel()`. Contrôles : `grad.sum(axis=2)` est nul, et une différence finie centrée sur un logit redonne sa dérivée.

</details>

### MB8.15 — Des poids d'importance calculés en log, auto-normalisés ou tronqués, et la taille effective de l'échantillon : `importance_weights`

<details><summary>Indice 1</summary>

Fiche §6 : « Changer de loi » et « Normaliser, mesurer, tronquer » ; M05a §8 (log-sum-exp) ; la docstring de `importance_weights`.

</details>
<details><summary>Indice 2</summary>

Les contrôles : deux tableaux à une dimension de même longueur $n \ge 1$ ; `log_target` sans `nan` ni $+\infty$ ($-\infty$ est permis) ; `log_proposal` fini ; `self_normalize` un booléen ; `max_weight` un nombre $> 0$ (ni booléen, ni `nan`). $d = \ln p - \ln q$, puis `np.minimum(d, math.log(c))`. La taille effective ne change pas quand on multiplie tous les poids par un même facteur : calcule-la sur $u = e^{d - \max d}$, dont les valeurs sont dans $[0, 1]$. Si tous les $d$ valent $-\infty$, tous les poids sont nuls.

</details>
<details><summary>Indice 3</summary>

Les lignes clés :
```python
u = np.exp(d - d.max())
ess = float(u.sum() ** 2 / (u ** 2).sum())
w = u / u.sum() if self_normalize else np.exp(d)
```
a) Les logarithmes des parts $p$ et $q$ des classes des six panélistes, avec `self_normalize=True`. b) Regarde d'abord `np.exp(LOG_P_15)` seul.

</details>

### MB8.16 — Les forces d'un modèle de Bradley-Terry par maximum de vraisemblance (l'algorithme de Zermelo), centrées, et le refus d'un tournoi où elles n'existent pas : `bradley_terry_fit`

<details><summary>Indice 1</summary>

Fiche §7 : « Le modèle », « Quand les forces existent » et « L'algorithme de Zermelo » ; M16 (puissances d'une matrice d'adjacence) ; la docstring de `bradley_terry_fit`.

</details>
<details><summary>Indice 2</summary>

Les contrôles : un tableau carré $K \times K$, $K \ge 2$, de nombres finis positifs, de diagonale nulle ; `tol` $> 0$ ; `max_iter` un entier $\ge 1$ (ni booléen ni flottant ; un entier NumPy est accepté). La connexité : $R$ = (`wins > 0`) ou $i = j$ ; tant que le produit booléen $R \cdot R$ ajoute des chemins, recommence ; refuse si un coefficient de $R$ reste faux. Zermelo : $W_i = \sum_j\mathrm{wins}[i, j]$, $n_{ij} = \mathrm{wins}[i, j] + \mathrm{wins}[j, i]$, puis $p_i \leftarrow W_i / \sum_{j \ne i}\frac{n_{ij}}{p_i + p_j}$, divisé par la moyenne géométrique ; arrête quand le plus grand changement de $\beta = \ln p$ passe sous `tol`, et lève `RuntimeError` après `max_iter` balayages.

</details>
<details><summary>Indice 3</summary>

Les lignes clés d'un balayage :
```python
n = wins + wins.T
p_new = W / (n / (p[:, None] + p[None, :])).sum(axis=1)   # the diagonal of n is 0
p_new /= np.exp(np.log(p_new).mean())
```
b) La sigmoïde de `beta[0] - beta[5]`. c) `W = WINS_16.copy(); W[:, 1] = 0`, puis appelle ta fonction dans un `try`.

</details>

### MB8.17 — Prédire l'ordre des écarts-types de l'estimateur score d'une même dérivée, sans baseline, avec la moyenne des autres tirages et avec la baseline optimale, puis les mesurer

<details><summary>Indice 1</summary>

Fiche §3 : « Une baseline pour l'estimateur score » et « Des baselines tirées de l'échantillon ». Écris tes deux prédictions avant d'ouvrir l'indice 2.

</details>
<details><summary>Indice 2</summary>

Les trois estimateurs ont la même espérance (∂ MB8.9 pour la moyenne des autres tirages) : seule leur dispersion peut différer. La variance est un trinôme en $b$, minimal en $b^\star$ (fiche §3, et sa figure). La moyenne des autres tirages se comporte comme $b = \mathbb{E}[f]$.

</details>
<details><summary>Indice 3</summary>

Ta prédiction, raisonnée : place $0$, $\mathbb{E}[f]$ et $b^\star$ sur une droite, en te demandant pour quels tirages $s^2$ est grand et si $f$ y vaut 0 ou 1 ; puis compare les distances à $b^\star$. Pour b), le rapport des écarts-types est la racine du rapport des variances. Pour mesurer : 2 000 boucles, `rng.poisson(3.5, 40)`, $f = \mathbf{1}\{x \ge 5\}$, $s = \frac{x}{3{,}5} - 1$, trois appels de `score_function_gradient`, puis l'écart-type (`ddof=1`) de chaque colonne.

</details>

### MB8.18 — Un événement rare, P(Z > 4) pour Z normale centrée réduite : Monte-Carlo naïf contre l'échantillonnage d'importance sous N(4, 1), la taille effective, puis des poids tronqués à c : le biais et la variance selon c

<details><summary>Indice 1</summary>

Fiche §6 : « Changer de loi » et « Normaliser, mesurer, tronquer » ; ton `importance_weights` (MB8.15).

</details>
<details><summary>Indice 2</summary>

Naïf : la moyenne de $\mathbf{1}\{z > 4\}$ sur 100 000 tirages. Importance : des $z$ tirés de $\mathcal{N}(4, 1)$, `importance_weights(norm.logpdf(z), norm.logpdf(z, 4, 1))`, puis la moyenne de $w\,\mathbf{1}\{z > 4\}$ et son erreur type. Troncature : `max_weight=c` ; pour chaque $c$, 400 répétitions ; le biais relatif (moyenne moins vraie valeur, divisé par la vraie valeur) et l'écart-type relatif.

</details>
<details><summary>Indice 3</summary>

Écris $\ln p(z) - \ln q(z) = -\frac{z^2}{2} + \frac{(z - 4)^2}{2}$ et simplifie : un poids de la forme $e^{\alpha - \beta z}$, décroissant en $z$. Pour quels $z > 4$ un poids dépasse-t-il $c$ ? La taille effective porte sur les 10 000 poids, que $z$ dépasse 4 ou non. Trace `plt.semilogx(C, biais)` et `plt.semilogx(C, ecarts)`.

</details>

### MB8.19 — Chasse à l'erreur : le score d'une loi exponentielle écrit pour la moyenne au lieu du taux, des poids d'importance inversés (q/p), une baseline qui contient le tirage lui-même, des forces de deux tournois sans joueur commun comparées sur une même échelle

<details><summary>Indice 1</summary>

Fiche §1 (le score de la loi exponentielle, par son taux), §3 (« Des baselines tirées de l'échantillon »), §6 (« Changer de loi ») et §7 (« Quand les forces existent »).

</details>
<details><summary>Indice 2</summary>

Pour chaque fonction, trouve d'abord ce qui est faux sur un petit cas comparé à la définition, puis pourquoi l'entrée du collègue le cache : au taux 1, que valent les deux expressions du score ? avec $p = q$, que valent les poids ? sur un batch de 10 000 tirages, que vaut le facteur de ∂ MB8.9 ? avec deux fois le même tableau, les deux échelles sont-elles décalées ? Corrige le code du collègue lui-même, sans appeler `mymath`.

</details>
<details><summary>Indice 3</summary>

(1) Dérive $\ln(\theta e^{-\theta x})$ par rapport à $\theta$. (2) Un poids est $\frac pq$ : dans quel ordre retrancher les logarithmes ? (3) La baseline de chaque tirage ne doit pas contenir sa propre valeur (∂ MB8.9). (4) Le graphe des victoires des deux tournois réunis est-il fortement connexe ? Fais lever `ValueError` quand il ne l'est pas. a) à c) : la fonction corrigée, puis la fautive, sur les mêmes données ; d) la fonction fautive, avant puis après l'ajout de B3.

</details>

### MB8.20 — Un test de propriété pour le gradient exact : sur des MDP tirés au hasard, comparé à des différences finies centrées, et de somme nulle sur les actions de chaque état

<details><summary>Indice 1</summary>

Fiche §4 : « Dériver le système de Bellman » (la vérification par différences finies, la somme nulle sur les actions) ; M05a §5 et §7 (différences finies centrées, choix du pas).

</details>
<details><summary>Indice 2</summary>

Chaque test tire plusieurs MDP : `rng.dirichlet(np.ones(m), size=(K, m))` pour les $\mathbf{P}[a]$, `rng.normal` pour les récompenses et les logits, $\gamma$ parmi $0{,}6$ et $0{,}7$. Les différences finies : pour chaque $(s, a)$, les valeurs par `np.linalg.solve` en $z \pm h$ sur ce seul logit, puis $\frac{V^+ - V^-}{2h}$, avec ta propre fonction des valeurs ($\pi$, $\mathbf{P}_\pi$, $\mathbf{r}_\pi$), pas `policy_gradient_exact` de la référence. Compare à $10^{-6}$ près : `np.abs(fd - grad).max() <= 1e-6` (la vérification essaie des méthodes fausses de quelques $10^{-6}$ en valeur relative, que `np.allclose` laisserait passer). La somme : `np.abs(grad.sum(axis=2)).max() <= 1e-10`. Rends un booléen Python.

</details>
<details><summary>Indice 3</summary>

Le pas : l'erreur de troncature croît comme $h^2$, celle d'arrondi comme $\frac{10^{-16}}{h}$ ; leur somme est la plus petite vers $h \approx 10^{-5}$ (M05a §7). Des logits non nuls et plusieurs MDP : une méthode fausse peut coïncider avec la bonne sur une politique uniforme, ou quand $\mathbf{M}$ est symétrique. a) Tes deux tests sur `policy_gradient_exact`.

</details>

### MB8.21 — Défi : estimer, avec un budget de tirages, la dérivée d'une probabilité de dépassement par rapport au paramètre d'une loi, assez précisément neuf fois sur dix (score, baseline, variable de contrôle)

<details><summary>Indice 1</summary>

Fiche §2 : « La méthode du score » et « Le score contre le chemin » ; §3 : « Une variable de contrôle » et « Une baseline pour l'estimateur score » ; 🔨 MB8.13.

</details>
<details><summary>Indice 2</summary>

`draw(k)` rend les tirages et leurs scores : l'estimateur score se calcule sans connaître la loi. Avec $f = \mathbf{1}\{x > c\}$, sa variance à un tirage est $\mathbb{E}[(f - b)^2s^2] - D^2$ : que vaut-elle pour $b = 0$ quand $P(X > c)$ est proche de 1 ? La baseline qui la réduit le plus est $b^\star = \frac{\mathbb{E}[fs^2]}{\mathbb{E}[s^2]}$ (fiche §3) : que vaut-elle quand $f$ vaut presque toujours 1 ? Elle doit rester sans biais : une constante, ou la moyenne des autres tirages. Ne gaspille pas le budget : les tirages à $\delta \ne 0$ coûtent autant que les autres.

</details>
<details><summary>Indice 3</summary>

La baseline optimale s'estime sur les tirages, $\hat b = \frac{\sum_if_is_i^2}{\sum_is_i^2}$, au prix d'un petit biais, comme pour $c^\star$ estimé sur les tirages (fiche §3, 💻) ; ou bien la moyenne des autres tirages, sans biais. Un seul appel `x, s = draw(budget)`, puis la moyenne des $(f_i - b_i)\,s_i$. Contrôle sur le cas d'essai : la dérivée exacte est ta réponse à MB8.1 b.

</details>
