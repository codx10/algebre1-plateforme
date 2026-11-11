# -*- coding: utf-8 -*-
"""Exercice 8 — le corps Q[i], preuve directe."""

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
from algebra_graphs import g_ex8  # noqa: E402

configurer_page("Exercice 8", "8️⃣")

titre_page(
    "Exercice 8 — Le corps Q[i]",
    "La preuve directe : on vérifie tous les axiomes de corps pour les complexes "
    "à coordonnées rationnelles.",
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
$$ \mathbb{Q}[i]=\{a+ib: a,b\in\mathbb{Q}\}. $$
Montrer que $(\mathbb{Q}[i],+,\times)$ est un **corps**.

C'est le même ensemble que $\mathbb{K}$ de l'exercice 5. Ici, on demande une preuve
directe, axiomé par axiome, sans passer par « sous-corps de $\mathbb{C}$ ».
""",
    )

    col_g, col_d = st.columns(2, gap="large")
    with col_g:
        encadre(
            "vert",
            "Ce qui est donné",
            puces=[
                "Les coordonnées sont rationnelles.",
                "$+$ et $\\times$ sont les opérations de $\\mathbb{C}$.",
                "Il faut montrer **tous** les axiomes de corps.",
            ],
        )
    with col_d:
        encadre(
            "violet",
            "Ce qu'il faut montrer",
            puces=[
                "$(\\mathbb{Q}[i],+)$ : groupe abélien.",
                "$(\\mathbb{Q}[i]^*,\\times)$ : groupe abélien.",
                "Distributivité.",
                "$1\\neq0$.",
            ],
        )

    st.info(
        r"""
**Pourquoi c'est un corps et pas seulement un anneau.** La différence avec $\mathbb{Z}[i]$
est la division : dans $\mathbb{Q}[i]$, $1/2$ est autorisé. L'inverse
$$ \frac1{a+bi}=\frac{a-bi}{a^2+b^2} $$
reste à coordonnées rationnelles, car $a,b,a^2+b^2\in\mathbb{Q}$.
"""
    )


# ---------------------------------------------------------------------------
# 2. Intuition
# ---------------------------------------------------------------------------
with onglets[1]:
    st.markdown("### L'inverse reste dans le plan rationnel")
    g_ex8()
    st.markdown(
        "Le conjugué renverse l'angle, la norme ajuste la longueur. Si $a$ et $b$ sont "
        "rationnels, alors $a/(a^2+b^2)$ et $-b/(a^2+b^2)$ le sont aussi."
    )


# ---------------------------------------------------------------------------
# 3. Idée
# ---------------------------------------------------------------------------
with onglets[2]:
    encadre(
        "bleu",
        "Le réflexe du prof",
        texte=r"""
On peut procéder de deux façons :

1. **Sous-corps** : $\mathbb{Q}[i]$ est un sous-corps de $\mathbb{C}$ (exercice 5).
2. **Preuve directe** : on vérifie les axiomes un par un.

Ici, on fait la preuve directe. Le seul point non trivial est l'inverse.
Tout le reste est hérité de $\mathbb{C}$ ou se vérifie composante par composante.
""",
    )

    st.markdown(
        r"""
**Les indices.**

- $(\mathbb{Q}[i],+)$ est essentiellement $(\mathbb{Q}^2,+)$.
- La multiplication est celle de $\mathbb{C}$ : associative, commutative, distributive.
- Le neutre multiplicatif est $1=1+0i$.
- L'inverse utilise $a^2+b^2$, qui est un rationnel non nul dès que $z\neq0$.
"""
    )

    encadre(
        "violet",
        "Plan de la preuve",
        puces=[
            "$(\\mathbb{Q}[i],+)$ : groupe abélien.",
            "$(\\mathbb{Q}[i]^*,\\times)$ : stabilité, associativité, neutre, inverse.",
            "Distributivité et $1\\neq0$.",
            "Conclusion : corps commutatif.",
        ],
    )


# ---------------------------------------------------------------------------
# 4. Preuve
# ---------------------------------------------------------------------------
with onglets[3]:
    etapes_preuve([
        {
            "titre": "(Q[i], +) est un groupe abélien",
            "texte": "L'addition est composante par composante. Le neutre est $0=0+0i$ et l'opposé de $a+ib$ est $-a-ib$.",
            "formules": [
                r"(a+ib)+(c+id)=(a+c)+i(b+d),",
                r"(a+ib)+(-a-ib)=0.",
            ],
            "pourquoi": "$\\mathbb{Q}$ est un groupe abélien pour l'addition ; on travaille composante par composante.",
        },
        {
            "titre": "Stabilité par multiplication",
            "formules": [
                r"(a+ib)(c+id)=(ac-bd)+i(ad+bc).",
            ],
            "texte": "Si $a,b,c,d\\in\\mathbb{Q}$, alors $ac-bd\\in\\mathbb{Q}$ et $ad+bc\\in\\mathbb{Q}$.",
            "pourquoi": "$\\mathbb{Q}$ est stable par addition, soustraction et multiplication.",
        },
        {
            "titre": "Associativité, commutativité, neutre",
            "texte": "La multiplication de $\\mathbb{Q}[i]$ est celle de $\\mathbb{C}$ : elle est associative, commutative, et $1=1+0i$ est neutre.",
            "pourquoi": "Ces propriétés sont héritées de $\\mathbb{C}$ ; il suffit que le produit reste dans $\\mathbb{Q}[i]$.",
        },
        {
            "titre": "Inverse d'un élément non nul",
            "texte": "Soit $z=a+ib\\neq0$. Alors $a^2+b^2\\neq0$ et",
            "formules": [
                r"z^{-1}=\frac{a-ib}{a^2+b^2}=\frac{a}{a^2+b^2}+i\frac{-b}{a^2+b^2}.",
                r"z\,z^{-1}=\frac{(a+ib)(a-ib)}{a^2+b^2}=\frac{a^2+b^2}{a^2+b^2}=1.",
            ],
            "pourquoi": "$a/(a^2+b^2)$ et $-b/(a^2+b^2)$ sont rationnels : l'inverse reste dans $\\mathbb{Q}[i]$.",
        },
        {
            "titre": "Distributivité",
            "formules": [
                r"z(w+w')=zw+zw'.",
            ],
            "texte": "C'est la distributivité dans $\\mathbb{C}$, valable pour tous $z,w,w'\\in\\mathbb{Q}[i]$.",
            "pourquoi": "On ne recalcule rien : $\\mathbb{Q}[i]\\subset\\mathbb{C}$ et la distributivité y est vraie.",
        },
        {
            "titre": "Conclusion : corps commutatif",
            "texte": "$(\\mathbb{Q}[i],+)$ est un groupe abélien, $(\\mathbb{Q}[i]^*,\\times)$ est un groupe abélien, la multiplication est distributive sur l'addition, et $1\\neq0$.",
            "pourquoi": "Ce sont exactement les axiomes d'un corps commutatif.",
        },
    ])

    st.success(
        "Le point clé est encore l'inverse : le dénominateur $a^2+b^2$ est un rationnel "
        "non nul, donc les coordonnées de $1/z$ restent rationnelles."
    )


# ---------------------------------------------------------------------------
# 5. Code
# ---------------------------------------------------------------------------
with onglets[4]:
    st.markdown("On vérifie l'inverse avec des fractions exactes.")

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

z = (Fraction(3, 2), Fraction(-1, 3))
w = inverse(z)
print("z =", z)
print("1/z =", w)
print("z * 1/z =", mult(z, w))
''',
        language="python",
    )

    if st.button("Lancer la vérification", key="ex8_btn_code"):
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

        z = (Fraction(3, 2), Fraction(-1, 3))
        w = inverse(z)
        st.write("z =", f"{z[0]} + ({z[1]})i")
        st.write("1/z =", f"{w[0]} + ({w[1]})i")
        st.write("z × (1/z) =", mult(z, w))

    st.info(
        "Les `Fraction` évitent les erreurs d'arrondi : on vérifie exactement que le produit "
        "vaut $(1,0)$."
    )


# ---------------------------------------------------------------------------
# 6. Erreurs
# ---------------------------------------------------------------------------
with onglets[5]:
    encadre(
        "orange",
        "Erreur 1 — Oublier de vérifier la stabilité",
        texte=r"""
Il ne suffit pas que $+$ et $\\times$ soient celles de $\\mathbb{C}$ : il faut vérifier
que le résultat reste dans $\\mathbb{Q}[i]$. C'est vrai, mais cela se prouve.
""",
    )
    encadre(
        "orange",
        "Erreur 2 — Diviser par z sans vérifier z ≠ 0",
        texte=r"""
L'inverse n'existe que pour $z\neq0$. Si $z=0$, alors $a^2+b^2=0$ et la formule
n'a pas de sens.
""",
    )
    encadre(
        "orange",
        "Erreur 3 — Écrire 1/(a+bi) = 1/a + (1/b)i",
        texte=r"""
C'est faux. Il faut multiplier par le conjugué :
$\\dfrac1{a+bi}=\\dfrac{a-bi}{a^2+b^2}$.
""",
    )
    encadre(
        "orange",
        "Erreur 4 — Confondre Q[i] et Z[i]",
        texte=r"""
Dans $\\mathbb{Z}[i]$, $2$ n'a pas d'inverse ; dans $\\mathbb{Q}[i]$, $1/2$ est autorisé.
C'est la différence entre anneau et corps.
""",
    )
    encadre(
        "orange",
        "Erreur 5 — Dire « c'est un corps donc c'est C »",
        texte=r"""
$\\mathbb{Q}[i]$ est un corps, mais il ne contient pas $\\sqrt2$ : ce n'est pas $\\mathbb{C}$.
C'est un sous-corps strict de $\\mathbb{C}$.
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
Pour diviser par $a+bi$, on multiplie en haut et en bas par $a-bi$ :
$$ \frac1{a+bi}=\frac{a-bi}{a^2+b^2}. $$
Tout le chapitre tient dans cette formule.
""",
    )

    encadre(
        "vert",
        "Squelette de preuve en 4 lignes",
        puces=[
            "$(\\mathbb{Q}[i],+)$ est un groupe abélien (composante par composante).",
            "$\\times$ est stable, associative, commutative, de neutre 1.",
            "Inverse : $1/z=\\overline z/|z|^2$, à coordonnées rationnelles.",
            "Distributivité et $1\\neq0$ : c'est un corps.",
        ],
    )

    st.markdown("### Trois questions pour te tester")
    mini_question(
        "Pourquoi 1/(a+bi) reste-t-il dans Q[i] ?",
        r"Parce que $1/(a+bi)=(a-bi)/(a^2+b^2)$ et que $a,b,a^2+b^2$ sont rationnels.",
    )
    mini_question(
        "Quel est le neutre de la multiplication ?",
        r"$1=1+0i$.",
    )
    mini_question(
        "Q[i] est-il égal à C ?",
        r"Non. $\\mathbb{Q}[i]$ ne contient que les complexes à coordonnées rationnelles ; "
        r"$\\sqrt2+i$ n'y est pas.",
    )

pied_page()
