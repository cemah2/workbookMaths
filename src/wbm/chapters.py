"""Chapter identifiers of workbookMaths and their place in the common study order with workbookIA.

The math chapters follow workbookIA (docs/BIBLE.md §8-9):

* ``R0`` ... ``R9``: catch-up chapters, studied alongside workbookIA 0A, before workbookIA 0B;
* ``M02a``, ``M02b``, ``M02c``: studied just before chapter 2 of workbookIA; ``M12a`` ... ``M12d`` before
  chapter 12; ``MB3`` before the bonus chapter B3 (the number is the workbookIA chapter they prepare);
* ``CP0`` ... ``CP6``: mock exams, each just before the checkpoint of the same part of workbookIA;
* ``POS``: placement test (before R0); ``PS``: final synthesis project.

This module is the single source of truth for ids, order and folder names; ``tools/syllabus.py`` (session 2)
checks that the syllabus data agrees with it.
"""

from __future__ import annotations

import re

# (id, short French title, part) in study order. Part "0" to "VII" as in workbookIA; "fin" for PS.
CHAPTERS: tuple[tuple[str, str, str], ...] = (
    ("R0", "Prise en main", "0"),
    ("POS", "Test de positionnement", "0"),
    ("R1", "Nombres et calcul", "0"),
    ("R2", "Calcul littéral et équations", "0"),
    ("R3", "Fonctions", "0"),
    ("R4", "Logique, ensembles, Σ et Π", "0"),
    ("R5", "Suites", "0"),
    ("R6", "Exponentielle et logarithmes", "0"),
    ("R7", "Limites et dérivation", "0"),
    ("R8", "Probabilités de base", "0"),
    ("R9", "Géométrie du plan, vecteurs et trigonométrie", "0"),
    ("CP0", "Bilan de remise à niveau", "0"),
    ("M02a", "Intégrales et densités", "I"),
    ("M02b", "Variables aléatoires et lois usuelles", "I"),
    ("M02c", "Échantillons et estimation", "I"),
    ("M03", "Probabilités conditionnelles", "I"),
    ("M04", "Bayes, vraisemblance et loi Beta", "I"),
    ("M05a", "Dérivées, Taylor et calcul numérique", "I"),
    ("M05b", "Fonctions de plusieurs variables et gradient", "I"),
    ("M06", "Théorie de l'information", "I"),
    ("CP1", "Examen blanc de la partie I", "I"),
    ("M07", "Vecteurs et géométrie de ℝⁿ", "II"),
    ("M08", "Tests statistiques", "II"),
    ("M09a", "Matrices et systèmes linéaires", "II"),
    ("M09b", "Moindres carrés et régularisation", "II"),
    ("M10", "Séparabilité linéaire et convexité", "II"),
    ("M11", "Logique, induction et inégalités de concentration", "II"),
    ("CP2", "Examen blanc de la partie II", "II"),
    ("M12a", "Espaces vectoriels et applications linéaires", "III"),
    ("M12b", "Orthogonalité et projections", "III"),
    ("M12c", "Valeurs propres et matrices symétriques", "III"),
    ("M12d", "SVD et analyse en composantes principales", "III"),
    ("M13a", "Vraisemblance et régression logistique", "III"),
    ("M13b", "Optimisation sous contraintes et SVM", "III"),
    ("M14", "Les maths des ensembles", "III"),
    ("CP3", "Examen blanc de la partie III", "III"),
    ("M16", "Applications affines, graphes et variance d'un produit", "IV"),
    ("M17", "Jacobienne et règle de la chaîne", "IV"),
    ("M18", "Différentiation automatique et calcul matriciel", "IV"),
    ("M19", "Hessienne, conditionnement et convergence", "IV"),
    ("M20", "Tenseurs, axes et estimateurs pondérés", "IV"),
    ("CP4", "Examen blanc de la partie IV", "IV"),
    ("M21", "Convolution, matrices de Toeplitz et équivariance", "V"),
    ("M22", "Récurrences vectorielles, rayon spectral et normes de matrices", "V"),
    ("CP5", "Examen blanc de la partie V", "V"),
    ("M25a", "Gaussienne multivariée, conditionnement et divergence KL", "VI"),
    ("M25b", "Variables latentes et ELBO", "VI"),
    ("M26", "Chaînes de Markov et équation de Bellman", "VI"),
    ("M27", "Jeux et distances entre lois", "VI"),
    ("M28", "Matrice de Gram, montée sur l'entrée et lois tronquées", "VI"),
    ("CP6", "Examen blanc de la partie VI", "VI"),
    ("MB2", "Cooccurrences, PMI et embeddings", "VII"),
    ("MB3", "Rotations et attention", "VII"),
    ("MB4", "Rang faible et recherche d'information", "VII"),
    ("MB5", "Les maths de la diffusion", "VII"),
    ("MB6", "Shapley, intégrales de chemin et équité", "VII"),
    ("MB8", "Gradient de politique", "VII"),
    ("PS", "Projet de synthèse", "fin"),
)

