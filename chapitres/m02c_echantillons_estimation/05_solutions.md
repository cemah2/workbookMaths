# M02c · Échantillons et estimation — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication](#reflexion) · [💼 Entretien](#entretien) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### M02c.Q1 — Résumer une série : vrai ou faux
1. **Faux** : avec un nombre pair de valeurs, la médiane est la moyenne des deux valeurs du milieu, souvent absente de la série (43,5 en M02c.1).
2. **Faux** : la variance ne change pas ; décaler les valeurs ne les disperse pas.
3. **Vrai** : $s_{ax} = \lvert a \rvert\,s_x$ (et la variance est multipliée par 9).
4. **Vrai** : la moyenne suit la valeur changée sans limite ; la médiane, la 6ᵉ des 11 valeurs triées, ne peut que passer à une valeur voisine dans la série triée.
5. **Vrai** : $\sum (x_i - \bar{x}) = \sum x_i - n\bar{x} = 0$.
6. **Faux** : $Q_1 \ge \min$ et $Q_3 \le \max$, donc $Q_3 - Q_1 \le \max - \min$.

### M02c.Q2 — z-scores et valeurs aberrantes
1. Elle est **1,5 écart-type sous la moyenne**.
2. Une moyenne de **0** et un écart-type de **1**.
3. $\text{EI} = 10$ : **5** et **45** ($20 - 15$ et $30 + 15$).
4. **Faux** : avec 8 valeurs, $\lvert z \rvert \le \sqrt{7} \approx 2{,}65$ (avec $s_n$), quelle que soit la valeur (fiche §2).
5. La valeur aberrante gonfle l'écart-type qui sert à la juger (effet de masque), alors que les quartiles ne bougent presque pas quand une valeur extrême devient plus extrême.
6. **Faux** : avec la moyenne et l'écart-type du jeu d'**entraînement**.

### M02c.Q3 — i.i.d. ou pas ?
1. **Oui** : des lancers indépendants d'un même dé.
2. **Non** : la température d'un jour dépend de celle de la veille (l'**indépendance** tombe) ; sur un mois, la saison peut aussi faire monter ou descendre les températures (la **même loi** tombe alors aussi).
3. **Non** : chaque carte a la même loi, mais les tirages sont **dépendants** (une carte sortie ne ressort pas).
4. **Oui, en pratique** : les tirages sont dépendants, mais le facteur $\frac{N - n}{N - 1}$ vaut 0,99998 : comme avec remise.
5. **Non** : les 10 photos d'une même personne se ressemblent (l'**indépendance** tombe ; on découpe entraînement et test **par personne**). Si les photos sont rangées personne par personne, la loi change aussi d'un bloc à l'autre : « les deux » est défendable.
6. **Faux** : chaque tirage a la même loi (uniforme sur la population) ; c'est la dépendance qui change.

### M02c.Q4 — Grands nombres et TCL : ce qu'ils disent, ce qu'ils ne disent pas
1. **Faux** : les lancers sont indépendants ; la loi des grands nombres dilue les écarts, elle ne les compense pas.
2. Par **10** : $\sqrt{\frac{10\,000}{100}} = 10$.
3. **Faux** : les tirages gardent la loi exponentielle ; c'est la **moyenne** de beaucoup de tirages qui devient normale.
4. À peu près $\mathcal{N}(5 ;\ 0{,}2^2)$ : espérance 5, écart-type $\frac{2}{\sqrt{100}} = 0{,}2$ (variance 0,04).
5. **Vrai** : Bienaymé-Tchebychev avec $\varepsilon = 2\sigma$ donne $\frac{1}{4}$.
6. **Faux** : la loi doit avoir une espérance (la densité $\frac{1}{x^2}$ sur $[1 ; +\infty[$ n'en a pas).

### M02c.Q5 — Biais, variance et ddof
1. **Non** : il est juste **en moyenne** sur tous les échantillons ; sur un échantillon donné, il se trompe (de l'ordre de son écart-type).
2. $2^2 + 5 = $ **9**.
3. Par $n$ ; par $n - 1$.
4. Par $\frac{4}{3}$ : $s^2 = \frac{n}{n - 1}s_n^2$.
5. **Faux** : l'erreur quadratique compte ; un estimateur biaisé mais peu dispersé peut être meilleur (fiche §6).
6. **Vrai** : $\frac{n}{n - 1} \to 1$.

### M02c.Q6 — Lire un intervalle de confiance
1. **Incorrecte** : la vraie moyenne est un nombre fixé. « 95 % » décrit la méthode : 95 % des intervalles construits ainsi contiennent la vraie moyenne.
2. **Incorrecte** : l'intervalle porte sur la **moyenne**, pas sur les sessions, beaucoup plus dispersées.
3. **12,8** minutes, le centre de l'intervalle.
4. La demi-largeur 0,7 vaut $1{,}96 \times \text{SE}$, donc $\text{SE} \approx \frac{0{,}7}{1{,}96} \approx$ **0,36** minute.
5. Environ **0,35** minute : 4 fois plus de données divisent la demi-largeur par $\sqrt{4} = 2$.
6. **Plus large** : 2,576 au lieu de 1,96.

### M02c.Q7 — Covariance et corrélation : vrai ou faux
1. **Faux** : la force d'une relation linéaire se lit sur $\lvert r \rvert$ ; $0{,}9 > 0{,}5$. Le signe dit seulement le sens.
2. **Vrai**.
3. **Vrai** : la covariance est linéaire en chaque variable.
4. **Faux** : $\mathbb{V}(X - Y) = \mathbb{V}(X) + \mathbb{V}(Y) - 2\operatorname{Cov}(X, Y)$.
5. **Faux** : l'**âge** fait grandir les pieds et progresser en lecture ; c'est une variable de confusion.
6. **10** : 4 variances, et 6 covariances, chacune écrite deux fois ($\Sigma_{ij} = \Sigma_{ji}$).

<a id="rappels"></a>

## 🔁 Rappels

### M02c.R1 — Espérance et variance d'une somme (M02b)
1. $\mathbb{E}[X + Y] = 3 - 1 = 2$ et $\mathbb{V}(X + Y) = 4 + 9 = 13$ (indépendantes).
2. $\mathbb{V}(X - Y) = 4 + 9 = 13$ : les variances s'additionnent aussi.
3. $\mathbb{V}(3X) = 9 \times 4 = 36$ et $\sigma(3X) = 6$.
4. Espérance 3, variance $\frac{4}{25} = 0{,}16$ (écart-type 0,4).

### M02c.R2 — Loi normale et fonction Φ (M02b)
1. 0,9750.
2. $2 \times 0{,}975 - 1 = 0{,}95$.
3. $\Phi\big(\frac{89 - 80}{6}\big) = \Phi(1{,}5) = 0{,}9332$.
4. $2\Phi(z) - 1 = 0{,}9$, donc $\Phi(z) = 0{,}95$ : $z = 1{,}645$.
5. $1 - \Phi(2{,}33) = 1 - 0{,}9901 = 0{,}0099$.

### M02c.R3 — Racines et puissances (R1)
1. 8 et 0,12.
2. $\frac{12}{6} = 2$.
3. $\sqrt{9n} = 3\sqrt{n}$ : multiplié par 3 ; $\frac{1}{\sqrt{n}}$ est divisé par 3.
4. $\sqrt{\frac{2}{9}} = \frac{\sqrt{2}}{3}$.
5. $\sqrt{n} = 12$, donc $n = 144$.

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex M02c.1 — Les statistiques d'une petite série : moyenne, médiane, quartiles, variance

**Réponses** : a) `45.0` · b) `43.5` · c) `328` · d) `41.0` · e) `46.857` · f) `39.75` · g) `48.0` · h) `8.25`.

