# -*- coding: utf-8 -*-
"""Exercice 6 — l'anneau F(R,R) des fonctions de R dans R."""

from __future__ import annotations

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
if str(RACINE) not in sys.path:
    sys.path.insert(0, str(RACINE))

import streamlit as st  # noqa: E402

from ui import (  # noqa: E402
    badge,
    configurer_page,
    encadre,
    etapes_preuve,
    mini_question,
    pied_page,
    titre_page,
)
from algebra_graphs import g_ex6  # noqa: E402

configurer_page("Exercice 6", "6️⃣")

titre_page(
    "Exercice 6 — L'anneau F(R,R)",
    "Les fonctions de R dans R, additionnées et multipliées point par point : "
    "un anneau commutatif, mais ni intègre, ni un corps.",
    "ALGÈBRE 1 · TD 3 · CP1",
)

st.markdown(
    badge("Anneau de fonctions", "bleu")
    + badge("Commutatif", "vert")
    + badge("Non intègre", "orange")
    + badge("Pas un corps", "violet"),
    unsafe_allow_html=True,
)

onglets = st.tabs([
    "Comprendre l'énoncé",
    "Intuition",
    "Comment trouver l'idée",
    "Preuve complète pas à pas",
    "Vérifier avec du code",
    "Erreurs à éviter",
    "À retenir",
])


# ---------------------------------------------------------------------------
# 1. Comprendre
# ---------------------------------------------------------------------------
with onglets[0]:
    encadre(
        "bleu",
        "L'énoncé en clair",
        texte=r"""
On note $\mathcal{F}(\mathbb{R},\mathbb{R})$ l'ensemble de toutes les fonctions de
$\mathbb{R}$ dans $\mathbb{R}$. On les additionne et on les multiplie **point par point** :
$$ (f+g)(x)=f(x)+g(x),\qquad (f\times g)(x)=f(x)g(x). $$

Il faut :
a) montrer que $(\mathcal{F},+,\times)$ est un anneau commutatif ;
b) dire s'il est intègre ;
c) dire si c'est un corps.
""",
    )

    col_g, col_d = st.columns(2, gap="large")
    with col_g:
        encadre(
            "vert",
            "Ce qui est donné",
            puces=[
                "Toutes les fonctions, sans condition de continuité.",
                "Les opérations se font valeur par valeur.",
                "La fonction nulle $0$ et la fonction constante $1$.",
            ],
        )
    with col_d:
        encadre(
            "violet",
            "Ce qu'il faut montrer",
            puces=[
                "$(\\mathcal{F},+)$ est un groupe abélien.",
                "$\\times$ est associative, commutative, distributive.",
                "Intégrité : $fg=0\\Rightarrow f=0$ ou $g=0$ ?",
                "Corps : tout $f\\neq0$ a-t-il un inverse ?",
            ],
        )

    st.info(
        r"""
**L'image mentale.** Une fonction est un grand vecteur indexé par $x$. L'addition et
la multiplication se font **coordonnée par coordonnée**. L'anneau $\mathcal{F}(\mathbb{R},\mathbb{R})$
est donc comme $\mathbb{R}^{\mathbb{R}}$ : un produit de copies de $\mathbb{R}$.

C'est précisément ce qui crée des diviseurs de zéro : deux fonctions peuvent être non nulles
sur des zones différentes.
"""
    )


# ---------------------------------------------------------------------------
# 2. Intuition
# ---------------------------------------------------------------------------
with onglets[1]:
    st.markdown("### Deux fonctions non nulles, un produit nul")
    g_ex6()
    st.markdown(
        "$f$ vaut $x$ pour $x>0$ et $0$ ailleurs ; $g$ vaut $-x$ pour $x<0$ et $0$ ailleurs. "
        "Sur chaque $x$, au moins l'une des deux est nulle, donc $f(x)g(x)=0$ partout."
    )