CHAPTER_ORDER: tuple[str, ...] = tuple(cid for cid, _, _ in CHAPTERS)
TITLES: dict[str, str] = {cid: title for cid, title, _ in CHAPTERS}
PARTS: dict[str, str] = {cid: part for cid, _, part in CHAPTERS}

PART_TITLES = {
    "0": "Remise à niveau",
    "I": "Fondations",
    "II": "Concepts",
    "III": "ML classique",
    "IV": "Réseaux",
    "V": "Architectures",
    "VI": "Génératif et RL",
    "VII": "Bonus",
    "fin": "Fin",
}

# workbookIA chapters in their study order (its tools/syllabus.py ORDER, without checkpoints and the final project).
IA_CHAPTERS: tuple[str, ...] = (
    "0A", "0B", *(str(i) for i in range(1, 30)), *(f"B{i}" for i in range(1, 9)),
)

# Titles of the workbookIA chapters (copied from its docs/syllabus/data, read-only), for tables and dashboards.
IA_TITLES: dict[str, str] = {
    '0A': 'Python, notebooks et outils',
    '0B': 'Maths du lycée au ML',
    '1': 'Introduction au machine learning et au deep learning',
    '2': 'Hasard et statistiques de base',
    '3': 'Probabilités et mesure de la qualité',
    '4': 'Règle de Bayes',
    '5': 'Courbes et surfaces',
    '6': "Théorie de l'information",
    '7': 'Classification',
    '8': 'Entraînement et test',
    '9': 'Overfitting et underfitting',
    '10': 'Neurones',
    '11': 'Apprentissage et raisonnement',
    '12': 'Préparation des données',
    '13': 'Classifieurs',
    '14': 'Ensembles',
    '15': 'scikit-learn',
    '16': 'Réseaux feed-forward',
    '17': "Fonctions d'activation",
    '18': 'Rétropropagation',
    '19': 'Optimiseurs',
    '20': 'Deep learning et premiers pas en PyTorch',
    '21': 'Réseaux convolutifs (CNN)',
    '22': 'Réseaux récurrents (RNN, LSTM, GRU)',
    '23': 'PyTorch en pratique 1 : du dataset au modèle sauvegardé',
    '24': 'PyTorch en pratique 2 : améliorer, chercher, CNN et RNN',
    '25': 'Autoencodeurs et VAE',
    '26': 'Apprentissage par renforcement',
    '27': 'Réseaux antagonistes génératifs (GAN)',
    '28': 'Applications créatives',
    '29': 'Datasets et préparation du projet final',
    'B1': 'Transfer learning et modèles pré-entraînés',
    'B2': 'Tokenisation et embeddings',
    'B3': 'Attention et Transformers : un mini-GPT from scratch',
    'B4': 'LLM en pratique : Hugging Face, prompting, RAG et LoRA',
    'B5': 'Modèles de diffusion : un DDPM minimal',
    'B6': 'Explicabilité, équité et éthique',
    'B7': 'Du notebook à la production',
    'B8': 'RL moderne : DQN, gradient de politique, PPO et RLHF',
}

_MATH = re.compile(r"M(B?)(\d+)([a-d]?)")


def ia_chapter_of(chapter_id: str) -> str | None:
    """The workbookIA chapter a math chapter prepares: 'M12c' -> '12', 'MB3' -> 'B3', 'R4' -> '0B'.

    The catch-up chapters R0-R9 and CP0 prepare workbookIA 0B (they are studied during 0A).
    Mock exams, the placement test and the synthesis project return None.
    """
    if re.fullmatch(r"R\d", chapter_id) or chapter_id == "CP0":
        return "0B"
    match = _MATH.fullmatch(chapter_id)
    if not match:
        return None
    bonus, number, _ = match.groups()
    return f"B{int(number)}" if bonus else str(int(number))


