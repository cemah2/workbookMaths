# M05a · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m05a_derivees_taylor/06_mes_reponses.md` (créée par `python tools/start_chapter.py M05a`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Pour une étude de fonction, écris $f'$ et $f''$ factorisées et leurs tableaux de signes ; pour une approximation, écris aussi son erreur ; garde les valeurs exactes ($\frac{19}{6}$, $\sqrt{10}$, $e$) jusqu'au bout. Les formules s'écrivent en LaTeX entre `$` (R0 §5) ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M05a.Q1 — Le signe de la dérivée seconde

1. 
2. 
3. 
4. 
5. 
6. 

### M05a.Q2 — Local ou global ?

1. 
2. 
3. 
4. 
5. 
6. 

### M05a.Q3 — Taylor : quel ordre, quelle précision ?

1. 
2. 
3. 
4. 
5. 
6. 

### M05a.Q4 — Newton converge-t-il ?

1. 
2. 
3. 
4. 
5. 
6. 

### M05a.Q5 — Différence avant ou centrée ?

1. 
2. 
3. 
4. 
5. 
6. 

### M05a.Q6 — Les flottants : vrai ou faux

1. 
2. 
3. 
4. 
5. 
6. 

### M05a.Q7 — Overflow, underflow, log-sum-exp

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M05a.R1 — Dérivées et variations (R7)

1. 
2. 
3. 
4. 
5. 

### M05a.R2 — Suites définies par récurrence (R5)

1. 
2. 
3. 
4. 
5. 

### M05a.R3 — Log-probabilités et log-sum-exp (M04)

1. 
2. 
3. 
4. 
5. 

## ✏️ Papier-crayon

### Ex M05a.1 — Dérivées secondes et convexité

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Le tableau de signes de g'' ; le signe de h) ; le même écart pour ln avec les points 1 et 3 :

### Ex M05a.2 — Extrema locaux et globaux sur un intervalle fermé

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- f'(x) factorisée et f'' en chaque point critique ; le tableau de variations sur [−2, 3] ; pourquoi le maximum global de d) n'annule pas f' :

### Ex M05a.3 — Points d'inflexion et test de la dérivée seconde

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- p' et p'' factorisées, leurs tableaux de signes ; pourquoi p''(0) = 0 ne donne pas un point d'inflexion en 0 :

### Ex M05a.4 — Polynômes de Taylor de trois fonctions usuelles

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- d), e) et g) comparés aux valeurs exactes ; le polynôme de h) en entier, développé, et ce que je retrouve :

### Ex M05a.5 — Le reste de Taylor : borner l'erreur d'une approximation

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- La borne comparée à l'erreur vraie ; les factorielles de d) ; pourquoi le reste d'ordre 4 en c), et ce qu'on y gagne :

### Ex M05a.6 — Newton à la main : une racine carrée en trois pas

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- L'itération écrite à partir de la formule de Newton ; l'identité exacte de l'erreur, et ce qu'elle explique pour e) ; la racine que cherche h) :

### Ex M05a.7 — L'erreur d'une différence avant et d'une différence centrée, par Taylor

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- f', f'' et f''' ; l'erreur de e) comparée à f) ; ce que h) approche, et à quel ordre :

### Ex M05a.8 — Les flottants : 0,1 en binaire, epsilon machine, nombres représentables

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- Les multiplications par 2 de a) et c), les fractions de b) ; pourquoi l'écart double à chaque puissance de 2 ; le nombre de float64 dans [1, 2[ :

### Ex M05a.9 — Le meilleur pas par le calcul : minimiser une borne d'erreur

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- La dérivée de chaque borne et E'(h) = 0 ; la vérification que c'est un minimum ; l'erreur au meilleur pas en δ^(2/3) :

### Ex M05a.10 — log-sum-exp à la main : la softmax stable de trois scores

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- Les étapes de c) ; c) et g) dans l'encadrement m ≤ LSE ≤ m + ln 3 : lequel touche une borne, et pourquoi :

## ∂ Démonstrations

