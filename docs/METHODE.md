# MÉTHODE — Construire (et utiliser) workbookMaths avec Claude

Ce guide est pour toi. Il explique **comment piloter Claude, session après session**, et **comment étudier les deux workbooks en même temps**. La spécification est `docs/BIBLE.md` ; les consignes que Claude lit à chaque session sont dans `CLAUDE.md`.

---

## 1. Principes

1. **Une spécification unique, la bible.** Toutes les sessions suivent le même document : chaque chapitre a la même structure et les mêmes conventions.
2. **Un chapitre par conversation.** Claude travaille mieux avec un contexte frais.
3. **Le dépôt GitHub comme mémoire.** Chaque session repart du dépôt (chapitres faits, code `mymath`, `suivi/PROGRESS.md`) et y pousse son travail.
4. **Rien n'est livré sans avoir été exécuté.** Claude fait tourner les notebooks de solutions et les tests, et fait revérifier les calculs par un second agent indépendant.
5. **Génération en avance sur l'étude**, dans l'**ordre de travail commun** (README) : la remise à niveau d'abord, puis les chapitres de maths dans l'ordre des chapitres de workbookIA qu'ils préparent.
6. **workbookIA n'est jamais modifié** par ces sessions : Claude le lit seulement, pour savoir de quelles maths chaque chapitre a besoin et pour ne jamais en reprendre les exercices.

## 2. Déroulé des sessions

| # | Session | Ce que tu demandes | Ton rôle après la session |
|---|---|---|---|
| 1 ✅ | Mise en place : outils, versions, consignes, démo | (fait le 2026-11-06) | Ouvrir `00_setup/demo.ipynb` dans Colab et vérifier qu'il tourne |
| 2 | Syllabus détaillé : tous les exercices planifiés, signatures `mymath`, parcours, temps | « Session 2 : syllabus » (modèle ci-dessous) | **Relire `docs/SYLLABUS.md`** : c'est le moment de tout changer |
| 3 → ~14 | Remise à niveau R0 à R9, test de positionnement, examen CP0 | « Session : chapitre R3 » | Commencer l'étude (et workbookIA 0A en parallèle) |
| suite | Chapitres M02a à MB8, dans l'ordre de travail commun ; un examen blanc à la fin de chaque partie | « Session : chapitre M12c » | Étudier, puis envoyer ton retour |
| après les parties 0, II, IV | Audit qualité indépendant | « Audit des parties … » | Valider les corrections majeures |
| dernière | Projet de synthèse, finalisation (index des notions, deck Anki global) | « Finalisation » | 🎓 |

Compte **environ 70 sessions**.

### Modèles de demandes (à copier dans une nouvelle conversation)

- **Générer un chapitre** : « Session de génération de workbookMaths : chapitre `M12c`. Clone `cemah2/workbookMaths` (écriture) et `cemah2/workbookIA` (lecture seule, ne le modifie jamais), lis `CLAUDE.md` puis suis-le. Pousse à la fin. »
- **Reprendre une session interrompue** : « Reprends la session de génération de workbookMaths là où `suivi/PROGRESS.md` l'indique. »
- **Correction ciblée** : « Dans workbookMaths, chapitre `R3`, exercice `R3.12` : [le problème]. Corrige en respectant la bible. »
- **Retour d'étude** (calibrage) : « Retour sur workbookMaths `R3` : temps réel [..], trop dur / trop facile [..], pas clair [..]. Mets à jour le calibrage dans `PROGRESS.md` pour les chapitres suivants. »
- **Tuteur** : « Je bloque sur l'exercice `M12c.7` de workbookMaths. Guide-moi par questions, sans me donner la réponse. »
- **Correction de mon travail** : « Corrige mon travail du chapitre `R3` de workbookMaths (`mon_travail/r3_…/06_mes_reponses.md` et mon notebook), en lecture seule. »

## 3. Comment étudier les deux workbooks en même temps

**L'ordre** est dans le README (« Ordre de travail commun ») et dans ton tableau de bord : remise à niveau R0 à R9 pendant workbookIA 0A, puis l'examen CP0, puis workbookIA 0B, puis, pour chaque chapitre k de workbookIA, d'abord ses chapitres de maths (`python tools/start_chapter.py k` les prépare tous).

**Routine d'un chapitre de maths :**

1. **`python tools/start_chapter.py M12c`** (ou `12`) : copie le notebook, ta feuille de réponses `06_mes_reponses.md` et les squelettes `mymath` dans `mon_travail/`.
2. **La fiche** (`01_fiche.md`) : lis « Comment utiliser ce chapitre », les objectifs et « L'essentiel en 10 lignes ».
3. **Bloc par bloc, comme avec Glassner** : la section de MML indiquée par la fiche, puis la partie de la fiche correspondante (elle reprend tout en français : appuie-toi dessus quand un passage du livre résiste), puis les quiz 🧠 et les exercices papier ✏️ et ∂ de ce bloc, **crayon en main**. La remise à niveau R0 à R9 n'a pas de livre : la fiche est le cours.
4. **Vérifie tes calculs papier** dans la partie 0 du notebook (`wbm.check`), puis fais le reste du notebook ; à chaque 🔮, écris ta prédiction avant d'exécuter.
5. **Bloqué 15 minutes** : indice 1 ; encore 5 minutes : indice 2, puis l'indice 3. Ou demande au tuteur.
6. **Corrige** avec les solutions ; pour une démonstration ∂, compare la tienne à la **grille de relecture** de la solution.
7. **Flashcards** : `python tools/export_flashcards.py --chapter M12c`, puis Anki (deck « workbookMaths », distinct de celui de workbookIA).
8. **Journal et tableau de bord** dans `mon_travail/suivi/`.
9. **Puis le chapitre de workbookIA** : les maths que tu viens de faire y sont appliquées.

**Règle d'or** : ne lis jamais une solution avant d'avoir *vraiment* essayé. L'effort de récupération, c'est ce qui fait apprendre.

## 4. Mises à jour de la bible

Pour changer une règle globale (plus de démonstrations, moins de quiz…), demande-le en écrivant « modifie la bible » : Claude met à jour `docs/BIBLE.md`, note la décision au §24 et indique quels chapitres déjà générés sont concernés.

## 5. Problèmes fréquents

| Symptôme | Que faire |
|---|---|
| Un passage semble recopié de MML | « Viole la règle §3 de la bible : réécris de manière originale. » |
| Un chapitre de workbookIA utilise une notion que les maths n'ont pas enseignée | Signale-le (correction ciblée) : c'est la règle §16.1 de la bible. |
| Un exercice de maths reprend un exercice de workbookIA | Correction ciblée, en citant la règle de partage du §8. |
| Un chapitre est trop dur ou trop facile | Retour d'étude : le calibrage s'applique aux chapitres suivants. |
