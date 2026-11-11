# -*- coding: utf-8 -*-
"""Exercice 4 — l'anneau A = R × R des nombres duaux."""

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
from algebra_graphs import g_ex4  # noqa: E402

configurer_page("Exercice 4", "4️⃣")

titre_page(
    "Exercice 4 — L'anneau des nombres duaux",
    "Deux opérations sur R × R : une addition qui fait un groupe, une multiplication "
    "qui fait un anneau commutatif, mais qui cache des diviseurs de zéro.",
    "ALGÈBRE 1 · TD 3 · CP1",
)

st.markdown(
    badge("Groupe additif", "bleu")
    + badge("Anneau", "vert")
    + badge("Distributivité", "violet")
    + badge("Diviseurs de zéro", "orange"),
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
On pose $A=\mathbb{R}\times\mathbb{R}$ et, pour $(x,y),(x',y')\in A$,
$$ (x,y)+(x',y')=(x+x',y+y'), $$
$$ (x,y)*(x',y')=(xx',\;xy'+x'y). $$

Il faut :
1. montrer que $(A,+)$ est un groupe commutatif ;
2. montrer que $*$ est commutative et associative ;
3. déterminer le neutre de $*$ ;
4. montrer que $(A,+,*)$ est un anneau commutatif.
""",
    )

    col_g, col_d = st.columns(2, gap="large")
    with col_g:
        encadre(
            "vert",
            "Ce qui est donné",
            puces=[
                "L'ensemble $A=\\mathbb{R}^2$.",
                "Une addition composante par composante.",
                "Une multiplication qui ressemble à celle des nombres complexes, mais avec un signe $+$.",
            ],
        )
    with col_d:
        encadre(
            "violet",
            "Ce qu'il faut montrer",
            puces=[
                "$(A,+)$ : neutre, opposé, associativité, commutativité.",
                "$*$ : clôture, commutativité, associativité, neutre $(1,0)$.",
                "Distributivité de $*$ sur $+$.",
                "Conclusion : anneau commutatif unitaire.",
            ],
        )

    st.info(
        r"""
**L'image mentale.** $(x,y)$ se représente par la matrice
$$ \begin{pmatrix} x & y \\ 0 & x\end{pmatrix}. $$
L'addition et la multiplication de ces matrices redonnent exactement $+$ et $*$.
C'est l'anneau des **nombres duaux** $\mathbb{R}[\varepsilon]/(\varepsilon^2)$, avec $\varepsilon=(0,1)$
et $\varepsilon^2=0$.
"""
    )


# ---------------------------------------------------------------------------
# 2. Intuition
# ---------------------------------------------------------------------------
with onglets[1]:
    st.markdown("### Voir la multiplication comme un produit de matrices")
    g_ex4()
    st.markdown(
        "La matrice $\\begin{pmatrix}x&y\\\\0&x\\end{pmatrix}$ code le couple $(x,y)$. "
        "Le produit matriciel donne $(xx',xy'+x'y)$ : la loi $*$ est associative pour free, "
        "car le produit de matrices l'est."
    )


# ---------------------------------------------------------------------------
# 3. Idée
# ---------------------------------------------------------------------------
with onglets[2]:
    encadre(
        "bleu",
        "Le réflexe du prof",
        texte=r"""
Pour un anneau, on vérifie **d'abord** le groupe additif, puis la multiplication, puis la distributivité.

Ici, l'addition est composante par composante : tout se ramène à $\mathbb{R}$.
La multiplication est celle des matrices triangulaires, ce qui donne l'associativité et la distributivité gratuitement.

Le neutre de $*$ est $(1,0)$ : c'est la matrice identité.
""",
    )

    st.markdown(
        r"""
**Les indices.**

- $+$ est l'addition usuelle sur $\mathbb{R}^2$ : le neutre est $(0,0)$.
- $*$ ressemble à $(x+iy)(x'+iy')$ avec $i^2=+1$ au lieu de $-1$ ; c'est pour cela que $(0,1)^2=(0,0)$.
- Le neutre de $*$ ne peut pas être $(0,0)$ : $0$ est absorbant, pas neutre.
- Pour la distributivité, développe $a*(b+c)$ et $a*b+a*c$.
"""
    )

    encadre(
        "violet",
        "Plan de la preuve",
        puces=[
            "$(A,+)$ : groupe abélien composante par composante.",
            "$*$ : commutative, associative, neutre $(1,0)$.",
            "Distributivité à gauche et à droite.",
            "Conclusion : anneau commutatif unitaire.",
            "Bonus : $(0,1)^2=(0,0)$ montre que ce n'est pas un corps.",
        ],
    )


# ---------------------------------------------------------------------------
# 4. Preuve
# ---------------------------------------------------------------------------
with onglets[3]:
    etapes_preuve([
        {
            "titre": "(A, +) est un groupe commutatif",
            "texte": "L'addition est définie composante par composante. Le neutre est $(0,0)$ et l'opposé de $(x,y)$ est $(-x,-y)$.",
            "formules": [
                r"(x,y)+(0,0)=(x,y),",
                r"(x,y)+(-x,-y)=(0,0),",
                r"\bigl((x,y)+(x',y')\bigr)+(x'',y'')=(x+x'+x'',y+y'+y'')=(x,y)+\bigl((x',y')+(x'',y'')\bigr).",
            ],
            "pourquoi": "Chaque composante vit dans $(\\mathbb{R},+)$, qui est un groupe abélien.",
        },
        {
            "titre": "La loi * est commutative",
            "formules": [
                r"(x,y)*(x',y')=(xx',xy'+x'y)=(x'x,x'y+xy')=(x',y')*(x,y).",
            ],
            "pourquoi": "La multiplication dans $\\mathbb{R}$ est commutative, et l'addition $xy'+x'y$ est symétrique.",
        },
        {
            "titre": "La loi * est associative",
            "texte": "On calcule les deux parenthésages :",
            "formules": [
                r"\bigl((x,y)*(x',y')\bigr)*(x'',y'')=(xx',xy'+x'y)*(x'',y''),",
                r"=\bigl(xx'x'',\; xx'y''+x''(xy'+x'y)\bigr),",
                r"(x,y)*\bigl((x',y')*(x'',y'')\bigr)=(x,y)*(x'x'',x'y''+y'x''),",
                r"=\bigl(xx'x'',\; x(x'y''+y'x'')+yx'x''\bigr).",
            ],
            "pourquoi": "Les deux deuxièmes coordonnées sont égales : $xx'y''+xx''y'+x''x'y$. L'associativité est prouvée.",
        },
        {
            "titre": "Neutre de *",
            "formules": [
                r"(x,y)*(1,0)=(x\cdot1,\;x\cdot0+y\cdot1)=(x,y),",
                r"(1,0)*(x,y)=(1\cdot x,\;1\cdot y+0\cdot x)=(x,y).",
            ],
            "pourquoi": "$(1,0)$ joue le rôle de la matrice identité.",
        },
        {
            "titre": "Distributivité",
            "formules": [
                r"(x,y)*\bigl((x',y')+(x'',y'')\bigr)=(x,y)*(x'+x'',y'+y''),",
                r"=\bigl(x(x'+x''),\;x(y'+y'')+y(x'+x'')\bigr),",
                r"=(xx',xy'+yx')+(xx'',xy''+yx'')=(x,y)*(x',y')+(x,y)*(x'',y'').",
            ],
            "pourquoi": "On développe et on reconnaît la somme des deux produits. L'autre distributivité est identique car $*$ est commutative.",
        },
        {
            "titre": "Conclusion : anneau commutatif unitaire",
            "texte": "$(A,+)$ est un groupe abélien, $*$ est associative, distributive sur $+$, commutative, et admet $(1,0)$ pour neutre.",
            "pourquoi": "Ce sont exactement les axiomes d'un anneau commutatif unitaire.",
        },
        {
            "titre": "Ce n'est pas un corps",
            "formules": [
                r"(0,1)*(0,1)=(0\cdot0,\;0\cdot1+1\cdot0)=(0,0).",
            ],
            "texte": "Le couple $(0,1)$ est non nul, mais son carré est nul. C'est un diviseur de zéro.",
            "pourquoi": "Dans un corps, un produit nul force l'un des facteurs à être nul. Ici, ce n'est pas le cas.",
        },
    ])


# ---------------------------------------------------------------------------
# 5. Code
# ---------------------------------------------------------------------------
with onglets[4]:
    st.markdown("On vérifie la loi avec des matrices, puis avec **SymPy**.")

    st.code(
        r'''
import sympy as sp

a, b, c, d = sp.symbols("a b c d", real=True)

M = sp.Matrix([[a, b], [0, a]])
N = sp.Matrix([[c, d], [0, c]])

print("Produit :", sp.expand(M*N))
print("Neutre :", sp.eye(2))

# Diviseur de zéro
E = sp.Matrix([[0, 1], [0, 0]])
print("E^2 :", E*E)
''',
        language="python",
    )

    if st.button("Lancer la vérification SymPy", key="ex4_btn_sympy"):
        import sympy as sp

        a, b, c, d = sp.symbols("a b c d", real=True)
        M = sp.Matrix([[a, b], [0, a]])
        N = sp.Matrix([[c, d], [0, c]])
        st.latex(r"M(a,b)\,N(c,d)=" + sp.latex(M * N))
        st.write("Le coefficient en haut à droite est bien $ad+bc$.")
        E = sp.Matrix([[0, 1], [0, 0]])
        st.latex(r"E^2=" + sp.latex(E * E))

    st.info(
        "La matrice $E=\\begin{pmatrix}0&1\\\\0&0\\end{pmatrix}$ est non nulle et $E^2=0$. "
        "C'est exactement le diviseur de zéro $(0,1)$."
    )


# ---------------------------------------------------------------------------
# 6. Erreurs
# ---------------------------------------------------------------------------
with onglets[5]:
    encadre(
        "orange",
        "Erreur 1 — Confondre les deux neutres",
        texte=r"""
Le neutre de $+$ est $(0,0)$ ; le neutre de $*$ est $(1,0)$. Ce ne sont pas les mêmes.
""",
    )
    encadre(
        "orange",
        "Erreur 2 — Mélanger les deux lois",
        texte=r"""
$(x,y)+(x',y')=(x+x',y+y')$, mais $(x,y)*(x',y')=(xx',xy'+x'y)$.
La première est composante par composante, la seconde non.
""",
    )
    encadre(
        "orange",
        "Erreur 3 — Oublier une distributivité",
        texte=r"""
Il y a deux distributivités : à gauche et à droite. Ici, comme $*$ est commutative,
elles sont équivalentes, mais il faut le dire.
""",
    )
    encadre(
        "orange",
        "Erreur 4 — Conclure « c'est un corps »",
        texte=r"""
Un anneau commutatif n'est pas forcément un corps. Ici, $(0,1)$ n'est pas inversible
et son carré est nul : ce n'est pas un corps.
""",
    )
    encadre(
        "orange",
        "Erreur 5 — Écrire (0,1)²=(0,1)",
        texte=r"""
$(0,1)*(0,1)=(0,0)$. C'est le phénomène des nombres duaux : $\varepsilon^2=0$.
""",
    )


# ---------------------------------------------------------------------------
# 7. À retenir
# ---------------------------------------------------------------------------
with onglets[6]:
    encadre(
        "violet",
        "L'image à retenir : deux étages",
        texte=r"""
Un anneau, c'est **deux étages** : en bas, un groupe abélien pour $+$ ; au-dessus,
une multiplication associative et distributive.

Ici, l'étage additif est celui de $\mathbb{R}^2$, et l'étage multiplicatif est celui
des matrices triangulaires.
""",
    )

    encadre(
        "vert",
        "Squelette de preuve en 4 lignes",
        puces=[
            "$(A,+)$ est un groupe abélien : neutre $(0,0)$, opposé $(-x,-y)$.",
            "$*$ est commutative, associative, de neutre $(1,0)$.",
            "Distributivité : développer $a*(b+c)$.",
            "Conclusion : anneau commutatif unitaire ; $(0,1)^2=0$ montre que ce n'est pas un corps.",
        ],
    )

    st.markdown("### Trois questions pour te tester")
    mini_question(
        "Quel est le neutre de la loi ∗ ?",
        r"$(1,0)$, car $(x,y)*(1,0)=(x,y)$ et $(1,0)*(x,y)=(x,y)$.",
    )
    mini_question(
        "Pourquoi (0,1) est-il un diviseur de zéro ?",
        r"Parce que $(0,1)\neq(0,0)$ et $(0,1)*(0,1)=(0,0)$.",
    )
    mini_question(
        "Pourquoi (A, +, ∗) n'est-il pas un corps ?",
        r"Parce qu'il possède des diviseurs de zéro : un corps est intègre. "
        r"$(0,1)$ n'a pas d'inverse.",
    )

pied_page()
