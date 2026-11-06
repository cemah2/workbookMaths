# R6 · Exponentielle et logarithmes — solutions

> Lis une solution **après** avoir vraiment essayé (règle des 15 minutes, puis les indices de `04_indices.md`). Pour chaque exercice : la réponse, la démarche (le *pourquoi*), les erreurs fréquentes et une variante, avec sa réponse, pour vérifier que tu as compris. Pour une démonstration, une **grille de relecture** dit ce que la tienne doit contenir : d'autres rédactions sont justes. Le code complet des exercices du notebook est dans `05_solutions.ipynb`, exécuté.

**Sommaire** : [🧠 Quiz](#quiz) · [🔁 Rappels](#rappels) · [✏️ Papier-crayon](#papier) · [∂ Démonstrations](#demonstrations) · [🔗 🗣️ Pont et explication](#reflexion) · [Notebook](#notebook)

<a id="quiz"></a>

## 🧠 Quiz

### R6.Q1 — Propriétés de l'exponentielle : vrai ou faux
1. **Vrai**.
2. **Faux** : $(e^{a})^{b} = e^{ab}$. Avec $a = 1$ et $b = 3$ : $(e^{1})^{3} = e^{3}$, alors que $e^{1 + 3} = e^{4}$.
3. **Faux** : une exponentielle est toujours strictement positive ; $e^{-x} = \frac{1}{e^{x}} > 0$.
4. **Vrai** : $(ab)^{x} = a^{x} b^{x}$.
5. **Faux** : $e^{x} > 0$ pour tout $x$.
6. **Vrai** (fiche §2).
7. **Vrai** : $4^{1/2} = \sqrt{4} = 2$.

### R6.Q2 — ln d'un produit, d'un quotient, d'une puissance
1. **Vrai**.
2. **Faux** : avec $a = b = 1$, $\ln 2 \approx 0{,}69$ et $\ln 1 + \ln 1 = 0$.
3. **Vrai**.
4. **Vrai**.
5. **Faux** : avec $a = e$, $(\ln e)^{2} = 1$ et $2 \ln e = 2$.
6. **Faux** : $\ln \frac{a}{b} = \ln a - \ln b$.
7. **Vrai** : pour $0 < x < 1$, $x = e^{y}$ avec $y < 0$.

### R6.Q3 — Combien de bits ?
1. **4** questions ($2^{4} = 16$).
2. **20** questions : $2^{19} = 524\,288$ ne suffit pas, $2^{20} = 1\,048\,576$ suffit.
3. **2** bits ($-\log_{2} \frac{1}{4} = 2$).
4. **0** bit : un événement certain n'apprend rien.
5. $2^{7} = $ **128** possibilités.
6. **Vrai** : 1 bit ≈ 0,693 nat, donc une même quantité compte plus de bits que de nats ($I$ bits $= 0{,}693\,I$ nats).

### R6.Q4 — Qui grandit le plus vite ?
1. $1{,}01^{x}$ (exponentielle contre puissance).
2. $x^{0{,}1}$ (puissance contre logarithme, mais très loin : R6.19).
3. $3^{x}$ ($\frac{3^{x}}{2^{x}} = 1{,}5^{x} \to +\infty$).
4. $e^{x}$.
5. $\sqrt{x}$ ($100 \ln x$ reste devant longtemps, mais une puissance finit par gagner).
6. **Vrai** : $10^{3} = 1\,000$ et $1{,}01^{10} \approx 1{,}10$. « Finit par » ne dit rien des petites valeurs.

### R6.Q5 — Lire une échelle logarithmique
1. **Oui** : chaque intervalle est un facteur 10, une décade.
2. **À la moitié**, à peu près : $\log_{10} 3 \approx 0{,}48$.
3. **Non** pour les deux : $\log 0$ et $\log(-5)$ n'existent pas.
4. $10^{2} = $ **100**.
5. Une croissance **exponentielle** : $\log y$ est une fonction affine de $x$.

### R6.Q6 — Sigmoïde : valeurs remarquables et symétrie
1. $\frac{1}{2}$.
2. **Faux** : $\sigma(x) < 1$ toujours, car $e^{-x} > 0$.
3. $1 - 0{,}7 = $ **0,3**.
4. **Vrai** : σ est strictement croissante et $\sigma(0) = \frac{1}{2}$.
5. $\tanh 0 = 0$ ; tanh est **impaire**.
6. $]-1 \;;\; 1[$.

<a id="rappels"></a>

## 🔁 Rappels

### R6.R1 — Suites géométriques (R5)
1. $u_{6} = 5 \times 2^{6} = 320$.
2. $1{,}5^{4} = 5{,}0625$.
3. $1{,}5^{5} \approx 7{,}59 \le 10$ et $1{,}5^{6} \approx 11{,}39 > 10$ : $n = 6$. (Avec R6 : $n > \frac{\ln 10}{\ln 1{,}5} \approx 5{,}68$.)

### R6.R2 — Fonction réciproque (R3)
1. $f^{-1}(y) = \frac{y - 3}{2}$.
2. La racine carrée.
3. Symétriques par rapport à la droite $y = x$.
4. **5**.

### R6.R3 — Notation scientifique (R1)
1. $4{,}2 \times 10^{-4}$ et $7{,}3 \times 10^{6}$.
2. $7 \times 10^{4}$.
3. **13** chiffres (un 1 suivi de 12 zéros).

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R6.1 — Simplifier avec les propriétés de exp

**Réponses** : a) `2.5` · b) `2` · c) `"x + 1"` · d) `"2*x + 3"` · e) `4` · f) `"1/3"` · g) `"2*x + 2"` · h) `1`.