**Démarche.** Triées : $38, 39, 40, 42, 45, 47, 51, 58$ (positions 0 à 7).
- a) La somme vaut 360, donc $\bar{x} = 45$.
- b) Les deux valeurs du milieu (positions 3 et 4) sont 42 et 45 : médiane 43,5.
- c) Écarts à 45 : $-3, -7, 6, 0, -5, 2, -6, 13$ (somme nulle) ; carrés : $9 + 49 + 36 + 0 + 25 + 4 + 36 + 169 = 328$.
- d) $\frac{328}{8} = 41$. e) $\frac{328}{7} \approx 46{,}857$.
- f) Position $0{,}25 \times 7 = 1{,}75$ : entre $x_{(1)} = 39$ et $x_{(2)} = 40$, $39 + 0{,}75 \times 1 = 39{,}75$.
- g) Position $0{,}75 \times 7 = 5{,}25$ : entre $x_{(5)} = 47$ et $x_{(6)} = 51$, $47 + 0{,}25 \times 4 = 48$.
- h) $48 - 39{,}75 = 8{,}25$.

Pour la copie : $\overline{x^2} = \frac{16\,528}{8} = 2\,066$ et $2\,066 - 45^2 = 41$. À la main, la méthode des écarts manipule de petits nombres et se vérifie (somme nulle) : elle est plus sûre ; la formule $\overline{x^2} - \bar{x}^2$ soustrait deux grands nombres voisins.

**Erreurs fréquentes.** Lire la médiane sur la série non triée (42,5) ; diviser par 7 pour la moyenne ; prendre les quartiles « à la Tukey » (médianes des moitiés : 39,5 et 49), une autre convention ; confondre écart interquartile et étendue (20).

**Variante.** Le percentile 90 de la série ? *Réponse* : position $0{,}9 \times 7 = 6{,}3$, $51 + 0{,}3 \times 7 = 53{,}1$.

### Ex M02c.2 — z-scores, écart interquartile et valeurs aberrantes

**Réponses** : a) `15.7` · b) `5.216` · c) `2.93` · d) `False` · e) `13.25` · f) `17.625` · g) `True` · h) `14.7`.

**Démarche.**
- a) La somme vaut 157 : $\bar{x} = 15{,}7$.
- b) Écarts : $-3{,}7 ;\ -1{,}7 ;\ -2{,}7 ;\ -0{,}7 ;\ -1{,}7 ;\ 0{,}3 ;\ -2{,}7 ;\ -0{,}7 ;\ -1{,}7 ;\ 15{,}3$ ; carrés de somme 272,1 ; $s_n = \sqrt{27{,}21} \approx 5{,}216$.
- c) $z = \frac{15{,}3}{5{,}216} \approx 2{,}93$. d) $2{,}93 < 3$ : la règle ne signale **pas** 31.
- e) Triées : $12, 13, 13, 14, 14, 14, 15, 15, 16, 31$ ; position $0{,}25 \times 9 = 2{,}25$ : $13 + 0{,}25 \times 1 = 13{,}25$.
- f) Position $0{,}75 \times 9 = 6{,}75$ : $15 + 0{,}75 \times 0 = 15 = Q_3$ ; $\text{EI} = 1{,}75$ ; barrière haute $15 + 2{,}625 = 17{,}625$. g) $31 > 17{,}625$ : signalée.
- h) Les 9 autres valeurs : moyenne $\frac{126}{9} = 14$, somme des carrés des écarts 12, $s_n = \sqrt{\frac{12}{9}} \approx 1{,}155$, et $z = \frac{17}{1{,}155} \approx 14{,}7$.

Pour la copie : c) est petit parce que 31 a gonflé elle-même l'écart-type (5,2 au lieu de 1,15) : l'**effet de masque**. Avec 10 valeurs, $\lvert z \rvert \le \sqrt{9} = 3$ (avec $s_n$) : la règle $\lvert z \rvert > 3$ ne peut jamais rien signaler ici.

**Erreurs fréquentes.** Diviser par $n - 1$ (5,498, puis $z \approx 2{,}78$) ; diviser par la variance dans le z-score ; oublier le facteur 1,5 dans la barrière.

**Variante.** La barrière basse ? *Réponse* : $13{,}25 - 2{,}625 = 10{,}625$ ; aucune valeur n'est en dessous.

### Ex M02c.3 — Imputer par la moyenne ou la médiane : ce qui change

**Réponses** : a) `10.0` · b) `8.0` · c) `43.0` · d) `10.0` · e) `32.25` · f) `0.866` · g) `9.5` · h) `8.0`.

**Démarche.**
- a) $\frac{60}{6} = 10$. b) Les valeurs du milieu sont 7 et 9 : médiane 8.
- c) Écarts : $-6, -4, -3, -1, 0, 14$ ; carrés de somme 258 ; $\frac{258}{6} = 43$.
- d) On ajoute deux 10 : la moyenne reste 10.
- e) La somme des carrés des écarts reste 258 (les deux valeurs ajoutées ont un écart nul), divisée maintenant par 8 : 32,25.
- f) $\sqrt{\frac{32{,}25}{43}} = \sqrt{\frac{6}{8}} \approx 0{,}866$ : c'est le facteur $\sqrt{\frac{m}{n}}$ de la fiche.
- g) On ajoute deux 8 : $\frac{60 + 16}{8} = 9{,}5$. h) Triées : $4, 6, 7, 8, 8, 9, 10, 24$ ; médiane $\frac{8 + 8}{2} = 8$.

Pour la copie : la série est asymétrique (la valeur 24 tire la moyenne au-dessus de la médiane). L'imputation par la médiane est moins sensible à cette valeur, mais les deux imputations réduisent la dispersion. Surtout, rien ne dit que les non-répondants ressemblent aux autres : s'ils ne répondent pas parce qu'ils regardent très peu (ou beaucoup) de vidéos, les deux imputations sont biaisées. Une colonne « n'a pas répondu » garde cette information.

**Erreurs fréquentes.** Compter les valeurs manquantes comme des zéros (moyenne 7,5) ; garder le dénominateur 6 après imputation ; donner le rapport des variances (0,75).

**Variante.** Avec 4 valeurs manquantes imputées par la moyenne, le rapport des écarts-types ? *Réponse* : $\sqrt{\frac{6}{10}} \approx 0{,}775$.

### Ex M02c.4 — Avec ou sans remise : la variance de la moyenne

**Réponses** : a) `8` · b) `4` · c) `10` · d) `6` · e) `3` · f) `-2` · g) `"3/4"` · h) `0.9901`.

**Démarche.**
- a) $\mu = 6$, écarts $-4, -2, 0, 2, 4$ : $\sigma^2 = \frac{16 + 4 + 0 + 4 + 16}{5} = 8$.
- b) Avec remise, les tirages sont i.i.d. : $\frac{\sigma^2}{n} = 4$.
- c) $\binom{5}{2} = 10$ paires.
- d) Chaque tirage a la loi uniforme sur la population : $\mathbb{E}[\bar{X}] = \mu = 6$.
- e) $\frac{\sigma^2}{n} \cdot \frac{N - n}{N - 1} = 4 \times \frac{3}{4} = 3$.
- f) $-\frac{\sigma^2}{N - 1} = -\frac{8}{4} = -2$. g) $\frac{3}{4}$, le facteur de correction.
- h) $\frac{9\,900}{9\,999} \approx 0{,}9901$.

