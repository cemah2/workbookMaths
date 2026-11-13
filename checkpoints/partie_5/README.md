# CP5 · Bilan de la partie V (M21 et M22)

Le bilan clôt la partie V, juste avant le checkpoint V de workbookIA. Il vérifie que les concepts tiennent : convolution et corrélation croisée, matrices de Toeplitz et circulantes, équivariance, positions d'une fenêtre et convolution transposée, canaux et champ récepteur, pire cas d'une perturbation bornée ; récurrences avec entrée et réponse impulsionnelle, valeurs propres complexes, rayon spectral, normes induites, produits de matrices et de jacobiennes, sensibilité à un paramètre utilisé à chaque pas, vecteurs faits de blocs. Compte environ **3 h 07** : la lecture de ce bilan (15 min), la synthèse (60 min), l'examen blanc (112 min), sans compter la correction et la remédiation. Pas de mini-projet : celui de workbookIA applique ces maths juste après.

| Fichier | Contenu | Quand |
|---|---|---|
| [`05_synthese.md`](05_synthese.md) | CP5.11 : ta carte mentale et ta fiche d'une page, puis les versions de référence (carte, formules clés, pièges, ce qui sert dans workbookIA, vocabulaire à l'oral) | **avant** l'examen |
| [`01_examen_sujet.md`](01_examen_sujet.md) | le sujet de l'examen blanc : 11 questions, 112 minutes, noté sur 20, tout sur papier | le jour de l'examen |
| [`04_mes_reponses.md`](04_mes_reponses.md) | ta copie : une section par question, et le tableau de ta note | pendant, puis après |
| [`02_examen_notebook.ipynb`](02_examen_notebook.ipynb) | la vérification automatique des réponses chiffrées de ta copie | **après** l'examen |
| [`03_examen_corrige.md`](03_examen_corrige.md) | le corrigé détaillé, le barème sur 20 et la remédiation | **après** l'examen |
| [`03_examen_solutions.ipynb`](03_examen_solutions.ipynb) | l'enregistrement des réponses vérifiées (pour Claude et les curieux) | après l'examen |

## Déroulé conseillé

1. **Prépare** : `python tools/start_chapter.py CP5` copie dans `mon_travail/checkpoints/partie_5/` le notebook de vérification et ta copie (`04_mes_reponses.md`). Ce sont ces copies que tu remplis : les fichiers de ce dossier sont mis à jour par Claude.
2. **Fais la synthèse** (`05_synthese.md`, environ 60 minutes), un autre jour que l'examen si possible.
3. **Passe l'examen en conditions réelles** : 112 minutes d'une traite, fiches, flashcards, annexes et corrigés fermés, sans assistant IA (les règles sont en tête du sujet). Tout se fait sur papier ou dans ta copie de `04_mes_reponses.md` ; la calculatrice est permise (ou Python comme simple calculatrice), mais pas NumPy : quand une question nomme une fonction de NumPy, c'est à toi de calculer ce qu'elle rendrait.
4. **Vérifie** : dans ta copie du notebook, passe `EXAM_OVER` à `True`, puis reporte les réponses de ta copie. Chaque réponse chiffrée reçoit ✅ ou ❌ avec une piste.
5. **Note ta copie** avec le barème du corrigé (un point par minute prévue, partagé également entre les sous-questions de chaque question ; ta note sur 20 est ton total sur 112 divisé par 5,6) : il donne aussi les points des démarches, des justifications, du quiz, de la démonstration et des corrections, que le notebook ne voit pas. Remplis le tableau en fin de copie, avec le temps réellement passé sur chaque question.
6. **Remédie** : pour chaque question où tu as eu moins de la moitié des points, refais les exercices indiqués par le corrigé ; une semaine plus tard, refais ces questions sans le corrigé.

Tu peux aussi faire corriger ta copie par Claude : il lit `mon_travail/checkpoints/partie_5/`, sans jamais y écrire.

Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`, puis coche CP5 dans ton tableau de bord. Ensuite : **le checkpoint V de workbookIA** et son mini-projet ; la suite de ce dépôt reprend avec la partie VI, par M25a (la gaussienne multivariée), avant workbookIA 25.
