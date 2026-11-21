# Projet de synthèse · Indices

> **Mode d'emploi.** Cherche d'abord seul. Si tu bloques sur une étape, ouvre **l'indice 1** (la direction), cherche encore, puis l'indice 2 (la méthode), puis l'indice 3 (le gabarit et la liste de contrôle). Ces indices valent pour tous les algorithmes : ce sont des conseils de méthode, jamais le résultat d'une dérivation. Le résultat, c'est toi qui le trouves, et c'est lui que la grille note.

**Sommaire** : [PS.1](#ps1) · [PS.2](#ps2) · [PS.3](#ps3) · [PS.4](#ps4) · [PS.5](#ps5) · [PS.6](#ps6) · [PS.7](#ps7) · [PS.8](#ps8) · [PS.9](#ps9) · [PS.E1](#pse1)

<a id="ps1"></a>

### PS.1 — Cadrer

<details><summary>Indice 1</summary>

Pars de la liste et de ton projet final de workbookIA. Pour chaque candidat, ouvre les fiches de la colonne « Préparé par » : choisis l'algorithme dont tu sais déjà écrire l'objectif en une ligne, et dont la dérivation te paraît longue sans te paraître hors de portée.

</details>
<details><summary>Indice 2</summary>

Écris l'objectif en une ligne, puis la liste des opérations qu'il faudra dériver ou démontrer (une composition, un produit de matrices, une espérance, un maximum, une itération). Pour chacune, cherche la section qui l'enseigne : `annexes/correspondances.md`, puis la table des matières des fiches. Pour l'oracle, lis la documentation de la fonction jusqu'à ses paramètres par défaut, et note chacun de ceux qui changent ce qui est calculé.

</details>
<details><summary>Indice 3</summary>

Un squelette de cadrage : (1) une phrase sur ce que l'algorithme calcule ; (2) ses entrées et ses sorties, avec leurs formes ; (3) quatre à huit notions, chacune sous la forme « notion → chapitre §n » ; (4) l'oracle, ses réglages, et ce qu'il ne voit pas (souvent : il ne voit que le résultat final, pas les étapes intermédiaires) ; (5) deux propriétés, l'une sur **ce que** l'algorithme trouve (existence, unicité, optimum), l'autre sur **la façon** dont il le trouve (convergence, coût, variance) ; le cas limite est l'hypothèse dont la première a besoin.

</details>

<a id="ps2"></a>

### PS.2 — Poser le problème

<details><summary>Indice 1</summary>

Tout symbole de §3 doit être dans le tableau des notations. Écris le tableau d'abord, la dérivation ensuite : un symbole qui manque au tableau est souvent un objet dont tu n'as pas fixé la forme.

</details>
<details><summary>Indice 2</summary>

Pour chaque objet, pose la question de la forme : combien d'exemples, combien de features, combien de sorties ? Écris `(n, p)`, jamais « une matrice ». Pour les hypothèses, parcours la dérivation que tu prévois : chaque division, chaque inverse, chaque logarithme, chaque racine en demande une.

</details>
<details><summary>Indice 3</summary>

Une ligne de tableau complète : symbole, sens, forme, domaine (« $\mathbf{X}$ | les exemples, un par ligne | $(n, p)$ | $\mathbb{R}^{n \times p}$ »). Les conventions à écrire noir sur blanc : les exemples sont-ils les lignes de $\mathbf{X}$ ? Le gradient a-t-il la forme de la variable, ou est-il écrit en ligne (M17 §4) ? L'objectif est-il une somme ou une moyenne sur les exemples, et ce choix se retrouve-t-il dans chaque formule qui en dérive ?

</details>

<a id="ps3"></a>

### PS.3 — La dérivation complète

<details><summary>Indice 1</summary>

Écris la loss (ou l'objectif) d'**un seul exemple** avant la somme : dérive-la, puis somme. Découpe le calcul en fonctions simples, comme un graphe de calcul (M18 §1), et dérive chaque maillon séparément avant de les recoller.

</details>
<details><summary>Indice 2</summary>

Deux méthodes, à croiser. En coordonnées : les dérivées partielles une à une, en dimension 2 ou 3 (M05b §2). En matrices : écris la différentielle $dL$ en fonction de $d\mathbf{W}$, mets-la sous la forme $\operatorname{tr}(\mathbf{G}^\top d\mathbf{W})$ et lis le gradient $\mathbf{G}$ (M18 §6 et §7). Les deux doivent coïncider. Vérifie les formes ligne à ligne : un produit incompatible signale un ordre de facteurs ou une transposée à revoir.

</details>
<details><summary>Indice 3</summary>

Un gabarit d'étape : « (3.k) l'équation — *Justification* : la règle de la chaîne (M17 §3) appliquée à $f \circ g$, avec $f = \dots$ et $g = \dots$ — *Formes* : $(1, m)$ fois $(m, p)$ donne $(1, p)$ ». La liste de contrôle : (a) chaque ligne n'applique qu'une règle ; (b) chaque règle a son renvoi ; (c) chaque formule finale est vérifiée par différences finies (M05a §5) **avant** d'être rédigée : si le chiffre ne colle pas, l'erreur est entre la dernière formule vérifiée et la suivante ; (d) les points délicats sont repérés : où divises-tu, où prends-tu un logarithme, où inverses-tu une matrice, où une fonction n'est-elle pas dérivable ?

</details>

<a id="ps4"></a>

### PS.4 — Deux propriétés et un cas limite

<details><summary>Indice 1</summary>

Une propriété utile répond à une question qu'un utilisateur de l'algorithme se pose : « y a-t-il une seule solution ? », « l'itération converge-t-elle, et à quelle vitesse ? », « l'estimateur est-il sans biais ? », « que coûte un pas ? », « que se passe-t-il si je change l'échelle des données ? ».

</details>
<details><summary>Indice 2</summary>

Quelques outils, selon la propriété. Une convexité : la hessienne et ses valeurs propres (M12c §7, M19 §2), ou la convexité en une variable le long de chaque droite (M05a §1). Une convergence : écris l'erreur à l'itération $k + 1$ en fonction de celle à l'itération $k$, puis majore (M19 §3, M22 §3 et §4). Une espérance : la linéarité, puis l'espérance conditionnelle (M02b, M26 §3). Un coût : compte les opérations de chaque produit (M18 §5). Rédige comme en R4 §8 : hypothèses, étapes justifiées, conclusion ; puis relis en barrant une hypothèse à la fois : quelle étape casse ?

</details>
<details><summary>Indice 3</summary>

Pour le cas limite, prends l'hypothèse dont ta démonstration se sert le plus, et construis le plus petit cas qui la viole : une dimension, deux exemples, une matrice de rang 1, une valeur nulle, un pas trop grand. Calcule ce que devient la conclusion, puis montre-le dans la cellule « cas limite » (un nombre, ou une suite d'itérés qui grandit). Un gabarit de démonstration : « *Hypothèses* : (H1), (H3). Soit … *Étape 1* : … car … (M12c §7). … *Conclusion* : … ∎ ».

</details>

<a id="ps5"></a>

### PS.5 — Un exemple à la main

<details><summary>Indice 1</summary>

Choisis l'exemple pour que le calcul tombe juste : de petits entiers, des valeurs toutes différentes, aucun 0 ni 1 qui ferait disparaître un terme, une matrice qui n'est pas symétrique.

</details>
<details><summary>Indice 2</summary>

Calcule en fractions (R1 §3), en suivant les formules de §3 dans l'ordre et en écrivant chaque intermédiaire ; vérifie ce calcul avec SymPy (`sp.Rational`, R0 §4) avant de le comparer à ton module. Le contrôle de vraisemblance, à écrire avant : un signe attendu, une symétrie, un cas dont tu connais la réponse.

</details>
<details><summary>Indice 3</summary>

Pour un algorithme itératif, une ou deux itérations suffisent. Si une exponentielle ou un logarithme empêche les fractions, garde-les sous forme symbolique jusqu'au bout, ou choisis des données qui les simplifient, et donne la tolérance : en flottants, l'écart attendu est de l'ordre de quelques epsilons machine fois la taille des nombres en jeu (M05a §6). Reprends le même exemple dans `test_algo.py::test_hand_example`.

</details>

<a id="ps6"></a>

### PS.6 — L'implémentation avec `mymath`

<details><summary>Indice 1</summary>

Une fonction par formule finale de §3, avec le même nom et les mêmes lettres. Écris d'abord la fonction la plus simple (l'objectif, ou la passe avant), vérifie-la, puis celles qui en dépendent.

