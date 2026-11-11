# -*- coding: utf-8 -*-
"""Fiche de synthèse — Algèbre 1, TD 3."""

from __future__ import annotations

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
if str(RACINE) not in sys.path:
    sys.path.insert(0, str(RACINE))

import streamlit as st  # noqa: E402

from ui import badge, configurer_page, encadre, pied_page, titre_page  # noqa: E402

configurer_page("Fiche de synthèse", "📄")

titre_page(
    "Fiche de synthèse — TD 3",
    "Tous les axiomes, les méthodes et les contre-exemples sur une page. "
    "À relire la veille du DS, puis à reconstruire de mémoire.",
    "ALGÈBRE 1 · CP1 · RÉVISION",
)

st.markdown(
    badge("Axiomes", "bleu")
    + badge("Méthodes", "vert")
    + badge("Exemples", "violet")
    + badge("Pièges", "orange"),
    unsafe_allow_html=True,
)

st.markdown("## 1. Les définitions en tableau")

st.markdown(
    r"""
| Structure | Ce qu'il faut vérifier |
|---|---|
| **Loi interne** | $\forall x,y\in E,\ x*y\in E$. |
| **Commutative** | $\forall x,y,\ x*y=y*x$. |
| **Associative** | $\forall x,y,z,\ (x*y)*z=x*(y*z)$. |
| **Neutre** | $\exists e,\ \forall x,\ e*x=x*e=x$. Unique. |
| **Symétrique** | $x*x'=x'*x=e$. Unique dans un groupe. |
| **Groupe** | Interne + associative + neutre + inverse pour tous. |
| **Abélien** | Groupe + commutative. |
| **Sous-groupe** | $H\neq\varnothing$, stable par $*$ et par inverse. |
| **Anneau** | $(A,+)$ groupe abélien, $\times$ associative et distributive sur $+$. |
| **Corps** | Anneau commutatif, $1\neq0$, tout $x\neq0$ inversible. |
| **Intègre** | Anneau commutatif sans diviseurs de zéro. |
"""
)

st.markdown("## 2. Les tests rapides")

col_g, col_d = st.columns(2, gap="large")

with col_g:
    encadre(
        "vert",
        "Montrer qu'un ensemble est un groupe",
        puces=[
            r"Clôture : $x*y\in G$.",
            "Associativité : calcul avec des lettres.",
            "Neutre : exhiber $e$, vérifier $e*x=x*e=x$.",
            "Inverse : exhiber $x^{-1}$, vérifier les deux côtés.",
        ],
    )
    encadre(
        "vert",
        "Montrer qu'un sous-ensemble H est un sous-groupe",
        puces=[
            "$H\\neq\\varnothing$.",
            "Stabilité : $x,y\\in H\\Rightarrow x*y\\in H$.",
            "Inverse : $x\\in H\\Rightarrow x^{-1}\\in H$.",
            "Version courte : $x*y^{-1}\\in H$ pour tous $x,y\\in H$.",
        ],
    )

with col_d:
    encadre(
        "vert",
        "Montrer qu'un ensemble est un anneau",
        puces=[
            "$(A,+)$ groupe abélien : neutre $0$, opposé $-x$.",
            "$\\times$ associative.",
            "$a(b+c)=ab+ac$ et $(a+b)c=ac+bc$.",
            "Si $\\times$ est commutative : anneau commutatif.",
            "Si $1$ existe : anneau unitaire.",
        ],
    )
    encadre(
        "vert",
        "Montrer qu'un anneau est un corps",
        puces=[
            "Tout ce qui précède (anneau commutatif unitaire).",
            "$1\\neq0$.",
            "Tout $x\\neq0$ a un inverse $x^{-1}$.",
            "Vérifier que l'inverse reste dans l'ensemble.",
        ],
    )

st.markdown("## 3. Les exemples à connaître par cœur")

st.markdown(
    r"""
| Ensemble | Structure | Pourquoi |
|---|---|---|
| $(\mathbb{Z},+,\times)$ | Anneau intègre, pas corps | $2$ n'est pas inversible. |
| $(\mathbb{Q},+,\times)$ | Corps | Tout rationnel non nul est inversible. |
| $(\mathbb{R},+,\times)$ | Corps | Tout réel non nul est inversible. |
| $(\mathbb{C},+,\times)$ | Corps | Tout complexe non nul est inversible. |
| $(\mathbb{Z}[i],+,\times)$ | Anneau intègre, pas corps | $2$ n'est pas inversible. |
| $(\mathbb{Q}[i],+,\times)$ | Corps | $1/(a+bi)=(a-bi)/(a^2+b^2)\in\mathbb{Q}[i]$. |
| $(\mathcal{F}(\mathbb{R},\mathbb{R}),+,\times)$ | Anneau commutatif, non intègre | $f=\max(0,x)$, $g=\max(0,-x)$, $fg=0$. |
| $(\mathbb{Z}/6\mathbb{Z},\times)$ | Pas un groupe | $0$ n'a pas d'inverse. |
| $(S_3,\circ)$ | Groupe non abélien | La table n'est pas symétrique. |
| $(\mathbb{R}^2,*)$ de l'ex. 2 | Groupe non abélien | $(1,0)*(0,1)\neq(0,1)*(1,0)$. |
| $(H,*)$ de l'ex. 3 | Groupe non abélien | $(2,0)*(1,1)\neq(1,1)*(2,0)$. |
| $(A,+,*)$ de l'ex. 4 | Anneau commutatif, pas corps | $(0,1)^2=(0,0)$. |
"""
)

st.markdown("## 4. Les contre-exemples du TD")

