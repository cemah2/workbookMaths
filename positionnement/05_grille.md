# Test de positionnement — la grille

> La dernière cellule du notebook calcule ta grille. Un exercice compte quand **toutes** ses questions sont justes ; chaque chapitre a deux exercices. Cette page dit ce que veut dire chaque verdict, et ce qu'il faut faire quand même.

## Les trois verdicts

| Score | Verdict | Ce que tu fais | Temps |
|---|---|---|---|
| 2/2 | **tu peux sauter** | lis « L'essentiel en 10 lignes » et « Les pièges classiques » de la fiche ; fais les quiz 🧠 ; écris les fonctions `mymath` du parcours essentiel (exercices ci-dessous) ; importe les flashcards | 1 h 15 à 2 h 30 selon le chapitre |
| 1/2 | **à survoler** | lis la fiche en entier, vite, en t'arrêtant sur les sections de tes questions ratées (`03_corrige.md` les donne) ; puis fais le **parcours essentiel** du chapitre | 7 à 11 h selon le chapitre (`docs/PARCOURS.md`) |
| 0/2 | **à faire en entier** | le chapitre complet, dans l'ordre de sa fiche | 9 à 14 h selon le chapitre |

Pourquoi écrire quand même les fonctions `mymath` d'un chapitre sauté ? Ta librairie se construit d'un chapitre à l'autre ; si tu en sautes un module, les notebooks des chapitres suivants prennent la version de référence à sa place (`start_chapter.py` te le signale), mais une librairie entièrement écrite de tes mains vaut plus, en entretien comme pour toi.

## Les fonctions `mymath` à écrire même si tu sautes le chapitre

| Chapitre | Exercices 🔨 du parcours essentiel | Durée totale |
|---|---|---|
| R1 · Nombres et calcul | R1.21, R1.22, R1.24 | 1 h 40 |
| R2 · Calcul littéral et équations | R2.18, R2.21 | 1 h 05 |
| R3 · Fonctions | R3.18, R3.19, R3.20 | 1 h 30 |
| R4 · Logique, ensembles, Σ et Π | R4.18, R4.19 | 55 min |
| R5 · Suites | R5.14, R5.15, R5.16 | 55 min |
| R6 · Exponentielle et logarithmes | R6.14, R6.15 | 35 min |
| R7 · Limites et dérivation | R7.17, R7.19 | 40 min |
| R8 · Probabilités de base | R8.16, R8.18, R8.19 | 50 min |
| R9 · Géométrie du plan, vecteurs et trigonométrie | R9.16, R9.17 | 35 min |

Pour chacun : `python tools/start_chapter.py R3` (par exemple), puis seulement ces exercices dans ta copie du notebook.

## Quatre conseils

- **Sois honnête avec toi-même.** Une réponse devinée juste te fait sauter un chapitre dont tu as besoin, et les chapitres de workbookIA te le feront payer plus tard. Dans le doute, choisis le verdict le plus prudent.
- **La grille est prudente.** Un exercice ne compte que si toutes ses questions sont justes : une seule étourderie le fait tomber, et un exercice de quatre questions y est plus exposé qu'un exercice de deux. Si le corrigé te montre qu'une erreur est vraiment une étourderie (tu savais faire, et tu le refais juste sans aide), tu peux remonter ce chapitre d'un cran ; si tu hésites, garde le verdict.
- **Les chapitres s'appuient les uns sur les autres.** Si tu sautes R5 mais fais R6 en entier, garde la fiche de R5 sous la main : R6 en suppose les notions.
- **Le verdict n'est pas définitif.** Si un chapitre « sauté » te manque plus tard (un exercice de R7 qui te bloque sur les fractions, par exemple), reviens au chapitre en question : sa fiche et ses exercices t'attendent.

Recopie ta grille à la fin de ta copie de `04_mes_reponses.md` et dans ton journal (`mon_travail/suivi/journal.md`). Dans ton tableau de bord, quand tu as fini ce que la grille demande pour un chapitre sauté, coche sa case dans « Ordre de travail commun » et note `sauté (POS 2/2)` au bout de la ligne.
