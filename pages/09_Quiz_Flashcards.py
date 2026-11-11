# -*- coding: utf-8 -*-
"""Quiz, cartes mémoire et jeu « trouve l'erreur » — Algèbre 1, TD 3."""

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
    pied_page,
    titre_page,
)

configurer_page("Quiz & cartes mémoire", "🧠")

titre_page(
    "Quiz, cartes mémoire et pièges",
    "Se tester sans regarder, puis vérifier. Trois modes : QCM, cartes à retourner, "
    "et affirmations à corriger.",
    "ALGÈBRE 1 · TD 3 · RÉVISION",
)

st.markdown(
    badge("15 QCM", "bleu") + badge("12 cartes", "vert") + badge("6 erreurs", "orange"),
    unsafe_allow_html=True,
)

onglets = st.tabs(["QCM", "Cartes mémoire", "Trouve l'erreur"])


# ---------------------------------------------------------------------------
# QCM
# ---------------------------------------------------------------------------
QUESTIONS = [
    {
        "q": "Une loi de composition interne sur E est une application…",
        "options": ["E → E", "E × E → E", "E × E → ℝ", "E → E × E"],
        "bonne": 1,
        "explication": "Elle prend deux éléments de E et rend un élément de E : c'est la clôture.",
    },
    {
        "q": "Dans un groupe, le neutre est…",
        "options": ["toujours 0", "toujours 1", "unique", "pas forcément unique"],
        "bonne": 2,
        "explication": "Si e et e' sont deux neutres, e = e*e' = e'. Il est donc unique.",
    },
    {
        "q": "La loi x∗y = √(x²+y²) sur ℝ⁺ est…",
        "options": ["seulement commutative", "commutative et associative", "un groupe", "non commutative"],
        "bonne": 1,
        "explication": "Elle est commutative et associative, de neutre 0, mais aucun x>0 n'a de symétrique.",
    },
    {
        "q": "La loi x∗y = xy + (x²−1)(y²−1) est…",
        "options": ["associative", "non associative", "un groupe", "non commutative"],
        "bonne": 1,
        "explication": "Elle est commutative, de neutre 1, mais (0∗0)∗2 = 2 et 0∗(0∗2) = −8.",
    },
    {
        "q": "Dans (ℝ², ∗) de l'exercice 2, le neutre est…",
        "options": ["(1,1)", "(0,0)", "(1,0)", "(0,1)"],
        "bonne": 1,
        "explication": "(x,y)∗(0,0) = (x, y e⁰ + 0) = (x,y).",
    },
    {
        "q": "Dans (ℝ², ∗) de l'exercice 2, l'inverse de (x,y) est…",
        "options": ["(−x,y)", "(x,−y)", "(−x,−y)", "(1/x,1/y)"],
        "bonne": 2,
        "explication": "La première coordonnée donne u=−x, puis la seconde v=−y.",
    },
    {
        "q": "Le groupe (H, ∗) de l'exercice 3 est…",
        "options": ["abélien", "non abélien", "pas un groupe", "fini"],
        "bonne": 1,
        "explication": "(2,0)∗(1,1) = (2,2) mais (1,1)∗(2,0) = (2,1).",
    },
    {
        "q": "Le sous-ensemble ]0,+∞[×ℝ de H est…",
        "options": ["un sous-groupe", "seulement stable par ∗", "pas stable par inverse", "vide"],
        "bonne": 0,
        "explication": "Il contient (1,0), est stable par ∗ et par inverse (1/x,−y/x) avec 1/x>0.",
    },
    {
        "q": "Dans l'anneau A = ℝ×ℝ de l'exercice 4, le neutre de ∗ est…",
        "options": ["(0,0)", "(1,0)", "(0,1)", "(1,1)"],
        "bonne": 1,
        "explication": "(x,y)∗(1,0) = (x, x·0 + y·1) = (x,y).",
    },
    {
        "q": "Dans A = ℝ×ℝ, l'élément (0,1) vérifie…",
        "options": ["(0,1)² = (0,1)", "(0,1)² = (0,0)", "(0,1)² = (1,0)", "(0,1) n'existe pas"],
        "bonne": 1,
        "explication": "(0,1)∗(0,1) = (0, 0·1+1·0) = (0,0). C'est un diviseur de zéro.",
    },
    {
        "q": "L'anneau F(ℝ,ℝ) est…",
        "options": ["intègre", "un corps", "commutatif mais non intègre", "non commutatif"],
        "bonne": 2,
        "explication": "Il est commutatif, mais f=max(0,x) et g=max(0,−x) sont non nulles et fg=0.",
    },
    {
        "q": "Dans Z[i], l'élément 2 est…",
        "options": ["inversible", "nul", "non inversible", "une unité"],
        "bonne": 2,
        "explication": "2(a+ib)=1 imposerait 2a=1, impossible dans Z. Z[i] n'est pas un corps.",
    },
    {
        "q": "Les unités de Z[i] sont…",
        "options": ["±1 seulement", "±1 et ±i", "tous les éléments de norme 2", "tous les éléments non nuls"],
        "bonne": 1,
        "explication": "Un élément est inversible si sa norme vaut 1 : a²+b²=1 donne (±1,0) et (0,±1).",
    },
    {
        "q": "Dans Q[i], l'inverse de 2+i est…",
        "options": ["2−i", "(2−i)/5", "(2+i)/5", "1/2 − i"],
        "bonne": 1,
        "explication": "1/(2+i) = (2−i)/(2²+1²) = (2−i)/5.",
    },
    {
        "q": "Un corps est toujours…",
        "options": ["fini", "intègre", "de caractéristique nulle", "un anneau non commutatif"],
        "bonne": 1,
        "explication": "Si xy=0 et x≠0, on multiplie par x⁻¹ et on trouve y=0.",
    },
]

