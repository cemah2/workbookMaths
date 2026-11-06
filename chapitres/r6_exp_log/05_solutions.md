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
2. **Faux** : $\ln 2 + \ln 3 = \ln 6$, pas $\ln 5$. Le logarithme d'une somme ne se découpe pas.
3. **Vrai**.
4. **Vrai**.
5. **Faux** : avec $a = e$, $(\ln e)^{2} = 1$ et $2 \ln e = 2$.
6. **Faux** : $\ln \frac{a}{b} = \ln a - \ln b$.
7. **Vrai** : pour $0 < x < 1$, $x = e^{y}$ avec $y < 0$.

### R6.Q3 — Combien de bits ?
1. **4** questions ($2^{4} = 16$).
2. **20** questions : $2^{19} = 524\,288$ ne suffit pas, $2^{20} = 1\,048\,576$ suffit.
3. **5** bits ($-\log_{2} \frac{1}{32} = 5$).
4. **0** bit : un événement certain n'apprend rien.
5. $2^{7} = $ **128** possibilités.
6. **Vrai** : 1 bit ≈ 0,693 nat, donc une quantité de $I$ bits vaut $0{,}693\,I$ nats, un nombre plus petit (4 bits ≈ 2,77 nats).

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
1. **Faux** : $\sigma(0) = \frac{1}{1 + 1} = \frac{1}{2}$.
2. **Faux** : $\sigma(x) < 1$ toujours, car $e^{-x} > 0$.
3. **Faux** : $\sigma(-x) = 1 - \sigma(x)$ ; $\sigma(-x)$ est positif, comme toute valeur de la sigmoïde.
4. **Vrai** : σ est strictement croissante et $\sigma(0) = \frac{1}{2}$.
5. **Faux** : tanh est impaire, la sigmoïde ne l'est pas ($\sigma(0) = \frac{1}{2} \ne 0$).
6. **Vrai** : elle va de −1 à 1 sans jamais les atteindre, et sa courbe, d'un seul tenant, passe par toutes les valeurs intermédiaires (R7 précisera ce « d'un seul tenant »).

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
2. $\frac{4{,}8}{1{,}6} \times 10^{5 - (-3)} = 3 \times 10^{8}$.
3. **13** chiffres (un 1 suivi de 12 zéros).

<a id="papier"></a>

## ✏️ Papier-crayon

### Ex R6.1 — Simplifier avec les propriétés de exp

**Réponses** : a) `2.5` · b) `1` · c) `"2 - 2*x"` · d) `"2*x + 3"` · e) `8` · f) `"1/5"` · g) `"2*x + 2"` · h) `1`.

**Démarche.**
- a) $4 + (-1{,}5) = 2{,}5$. b) $(e^{2})^{3} = e^{6}$, puis $7 - 6 = 1$.
- c) $3x + (2 - 5x) = 2 - 2x$. d) $x + (x + 3) = 2x + 3$.
- e) $16^{3/4} = (\sqrt[4]{16})^{3} = 2^{3} = 8$. f) $125^{-1/3} = \frac{1}{\sqrt[3]{125}} = \frac{1}{5}$.
- g) $(e^{x})^{3} = e^{3x}$, puis $3x - (x - 2) = 2x + 2$.
- h) $(\sqrt{e})^{4} = (e^{1/2})^{4} = e^{2}$, et $e^{2} \times e^{-2} = e^{0} = 1$ : la valeur est 1 (l'exposant, lui, vaut 0).

**Erreurs fréquentes.** Multiplier les exposants d'un produit (a, c) ou additionner ceux d'une puissance de puissance (b) ; perdre le signe moins de $-5x$ (c) ou oublier les parenthèses de $x - 2$ (g) ; lire $16^{3/4}$ comme $16 \times \frac{3}{4}$ ; croire qu'un exposant négatif rend le nombre négatif (f) ; répondre 0, l'exposant, en h.

**Variante.** $81^{3/4}$ et $e^{x} \times e^{4 - 3x} / e^{-1}$ ? *Réponse* : $(\sqrt[4]{81})^{3} = 27$ et $e^{5 - 2x}$.

### Ex R6.2 — Simplifier avec les propriétés de ln

**Réponses** : a) `2` · b) `5` · c) `36` · d) `"-5/2"` · e) `20` · f) `2` · g) `"a + 2*b"` · h) `"b - 2*a"`.

