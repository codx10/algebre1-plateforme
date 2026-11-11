# -*- coding: utf-8 -*-
"""Exercice 3 — le groupe affine H et son sous-groupe."""

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
from algebra_graphs import g_affine  # noqa: E402

configurer_page("Exercice 3", "3️⃣")

titre_page(
    "Exercice 3 — Le groupe affine H",
    "Composer des transformations x t + y : le modèle concret d'un groupe non commutatif, "
    "avec un sous-groupe naturel.",
    "ALGÈBRE 1 · TD 3 · CP1",
)

st.markdown(
    badge("Groupe non commutatif", "bleu")
    + badge("Transformations affines", "vert")
    + badge("Sous-groupe", "violet"),
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
On pose $H=\mathbb{R}^*\times\mathbb{R}$ et, pour $(x,y),(x',y')\in H$,
$$ (x,y)*(x',y')=(xx',\; xy'+y). $$
Il faut montrer que $(H,*)$ est un groupe **non commutatif**, puis que
$$ S=]0,+\infty[\times\mathbb{R} $$
est un sous-groupe de $(H,*)$.
""",
    )

    col_g, col_d = st.columns(2, gap="large")
    with col_g:
        encadre(
            "vert",
            "Ce qui est donné",
            puces=[
                "$H=\\mathbb{R}^*\\times\\mathbb{R}$ : la première coordonnée est non nulle.",
                "Une loi qui ressemble à la composition de $t\\mapsto xt+y$.",
                "Deux questions : groupe, puis sous-groupe $S$.",
            ],
        )
    with col_d:
        encadre(
            "violet",
            "Ce qu'il faut montrer",
            puces=[
                "Clôture : $xx'\\neq0$.",
                "Associativité et neutre $(1,0)$.",
                "Inverse de $(x,y)$.",
                "Un contre-exemple de commutativité.",
                "Les trois conditions de sous-groupe pour $S$.",
            ],
        )

    st.info(
        r"""
**L'image mentale.** Un couple $(x,y)$ représente la transformation
$$ T_{x,y}:t\longmapsto xt+y. $$
Composer $T_{x,y}$ après $T_{x',y'}$ donne
$$ T_{x,y}\circ T_{x',y'}(t)=x(x't+y')+y=xx't+xy'+y, $$
c'est-à-dire exactement $(xx',xy'+y)$. La loi de l'énoncé est donc la composition
des transformations affines.
"""
    )


# ---------------------------------------------------------------------------
# 2. Intuition
# ---------------------------------------------------------------------------
with onglets[1]:
    st.markdown("### Voir la transformation sur une grille")
    g_affine()
    st.markdown(
        "La transformation $(X,Y)\\mapsto(xX+y,xY+y)$ est une homothétie de rapport $x$ "
        "suivie d'une translation de $y$. En composant deux transformations, on retrouve "
        "la loi $(x,y)*(x',y')=(xx',xy'+y)$."
    )


# ---------------------------------------------------------------------------
# 3. Idée
# ---------------------------------------------------------------------------
with onglets[2]:
    encadre(
        "bleu",
        "Le réflexe du prof",
        texte=r"""
Quand une loi ressemble à $(xx',xy'+y)$, pense **transformations affines**. Cela donne
immédiatement le neutre et l'inverse :

- neutre : l'identité $t\mapsto t$, donc $(1,0)$ ;
- inverse : la transformation qui défait $t\mapsto xt+y$, donc $t\mapsto \frac1x t-\frac yx$, soit $(1/x,-y/x)$.

Pour le sous-groupe $S$, il suffit de vérifier : non vide, stable par la loi, stable par inverse.
""",
    )

    st.markdown(
        r"""
**Les indices.**

- $x$ et $x'$ sont non nuls, donc $xx'$ est non nul : la clôture est immédiate.
- Le neutre ne peut pas être $(0,0)$ : $0\notin\mathbb{R}^*$.
- L'inverse doit avoir pour première coordonnée $1/x$.
- $S$ impose $x>0$ : il faut vérifier que $1/x>0$ aussi.
"""
    )

    encadre(
        "violet",
        "Plan de la preuve",
        puces=[
            "Clôture, associativité, neutre $(1,0)$, inverse $(1/x,-y/x)$.",
            "Contre-exemple de commutativité avec $(2,0)$ et $(1,1)$.",
            "$S$ : non vide, stable par $*$, stable par inverse.",
        ],
    )


# ---------------------------------------------------------------------------
# 4. Preuve
# ---------------------------------------------------------------------------
with onglets[3]:
    etapes_preuve([
        {
            "titre": "Clôture",
            "texte": "Si $x,x'\\in\\mathbb{R}^*$, alors $xx'\\neq0$. La seconde coordonnée $xy'+y$ est un réel quelconque. Donc $(x,y)*(x',y')\\in H$.",
            "pourquoi": "Le produit de deux réels non nuls est non nul.",
        },
        {
            "titre": "Associativité",
            "formules": [
                r"\bigl((x,y)*(x',y')\bigr)*(x'',y'')=(xx',xy'+y)*(x'',y''),",
                r"=\bigl(xx'x'',\; xx'y''+xy'+y\bigr).",
                r"(x,y)*\bigl((x',y')*(x'',y'')\bigr)=(x,y)*(x'x'',x'y''+y'),",
                r"=\bigl(xx'x'',\; x(x'y''+y')+y\bigr)=\bigl(xx'x'',\; xx'y''+xy'+y\bigr).",
            ],
            "pourquoi": "Les deux parenthésages donnent le même couple : la loi est associative.",
        },
        {
            "titre": "Neutre",
            "formules": [
                r"(x,y)*(1,0)=(x\cdot1,\; x\cdot0+y)=(x,y),",
                r"(1,0)*(x,y)=(1\cdot x,\; 1\cdot y+0)=(x,y).",
            ],
            "pourquoi": "$1$ ne change pas $x$ et $0$ annule la translation.",
        },
        {
            "titre": "Inverse",
            "texte": "On cherche $(u,v)$ tel que $(x,y)*(u,v)=(1,0)$.",
            "formules": [
                r"xu=1\ \Longrightarrow\ u=\frac1x,",
                r"xv+y=0\ \Longrightarrow\ v=-\frac yx.",
                r"(x,y)*\left(\frac1x,-\frac yx\right)=\left(1,\;x\left(-\frac yx\right)+y\right)=(1,0).",
            ],
            "pourquoi": "On vérifie aussi l'autre côté : $\\left(\\frac1x,-\\frac yx\\right)*(x,y)=(1,0)$.",
        },
        {
            "titre": "Non-commutativité",
            "formules": [
                r"(2,0)*(1,1)=(2,\;2\cdot1+0)=(2,2),",
                r"(1,1)*(2,0)=(2,\;1\cdot0+1)=(2,1).",
            ],
            "pourquoi": "$(2,2)\\neq(2,1)$ : le groupe n'est pas abélien.",
        },
        {
            "titre": "S est non vide",
            "texte": "$(1,0)\\in S$ car $1>0$ et $0\\in\\mathbb{R}$.",
            "pourquoi": "Un sous-groupe doit au moins contenir un élément.",
        },
        {
            "titre": "S est stable par la loi",
            "texte": "Si $x>0$ et $x'>0$, alors $xx'>0$, et $xy'+y\\in\\mathbb{R}$. Donc $(x,y)*(x',y')\\in S$.",
            "pourquoi": "Le produit de deux réels strictement positifs est strictement positif.",
        },
        {
            "titre": "S est stable par inverse",
            "texte": "Si $x>0$, alors $1/x>0$, et $-y/x\\in\\mathbb{R}$. Donc $(x,y)^{-1}\\in S$.",
            "pourquoi": "L'inverse de $(x,y)$ est $(1/x,-y/x)$ ; la première coordonnée reste strictement positive.",
        },
    ])

    st.success(
        "Conclusion : $(H,*)$ est un groupe non commutatif, et $S=]0,+\\infty[\\times\\mathbb{R}$ "
        "est un sous-groupe de $H$."
    )


# ---------------------------------------------------------------------------
# 5. Code
# ---------------------------------------------------------------------------
with onglets[4]:
    st.markdown("On représente chaque couple par la fonction affine $t\\mapsto xt+y$.")

    st.code(
        r'''
import sympy as sp

t = sp.symbols("t", real=True)

def transformation(couple):
    x, y = couple
    return x*t + y

def compose(a, b):
    # a après b : t -> a(b(t))
    return sp.expand(transformation(a).subs(t, transformation(b)))

# Vérification de la loi
x, y, xp, yp = sp.symbols("x y xp yp", real=True)
a = (x, y)
b = (xp, yp)
print("Composition :", compose(a, b))
print("Loi attendue :", x*xp*t + x*yp + y)

# Inverse
print("a * (1/x, -y/x) :", compose(a, (1/x, -y/x)))
print("(1/x, -y/x) * a :", compose((1/x, -y/x), a))
''',
        language="python",
    )

    if st.button("Lancer la vérification SymPy", key="ex3_btn_sympy"):
        import sympy as sp

        t = sp.symbols("t", real=True)
        x, y, xp, yp = sp.symbols("x y xp yp", real=True)

        def trans(couple):
            xx, yy = couple
            return xx * t + yy

        def compose(a, b):
            return sp.expand(trans(a).subs(t, trans(b)))

        st.latex(r"T_{x,y}\circ T_{x',y'}(t)=" + sp.latex(compose((x, y), (xp, yp))))
        st.latex(r"T_{x,y}\circ T_{1/x,-y/x}(t)=" + sp.latex(sp.simplify(compose((x, y), (1 / x, -y / x)))))
        st.latex(r"T_{1/x,-y/x}\circ T_{x,y}(t)=" + sp.latex(sp.simplify(compose((1 / x, -y / x), (x, y)))))

    st.info(
        "La composition redonne $xx't+xy'+y$ : le couple $(xx',xy'+y)$ n'est rien d'autre "
        "que la transformation composée."
    )


# ---------------------------------------------------------------------------
# 6. Erreurs
# ---------------------------------------------------------------------------
with onglets[5]:
    encadre(
        "orange",
        "Erreur 1 — Prendre (0, 0) comme neutre",
        texte=r"""
$(0,0)\notin H$ car $0\notin\mathbb{R}^*$. Le neutre est $(1,0)$, qui correspond à
l'identité $t\mapsto t$.
""",
    )
    encadre(
        "orange",
        "Erreur 2 — Se tromper de signe dans l'inverse",
        texte=r"""
L'inverse est $(1/x,-y/x)$, pas $(1/x,y/x)$. Vérifie toujours :
$x\cdot(-y/x)+y=0$.
""",
    )
    encadre(
        "orange",
        "Erreur 3 — Prendre x ≥ 0 pour le sous-groupe",
        texte=r"""
$S$ est $]0,+\infty[\times\mathbb{R}$ : $x$ doit être **strictement** positif, sinon
$1/x$ n'existe pas. $x=0$ est exclu.
""",
    )
    encadre(
        "orange",
        "Erreur 4 — Croire que la loi est commutative",
        texte=r"""
$(2,0)*(1,1)=(2,2)$ mais $(1,1)*(2,0)=(2,1)$. La multiplication des premières
coordonnées est commutative, mais la translation ne l'est pas.
""",
    )
    encadre(
        "orange",
        "Erreur 5 — Oublier la stabilité par inverse pour S",
        texte=r"""
Un sous-groupe ne se contente pas d'être stable par la loi : il doit aussi contenir
l'inverse de chacun de ses éléments.
""",
    )


# ---------------------------------------------------------------------------
# 7. À retenir
# ---------------------------------------------------------------------------
with onglets[6]:
    encadre(
        "violet",
        "L'image à retenir : x t + y",
        texte=r"""
Chaque couple $(x,y)$ est une transformation de la droite : on multiplie par $x$,
puis on translate de $y$. La loi de $H$ est simplement la **composition** de ces
transformations. C'est le groupe affine de la droite.
""",
    )

    encadre(
        "vert",
        "Squelette de preuve en 4 lignes",
        puces=[
            "Clôture : $x,x'\\neq0\\Rightarrow xx'\\neq0$.",
            "Associativité : développer les deux parenthésages ; ils coïncident.",
            "Neutre $(1,0)$ ; inverse $(1/x,-y/x)$.",
            "$S$ : non vide, stable par $*$ et par inverse ; contre-exemple $(2,0)*(1,1)\\neq(1,1)*(2,0)$.",
        ],
    )

    st.markdown("### Trois questions pour te tester")
    mini_question(
        "Quelle transformation représente le couple (x, y) ?",
        r"$T_{x,y}(t)=xt+y$. C'est une homothétie de rapport $x$ suivie d'une translation de $y$.",
    )
    mini_question(
        "Pourquoi H n'est-il pas commutatif ?",
        r"$(2,0)*(1,1)=(2,2)$ et $(1,1)*(2,0)=(2,1)$. Les translations ne commutent pas "
        r"avec les homothéties.",
    )
    mini_question(
        "Pourquoi S est-il un sous-groupe ?",
        r"$S$ contient $(1,0)$, il est stable par produit (produit de deux réels $>0$) et "
        r"par inverse ($1/x>0$). C'est la caractérisation d'un sous-groupe.",
    )

pied_page()