st.markdown("### 15 questions")
st.caption("Choisis une réponse, puis clique sur « Corriger ». Les explications apparaissent en dessous.")

reponses = []
for i, question in enumerate(QUESTIONS):
    st.markdown(f"**{i + 1}. {question['q']}**")
    reponse = st.radio(
        "Ta réponse",
        question["options"],
        index=None,
        key=f"qcm_{i}",
        label_visibility="collapsed",
    )
    reponses.append(reponse)

if st.button("Corriger le QCM", type="primary", key="qcm_corriger"):
    score = 0
    for i, (question, reponse) in enumerate(zip(QUESTIONS, reponses)):
        bonne = question["options"][question["bonne"]]
        if reponse == bonne:
            score += 1
    st.success(f"Score : {score} / {len(QUESTIONS)}")
    for i, (question, reponse) in enumerate(zip(QUESTIONS, reponses)):
        bonne = question["options"][question["bonne"]]
        if reponse is None:
            st.warning(f"Question {i + 1} : pas de réponse. La bonne réponse est « {bonne} ».")
        elif reponse == bonne:
            st.success(f"Question {i + 1} : juste. {question['explication']}")
        else:
            st.error(f"Question {i + 1} : tu as répondu « {reponse} ». La bonne réponse est « {bonne} ». {question['explication']}")


# ---------------------------------------------------------------------------
# Cartes mémoire
# ---------------------------------------------------------------------------
CARTES = [
    ("Loi interne", "Une application ∗ : E×E → E. Le résultat reste dans E."),
    ("Commutativité", "∀x,y, x∗y = y∗x."),
    ("Associativité", "∀x,y,z, (x∗y)∗z = x∗(y∗z)."),
    ("Neutre", "∃e, ∀x, e∗x = x∗e = x. Il est unique."),
    ("Symétrique", "x∗x′ = x′∗x = e. Unique dans un groupe."),
    ("Groupe", "Loi interne + associative + neutre + inverse pour tous."),
    ("Groupe abélien", "Groupe + commutatif."),
    ("Sous-groupe", "H non vide, stable par ∗ et par inverse. Caractérisation : x∗y⁻¹ ∈ H."),
    ("Anneau", "(A,+) groupe abélien, × associative et distributive sur +."),
    ("Corps", "Anneau commutatif unitaire, 1≠0, tout élément non nul inversible."),
    ("Intègre", "Anneau commutatif sans diviseurs de zéro : xy=0 ⇒ x=0 ou y=0."),
    ("Z[i] vs Q[i]", "Z[i] : anneau, pas corps (2 n'est pas inversible). Q[i] : corps."),
]

