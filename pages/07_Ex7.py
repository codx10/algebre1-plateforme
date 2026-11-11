# -*- coding: utf-8 -*-
"""Exercice 7 — l'anneau Z[i] des entiers de Gauss."""

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
from algebra_graphs import g_ex7  # noqa: E402

configurer_page("Exercice 7", "7️⃣")

titre_page(
    "Exercice 7 — Les entiers de Gauss Z[i]",
    "Un réseau de points dans le plan complexe : un anneau commutatif, "
    "mais pas un corps. La norme explique tout.",
    "ALGÈBRE 1 · TD 3 · CP1",
)

st.markdown(
    badge("Sous-anneau de C", "bleu")
    + badge("Anneau commutatif", "vert")
    + badge("Unités", "violet")
    + badge("Pas un corps", "orange"),
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
On pose
$$ \mathbb{Z}[i]=\{a+ib: a,b\in\mathbb{Z}\}. $$
a) Montrer que $(\mathbb{Z}[i],+,\times)$ est un anneau commutatif ; on l'appelle
l'anneau des **entiers de Gauss**.
b) Est-ce un corps ?
""",
    )

    col_g, col_d = st.columns(2, gap="large")
    with col_g:
        encadre(
            "vert",
            "Ce qui est donné",
            puces=[
                "Les coordonnées sont des **entiers**.",
                "Les opérations sont celles de $\\mathbb{C}$.",
                "Il faut montrer que $\\mathbb{Z}[i]$ est un sous-anneau de $\\mathbb{C}$.",
            ],
        )
    with col_d:
        encadre(
            "violet",
            "Ce qu'il faut montrer",
            puces=[
                "$0,1\\in\\mathbb{Z}[i]$.",
                "Stabilité par $+$, par opposé et par $\\times$.",
                "Les axiomes d'anneau sont hérités de $\\mathbb{C}$.",
                "Un élément non nul sans inverse : $2$.",
            ],
        )

    st.info(
        r"""
**L'image mentale.** $\mathbb{Z}[i]$ est un **réseau** : les points à coordonnées entières
du plan complexe. On peut les additionner et les multiplier, mais on ne peut pas toujours
diviser : $1/2$ n'est pas dans le réseau.
"""
    )


# ---------------------------------------------------------------------------
# 2. Intuition
# ---------------------------------------------------------------------------
with onglets[1]:
    st.markdown("### Le réseau des entiers de Gauss")
    g_ex7()
    st.markdown(
        "La norme $N(a+ib)=a^2+b^2$ mesure le carré de la distance à l'origine. "
        "Un élément est inversible dans $\\mathbb{Z}[i]$ seulement si sa norme vaut $1$ : "
        "ce sont les unités $\\pm1,\\pm i$."
    )


# ---------------------------------------------------------------------------
# 3. Idée
# ---------------------------------------------------------------------------
with onglets[2]:
    encadre(
        "bleu",
        "Le réflexe du prof",
        texte=r"""
$\mathbb{Z}[i]$ est contenu dans $\mathbb{C}$, qui est un corps. Pour montrer que c'est
un anneau, il suffit de montrer que c'est un **sous-anneau** :
$0,1$ dedans, stable par $+$, par opposé et par $\times$.

Pour montrer que ce n'est **pas** un corps, il suffit d'un élément non nul sans inverse.
Le plus simple est $2$ : si $2(a+ib)=1$, alors $2a=1$, impossible avec $a\in\mathbb{Z}$.
""",
    )

    st.markdown(
        r"""
**Les indices.**

