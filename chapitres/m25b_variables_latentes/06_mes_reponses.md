# M25b · Mes réponses

> Ta copie de ce fichier est dans `mon_travail/m25b_variables_latentes/06_mes_reponses.md` (créée par `python tools/start_chapter.py M25b`) : c'est **elle** que tu remplis, et c'est elle que Claude lit s'il corrige ton travail.
> Écris ta démarche, pas seulement le résultat : une réponse juste pour une mauvaise raison ne t'apprend rien. Vérifie chaque résultat : des responsabilités positives dont chaque ligne a pour somme 1, un posterior qui fait aussi 1, une variance de mélange qui contient la variance entre les groupes, une log-vraisemblance qui ne baisse pas après une itération de l'EM sans régularisation, une ELBO toujours sous $\ln p(\mathbf{x})$ et égale à lui au posterior, un écart égal à $\mathrm{KL}(q \,\|\, p(\mathbf{z} \mid \mathbf{x}))$ ($q$ en premier), une covariance a posteriori de l'ACP probabiliste qui ne dépend pas de $\mathbf{x}$, des angles principaux entre 0° et 90°, une KL positive ou nulle, une KL moyenne au prior égale à l'information mutuelle plus la KL du posterior agrégé. Les formules s'écrivent en LaTeX entre `$` (R0 §5), une loi comme `$\mathcal{N}(\mu, \sigma^2)$` et une divergence comme `$\mathrm{KL}(q \,\|\, p)$` ; une démonstration s'écrit en phrases (R4 §8).

## 🧠 Quiz

### M25b.Q1 — Lire un graphe orienté : factoriser la loi jointe, l'ordre d'un tirage ancestral, et les variables qui deviennent dépendantes quand on observe leur effet commun

1. 
2. 
3. 
4. 
5. 
6. 

### M25b.Q2 — Marginaliser ou conditionner : vraisemblance marginale, posterior d'un latent, moyenne et variance d'un mélange

1. 
2. 
3. 
4. 
5. 
6. 

### M25b.Q3 — Un mélange de gaussiennes : responsabilités, logarithme d'une somme, vraisemblance infinie et composantes renumérotées

1. 
2. 
3. 
4. 
5. 
6. 

### M25b.Q4 — L'EM : ce que font le pas E et le pas M, ce qui ne baisse jamais, ce qui n'est pas garanti, et k-means comme limite

1. 
2. 
3. 
4. 
5. 
6. 

### M25b.Q5 — L'ELBO : une borne de quoi, une égalité quand, un écart égal à quelle KL ?

1. 
2. 
3. 
4. 
5. 
6. 

### M25b.Q6 — L'ACP probabiliste : covariance marginale, rotation de W, angles principaux et directions éteintes

1. 
2. 
3. 
4. 
5. 
6. 

### M25b.Q7 — KL directe ou inverse, inférence amortie et écart d'amortissement, et dériver sous l'espérance : quand le peut-on ?

1. 
2. 
3. 
4. 
5. 
6. 
7. 

### M25b.Q8 — Pondérer la KL : multiplicateur, information mutuelle, posterior agrégé et code effondré

1. 
2. 
3. 
4. 
5. 
6. 

## 🔁 Rappels

### M25b.R1 — Bayes sur une variable cachée et log-sum-exp : probabilités totales, posterior, et une somme d'exponentielles sans dépassement (M04, M05a)

1. 
2. 
3. 
4. 
5. 
6. 

### M25b.R2 — L'inégalité de Jensen, la KL continue et l'information mutuelle (M06, M25a)

1. 
2. 
3. 
4. 
5. 
6. 

### M25b.R3 — La SVD, l'ACP et la projection orthogonale sur un sous-espace (M12b, M12d)

1. 
2. 
3. 
4. 
5. 
6. 

## ✏️ Papier-crayon

### Ex M25b.1 — Trois machines produisent des pièces de longueurs gaussiennes : le graphe, la loi jointe, un tirage ancestral à la main, la vraisemblance marginale d'une longueur et le posterior de la machine

- a :
- b :
- c :
- d :
- e :
- f :
- dans ta copie :

