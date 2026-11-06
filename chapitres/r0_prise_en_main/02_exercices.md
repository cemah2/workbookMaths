# R0 · Prise en main — exercices papier et quiz

> Écris tes réponses dans **ta copie** `mon_travail/r0_prise_en_main/06_mes_reponses.md` (créée par `python tools/start_chapter.py R0`), jamais dans ce fichier : il est mis à jour par Claude.
> Les réponses de l'exercice ✏️ se vérifient dans la **partie 0** du notebook (`wbm.check`) ; les quiz et les exercices 🗣️ et 🛠️ se corrigent avec `05_solutions.md`. Indices : `04_indices.md`.

**Sommaire** : [🧠 Quiz](#quiz) · [✏️ Papier-crayon](#papier) · [🗣️ 🛠️ Réflexion et outils](#reflexion) · [Exercices du notebook](#notebook)

Légende : ★ application directe · ★★ standard · ★★★ approfondi · ★★★★ défi · ⏱️ durée indicative · parcours C = complet, E = essentiel.

R0 n'a pas d'exercice de rappel 🔁 : c'est le premier chapitre. Les rappels commencent en R1.

<a id="quiz"></a>

## 🧠 Quiz

Sans la fiche, en 3 minutes chacun. Réponds vite, puis vérifie dans `05_solutions.md`.

### R0.Q1 — Le notebook : cellules, ordre d'exécution, « Run all » 🧠 ★ ⏱️ 3 min
*Fiche §1 · parcours C, E*

Vrai ou faux ?
1. Tu écris tes réponses dans les fichiers de `chapitres/r0_prise_en_main/`.
2. La cellule ⚙️ SETUP s'exécute en premier, à chaque ouverture du notebook.
3. Une cellule qui affiche ⏳ contient une erreur dans ton code.
4. « Redémarrer et tout exécuter » vérifie que le notebook fonctionne de haut en bas, à partir d'une mémoire vide.
5. Pour un exercice ✏️, on tape d'abord une réponse dans le notebook, puis on refait le calcul sur papier pour comprendre.

### R0.Q2 — Python calculatrice : `**` ou `^`, `//` ou `%` 🧠 ★ ⏱️ 3 min
*Fiche §2 · parcours C, E*

Que vaut chaque expression en Python ? Donne la valeur **et** dis si c'est un entier (`int`) ou un flottant (`float`).
1. `2 ** 3`
2. `2 ^ 3`
3. `20 // 3`
4. `20 % 3`
5. `20 / 4`
6. `-7 // 2`

### R0.Q3 — Taper une réponse : fraction, expression, intervalle 🧠 ★ ⏱️ 3 min
*Fiche §3 · parcours C, E*

Pour chaque réponse tapée, `wbm.check` l'accepte-t-il ? Réponds par oui ou non.
1. Réponse attendue : la fraction exacte $\frac{1}{3}$. Tu tapes `1/3`, sans guillemets.
2. Même réponse attendue. Tu tapes `"1/3"`, entre guillemets.
3. Réponse attendue : l'expression $2x^2 + 1$. Tu tapes `"2x^2 + 1"`.
4. Réponse attendue : l'intervalle des réels positifs ou nuls. Tu tapes `"[0 ; +oo]"`.
5. Réponse attendue : l'intervalle $]1 ; 4]$. Tu tapes `"(1, 4]"`.

### R0.Q4 — SymPy et LaTeX : vrai ou faux 🧠 ★ ⏱️ 3 min
*Fiche §4, §5 · parcours C*

Avec `import sympy as sp` et `x = sp.Symbol("x")` déjà exécutés. Vrai ou faux ?
1. `sp.expand((x + 1)**2)` renvoie `x**2 + 2*x + 1`.
2. `sp.sqrt(8)` renvoie une valeur approchée, `2.828…`.
3. Pour vérifier que mon développement `mine` de `(x + 5)**2` est juste, je peux regarder si `sp.expand((x + 5)**2 - mine)` vaut 0.
4. En LaTeX, `$x^10$` affiche $x$ à la puissance 10.
5. En LaTeX, `$\frac{a}{b}$` affiche la fraction $a$ sur $b$.

<a id="papier"></a>

## ✏️ Papier-crayon

Fais-le **à la main**, sans ordinateur, en écrivant ta démarche dans ta copie de `06_mes_reponses.md`. Reporte ensuite **la valeur** trouvée dans la **partie 0 du notebook**, qui la vérifie avec `wbm.check` (par exemple `answer_R0_1a = 23` si tu as trouvé 23, et pas le calcul lui-même).

### Ex R0.1 — Calculer avec Python : priorités, division entière et reste ✏️ ★ ⏱️ 10 min
**Objectif :** prévoir ce que Python calcule en appliquant ses priorités, sa division euclidienne et ses puissances.
**Prérequis :** fiche §2 · **Parcours :** C, E

Sans ordinateur, donne la valeur que Python affiche pour chaque expression. Pour j, écris un flottant (avec un point).

| | Expression |
|---|---|
| a | `5 + 2 * 3 ** 2` |
| b | `(5 + 2) * 3 ** 2` |
| c | `-4 ** 2` |
| d | `(-4) ** 2` |
| e | `29 // 6` |
| f | `29 % 6` |
| g | `-29 // 6` |
| h | `-29 % 6` |
| i | `4 ** 3 ** 0` |
| j | `10 / 4 * 2` |

Pour g et h, écris d'abord la division euclidienne sous la forme $-29 = 6q + r$ avec $0 \le r < 6$.

<a id="reflexion"></a>

## 🗣️ 🛠️ Réflexion et outils

### Ex R0.2 — Expliquer à quoi sert `wbm.check`, et pourquoi il ne montre jamais la réponse 🗣️ ★ ⏱️ 10 min
**Objectif :** expliquer simplement comment une réponse peut être vérifiée sans être stockée.
**Prérequis :** fiche §3 · **Parcours :** C

Un ami découvre le workbook. Il demande : « Si le notebook sait dire que ma réponse est fausse, c'est qu'il connaît la bonne : pourquoi ne pas l'afficher ? Et si elle est quelque part dans le dépôt, je peux la lire ? »

Réponds-lui **en cinq lignes au plus**, sans jargon. Ta réponse doit parler de : l'empreinte d'une réponse, ce que `wbm.check` compare vraiment, et la raison pédagogique de ne pas afficher la réponse.

### Ex R0.8 — Écrire trois formules en LaTeX dans ta feuille de réponses 🛠️ ★ ⏱️ 15 min
**Objectif :** écrire des formules lisibles en LaTeX dans un fichier Markdown.
**Prérequis :** fiche §5 · **Parcours :** C, E

**Fais-le tôt** : tu t'en serviras pour toutes tes réponses papier de la remise à niveau.

Dans ta copie de `06_mes_reponses.md` (section R0.8), écris en LaTeX, chacune sur sa ligne entre `$$` :
1. la moyenne de deux nombres : $\dfrac{a + b}{2}$ ;
2. la somme des carrés de $n$ nombres : $\displaystyle\sum_{i=1}^{n} x_i^2$ ;
3. la distance entre deux points du plan : $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.

Vérifie le rendu : aperçu Markdown de VS Code, cellule Markdown de Jupyter ou de Colab, ou page GitHub. Puis compare ton code LaTeX à celui de `05_solutions.md` : plusieurs écritures sont justes.

<a id="notebook"></a>

## Exercices du notebook

Les exercices suivants se font dans `03_notebook.ipynb` (ta copie : `mon_travail/r0_prise_en_main/03_notebook.ipynb`). La partie 0 du notebook vérifie tes réponses à l'exercice ✏️ R0.1.

| ID | Titre | Type | ★ | ⏱️ | Parcours |
|---|---|---|---|---|---|
| R0.3 | Taper une fraction exacte, une expression et un intervalle | 📦 | ★ | 10 | C, E |
| R0.4 | Prédire : 0,1 + 0,2 vaut-il 0,3 pour Python ? | 🔮 | ★ | 10 | C, E |
| R0.5 | Vérifier un développement avec SymPy (`expand`, `simplify`) | 📦 | ★ | 15 | C, E |
| R0.6 | Chasse à l'erreur : `x^2` et `2x` en Python | 🐛 | ★ | 10 | C, E |
| R0.7 | Tracer une fonction avec matplotlib | 🎨 | ★ | 10 | C |
| R0.9 | Ta première fonction : la moyenne (`mean`) | 🔨 | ★ | 25 | C, E |

Indices : `04_indices.md` (section « Notebook ») ; solutions commentées : `05_solutions.md` et `05_solutions.ipynb`.