Pour la copie : les 10 paires ont pour moyennes $3, 4, 5, 6, 5, 6, 7, 7, 8, 9$ (pour $\{2, 4\}, \{2, 6\}, \{2, 8\}, \{2, 10\}, \{4, 6\}, \{4, 8\}, \{4, 10\}, \{6, 8\}, \{6, 10\}, \{8, 10\}$), de moyenne 6 ; écarts au carré $9, 4, 1, 0, 1, 0, 1, 1, 4, 9$, de somme 30 : variance $\frac{30}{10} = 3$. h) Un sondage de 100 personnes dans 10 000 se calcule presque comme un échantillon i.i.d. : 1 % de variance en moins.

**Erreurs fréquentes.** Diviser par $N - 1$ en a) (10) ; compter les paires ordonnées (20) ; oublier le facteur de correction ; donner une covariance positive.

**Variante.** Sans remise, avec $n = 4$ ? *Réponse* : $\frac{8}{4} \times \frac{1}{4} = \frac{1}{2}$.

### Ex M02c.5 — Combien d'observations pour une moyenne précise à 1 % ?

**Réponses** : a) `0.5` · b) `0.98` · c) `62` · d) `0.258` · e) `320` · f) `4` · g) `0.1` · h) `246`.

**Démarche.**
- a) $\frac{2}{\sqrt{16}} = 0{,}5$. b) $1{,}96 \times 0{,}5 = 0{,}98$.
- c) $1{,}96 \times \frac{2}{\sqrt{n}} \le 0{,}5 \iff \sqrt{n} \ge 7{,}84 \iff n \ge 61{,}47$ : $n = 62$.
- d) $\frac{\sigma^2}{n\varepsilon^2} = \frac{4}{62 \times 0{,}25} \approx 0{,}258$.
- e) $\frac{4}{0{,}25\,n} \le 0{,}05 \iff n \ge 320$.
- f) La demi-largeur varie en $\frac{1}{\sqrt{n}}$ : 4 fois plus de mesures.
- g) $\frac{2}{20} = 0{,}1$. h) $\big(\frac{1{,}96 \times 4}{0{,}5}\big)^2 \approx 245{,}86$ : $n = 246$ (4 fois plus qu'en c, car $\sigma$ est doublé).

Pour la copie : c) donne une probabilité d'environ 5 % de se tromper de plus de 0,5 W, **si** le théorème central limite s'applique (ici, avec 62 mesures, c'est raisonnable). e) **garantit** au plus 5 %, pour n'importe quelle loi, sans approximation ; le prix de cette garantie universelle est une borne large, donc 5 fois plus de mesures.

**Erreurs fréquentes.** $\frac{\sigma}{n}$ au lieu de $\frac{\sigma}{\sqrt{n}}$ ; arrondir 61,47 à 61 ; utiliser $\sigma$ au lieu de $\sigma^2$ dans Bienaymé-Tchebychev.

**Variante.** Le plus petit $n$ pour une demi-largeur à 99 % d'au plus 0,5 W ? *Réponse* : $\big(\frac{2{,}576 \times 2}{0{,}5}\big)^2 \approx 106{,}2$, donc 107.

### Ex M02c.6 — Le théorème central limite à la main : une somme de 100 variables

**Réponses** : a) `0.3` · b) `3.61` · c) `30.0` · d) `19.0` · e) `0.1587` · f) `0.683` · g) `0.19` · h) `155`.

**Démarche.**
- a) $-0{,}5 + 0 + 0{,}8 = 0{,}3$.
- b) $\mathbb{E}[X^2] = 0{,}5 + 0 + 3{,}2 = 3{,}7$, donc $\mathbb{V}(X) = 3{,}7 - 0{,}09 = 3{,}61$ ($\sigma = 1{,}9$).
- c) $100 \times 0{,}3 = 30$. d) $\sqrt{100 \times 3{,}61} = 19$.
- e) $1 - \Phi\big(\frac{49 - 30}{19}\big) = 1 - \Phi(1) = 0{,}1587$.
- f) $\Phi(1) - \Phi(-1) = 2 \times 0{,}8413 - 1 \approx 0{,}683$.
- g) $\frac{1{,}9}{\sqrt{100}} = 0{,}19$.
- h) $P(S_n > 0) \approx \Phi\big(\frac{0{,}3\,n}{1{,}9\sqrt{n}}\big) = \Phi\big(\frac{0{,}3\sqrt{n}}{1{,}9}\big) \ge 0{,}975 \iff \frac{0{,}3\sqrt{n}}{1{,}9} \ge 1{,}96 \iff n \ge 154{,}09$ : $n = 155$.

Pour la copie : $S$ est une somme de 100 variables i.i.d. de variance finie : le théorème central limite s'applique, quelle que soit l'asymétrie de $X$ (100 termes suffisent largement ici). Un seul jour ne prend que trois valeurs : la loi normale n'a aucun sens pour lui.

Pour aller plus loin : $S$ ne prend que des valeurs entières, et la valeur exacte de $P(S > 49)$ est environ 0,1529. Une **correction de continuité** (remplacer 49 par 49,5, à mi-chemin entre deux valeurs possibles) donne 0,1524, plus proche que 0,1587. L'énoncé demande l'approximation directe, celle de la fiche.

**Erreurs fréquentes.** Oublier de retirer $\mathbb{E}[X]^2$ ; additionner les écarts-types (190) ; prendre $\Phi(1)$ pour $P(S > 49)$ ; en h, oublier que l'écart-type de $S_n$ grandit comme $\sqrt{n}$.

**Variante.** $P(S < 0)$ ? *Réponse* : $\Phi\big(\frac{0 - 30}{19}\big) \approx \Phi(-1{,}58) \approx 0{,}057$.

### Ex M02c.7 — Biais, variance et erreur quadratique de trois estimateurs

**Réponses** : a) `-1.5` · b) `3` · c) `"27/16"` · d) `3.9375` · e) `2` · f) `1.9375` · g) `3` · h) `4.583`.

**Démarche.** $T_1$ et $T_2$ sont sans biais, de variances $\sigma^2 = 9$ et $\frac{3\sigma^2}{9} = 3$. $\mathbb{E}[T_3] = \frac{3\mu}{4}$ : biais $-\frac{\mu}{4}$, variance $\frac{3\sigma^2}{16} = \frac{27}{16}$.
- a) $-\frac{6}{4} = -1{,}5$. b) 3. c) $\frac{27}{16}$.
- d) $\text{EQM}(T_3) = 1{,}5^2 + \frac{27}{16} = 2{,}25 + 1{,}6875 = 3{,}9375$.
- e) $\text{EQM} = 9$, 3 et 3,9375 : $T_2$.
- f) Biais $-0{,}5$ : $0{,}25 + 1{,}6875 = 1{,}9375$. g) $1{,}9375 < 3$ : $T_3$.
- h) $\frac{\mu^2}{16} + \frac{27}{16} < 3 \iff \mu^2 < 21 \iff \lvert \mu \rvert < \sqrt{21} \approx 4{,}583$.

Pour la copie : $\text{biais}(T_3) = -\frac{\mu}{4}$ et $\text{EQM}(T_3) = \frac{\mu^2 + 27}{16}$. Choisir $T_3$ demande de savoir si $\lvert \mu \rvert < 4{,}583$, c'est-à-dire de connaître $\mu$, ce qu'on cherche justement. Un estimateur « rétréci » vers 0 gagne quand la vraie valeur est près de 0 : c'est l'idée de la régularisation (chapitre 9 de workbookIA), qui rétrécit les poids d'un modèle.

**Erreurs fréquentes.** Biais de signe inversé ; $\mathbb{V}(T_3) = \frac{3\sigma^2}{4}$ (oublier le carré du facteur) ; ajouter le biais sans l'élever au carré.

**Variante.** L'erreur quadratique de $T_3$ quand $\mu = 0$ ? *Réponse* : $\frac{27}{16} = 1{,}6875$.