def chapters_before_ia(ia_chapter: str) -> list[str]:
    """Math chapters to study just before a workbookIA chapter: '12' -> ['M12a', 'M12b', 'M12c', 'M12d'].

    '0B' -> the whole catch-up part (R0-R9); '0A' -> [] (R0-R9 are studied alongside 0A, see ``chapters_with_ia``);
    a chapter without new maths (1, 15, 23, 24, 29, B1, B7) -> [].
    """
    ia = canonical_ia(ia_chapter)
    return [cid for cid in CHAPTER_ORDER
            if ia_chapter_of(cid) == ia and cid != "CP0" and not cid.startswith("CP")]


def canonical_ia(raw: str) -> str:
    """'12' -> '12', '02' -> '2', '0b' -> '0B', 'b3' -> 'B3', 'ch18' -> '18'; ValueError if unknown."""
    text = str(raw).strip().upper()
    text = re.sub(r"^(CH|IA)[ .-]?", "", text)
    if re.fullmatch(r"0[AB]", text):
        result = text
    elif re.fullmatch(r"\d+", text):
        result = str(int(text))
    else:
        result = text
    if result not in IA_CHAPTERS:
        raise ValueError(f"chapitre de workbookIA inconnu : {raw!r} (exemples : 2, 12, 0B, B3)")
    return result


def canonical_id(raw: str) -> str:
    """Normalise a math chapter id: 'r3' -> 'R3', 'm12C' -> 'M12c', 'M2a' -> 'M02a', 'mb3' -> 'MB3', 'pos' -> 'POS'.

    ValueError for an unknown id (a bare workbookIA number such as '12' is not a math chapter id:
    see ``chapters_before_ia``).
    """
    text = str(raw).strip()
    upper = text.upper()
    if upper in {"POS", "PS"} or re.fullmatch(r"CP\d", upper) or re.fullmatch(r"R\d", upper):
        result = upper
    else:
        match = re.fullmatch(r"M(B?)0*(\d+)([A-Da-d]?)", upper)
        if not match:
            raise ValueError(f"identifiant de chapitre invalide : {raw!r} (exemples : R3, M02a, M12c, MB3, CP1)")
        bonus, number, letter = match.groups()
        result = f"MB{int(number)}" if bonus else f"M{int(number):02d}{letter.lower()}"
    if result not in CHAPTER_ORDER:
        raise ValueError(f"chapitre inconnu : {raw!r} (exemples : R3, M02a, M12c, MB3, CP1)")
    return result


def dir_prefix(chapter_id: str) -> str:
    """Folder prefix of a chapter in chapitres/: 'R3' -> 'r3', 'M12c' -> 'm12c', 'MB3' -> 'mb3'."""
    return chapter_id.lower()


def checkpoint_number(chapter_id: str) -> int | None:
    """'CP3' -> 3 (a mock exam), anything else -> None."""
    match = re.fullmatch(r"CP(\d)", chapter_id)
    return int(match.group(1)) if match else None


def common_order() -> list[tuple[str, str]]:
    """The common study order of both workbooks, as (workbook, id) pairs: ("maths", "R0"), ("IA", "0A")...

    R0, POS and R1-R9 are listed with workbookIA 0A (studied alongside it; each R chapter names the 0A sections it
    needs, see docs/PARCOURS.md); each math chapter comes just before the
    workbookIA chapter it prepares; each mock exam just before the workbookIA checkpoint of the same part.
    """
    order: list[tuple[str, str]] = []
    for cid in CHAPTER_ORDER:
        if re.fullmatch(r"R\d|POS", cid):         # R0, then the placement test, then R1 to R9
            order.append(("maths", cid))
    order += [("IA", "0A"), ("maths", "CP0"), ("IA", "0B")]
    ia_checkpoints = {"6": 1, "11": 2, "15": 3, "20": 4, "24": 5, "29": 6}
    for ia in IA_CHAPTERS[2:]:
        order += [("maths", cid) for cid in chapters_before_ia(ia)]
        order.append(("IA", ia))
        if ia in ia_checkpoints:
            n = ia_checkpoints[ia]
            order += [("maths", f"CP{n}"), ("IA", f"CP{n}")]
    order += [("maths", "PS"), ("IA", "PF")]
    return order