**Démarche.**
- a) $3 \times 2 - 4 = 2$. b) $\ln \frac{60}{4 \times 3} = \ln 5$. c) $\ln 9 + \ln 4 = \ln 36$.
- d) $\ln(e^{1/2}) - \ln(e^{3}) = \frac{1}{2} - 3 = -\frac{5}{2}$.
- e) $e^{\ln 4} \times e^{\ln 5} = 4 \times 5 = 20$ (ou $e^{\ln 20}$). f) $e^{3 \ln 2 - \ln 4} = \frac{e^{\ln 8}}{e^{\ln 4}} = \frac{8}{4} = 2$.
- g) $18 = 2 \times 3^{2}$ : $\ln 2 + 2 \ln 3 = a + 2b$.
- h) $0{,}75 = \frac{3}{2^{2}}$ : $\ln 3 - 2 \ln 2 = b - 2a$ (négatif, comme le logarithme de tout nombre plus petit que 1).

**Erreurs fréquentes.** $\ln 60 - \ln 4 - \ln 3 = \ln 53$ ; $2 \ln 3 = \ln 6$ ; diviser les logarithmes au lieu de les soustraire (a, d) ; $e^{u - v} = e^{u} - e^{v}$ en f ; en h, oublier que $4 = 2^{2}$.

**Variante.** $\ln 0{,}5$ en fonction de $a$, et $\ln 24$ en fonction de $a$ et $b$ ? *Réponse* : $-a$ ; $24 = 2^{3} \times 3$, donc $3a + b$.

### Ex R6.3 — Équations et inéquations avec exp et ln

**Réponses** : a) `1.61` · b) `-0.40` · c) `12.18` · d) `3` · e) `12` · f) `19` · g) `"]1 ; 2]"` · h) `[0.6931, 1.0986]`.

**Démarche.**
- a) $4e^{x} = 20$, $e^{x} = 5$, $x = \ln 5 \approx 1{,}609$.
- b) $1 - 2x = \ln 6$, $-2x = \ln 6 - 1$, donc $x = \frac{1 - \ln 6}{2} \approx -0{,}396$.
- c) $2 \ln x = 5$, $\ln x = 2{,}5$, $x = e^{2{,}5} \approx 12{,}18$.
- d) Domaine : $x - 1 > 0$ et $x + 1 > 0$, donc $x > 1$. Puis $\ln\big((x - 1)(x + 1)\big) = \ln 8 \iff x^{2} - 1 = 8 \iff x^{2} = 9$ : $x = 3$ ou $x = -3$, et seul 3 est dans le domaine.
- e) $1{,}04^{n} > 1{,}6 \iff n > \frac{\ln 1{,}6}{\ln 1{,}04} \approx 11{,}98$ : $n = 12$. Contrôle : $5 \times 1{,}04^{11} \approx 7{,}70$ et $5 \times 1{,}04^{12} \approx 8{,}005$.
- f) $n \ln 0{,}85 < \ln 0{,}05 \iff n > \frac{\ln 0{,}05}{\ln 0{,}85} \approx 18{,}43$ ($\ln 0{,}85 < 0$ : le sens change) : $n = 19$.
- g) Domaine : $x > 1$ ; puis $\ln(x - 1) \le 0 = \ln 1 \iff x - 1 \le 1 \iff x \le 2$ : $]1 \;;\; 2]$.
- h) Avec $X = e^{x}$ : $X^{2} - 5X + 6 = (X - 2)(X - 3) = 0$, donc $e^{x} = 2$ ou $e^{x} = 3$ : $x = \ln 2 \approx 0{,}6931$ ou $x = \ln 3 \approx 1{,}0986$.

**Erreurs fréquentes.** Prendre le logarithme avant d'avoir isolé $e^{x}$ (a) ; un signe perdu en divisant par $-2$ (b) ; $x = \ln 2{,}5$ en c ; garder $-3$ en d, ou écrire $\ln(x - 1) + \ln(x + 1) = \ln(2x)$ ; oublier de changer le sens de l'inégalité en f ; oublier le domaine en g (et répondre $]-\infty \;;\; 2]$) ; en h, s'arrêter à $X = 2$ et $X = 3$.