st.markdown("### 12 cartes à retourner")
st.caption("Lis la notion, essaie de la définir à voix haute, puis retourne la carte.")

choix_carte = st.selectbox(
    "Choisir une carte",
    range(len(CARTES)),
    format_func=lambda i: CARTES[i][0],
    key="flash_choix",
)

if "flash_retour" not in st.session_state:
    st.session_state["flash_retour"] = False

col_g, col_d = st.columns([1, 1])
with col_g:
    if st.button("Retourner la carte", key="flash_btn"):
        st.session_state["flash_retour"] = not st.session_state["flash_retour"]
with col_d:
    st.caption("Le bouton alterne recto et verso.")

titre, dos = CARTES[choix_carte]
if st.session_state["flash_retour"]:
    encadre("vert", f"Verso — {titre}", texte=dos)
else:
    encadre("bleu", f"Recto — {titre}", texte="À toi de jouer : donne la définition exacte, puis retourne la carte.")


# ---------------------------------------------------------------------------
# Trouve l'erreur
# ---------------------------------------------------------------------------
ERREURS = [
    {
        "affirmation": "Dans un groupe, le neutre peut dépendre de l'élément.",
        "vrai": False,
        "correction": "Faux : le neutre est unique. Si e et e′ sont neutres, e = e∗e′ = e′.",
    },
    {
        "affirmation": "Une loi associative est forcément commutative.",
        "vrai": False,
        "correction": "Faux : la composition des permutations S3 est associative mais non commutative.",
    },
    {
        "affirmation": "Z[i] est un corps car il est contenu dans C.",
        "vrai": False,
        "correction": "Faux : être contenu dans un corps ne suffit pas. 2 n'a pas d'inverse dans Z[i].",
    },
    {
        "affirmation": "Dans F(R,R), deux fonctions non nulles peuvent avoir un produit nul.",
        "vrai": True,
        "correction": "Vrai : f=max(0,x) et g=max(0,−x) sont non nulles et fg=0.",
    },
    {
        "affirmation": "Un anneau commutatif unitaire est toujours un corps.",
        "vrai": False,
        "correction": "Faux : Z est un anneau commutatif unitaire, mais 2 n'y est pas inversible.",
    },
    {
        "affirmation": "Dans Q[i], l'inverse de a+bi est (a−bi)/(a²+b²).",
        "vrai": True,
        "correction": "Vrai : c'est le conjugué divisé par la norme au carré.",
    },
]

st.markdown("### 6 affirmations : vraies ou fausses ?")
st.caption("Choisis Vrai ou Faux, puis vérifie. Si c'est faux, corrige la phrase.")

for i, item in enumerate(ERREURS):
    st.markdown(f"**{i + 1}. {item['affirmation']}**")
    st.radio(
        "Ton verdict",
        ["Vrai", "Faux"],
        index=None,
        key=f"err_{i}",
        horizontal=True,
        label_visibility="collapsed",
    )

if st.button("Vérifier les affirmations", key="err_btn"):
    for i, item in enumerate(ERREURS):
        reponse = st.session_state.get(f"err_{i}")
        attendu = "Vrai" if item["vrai"] else "Faux"
        if reponse == attendu:
            st.success(f"{i + 1}. Exact. {item['correction']}")
        else:
            st.error(f"{i + 1}. Non : la bonne réponse est « {attendu} ». {item['correction']}")

pied_page()