### Ex M25b.2 — Deux variétés de grains de café (longueur, largeur) : moyenne et covariance du mélange par la variance totale, part de la variance entre variétés, et une corrélation qu'aucune variété n'a

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M25b.3 — Deux séries de résistances mélangées : les responsabilités de quatre mesures en log, un pas M (proportion, moyennes, variances), et la log-vraisemblance qui monte (suite de M13a, composantes inconnues)

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M25b.6 — Une sonde de qualité de l'eau, un état caché à deux valeurs et une mesure gaussienne : ln p(x), l'ELBO pour trois lois q, et l'écart égal à la KL au posterior

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M25b.9 — Trois épreuves d'un concours expliquées par une aptitude cachée : covariance marginale, posterior d'un candidat (une règle affine des notes), et maximum de vraisemblance à partir de valeurs propres données, dont une direction éteinte

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- i :
- dans ta copie :

### Ex M25b.10 — Les angles principaux entre deux plans de ℝ⁴ et entre deux droites de ℝ³ : bases orthonormées, SVD de Q_Aᵀ Q_B, et pourquoi le résultat ne dépend pas des bases choisies

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M25b.12 — Le coût d'un stock c face à une demande gaussienne : E[(D − c)⁺], ses dérivées en μ et en σ par le chemin, puis par la formule fermée

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- dans ta copie :

### Ex M25b.13 — Une seule gaussienne pour la loi bimodale des temps de trajet par deux itinéraires : KL(p ‖ q) apparie les moments, KL(q ‖ p) choisit un itinéraire

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

### Ex M25b.14 — Un code stochastique d'une source à trois symboles : posterior agrégé, information mutuelle, KL moyenne au prior décomposée en I(X ; Z) + KL(q(z) ‖ p(z)), puis le code qui s'effondre

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

## ∂ Démonstrations

### Ex M25b.4 — Le pas M d'un mélange de gaussiennes : les poids N_k/n par un multiplicateur de Lagrange, les moyennes et les covariances comme maximum de vraisemblance pondéré

1. 
2. 
3. 
4. 
5. 

### Ex M25b.5 — L'ELBO en général : ln p(x) = ELBO(q) + KL(q ‖ p(z | x)) pour un latent discret ou continu, la borne retrouvée par Jensen, et la forme E_q[ln p(x | z)] − KL(q ‖ p(z))

1. 
2. 
3. 
4. 
5. 

### Ex M25b.7 — L'EM comme montée par coordonnées de l'ELBO : le pas E maximise en q, le pas M en θ, d'où la monotonie ; et ∇ ln p(x) = E_{p(z | x)}[∇ ln p(x, z)] pour la moyenne d'une composante

1. 
2. 
3. 
4. 
5. 

### Ex M25b.8 — L'ACP probabiliste : la loi marginale N(μ, WWᵀ + σ²I), le posterior de z par le modèle linéaire gaussien, et W ou WR donnent la même loi

1. 
2. 
3. 
4. 
5. 

### Ex M25b.11 — Dériver une espérance par rapport à un paramètre de la loi : l'échange de la dérivée et de l'espérance sous une hypothèse de domination (démontré), la variance de l'estimateur à un tirage de ∂_σ E[e^X], et une indicatrice 1{X > c} pour laquelle l'échange échoue

1. 
2. 
3. 
4. 

### Ex M25b.15 — β comme multiplicateur de Lagrange : une mesure gaussienne codée avec du bruit, distorsion s² e^{−2I}, le lagrangien D + βI, et le code qui s'éteint quand β dépasse 2s²

1. 
2. 
3. 
4. 
5. 

## 📖 🗣️ 🔗 Lecture, explication et pont

### Ex M25b.16 — MML §8.4 et §8.5 : modèles probabilistes, inférence bayésienne, modèles à variables latentes, graphes orientés et d-séparation (survol), en anglais

1. 
2. 
3. 
4. 
5. 

### Ex M25b.17 — MML ch. 11 : mélange de gaussiennes, responsabilités, mises à jour, EM et point de vue latent, en anglais ; refaire l'Exemple 11.1 avec ses propres données

1. 
2. 
3. 
4. 
5. 

### Ex M25b.18 — MML §10.7 : l'ACP probabiliste, processus génératif, vraisemblance, loi jointe et posterior, en anglais

