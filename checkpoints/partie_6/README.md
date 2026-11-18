# CP6 · Bilan de la partie VI (M25a, M25b, M26, M27 et M28)

Le bilan clôt la partie VI, juste avant le checkpoint VI de workbookIA. Il vérifie que les concepts tiennent : vecteur gaussien, tirage par Cholesky, lois marginales et conditionnelles, KL entre gaussiennes et interpolation sphérique ; mélanges, responsabilités, EM et ELBO ; chaînes de Markov, loi à $n$ pas et système de Bellman d'une politique fixée ; jeux à somme nulle et stratégies mixtes, distances de Wasserstein et de Fréchet, biais d'une distance estimée ; double centrage et positions à une isométrie près, température, troncature top-p et son coût en KL, itérations qui bouclent. Compte environ **3 h 06** : la lecture de ce bilan (15 min), la synthèse (60 min), l'examen blanc (111 min), sans compter la correction et la remédiation. Pas de mini-projet : celui de workbookIA applique ces maths juste après.

| Fichier | Contenu | Quand |
|---|---|---|
| [`05_synthese.md`](05_synthese.md) | CP6.11 : ta carte mentale et ta fiche d'une page, puis les repères de comparaison (carte par questions, ponts, sept mesures entre lois, formules et leurs conditions, faux amis, ce qui sert dans workbookIA, vocabulaire à l'oral) | **avant** l'examen |
| [`01_examen_sujet.md`](01_examen_sujet.md) | le sujet de l'examen blanc : 11 questions, 111 minutes, noté sur 20, tout sur papier | le jour de l'examen |
| [`04_mes_reponses.md`](04_mes_reponses.md) | ta copie : une section par question, et le tableau de ta note | pendant, puis après |
| [`02_examen_notebook.ipynb`](02_examen_notebook.ipynb) | la vérification automatique des réponses chiffrées de ta copie | **après** l'examen |
| [`03_examen_corrige.md`](03_examen_corrige.md) | le corrigé détaillé, le barème sur 20 et la remédiation | **après** l'examen |
| [`03_examen_solutions.ipynb`](03_examen_solutions.ipynb) | l'enregistrement des réponses vérifiées (pour Claude et les curieux) | après l'examen |

## Déroulé conseillé

1. **Prépare** : `python tools/start_chapter.py CP6` copie dans `mon_travail/checkpoints/partie_6/` le notebook de vérification et ta copie (`04_mes_reponses.md`). Ce sont ces copies que tu remplis : les fichiers de ce dossier sont mis à jour par Claude.
2. **Fais la synthèse** (`05_synthese.md`, environ 60 minutes), un autre jour que l'examen si possible.
3. **Passe l'examen en conditions réelles** : 111 minutes d'une traite, fiches, flashcards, annexes et corrigés fermés, sans assistant IA (les règles sont en tête du sujet). Tout se fait sur papier ou dans ta copie de `04_mes_reponses.md` ; la calculatrice est permise (ou Python comme simple calculatrice), mais pas NumPy.
4. **Vérifie** : dans ta copie du notebook, passe `EXAM_OVER` à `True`, puis reporte les réponses de ta copie (ou colle les lignes de `04_mes_reponses.md`). Chaque réponse chiffrée reçoit ✅ ou ❌ avec une piste. Le quiz CP6.Q1, la démonstration CP6.8, les corrections de CP6.9 b) et les justifications « sur ta copie » ne sont pas vérifiés par le notebook : ils se notent avec le corrigé, comme dans CP5.
5. **Note ta copie** avec le barème du corrigé (un point par minute prévue, partagé également entre les sous-questions de chaque question ; ta note sur 20 est ton total sur 111 multiplié par $\frac{20}{111}$, c'est-à-dire divisé par 5,55) : il donne aussi les points des démarches, des justifications, du quiz, de la démonstration et des corrections, que le notebook ne voit pas. Remplis le tableau en fin de copie, avec le temps réellement passé sur chaque question.
6. **Remédie** : pour chaque question où tu as eu moins de la moitié des points, refais les exercices indiqués par le corrigé ; une semaine plus tard, refais ces questions sans le corrigé.

Tu peux aussi faire corriger ta copie par Claude : il lit `mon_travail/checkpoints/partie_6/`, sans jamais y écrire.

Reporte ta note et tes points faibles dans `mon_travail/suivi/journal.md` et `mon_travail/suivi/auto_evaluation.md`, puis coche CP6 dans ton tableau de bord. Ensuite : **le checkpoint VI de workbookIA** et son mini-projet ; la suite de ce dépôt reprend avec la partie VII, par MB2 (cooccurrences, PMI et embeddings), avant workbookIA B2.