# ---------------------------------------------------------------------------
# 3. Idée
# ---------------------------------------------------------------------------
with onglets[2]:
    encadre(
        "bleu",
        "Le réflexe du prof",
        texte=r"""
Pour un anneau de fonctions, tous les axiomes se vérifient **point par point** :
on se ramène à $\mathbb{R}$ pour chaque $x$.

Pour l'intégrité, cherche deux fonctions dont les supports sont **disjoints**.
Pour le corps, cherche une fonction non nulle qui s'annule quelque part : elle ne peut
pas avoir d'inverse, car il faudrait diviser par $0$ en ce point.
""",
    )

    st.markdown(
        r"""
**Les indices.**

- Le neutre de $+$ est la fonction nulle ; le neutre de $\times$ est la fonction constante $1$.
- L'opposé de $f$ est $-f$.
- Pour l'intégrité : $f(x)=\max(0,x)$ et $g(x)=\max(0,-x)$ sont non nulles, mais $fg=0$.
- Pour le corps : la fonction $h(x)=x$ est non nulle, mais $h(0)=0$, donc $1/h$ n'est pas définie en $0$.
"""
    )

    encadre(
        "violet",
        "Plan de la preuve",
        puces=[
            "Vérifier les axiomes d'anneau point par point.",
            "Exhiber $f,g$ non nulles avec $fg=0$ : pas intègre.",
            "En déduire que ce n'est pas un corps.",
        ],
    )


# ---------------------------------------------------------------------------
# 4. Preuve
# ---------------------------------------------------------------------------
with onglets[3]:
    etapes_preuve([
        {
            "titre": "L'addition est un groupe abélien",
            "texte": "Pour $f,g,h\\in\\mathcal{F}$, la fonction nulle $0$ vérifie $f+0=f$, et $-f$ est l'opposé. Les égalités se vérifient pour chaque $x$.",
            "formules": [
                r"(f+g)(x)=f(x)+g(x)=g(x)+f(x)=(g+f)(x),",
                r"\bigl((f+g)+h\bigr)(x)=f(x)+g(x)+h(x)=\bigl(f+(g+h)\bigr)(x).",
            ],
            "pourquoi": "Pour chaque $x$, on est dans $(\\mathbb{R},+)$, qui est un groupe abélien.",
        },
        {
            "titre": "La multiplication est associative et commutative",
            "formules": [
                r"\bigl((f\times g)\times h\bigr)(x)=f(x)g(x)h(x)=\bigl(f\times(g\times h)\bigr)(x),",
                r"(f\times g)(x)=f(x)g(x)=g(x)f(x)=(g\times f)(x).",
            ],
            "pourquoi": "La multiplication dans $\\mathbb{R}$ est associative et commutative.",
        },
        {
            "titre": "Neutre de la multiplication",
            "texte": "La fonction constante $\\mathbf{1}:x\\mapsto1$ vérifie $f\\times\\mathbf{1}=f$.",
            "pourquoi": "$f(x)\\cdot1=f(x)$ pour tout $x$.",
        },
        {
            "titre": "Distributivité",
            "formules": [
                r"\bigl(f\times(g+h)\bigr)(x)=f(x)\bigl(g(x)+h(x)\bigr)=f(x)g(x)+f(x)h(x).",
            ],
            "pourquoi": "C'est la distributivité dans $\\mathbb{R}$, appliquée à chaque $x$.",
        },
        {
            "titre": "Conclusion (a) : anneau commutatif",
            "texte": "$(\\mathcal{F},+)$ est un groupe abélien, $\\times$ est associative, commutative, distributive et admet $\\mathbf{1}$ pour neutre.",
            "pourquoi": "Ce sont les axiomes d'un anneau commutatif unitaire.",
        },
        {
            "titre": "(b) L'anneau n'est pas intègre",
            "texte": "Posons $f(x)=\\max(0,x)$ et $g(x)=\\max(0,-x)$.",
            "formules": [
                r"f\neq0,\qquad g\neq0,\qquad f(x)g(x)=0\ \text{pour tout }x.",
            ],
            "pourquoi": "Pour $x>0$, $g(x)=0$ ; pour $x<0$, $f(x)=0$ ; en $0$, les deux sont nulles.",
        },
        {
            "titre": "(c) Ce n'est pas un corps",
            "texte": "Un corps est intègre. Comme $\\mathcal{F}$ ne l'est pas, ce n'est pas un corps.",
            "pourquoi": "On peut aussi remarquer que $h(x)=x$ est non nulle mais n'a pas d'inverse, car $h(0)=0$.",
        },
    ])