1. 
2. 
3. 
4. 
5. 

### Ex M25b.19 — Expliquer l'EM avec un bac de pièces venues de deux machines inconnues : deviner, réestimer, recommencer, sans jamais reculer

*Ta réponse en 6 à 10 phrases, sans formule, avec l'image du bac, puis en 3 phrases.*

> 

### Ex M25b.23 — Pont : l'ELBO de n mesures rangées en lignes, écrite « reconstruction moins KL au prior » E_q[ln p(x | z)] − KL(q ‖ π), en nats par mesure, et ce que gagne chaque terme quand q devient le posterior

- a :
- b :
- c :
- d :
- e :
- f :
- g :
- h :
- dans ta copie :

## 💼 Entretien

### M25b.E1 — « Pourquoi l'algorithme EM ne fait-il jamais baisser la vraisemblance, et vers quoi converge-t-il ? »

*Ta réponse orale de 60 secondes, écrite ici après l'avoir dite à voix haute.*

> 

## Notebook

*Tes réponses aux exercices du notebook se tapent dans ta copie du notebook. Note ici ce que tu veux garder : tes raisonnements, tes erreurs, tes questions.*

### Ex M25b.20 — Les responsabilités d'un mélange de gaussiennes, calculées en log (le pas E) · gmm_e_step

- tes contrôles d'entrées ; le log-sum-exp de chaque ligne ; ce que donne la résistance de 120 Ω :

### Ex M25b.21 — Le pas M d'un mélange de gaussiennes : poids, moyennes et covariances pondérées, avec une régularisation · gmm_m_step

- la division par N_k, la nouvelle moyenne dans la covariance ; le cas d'une seule résistance :

### Ex M25b.22 — La log-vraisemblance d'un mélange de gaussiennes, et son ELBO pour des responsabilités quelconques · gmm_log_likelihood, gmm_elbo

- la convention 0 ln 0 = 0 ; l'ELBO sous la log-vraisemblance et l'écart en KL :

### Ex M25b.24 — scipy.linalg.subspace_angles et np.linalg.eigh : les angles principaux de M25b.10, et l'ACP probabiliste de mesures par leurs valeurs propres, contre la vraisemblance de mvn_logpdf

- ce que dit la section *Returns* ; σ̂², ŵ et les comparaisons de log-vraisemblances :

### Ex M25b.25 — Prédire ce que devient la log-vraisemblance quand une composante centrée sur un point se resserre (σ_k = 10⁻¹, 10⁻³, 10⁻⁶), puis avec une régularisation, et mesurer

- tes prédictions avant l'expérience ; celles qui étaient fausses, et pourquoi :

### Ex M25b.26 — L'EM sur des longueurs de poissons de trois cohortes : la log-vraisemblance et l'ELBO après chaque demi-pas, sans régularisation, plusieurs initialisations et des maxima locaux

- l'escalier des deux courbes ; les essais bloqués et ce qu'ils font des cohortes :

### Ex M25b.27 — Une gaussienne ajustée à un mélange bimodal par KL(p ‖ q) puis par KL(q ‖ p) : les deux courbes, et les deux minima de la KL inverse

- ce que montre chaque panneau ; pourquoi ln p par un log-sum-exp :

### Ex M25b.28 — Chasse à l'erreur : des responsabilités sans log qui donnent 0/0, un pas M qui divise par n au lieu de N_k, et une ELBO sans l'entropie de q

- pour chaque erreur : ce qu'elle faisait, pourquoi la vérification fournie ne la voyait pas, et ta correction :

### Ex M25b.29 — Un test de propriété : sur des mélanges tirés au hasard, ELBO ≤ log-vraisemblance, égalité après le pas E, et un EM sans régularisation (reg = 0) qui ne descend jamais (à une tolérance près)

- ta tolérance et sa justification ; les compteurs, et les pas faux que ton test attrape :

### Ex M25b.30 — Défi : retrouver trois populations de mesures en dimension 2 par l'EM, sous un seuil de log-vraisemblance moyenne sur des mesures de test

- tes réglages (initialisations, reg, arrêt) ; ta log-vraisemblance de test et ce que donnent K = 2 et K = 6 :
