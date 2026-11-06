# Test de positionnement (POS)

> Juste après R0, avant R1. Deux heures environ, sur papier. Il mesure ce qui te reste du lycée, chapitre par chapitre de la remise à niveau (R1 à R9), et te dit pour chacun : **tu peux sauter**, **à survoler** ou **à faire en entier**.

Tu peux aussi ne pas le passer et faire R1 à R9 en entier : c'est le parcours par défaut, et le plus sûr si tes maths sont très loin. Le test sert à ne pas passer dix heures sur un chapitre que tu sais déjà.

## Les fichiers

| Fichier | Ce que c'est | Quand |
|---|---|---|
| `01_sujet.md` | les 18 exercices, deux par chapitre de R1 à R9 | pendant le test |
| `02_notebook.ipynb` | vérifie tes réponses et calcule ta grille | après le test |
| `04_mes_reponses.md` | ta feuille de réponses (ta copie est dans `mon_travail/positionnement/`) | pendant le test |
| `05_grille.md` | ce que veut dire chaque verdict, et ce qu'il faut faire quand même | après le notebook |
| `03_corrige.md` | réponses, démarche, erreur fréquente et section qui enseigne chaque question | **en dernier** |
| `03_solutions.ipynb` | le notebook rempli avec les bonnes réponses | jamais avant la fin |

## Les étapes

1. **Prépare ta copie** : `python tools/start_chapter.py POS` copie le notebook et la feuille de réponses dans `mon_travail/positionnement/` (sur Colab : `00_setup/COLAB.md` §2). Ouvre **ta copie** du notebook.
2. **Passe le test sur papier** (environ 2 h) : `01_sujet.md`, sans fiche, sans calculatrice, sans assistant IA. Écris réponses et démarche dans ta copie de `04_mes_reponses.md` ou sur une feuille. Laisse vide ce que tu ne sais pas faire.
3. **Reporte tes réponses** dans ta copie du notebook, une cellule par exercice, sous la forme apprise en R0 (fiche §3) : `0.75`, `"5/8"`, `"3*x**2 - 1"`, `"]-7 ; 0]"`, `[4, -1]`, `True`. Une question laissée vide reste à `...` (points de suspension). Ne corrige rien à ce moment-là : reporte ce que tu as écrit sur papier.
4. **Calcule ta grille** : dans la cellule des outils, mets `FINISHED = True`, puis « Tout exécuter ». La dernière cellule affiche, pour chaque chapitre, un score sur 2 et un verdict.
5. **Lis `05_grille.md`** : pour un chapitre « sauté », il reste quelques exercices à faire (les fonctions de ta librairie `mymath`), et les quiz.
6. **Lis `03_corrige.md`** pour chaque question ratée : il dit quelle section du chapitre l'enseigne.
7. **Recopie ta grille** à la fin de ta copie de `04_mes_reponses.md` et dans ton journal (`mon_travail/suivi/journal.md`), coche POS dans ton tableau de bord, puis passe à R1.

## Les messages du notebook

Chaque cellule affiche ✅ ou un message, comme dans les chapitres. Ici, ne t'en sers pas pour corriger ta réponse et relancer : le test mesure ce que tu savais **sur papier**, et une réponse corrigée grâce au message te ferait sauter un chapitre dont tu as besoin. Les messages te serviront au corrigé, pour comprendre ton erreur.

Une seule exception : quand le message porte sur la **forme** (une virgule au lieu d'un point hors des guillemets, des guillemets oubliés, une expression que `wbm.check` ne sait pas lire), corrige la forme et relance, sans toucher à la valeur que tu avais écrite sur papier.

Si tu refais le test plus tard (après avoir travaillé un chapitre, par exemple), garde ta première grille : c'est elle qui mesure ce qui te restait du lycée.
