# -*- coding: utf-8 -*-
"""Exercice 5 — le corps Q(i)."""

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
from algebra_graphs import g_ex5  # noqa: E402

configurer_page("Exercice 5", "5️⃣")

titre_page(
    "Exercice 5 — Le corps Q(i)",
    "Les nombres complexes à coordonnées rationnelles : un groupe pour l'addition, "
    "un groupe pour la multiplication, et même un corps.",
    "ALGÈBRE 1 · TD 3 · CP1",
)

st.markdown(
    badge("Groupe additif", "bleu")
    + badge("Groupe multiplicatif", "vert")
    + badge("Corps", "violet"),
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
$$ \mathbb{K}=\{r+is: r,s\in\mathbb{Q}\}. $$
Il faut montrer que :
1. $(\mathbb{K},+)$ est un groupe commutatif ;
2. $(\mathbb{K}^*,\cdot)$ est un groupe commutatif, où $\mathbb{K}^*=\mathbb{K}\setminus\{0\}$ ;
3. $(\mathbb{K},+,\cdot)$ est un corps commutatif.
""",
    )

    col_g, col_d = st.columns(2, gap="large")
    with col_g:
        encadre(
            "vert",
            "Ce qui est donné",
            puces=[
                "Les coordonnées sont **rationnelles**, pas réelles.",
                "L'addition et la multiplication sont celles de $\\mathbb{C}$.",
                "$\\mathbb{K}^*$ signifie $\\mathbb{K}$ privé de $0$.",
            ],
        )
    with col_d:
        encadre(
            "violet",
            "Ce qu'il faut montrer",
            puces=[
                "Stabilité par $+$ et par $\\times$.",
                "Neutre, opposé, inverse.",
                "Toutes les coordonnées restent rationnelles.",
                "Distributivité et $1\\neq0$.",
            ],
        )

    st.info(
        r"""
**Pourquoi ce n'est pas $\mathbb{Z}[i]$.** Dans $\mathbb{Z}[i]$, les coordonnées sont des
**entiers** : $2$ n'a pas d'inverse. Ici, les coordonnées sont des **rationnels** :
$$ \frac1{2+i}=\frac{2-i}{5}=\frac25-\frac15 i\in\mathbb{K}. $$
C'est cette possibilité de diviser qui transforme l'anneau en corps.
"""
    )


# ---------------------------------------------------------------------------
# 2. Intuition
# ---------------------------------------------------------------------------
with onglets[1]:
    st.markdown("### L'inverse dans le plan complexe")
    g_ex5()
    st.markdown(
        "L'inverse de $z=a+bi$ est $\\dfrac{\\overline z}{|z|^2}=\\dfrac{a-bi}{a^2+b^2}$. "
        "Le conjugué renverse l'angle, la norme ajuste la longueur."
    )


# ---------------------------------------------------------------------------
# 3. Idée
# ---------------------------------------------------------------------------
with onglets[2]:
    encadre(
        "bleu",
        "Le réflexe du prof",
        texte=r"""
On connaît déjà $\mathbb{C}$ : c'est un corps. Il suffit de montrer que $\mathbb{K}$
est un **sous-corps** de $\mathbb{C}$.

Pour cela :
1. $0,1\in\mathbb{K}$ ;
2. $\mathbb{K}$ est stable par $+$, par opposé et par $\times$ ;
3. pour $z\in\mathbb{K}^*$, $1/z\in\mathbb{K}$.

Le seul point vraiment calculatoire est l'inverse : il faut vérifier que
$a/(a^2+b^2)$ et $-b/(a^2+b^2)$ sont rationnels.
""",
    )

    st.markdown(
        r"""
**Les indices.**

- $r,s\in\mathbb{Q}$ : toute somme, différence, produit de rationnels reste rationnel.
- L'inverse utilise $a^2+b^2$, qui est un rationnel non nul si $z\neq0$.
- $1\neq0$ dans $\mathbb{K}$ : c'est vrai car $\mathbb{K}\subset\mathbb{C}$.
"""
    )

    encadre(
        "violet",
        "Plan de la preuve",
        puces=[
            r"$(\mathbb{K},+)$ : sous-groupe de $(\mathbb{C},+)$.",
            r"$(\mathbb{K}^*,\cdot)$ : stabilité, associativité, neutre, inverse.",
            r"Distributivité héritée de $\mathbb{C}$.",
            "Conclusion : corps commutatif.",
        ],
    )


# ---------------------------------------------------------------------------
# 4. Preuve
# ---------------------------------------------------------------------------
with onglets[3]:
    etapes_preuve([
        {
            "titre": "K contient 0 et 1",
            "texte": "$0=0+0i$ et $1=1+0i$, avec $0,1\\in\\mathbb{Q}$.",
            "pourquoi": "Ce sont les neutres de $+$ et de $\\times$ dans $\\mathbb{C}$.",
        },
        {
            "titre": "(K, +) est un groupe commutatif",
            "texte": "Si $z=r+is$ et $z'=r'+is'$ avec $r,s,r',s'\\in\\mathbb{Q}$, alors",
            "formules": [
                r"z+z'=(r+r')+i(s+s')\in\mathbb{K},",
                r"-z=-r+i(-s)\in\mathbb{K}.",
            ],
            "pourquoi": "$\\mathbb{Q}$ est stable par addition et par opposé. L'associativité et la commutativité sont héritées de $\\mathbb{C}$.",
        },
        {
            "titre": "K est stable par multiplication",
            "formules": [
                r"(r+is)(r'+is')=(rr'-ss')+i(rs'+sr').",
            ],
            "texte": "Or $rr'-ss'\\in\\mathbb{Q}$ et $rs'+sr'\\in\\mathbb{Q}$.",
            "pourquoi": "$\\mathbb{Q}$ est stable par addition, soustraction et multiplication.",
        },
        {
            "titre": "(K*, ·) est un groupe commutatif",
            "texte": "La multiplication est associative et commutative dans $\\mathbb{C}$, donc dans $\\mathbb{K}$. Le neutre est $1=1+0i\\in\\mathbb{K}$.",
            "pourquoi": "Il ne reste que l'inverse à vérifier.",
        },
        {
            "titre": "Inverse d'un élément non nul",
            "texte": "Soit $z=r+is\\neq0$. Alors $r^2+s^2\\neq0$ et",
            "formules": [
                r"\frac1z=\frac{r-is}{r^2+s^2}=\frac{r}{r^2+s^2}+i\,\frac{-s}{r^2+s^2}.",
                r"z\cdot\frac1z=\frac{(r+is)(r-is)}{r^2+s^2}=\frac{r^2+s^2}{r^2+s^2}=1.",
            ],
            "pourquoi": "$r^2+s^2$ est un rationnel non nul, donc les deux coordonnées de $1/z$ sont rationnelles. L'inverse reste dans $\\mathbb{K}$.",
        },
        {
            "titre": "(K, +, ·) est un corps commutatif",
            "texte": "$(\\mathbb{K},+)$ est un groupe abélien, $(\\mathbb{K}^*,\\cdot)$ est un groupe abélien, la multiplication est distributive sur l'addition, et $1\\neq0$.",
            "pourquoi": "Ce sont exactement les axiomes d'un corps commutatif.",
        },
    ])

    st.success(
        "Le point clé est l'inverse : le dénominateur $r^2+s^2$ est un rationnel non nul, "
        "donc $1/z$ reste dans $\\mathbb{K}$."
    )


# ---------------------------------------------------------------------------
# 5. Code
# ---------------------------------------------------------------------------
with onglets[4]:
    st.markdown("On vérifie l'inverse avec des rationnels exacts, sans flottants.")

    st.code(
        r'''
from fractions import Fraction

def mult(z, w):
    a, b = z
    c, d = w
    return (a*c - b*d, a*d + b*c)

def inverse(z):
    a, b = z
    n = a*a + b*b
    if n == 0:
        raise ZeroDivisionError
    return (Fraction(a, n), Fraction(-b, n))

z = (Fraction(2), Fraction(1))   # 2 + i
w = inverse(z)
print("1/z =", w)
print("z * 1/z =", mult(z, w))
''',
        language="python",
    )

    if st.button("Lancer la vérification", key="ex5_btn_code"):
        from fractions import Fraction

        def mult(z, w):
            a, b = z
            c, d = w
            return (a * c - b * d, a * d + b * c)

        def inverse(z):
            a, b = z
            n = a * a + b * b
            if n == 0:
                raise ZeroDivisionError
            return (Fraction(a, n), Fraction(-b, n))

        z = (Fraction(2), Fraction(1))
        w = inverse(z)
        st.write("z = 2 + i")
        st.write("1/z =", f"{w[0]} + ({w[1]})i")
        st.write("z × (1/z) =", mult(z, w))

    st.info(
        "$\\mathbb{Q}$ est stable par les quatre opérations (sauf division par zéro). "
        "C'est cette stabilité qui permet à l'inverse de rester dans $\\mathbb{K}$."
    )


# ---------------------------------------------------------------------------
# 6. Erreurs
# ---------------------------------------------------------------------------
with onglets[5]:
    encadre(
        "orange",
        "Erreur 1 — Écrire 1/(a+bi) = 1/a + (1/b)i",
        texte=r"""
C'est faux. Il faut multiplier par le conjugué :
$$ \frac1{a+bi}=\frac{a-bi}{a^2+b^2}. $$
""",
    )
    encadre(
        "orange",
        "Erreur 2 — Oublier la condition z ≠ 0",
        texte=r"""
Si $z=0$, alors $a^2+b^2=0$ et l'inverse n'existe pas. Le groupe multiplicatif est
$\mathbb{K}^*$, pas $\mathbb{K}$.
""",
    )
    encadre(
        "orange",
        "Erreur 3 — Confondre Q(i) et Z[i]",
        texte=r"""
Dans $\mathbb{Z}[i]$, les coordonnées sont entières : $2$ n'a pas d'inverse.
Dans $\mathbb{Q}[i]$, les coordonnées sont rationnelles : $1/2$ est autorisé.
C'est toute la différence entre un anneau et un corps.
""",
    )
    encadre(
        "orange",
        "Erreur 4 — Dire « c'est évident que c'est un corps »",
        texte=r"""
Il faut vérifier la stabilité par inverse. C'est le seul axiome qui n'est pas hérité
automatiquement de $\mathbb{C}$.
""",
    )
    encadre(
        "orange",
        "Erreur 5 — Écrire que K = C",
        texte=r"""
$\mathbb{K}$ ne contient que les complexes dont les parties réelle et imaginaire sont
rationnelles. $\sqrt2+i$ n'est pas dans $\mathbb{K}$.
""",
    )


# ---------------------------------------------------------------------------
# 7. À retenir
# ---------------------------------------------------------------------------
with onglets[6]:
    encadre(
        "violet",
        "L'image à retenir : le conjugué",
        texte=r"""
Pour inverser un complexe, on multiplie en haut et en bas par le conjugué :
$$ \frac1z=\frac{\overline z}{z\overline z}=\frac{\overline z}{|z|^2}. $$
Le dénominateur est un **rationnel** si $z\in\mathbb{Q}[i]$. C'est ce qui fait tenir le corps.
""",
    )

    encadre(
        "vert",
        "Squelette de preuve en 3 lignes",
        puces=[
            "$(\\mathbb{K},+)$ est un sous-groupe de $(\\mathbb{C},+)$.",
            "$(\\mathbb{K}^*,\\cdot)$ est un groupe : stabilité, neutre 1, inverse $\\overline z/|z|^2$.",
            "La distributivité est héritée de $\\mathbb{C}$ : $\\mathbb{K}$ est un corps.",
        ],
    )

    st.markdown("### Trois questions pour te tester")
    mini_question(
        "Quel est l'inverse de 2 + i ?",
        r"$\dfrac{2-i}{2^2+1^2}=\dfrac25-\dfrac15 i$.",
    )
    mini_question(
        "Pourquoi 1/z reste-t-il dans Q(i) ?",
        r"Parce que $1/z=(a-bi)/(a^2+b^2)$ et que $a,b,a^2+b^2$ sont rationnels.",
    )
    mini_question(
        "Quelle différence avec Z[i] ?",
        r"Dans $\mathbb{Z}[i]$, $a^2+b^2$ n'est pas inversible dans $\mathbb{Z}$ en général. "
        r"Par exemple, $1/2\notin\mathbb{Z}$, donc $2$ n'a pas d'inverse dans $\mathbb{Z}[i]$.",
    )

pied_page()