**Variante.** Résous $e^{2x} = 10$ et trouve le plus petit $n$ tel que $0{,}7^{n} < 0{,}5$. *Réponse* : $x = \frac{\ln 10}{2} \approx 1{,}15$ ; $n > \frac{\ln 0{,}5}{\ln 0{,}7} \approx 1{,}94$, donc $n = 2$.

### Ex R6.4 — Changer de base : log₂, log₁₀, ln

**Réponses** : a) `9` · b) `2` · c) `3` · d) `-7` · e) `2.113` · f) `2.807` · g) `31` · h) `"3/2"`.

**Démarche.**
- a) $2^{9} = 512$. b) $\log_{10}(25 \times 4) = \log_{10} 100 = 2$. c) $6^{3} = 216$. d) $\frac{1}{128} = 2^{-7}$.
- e) $\frac{\ln 30}{\ln 5} \approx \frac{3{,}401}{1{,}609} \approx 2{,}113$. f) $\frac{\ln 7}{\ln 2} \approx \frac{1{,}946}{0{,}693} \approx 2{,}807$.
- g) $\log_{10}(2^{100}) = 100 \log_{10} 2 \approx 30{,}10$ : $2^{100}$ est entre $10^{30}$ et $10^{31}$, il a 31 chiffres.
- h) $4^{y} = 8 \iff 2^{2y} = 2^{3} \iff y = \frac{3}{2}$ (ou $\frac{\ln 8}{\ln 4} = \frac{3 \ln 2}{2 \ln 2}$).

**Erreurs fréquentes.** Diviser 512 par 2 ; $\log_{10} 29$ en b (une somme de logarithmes est le logarithme du **produit**) ; un signe oublié en d ; le quotient à l'envers en e et f ; 30 chiffres en g.

**Variante.** $\log_{7} 100$, et le nombre de chiffres de $5^{50}$ (avec $\log_{10} 5 \approx 0{,}699$) ? *Réponse* : $\frac{\ln 100}{\ln 7} \approx 2{,}367$ ; $50 \times 0{,}699 \approx 34{,}9$, donc 35 chiffres.

### Ex R6.5 — Compter en bits et en nats : combien de questions oui ou non ?

**Réponses** : a) `9` · b) `8.23` · c) `14.10` · d) `11` · e) `5.70` · f) `2.12` · g) `0.0498` · h) `6.93`.

**Démarche.**
- a) $2^{8} = 256 < 300 \le 512 = 2^{9}$ : 9 questions. b) $\frac{\ln 300}{\ln 2} \approx 8{,}23$ : un peu plus de 8 bits, d'où 9 questions entières.
- c) $26^{3} = 17\,576$ codes également probables : $\log_{2}(26^{3}) = 3 \log_{2} 26 \approx 3 \times 4{,}700 = 14{,}10$ bits. Chaque lettre apporte $\log_{2} 26$ bits, et les informations s'additionnent.
- d) $n \log_{2} 26 \ge 50 \iff n \ge \frac{50}{4{,}700} \approx 10{,}64$ : 11 lettres (10 lettres n'apportent que 47 bits).
- e) $\log_{2} 52 \approx 5{,}70$ bits.
- f) $p = \frac{12}{52}$ : $-\log_{2} \frac{12}{52} = \log_{2} \frac{52}{12} \approx 2{,}12$ bits, moins qu'en e : savoir que c'est une figure apprend moins que connaître la carte.
- g) $-\ln p = 3 \iff p = e^{-3} \approx 0{,}0498$.
- h) $10 \times \ln 2 \approx 6{,}93$ nats.

**Erreurs fréquentes.** Répondre 8 en a ($2^{8} = 256$ ne suffit pas) ; $\log_{2}(26 \times 3)$ en c ; 10 en d ; $\log_{2} 12$ en f (le nombre de figures, pas la probabilité) ; diviser par $\ln 2$ pour passer des bits aux nats ; $p = 2^{-3}$ en g (des bits, pas des nats).

**Variante.** Combien de questions oui ou non pour un nombre choisi entre 1 et 2 000, et combien de bits apporte « la carte est un as » (4 cartes sur 52) ? *Réponse* : 11 ($2^{11} = 2\,048$) ; $\log_{2} 13 \approx 3{,}70$ bits.

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

