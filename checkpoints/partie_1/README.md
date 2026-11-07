# CP1 · Bilan de la partie I (M02a à M06)

Le bilan clôt la partie I, juste avant le checkpoint I de workbookIA. Il vérifie que les fondations tiennent : intégrales et densités, lois et estimation, probabilités conditionnelles et Bayes, dérivées, gradient et théorie de l'information. Compte environ **3 h 20** : la synthèse (75 min, sa lecture comprise), l'examen blanc (124 min), sans compter la correction et la remédiation. Pas de mini-projet : celui de workbookIA applique ces maths juste après.

| Fichier | Contenu | Quand |
|---|---|---|
| [`05_synthese.md`](05_synthese.md) | CP1.13 : ta carte mentale et ta fiche d'une page, puis les versions de référence (carte, formules clés, pièges, ce qui sert dans workbookIA, vocabulaire à l'oral) | **avant** l'examen |
| [`01_examen_sujet.md`](01_examen_sujet.md) | le sujet de l'examen blanc : 13 questions, 124 minutes, noté sur 20, tout sur papier | le jour de l'examen |
| [`04_mes_reponses.md`](04_mes_reponses.md) | ta copie : une section par question, et le tableau de ta note | pendant, puis après |
| [`02_examen_notebook.ipynb`](02_examen_notebook.ipynb) | la vérification automatique des réponses chiffrées de ta copie | **après** l'examen |
| [`03_examen_corrige.md`](03_examen_corrige.md) | le corrigé détaillé, le barème sur 20 et la remédiation | **après** l'examen |
| [`03_examen_solutions.ipynb`](03_examen_solutions.ipynb) | l'enregistrement des réponses vérifiées (pour Claude et les curieux) | après l'examen |

## Déroulé conseillé

1. **Prépare** : `python tools/start_chapter.py CP1` copie dans `mon_travail/checkpoints/partie_1/` le notebook de vérification et ta copie (`04_mes_reponses.md`). Ce sont ces copies que tu remplis : les fichiers de ce dossier sont mis à jour par Claude.
2. **Fais la synthèse** (`05_synthese.md`, environ 75 minutes), un autre jour que l'examen si possible.
3. **Passe l'examen en conditions réelles** : 124 minutes d'une traite, fiches, flashcards, annexes et corrigés fermés, sans assistant IA (les règles sont en tête du sujet). Tout se fait sur papier ou dans ta copie de `04_mes_reponses.md` ; la calculatrice est permise, et les valeurs utiles de la loi normale et des logarithmes sont dans l'énoncé.
4. **Vérifie** : dans ta copie du notebook, passe `EXAM_OVER` à `True`, puis reporte les réponses de ta copie. Chaque réponse chiffrée reçoit ✅ ou ❌ avec une piste.
5. **Note ta copie** avec le barème du corrigé : il donne aussi les points des démarches, des justifications, du quiz, de la démonstration et des corrections, que le notebook ne voit pas. Remplis le tableau en fin de copie, avec le temps réellement passé sur chaque question.
6. **Remédie** : pour chaque question où tu as eu moins de la moitié des points, refais les exercices indiqués par le corrigé ; une semaine plus tard, refais ces questions sans le corrigé.

Tu peux aussi faire corriger ta copie par Claude : il lit `mon_travail/checkpoints/partie_1/`, sans jamais y écrire.

Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`, puis coche CP1 dans ton tableau de bord. Ensuite : **le checkpoint I de workbookIA** ; la suite de ce dépôt reprend avec M07, avant workbookIA 7.