### Ex M05a.11 — La différence centrée est d'ordre 2 : le calcul par Taylor (cas général)

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M05a.12 — Newton double les décimales justes : l'erreur au carré (racine simple)

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M05a.13 — Encadrer le log-sum-exp : max ≤ LSE ≤ max + ln n

1. 
2. 
3. 
4. 
5. 
6. 

## 🔗 📖 🧮 🗣️ Pont, lecture, estimation et explication

### Ex M05a.14 — Pourquoi les bibliothèques de ML calculent log(softmax) d'un seul coup

- a :
- b :
- c :
- d :
- e :
- f :
- Ce que fait -math.log(p2) ; pourquoi la loss de d) est si grande, et pourquoi elle reste utile ; pourquoi une bibliothèque part des scores, en deux phrases :

### Ex M05a.15 — MML §5.1 : dérivée d'une fonction d'une variable et série de Taylor (lecture guidée)

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### Ex M05a.16 — Fermi : l'erreur d'arrondi d'une somme d'un million de nombres

1. 
2. 
3. 
4. 
5. 
6. 

### Ex M05a.17 — Expliquer la convexité et pourquoi elle rassure quand on minimise

*Huit lignes au plus, sans formule compliquée.*

> 

## 💼 Entretien

### M05a.E1 — Pourquoi soustraire le maximum avant de calculer une softmax ?

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M05a.18 — Évaluer un polynôme de Taylor · `taylor_polynomial`

- Les fonctions de a), b) et c), comparées aux vraies valeurs ; b) refait à la main :

### Ex M05a.19 — La méthode de Newton, avec ses cas d'échec · `newton`

- Les trois premiers pas de a) ; le nombre que b) résout ; pourquoi c) échoue ; pourquoi l'ordre des tests compte pour e) :

### Ex M05a.20 — L'extrapolation de Richardson : annuler le terme d'erreur en h² · `richardson_derivative`

- Les dérivées exactes ; D(0,1) et son erreur comparée à g) ; pourquoi d) est exact ; ce que dit e) :

### Ex M05a.21 — L'epsilon machine, en float64, float32 et float16 · `machine_epsilon`

- Le nombre de tours de boucle ; e) expliqué (le milieu entre deux flottants) ; f) expliqué :

### Ex M05a.22 — Un log-sum-exp stable · `logsumexp`

- Le calcul direct pour b) et c) ; b) et h) dans l'encadrement :

### Ex M05a.23 — SymPy `series` et `numpy.finfo` contre tes fonctions

- Le développement de tan affiché ; les dérivées de f) ; f) comparé à e^(sin 0,3) ; pourquoi le plus grand float16 est si petit ; ce qu'il y a entre 0 et tiny :

### Ex M05a.24 — Prédire : Newton depuis un mauvais point de départ

- Mes prédictions avant l'expérience (et pourquoi) ; les tangentes de a) et b) ; les pas de c), d) et e) à la main :

### Ex M05a.25 — Taylor de plus en plus loin : où le polynôme décroche

- L'erreur selon n pour chaque point ; la comparaison au premier terme négligé ; pourquoi x = 1,5 diverge ; le nombre de termes pour 10^(−6) en x = 1 :

### Ex M05a.26 — Une fonction et ses polynômes de Taylor d'ordre 1, 2 et 3

- La largeur où chaque polynôme colle ; la position du polynôme d'ordre 2 ; pourquoi un ordre de plus n'aide pas loin de a :

### Ex M05a.27 — Chasse à l'erreur : une softmax qui renvoie `nan`

- L'erreur de chaque ligne fausse et sa correction ; la ligne qui échoue à l'exécution ; d'où vient le nan :

### Ex M05a.28 — Erreur relative ou absolue : choisir la tolérance d'un test

- Mes tolérances pour les deux tests ; la dissymétrie et le piège d'atol de numpy.isclose :

### Ex M05a.29 — Défi : une racine cubique à 10⁻¹² en le moins d'itérations possible

- L'erreur de mon point de départ ; le nombre de pas prévu par ε_(k+1) ≈ ε_k² ; pourquoi x0 = 1 est si lent pour 10^30 :