</details>
<details><summary>Indice 2</summary>

Cherche dans `mymath` les briques que ta dérivation utilise déjà : une fonction d'activation, un log-sum-exp, une décomposition, une norme, une loi stationnaire (la colonne « `mymath` utile » de la liste ; les signatures sont dans `templates/mymath_stubs/`). Pour la docstring, suis le modèle de `example_function`. Pour vectoriser, une somme sur les exemples est un produit de matrices ou une réduction le long d'un axe (M20 §2).

</details>
<details><summary>Indice 3</summary>

Un plan de module, à adapter : une fonction pour l'objectif, une pour chaque dérivée, une pour un pas de l'algorithme, une qui itère et garde l'historique (il te servira en §8). Au début de chaque fonction publique, contrôle les formes et lève `ValueError("expected … , got …")`. Lance la cellule « Contrôle du module » après chaque ajout : elle dit quelles fonctions de `mymath` tu appelles et si leur module vient de ta librairie ou de la référence.

</details>

<a id="ps7"></a>

### PS.7 — La vérification

<details><summary>Indice 1</summary>

Un test par promesse de l'article : le résultat (contre l'oracle), les dérivées (contre des différences finies), une propriété de §4, l'exemple à la main, une entrée invalide.

</details>
<details><summary>Indice 2</summary>

