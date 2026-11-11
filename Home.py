# -*- coding: utf-8 -*-
"""
Home.py — accueil de la plateforme Algèbre 1 (TD 3).

Lancement :
    pip install -r requirements.txt
    streamlit run Home.py
"""

from __future__ import annotations

import textwrap
from pathlib import Path

import streamlit as st

from ui import (
    BLEU,
    ORANGE,
    VERT,
    VIOLET,
    carte_stat,
    configurer_page,
    lien_page,
    pied_page,
)

RACINE = Path(__file__).resolve().parent

configurer_page("Accueil", "🏠")


def _html(contenu: str) -> None:
    st.markdown(textwrap.dedent(contenu).strip(), unsafe_allow_html=True)


def _md_bloc(contenu: str) -> None:
    st.markdown(textwrap.dedent(contenu).strip())


with st.sidebar:
    st.markdown("### Algèbre 1 · CP1")
    st.caption("ENSA Marrakech · TD 3")
    st.markdown(
        "Utilise le menu **↑** pour ouvrir une page. "
        "Commence par la **Boîte à outils**, puis attaque les exercices."
    )
    st.markdown("---")
    st.caption("Règle d'or : une structure se vérifie axiome par axiome.")


# ---------------------------------------------------------------------------
# 1. Hero
# ---------------------------------------------------------------------------
_html(
    """
    <div class="hero">
        <div class="surtitre">ENSA Marrakech · CP1 · ALGÈBRE 1</div>
        <h1>Comprendre les structures,<br>pas les tables.</h1>
        <p>
            Une plateforme pour le TD 3 : <b>Vocabulaire des structures algébriques</b>.
            Pour chaque exercice : le sens de l'énoncé, une table ou un dessin,
            l'idée de la preuve, la preuve complète, du code pour vérifier,
            les erreurs à éviter et un moyen de retenir.
        </p>
        <span class="puce">8 exercices</span>
        <span class="puce">15 notions</span>
        <span class="puce">7 onglets par exercice</span>
        <span class="puce">quiz + cartes mémoire</span>
    </div>
    """
)

st.write("")


# ---------------------------------------------------------------------------
# 2. Chiffres clés
# ---------------------------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(carte_stat("8", "exercices du TD 3, un par page", BLEU), unsafe_allow_html=True)
with c2:
    st.markdown(carte_stat("15", "notions expliquées dans la boîte à outils", VERT), unsafe_allow_html=True)
with c3:
    st.markdown(carte_stat("7", "onglets pour ne jamais sauter une étape", VIOLET), unsafe_allow_html=True)