**Démarche.**
- a) $4 + (-1{,}5) = 2{,}5$. b) $(e^{3})^{2} = e^{6}$, puis $6 - 4 = 2$.
- c) $2x + (1 - x) = x + 1$. d) $x + (x + 3) = 2x + 3$.
- e) $8^{2/3} = (\sqrt[3]{8})^{2} = 2^{2} = 4$. f) $27^{-1/3} = \frac{1}{\sqrt[3]{27}} = \frac{1}{3}$.
- g) $(e^{x})^{3} = e^{3x}$, puis $3x - (x - 2) = 2x + 2$.
- h) $(\sqrt{e})^{4} = (e^{1/2})^{4} = e^{2}$, et $e^{2} \times e^{-2} = e^{0} = 1$.

**Erreurs fréquentes.** Multiplier les exposants d'un produit (a, c) ou additionner ceux d'une puissance de puissance (b) ; oublier de distribuer le signe moins (g) ; lire $8^{2/3}$ comme $8 \times \frac{2}{3}$ ; croire qu'un exposant négatif rend le nombre négatif (f).

**Variante.** $16^{3/4}$ et $e^{3x} \times e^{-x} / e^{2}$ ? *Réponse* : $(\sqrt[4]{16})^{3} = 8$ et $e^{2x - 2}$.

### Ex R6.2 — Simplifier avec les propriétés de ln

**Réponses** : a) `3` · b) `25` · c) `36` · d) `"5/2"` · e) `20` · f) `9` · g) `"a + 2*b"` · h) `"b - 2*a"`.

**Démarche.**
- a) $5 - 2 = 3$. b) $\ln \frac{50}{2} = \ln 25$. c) $\ln 9 + \ln 4 = \ln 36$.
- d) $\ln(e^{3}) - \ln(e^{1/2}) = 3 - \frac{1}{2} = \frac{5}{2}$.
- e) $e^{\ln 4} \times e^{\ln 5} = 4 \times 5 = 20$ (ou $e^{\ln 20}$). f) $e^{\ln 9} = 9$.
- g) $18 = 2 \times 3^{2}$ : $\ln 2 + 2 \ln 3 = a + 2b$.
- h) $0{,}75 = \frac{3}{2^{2}}$ : $\ln 3 - 2 \ln 2 = b - 2a$ (négatif, comme le logarithme de tout nombre plus petit que 1).

**Erreurs fréquentes.** $\ln 50 - \ln 2 = \ln 48$ ; $2 \ln 3 = \ln 6$ ; $\frac{\ln(e^{5})}{\ln(e^{2})}$ au lieu d'une différence ; en h, oublier que $4 = 2^{2}$.

**Variante.** $\ln 0{,}5$ en fonction de $a$, et $e^{3 \ln 2 - \ln 4}$ ? *Réponse* : $-a$, et $e^{\ln \frac{8}{4}} = 2$.

### Ex R6.3 — Équations et inéquations avec exp et ln

**Réponses** : a) `2.71` · b) `1.40` · c) `12.18` · d) `1` · e) `12` · f) `19` · g) `"]1 ; 2]"` · h) `[0.6931, 1.0986]`.

