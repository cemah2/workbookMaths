# Fiches des datasets (*data cards*)

Une fiche par dataset (BIBLE §10) : provenance, licence, taille, variables, limites, chapitres qui l'utilisent. Les données sont ajoutées avec le premier chapitre qui s'en sert, recopiées depuis leurs sources officielles (jamais depuis workbookIA), et la plupart des exercices utilisent des données synthétiques (`wbm.synth`, avec graine). Les fichiers versionnés se reconstruisent et se contrôlent avec `python tools/build_datasets.py` (`--check` : sans réseau) ; ils se chargent avec `wbm.datasets`.

| Dataset | Premier chapitre prévu | Fiche |
|---|---|---|
| Données synthétiques | dès R0 | *(à venir)* |
| Palmer Penguins (CC0) | M02c | *(à venir)* |
| Holmes et Verne (Project Gutenberg, domaine public) | M03 | *(à venir)* |
| La tasse de café (photographie, CC0, via scikit-image) | M12d | [tasse_cafe.md](tasse_cafe.md) |

Règle de partage (BIBLE §8) : un chapitre de maths n'utilise jamais les données d'un exercice du chapitre de workbookIA qu'il prépare.