### Ex R6.7 — La cote et le logit : d'une probabilité à un score, et retour

**Réponses** : a) `19` · b) `2.944` · c) `0.3` · d) `-0.847` · e) `0.769` · f) `-1.2` · g) `20.09` · h) `0.6`.

**Démarche.**
- a) $\frac{0{,}95}{0{,}05} = 19$. b) $\ln 19 \approx 2{,}944$.
- c) $\frac{p}{1 - p} = \frac{3}{7} \iff 7p = 3 - 3p \iff p = \frac{3}{10} = 0{,}3$ (une cote « $a$ contre $b$ » donne $p = \frac{a}{a + b}$). d) $\ln \frac{3}{7} \approx -0{,}847$, négatif car $p < \frac{1}{2}$.
- e) $\sigma(1{,}2) = \frac{1}{1 + e^{-1{,}2}} \approx \frac{1}{1{,}301} \approx 0{,}769$.
- f) La probabilité contraire $1 - p$ a la cote $\frac{1 - p}{p}$, l'inverse de celle de $p$ ; son logit est le logarithme de l'inverse, donc l'opposé : $-1{,}2$, puisque le logit de $p$ est le score $1{,}2$.
- g) Le logit est le logarithme de la cote : la cote vaut $e^{3} \approx 20{,}09$.
- h) La cote de 0,2 est $\frac{0{,}2}{0{,}8} = 0{,}25$ ; ajouter $\ln 6$ au logit la multiplie par 6 : $1{,}5$ ; la probabilité vaut $\frac{1{,}5}{1 + 1{,}5} = 0{,}6$.

**Erreurs fréquentes.** La cote à l'envers ($\frac{1}{19}$) ; prendre $\ln p$ pour le logit ; $\frac{3}{7}$ pour la probabilité en c ; oublier le signe moins de $e^{-x}$ (e donne 0,231) ; donner en f la probabilité contraire (0,231) au lieu de son logit ; $10^{3}$ en g ; multiplier la probabilité par 6 en h.

**Variante.** Une cote de « 2 contre 3 » : la probabilité et le logit ? Puis on ajoute $\ln 3$ au logit : la nouvelle probabilité ? *Réponse* : 0,4 et $\ln \frac{2}{3} \approx -0{,}405$ ; la cote devient $\frac{2}{3} \times 3 = 2$, la probabilité $\frac{2}{3} \approx 0{,}667$.

### Ex R6.8 — Placer des valeurs sur une échelle logarithmique

**Réponses** : a) `10` · b) `16.5` · c) `3.5` · d) `31.62` · e) `3.98`.

**Démarche.**
- a) $5 \times \log_{10} 100 = 10$ cm. b) $5 \times \log_{10} 2\,000 \approx 5 \times 3{,}301 \approx 16{,}5$ cm. c) $5 \times \log_{10} 5 \approx 5 \times 0{,}699 \approx 3{,}5$ cm.
- d) $7{,}5$ cm $= 1{,}5$ décade : $10^{1{,}5} \approx 31{,}62$.
- e) 3 cm $= 0{,}6$ décade : un rapport $10^{0{,}6} \approx 3{,}98$.

**Erreurs fréquentes.** Oublier le facteur 5 cm par décade ; placer 5 au milieu de la décade (2,5 cm) ; répondre 1,5 ou 0,6 (des décades) au lieu des valeurs.

**Variante.** La position de 300 ? *Réponse* : $5 \log_{10} 300 \approx 12{,}4$ cm.

<a id="demonstrations"></a>

## ∂ Démonstrations

### Ex R6.9 — Démontrer ln(ab) = ln a + ln b à partir de exp