**Démarche.**
- a) $x = \ln 15 \approx 2{,}708$.
- b) $2x - 1 = \ln 6$, donc $x = \frac{1 + \ln 6}{2} \approx 1{,}396$.
- c) $x = e^{2{,}5} \approx 12{,}18$.
- d) Il faut $3x - 2 > 0$ ; $\ln(3x - 2) = 0 \iff 3x - 2 = 1 \iff x = 1$ (et $3 \times 1 - 2 = 1 > 0$).
- e) $1{,}04^{n} > 1{,}6 \iff n > \frac{\ln 1{,}6}{\ln 1{,}04} \approx 11{,}98$ : $n = 12$. Contrôle : $5 \times 1{,}04^{11} \approx 7{,}70$ et $5 \times 1{,}04^{12} \approx 8{,}005$.
- f) $n \ln 0{,}85 < \ln 0{,}05 \iff n > \frac{\ln 0{,}05}{\ln 0{,}85} \approx 18{,}43$ ($\ln 0{,}85 < 0$ : le sens change) : $n = 19$.
- g) Domaine : $x > 1$ ; puis $\ln(x - 1) \le 0 = \ln 1 \iff x - 1 \le 1 \iff x \le 2$ : $]1 \;;\; 2]$.
- h) Avec $X = e^{x}$ : $X^{2} - 5X + 6 = (X - 2)(X - 3) = 0$, donc $e^{x} = 2$ ou $e^{x} = 3$ : $x = \ln 2 \approx 0{,}6931$ ou $x = \ln 3 \approx 1{,}0986$.

**Erreurs fréquentes.** Diviser par 2 avant d'ajouter 1 (b) ; $x = \ln 2{,}5$ en c ; oublier de changer le sens de l'inégalité en f ; oublier le domaine en g (et répondre $]-\infty \;;\; 2]$) ; en h, s'arrêter à $X = 2$ et $X = 3$.

**Variante.** Résous $e^{2x} = 10$ et trouve le plus petit $n$ tel que $0{,}7^{n} < 0{,}5$. *Réponse* : $x = \frac{\ln 10}{2} \approx 1{,}15$ ; $n > \frac{\ln 0{,}5}{\ln 0{,}7} \approx 1{,}94$, donc $n = 2$.

### Ex R6.4 — Changer de base : log₂, log₁₀, ln

**Réponses** : a) `9` · b) `-4` · c) `4` · d) `-7` · e) `2.113` · f) `3.322` · g) `31` · h) `"3/2"`.

**Démarche.**
- a) $2^{9} = 512$. b) $0{,}0001 = 10^{-4}$. c) $3^{4} = 81$. d) $\frac{1}{128} = 2^{-7}$.
- e) $\frac{\ln 30}{\ln 5} \approx \frac{3{,}401}{1{,}609} \approx 2{,}113$. f) $\frac{\ln 10}{\ln 2} \approx 3{,}322$.
- g) $\log_{10}(2^{100}) = 100 \log_{10} 2 \approx 30{,}10$ : $2^{100}$ est entre $10^{30}$ et $10^{31}$, il a 31 chiffres.
- h) $4^{y} = 8 \iff 2^{2y} = 2^{3} \iff y = \frac{3}{2}$ (ou $\frac{\ln 8}{\ln 4} = \frac{3 \ln 2}{2 \ln 2}$).

**Erreurs fréquentes.** Diviser 512 par 2 ; un signe oublié en b et d ; $\frac{\ln 5}{\ln 30}$ en e (le quotient à l'envers) ; 30 chiffres en g.

**Variante.** $\log_{7} 100$, et le nombre de chiffres de $5^{50}$ (avec $\log_{10} 5 \approx 0{,}699$) ? *Réponse* : $\frac{\ln 100}{\ln 7} \approx 2{,}367$ ; $50 \times 0{,}699 \approx 34{,}9$, donc 35 chiffres.

### Ex R6.5 — Compter en bits et en nats : combien de questions oui ou non ?

**Réponses** : a) `9` · b) `8.23` · c) `9` · d) `6.238` · e) `5.70` · f) `13.93` · g) `0.0498` · h) `6.93`.

**Démarche.**
- a) $2^{8} = 256 < 300 \le 512 = 2^{9}$ : 9 questions. b) $\frac{\ln 300}{\ln 2} \approx 8{,}23$ : un peu plus de 8 bits, d'où 9 questions entières.
- c) $-\log_{2} \frac{1}{512} = 9$ bits. d) $9 \ln 2 \approx 6{,}238$ nats.
- e) $\log_{2} 52 \approx 5{,}70$ bits.
- f) Indépendants : les probabilités se multiplient, les informations s'additionnent : $5{,}70 + 8{,}23 = 13{,}93$ bits.
- g) $-\ln p = 3 \iff p = e^{-3} \approx 0{,}0498$.
- h) $10 \times \ln 2 \approx 6{,}93$ nats.

**Erreurs fréquentes.** Répondre 8 en a ($2^{8} = 256$ ne suffit pas) ; diviser par $\ln 2$ pour passer des bits aux nats ; multiplier les informations en f ; $p = 2^{-3}$ en g (des bits, pas des nats).

**Variante.** Combien de questions oui ou non pour un nombre choisi entre 1 et 2 000, et combien de nats apporte un événement de probabilité $\frac{1}{8}$ ? *Réponse* : 11 ($2^{11} = 2\,048$) ; $\ln 8 \approx 2{,}079$ nats.

### Ex R6.6 — Temps de doublement et demi-vie