with c4:
    st.markdown(carte_stat("0", "table à apprendre par cœur", ORANGE), unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# 3. Méthode
# ---------------------------------------------------------------------------
st.subheader("Comment utiliser la plateforme")
st.markdown(
    "Chaque page suit le même chemin. L'ordre compte : comprendre, manipuler, "
    "prouver, vérifier, puis restituer."
)

m1, m2, m3 = st.columns(3)
with m1:
    _html(
        """
        <div class="carte">
            <div style="color:#8ab4ff;font-size:.72rem;letter-spacing:.14em;">ÉTAPE 1</div>
            <div style="font-size:1.05rem;font-weight:700;margin:.25rem 0 .35rem 0;">Je comprends</div>
            <div style="color:#aeb8c6;font-size:.88rem;">
                Je repère l'ensemble, la loi, le neutre et ce qu'on me demande
                exactement. Je réécris l'énoncé avec mes mots.
            </div>
        </div>
        """
    )
with m2:
    _html(
        """
        <div class="carte">
            <div style="color:#7ee787;font-size:.72rem;letter-spacing:.14em;">ÉTAPE 2</div>
            <div style="font-size:1.05rem;font-weight:700;margin:.25rem 0 .35rem 0;">Je manipule</div>
            <div style="color:#aeb8c6;font-size:.88rem;">
                Je teste la loi sur des petits nombres, je regarde la table,
                je cherche un contre-exemple avant de rédiger.
            </div>
        </div>
        """
    )
with m3:
    _html(
        """
        <div class="carte">
            <div style="color:#d2b3ff;font-size:.72rem;letter-spacing:.14em;">ÉTAPE 3</div>
            <div style="font-size:1.05rem;font-weight:700;margin:.25rem 0 .35rem 0;">Je restitue</div>
            <div style="color:#aeb8c6;font-size:.88rem;">
                Je ferme l'écran et je réécris les axiomes et la preuve.
                Je compare, je corrige, je recommence demain.
            </div>
        </div>
        """
    )

st.write("")
st.info(
    "**La règle des 3 passages.** 1) Je lis pour comprendre. "
    "2) Je refais en ne regardant que les titres des étapes. "
    "3) Je rédige seul, comme en DS. Si le passage 3 bloque, c'est exactement "
    "l'endroit à retravailler."
)


# ---------------------------------------------------------------------------
# 4. Les sept onglets et le code couleur
# ---------------------------------------------------------------------------
st.subheader("Les 7 onglets d'une page d'exercice")

g1, g2 = st.columns([1.15, 1], gap="large")
with g1:
    _md_bloc(
        """
        1. **Comprendre l'énoncé** — la version simple, les données, le but.
        2. **Intuition** — une table de Cayley, un dessin ou un contre-exemple animé.
        3. **Comment trouver l'idée** — le réflexe du prof, pas seulement la solution.
        4. **Preuve complète pas à pas** — chaque axiome vérifié, chaque calcul justifié.
        5. **Vérifier avec du code** — Python et SymPy pour contrôler les calculs.
        6. **Erreurs à éviter** — les pièges classiques du devoir.
        7. **À retenir** — un squelette de preuve et 3 questions pour se tester.
        """
    )
with g2:
    _html(
        """
        <div class="carte" style="border-left:5px solid #4c8dff;">
            <b style="color:#9cc0ff;">Bleu</b> — l'intuition, l'image mentale.
        </div><br>
        <div class="carte" style="border-left:5px solid #3fb950;">
            <b style="color:#7ee787;">Vert</b> — un exemple, une étape de preuve.
        </div><br>
        <div class="carte" style="border-left:5px solid #f0883e;">
            <b style="color:#ffb077;">Orange</b> — une erreur fréquente, un contre-exemple.
        </div><br>
        <div class="carte" style="border-left:5px solid #bc8cff;">
            <b style="color:#d2b3ff;">Violet</b> — ce qu'il faut absolument retenir.
        </div>
        """
    )


# ---------------------------------------------------------------------------
# 5. Feuille de route
# ---------------------------------------------------------------------------
st.subheader("La feuille de route du TD 3")
st.caption(
    "TD 3 : Vocabulaire des structures algébriques · Algèbre 1 · CP1 ENSA Marrakech · Pr. Laila Taourirte"
)

st.warning(
    "**Attention à l'exercice 1.** L'énoncé écrit $\\mathbb{R}^{+*}$ mais demande de montrer que "
    "$0$ est neutre. Or $0\\notin\\mathbb{R}^{+*}$ : c'est incompatible. "
    "L'interprétation cohérente est $\\mathbb{R}_+=[0,+\\infty[$. "
    "La page de l'exercice 1 explique ce point en détail."
)

EXERCICES = [
    {
        "fichier": "01_Ex1.py",
        "titre": "La loi √(x² + y²)",
        "notions": "Loi interne · commutativité · associativité · neutre · symétrique",
        "resume": "Deux lois sur R : une qui ressemble à une norme, une qui cache un défaut d'associativité.",
    },
    {
        "fichier": "02_Ex2.py",
        "titre": "Le groupe (R², ∗)",
        "notions": "Groupe · associativité · inverse · non-commutativité",
        "resume": "Une loi qui mélange translation et dilatation : le groupe est non abélien.",
    },
    {
        "fichier": "03_Ex3.py",
        "titre": "Le groupe affine H",
        "notions": "Groupe · transformations affines · sous-groupe",
        "resume": "Composer x t + y : le modèle concret du groupe non commutatif.",
    },
    {
        "fichier": "04_Ex4.py",
        "titre": "L'anneau des nombres duaux",
        "notions": "Anneau · distributivité · élément neutre · diviseurs de zéro",
        "resume": "R × R avec (x,y)∗(x′,y′)=(xx′,xy′+x′y) : un anneau, mais pas un corps.",
    },
    {
        "fichier": "05_Ex5.py",
        "titre": "Le corps Q(i)",
        "notions": "Groupe additif · groupe multiplicatif · corps",
        "resume": "Les complexes à coordonnées rationnelles : on peut y diviser.",
    },
    {
        "fichier": "06_Ex6.py",
        "titre": "L'anneau F(R,R)",
        "notions": "Anneau de fonctions · intégrité · corps",
        "resume": "Deux fonctions non nulles peuvent avoir un produit nul : pas de corps.",
    },
    {
        "fichier": "07_Ex7.py",
        "titre": "Les entiers de Gauss Z[i]",
        "notions": "Sous-anneau de C · unités · anneau non corps",
        "resume": "Un réseau de points dans le plan complexe ; 2 n'y a pas d'inverse.",
    },
    {
        "fichier": "08_Ex8.py",
        "titre": "Le corps Q[i]",
        "notions": "Corps · inverse · sous-corps de C",
        "resume": "La même idée que Q(i), mais on prouve directement la structure de corps.",
    },
]

colonne_gauche, colonne_droite = st.columns(2, gap="large")
for indice, exo in enumerate(EXERCICES):
    colonne = colonne_gauche if indice % 2 == 0 else colonne_droite
    chemin = f"pages/{exo['fichier']}"
    disponible = (RACINE / chemin).exists()
    with colonne:
        statut = (
            '<span class="statut ok">disponible</span>'
            if disponible
            else '<span class="statut">en préparation</span>'
        )
        _html(
            f"""
            <div class="carte-exo">
                <div class="num">Exercice {indice + 1}</div>
                <div class="titre">{exo['titre']}</div>
                <div class="notions">{exo['notions']}</div>
                <div style="color:#c9d3e0;font-size:.86rem;margin-top:.45rem;">{exo['resume']}</div>
                {statut}
            </div>
            """
        )
        if disponible:
            lien_page(chemin, "Ouvrir l'exercice →")
        else:
            st.caption("Bientôt disponible.")
        st.write("")


# ---------------------------------------------------------------------------
# 6. Outils transversaux
# ---------------------------------------------------------------------------
st.subheader("Les outils transversaux")

outils = [
    {
        "fichier": "pages/00_Toolbox.py",
        "titre": "Boîte à outils",
        "texte": "Les 15 notions du TD, avec une table, un exemple et un contre-exemple pour chacune.",
        "couleur": BLEU,
    },
    {
        "fichier": "pages/09_Quiz_Flashcards.py",
        "titre": "Quiz & cartes mémoire",
        "texte": "QCM, flashcards et jeu « trouve l'erreur » pour réviser autrement.",
        "couleur": VERT,
    },
    {
        "fichier": "pages/10_Cheat_Sheet.py",
        "titre": "Fiche de synthèse",
        "texte": "Tous les axiomes, les méthodes et les contre-exemples sur une page.",
        "couleur": VIOLET,
    },
]

outil_cols = st.columns(3, gap="large")
for colonne, outil in zip(outil_cols, outils):
    with colonne:
        _html(
            f"""
            <div class="carte" style="border-left:5px solid {outil['couleur']};">
                <div style="font-size:1.02rem;font-weight:750;margin-bottom:.35rem;">{outil['titre']}</div>
                <div style="color:#aeb8c6;font-size:.87rem;">{outil['texte']}</div>
            </div>
            """
        )
        if (RACINE / outil["fichier"]).exists():
            lien_page(outil["fichier"], "Ouvrir →")
        else:
            st.caption("En préparation.")


# ---------------------------------------------------------------------------
# 7. Progression
# ---------------------------------------------------------------------------
st.subheader("Ma progression")

OBJECTIFS = [
    ("alg_prog_toolbox", "J'ai parcouru les 15 notions de la boîte à outils"),
    ("alg_prog_ex1", "Ex 1 — je sais expliquer le piège de R^{+*} et le défaut d'associativité"),
    ("alg_prog_ex2", "Ex 2 — je sais prouver que (R², ∗) est un groupe non abélien"),
    ("alg_prog_ex3", "Ex 3 — je sais montrer que H est un groupe et que ]0,∞[×R est un sous-groupe"),
    ("alg_prog_ex4", "Ex 4 — je sais vérifier les axiomes d'anneau et trouver un diviseur de zéro"),
    ("alg_prog_ex5", "Ex 5 — je sais montrer que Q(i) est un corps"),
    ("alg_prog_ex6", "Ex 6 — je sais prouver que F(R,R) n'est ni intègre ni un corps"),
    ("alg_prog_ex7", "Ex 7 — je sais montrer que Z[i] est un anneau mais pas un corps"),
    ("alg_prog_ex8", "Ex 8 — je sais prouver directement que Q[i] est un corps"),
    ("alg_prog_quiz", "J'ai fait le quiz et les cartes mémoire"),
    ("alg_prog_cheat", "J'ai relu la fiche de synthèse"),
]


def reinitialiser_progression() -> None:
    for cle, _ in OBJECTIFS:
        if cle in st.session_state:
            st.session_state[cle] = False


cases_gauche, cases_droite = st.columns(2, gap="large")
for index, (cle, libelle) in enumerate(OBJECTIFS):
    colonne = cases_gauche if index % 2 == 0 else cases_droite
    with colonne:
        st.checkbox(libelle, key=cle)

faits = sum(1 for cle, _ in OBJECTIFS if st.session_state.get(cle, False))
st.progress(faits / len(OBJECTIFS), text=f"{faits} / {len(OBJECTIFS)} objectifs cochés")
st.button("Réinitialiser ma progression", on_click=reinitialiser_progression)
st.caption("La progression est gardée pendant la session ; elle repart de zéro après un rechargement complet.")


# ---------------------------------------------------------------------------
# 8. Plan et installation
# ---------------------------------------------------------------------------
with st.expander("Un plan de travail sur 7 jours"):
    _md_bloc(
        """
        **Jour 1 — Les axiomes.** Boîte à outils : loi interne, commutativité,
        associativité, neutre, symétrique. Puis exercice 1.

        **Jour 2 — Groupes.** Exercices 2 et 3 : (R², ∗), puis le groupe affine H.

        **Jour 3 — Anneaux.** Exercice 4 : vérifier les axiomes, chercher les diviseurs de zéro.

        **Jour 4 — Corps.** Exercice 5 : Q(i), puis exercice 8 pour consolider.

        **Jour 5 — Fonctions et intégrité.** Exercice 6 : F(R,R).

        **Jour 6 — Anneaux de nombres.** Exercice 7 : Z[i], unités et norme.

        **Jour 7 — Restitution.** Quiz, cartes mémoire, fiche de synthèse.
        Tu réécris les squelettes de preuve de mémoire.
        """
    )

with st.expander("Installer et lancer la plateforme"):
    _md_bloc(
        """
        Dans un terminal, place-toi dans le dossier du projet, puis :

        ```bash
        pip install -r requirements.txt
        streamlit run Home.py
        ```

        Il faut Python 3.10 ou plus récent.
        """
    )


# ---------------------------------------------------------------------------
# 9. Conseil final
# ---------------------------------------------------------------------------
st.write("")
_html(
    """
    <div class="carte" style="border-left:5px solid #bc8cff;">
        <div style="font-size:1.05rem;font-weight:750;color:#d2b3ff;margin-bottom:.35rem;">
            Le conseil du prof
        </div>
        <div style="color:#c9d3e0;font-size:.95rem;">
            En algèbre, une preuve n'est presque jamais un calcul compliqué :
            c'est une <i>vérification d'axiomes</i> faite dans le bon ordre.
            Si tu sais dire quel axiome tu vérifies et pourquoi il est nécessaire,
            tu peux reconstruire toute la preuve.
        </div>
    </div>
    """
)

pied_page()