**Démonstration.**
1. Par définition de $\ln$, $e^{\ln a} = a$ et $e^{\ln b} = b$. Avec $e^{u + v} = e^{u} e^{v}$ : $e^{\ln a + \ln b} = e^{\ln a} \times e^{\ln b} = ab$.
2. Le réel $\ln a + \ln b$ a donc pour exponentielle $ab$. Or $\ln(ab)$ est **l'unique** réel dont l'exponentielle vaut $ab$ (et $ab > 0$). Donc $\ln(ab) = \ln a + \ln b$. ∎
3. Avec 2 appliqué à $b$ et $\frac{1}{b}$ : $\ln b + \ln \frac{1}{b} = \ln\left(b \times \frac{1}{b}\right) = \ln 1 = 0$ (car $e^{0} = 1$), donc $\ln \frac{1}{b} = -\ln b$. Puis $\ln \frac{a}{b} = \ln\left(a \times \frac{1}{b}\right) = \ln a + \ln \frac{1}{b} = \ln a - \ln b$.
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

### Ex R6.10 — Les propriétés de tanh, démontrées avec exp

**Démonstration.**
1. Pour tout réel $x$, $e^{x} \ne 0$ : on peut multiplier le numérateur et le dénominateur par $e^{x}$. Comme $e^{x} \times e^{x} = e^{2x}$ et $e^{x} \times e^{-x} = e^{0} = 1$ : $\tanh x = \frac{e^{2x} - 1}{e^{2x} + 1}$.
2. $\tanh(-x) = \frac{e^{-x} - e^{x}}{e^{-x} + e^{x}} = -\frac{e^{x} - e^{-x}}{e^{x} + e^{-x}} = -\tanh x$ : échanger $x$ et $-x$ change le signe du numérateur, pas le dénominateur. tanh est impaire.
3. Posons $u = e^{2x} > 0$. Alors $u + 1 > 0$, et $-(u + 1) < u - 1 < u + 1$ : à gauche, car $-u - 1 < u - 1 \iff 0 < 2u$ ; à droite, car $-1 < 1$. En divisant par $u + 1 > 0$ (le sens est gardé) : $-1 < \tanh x < 1$.
4. $\tanh b - \tanh a = \frac{B - 1}{B + 1} - \frac{A - 1}{A + 1} = \frac{(B - 1)(A + 1) - (A - 1)(B + 1)}{(A + 1)(B + 1)} = \frac{2(B - A)}{(A + 1)(B + 1)}$. Si $a < b$, alors $2a < 2b$ et, exp étant strictement croissante, $A < B$ : le numérateur est positif, le dénominateur aussi. Donc $\tanh a < \tanh b$ : tanh est strictement croissante.
5. $\tanh a + \tanh b = \frac{(A - 1)(B + 1) + (B - 1)(A + 1)}{(A + 1)(B + 1)} = \frac{2(AB - 1)}{(A + 1)(B + 1)}$ et $1 + \tanh a \tanh b = \frac{(A + 1)(B + 1) + (A - 1)(B - 1)}{(A + 1)(B + 1)} = \frac{2(AB + 1)}{(A + 1)(B + 1)}$. Leur quotient vaut $\frac{AB - 1}{AB + 1}$. Or $AB = e^{2a} e^{2b} = e^{2(a + b)}$ : d'après 1, c'est $\tanh(a + b)$. ∎

**Grille de relecture.**
- En 1, la multiplication par $e^{x}$ est justifiée ($e^{x} \ne 0$) et les calculs $e^{x} e^{x} = e^{2x}$, $e^{x} e^{-x} = 1$ apparaissent.
- En 3, la positivité de $e^{2x}$ sert deux fois : pour l'encadrement, et pour diviser sans changer le sens.
- En 4, la différence est mise sur un seul dénominateur, le signe de chaque facteur est justifié, et la croissance de exp est citée pour passer de $a < b$ à $A < B$.
- En 5, les deux fractions sont réduites, et $AB = e^{2(a + b)}$ est écrit avec la règle $e^{u} e^{v} = e^{u + v}$.

**Erreurs fréquentes.** Diviser une inégalité sans regarder le signe du diviseur ; en 4, conclure sur deux ou trois exemples ; en 5, écrire $e^{2a} e^{2b} = e^{4ab}$ ; partir de la formule à démontrer.

**Variante.** Avec la formule de 5, exprime $\tanh(2a)$ en fonction de $t = \tanh a$, puis vérifie avec $a = 1$ ($\tanh 1 \approx 0{,}7616$). *Réponse* : $\tanh 2a = \frac{2t}{1 + t^{2}}$ ; $\frac{2 \times 0{,}7616}{1 + 0{,}5800} \approx 0{,}9640$, la valeur de $\tanh 2$.

