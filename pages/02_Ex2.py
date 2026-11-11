# -*- coding: utf-8 -*-
"""Exercice 2 — le groupe (R², ∗)."""

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
from algebra_graphs import g_ex2  # noqa: E402

configurer_page("Exercice 2", "2️⃣")

titre_page(
    "Exercice 2 — Le groupe (R², ∗)",
    "Une loi qui mélange translation et dilatation. On va prouver les quatre axiomes, "
    "puis montrer que le groupe n'est pas commutatif.",
    "ALGÈBRE 1 · TD 3 · CP1",
)

st.markdown(
    badge("Groupe", "bleu")
    + badge("Associativité", "vert")
    + badge("Inverse", "violet")
    + badge("Non commutatif", "orange"),
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
On munit $G=\mathbb{R}^2$ de la loi
$$ (x,y)*(x',y')=\bigl(x+x',\; y e^{x'}+y' e^{-x}\bigr). $$
Il faut montrer que $(G,*)$ est un groupe, puis répondre à la question :
est-il commutatif ?
""",
    )

    col_g, col_d = st.columns(2, gap="large")
    with col_g:
        encadre(
            "vert",
            "Ce qui est donné",
            puces=[
                "L'ensemble $G=\\mathbb{R}^2$.",
                "Une loi définie par une formule avec des exponentielles.",
                "Une question en deux temps : groupe, puis groupe commutatif ?",
            ],
        )
    with col_d:
        encadre(
            "violet",
            "Ce qu'il faut montrer",
            puces=[
                "Clôture : le résultat est encore dans $\\mathbb{R}^2$.",
                "Associativité : $(a*b)*c=a*(b*c)$.",
                "Neutre : trouver $e$ tel que $e*a=a*e=a$.",
                "Inverse : trouver $(x,y)^{-1}$.",
                "Commutativité : vraie ou fausse ?",
            ],
        )

    st.info(
        r"""
**Le dessin mental.** La première coordonnée est une translation : $x+x'$.
La seconde est plus subtile : $y e^{x'}+y' e^{-x}$. Les exponentielles servent à
« transporter » $y$ et $y'$ dans le bon repère avant de les additionner.

Le neutre probable est $(0,0)$ : les exponentielles valent alors $1$, et le second
terme devient $y+y'$… mais attention, la formule n'est pas symétrique en $x$ et $x'$.
"""
    )


# ---------------------------------------------------------------------------
# 2. Intuition
# ---------------------------------------------------------------------------
with onglets[1]:
    st.markdown("### Composer deux éléments de G")
    g_ex2()
    st.markdown(
        "La transformation associée à $(x,y)$ déforme une grille : elle translate, "
        "puis dilate. En échangeant les deux couples, on ne obtient pas la même image."
    )


# ---------------------------------------------------------------------------
# 3. Idée
# ---------------------------------------------------------------------------
with onglets[2]:
    encadre(
        "bleu",
        "Le réflexe du prof",
        texte=r"""
Pour montrer qu'une loi est un groupe, on suit toujours le même ordre :

1. **Clôture** : le résultat est dans $G$. Ici, c'est immédiat.
2. **Associativité** : on calcule $(a*b)*c$ et $a*(b*c)$ avec des lettres.
3. **Neutre** : on le devine, puis on vérifie les deux côtés.
4. **Inverse** : on résout $a*a^{-1}=e$, puis on vérifie l'autre côté.

Pour la commutativité, on ne cherche pas une preuve : on cherche **un contre-exemple**.
""",
    )

    st.markdown(
        r"""
**Les indices.**

- $(0,0)$ est le candidat naturel pour le neutre : $e^0=1$.
- Pour l'inverse, la première coordonnée doit être $-x$ pour annuler $x+u$.
- La seconde coordonnée se résout ensuite : $y e^{u}+v e^{-x}=0$.
- Pour la non-commutativité, prends deux couples très simples, par exemple $(1,0)$ et $(0,1)$.
"""
    )

    encadre(
        "violet",
        "Plan de la preuve",
        puces=[
            "Clôture : somme de réels et exponentielles de réels.",
            "Associativité : développer les deux parenthésages et comparer les trois termes.",
            "Neutre $(0,0)$, inverse $(-x,-y)$.",
            "Contre-exemple de commutativité : $(1,0)*(0,1)\\neq(0,1)*(1,0)$.",
        ],
    )


# ---------------------------------------------------------------------------
# 4. Preuve
# ---------------------------------------------------------------------------
with onglets[3]:
    etapes_preuve([
        {
            "titre": "Clôture",
            "texte": "Si $x,y,x',y'\\in\\mathbb{R}$, alors $x+x'\\in\\mathbb{R}$ et $y e^{x'}+y' e^{-x}\\in\\mathbb{R}$. Donc $(x,y)*(x',y')\\in G$.",
            "pourquoi": "$\\mathbb{R}$ est stable par addition et par multiplication par une exponentielle réelle.",
        },
        {
            "titre": "Associativité",
            "texte": "Posons $a=(x,y)$, $b=(x',y')$, $c=(x'',y'')$. D'un côté :",
            "formules": [
                r"a*b=\bigl(x+x',\; y e^{x'}+y' e^{-x}\bigr),",
                r"(a*b)*c=\Bigl(x+x'+x'',\; (y e^{x'}+y' e^{-x})e^{x''}+y''e^{-(x+x')}\Bigr),",
                r"=\Bigl(x+x'+x'',\; y e^{x'+x''}+y' e^{x''-x}+y''e^{-x-x'}\Bigr).",
            ],
            "pourquoi": "On développe et on utilise $e^a e^b=e^{a+b}$.",
        },
        {
            "titre": "Associativité, autre parenthésage",
            "formules": [
                r"b*c=\bigl(x'+x'',\; y' e^{x''}+y'' e^{-x'}\bigr),",
                r"a*(b*c)=\Bigl(x+x'+x'',\; y e^{x'+x''}+(y'e^{x''}+y''e^{-x'})e^{-x}\Bigr),",
                r"=\Bigl(x+x'+x'',\; y e^{x'+x''}+y'e^{x''-x}+y''e^{-x'-x}\Bigr).",
            ],
            "pourquoi": "Les deux résultats sont identiques : l'associativité est prouvée.",
        },
        {
            "titre": "Neutre",
            "formules": [
                r"(x,y)*(0,0)=\bigl(x+0,\; y e^{0}+0\cdot e^{-x}\bigr)=(x,y),",
                r"(0,0)*(x,y)=\bigl(0+x,\; 0\cdot e^{x}+y e^{0}\bigr)=(x,y).",
            ],
            "pourquoi": "$e^0=1$ et multiplier par $0$ annule le terme correspondant.",
        },
        {
            "titre": "Inverse",
            "texte": "Cherchons $(u,v)$ tel que $(x,y)*(u,v)=(0,0)$. La première coordonnée impose $u=-x$. La seconde donne :",
            "formules": [
                r"y e^{u}+v e^{-x}=0\ \Longrightarrow\ y e^{-x}+v e^{-x}=0\ \Longrightarrow\ v=-y.",
                r"(x,y)*(-x,-y)=\bigl(0,\; y e^{-x}-y e^{-x}\bigr)=(0,0).",
            ],
            "pourquoi": "On vérifie aussi $(-x,-y)*(x,y)=(0,0)$ : c'est le même calcul avec les rôles échangés.",
        },
        {
            "titre": "Le groupe est non commutatif",
            "formules": [
                r"(1,0)*(0,1)=\bigl(1,\; 0\cdot e^{0}+1\cdot e^{-1}\bigr)=(1,e^{-1}),",
                r"(0,1)*(1,0)=\bigl(1,\; 1\cdot e^{1}+0\cdot e^{0}\bigr)=(1,e).",
            ],
            "texte": "Comme $e\\neq e^{-1}$, les deux résultats diffèrent.",
            "pourquoi": "Un seul couple qui ne commute pas suffit pour nier la commutativité.",
        },
    ])

    st.success(
        "Bilan : $(G,*)$ est un groupe, mais il n'est pas abélien. "
        "Le neutre est $(0,0)$, l'inverse de $(x,y)$ est $(-x,-y)$."
    )


# ---------------------------------------------------------------------------
# 5. Code
# ---------------------------------------------------------------------------
with onglets[4]:
    st.markdown("On vérifie l'associativité et l'inverse avec **SymPy**.")

    st.code(
        r'''
import sympy as sp

x, y, xp, yp, xpp, ypp = sp.symbols("x y xp yp xpp ypp", real=True)

def loi(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1 + x2, y1*sp.exp(x2) + y2*sp.exp(-x1))

a = (x, y)
b = (xp, yp)
c = (xpp, ypp)

gauche = loi(loi(a, b), c)
droite = loi(a, loi(b, c))
print("Associativité :", [sp.simplify(g - d) for g, d in zip(gauche, droite)])

print("Neutre :", loi(a, (0, 0)), loi((0, 0), a))
print("Inverse :", loi(a, (-x, -y)), loi((-x, -y), a))
''',
        language="python",
    )

    if st.button("Lancer la vérification SymPy", key="ex2_btn_sympy"):
        import sympy as sp

        x, y, xp, yp, xpp, ypp = sp.symbols("x y xp yp xpp ypp", real=True)

        def loi(a, b):
            x1, y1 = a
            x2, y2 = b
            return (x1 + x2, y1 * sp.exp(x2) + y2 * sp.exp(-x1))

        a, b, c = (x, y), (xp, yp), (xpp, ypp)
        gauche = loi(loi(a, b), c)
        droite = loi(a, loi(b, c))
        st.write("Associativité : ", [sp.simplify(g - d) for g, d in zip(gauche, droite)])
        st.write("Neutre : ", loi(a, (0, 0)), " et ", loi((0, 0), a))
        st.write("Inverse : ", loi(a, (-x, -y)), " et ", loi((-x, -y), a))
        st.write("Commutateur : ", sp.simplify(loi((1, 0), (0, 1))[1] - loi((0, 1), (1, 0))[1]))

    st.info(
        "Le commutateur vaut $e^{-1}-e\\neq0$ : c'est la preuve numérique de la non-commutativité."
    )


# ---------------------------------------------------------------------------
# 6. Erreurs
# ---------------------------------------------------------------------------
with onglets[5]:
    encadre(
        "orange",
        "Erreur 1 — Se tromper de signe dans l'exponentielle",
        texte=r"""
La loi est $y e^{x'}+y' e^{-x}$, pas $y e^{x}+y' e^{-x'}$. Les rôles de $x$ et $x'$
sont croisés : c'est précisément ce qui rend la loi non commutative.
""",
    )
    encadre(
        "orange",
        "Erreur 2 — Proposer (−x, y) comme inverse",
        texte=r"""
Il faut annuler la seconde coordonnée : $y e^{-x}+v e^{-x}=0$ donne $v=-y$.
L'inverse est $(-x,-y)$, pas $(-x,y)$.
""",
    )
    encadre(
        "orange",
        "Erreur 3 — Vérifier la commutativité avec un couple qui commute",
        texte=r"""
Si tu prends $(0,0)$ et $(1,0)$, tout commute. Il faut choisir un couple qui révèle
la dissymétrie : $(1,0)$ et $(0,1)$ fonctionnent.
""",
    )
    encadre(
        "orange",
        "Erreur 4 — Oublier de vérifier l'autre côté pour l'inverse",
        texte=r"""
Dans un groupe, il faut $a*a^{-1}=e$ **et** $a^{-1}*a=e$. Si la loi n'est pas
commutative, l'un ne donne pas automatiquement l'autre.
""",
    )
    encadre(
        "orange",
        "Erreur 5 — Écrire « c'est évident » pour l'associativité",
        texte=r"""
L'associativité n'est jamais évidente quand la formule mélange $x$ et $x'$.
Il faut développer les deux parenthésages et comparer.
""",
    )


# ---------------------------------------------------------------------------
# 7. À retenir
# ---------------------------------------------------------------------------
with onglets[6]:
    encadre(
        "violet",
        "L'image à retenir",
        texte=r"""
La loi transporte $y$ et $y'$ dans des repères différents avant de les additionner.
C'est une **translation** sur la première coordonnée et une **dilatation croisée**
sur la seconde. D'où la non-commutativité.
""",
    )

    encadre(
        "vert",
        "Squelette de preuve en 4 lignes",
        puces=[
            "Clôture : somme et exponentielles de réels.",
            "Associativité : développer $(a*b)*c$ et $a*(b*c)$ ; les trois termes coïncident.",
            "Neutre $(0,0)$ ; inverse $(-x,-y)$.",
            "Non commutatif : $(1,0)*(0,1)=(1,e^{-1})\\neq(1,e)=(0,1)*(1,0)$.",
        ],
    )

    st.markdown("### Trois questions pour te tester")
    mini_question(
        "Quel est le neutre de (G, ∗) ?",
        r"$(0,0)$, car $e^0=1$ et les termes en $0$ disparaissent.",
    )
    mini_question(
        "Quel est l'inverse de (x, y) ?",
        r"$(-x,-y)$. La première coordonnée donne $u=-x$, puis la seconde donne $v=-y$.",
    )
    mini_question(
        "Pourquoi (G, ∗) n'est-il pas commutatif ?",
        r"$(1,0)*(0,1)=(1,e^{-1})$ alors que $(0,1)*(1,0)=(1,e)$, et $e\neq e^{-1}$.",
    )

pied_page()