### Ex M02c.8 — Erreur type et intervalle de confiance d'une moyenne

**Réponses** : a) `2.0` · b) `[116.58, 124.42]` · c) `7.84` · d) `3.29` · e) `189` · f) `0.015` · g) `0.0294` · h) `False`.

**Démarche.**
- a) $\frac{14}{\sqrt{49}} = 2$. b) $120{,}5 \pm 1{,}96 \times 2 = 120{,}5 \pm 3{,}92$. c) $2 \times 3{,}92 = 7{,}84$.
- d) $1{,}645 \times 2 = 3{,}29$.
- e) $1{,}96 \times \frac{14}{\sqrt{n}} \le 2 \iff \sqrt{n} \ge 13{,}72 \iff n \ge 188{,}24$ : 189.
- f) $\hat{p} = 0{,}9$, $\sqrt{\frac{0{,}9 \times 0{,}1}{400}} = \frac{0{,}3}{20} = 0{,}015$. g) $1{,}96 \times 0{,}015 = 0{,}0294$.
- h) $0{,}02 < 0{,}0294$ : non.

Pour la copie : « Si l'on répétait la mesure sur beaucoup de séries de 49 images, environ 95 % des intervalles calculés ainsi contiendraient le vrai temps moyen ; celui-ci est $[116{,}58 ; 124{,}42]$. » Pour départager les deux modèles : un jeu de test plus grand, ou mieux, une comparaison **appariée** sur les mêmes images (compter les images où ils diffèrent, chapitre 8 de workbookIA).

**Erreurs fréquentes.** Diviser par 49 au lieu de 7 ; utiliser $s$ au lieu de l'erreur type ; garder 1,96 à 90 % ; oublier la racine en f.

**Variante.** L'intervalle à 99 % de la moyenne ? *Réponse* : $120{,}5 \pm 2{,}576 \times 2$, soit environ $[115{,}35 ;\ 125{,}65]$.

### Ex M02c.9 — La variance d'une somme et la covariance : V(X + Y), V(X − Y)

**Réponses** : a) `0.5` · b) `19` · c) `7` · d) `13` · e) `6` · f) `4.0` · g) `0.924` · h) `18.0`.

**Démarche.**
- a) $\frac{3}{2 \times 3} = 0{,}5$. b) $4 + 9 + 6 = 19$. c) $4 + 9 - 6 = 7$.
- d) $4 \times 4 + 9 - 2 \times 2 \times 3 = 16 + 9 - 12 = 13$.
- e) Les constantes disparaissent : $2 \times 1 \times 3 = 6$.
- f) $\bar{x} = 3$, $\bar{y} = 5$ ; écarts $(-2 ; -2)$, $(-1 ; -3)$, $(1 ; 1)$, $(2 ; 4)$ ; produits $4, 3, 1, 8$, de somme 16 ; $\frac{16}{4} = 4$.
- g) $s_x^2 = \frac{4 + 1 + 1 + 4}{4} = 2{,}5$, $s_y^2 = \frac{4 + 9 + 1 + 16}{4} = 7{,}5$ ; $r = \frac{4}{\sqrt{18{,}75}} \approx 0{,}924$.
- h) Les sommes valent $4, 4, 10, 14$, de moyenne 8 ; écarts $-4, -4, 2, 6$ ; $\frac{16 + 16 + 4 + 36}{4} = 18$.

Pour la copie : $2{,}5 + 7{,}5 + 2 \times 4 = 18$. Les quatre points montent presque en ligne droite : 0,92 est cohérent.

**Erreurs fréquentes.** Diviser la covariance par le produit des variances ; oublier le facteur 2 du terme croisé ; retrancher $\mathbb{V}(Y)$ pour une différence ; multiplier par $2^2$ dans e.

**Variante.** $\mathbb{V}(X + 2Y)$ ? *Réponse* : $4 + 4 \times 9 + 2 \times 2 \times 3 = 52$.

### Ex M02c.10 — La matrice de covariance de trois variables : la lire et la vérifier

**Réponses** : a) `9` · b) `-1` · c) `"1/3"` · d) `True` · e) `16` · f) `7` · g) `"B"` · h) `9`.

**Démarche.**
- a) La case $(2, 2)$ : 9. b) La case $(1, 3)$ : $-1$.
- c) $\frac{2}{\sqrt{4}\sqrt{9}} = \frac{2}{6} = \frac{1}{3}$. d) $\Sigma_{23} = 0$ : oui.
- e) La somme de toutes les cases : $4 + 9 + 1 + 2 \times (2 - 1 + 0) = 16$.
- f) $4 + 1 - 2 \times (-1) = 7$.
- g) $\mathbf{A}$ n'est pas symétrique ; $\mathbf{C}$ donnerait $\rho = \frac{7}{2 \times 3} > 1$ ; $\mathbf{B}$ donne $\rho = \frac{-3}{6} = -0{,}5$ : **B**.
- h) Diagonale : $1 \times 4 + 1 \times 9 + 4 \times 1 = 17$ ; hors diagonale, $2\big(w_1w_2\Sigma_{12} + w_1w_3\Sigma_{13} + w_2w_3\Sigma_{23}\big) = 2\big(-2 - 2 + 0\big) = -8$ ; total 9.

Pour la copie : la matrice de corrélation a des 1 sur la diagonale, $\rho_{12} = \frac{1}{3}$, $\rho_{13} = \frac{-1}{2 \times 1} = -\frac{1}{2}$, $\rho_{23} = 0$.

**Erreurs fréquentes.** Lire un écart-type sur la diagonale ; compter chaque covariance une seule fois ; oublier les termes hors diagonale en h (17).

**Variante.** $\mathbb{V}(X_2 + 3X_3)$ ? *Réponse* : $9 + 9 \times 1 + 2 \times 3 \times 0 = 18$.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex M02c.11 — Pourquoi diviser par n − 1 : E[S²] = σ²

**Réponse modèle.**
1. On écrit $X_i - \mu = (X_i - \bar{X}) + (\bar{X} - \mu)$ et on développe : $\sum_i (X_i - \mu)^2 = \sum_i (X_i - \bar{X})^2 + 2(\bar{X} - \mu)\sum_i (X_i - \bar{X}) + n(\bar{X} - \mu)^2$. Le terme du milieu est nul car $\sum_i (X_i - \bar{X}) = \sum_i X_i - n\bar{X} = 0$. D'où l'identité.
2. $\mathbb{E}\big[(X_i - \mu)^2\big] = \mathbb{V}(X_i) = \sigma^2$ par définition de la variance ; $\mathbb{E}\big[(\bar{X} - \mu)^2\big] = \mathbb{V}(\bar{X}) = \frac{\sigma^2}{n}$, car $\mathbb{E}[\bar{X}] = \mu$ et, les $X_i$ étant **indépendantes**, $\mathbb{V}(\bar{X}) = \frac{n\sigma^2}{n^2}$ (fiche §3).
3. Par linéarité de l'espérance appliquée à l'identité : $\mathbb{E}\big[\sum_i (X_i - \bar{X})^2\big] = n\sigma^2 - n\,\frac{\sigma^2}{n} = (n - 1)\sigma^2$. Donc $\mathbb{E}[S_n^2] = \frac{n - 1}{n}\sigma^2$ et $\mathbb{E}[S^2] = \frac{(n - 1)\sigma^2}{n - 1} = \sigma^2$.
4. $\text{biais}(S_n^2) = \frac{n - 1}{n}\sigma^2 - \sigma^2 = -\frac{\sigma^2}{n}$, qui tend vers 0 : $S_n^2$ sous-estime $\sigma^2$, de moins en moins.
5. Avec $n = 1$ : $\bar{X} = X_1$, donc $S_n^2 = 0$, et $S^2 = \frac{0}{0}$ n'est pas défini. Une seule valeur ne dit rien de l'écart entre les valeurs : l'écart à $\bar{X}$ est nul par construction, et l'écart à $\mu$ est inconnu.
6. Au calcul de $\mathbb{V}(\bar{X}) = \frac{\sigma^2}{n}$ (question 2), qui utilise $\mathbb{V}(\sum X_i) = \sum \mathbb{V}(X_i)$.
7. Si $\mu$ est connu, $\mathbb{E}\big[\frac{1}{n}\sum_i (X_i - \mu)^2\big] = \frac{1}{n} \times n\sigma^2 = \sigma^2$ : sans biais. Le terme $-n(\bar{X} - \mu)^2$ de l'identité vient de ce qu'on mesure les écarts depuis $\bar{X}$, estimé sur les mêmes données, au lieu de $\mu$ : il « consomme » une valeur, d'où $n - 1$.