- Le produit $(a+ib)(c+id)=(ac-bd)+i(ad+bc)$ reste à coordonnées entières.
- L'inverse dans $\mathbb{C}$ est $(a-ib)/(a^2+b^2)$ ; il n'est pas toujours à coordonnées entières.
- $N(z)=z\overline z=a^2+b^2$ est un entier.
- Les unités sont les éléments de norme $1$.
"""
    )

    encadre(
        "violet",
        "Plan de la preuve",
        puces=[
            "Sous-anneau : $0,1$, stabilité par $+$, $-$, $\\times$.",
            "Anneau commutatif : hérité de $\\mathbb{C}$.",
            "Pas un corps : $2$ n'a pas d'inverse.",
            "Bonus : les unités sont $\\pm1,\\pm i$.",
        ],
    )


# ---------------------------------------------------------------------------
# 4. Preuve
# ---------------------------------------------------------------------------
with onglets[3]:
    etapes_preuve([
        {
            "titre": "Z[i] contient 0 et 1",
            "texte": "$0=0+0i$ et $1=1+0i$, avec $0,1\\in\\mathbb{Z}$.",
            "pourquoi": "Un sous-anneau doit contenir les neutres de l'anneau ambiant.",
        },
        {
            "titre": "Stabilité par addition et par opposé",
            "formules": [
                r"(a+ib)+(c+id)=(a+c)+i(b+d)\in\mathbb{Z}[i],",
                r"-(a+ib)=(-a)+i(-b)\in\mathbb{Z}[i].",
            ],
            "pourquoi": "$\\mathbb{Z}$ est stable par addition et par opposé.",
        },
        {
            "titre": "Stabilité par multiplication",
            "formules": [
                r"(a+ib)(c+id)=(ac-bd)+i(ad+bc).",
            ],
            "texte": "Or $ac-bd\\in\\mathbb{Z}$ et $ad+bc\\in\\mathbb{Z}$.",
            "pourquoi": "$\\mathbb{Z}$ est stable par addition, soustraction et multiplication.",
        },
        {
            "titre": "Anneau commutatif",
            "texte": "L'addition et la multiplication de $\\mathbb{Z}[i]$ sont celles de $\\mathbb{C}$. Elles sont donc associatives, distributives, et la multiplication est commutative.",
            "pourquoi": "Toutes les propriétés d'anneau sont héritées de $\\mathbb{C}$ ; il suffit d'avoir la stabilité.",
        },
        {
            "titre": "Ce n'est pas un corps : 2 n'a pas d'inverse",
            "texte": "Supposons qu'il existe $a+ib\\in\\mathbb{Z}[i]$ tel que $2(a+ib)=1$. En identifiant les parties réelles et imaginaires :",
            "formules": [
                r"2a=1\quad\text{et}\quad 2b=0.",
                r"a=\frac12\notin\mathbb{Z}.",
            ],
            "pourquoi": "Aucun entier $a$ ne vérifie $2a=1$. Donc $2$ n'est pas inversible dans $\\mathbb{Z}[i]$.",
        },
        {
            "titre": "Les unités",
            "texte": "La norme est multiplicative et entière : $N(zz')=N(z)N(z')$. Si $z=a+ib$ est inversible dans $\\mathbb{Z}[i]$, alors $N(z)N(z^{-1})=N(1)=1$, donc $N(z)=1$.",
            "formules": [
                r"a^2+b^2=1\ \Longrightarrow\ (a,b)\in\{(\pm1,0),(0,\pm1)\}.",
            ],
            "pourquoi": "Les seules solutions entières de $a^2+b^2=1$ sont les quatre points du cercle unité.",
        },
    ])


# ---------------------------------------------------------------------------
# 5. Code
# ---------------------------------------------------------------------------
with onglets[4]:
    st.markdown("On manipule les entiers de Gauss comme des couples d'entiers.")

    st.code(
        r'''
def mult(z, w):
    a, b = z
    c, d = w
    return (a*c - b*d, a*d + b*c)

def norme(z):
    a, b = z
    return a*a + b*b

def inverse_dans_Zi(z):
    a, b = z
    n = norme(z)
    if n == 0:
        return None
    # L'inverse dans C est (a - ib)/n ; il est dans Z[i] ssi n divise a et b.
    if a % n == 0 and (-b) % n == 0:
        return (a // n, (-b) // n)
    return None

for z in [(1, 0), (1, 1), (2, 0), (2, 1), (0, 1)]:
    print(z, "norme", norme(z), "inverse", inverse_dans_Zi(z))
''',
        language="python",
    )

    if st.button("Lancer la vérification", key="ex7_btn_code"):
        def mult(z, w):
            a, b = z
            c, d = w
            return (a * c - b * d, a * d + b * c)

        def norme(z):
            a, b = z
            return a * a + b * b

        def inverse_dans_Zi(z):
            a, b = z
            n = norme(z)
            if n == 0:
                return None
            if a % n == 0 and (-b) % n == 0:
                return (a // n, (-b) // n)
            return None

        st.dataframe(
            {
                "z": [str(z) for z in [(1, 0), (1, 1), (2, 0), (2, 1), (0, 1)]],
                "norme": [norme(z) for z in [(1, 0), (1, 1), (2, 0), (2, 1), (0, 1)]],
                "inverse dans Z[i]": [str(inverse_dans_Zi(z)) for z in [(1, 0), (1, 1), (2, 0), (2, 1), (0, 1)]],
            },
            hide_index=True,
        )
        st.info("Seuls les éléments de norme 1 ont un inverse dans Z[i] : ce sont les unités.")

    st.info(
        "La norme est multiplicative : $N(zz')=N(z)N(z')$. C'est elle qui permet de comprendre "
        "les unités et la factorisation dans $\\mathbb{Z}[i]$."
    )


# ---------------------------------------------------------------------------
# 6. Erreurs
# ---------------------------------------------------------------------------
with onglets[5]:
    encadre(
        "orange",
        "Erreur 1 — Écrire que Z[i] est un corps",
        texte=r"""
