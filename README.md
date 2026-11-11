# Plateforme d'apprentissage — Algèbre 1 (CP1 ENSA Marrakech)

Application **Streamlit** pour travailler le **TD 3 : Vocabulaire des structures algébriques**
(Algèbre 1, CP1, ENSA Marrakech, Pr. Laila Taourirte).

## Lancer l'application

```bash
pip install -r requirements.txt
streamlit run Home.py
```

Python 3.10 ou plus récent.

## Structure

```text
Plateforme_Algebre1/
├── Home.py                  # accueil, méthode, feuille de route, progression
├── requirements.txt
├── ui.py                    # styles, encadrés colorés, composants communs
├── algebra_graphs.py        # tables de Cayley et visualisations Plotly
├── .streamlit/
│   └── config.toml          # thème sombre
└── pages/
    ├── 00_Toolbox.py        # 15 notions du TD
    ├── 01_Ex1.py            # deux lois sur R
    ├── 02_Ex2.py            # le groupe (R², ∗)
    ├── 03_Ex3.py            # le groupe affine H
    ├── 04_Ex4.py            # l'anneau des nombres duaux
    ├── 05_Ex5.py            # le corps Q(i)
    ├── 06_Ex6.py            # l'anneau F(R,R)
    ├── 07_Ex7.py            # les entiers de Gauss Z[i]
    ├── 08_Ex8.py            # le corps Q[i]
    ├── 09_Quiz_Flashcards.py
    └── 10_Cheat_Sheet.py
```

Chaque page d'exercice contient 7 onglets :

1. Comprendre l'énoncé
2. Intuition
3. Comment trouver l'idée
4. Preuve complète pas à pas
5. Vérifier avec du code
6. Erreurs à éviter
7. À retenir

## Remarque sur l'exercice 1

Le PDF écrit $\mathbb{R}^{+*}$ mais demande de montrer que $0$ est neutre. Comme
$0\notin\mathbb{R}^{+*}$, l'énoncé est incohérent. L'application interprète l'ensemble
comme $\mathbb{R}^+=[0,+\infty[$ et explique cette correction dans la page de l'exercice 1.

## Vérifications

- Toutes les pages ont été testées avec `streamlit.testing.v1.AppTest`.
- Les calculs symboliques sont vérifiés avec SymPy dans les onglets « Vérifier avec du code ».
- Les 15 notions et les branches alternatives des graphiques ont été testées.