**Grille.** Une bonne démonstration : (1) développe le carré autour de $\bar{X}$ et justifie que le terme croisé est nul ; (2) identifie $\mathbb{E}[(X_i - \mu)^2]$ comme une variance et calcule $\mathbb{E}[(\bar{X} - \mu)^2] = \frac{\sigma^2}{n}$ en citant l'indépendance ; (3) applique la linéarité de l'espérance et conclut pour $S_n^2$ et $S^2$ ; (4) donne le biais $-\frac{\sigma^2}{n}$ et sa limite ; (5) discute $n = 1$ ; (6) situe l'usage de l'indépendance ; (7) explique l'origine du $n - 1$.

### Ex M02c.12 — La variance de la moyenne : V(X̄) = σ²/n, et l'erreur type

**Réponse modèle.**
1. Par linéarité de l'espérance, $\mathbb{E}[\bar{X}] = \frac{1}{n}\sum_i \mathbb{E}[X_i] = \frac{n\mu}{n} = \mu$. La linéarité ne demande **pas** l'indépendance.
2. $\mathbb{V}(\bar{X}) = \mathbb{V}\big(\frac{1}{n}\sum_i X_i\big) = \frac{1}{n^2}\,\mathbb{V}\big(\sum_i X_i\big)$ (une constante sort au carré) $= \frac{1}{n^2}\sum_i \mathbb{V}(X_i)$ (variables indépendantes, M02b §6) $= \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}$.
3. $\sigma(\bar{X}) = \frac{\sigma}{\sqrt{n}}$ ; $\sigma$ est inconnu, on le remplace par son estimation $s$, d'où $\frac{s}{\sqrt{n}}$. Avec 100 fois plus de données, $s$ reste du même ordre (il estime la dispersion des données, qui ne change pas), tandis que l'erreur type est divisée par $\sqrt{100} = 10$.
4. $\mathbb{V}\big(\sum_i X_i\big) = \sum_i \mathbb{V}(X_i) + \sum_{i \ne j}\operatorname{Cov}(X_i, X_j) = n\sigma^2 + n(n - 1)\rho\sigma^2$ ($n(n - 1)$ couples ordonnés, chacun de covariance $\rho\sigma^2$). En divisant par $n^2$ : $\mathbb{V}(\bar{X}) = \frac{\sigma^2}{n} + \frac{n - 1}{n}\rho\sigma^2 = \sigma^2\big(\frac{1}{n} + (1 - \frac{1}{n})\rho\big)$.
5. Elle tend vers $\rho\sigma^2$, et non vers 0 : la part commune des erreurs ne se moyenne pas. Moyenner 1 000 modèles très corrélés ($\rho = 0{,}9$) laisse 90 % de la variance d'un seul : il faut des modèles **peu corrélés** (c'est l'idée des forêts aléatoires, chapitre 14 de workbookIA).
6. Avec $\rho = -\frac{1}{N - 1}$ : $\sigma^2\big(\frac{1}{n} - \frac{n - 1}{n(N - 1)}\big) = \frac{\sigma^2}{n}\cdot\frac{N - 1 - (n - 1)}{N - 1} = \frac{\sigma^2}{n}\cdot\frac{N - n}{N - 1}$.

**Grille.** (1) linéarité, et remarque qu'elle se passe d'indépendance ; (2) les trois étapes justifiées : constante au carré, indépendance, calcul ; (3) la différence entre écart-type des données et erreur type, avec le facteur 10 ; (4) le compte des $n(n - 1)$ couples et le calcul ; (5) la limite $\rho\sigma^2$ et son interprétation ; (6) la vérification algébrique.

<a id="reflexion"></a>

## 🔗 📖 ⚖️ 🗣️ Pont, lecture, éthique et explication

### Ex M02c.13 — Le 99e percentile d'une latence : l'estimer et dire son incertitude

**Réponses** : a) `989.01` · b) `179.03` · c) `290.122` · d) `10` · e) `3.146` · f) `184.21` · g) `10000`.

**Démarche.**
- a) $0{,}99 \times 999 = 989{,}01$. b) Entre $x_{(989)} = 179$ et $x_{(990)} = 182$ : $179 + 0{,}01 \times 3 = 179{,}03$ ms.
- c) Position $0{,}999 \times 999 = 998{,}001$ : $290 + 0{,}001 \times 122 = 290{,}122$ ms.
- d) Chaque mesure dépasse $q_{0{,}99}$ avec la probabilité 0,01 : en moyenne $1\,000 \times 0{,}01 = 10$.
- e) Ce nombre suit $\mathcal{B}(1\,000 ;\ 0{,}01)$ : $\sqrt{1\,000 \times 0{,}01 \times 0{,}99} = \sqrt{9{,}9} \approx 3{,}146$.
- f) $P(T > q) = e^{-q/40} = 0{,}01$, donc $q = 40\ln 100 \approx 184{,}21$ ms.
- g) $n \times 0{,}001 = 10$ : $n = 10\,000$.

Pour la copie : le p99,9 de 1 000 mesures repose sur les **deux** plus grandes (290 et 412), et presque entièrement sur la 999ᵉ. Une heure sans requête exceptionnelle, puis une heure avec une seule réponse à 400 ms, et le p99,9 saute de 100 ms. On propose : l'afficher seulement sur des fenêtres de plus de 10 000 mesures, l'accompagner d'un intervalle (bootstrap, fiche §7), ou suivre le p99, plus stable.

**Erreurs fréquentes.** Position $p \times n = 990$ au lieu de $p(n - 1)$ ; ne pas interpoler ; donner la variance en e ; en f, prendre $\lambda = 40$ au lieu de $\frac{1}{40}$.

**Variante.** La médiane d'une loi exponentielle d'espérance 40 ms ? *Réponse* : $40\ln 2 \approx 27{,}7$ ms : le p99 vaut presque 7 fois la médiane.

### Ex M02c.14 — Standardiser des features avec les statistiques du seul train

**Réponses** : a) `14.0` · b) `2.828` · c) `2.121` · d) `-0.354` · e) `14.714` · f) `1.632` · g) `0.0`.

**Démarche.**
- a) $\frac{70}{5} = 14$. b) Écarts $-4, -2, 0, 2, 4$ ; $\frac{40}{5} = 8$ ; $s_n = \sqrt{8} \approx 2{,}828$.
- c) $\frac{20 - 14}{2{,}828} \approx 2{,}121$. d) $\frac{13 - 14}{2{,}828} \approx -0{,}354$.
- e) $\frac{70 + 33}{7} \approx 14{,}714$.
- f) Avec les 7 valeurs, $s_n \approx 3{,}239$ : $\frac{20 - 14{,}714}{3{,}239} \approx 1{,}632$.
- g) Par construction, des valeurs standardisées avec leurs propres moyenne et écart-type ont une moyenne nulle.