**Réponses** : a) `23.45` · b) `23.33` · c) `6.58` · d) `1.1487` · e) `5.28` · f) `17.33` · g) `"1/16"`.

**Démarche.**
- a) $\frac{\ln 2}{\ln 1{,}03} \approx 23{,}45$ ans. b) $\frac{70}{3} \approx 23{,}33$ : très proche, car 3 % est un petit taux.
- c) $0{,}9^{n} = \frac{1}{2} \iff n = \frac{\ln 0{,}5}{\ln 0{,}9} \approx 6{,}58$ ans.
- d) $m^{5} = 2 \iff m = 2^{1/5} \approx 1{,}1487$ (une hausse d'environ 14,9 % par heure).
- e) $2^{12/5} = 2^{2{,}4} \approx 5{,}28$.
- f) $e^{0{,}04\,t} = 2 \iff t = \frac{\ln 2}{0{,}04} \approx 17{,}33$.
- g) 24 heures font 4 demi-vies : $\left(\frac{1}{2}\right)^{4} = \frac{1}{16}$.

**Erreurs fréquentes.** Confondre la valeur exacte et la règle de 70 (a, b) ; $\ln 1{,}1$ au lieu de $\ln 0{,}9$ pour une baisse ; $2 \times \frac{12}{5}$ au lieu de $2^{12/5}$ ; $\frac{\ln 2}{\ln 1{,}04}$ pour une croissance continue.

**Variante.** Une population baisse de 5 % par an : sa demi-vie ? Et une grandeur qui triple toutes les 3 heures, par quel nombre est-elle multipliée par heure ? *Réponse* : $\frac{\ln 0{,}5}{\ln 0{,}95} \approx 13{,}51$ ans ; $3^{1/3} \approx 1{,}442$.

### Ex R6.7 — Sigmoïde et logit : la symétrie σ(−x) = 1 − σ(x), la cote et la log-cote

**Réponses** : a) `"3/4"` · b) `"1/4"` · c) `0.769` · d) `0.231` · e) `19` · f) `2.944` · g) `-1.386` · h) `0.6`.

**Démarche.**
- a) $e^{-\ln 3} = \frac{1}{3}$, donc $\sigma(\ln 3) = \frac{1}{1 + \frac{1}{3}} = \frac{3}{4}$. b) $1 - \frac{3}{4} = \frac{1}{4}$ (symétrie), ou $\frac{1}{1 + 3}$.
- c) $\frac{1}{1 + e^{-1{,}2}} \approx \frac{1}{1{,}301} \approx 0{,}769$. d) $1 - 0{,}769 = 0{,}231$.
- e) $\frac{0{,}95}{0{,}05} = 19$. f) $\ln 19 \approx 2{,}944$.
- g) $x = \ln \frac{0{,}2}{0{,}8} = \ln \frac{1}{4} = -\ln 4 \approx -1{,}386$ (négatif, car $0{,}2 < \frac{1}{2}$).
- h) La cote de 0,2 est $\frac{0{,}2}{0{,}8} = \frac{1}{4}$ ; ajouter $\ln 6$ au logit la multiplie par 6 : $\frac{6}{4} = 1{,}5$ ; la probabilité vaut $\frac{1{,}5}{1 + 1{,}5} = 0{,}6$.

**Erreurs fréquentes.** Oublier le signe moins de $e^{-x}$ (c donne 0,231) ; $\sigma(-x) = -\sigma(x)$ ; la cote à l'envers ($\frac{1}{19}$) ; prendre $\ln p$ pour le logit ; multiplier la probabilité par 6 en h.

**Variante.** $\sigma(\ln 5)$ et le logit de 0,7 ? *Réponse* : $\frac{5}{6}$ ; $\ln \frac{0{,}7}{0{,}3} \approx 0{,}847$.

### Ex R6.8 — Placer des valeurs sur une échelle logarithmique

**Réponses** : a) `10` · b) `16.51` · c) `3.49` · d) `31.62` · e) `3.98`.

**Démarche.**
- a) $5 \times \log_{10} 100 = 10$ cm. b) $5 \times \log_{10} 2\,000 \approx 5 \times 3{,}301 = 16{,}51$ cm. c) $5 \times \log_{10} 5 \approx 3{,}49$ cm.
- d) $7{,}5$ cm $= 1{,}5$ décade : $10^{1{,}5} \approx 31{,}62$.
- e) 3 cm $= 0{,}6$ décade : un rapport $10^{0{,}6} \approx 3{,}98$.

**Erreurs fréquentes.** Oublier le facteur 5 cm par décade ; placer 5 au milieu de la décade (2,5 cm) ; répondre 1,5 ou 0,6 (des décades) au lieu des valeurs.

**Variante.** La position de 300 ? *Réponse* : $5 \log_{10} 300 \approx 12{,}39$ cm.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R6.9 — Démontrer ln(ab) = ln a + ln b à partir de exp