C'est faux : $2\in\mathbb{Z}[i]$ n'a pas d'inverse. Un corps exigerait que tout
élément non nul soit inversible.
""",
    )
    encadre(
        "orange",
        "Erreur 2 — Se tromper de signe dans le produit",
        texte=r"""
$(a+ib)(c+id)=ac+iad+ibc+i^2bd=(ac-bd)+i(ad+bc)$.
Le terme $bd$ est **soustrait**.
""",
    )
    encadre(
        "orange",
        "Erreur 3 — Croire que tout élément de norme > 1 est inversible",
        texte=r"""
L'inverse dans $\mathbb{C}$ est $(a-ib)/N(z)$. Il n'est dans $\mathbb{Z}[i]$ que si
$N(z)$ divise $a$ et $b$. Ce n'est pas le cas en général.
""",
    )
    encadre(
        "orange",
        "Erreur 4 — Oublier les unités",
        texte=r"""
Les unités de $\mathbb{Z}[i]$ sont $\pm1,\pm i$. Un élément inversible doit avoir
une norme égale à $1$.
""",
    )
    encadre(
        "orange",
        "Erreur 5 — Confondre anneau et corps",
        texte=r"""
$\mathbb{Z}[i]$ est un anneau intègre, mais pas un corps. $\mathbb{Z}$ est aussi
un anneau intègre non corps : c'est le même phénomène.
""",
    )


# ---------------------------------------------------------------------------
# 7. À retenir
# ---------------------------------------------------------------------------
with onglets[6]:
    encadre(
        "violet",
        "L'image à retenir : un réseau",
        texte=r"""
$\mathbb{Z}[i]$ est le réseau des points à coordonnées entières. On peut additionner
et multiplier, mais pas diviser par n'importe quoi : $1/2$ n'est pas dans le réseau.

La norme $N(a+ib)=a^2+b^2$ est la bonne lunette pour étudier ce réseau.
""",
    )

    encadre(
        "vert",
        "Squelette de preuve en 3 lignes",
        puces=[
            "$\\mathbb{Z}[i]$ est un sous-anneau de $\\mathbb{C}$ : stable par $+$, $-$, $\\times$, contient $0,1$.",
            "Il est commutatif car $\\mathbb{C}$ l'est.",
            "$2$ n'a pas d'inverse : $2(a+ib)=1$ imposerait $2a=1$, impossible dans $\\mathbb{Z}$.",
        ],
    )

    st.markdown("### Trois questions pour te tester")
    mini_question(
        "Pourquoi 2 n'a-t-il pas d'inverse dans Z[i] ?",
        r"Si $2(a+ib)=1$, alors $2a=1$ avec $a\in\mathbb{Z}$ : impossible.",
    )
    mini_question(
        "Quelles sont les unités de Z[i] ?",
        r"$\pm1$ et $\pm i$, c'est-à-dire les éléments de norme 1.",
    )
    mini_question(
        "Z[i] est-il intègre ?",
        r"Oui, car c'est un sous-anneau de $\mathbb{C}$, qui est un corps donc intègre. "
        r"Mais intègre ne veut pas dire corps.",
    )

pied_page()