<a id="reflexion"></a>

## 🔗 🗣️ Pont et explication

### Ex R6.11 — Des produits de probabilités aux sommes de logarithmes

**Réponses** : a) `0.0648` · b) `-2.7364` · c) `-0.5473` · d) `0.1681` · e) `2` · f) `-897.5` · g) `18.8` · h) `8.17`.

**Démarche.**
- a) $0{,}9 \times 0{,}6 \times 0{,}3 \times 0{,}8 \times 0{,}5 = 0{,}0648$.
- b) $\ln 0{,}9 + \ln 0{,}6 + \ln 0{,}3 + \ln 0{,}8 + \ln 0{,}5 \approx -0{,}105 - 0{,}511 - 1{,}204 - 0{,}223 - 0{,}693 = -2{,}736$ (c'est aussi $\ln 0{,}0648$).
- c) $\frac{-2{,}7364}{5} \approx -0{,}5473$.
- d) $0{,}7^{5} \approx 0{,}1681$. e) $0{,}1681 > 0{,}0648$ : le second modèle explique mieux les résultats observés.
- f) $600 \ln 0{,}5 + 400 \ln 0{,}3 \approx 600 \times (-0{,}6931) + 400 \times (-1{,}2040) \approx -415{,}9 - 481{,}6 = -897{,}5$.
- g) Pour A : $1000 \ln 0{,}4 \approx -916{,}3$. L'écart vaut $-897{,}5 - (-916{,}3) \approx 18{,}8$ (18,81 avec les valeurs non arrondies) : B est meilleur.
- h) $\ln \frac{L_{B}}{L_{A}} = \ln L_{B} - \ln L_{A} \approx 18{,}81$, donc $\log_{10} \frac{L_{B}}{L_{A}} = \frac{18{,}81}{\ln 10} \approx 8{,}17$ : B est environ $10^{8}$ fois plus vraisemblable que A, sans qu'on ait jamais calculé ces vraisemblances.

Dans ta copie : $-\ln p$ est l'information, en nats, de ce qui s'est produit, la « surprise » du modèle. Le premier modèle a été le plus surpris par le troisième résultat, auquel il donnait 0,3 : $-\ln 0{,}3 \approx 1{,}20$ nat.

**Erreurs fréquentes.** Additionner les probabilités en a ; utiliser $\log_{10}$ en b et f ; oublier de diviser par 5 en c ; choisir le premier modèle parce qu'il donne 0,9 à un résultat ; $1000 \ln(0{,}5 \times 0{,}3)$ en f ; oublier de diviser par $\ln 10$ en h.

**Variante.** Un modèle C donne 0,45 à chacun des 1 000 résultats : sa log-vraisemblance, et est-il meilleur que B ? *Réponse* : $1000 \ln 0{,}45 \approx -798{,}5 > -897{,}5$ : oui.

### Ex R6.12 — Des logarithmes au travail : TF-IDF et PSNR

**Réponses** : a) `0` · b) `4.605` · c) `2.303` · d) `[9.210, 11.513]` · e) `30` · f) `6.99` · g) `6.5025`.

**Démarche.**
- a) $\ln \frac{2000}{2000} = \ln 1 = 0$. b) $\ln 100 \approx 4{,}605$. c) $\ln 10 \approx 2{,}303$.
- d) $2 \ln 100 \approx 9{,}210$ et $5 \ln 10 \approx 11{,}513$ (avec l'arrondi 2,303, on trouverait 11,515 : on garde les valeurs exactes jusqu'au bout). Le mot fréquent dans le document l'emporte, malgré un idf plus petit.
- e) $\frac{255^{2}}{65{,}025} = \frac{65\,025}{65{,}025} = 1\,000$, et $10 \log_{10} 1\,000 = 30$ dB.
- f) Diviser la MSE par 5 multiplie le rapport par 5 : $+10 \log_{10} 5 \approx 6{,}99$ dB.
- g) $10 \log_{10} R = 40 \iff R = 10^{4}$, donc $\mathrm{MSE} = \frac{65\,025}{10\,000} = 6{,}5025$.

