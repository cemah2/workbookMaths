# Fiche de données : la tasse de café (`data/images/tasse_cafe.png`)

| | |
|---|---|
| **Contenu** | une photographie d'une tasse d'espresso sur sa soucoupe, avec une cuillère, posée sur une table en bois ; aucune personne |
| **Forme** | 400 × 600 pixels, niveaux de gris sur 8 bits (0 = noir, 255 = blanc) ; niveau moyen ≈ 103,6 |
| **Chargement** | `A = wbm.datasets.load_image("tasse")` : un tableau NumPy `float64` de forme `(400, 600)` (lignes = lignes de pixels), une copie neuve à chaque appel |
| **Source** | le fichier `skimage/data/coffee.png` (couleur, 400 × 600) de la roue officielle `scikit-image==0.25.2` sur PyPI (fonction `skimage.data.coffee`) |
| **Auteur et licence** | photographie de Rachel Michetti, offerte par le Pikolo Espresso Bar ; **CC0** (« No copyright restrictions. CC0 by the photographer », documentation de `skimage.data.coffee`) : versée au domaine public, sans condition d'usage ni d'attribution (on la cite quand même) |
| **Transformation** | passage en niveaux de gris avec les poids de la recommandation UIT-R BT.601, en arithmétique entière : $L = (19595\,R + 38470\,G + 7471\,B + 32768) \gg 16$ (la formule de `convert("L")` de Pillow), puis enregistrement en PNG 8 bits ; rien d'autre (ni recadrage, ni redimensionnement) |
| **Reconstruction** | `python tools/build_datasets.py tasse` (télécharge la roue dans `data/downloads/`, non versionné, et la lit comme une archive zip sans rien en exécuter) ; `python tools/build_datasets.py --check` contrôle l'empreinte SHA-256 des pixels |
| **Empreintes** | `coffee.png` d'origine : `cc02f8ca188b167c775a7101b5d767d1e71792cf762c33d6fa15a4599b5a8de7` ; pixels gris (`uint8`, ordre C) : `3e8857c7e771b09cbf5d2e6e60d921830a1b1f097fe066f05d238ba19f87bf61` |
| **Chapitres** | M12d (🔮 M12d.31, 🔬 M12d.32, 🏆 M12d.37) : valeurs singulières d'une photo, approximation de rang faible, compression |

## Limites

- Une seule photo, assez sombre, avec de grandes zones lisses (la soucoupe, l'intérieur de la tasse) et une texture fine (le grain du bois) : les ordres de grandeur des exercices (90 % de l'énergie de l'image centrée au rang 13) valent pour **cette** image ; une autre photo donne d'autres rangs, avec la même allure (une décroissance rapide, puis une longue traîne).
- Les niveaux de gris sont des entiers arrondis (quantification sur 8 bits) : une approximation de rang plein redonne l'image aux erreurs d'arrondi près, et les dernières valeurs singulières mêlent ce bruit de quantification et la texture.
- La norme de Frobenius n'est pas la perception : deux reconstructions de même énergie peuvent sembler de qualité très différente (fiche M12d §3).
- Le passage en gris suit une convention (BT.601) parmi d'autres ; une autre pondération change légèrement tous les nombres.

## Règle de partage

workbookIA n'utilise pas cette image (vérifié : aucune image de `skimage.data` dans workbookIA). Les chapitres de maths ne s'en servent pas pour l'ACP de données tabulaires.