Pour la copie : f) est plus petit parce que la valeur 20 elle-même a tiré la moyenne vers le haut et gonflé l'écart-type : l'exemple de test a influencé sa propre transformation. En production, un exemple arrive seul : on ne peut le standardiser qu'avec des statistiques calculées **avant**, sur l'entraînement. Standardiser avec le test donne au modèle une information qu'il n'aura jamais en production : son score de test est trop optimiste (une fuite de données, chapitres 8 et 12 de workbookIA).

**Erreurs fréquentes.** L'écart-type divisé par $n - 1$ (3,162) ; standardiser le test avec ses propres statistiques ; oublier le signe en d.

**Variante.** La valeur standardisée de l'exemple de test 13 avec les statistiques des 7 valeurs ? *Réponse* : $\frac{13 - 14{,}714}{3{,}239} \approx -0{,}529$.

### Ex M02c.15 — MML §6.4 : moyennes et covariances empiriques, en anglais

**Éléments de réponse** (ta formulation compte, pas la nôtre).
1. La **médiane** et le **mode**. Pour la série de M02c.1 : la médiane (43,5) a un sens ; le mode n'en a pas vraiment, toutes les valeurs étant différentes.
2. La moyenne empirique est la moyenne arithmétique des $N$ vecteurs ; la covariance empirique, la moyenne des produits $(\mathbf{x}_n - \bar{\mathbf{x}})(\mathbf{x}_n - \bar{\mathbf{x}})^\top$, divisée par $N$. Le livre signale que c'est une estimation biaisée, et que la version corrigée divise par $N - 1$ (fiche §6).
3. Pour $D = 1$, le produit d'un écart par lui-même est son carré : on retrouve $s_n^2$. Pour $D = 2$, une matrice $2 \times 2$ : les deux variances sur la diagonale, la covariance des deux coordonnées dans les deux autres cases.
4. La covariance joue le rôle d'un **produit scalaire** entre variables aléatoires, la variance celui du carré d'une **norme**, l'écart-type celui de la **longueur** ; la corrélation est le **cosinus de l'angle** entre deux variables.
5. $\mathbf{u} = (-3, -1, 1, 3)$, $\mathbf{v} = (-3{,}5 ;\ 0{,}5 ;\ -0{,}5 ;\ 3{,}5)$ : $\cos\theta = \frac{20}{\sqrt{20} \times 5} \approx 0{,}894$, donc $\theta \approx 26{,}6°$.
6. Une corrélation nulle : des vecteurs d'écarts **orthogonaux** (angle de 90°) ; une corrélation de $-1$ : des vecteurs de sens opposés (angle de 180°), les points sont alignés sur une droite décroissante.
7. Personnel. Mots fréquents : *empirical* (empirique), *sample mean*, *biased estimate*, *uncorrelated* (non corrélées), *inner product*, *orthogonal*.

### Ex M02c.16 — Le biais du survivant : des données qui ne montrent que ceux qui restent

**Éléments de réponse.**
1. Le modèle n'a vu que les demandes **acceptées** par les anciennes règles ; il sera utilisé sur **toutes** les demandes, y compris celles que ces règles refusaient. On n'observe le résultat que pour ceux qui ont « survécu » au filtre des anciennes décisions.
2. Le jeu de test vient du même historique filtré : il mesure la performance sur les clients autrefois acceptés, pas sur la population où le modèle décidera. Une bonne accuracy sur une population biaisée ne dit rien sur les autres.
3. Les profils autrefois refusés sont presque absents des données : le modèle ne sait rien d'eux, et risque de reproduire les anciens refus (ou de se tromper au hasard sur eux). Des décisions passées injustes deviennent des données, puis un modèle « objectif » qui les prolonge : c'est un problème d'équité, parce que des groupes entiers sont mal traités de façon systématique, pas seulement plus souvent mal classés.
4. Non : plus d'exemples réduisent la **variance** de l'estimation, pas son **biais**. Un million de prêts acceptés de plus donnent une estimation très précise de la mauvaise quantité.
5. Par exemple : accorder une petite part de prêts au hasard parmi les demandes qu'on aurait refusées, pour observer leur remboursement (cela coûte des défauts de paiement) ; utiliser d'autres sources (les données d'autres prêteurs, les remboursements de crédits ailleurs), avec leurs propres biais ; corriger par des méthodes de repondération ou d'inférence des refusés (*reject inference*), qui reposent sur des hypothèses fortes ; et dans tous les cas, mesurer la performance par groupe.

### Ex M02c.17 — Expliquer le théorème central limite avec un histogramme

**Exemple de réponse.**

> Non : les données, elles, gardent leur loi, même avec un million de valeurs ; si les durées sont très asymétriques, leur histogramme le reste. Le théorème parle de la **moyenne** (ou de la somme) de beaucoup de valeurs indépendantes : si je refais l'expérience des milliers de fois et que je trace l'histogramme des moyennes, il prend la forme d'une cloche. Quand $n$ grandit, ce histogramme reste centré sur la vraie moyenne, devient plus étroit (comme $\frac{1}{\sqrt{n}}$), et de plus en plus symétrique. Il faut que les valeurs soient indépendantes et que leur loi ait une variance. On ne suppose donc pas que tout est gaussien : on utilise le fait que les **moyennes** le sont presque, et c'est justement une moyenne qu'on calcule pour un intervalle de confiance ou un score de test.

**Grille.** Une bonne réponse : (1) le théorème porte sur la moyenne ou la somme, pas sur les données ; (2) quand $n$ grandit : même centre, largeur en $\frac{1}{\sqrt{n}}$, forme de cloche ; (3) une condition (indépendance, variance finie) ; (4) le lien avec les intervalles de confiance ; (5) huit lignes au plus, sans formule compliquée.

<a id="entretien"></a>

## 💼 Entretien

### M02c.E1 — L'erreur type décroît en 1/√n : qu'est-ce que cela change pour un jeu de test ?

**Réponse modèle (60 secondes).**

> Sur 500 exemples, une accuracy de 87 % a une erreur type d'environ $\sqrt{0{,}87 \times 0{,}13 / 500} \approx 1{,}5$ point : son intervalle à 95 % va d'environ 84 à 90 %. L'écart de 2 points entre les deux versions est du même ordre que l'incertitude de chaque score, donc je ne l'annoncerais pas comme une amélioration. Pour diviser l'erreur type par 2, il faut 4 fois plus d'exemples, car elle décroît en $1/\sqrt{n}$ : pour une erreur type d'un demi-point, il faut de l'ordre de 4 500 exemples. Mais la meilleure option est souvent de comparer les deux modèles **sur les mêmes exemples** : leurs erreurs sont corrélées, et ce qui compte, ce sont les exemples où ils ne sont pas d'accord. Un test apparié, comme celui de McNemar, ou un bootstrap de la différence sur les mêmes exemples, tranche avec beaucoup moins de données. Et je vérifierais que le jeu de test ressemble à la production.

**Grille.** (1) l'erreur type chiffrée (environ 1,5 point) et l'intervalle ; (2) la conclusion : écart non significatif ; (3) la décroissance en $\frac{1}{\sqrt{n}}$ : 4 fois plus pour 2 fois moins d'erreur, et un ordre de grandeur de taille ; (4) la comparaison appariée sur les mêmes exemples ; (5) un mot sur la représentativité du jeu de test.

<a id="notebook"></a>

## Notebook

### Ex M02c.18 — La distribution des moyennes d'échantillons · `sample_means`

**Réponses** : a) `[4.0, 3.25, 3.0]` · b) `500` · c) `1.99` · d) `0.9` · e) `0.5` · f) `"ValueError"` · g) `"ndarray"` · h) `0.95`.