Règle l'oracle pour qu'il calcule exactement la même chose que toi : relis sa documentation (régularisation, normalisation de la loss, critère d'arrêt, initialisation). Si l'oracle est un optimiseur, compare au point trouvé avec une tolérance liée à son critère d'arrêt, ou compare les valeurs de l'objectif. Pour les différences finies centrées, l'erreur de troncature est en $h^2$ et l'erreur d'arrondi en $\varepsilon / h$ : choisis $h$ qui équilibre les deux (M05a §7), et une tolérance de l'ordre de l'erreur qui reste.

</details>
<details><summary>Indice 3</summary>

Un gabarit :

```python
@pytest.mark.parametrize("seed", SEEDS)
@pytest.mark.parametrize("size", SIZES, ids=[f"n={n},p={p}" for n, p in SIZES])
def test_matches_oracle(algo, size, seed):
    rng = np.random.default_rng(seed)
    data = ...                                   # drawn with rng only
    got = algo.my_function(data)
    expected = ...                               # the oracle, with its settings
    assert_close(got, expected, rtol=..., atol=..., what="my_function against <oracle>")
```

Pour la mutation, choisis l'erreur que tu as le plus failli faire en écrivant §3. Si aucun test ne l'attrape, un test manque : souvent, les tailles sont toutes égales (une transposée passe inaperçue), les données sont trop symétriques, ou une seule graine est essayée.

</details>

<a id="ps8"></a>

### PS.8 — Une expérience numérique

<details><summary>Indice 1</summary>

Pars d'une propriété de §4 qui contient un nombre (une vitesse, un seuil, un ordre de grandeur) : l'expérience mesure ce nombre.

</details>
<details><summary>Indice 2</summary>

Écris la prédiction avant de coder l'expérience. Fais varier une seule chose (un pas, un conditionnement, une taille, un hyperparamètre), garde le reste fixé, et répète sur plusieurs graines. Une erreur qui décroît vite se lit sur une échelle logarithmique.

</details>
<details><summary>Indice 3</summary>

Un gabarit : `run_experiment()` rend un dictionnaire (les valeurs du paramètre, et les mesures, une ligne par graine) ; `plot_experiment(results, ax)` trace la moyenne et une bande (le minimum et le maximum, ou un écart type de part et d'autre), puis appelle `ax.set_xlabel`, `ax.set_ylabel` (avec les unités), `ax.set_title` et `ax.legend()`. La conclusion cite la valeur lue (une pente, un seuil) et la compare à la prédiction.

</details>

<a id="ps9"></a>

### PS.9 — Rédiger l'article

<details><summary>Indice 1</summary>

Relis l'article comme quelqu'un qui ne l'a pas écrit : le résumé et l'introduction suffisent-ils à savoir ce que tu as fait, et pourquoi ?

</details>
<details><summary>Indice 2</summary>

Le plan d'un article : résumé (cinq lignes), introduction (pourquoi, quoi, plan), corps (§2 à §8), conclusion (ce qui est établi), limites (ce qui ne l'est pas), références. Numérote les équations que tu cites. Ouvre le notebook sur GitHub et sur Colab, et reprends chaque formule qui ne s'affiche pas.

</details>
<details><summary>Indice 3</summary>

Avant de rendre : « Redémarrer et tout exécuter » ; la dernière cellule donne la durée ; aucun bloc 📝 ne reste (`grep -c "📝" synthese.ipynb` donne 0) ; les sorties sont gardées ; les références sont par sections.

</details>

<a id="pse1"></a>

### PS.E1 — Présenter

<details><summary>Indice 1</summary>

Cinq minutes, c'est trois idées : le problème, l'équation clé, la preuve que ton code est juste.

</details>
<details><summary>Indice 2</summary>

Un plan type : 30 secondes pour le problème ; 2 minutes pour la dérivation (l'équation clé et le chemin qui y mène) ; 1 minute pour une propriété ; 1 minute pour la vérification (l'oracle, la mutation attrapée) ; 30 secondes pour l'expérience et la conclusion. Répète à voix haute, chronomètre en main.

</details>
<details><summary>Indice 3</summary>

Pour chaque question : la réponse en une phrase, le renvoi à l'article (« éq. (3.4) », « propriété 2 », « la figure de §8 »), puis la limite (« je ne l'ai vérifié que pour … »). Si tu ne sais pas, dis comment tu le vérifierais : un test, une expérience, une section de MML.

</details>
