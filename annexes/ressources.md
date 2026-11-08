# Ressources

Les ressources que les fiches citent. Chaque lien a été vérifié avant d'être cité (date entre parenthèses) ; une ressource « à confirmer » n'est citée par une fiche qu'après une nouvelle vérification.

## Le livre de référence

| Ressource | Ce que c'est | Accès et licence | Vérifié |
|---|---|---|---|
| M. P. Deisenroth, A. A. Faisal, C. S. Ong, *Mathematics for Machine Learning* (MML), Cambridge University Press, 2020 | le livre que suit le workbook à partir de la partie I (algèbre linéaire, géométrie, décompositions, calcul vectoriel, probabilités, optimisation, puis régression, ACP, mélanges, SVM) | PDF gratuit pour un **usage personnel** sur le site du livre ([mml-book.github.io](https://mml-book.github.io/)) ; redistribution et œuvres dérivées interdites : ne le mets jamais dans ton dépôt | 2026-11-05 (sommaire et notice) |

## Probabilités, statistique, information

| Ressource | Ce que c'est | Accès et licence | Vérifié |
|---|---|---|---|
| J. K. Blitzstein et J. Hwang, *Introduction to Probability* (2ᵉ éd.) | le livre du cours Stat 110 de Harvard, très pédagogique (dénombrement, lois, espérance conditionnelle, théorèmes limites, chaînes de Markov) ; cité par R8, M02a, M02b, M02c, M03, M04 (formule de Bayes, loi Beta) et M11 | version en ligne gratuite annoncée par la page du cours ([stat110.hsites.harvard.edu](https://stat110.hsites.harvard.edu/)), vers probabilitybook.net | 2026-11-05 |
| *OpenIntro Statistics* | statistique d'introduction : estimation, intervalles, tests ; cité par M08 | licence Creative Commons BY-SA 3.0 ([openintro.org/license](https://openintro.org/license)) | 2026-11-06 (licence) |
| A. Chouldechova, « Fair prediction with disparate impact: A study of bias in recidivism prediction instruments » (2017) | l'article qui montre qu'on ne peut pas égaliser à la fois precisions et taux d'erreur de groupes de prévalences différentes ; cité par M03 (§8) | prépublication gratuite sur arXiv ([arxiv.org/abs/1703.00056](https://arxiv.org/abs/1703.00056)) | 2026-11-07 (page arXiv) |
| D. J. C. MacKay, *Information Theory, Inference, and Learning Algorithms*, Cambridge University Press, 2003 | la référence libre en théorie de l'information, reliée à l'apprentissage ; lecture facultative de M06 (chapitres 1, 2, 5 et 8) | PDF gratuit mis en ligne par l'auteur **pour la lecture à l'écran** (« free on-screen viewing », annonce de l'auteur, [liste connectionists, octobre 2003](https://mailman.srv.cs.cmu.edu/pipermail/connectionists/2003-October/021362.html) ; « A free PDF is available », [notes du cours MLPR d'Édimbourg](https://www.inf.ed.ac.uk/teaching/courses/mlpr/2019/notes/w0b_books.pdf)), sur la page du livre ([inference.org.uk/mackay/itila/book.html](http://www.inference.org.uk/mackay/itila/book.html)) ; cette page n'a pas pu être lue depuis l'environnement de génération : ouvre-la pour voir les conditions exactes | 2026-11-07 (sources secondaires) |
| C. E. Shannon, « A Mathematical Theory of Communication », *Bell System Technical Journal*, vol. 27, 1948 (n° 3, p. 379–423, et n° 4, p. 623–656) | l'article fondateur de la théorie de l'information (entropie, codage de source, capacité d'un canal), que le chapitre 6 de workbookIA fait lire ; cité par M06 | référence vérifiée sur l'article de Wikipédia qui lui est consacré, lequel renvoie à des copies gratuites du texte intégral ; aucun lien n'est cité tant qu'il n'a pas été ouvert | 2026-11-08 (référence) |
| T. Lattimore et C. Szepesvári, *Bandit Algorithms*, Cambridge University Press, 2020 | le traité de référence sur les bandits, très mathématique : inégalités de concentration (chapitre 5, *Concentration of Measure*), UCB (chapitre 7, *The Upper Confidence Bound Algorithm*), Thompson ; lecture facultative de M11 | édité par Cambridge University Press ; les auteurs diffusent une version PDF sur leur site (tor-lattimore.com, adresse donnée par la notice BibBase du livre) | 2026-11-08 (titres des chapitres 5 et 7 d'après la table des matières de l'éditeur ; accès libre au PDF à confirmer) |

## Calcul numérique

| Ressource | Ce que c'est | Accès et licence | Vérifié |
|---|---|---|---|
| Documentation de Python, tutoriel, chapitre 15 : *Floating-Point Arithmetic: Issues and Limitations* | pourquoi 0,1 n'est pas exact en binaire, l'erreur de représentation, `math.fsum` ; cité par R0 et M05a | gratuit, documentation officielle ([docs.python.org/3/tutorial/floatingpoint.html](https://docs.python.org/3/tutorial/floatingpoint.html)) | 2026-11-07 |

## Documentation officielle

Les fiches de la remise à niveau renvoient aussi aux documentations des bibliothèques qu'elles emploient.

| Ressource | Ce que c'est | Accès | Vérifié |
|---|---|---|---|
| Python, module `fractions` | les fractions exactes de Python ; cité par R1 ([docs.python.org/fr/3/library/fractions.html](https://docs.python.org/fr/3/library/fractions.html)) | gratuit, documentation officielle | 2026-11-06 |
| SymPy, tutoriel *Solvers* | résoudre une équation ou un système avec SymPy ; cité par R2 ([docs.sympy.org/latest/tutorials/intro-tutorial/solvers.html](https://docs.sympy.org/latest/tutorials/intro-tutorial/solvers.html)) | gratuit, documentation officielle | 2026-11-06 |
| NumPy, `numpy.polyval` | évaluer un polynôme, coefficients du plus haut degré au terme constant ; cité par R3 ([numpy.org/doc/stable/reference/generated/numpy.polyval.html](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html)) | gratuit, documentation officielle | 2026-11-06 |

## Démonstrations

| Ressource | Ce que c'est | Accès et licence | Vérifié |
|---|---|---|---|
| R. Hammack, *Book of Proof* (3ᵉ éd., version 3.3) | apprendre à lire et à écrire une démonstration : logique, ensembles, raisonnements direct, par contraposée, par l'absurde, par récurrence ; cité par R4, R5 et M11 | PDF gratuit, licence Creative Commons BY-NC-ND 4.0 ([people.vcu.edu/~rhammack/BookOfProof](https://www.people.vcu.edu/~rhammack/BookOfProof)) | 2026-11-06 |

## Remise à niveau et lycée, en français

| Ressource | Ce que c'est | Accès | Vérifié |
|---|---|---|---|
| Maths et tiques (Yvan Monka) | cours, exercices corrigés et vidéos, du collège au lycée, classés par niveau ([maths-et-tiques.fr](https://www.maths-et-tiques.fr)) | gratuit | 2026-11-06 |
| Khan Academy en français | cours en vidéo et exercices interactifs, du collège au lycée | gratuit | 2026-11-06 (existence de la version française ; lien précis par chapitre à confirmer) |
| Sésamath | manuels libres du collège et du lycée, écrits par des enseignants | gratuit ; licence de chaque manuel à confirmer | à confirmer (R1) |

## Niveau licence, en français

| Ressource | Ce que c'est | Accès | Vérifié |
|---|---|---|---|
| Exo7 (Université de Lille) | cours et exercices en vidéo de première année : dérivées, développements limités, applications linéaires, déterminants, dimension finie, dénombrement… ([pod.univ-lille.fr/exo7](https://pod.univ-lille.fr/exo7/)) ; cité par R9, M02a et M02b | gratuit | 2026-11-06 |

## Pour voir les maths

| Ressource | Ce que c'est | Vérifié |
|---|---|---|
| 3Blue1Brown, *Essence of linear algebra* | série de vidéos courtes et très visuelles (en anglais, sous-titres disponibles) : une matrice vue comme une transformation du plan, le produit comme une composition ; déjà conseillée par le chapitre 0B de workbookIA ; citée par M09a ([3blue1brown.com/lessons/eola-preview](https://www.3blue1brown.com/lessons/eola-preview), le chapitre 0 de la série) | 2026-11-08 |
| 3Blue1Brown, *Essence of calculus* | la série équivalente sur le calcul différentiel et intégral, déjà conseillée par le chapitre 0B de workbookIA | à confirmer à la première citation |
| 3Blue1Brown, *Why π is in the normal distribution (beyond integral tricks)* (2023) | une vidéo (en anglais, sous-titres disponibles) sur l'origine du $\pi$ de la loi normale, par la symétrie de la loi à deux dimensions ; citée par M02b ([3blue1brown.substack.com](https://3blue1brown.substack.com/p/why-is-in-the-normal-distribution)) | 2026-11-07 |
| 3Blue1Brown, *But what is the Central Limit Theorem?* (2023) | une vidéo (en anglais, sous-titres disponibles) sur le théorème central limite, vu sur des sommes de dés ; citée par M02c ([3blue1brown.com/lessons/clt](https://www.3blue1brown.com/lessons/clt)) | 2026-11-07 |
