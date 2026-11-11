# -*- coding: utf-8 -*-
"""Exercice 1 — deux lois de composition sur R."""

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
from algebra_graphs import g_associativite, g_loi_ex1  # noqa: E402

configurer_page("Exercice 1", "1️⃣")

titre_page(
    "Exercice 1 — Deux lois sur R",
    "Commutativité, associativité, neutre et symétrique : les quatre premiers axiomes, "
    "testés sur deux lois très différentes.",
    "ALGÈBRE 1 · TD 3 · CP1",
)

st.markdown(
    badge("Loi interne", "bleu")
    + badge("Commutativité", "bleu")
    + badge("Associativité", "vert")
    + badge("Neutre", "violet")
    + badge("Symétrique", "orange"),
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
On nous donne deux opérations sur des réels. Pour chacune, il faut répondre à quatre questions :
la loi est-elle **commutative** ? **associative** ? admet-elle un **neutre** ? ses éléments ont-ils un **symétrique** ?

La première loi, $x*y=\sqrt{x^2+y^2}$, ressemble à une distance. La seconde,
$x*y=xy+(x^2-1)(y^2-1)$, est construite pour être commutative et avoir un neutre, mais pour échouer à l'associativité.
""",
    )

    st.latex(r"\text{Loi 1 :}\qquad \forall x,y\in\mathbb{R}^+,\quad x*y=\sqrt{x^2+y^2}")
    st.latex(r"\text{Loi 2 :}\qquad \forall x,y\in\mathbb{R},\quad x*y=xy+(x^2-1)(y^2-1)")

    col_g, col_d = st.columns(2, gap="large")
    with col_g:
        encadre(
            "vert",
            "Ce qui est donné",
            puces=[
                "Un ensemble : $\\mathbb{R}^+$ pour la loi 1, $\\mathbb{R}$ pour la loi 2.",
                "Une formule qui définit $x*y$.",
                "Quatre questions : commutative, associative, neutre, symétrique.",
            ],
        )
    with col_d:
        encadre(
            "violet",
            "Ce qu'il faut montrer",
            puces=[
                "1a et 2a : $x*y=y*x$ pour tous $x,y$.",
                "1b : $(x*y)*z=x*(y*z)$ ; 2b : trouver un triplet qui échoue.",
                "1c et 2c : exhiber le neutre et vérifier les deux côtés.",
                "1d : montrer qu'aucun $x>0$ n'a de symétrique.",
            ],
        )

    st.warning(
        r"""
**Piège de l'énoncé.** Le PDF écrit $\mathbb{R}^{+*}$ (réels strictement positifs), mais demande
de montrer que **0 est élément neutre**. Or $0\notin\mathbb{R}^{+*}$ : c'est incompatible.

L'interprétation cohérente est $\mathbb{R}^+=[0,+\infty[$. Avec cet ensemble :
- $0$ est bien neutre : $\sqrt{x^2+0}=|x|=x$ pour $x\ge0$ ;
- aucun $x>0$ n'a de symétrique, car $\sqrt{x^2+y^2}=0$ force $x=y=0$.

Si ton professeur maintient $\mathbb{R}^{+*}$, alors la question 1c est fausse et il faut le signaler :
la loi n'a pas de neutre dans $\mathbb{R}^{+*}$.
"""
    )

    st.markdown(
        "**Le dessin mental.** La loi 1 transforme deux nombres en la distance du point $(x,y)$ "
        "à l'origine. La loi 2 est une surface plus cabossée : elle est symétrique en $x$ et $y$, "
        "mais elle ne se plie pas correctement pour l'associativité."
    )


# ---------------------------------------------------------------------------
# 2. Intuition
# ---------------------------------------------------------------------------
with onglets[1]:
    st.markdown("### La surface de la loi 1 et de la loi 2")
    g_loi_ex1()

    st.markdown("### Le défaut d'associativité de la loi 2")
    st.markdown(
        "Ici, on compare $(x*y)*z$ et $x*(y*z)$. Pour la loi 2, un petit triplet suffit "
        "à faire apparaître la différence."
    )
    g_associativite()


# ---------------------------------------------------------------------------
# 3. Idée
# ---------------------------------------------------------------------------
with onglets[2]:
    encadre(
        "bleu",
        "Le réflexe du prof",
        texte=r"""
Quand on te donne une loi définie par une formule, ne commence jamais par calculer au hasard.
Pose les quatre questions dans l'ordre :

1. **La loi est-elle interne ?** Le résultat reste-t-il dans l'ensemble ?
2. **Est-elle commutative ?** Développe $x*y$ et $y*x$.
3. **Est-elle associative ?** Calcule $(x*y)*z$ et $x*(y*z)$ avec des lettres.
4. **Y a-t-il un neutre ?** Résous $e*x=x$ pour tout $x$.
5. **Y a-t-il des symétriques ?** Résous $x*y=e$.

Pour une **preuve**, il faut des lettres. Pour une **réfutation**, un seul contre-exemple suffit.
""",
    )

    st.markdown(
        r"""
**Les indices de l'énoncé.**

- La loi 1 contient $x^2+y^2$ : c'est symétrique en $x$ et $y$, donc la commutativité est immédiate.
- La loi 1 contient une racine carrée : pour l'associativité, il faudra utiliser $(\sqrt a)^2=a$ pour $a\ge0$.
- La loi 2 contient $(x^2-1)(y^2-1)$ : le neutre probable est $1$, car $1^2-1=0$.
- La question 2b demande explicitement « non associative » : il faut donc **chercher un contre-exemple**, pas prouver.
"""
    )

    encadre(
        "violet",
        "Plan de la preuve",
        puces=[
            "Traiter la loi 1 : commutativité, associativité, neutre 0, absence de symétrique pour $x>0$.",
            "Traiter la loi 2 : commutativité par développement, non-associativité par $(0,0,2)$, neutre 1.",
            "Conclure proprement : chaque réponse est justifiée par un calcul ou un contre-exemple.",
        ],
    )


# ---------------------------------------------------------------------------
# 4. Preuve
# ---------------------------------------------------------------------------
with onglets[3]:
    st.markdown("## Loi 1 : $x*y=\\sqrt{x^2+y^2}$ sur $\\mathbb{R}^+$")

    etapes_preuve([
        {
            "titre": "La loi est interne",
            "texte": "Si $x,y\\ge0$, alors $x^2+y^2\\ge0$, donc $\\sqrt{x^2+y^2}$ est un réel positif.",
            "pourquoi": "Une racine carrée d'un réel positif existe toujours et est positive.",
        },
        {
            "titre": "Commutativité (1a)",
            "formules": [r"x*y=\sqrt{x^2+y^2}=\sqrt{y^2+x^2}=y*x."],
            "pourquoi": "L'addition dans la racine est commutative.",
        },
        {
            "titre": "Associativité (1b)",
            "formules": [
                r"(x*y)*z=\sqrt{(x*y)^2+z^2}=\sqrt{\left(\sqrt{x^2+y^2}\right)^2+z^2}=\sqrt{x^2+y^2+z^2}.",
                r"x*(y*z)=\sqrt{x^2+(y*z)^2}=\sqrt{x^2+y^2+z^2}.",
            ],
            "pourquoi": "On utilise $(\\sqrt a)^2=a$ pour $a\\ge0$, puis la commutativité de l'addition.",
        },
        {
            "titre": "Neutre (1c)",
            "formules": [r"x*0=\sqrt{x^2+0}=\sqrt{x^2}=|x|=x\qquad(x\ge0)."],
            "texte": "De même, $0*x=x$. Donc $0$ est neutre.",
            "pourquoi": "Pour $x\\ge0$, $|x|=x$. C'est ici qu'on utilise $\\mathbb{R}^+$ et non $\\mathbb{R}^{+*}$.",
        },
        {
            "titre": "Aucun $x>0$ n'a de symétrique (1d)",
            "texte": "Supposons que $x>0$ ait un symétrique $y\\ge0$. Alors $x*y=0$, donc $\\sqrt{x^2+y^2}=0$.",
            "formules": [r"x^2+y^2=0\ \Longrightarrow\ x=0\ \text{et}\ y=0,"],
            "pourquoi": "Une somme de carrés n'est nulle que si chaque carré est nul. Cela contredit $x>0$.",
        },
    ])

    st.markdown("## Loi 2 : $x*y=xy+(x^2-1)(y^2-1)$ sur $\\mathbb{R}$")

    etapes_preuve([
        {
            "titre": "Commutativité (2a)",
            "formules": [
                r"x*y=xy+(x^2-1)(y^2-1)=yx+(y^2-1)(x^2-1)=y*x.",
            ],
            "pourquoi": "Le produit $xy$ et le produit des deux facteurs sont commutatifs.",
        },
        {
            "titre": "Non-associativité (2b)",
            "texte": "Prenons $x=0$, $y=0$, $z=2$. On calcule d'abord $0*0$ :",
            "formules": [
                r"0*0=0\cdot0+(0-1)(0-1)=1.",
                r"(0*0)*2=1*2=1\cdot2+(1-1)(4-1)=2.",
                r"0*2=0\cdot2+(0-1)(4-1)=-3,",
                r"0*(0*2)=0*(-3)=0\cdot(-3)+(0-1)(9-1)=-8.",
            ],
            "pourquoi": "On trouve $2$ à gauche et $-8$ à droite : les deux parenthésages diffèrent, donc la loi n'est pas associative.",
        },
        {
            "titre": "Neutre (2c)",
            "formules": [
                r"x*1=x\cdot1+(x^2-1)(1^2-1)=x.",
                r"1*x=1\cdot x+(1^2-1)(x^2-1)=x.",
            ],
            "pourquoi": "Le facteur $(1^2-1)$ est nul, donc le deuxième terme disparaît.",
        },
        {
            "titre": "Conclusion de l'exercice 1",
            "texte": "La loi 1 est commutative, associative, de neutre $0$, mais aucun $x>0$ n'a de symétrique : ce n'est pas un groupe. La loi 2 est commutative, de neutre $1$, mais non associative : ce n'est pas un groupe non plus.",
            "pourquoi": "Un groupe exige les quatre axiomes à la fois ; il suffit qu'un seul manque pour que ce ne soit pas un groupe.",
        },
    ])


# ---------------------------------------------------------------------------
# 5. Code
# ---------------------------------------------------------------------------
with onglets[4]:
    st.markdown(
        "On vérifie les calculs avec **SymPy**. Le code cherche aussi un contre-exemple "
        "à l'associativité de la loi 2."
    )

    st.code(
        r'''
import sympy as sp

x, y, z = sp.symbols("x y z", real=True)

# Loi 1 : x*y = sqrt(x^2 + y^2)
def loi1(a, b):
    return sp.sqrt(a**2 + b**2)

print("Commutativité 1 :", sp.simplify(loi1(x, y) - loi1(y, x)))
print("Associativité 1 :", sp.simplify(loi1(loi1(x, y), z) - loi1(x, loi1(y, z))))

# Loi 2 : x*y = x*y + (x^2 - 1)(y^2 - 1)
def loi2(a, b):
    return a*b + (a**2 - 1)*(b**2 - 1)

print("Commutativité 2 :", sp.expand(loi2(x, y) - loi2(y, x)))

# Cherche un contre-exemple à l'associativité
for a in range(-2, 3):
    for b in range(-2, 3):
        for c in range(-2, 3):
            if loi2(loi2(a, b), c) != loi2(a, loi2(b, c)):
                print("Contre-exemple :", (a, b, c),
                      loi2(loi2(a, b), c), loi2(a, loi2(b, c)))
                raise SystemExit
''',
        language="python",
    )

    if st.button("Lancer la vérification SymPy", key="ex1_btn_sympy"):
        import sympy as sp

        x, y, z = sp.symbols("x y z", real=True)

        def loi1(a, b):
            return sp.sqrt(a**2 + b**2)

        def loi2(a, b):
            return a * b + (a**2 - 1) * (b**2 - 1)

        st.write("Commutativité loi 1 :", sp.simplify(loi1(x, y) - loi1(y, x)))
        st.write("Associativité loi 1 :", sp.simplify(loi1(loi1(x, y), z) - loi1(x, loi1(y, z))))
        st.write("Commutativité loi 2 :", sp.expand(loi2(x, y) - loi2(y, x)))

        trouve = None
        for a in range(-2, 3):
            for b in range(-2, 3):
                for c in range(-2, 3):
                    if loi2(loi2(a, b), c) != loi2(a, loi2(b, c)):
                        trouve = (a, b, c, loi2(loi2(a, b), c), loi2(a, loi2(b, c)))
                        break
                if trouve:
                    break
            if trouve:
                break

        if trouve:
            a, b, c, g, d = trouve
            st.error(
                f"Contre-exemple trouvé : x={a}, y={b}, z={c}. "
                f"À gauche : {g}, à droite : {d}."
            )
        else:
            st.success("Aucun contre-exemple sur cette grille.")

    st.info(
        "Le code ne remplace pas la preuve : il confirme les calculs et trouve des contre-exemples. "
        "En DS, tu dois écrire le calcul avec des lettres."
    )


# ---------------------------------------------------------------------------
# 6. Erreurs
# ---------------------------------------------------------------------------
with onglets[5]:
    encadre(
        "orange",
        "Erreur 1 — Croire que 0 est dans R^{+*}",
        texte=r"""
$0$ n'est pas strictement positif. Si l'ensemble est vraiment $\mathbb{R}^{+*}$, la question 1c
est fausse. Il faut donc signaler l'ambiguïté et travailler dans $\mathbb{R}^+$ pour que
l'énoncé ait un sens.
""",
    )
    encadre(
        "orange",
        "Erreur 2 — Vérifier l'associativité avec un seul exemple",
        texte=r"""
Un exemple où $(x*y)*z=x*(y*z)$ ne prouve **rien** : il faut le faire avec des lettres.
En revanche, un seul contre-exemple suffit pour prouver que la loi n'est **pas** associative.
""",
    )
    encadre(
        "orange",
        "Erreur 3 — Écrire √(x²+y²)=x+y",
        texte=r"""
C'est faux : $\sqrt{x^2+y^2}$ n'est pas $x+y$. Par exemple, $\sqrt{3^2+4^2}=5$, alors que $3+4=7$.
""",
    )
    encadre(
        "orange",
        "Erreur 4 — Confondre neutre et absorbant",
        texte=r"""
Un neutre vérifie $e*x=x$. Un absorbant vérifie $a*x=a$. Dans la loi 1, $0$ est neutre,
pas absorbant : $0*x=x$, pas $0$.
""",
    )
    encadre(
        "orange",
        "Erreur 5 — Oublier un côté pour le neutre",
        texte=r"""
Il faut vérifier $e*x=x$ **et** $x*e=x$. Si la loi n'est pas commutative, les deux calculs
peuvent donner des résultats différents.
""",
    )


# ---------------------------------------------------------------------------
# 7. À retenir
# ---------------------------------------------------------------------------
with onglets[6]:
    encadre(
        "violet",
        "Le moyen mnémotechnique : C.A.N.S.",
        texte=r"""
Pour toute loi, pose les questions dans cet ordre :

**C**ommutative ? **A**ssociative ? **N**eutre ? **S**ymétrique ?

C'est l'ordre de la définition d'un groupe. Si tu oublies un axiome, tu ne peux pas conclure.
""",
    )

    encadre(
        "vert",
        "Squelette de preuve en 3 lignes",
        puces=[
            "Loi 1 : commutative et associative par symétrie de $x^2+y^2$ ; neutre $0$ ; aucun $x>0$ n'a de symétrique.",
            "Loi 2 : commutative par développement ; non associative (contre-exemple) ; neutre $1$.",
            "Conclusion : la loi 1 n'est pas un groupe (les éléments positifs n'ont pas d'inverse) ; la loi 2 n'est pas un groupe (non associative).",
        ],
    )

    st.markdown("### Trois questions pour te tester")
    mini_question(
        "Pourquoi 0 ne peut-il pas être neutre dans R^{+*} ?",
        r"Parce que $0\notin\mathbb{R}^{+*}$. Un neutre doit appartenir à l'ensemble. "
        r"Si l'ensemble est $\mathbb{R}^+$, alors 0 est neutre.",
    )
    mini_question(
        "Que vaut (0∗0)∗2 pour la loi 2 ?",
        r"$0*0=1$, donc $(0*0)*2=1*2=2$. Mais $0*(0*2)=0*(-3)=-8$ : "
        r"les deux parenthésages diffèrent, ce qui prouve que la loi n'est pas associative.",
    )
    mini_question(
        "Un élément x>0 peut-il avoir un symétrique pour la loi 1 ?",
        r"Non : $x*y=0$ implique $x^2+y^2=0$, donc $x=0$. "
        r"Aucun $x>0$ n'a de symétrique ; seul 0 est son propre symétrique.",
    )

pied_page()