**Démarche.** Tester `n < 1 or repeats < 1` d'abord (`raise ValueError(...)`), puis `rng = np.random.default_rng(seed)` **une seule fois**, et `np.array([float(np.mean(draw(rng, n))) for _ in range(repeats)], dtype=float)`. Pour la copie : c) 1,99 pour $\mu = 2$ ; d) 0,90 pour $\frac{2}{\sqrt{5}} \approx 0{,}894$ ; e) 0,50 pour $\sqrt{\frac{5}{20}}$ ; h) 0,949 pour 0,95 : avec 30 valeurs, la loi normale prédit déjà bien la proportion.

**Erreurs fréquentes.** Créer le générateur dans la boucle (tous les échantillons sont alors identiques : a) donne trois fois la même moyenne) ; ignorer la graine reçue ; renvoyer la somme de chaque échantillon ; renvoyer une liste.

### Ex M02c.19 — Biais et erreur quadratique d'un estimateur, par simulation · `estimator_bias, estimator_mse`

**Réponses** : a) `-0.8` · b) `0.01` · c) `5.8` · d) `8.1` · e) `5.2` · f) `"ValueError"` · g) `"float"` · h) `-1.68`.

**Démarche.** Une fonction auxiliaire `_estimates(estimator, draw_sample, repeats, seed)` : tester `repeats < 1`, puis `rng = np.random.default_rng(seed)` et `np.array([float(estimator(draw_sample(rng))) for _ in range(repeats)])`. Le biais : `float(np.mean(estimates) - true_value)` ; l'erreur quadratique : `float(np.mean((estimates - true_value) ** 2))`. Pour la copie : a) $-0{,}80$ pour $-\frac{4}{5}$, b) 0,01 pour 0, c) 5,8 pour 5,76, d) 8,1 pour 8 ; e) est la variance de $S_n^2$ (5,12 en théorie). Sur l'erreur quadratique, la variance divisée par $n$ gagne. h) $-1{,}68$ pour $-\frac{10}{6} \approx -1{,}67$ (fiche §6).

**Erreurs fréquentes.** Oublier de retrancher la vraie valeur (a donne 3,20) ; mesurer les écarts à la moyenne des estimations dans l'erreur quadratique (on obtient la variance, 5,18) ; élever au carré l'erreur moyenne (0,63) ; un générateur par échantillon.

### Ex M02c.20 — Erreur type et intervalle de confiance · `standard_error, confidence_interval_mean`

**Réponses** : a) `1.2247` · b) `1.0954` · c) `[11.5995, 16.4005]` · d) `[11.9853, 16.0147]` · e) `"ValueError"` · f) `"ValueError"` · g) `"tuple"` · h) `2.07`.

**Démarche.** `standard_error` : `x = np.asarray(sample, dtype=float)`, `n = len(x)`, `if n <= ddof: raise ValueError(...)`, puis `math.sqrt(np.sum((x - x.mean()) ** 2) / (n - ddof)) / math.sqrt(n)`. `confidence_interval_mean` : tester `len(sample) < 2` et `z <= 0`, puis `m = float(np.mean(sample))`, `se = standard_error(sample)` et `(m - z * se, m + z * se)`. Pour la copie : $\bar{x} = 14$, somme des carrés des écarts 30, $s = \sqrt{7{,}5} \approx 2{,}739$, erreur type $\approx 1{,}2247$, intervalle $14 \pm 2{,}4005$. h) 2,07 et non 1,96, car $s \approx 10{,}6$ sur ces 400 valeurs, pas exactement $\sigma = 10$.

**Erreurs fréquentes.** Diviser par $n$ au lieu de $\sqrt{n}$ ; oublier la racine de la variance ; `ddof=0` par défaut ; renvoyer une liste ; laisser `[5.0]` provoquer une division par zéro.

### Ex M02c.21 — NumPy et SciPy : `ddof`, `np.percentile`, `scipy.stats.sem`

**Réponses** : a) `16.755` · b) `4.326` · c) `30.6` · d) `31.0` · e) `5.5` · f) `1` · g) `30.6` · h) `0.9661`.

**Démarche.** a) `np.std(DATA_21, ddof=1)` ; b) `stats.sem(DATA_21)` (= a) divisé par $\sqrt{15}$) ; c) `np.percentile(DATA_21, 90)` ; d) `np.percentile(DATA_21, 90, method="nearest")` ; e) `stats.iqr(DATA_21)` ; f) barrières $22{,}5 - 8{,}25 = 14{,}25$ et $28 + 8{,}25 = 36{,}25$ : seule 88 est dehors ; g) `np.quantile(DATA_21, 0.9)` ; h) $\sqrt{\frac{14}{15}}$. Pour la copie : la position du percentile 90 est $0{,}9 \times 14 = 12{,}6$, entre $x_{(12)} = 30$ et $x_{(13)} = 31$ : 30,6 ; `nearest` prend la position 13.

**Erreurs fréquentes.** `np.std` sans `ddof=1` (16,187) ; diviser `stats.sem` par $\sqrt{n}$ une seconde fois ; `np.percentile(DATA_21, 0.9)` (le percentile 0,9 : 19,126) ; confondre l'échelle de `np.quantile` (0 à 1) et celle de `np.percentile` (0 à 100).

### Ex M02c.22 — Prédire : l'histogramme des moyennes d'une loi exponentielle quand n grandit

**Réponses** : a) `2` · b) `1` · c) `2` · d) `2`.

**Démarche.** a) $\sigma(\bar{X}_n) = \frac{1}{\sqrt{n}}$ : de 0,5 à 0,25, divisé par 2. b) $\mathbb{E}[\bar{X}_n] = 1$ pour tout $n$. c) Pour $n = 1$, l'histogramme est la densité $e^{-x}$ : maximum en 0, longue queue à droite. d) La médiane vaut $\ln 2 \approx 0{,}69 < 1$. Pour la copie : la médiane des moyennes remonte vers 1 (0,92 pour $n = 4$, 0,996 pour $n = 64$) : la distribution se symétrise, en gardant une légère asymétrie.

**Erreurs fréquentes.** Croire que la largeur diminue comme $\frac{1}{n}$ (choix 3) ; croire que le centre bouge ; attendre une cloche dès $n = 1$.

### Ex M02c.23 — Couverture : 95 % des intervalles contiennent-ils la vraie moyenne ?

**Réponses** : a) `0.933` · b) `0.87` · c) `0.941` · d) `0.877` · e) `0.947`.

**Démarche.** `means = samples.mean(axis=1)`, `half = z * samples.std(axis=1, ddof=1) / math.sqrt(samples.shape[1])`, puis `np.mean((means - half <= true_mean) & (true_mean <= means + half))`. Pour la copie : l'aléa est d'environ 0,002 ; a), b), c) et d) sont nettement sous leur niveau. b) est la plus basse : avec 10 valeurs d'une loi très asymétrique, la moyenne n'est pas encore normale, et $s$ est petit justement quand $\bar{x}$ l'est (les deux dépendent des rares grandes valeurs). c) remonte car 100 valeurs rendent la moyenne presque normale. e) corrige l'incertitude de $s$ pour des données **normales** (2,093 au lieu de 1,96).

**Erreurs fréquentes.** `ddof=0` (a donne 0,925) ; utiliser $s$ au lieu de $\frac{s}{\sqrt{n}}$ (couverture 1) ; une boucle sur les lignes (juste, mais lente) ; calculer sur les colonnes (`axis=0`).

### Ex M02c.24 — Grande dimension : le cube dont le centre est vide

**Réponses** : a) `0.7849` · b) `0.5242` · c) `0.0023` · d) `0.639` · e) `0.00249` · f) `0`.