**Démonstration.**
1. Par définition de $\ln$, $e^{\ln a} = a$ et $e^{\ln b} = b$. Avec $e^{u + v} = e^{u} e^{v}$ : $e^{\ln a + \ln b} = e^{\ln a} \times e^{\ln b} = ab$.
2. Le réel $\ln a + \ln b$ a donc pour exponentielle $ab$. Or $\ln(ab)$ est **l'unique** réel dont l'exponentielle vaut $ab$ (et $ab > 0$). Donc $\ln(ab) = \ln a + \ln b$. ∎
3. Avec 2 appliqué à $b$ et $\frac{1}{b}$ : $\ln b + \ln \frac{1}{b} = \ln\left(b \times \frac{1}{b}\right) = \ln 1 = 0$, donc $\ln \frac{1}{b} = -\ln b$. Puis $\ln \frac{a}{b} = \ln\left(a \times \frac{1}{b}\right) = \ln a + \ln \frac{1}{b} = \ln a - \ln b$.
4. *Initialisation* : $\ln(a^{0}) = \ln 1 = 0 = 0 \times \ln a$. *Hérédité* : si $\ln(a^{n}) = n \ln a$, alors $\ln(a^{n+1}) = \ln(a^{n} \times a) = \ln(a^{n}) + \ln a = (n + 1) \ln a$. *Conclusion* : vrai pour tout $n \ge 0$. Puis $\ln a = \ln(\sqrt{a} \times \sqrt{a}) = 2 \ln \sqrt{a}$, donc $\ln \sqrt{a} = \frac{1}{2} \ln a$.
5. $a = b = 1$ : $\ln(1 + 1) = \ln 2 \approx 0{,}693$, mais $\ln 1 + \ln 1 = 0$.

**Grille de relecture.**
- Les hypothèses $a > 0$, $b > 0$ sont dites (sinon $\ln a$ n'existe pas).
- Le calcul de $e^{\ln a + \ln b}$ utilise $e^{u+v} = e^{u} e^{v}$ et $e^{\ln x} = x$, en le disant.
- La conclusion de 2 cite **l'unicité** de la définition (ou le fait que exp ne prend jamais deux fois la même valeur).
- La récurrence de 4 a ses trois étapes, et l'hérédité utilise le résultat de 2.
- Le contre-exemple de 5 est un calcul, pas une phrase.

**Erreurs fréquentes.** Partir de $\ln(ab) = \ln a + \ln b$ pour arriver à quelque chose de vrai (on suppose ce qu'on démontre) ; oublier l'unicité ; démontrer $\ln(a^{n}) = n \ln a$ sur deux ou trois exemples.

**Variante.** Démontre de même que $\ln(a^{-1}) = -\ln a$ sans passer par 3, en calculant $e^{-\ln a}$. *Réponse* : $e^{-\ln a} = \frac{1}{e^{\ln a}} = \frac{1}{a}$, donc $-\ln a$ est l'unique réel dont l'exponentielle vaut $\frac{1}{a}$.

### Ex R6.10 — tanh(x) = 2σ(2x) − 1

**Démonstration.**
1. $2\sigma(2x) - 1 = \frac{2}{1 + e^{-2x}} - \frac{1 + e^{-2x}}{1 + e^{-2x}} = \frac{1 - e^{-2x}}{1 + e^{-2x}}$.
2. En multipliant le haut et le bas par $e^{x}$ (non nul) : $\frac{e^{x} - e^{-x}}{e^{x} + e^{-x}} = \tanh x$. Donc $\tanh x = 2\sigma(2x) - 1$ pour tout réel $x$. ∎
3. $\tanh(-x) = 2\sigma(-2x) - 1 = 2(1 - \sigma(2x)) - 1 = 1 - 2\sigma(2x) = -(2\sigma(2x) - 1) = -\tanh x$ : tanh est impaire.
4. $0 < \sigma(2x) < 1$, donc $0 < 2\sigma(2x) < 2$, et $-1 < 2\sigma(2x) - 1 < 1$.
5. Avec $u = 2x$ : $\tanh \frac{u}{2} = 2\sigma(u) - 1$, donc $\sigma(u) = \frac{1 + \tanh \frac{u}{2}}{2}$.

**Grille de relecture.**
- La réduction au même dénominateur est écrite, avec le dénominateur $1 + e^{-2x}$.
- La multiplication par $e^{x}$ est justifiée ($e^{x} \ne 0$) et le calcul $e^{x} e^{-2x} = e^{-x}$ apparaît.
- En 3, la symétrie de σ est citée au bon endroit ; en 4, les inégalités sont transformées pas à pas.
- En 5, le changement de variable est dit.

**Erreurs fréquentes.** Partir de tanh pour arriver à $\tanh x$ ; oublier le $-1$ ; écrire $\sigma(2x) = 2\sigma(x)$.

**Variante.** Vérifie numériquement la relation de 5 pour $u = 5$ : $\sigma(5)$ et $\frac{1 + \tanh 2{,}5}{2}$. *Réponse* : les deux valent environ 0,9933 (calculatrice).

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R6.11 — Des produits de probabilités aux sommes de logarithmes

**Réponses** : a) `0.0648` · b) `-2.7364` · c) `-0.5473` · d) `0.1681` · e) `2` · f) `-397.94` · g) `False` · h) `-916.3`.