# ---------------------------------------------------------------------------
# 5. Code
# ---------------------------------------------------------------------------
with onglets[4]:
    st.markdown("On vérifie le contre-exemple sur une grille de valeurs.")

    st.code(
        r'''
import numpy as np

x = np.linspace(-3, 3, 13)
f = np.maximum(0, x)
g = np.maximum(0, -x)

print("f :", f)
print("g :", g)
print("f*g :", f*g)
print("f est non nulle ?", np.any(f != 0))
print("g est non nulle ?", np.any(g != 0))
print("produit nul partout ?", np.all(f*g == 0))
''',
        language="python",
    )

    if st.button("Lancer la vérification", key="ex6_btn_code"):
        import numpy as np

        x = np.linspace(-3, 3, 13)
        f = np.maximum(0, x)
        g = np.maximum(0, -x)
        st.write("f(x) = max(0,x) :", f)
        st.write("g(x) = max(0,−x) :", g)
        st.write("f(x)g(x) :", f * g)
        st.success(
            f"f est non nulle : {bool(np.any(f != 0))} ; g est non nulle : "
            f"{bool(np.any(g != 0))} ; produit nul partout : {bool(np.all(f * g == 0))}."
        )

    st.info(
        "Ce contre-exemple est encore plus fort avec des fonctions continues : "
        "il n'y a pas besoin de fonctions bizarrement discontinues."
    )


# ---------------------------------------------------------------------------
# 6. Erreurs
# ---------------------------------------------------------------------------
with onglets[5]:
    encadre(
        "orange",
        "Erreur 1 — Confondre « f nulle » et « f s'annule quelque part »",
        texte=r"""
$f=0$ signifie $f(x)=0$ pour **tout** $x$. Une fonction peut s'annuler en un point
sans être la fonction nulle.
""",
    )
    encadre(
        "orange",
        "Erreur 2 — Croire qu'une fonction non nulle est inversible",
        texte=r"""
L'inverse de $f$ est $1/f$, qui n'existe que si $f(x)\neq0$ pour tout $x$.
La fonction $h(x)=x$ est non nulle, mais $h(0)=0$ : elle n'a pas d'inverse.
""",
    )
    encadre(
        "orange",
        "Erreur 3 — Exiger la continuité",
        texte=r"""
L'énoncé parle de **toutes** les fonctions. La continuité n'est pas demandée.
Le contre-exemple avec $f=\max(0,x)$ et $g=\max(0,-x)$ est même continu.
""",
    )
    encadre(
        "orange",
        "Erreur 4 — Dire « anneau donc corps »",
        texte=r"""
Un anneau commutatif n'est pas forcément un corps. Ici, les diviseurs de zéro
empêchent la structure de corps.
""",
    )
    encadre(
        "orange",
        "Erreur 5 — Oublier le neutre multiplicatif",
        texte=r"""
Le neutre de $\times$ est la fonction constante $1$, pas la fonction nulle.
La fonction nulle est absorbante : $0\times f=0$.
""",
    )


# ---------------------------------------------------------------------------
# 7. À retenir
# ---------------------------------------------------------------------------
with onglets[6]:
    encadre(
        "violet",
        "L'image à retenir : des coordonnées",
        texte=r"""
Une fonction, c'est une infinité de coordonnées $f(x)$, une pour chaque $x$.
L'anneau $\mathcal{F}(\mathbb{R},\mathbb{R})$ est donc un produit de copies de $\mathbb{R}$.

Et dans un produit, on peut être nul sur une coordonnée et non nul sur une autre :
c'est exactement ce qui crée les diviseurs de zéro.
""",
    )

    encadre(
        "vert",
        "Squelette de preuve en 3 lignes",
        puces=[
            "Tous les axiomes d'anneau se vérifient point par point.",
            "$f=\\max(0,x)$ et $g=\\max(0,-x)$ sont non nulles et $fg=0$ : pas intègre.",
            "Un corps est intègre ; donc $\\mathcal{F}$ n'est pas un corps.",
        ],
    )

    st.markdown("### Trois questions pour te tester")
    mini_question(
        "Pourquoi F(R,R) n'est-il pas intègre ?",
        r"Parce qu'il existe $f,g$ non nulles avec $fg=0$ : $f=\\max(0,x)$ et $g=\\max(0,-x)$.",
    )
    mini_question(
        "La fonction h(x)=x a-t-elle un inverse dans F(R,R) ?",
        r"Non : $1/h$ n'est pas définie en $0$. Une fonction inversible ne doit s'annuler nulle part.",
    )
    mini_question(
        "Quel est le neutre de la multiplication ?",
        r"La fonction constante $\\mathbf{1}(x)=1$, pas la fonction nulle.",
    )

pied_page()