Dans ta copie : un mot présent partout ne distingue aucun document (son idf vaut $\ln 1 = 0$) ; le logarithme du PSNR change les rapports en écarts : multiplier le rapport par un même nombre ajoute toujours le même nombre de décibels, quelle que soit la qualité de départ, et des erreurs de tailles très différentes deviennent comparables.

**Erreurs fréquentes.** $\log_{10}$ au lieu de $\ln$ dans l'idf ; oublier le facteur 10 du PSNR ; inverser le rapport en g.

**Variante.** L'idf d'un mot présent dans 400 documents, et le PSNR d'une MSE de 26,01 ? *Réponse* : $\ln 5 \approx 1{,}609$ ; $10 \log_{10} 2\,500 \approx 33{,}98$ dB.

### Ex R6.13 — Expliquer ce que compte un logarithme : des chiffres, des doublements, des bits

**Exemple de réponse.**

> Un logarithme répond à une seule question : « à quelle puissance faut-il élever la base pour obtenir ce nombre ? ». Par exemple $\log_{10} 100\,000 = 5$, parce que $10^{5} = 100\,000$. En base 10, il compte donc à peu près les chiffres : un nombre de 5 chiffres a un $\log_{10}$ entre 4 et 5. En base 2, il compte les doublements : $\log_{2} 4\,096 = 12$, il faut doubler 12 fois 1 pour atteindre 4 096. C'est aussi le nombre de questions oui ou non pour retrouver un objet parmi 4 096, en coupant à chaque fois en deux : 12 bits. Et comme multiplier deux puissances revient à additionner leurs exposants, le logarithme d'un produit est la somme des logarithmes : il transforme les multiplications en additions.

**Grille.** Une bonne réponse : (1) la question « à quelle puissance… ? » avec un exemple ; (2) les chiffres pour $\log_{10}$ ; (3) les doublements, puis les questions oui ou non, pour $\log_{2}$ ; (4) le produit qui devient une somme, avec sa raison (les exposants s'additionnent) ; (5) huit lignes au plus.

<a id="notebook"></a>

## Notebook

### Ex R6.14 — Un logarithme dans n'importe quelle base · `log_base`

**Réponses** : a) `[6.0, -9.0]` · b) `-2.585` · c) `"ValueError"` · d) `"ValueError"`.

**Démarche.** Les deux tests (`x <= 0`, puis `base <= 0 or base == 1`) lèvent une `ValueError` ; puis `return math.log(x) / math.log(base)`. Pour la copie : la base 1 donnerait $\ln 1 = 0$ au dénominateur ; aucune puissance de 1 ne vaut autre chose que 1.

**Erreurs fréquentes.** Le quotient à l'envers ; oublier le test de la base 1 (`ZeroDivisionError`) ; utiliser `math.log(x, base)`, `math.log2` ou `math.log10`, que la docstring interdit (un test le vérifie).

### Ex R6.15 — Sigmoïde et tanh à partir de exp · `sigmoid`, `tanh`

**Réponses** : a) `[0.5, 0.6682, 0.3318]` · b) `[True, True]` · c) `[0.0, 0.63515, -0.96403]` · d) `True` · e) `[1.0, -1.0]`.

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

### Ex R6.18 — Prédire : exp(800) et exp(−800), avec math et avec NumPy

**Réponses** : a) `3` · b) `2` · c) `2` · d) `3`.

**Démarche.** `math.exp(800)` lève `OverflowError` : Python s'arrête plutôt que de rendre un faux nombre. `np.exp(800.0)` rend `inf` avec une alerte (`RuntimeWarning: overflow`) et continue : sur un tableau, une case qui déborde n'arrête pas les autres. Dans l'autre sens, $e^{-800}$ est trop petit pour un flottant : `math.exp(-800)` et `np.exp(-800.0)` rendent exactement `0.0`, sans erreur ni alerte. Pour la copie : c'est ce 0 silencieux le plus dangereux, car il ressemble à un résultat normal ; plus loin, `math.log` de ce 0 lèverait `ValueError`, et une division par lui donnerait une erreur ou `inf`, loin de la vraie cause.

**Erreurs fréquentes.** Croire que Python et NumPy réagissent pareil ; attendre une erreur ou une alerte pour le nombre trop petit, comme pour le nombre trop grand.

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