**Démarche.**
- a) $0{,}9 \times 0{,}6 \times 0{,}3 \times 0{,}8 \times 0{,}5 = 0{,}0648$.
- b) $\ln 0{,}9 + \ln 0{,}6 + \ln 0{,}3 + \ln 0{,}8 + \ln 0{,}5 \approx -0{,}105 - 0{,}511 - 1{,}204 - 0{,}223 - 0{,}693 = -2{,}736$ (c'est aussi $\ln 0{,}0648$).
- c) $\frac{-2{,}7364}{5} \approx -0{,}5473$.
- d) $0{,}7^{5} \approx 0{,}1681$. e) $0{,}1681 > 0{,}0648$ : le second modèle explique mieux les résultats observés.
- f) $\log_{10}(0{,}4^{1000}) = 1000 \log_{10} 0{,}4 \approx -397{,}94$ : la vraisemblance vaut environ $10^{-397{,}9}$.
- g) **Faux** : c'est bien plus petit que le plus petit flottant positif (de l'ordre de $10^{-308}$, fiche §5) : un `float64` donnerait 0.
- h) $1000 \ln 0{,}4 \approx -916{,}3$, un nombre ordinaire.

Dans ta copie : $\ln$ est strictement croissante, donc le plus grand produit a la plus grande somme de logarithmes ; et $-\ln p$ est l'information, en nats, de ce qui s'est produit : la « surprise » du modèle. Un bon modèle est peu surpris par ce qui arrive : sa somme des $-\ln p$ est petite.

**Erreurs fréquentes.** Additionner les probabilités en a ; utiliser $\log_{10}$ en b et h ; oublier de diviser par 5 en c ; choisir le premier modèle parce qu'il donne 0,9 à un résultat.

**Variante.** Quatre résultats de probabilités 0,5 et un de 0,8 : la vraisemblance et la log-vraisemblance ? *Réponse* : $0{,}5^{4} \times 0{,}8 = 0{,}05$ ; $\ln 0{,}05 \approx -2{,}996$.

### Ex R6.12 — Des logarithmes au travail : TF-IDF et PSNR

**Réponses** : a) `0` · b) `4.605` · c) `2.303` · d) `[9.210, 11.513]` · e) `30` · f) `3.01` · g) `6.5025`.

**Démarche.**
- a) $\ln \frac{2000}{2000} = \ln 1 = 0$. b) $\ln 100 \approx 4{,}605$. c) $\ln 10 \approx 2{,}303$.
- d) $2 \times 4{,}605 = 9{,}210$ et $5 \times 2{,}303 = 11{,}513$ : le mot fréquent dans le document l'emporte, malgré un idf plus petit.
- e) $\frac{255^{2}}{65{,}025} = \frac{65\,025}{65{,}025} = 1\,000$, et $10 \log_{10} 1\,000 = 30$ dB.
- f) Diviser la MSE par 2 multiplie le rapport par 2 : $+10 \log_{10} 2 \approx 3{,}01$ dB.
- g) $10 \log_{10} R = 40 \iff R = 10^{4}$, donc $\mathrm{MSE} = \frac{65\,025}{10\,000} = 6{,}5025$.

Dans ta copie : un mot présent partout ne distingue aucun document (son idf vaut $\ln 1 = 0$) ; le logarithme du PSNR transforme des rapports en écarts additifs (diviser l'erreur par 10, c'est toujours +10 dB), et rend comparables des erreurs de tailles très différentes.

**Erreurs fréquentes.** $\log_{10}$ au lieu de $\ln$ dans l'idf ; oublier le facteur 10 du PSNR ; inverser le rapport en g.

**Variante.** L'idf d'un mot présent dans 400 documents, et le PSNR d'une MSE de 26,01 ? *Réponse* : $\ln 5 \approx 1{,}609$ ; $10 \log_{10} 2\,500 \approx 33{,}98$ dB.

### Ex R6.13 — Expliquer ce que compte un logarithme : des chiffres, des doublements, des bits

**Exemple de réponse.**