col_g, col_d = st.columns(2, gap="large")
with col_g:
    encadre(
        "orange",
        "Pour nier une propriété, un seul exemple suffit",
        puces=[
            "Non associative : $x*y=xy+(x^2-1)(y^2-1)$, avec $(0,0,2)$.",
            "Non commutative : $S_3$ ; ou $(2,0)*(1,1)\\neq(1,1)*(2,0)$.",
            "Pas un groupe : $(\\mathbb{Z}/6\\mathbb{Z},\\times)$, car $0$ n'a pas d'inverse.",
            "Pas un corps : $\\mathbb{Z}$ et $\\mathbb{Z}[i]$, car $2$ n'est pas inversible.",
        ],
    )
with col_d:
    encadre(
        "orange",
        "Les phrases qui coûtent des points",
        puces=[
            "« $0$ est neutre dans $\\mathbb{R}^{+*}$ » : faux, $0\\notin\\mathbb{R}^{+*}$.",
            "« Une loi associative est commutative » : faux.",
            "« Un anneau commutatif est un corps » : faux.",
            "« $\\mathbb{Z}[i]$ est un corps » : faux.",
            "« $\\sqrt{x^2+y^2}=x+y$ » : faux.",
        ],
    )

st.markdown("## 5. Les 8 exercices en une ligne")

st.markdown(
    r"""
1. **Loi 1** : $x*y=\sqrt{x^2+y^2}$ sur $\mathbb{R}^+$ : commutative, associative, neutre $0$, mais aucun $x>0$ n'a de symétrique.
2. **Loi 2** : $x*y=xy+(x^2-1)(y^2-1)$ : commutative, neutre $1$, non associative.
3. **Exercice 2** : $(x,y)*(x',y')=(x+x',ye^{x'}+y'e^{-x})$ : groupe, neutre $(0,0)$, inverse $(-x,-y)$, non abélien.
4. **Exercice 3** : $(x,y)*(x',y')=(xx',xy'+y)$ : groupe affine, neutre $(1,0)$, inverse $(1/x,-y/x)$ ; $]0,\infty[\times\mathbb{R}$ est un sous-groupe.
5. **Exercice 4** : $(x,y)*(x',y')=(xx',xy'+x'y)$ : anneau commutatif unitaire, neutre $(1,0)$, diviseur de zéro $(0,1)$.
6. **Exercice 5** : $\mathbb{Q}(i)$ est un corps : inverse $(a-bi)/(a^2+b^2)$.
7. **Exercice 6** : $\mathcal{F}(\mathbb{R},\mathbb{R})$ est un anneau commutatif non intègre, donc pas un corps.
8. **Exercice 7** : $\mathbb{Z}[i]$ est un anneau commutatif, pas un corps ; unités $\pm1,\pm i$.
9. **Exercice 8** : $\mathbb{Q}[i]$ est un corps (preuve directe).
"""
)

st.markdown("## 6. Squelettes de rédaction")

encadre(
    "violet",
    "Groupe",
    texte=r"""
**Clôture.** Pour $x,y\in G$, $x*y\in G$ car …

**Associativité.** Pour $x,y,z\in G$, on calcule $(x*y)*z$ et $x*(y*z)$ ; on obtient …

**Neutre.** $e=…$ vérifie $e*x=x*e=x$.

**Inverse.** Pour $x\in G$, $x^{-1}=…$ vérifie $x*x^{-1}=x^{-1}*x=e$.

**Conclusion.** $(G,*)$ est un groupe.
""",
)

encadre(
    "violet",
    "Sous-groupe",
    texte=r"""
**Non vide.** $e\in H$.

**Stabilité.** Pour $x,y\in H$, $x*y\in H$ car …

**Inverse.** Pour $x\in H$, $x^{-1}\in H$ car …

**Conclusion.** $H$ est un sous-groupe de $G$.
""",
)

encadre(
    "violet",
    "Anneau",
    texte=r"""
**Groupe additif.** $(A,+)$ est un groupe abélien : neutre $0$, opposé $-x$.

**Multiplication.** $\times$ est associative.

**Distributivité.** Pour $a,b,c\in A$, $a(b+c)=ab+ac$ et $(a+b)c=ac+bc$.

**Conclusion.** $(A,+,\times)$ est un anneau. S'il est commutatif et a un $1$, c'est un anneau commutatif unitaire.
""",
)

encadre(
    "violet",
    "Corps",
    texte=r"""
**Anneau.** $(K,+,\times)$ est un anneau commutatif unitaire.

**Non nul.** $1\neq0$.

**Inverse.** Pour tout $x\in K\setminus\{0\}$, il existe $y\in K$ tel que $xy=1$ ; on l'exhibe.

**Conclusion.** $K$ est un corps.
""",
)

st.markdown("## 7. Les 10 réflexes du DS")

st.markdown(
    r"""
1. Je commence par écrire **l'ensemble** et **la loi**.
2. Je vérifie la **clôture** avant tout.
3. Pour une loi, je teste **commutativité**, **associativité**, **neutre**, **inverse** dans cet ordre.
4. Pour un groupe, je devine le neutre avant de l'exhiber.
5. Pour un sous-groupe, je vérifie **non vide + stable + inverse**.
6. Pour un anneau, je sépare **groupe additif** et **multiplication**.
7. Pour un corps, je cherche un **élément non inversible** pour prouver que ce n'en est pas un.
8. Pour une **non-associativité**, un triplet suffit ; pour l'associativité, il faut des lettres.
9. Je vérifie toujours **les deux côtés** de $x*x'=e$.
10. Je termine par une **phrase de conclusion** qui nomme la structure.
"""
)

st.write("")
st.info(
    "**Le jour du DS :** si tu bloques, reviens aux axiomes. Écris-les, puis regarde lequel tu n'as pas encore vérifié. "
    "C'est souvent celui qui manque."
)

pied_page()