**Démarche.** `np.mean(np.sum(points ** 2, axis=1) <= 1)` ; `np.mean(np.max(np.abs(points), axis=1) > 1 - eps)` ; `math.pi ** (d / 2) / math.gamma(d / 2 + 1) / 2 ** d`. Pour la copie : a), b), d) sont à quelques millièmes de $\frac{\pi}{4} \approx 0{,}7854$, $\frac{\pi}{6} \approx 0{,}5236$ et 0,6415 (l'erreur type d'une proportion proche de 0,5 sur 100 000 points vaut environ 0,0016). c) 0,0023 contre 0,00249 : l'erreur type d'une proportion de 0,0025 sur 100 000 points vaut 0,00016, l'écart en fait un peu plus d'une : normal. En dimension 20, la boule occupe $2{,}5 \times 10^{-8}$ du cube : il faut en moyenne 40 millions de points pour en voir un ; avec 100 000, on n'en voit aucun, et Monte-Carlo est inutilisable (erreur relative $\frac{1}{\sqrt{Np}}$).

**Erreurs fréquentes.** Comparer la somme des carrés à $\frac{1}{4}$ (une boule de rayon $\frac{1}{2}$) ; utiliser le minimum des valeurs absolues dans `border_fraction` (toutes les coordonnées près du bord, presque jamais) ; oublier de diviser par $2^d$.

### Ex M02c.25 — Voir le théorème central limite : histogrammes et densité normale

**Démarche.** Pour chaque `ax, n` : `means = mymath.estimation.sample_means(draw, n, repeats, seed)`, `ax.hist(means, bins=60, density=True)`, puis `grid = np.linspace(mu - 4 * w, mu + 4 * w, 300)` avec `w = sigma / math.sqrt(n)`, `ax.plot(grid, stats.norm(mu, w).pdf(grid))` et `ax.set_title(f"n = {n}")`. Pour la copie : pour $n = 1$, la cloche $\mathcal{N}(1, 1)$ n'a rien à voir avec la densité $e^{-x}$ (elle met même du poids sur des valeurs négatives) ; pour $n = 10$, le sommet de l'histogramme est à gauche de 1, et l'écart se voit surtout dans les queues ; pour $n = 50$, la cloche décrit bien le centre.

**Erreurs fréquentes.** Oublier `density=True` (l'histogramme compte des effectifs, la densité est minuscule à côté) ; tracer $\mathcal{N}(\mu, \sigma^2)$ au lieu de $\mathcal{N}\big(\mu, \frac{\sigma^2}{n}\big)$ ; une grille trop étroite pour $n = 1$ ; ouvrir une nouvelle figure dans la fonction.

### Ex M02c.26 — Chasse à l'erreur : un intervalle de confiance mal calculé

**Réponses** : a) `"ABDE"` · b) `[3.92, 3.92, 3.29, 5.152, 3.92, 0.02]`.

**Démarche.** (A) divise par $n$ au lieu de $\sqrt{n}$ : 0,784 au lieu de $1{,}96 \times 2 = 3{,}92$. (B) multiplie la variance $s^2 = 100$ au lieu de l'écart-type : 39,2. (D) garde 1,96 à 99 % : $2{,}576 \times 2 \approx 5{,}152$. (E) oublie le $\sqrt{n}$ : $[30{,}4 ; 69{,}6]$ contient environ 95 % des **durées** (si elles sont à peu près normales), pas la moyenne ; la bonne demi-largeur est 3,92. (C) et (F) sont justes : $1{,}645 \times 2 = 3{,}29$ et $\sqrt{\frac{0{,}16}{400}} = 0{,}02$. Pour la copie : l'intervalle de (E) a un sens, mais pour une autre question : où tombera une **nouvelle** durée (un intervalle de prédiction).

**Erreurs fréquentes.** Accuser (C) (1,645 est bien le quantile de 90 %) ou (F) ; donner pour (D) la valeur à 95 %.

### Ex M02c.27 — Tester une fonction aléatoire : une tolérance en erreurs types

**Démarche.** `pi_standard_error(n)` : `p = math.pi / 4`, puis `4 * math.sqrt(p * (1 - p) / n)` (le 4 vient de ce que l'estimation est 4 fois une proportion). `TOLERANCE_K = 5` (ou 4) : une fausse alarme a la probabilité $2(1 - \Phi(5)) \approx 6 \times 10^{-7}$ (ou $6 \times 10^{-5}$), et la copie fausse, à 12 erreurs types, reste toujours dehors. `pi_test` : `abs(estimate(n, np.random.default_rng(seed)) - math.pi) <= TOLERANCE_K * pi_standard_error(n)`. Pour la copie : avec $k = 1$, la bonne fonction échoue environ une fois sur trois ($2(1 - \Phi(1)) \approx 0{,}32$) : un test instable ; avec `k=50`, même la copie au rayon de 0,99 (biais d'environ $-0{,}063$, 12 erreurs types) passe. Le décalage de 0,002 vaut 0,4 erreur type pour 100 000 points : il faudrait de l'ordre de 11 millions de points pour que 4 erreurs types descendent sous 0,002, et davantage pour l'attraper à coup sûr.

**Erreurs fréquentes.** Oublier le facteur 4 dans l'erreur type (tolérance 4 fois trop étroite : la bonne fonction échoue souvent) ; $k = 2$ ou 3 (des fausses alarmes sur des milliers de tests) ; une tolérance fixe sans lien avec $n$ ; créer le générateur sans la graine reçue (le test n'est plus reproductible) ; renvoyer le texte `"True"` au lieu du booléen.

### Ex M02c.28 — Défi : un intervalle à 95 % avec dix valeurs d'une loi asymétrique

**Démarche.** La remarque clé : $\frac{X_i}{\mu}$ suit la loi exponentielle de moyenne 1, donc la loi de $\frac{\bar{X}}{\mu}$ est **la même pour tous les $\mu$** (un **pivot**). On la simule une fois (200 000 moyennes de 10 exponentielles de moyenne 1 ; avec quelques milliers seulement, l'aléa sur les percentiles fait sortir la couverture de la fenêtre environ une fois sur 13 avec 2 000 moyennes, une fois sur 4 avec 1 000), on lit ses quantiles $q_{0{,}025} \approx 0{,}48$ et $q_{0{,}975} \approx 1{,}71$, et $q_{0{,}025} \le \frac{\bar{X}}{\mu} \le q_{0{,}975}$ s'inverse en $\frac{\bar{X}}{q_{0{,}975}} \le \mu \le \frac{\bar{X}}{q_{0{,}025}}$, soit environ $[0{,}58\,\bar{x} ;\ 2{,}09\,\bar{x}]$. Couverture mesurée : 0,949, largeur moyenne 1,51 $\mu$. La loi de $\frac{\bar{X}}{\mu}$ a d'ailleurs une formule, une loi gamma (`stats.gamma(10, scale=1/10)`), qui donne les mêmes quantiles. Pour la copie : l'intervalle est asymétrique, plus long vers le haut, comme la loi elle-même ; le bootstrap des percentiles couvre environ 86 fois sur 100, car la loi empirique de 10 valeurs n'a presque jamais la longue queue de la vraie loi.

**Erreurs fréquentes.** Le bootstrap des percentiles ou l'intervalle de Student (couverture 0,86 et 0,90) ; un bootstrap écrit avec une boucle Python sur les rééchantillons (plus d'une minute : `sample[rng.integers(0, 10, (2000, 10))]` les tire d'un coup) ; un intervalle d'une seule borne $[0 ;\ c\,\bar{x}]$, qui couvre mais est trop large (environ 1,85 $\mu$) ; simuler le pivot à chaque appel (lent) ; un intervalle qui dépend d'une échelle fixée d'avance.