> Un logarithme répond à une seule question : « à quelle puissance faut-il élever la base pour obtenir ce nombre ? ». Par exemple $\log_{10} 1\,000 = 3$, parce que $10^{3} = 1\,000$. En base 10, il compte donc à peu près les chiffres : un nombre de 5 chiffres a un $\log_{10}$ entre 4 et 5. En base 2, il compte les doublements : $\log_{2} 4\,096 = 12$, il faut doubler 12 fois 1 pour atteindre 4 096. C'est aussi le nombre de questions oui ou non pour retrouver un objet parmi 4 096, en coupant à chaque fois en deux : 12 bits. Et comme multiplier deux puissances revient à additionner leurs exposants, le logarithme d'un produit est la somme des logarithmes : il transforme les multiplications en additions.

**Grille.** Une bonne réponse : (1) la question « à quelle puissance… ? » avec un exemple ; (2) les chiffres pour $\log_{10}$ ; (3) les doublements, puis les questions oui ou non, pour $\log_{2}$ ; (4) le produit qui devient une somme, avec sa raison (les exposants s'additionnent) ; (5) huit lignes au plus.

<a id="notebook"></a>

## Notebook

### Ex R6.14 — Un logarithme dans n'importe quelle base · `log_base`

**Réponses** : a) `[6.0, -9.0]` · b) `-3.3219` · c) `"ValueError"` · d) `"ValueError"`.

**Démarche.** Les deux tests (`x <= 0`, puis `base <= 0 or base == 1`) lèvent une `ValueError` ; puis `return math.log(x) / math.log(base)`. Pour la copie : la base 1 donnerait $\ln 1 = 0$ au dénominateur ; aucune puissance de 1 ne vaut autre chose que 1.

**Erreurs fréquentes.** Le quotient à l'envers ; oublier le test de la base 1 (`ZeroDivisionError`) ; utiliser `math.log(x, base)`, `math.log2` ou `math.log10`, que la docstring interdit.

### Ex R6.15 — Sigmoïde et tanh à partir de exp · `sigmoid`, `tanh`

**Réponses** : a) `[0.5, 0.8176, 0.1824]` · b) `[True, True]` · c) `[0.0, 0.63515, -0.96403]` · d) `True` · e) `[1.0, -1.0]`.

**Démarche.** `sigmoid` : `1 / (1 + math.exp(-x))`. `tanh` : `2 * sigmoid(2 * x) - 1`, ou `(a - b) / (a + b)` avec `a = math.exp(x)` et `b = math.exp(-x)`.

**Erreurs fréquentes.** `math.exp(x)` au lieu de `math.exp(-x)` (σ inversée) ; `2 * sigmoid(x) - 1` (oubli du $2x$) ; `math.tanh`, interdite.

### Ex R6.16 — Temps de doublement · `doubling_time`

**Réponses** : a) `[10.2448, 3.1063]` · b) `"ValueError"` · c) `[69.6607, 7.2725, 1.7095]`.

**Démarche.** La `ValueError` si `rate <= 0`, puis `math.log(2) / math.log(1 + rate)`. Pour la copie : la règle de 70 donne 70 ; 7 ; 1,4. Elle est excellente à 1 %, correcte à 10 %, mauvaise à 50 %, car elle remplace $\ln(1 + r)$ par $r$, ce qui n'est juste que pour un petit $r$.

**Erreurs fréquentes.** $\frac{\ln 2}{r}$ (la croissance continue, pas un taux par période) ; arrondir à l'entier supérieur ; oublier le cas `rate == 0`.

### Ex R6.17 — Sur tout un tableau : `np.exp`, `np.log2` et `scipy.special.expit`

**Réponses** : a) `[-2, 1, 11]` · b) `[1, 4, 7]` · c) `[0.0759, 0.5, 0.9241]` · d) `[0.0001, 0.001, 0.01, 0.1, 1]`.

**Démarche.** a) `np.log2(values_a)` ; b) `np.floor(np.log10(values_b)) + 1` ; c) `expit(values_c)` ; d) `np.logspace(-4, 0, 5)`.

**Erreurs fréquentes.** `np.log` au lieu de `np.log2` ; oublier le `+ 1` en b ; `np.linspace` au lieu de `np.logspace` en d.

### Ex R6.18 — Prédire : exp(800) avec math et NumPy, et le produit de 600 probabilités de 0,25

**Réponses** : a) `3` · b) `2` · c) `2` · d) `1` · e) `-831.8`.

**Démarche.** `math.exp(800)` lève `OverflowError` : Python s'arrête plutôt que de rendre un faux nombre. `np.exp(800.0)` rend `inf` avec une alerte (`RuntimeWarning: overflow`) et continue : sur un tableau, une case qui déborde n'arrête pas les autres. `np.prod` rend exactement `0.0`, sans alerte : le résultat le plus trompeur. La somme des logarithmes vaut $600 \ln 0{,}25 \approx -831{,}8$, un nombre ordinaire. Pour la copie : le produit de milliers de probabilités devient 0 en flottant, et deux modèles ne se distinguent plus ; leurs sommes de log-probabilités, elles, restent comparables.

