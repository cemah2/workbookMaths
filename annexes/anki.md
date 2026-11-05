# Réviser avec Anki : importer les flashcards de workbookMaths

Chaque chapitre publié a son fichier `flashcards.csv` (15 à 30 cartes). L'outil `tools/export_flashcards.py` les rassemble en **un deck « workbookMaths »**, distinct de celui de workbookIA, rangé en **sous-paquets** par partie et par chapitre, dans l'ordre d'étude :

```
workbookMaths
├── Partie 0
│   ├── 01 R0 Prise en main
│   ├── 02 R1 Nombres et calcul
│   └── …
├── Partie I
│   ├── 12 M02a Intégrales et densités
│   └── …
└── Partie VII
    └── 56 MB8 Gradient de politique
```

Le numéro en tête est le rang du chapitre dans l'ordre d'étude : Anki range les paquets par ordre alphabétique, et la liste suit ainsi l'ordre du workbook. Chaque carte garde son tag de chapitre (`mwb::m12c::valeur_propre`) et reçoit le tag de sa partie (`mwb::partie_III::m12c`).

## 1. Fabriquer le fichier à importer

| Commande | Fichier créé dans `exports/` | Quand ? |
|---|---|---|
| `python tools/export_flashcards.py --chapter M12c` | `mwb_anki_m12c_….csv` : les cartes d'un chapitre | à la fin de chaque chapitre |
| `python tools/export_flashcards.py` | `mwb_anki.csv` : toutes les cartes | pour rattraper plusieurs chapitres |
| `python tools/export_flashcards.py --apkg` | `mwb_anki.apkg` : un paquet Anki | si tu préfères un double-clic (demande `pip install genanki`) |

Sur Colab : `!python /content/drive/MyDrive/workbookMaths/tools/export_flashcards.py --chapter M12c`, puis télécharge le fichier depuis `Mon Drive/workbookMaths/exports/`.

## 2. Importer

Comme pour workbookIA (son `annexes/anki.md`, sections 2 et 3) : **Fichier > Importer**, type de note « Basique », les premières lignes du fichier règlent séparateur, HTML, tags et paquet à ta place. Les formules s'affichent avec MathJax, intégré à Anki. Choisis une seule méthode (CSV ou `.apkg`) pour éviter les doublons.

## 3. Deux decks, une routine

Révise les deux decks chaque jour (10 minutes suffisent). Suspends les sous-paquets des chapitres pas encore étudiés : dans **Parcourir**, sélectionne le sous-paquet, puis **Cartes > Suspendre**.