**Erreurs fréquentes.** Croire que Python et NumPy réagissent pareil ; attendre une erreur pour le produit trop petit ; utiliser $\log_{10}$ en e.

### Ex R6.19 — Croissances comparées : x¹⁰, 2ˣ et ln x de plus en plus loin

**Réponses** : a) `57` · b) `59` · c) `271.03` · d) `36` · e) `3269018`.

**Démarche.** `gap = n * math.log(2) - 10 * np.log(n)` et `race = 0.1 * t - np.log(t)`. a) $2^{n} \le n^{10}$ pour $n = 2, \dots, 58$ : 57 entiers. b) À partir de 59, $2^{n}$ reste devant. c) $1000 \log_{10} 2 - 10 \log_{10} 1000 = 301{,}03 - 30 = 271{,}03$. d) $0{,}1\,t > \ln t$ pour la première fois à partir de $t = 36$ (à $t = 35$, $3{,}5 < \ln 35 \approx 3{,}555$). e) $e^{15} \approx 3\,269\,017{,}4$, donc $k = 3\,269\,018$. Pour la copie : $x^{0{,}1}$ ne dépasse $\ln x$ que pour $x \ge e^{36} \approx 4 \times 10^{15}$.

**Erreurs fréquentes.** Calculer $2^{n}$ et $n^{10}$ directement (ça marche en Python avec des entiers, mais pas avec des flottants au-delà de $2^{1023}$) ; compter les $n$ où $2^{n}$ gagne en a ; diviser par $\ln 10$ en oubliant les $\ln$ (c).

### Ex R6.20 — Les mêmes données en échelle linéaire et en échelle logarithmique

**Réponses** : a) `0.204` · b) `4.90`.

**Démarche.** Deux `plot(..., "o")`, `axes[1].set_yscale("log")`, deux titres. a) $\log_{10} 1{,}6 \approx 0{,}204$ décade par pas ; b) $\frac{1}{0{,}204} \approx 4{,}90$ pas par décade. Pour la copie : les premières valeurs se voient sur l'échelle logarithmique (écrasées sur l'autre) ; un ralentissement ferait passer les derniers points sous la droite.

**Erreurs fréquentes.** `plt.yscale` ou `plt.plot` au lieu de `axes[1]` ; $\ln 1{,}6$ au lieu de $\log_{10} 1{,}6$ ; ouvrir une figure dans la fonction.

### Ex R6.21 — Chasse à l'erreur : ln(a + b), e^(a + b) et log(0)

**Réponses** : a) `"AEF"` · b) `"ValueError"` · c) `[-1.6094, 1.6094, 164.8721]`.

**Démarche.** (A) une somme part de 0 ; (E) `math.log(a + b)` ; (F) `start * math.exp(rate * t1) * math.exp(rate * t2)` (ou `math.exp(rate * (t1 + t2))`). b) `math.log(0)` lève `ValueError: math domain error`. c) $\ln(0{,}5 \times 0{,}4) = \ln 0{,}2$, $\ln 5$, $100\,e^{0{,}05 \times 10} = 100\,e^{0{,}5}$. Pour la copie : $\ln 0$ n'existe pas ($-\infty$ à la limite) ; un modèle qui donne la probabilité 0 à ce qui arrive vraiment a une log-vraisemblance de $-\infty$ : aucune autre réponse juste ne peut rattraper cette erreur.

**Erreurs fréquentes.** Accuser (C), qui est juste ; oublier (A) (le code rend une valeur décalée de 1, sans erreur) ; répondre `-inf` en b (c'est NumPy, pas `math`).

### Ex R6.22 — Lire la documentation de `numpy.log`, `log2`, `log10`, `log1p`

**Réponses attendues dans la copie.**
1. `np.log1p(x)` calcule $\ln(1 + x)$, précisément même pour $x$ très petit : `1 + 1e-12` arrondi en flottant ne garde que quelques chiffres de `1e-12`, et `np.log(1 + 1e-12)` est faux dès le cinquième chiffre (≈ 1,000 089 × 10⁻¹²), alors que `np.log1p(1e-12)` donne $10^{-12}$ à la précision du flottant.
2. `np.log(0.0)` rend `-inf` et `np.log(-1.0)` rend `nan`, chacun avec une alerte ; `math.log` lève une `ValueError`. L'erreur est préférable pour détecter un bug ; la valeur spéciale pour calculer sur un tableau sans s'arrêter (mais il faut surveiller les alertes).
3. `np.log2`, `np.log10` et `np.log` (= $\ln$). `np.log` n'a pas d'argument de base : pour une autre base, on divise par `np.log(b)`.
