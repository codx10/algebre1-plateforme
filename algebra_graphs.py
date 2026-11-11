# -*- coding: utf-8 -*-
"""
algebra_graphs.py — les visualisations interactives de la plateforme Algèbre 1.

On y trouve :
  * des tables de Cayley pour lire une loi de composition ;
  * des expériences numériques pour l'associativité, le neutre, les inverses ;
  * des dessins pour les groupes de transformations et les anneaux de nombres.

Comme pour le TD d'analyse, chaque fonction affiche ses curseurs, construit une
figure Plotly et ajoute une phrase de lecture.
"""

from __future__ import annotations

from itertools import product

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from ui import (
    BLEU,
    GRIS,
    ORANGE,
    ROUGE,
    VERT,
    VIOLET,
    base_figure,
    graphique,
)


# ---------------------------------------------------------------------------
# 0. Petits utilitaires
# ---------------------------------------------------------------------------
Z6 = list(range(6))
LABELS_Z6 = [str(k) for k in Z6]


def add_mod6(a: int, b: int) -> int:
    return (a + b) % 6


def mul_mod6(a: int, b: int) -> int:
    return (a * b) % 6


S3 = [
    (0, 1, 2),
    (0, 2, 1),
    (1, 0, 2),
    (1, 2, 0),
    (2, 0, 1),
    (2, 1, 0),
]
LABELS_S3 = ["e", "a", "b", "c", "d", "f"]


def compose_permutations(p: tuple[int, int, int], q: tuple[int, int, int]) -> tuple[int, int, int]:
    """Renvoie p∘q : on applique q, puis p."""
    return tuple(p[q[i]] for i in range(3))


def _table_cayley(
    elements,
    operation,
    labels: list[str],
    titre: str,
    hauteur: int = 440,
    neutre=None,
    sous_groupe=None,
    cellule=None,
) -> go.Figure:
    """Construit une table de Cayley colorée.

    `z` code l'indice du résultat : la couleur sert seulement à repérer les
    paquets de résultats identiques. Le texte affiché est le vrai résultat.
    """
    n = len(elements)
    position = {element: i for i, element in enumerate(elements)}
    z, textes = [], []
    for x in elements:
        ligne_z, ligne_txt = [], []
        for y in elements:
            resultat = operation(x, y)
            if resultat not in position:
                raise ValueError(f"Résultat hors de l'ensemble : {resultat}")
            ligne_z.append(position[resultat])
            ligne_txt.append(labels[position[resultat]])
        z.append(ligne_z)
        textes.append(ligne_txt)

    fig = base_figure(titre, hauteur=hauteur)
    positions = list(range(n))
    fig.add_trace(
        go.Heatmap(
            z=z,
            x=positions,
            y=positions,
            text=textes,
            texttemplate="%{text}",
            textfont=dict(size=13, color="#f2f6fb"),
            colorscale=[
                [0.0, "#12233d"],
                [0.5, "#1c3d6b"],
                [1.0, "#2f6fbe"],
            ],
            showscale=False,
            hovertemplate="%{text}<extra></extra>",
        )
    )
    fig.update_xaxes(
        side="top", title="", tickmode="array",
        tickvals=positions, ticktext=labels,
    )
    fig.update_yaxes(
        autorange="reversed", title="", tickmode="array",
        tickvals=positions, ticktext=labels,
    )
    fig.update_layout(height=hauteur, margin=dict(l=10, r=10, t=75, b=10))

    if neutre is not None:
        i = position[neutre]
        fig.add_shape(
            type="rect", x0=-0.5, x1=n - 0.5, y0=i - 0.5, y1=i + 0.5,
            line=dict(color=VERT, width=3),
        )
        fig.add_shape(
            type="rect", x0=i - 0.5, x1=i + 0.5, y0=-0.5, y1=n - 0.5,
            line=dict(color=VERT, width=3),
        )

    if sous_groupe:
        indices = [position[element] for element in sous_groupe]
        for i in indices:
            fig.add_shape(
                type="rect", x0=-0.5, x1=n - 0.5, y0=i - 0.5, y1=i + 0.5,
                line=dict(color=VIOLET, width=2),
                fillcolor="rgba(188,140,255,0.10)",
                layer="above",
            )
            fig.add_shape(
                type="rect", x0=i - 0.5, x1=i + 0.5, y0=-0.5, y1=n - 0.5,
                line=dict(color=VIOLET, width=2),
                fillcolor="rgba(188,140,255,0.10)",
                layer="above",
            )

    if cellule is not None:
        i, j = cellule
        fig.add_shape(
            type="rect", x0=j - 0.5, x1=j + 0.5, y0=i - 0.5, y1=i + 0.5,
            line=dict(color=ORANGE, width=4),
            fillcolor="rgba(240,136,62,0.12)",
            layer="above",
        )

    return fig


# ---------------------------------------------------------------------------
# 1. Loi de composition : la surface qui montre le résultat
# ---------------------------------------------------------------------------
def g_loi_ex1() -> None:
    choix = st.radio(
        "Quelle loi veux-tu voir ?",
        [
            "1) x ∗ y = √(x² + y²)",
            "2) x ∗ y = xy + (x² − 1)(y² − 1)",
        ],
        key="alg_g_loi_choix",
    )

    col_g, col_d = st.columns([2.2, 1], gap="large")
    with col_d:
        if choix.startswith("1"):
            x0 = st.slider("x", 0.0, 3.0, 1.2, 0.1, key="alg_g_loi_x1")
            y0 = st.slider("y", 0.0, 3.0, 0.8, 0.1, key="alg_g_loi_y1")
            grille = np.linspace(0, 3, 70)
            X, Y = np.meshgrid(grille, grille)
            Z = np.sqrt(X ** 2 + Y ** 2)
            z0 = float(np.sqrt(x0 ** 2 + y0 ** 2))
            titre = "Loi 1 : le résultat est la distance à l'origine"
        else:
            x0 = st.slider("x", -2.0, 2.0, 0.7, 0.1, key="alg_g_loi_x2")
            y0 = st.slider("y", -2.0, 2.0, 0.4, 0.1, key="alg_g_loi_y2")
            grille = np.linspace(-2, 2, 70)
            X, Y = np.meshgrid(grille, grille)
            Z = X * Y + (X ** 2 - 1) * (Y ** 2 - 1)
            z0 = float(x0 * y0 + (x0 ** 2 - 1) * (y0 ** 2 - 1))
            titre = "Loi 2 : une surface plus cabossée"

    with col_g:
        fig = go.Figure()
        fig.add_trace(
            go.Surface(
                x=grille, y=grille, z=Z,
                colorscale="Blues",
                opacity=0.88,
                showscale=False,
                name="x ∗ y",
            )
        )
        fig.add_trace(
            go.Scatter3d(
                x=[x0], y=[y0], z=[z0],
                mode="markers",
                marker=dict(size=7, color=ORANGE),
                name=f"({x0:.1f}, {y0:.1f}) ↦ {z0:.2f}",
            )
        )
        fig.update_layout(
            height=460,
            margin=dict(l=0, r=0, t=55, b=0),
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#c9d1d9"),
            title=dict(text=titre, x=0.01, font=dict(size=15, color="#e6edf3")),
            scene=dict(
                xaxis=dict(title="x", gridcolor="rgba(255,255,255,0.08)"),
                yaxis=dict(title="y", gridcolor="rgba(255,255,255,0.08)"),
                zaxis=dict(title="x ∗ y", gridcolor="rgba(255,255,255,0.08)"),
                bgcolor="rgba(0,0,0,0)",
            ),
            legend=dict(orientation="h", y=1.02, x=0, bgcolor="rgba(0,0,0,0)"),
        )
        graphique(fig)

    if choix.startswith("1"):
        st.info(
            "La surface ne dépend que de la distance √(x²+y²) : elle est symétrique "
            "en x et y, donc la loi est commutative. Le point (0,0) donne exactement x "
            "ou y : 0 est neutre. Mais pour x > 0, aucun y ne peut donner 0."
        )
    else:
        st.info(
            "La surface est symétrique par rapport au plan x = y : la loi est commutative. "
            "Le point (1,1) est à la hauteur 1, et la surface passe par 0 en (0,0) : "
            "1 est neutre. En revanche, elle n'est pas plate le long des diagonales, "
            "ce qui annonce le défaut d'associativité."
        )


# ---------------------------------------------------------------------------
# 2. Associativité : (x∗y)∗z contre x∗(y∗z)
# ---------------------------------------------------------------------------
def g_associativite() -> None:
    choix = st.radio(
        "Quelle loi ?",
        [
            "x ∗ y = xy + (x² − 1)(y² − 1)",
            "x ∗ y = x − y (soustraction sur Z)",
        ],
        key="alg_g_assoc_choix",
    )
    col_g, col_d = st.columns([2.2, 1], gap="large")
    with col_d:
        x = st.slider("x", -3, 3, 0, 1, key="alg_g_assoc_x")
        y = st.slider("y", -3, 3, 1, 1, key="alg_g_assoc_y")
        z = st.slider("z", -3, 3, 0, 1, key="alg_g_assoc_z")

    if choix.startswith("x ∗ y = xy"):
        def loi(a, b):
            return a * b + (a ** 2 - 1) * (b ** 2 - 1)
    else:
        def loi(a, b):
            return a - b

    gauche = loi(loi(x, y), z)
    droite = loi(x, loi(y, z))

    with col_g:
        fig = base_figure("Associativité : les deux parenthésages donnent-ils le même résultat ?")
        fig.add_trace(
            go.Bar(
                x=["(x ∗ y) ∗ z", "x ∗ (y ∗ z)"],
                y=[gauche, droite],
                text=[str(gauche), str(droite)],
                textposition="outside",
                marker_color=[BLEU, VERT if gauche == droite else ORANGE],
                width=0.5,
            )
        )
        fig.update_yaxes(title="valeur")
        fig.update_layout(showlegend=False)
        graphique(fig)

    if gauche == droite:
        st.success(f"Pour ce triplet, les deux parenthésages donnent {gauche}. Cela ne prouve pas l'associativité : il faut le montrer pour tous x, y, z.")
    else:
        st.error(f"Contre-exemple : (x∗y)∗z = {gauche}, alors que x∗(y∗z) = {droite}. La loi n'est pas associative.")

    if st.button("Chercher un contre-exemple dans [−2, 2]", key="alg_g_assoc_bouton"):
        trouve = None
        for a, b, c in product(range(-2, 3), repeat=3):
            if loi(loi(a, b), c) != loi(a, loi(b, c)):
                trouve = (a, b, c, loi(loi(a, b), c), loi(a, loi(b, c)))
                break
        if trouve:
            a, b, c, g, d = trouve
            st.warning(f"Trouvé : x={a}, y={b}, z={c} donne {g} à gauche et {d} à droite.")
        else:
            st.info("Aucun contre-exemple sur cette grille. Pour la soustraction, essaie x=0, y=0, z=1.")


# ---------------------------------------------------------------------------
# 3. Tables de Cayley : commutativité, neutre, inverse, groupe
# ---------------------------------------------------------------------------
def g_commutativite() -> None:
    choix = st.radio(
        "Quelle table ?",
        ["Addition dans Z/6Z", "Composition dans S3"],
        key="alg_g_comm_choix",
    )
    if choix.startswith("Addition"):
        elements, labels = Z6, LABELS_Z6
        operation = add_mod6
        titre = "Table de l'addition dans Z/6Z"
    else:
        elements, labels = S3, LABELS_S3
        operation = compose_permutations
        titre = "Table de la composition dans S3"

    fig = _table_cayley(elements, operation, labels, titre, hauteur=480)
    graphique(fig)

    if choix.startswith("Addition"):
        st.success("La table est symétrique par rapport à la diagonale : la loi est commutative.")
    else:
        difference = None
        for i, a in enumerate(elements):
            for j, b in enumerate(elements):
                if operation(a, b) != operation(b, a):
                    difference = (labels[i], labels[j])
                    break
            if difference:
                break
        if difference:
            i, j = difference
            st.error(f"La table n'est pas symétrique : {i}∘{j} ≠ {j}∘{i}. S3 n'est pas commutatif.")
        else:
            st.success("La table est symétrique.")


def g_neutre() -> None:
    choix = st.radio(
        "Quelle loi ?",
        ["Addition dans Z/6Z", "Multiplication dans Z/6Z"],
        key="alg_g_neutre_choix",
    )
    if choix.startswith("Addition"):
        elements, labels = Z6, LABELS_Z6
        operation, neutre, titre = add_mod6, 0, "Le neutre de l'addition dans Z/6Z"
    else:
        elements, labels = Z6, LABELS_Z6
        operation, neutre, titre = mul_mod6, 1, "Le neutre de la multiplication dans Z/6Z"

    fig = _table_cayley(elements, operation, labels, titre, hauteur=460, neutre=neutre)
    graphique(fig)
    st.success(
        f"La ligne et la colonne de {neutre} sont surlignées en vert. "
        f"On lit : {neutre} ∗ x = x et x ∗ {neutre} = x pour tout x. "
        "Le neutre est unique dans un groupe."
    )


def g_symetrique() -> None:
    choix = st.radio(
        "Quelle loi ?",
        ["Addition dans Z/6Z", "Composition dans S3"],
        key="alg_g_sym_choix",
    )
    if choix.startswith("Addition"):
        elements, labels = Z6, LABELS_Z6
        operation = add_mod6
        neutre = 0
        titre = "Chercher le symétrique dans Z/6Z"
    else:
        elements, labels = S3, LABELS_S3
        operation = compose_permutations
        neutre = (0, 1, 2)
        titre = "Chercher l'inverse dans S3"

    element = st.selectbox("Élément x", elements, format_func=lambda e: labels[elements.index(e)], key="alg_g_sym_element")
    i = elements.index(element)
    j = None
    for k, y in enumerate(elements):
        if operation(element, y) == neutre and operation(y, element) == neutre:
            j = k
            break

    fig = _table_cayley(
        elements, operation, labels, titre, hauteur=460,
        neutre=neutre, cellule=(i, j) if j is not None else None,
    )
    graphique(fig)

    if j is None:
        st.error(f"{labels[i]} n'a pas de symétrique : la loi n'est pas un groupe.")
    else:
        st.success(
            f"Le symétrique de {labels[i]} est {labels[j]} : la case orange contient le neutre. "
            "Dans un groupe, tout élément a un symétrique unique."
        )


def g_groupe() -> None:
    choix = st.radio(
        "Quelle structure ?",
        [
            "Z/6Z avec l'addition",
            "Z/6Z avec la multiplication",
            "S3 avec la composition",
        ],
        key="alg_g_groupe_choix",
    )
    if choix.startswith("Z/6Z avec l'addition"):
        elements, labels = Z6, LABELS_Z6
        operation, titre = add_mod6, "Z/6Z, + : un groupe"
        verdict = "groupe"
    elif "multiplication" in choix:
        elements, labels = Z6, LABELS_Z6
        operation, titre = mul_mod6, "Z/6Z, × : ce n'est pas un groupe"
        verdict = "pas groupe"
    else:
        elements, labels = S3, LABELS_S3
        operation, titre = compose_permutations, "S3, ∘ : un groupe non commutatif"
        verdict = "groupe"

    fig = _table_cayley(elements, operation, labels, titre, hauteur=470)
    graphique(fig)

    if verdict == "groupe":
        st.success(
            "Clôture : la table ne sort pas de l'ensemble. Associativité : elle est héritée "
            "de la composition. Neutre : la ligne du neutre recopie les étiquettes. "
            "Inverse : chaque ligne contient le neutre. C'est un groupe."
        )
    else:
        st.error(
            "La multiplication dans Z/6Z n'est pas un groupe : 0 n'a pas d'inverse, "
            "et 2, 3, 4 non plus. La table contient des lignes sans le neutre 1."
        )


def g_sous_groupe() -> None:
    choix = st.radio(
        "Quel sous-ensemble H de Z/6Z ?",
        ["H = {0, 3}", "H = {0, 2, 4}"],
        key="alg_g_sg_choix",
    )
    H = [0, 3] if "0, 3" in choix else [0, 2, 4]
    fig = _table_cayley(
        Z6, add_mod6, LABELS_Z6,
        f"Le sous-ensemble H = {H} est-il un sous-groupe ?",
        hauteur=450, sous_groupe=H,
    )
    graphique(fig)

    stable = all(add_mod6(x, y) in H for x in H for y in H)
    inverse = all(any(add_mod6(x, y) == 0 for y in H) for x in H)
    if stable and inverse:
        st.success(
            f"H = {H} contient 0, est stable par addition et contient l'opposé de chacun "
            "de ses éléments : c'est un sous-groupe."
        )
    else:
        st.error(f"H = {H} n'est pas stable ou ne contient pas tous les opposés : ce n'est pas un sous-groupe.")

    st.markdown("**La table interne de H :**")
    st.dataframe(
        {f"∗ {y}": [add_mod6(x, y) for x in H] for y in H},
        hide_index=True,
    )


# ---------------------------------------------------------------------------
# 4. Anneau, distributivité, corps
# ---------------------------------------------------------------------------
def g_anneau() -> None:
    col_g, col_d = st.columns([2.2, 1], gap="large")
    with col_d:
        a = st.slider("a", -2.0, 2.0, 1.0, 0.1, key="alg_g_ann_a")
        b = st.slider("b", -2.0, 2.0, 0.5, 0.1, key="alg_g_ann_b")
        c = st.slider("c", -2.0, 2.0, 0.7, 0.1, key="alg_g_ann_c")
        d = st.slider("d", -2.0, 2.0, -0.3, 0.1, key="alg_g_ann_d")

    produit = (a * c, a * d + b * c)
    with col_g:
        st.latex(
            r"\begin{pmatrix} a & b \\ 0 & a\end{pmatrix}"
            r"\begin{pmatrix} c & d \\ 0 & c\end{pmatrix}"
            r"="
            r"\begin{pmatrix} ac & ad+bc \\ 0 & ac\end{pmatrix}"
        )
        st.latex(
            rf"\begin{{pmatrix}} {a:.1f} & {b:.1f} \\ 0 & {a:.1f}\end{{pmatrix}}"
            rf"\begin{{pmatrix}} {c:.1f} & {d:.1f} \\ 0 & {c:.1f}\end{{pmatrix}}"
            rf"=\begin{{pmatrix}} {produit[0]:.2f} & {produit[1]:.2f} \\ 0 & {produit[0]:.2f}\end{{pmatrix}}"
        )
        st.info(
            "Chaque couple (x, y) se représente par une matrice triangulaire. "
            "La multiplication des matrices redonne exactement la loi ∗ de l'exercice 4."
        )

    x, y = 1.0, 1.0
    carre = (x * x, x * y + y * x)
    st.markdown("**Un phénomène important : les diviseurs de zéro.**")
    st.latex(r"(0,1)*(0,1)=(0,0)")
    st.warning(
        "Le couple (0,1) est non nul, mais son carré est nul. Donc (A, +, ∗) "
        "n'est pas un corps : un corps n'a pas de diviseurs de zéro."
    )


def g_distributivite() -> None:
    col_g, col_d = st.columns([2.2, 1], gap="large")
    with col_d:
        a = st.slider("a", 0, 5, 2, 1, key="alg_g_dist_a")
        b = st.slider("b", 0, 5, 3, 1, key="alg_g_dist_b")
        c = st.slider("c", 0, 5, 4, 1, key="alg_g_dist_c")
    gauche = mul_mod6(a, add_mod6(b, c))
    droite = add_mod6(mul_mod6(a, b), mul_mod6(a, c))
    with col_g:
        fig = base_figure("Distributivité dans Z/6Z : a × (b + c) = a×b + a×c")
        fig.add_trace(
            go.Bar(
                x=["a × (b + c)", "a×b + a×c"],
                y=[gauche, droite],
                text=[str(gauche), str(droite)],
                textposition="outside",
                marker_color=[BLEU, VERT if gauche == droite else ORANGE],
                width=0.45,
            )
        )
        fig.update_yaxes(title="reste modulo 6")
        fig.update_layout(showlegend=False)
        graphique(fig)
    if gauche == droite:
        st.success(f"{a} × ({b}+{c}) ≡ {gauche} mod 6 et {a}×{b} + {a}×{c} ≡ {droite} mod 6. La distributivité fonctionne.")
    else:
        st.error("La distributivité échoue : ce n'est pas un anneau.")


def g_corps() -> None:
    col_g, col_d = st.columns([2.2, 1], gap="large")
    with col_d:
        a = st.slider("Partie réelle a", -3.0, 3.0, 1.0, 0.1, key="alg_g_corps_a")
        b = st.slider("Partie imaginaire b", -3.0, 3.0, 0.5, 0.1, key="alg_g_corps_b")

    norme = a * a + b * b
    if norme == 0:
        with col_g:
            st.error("z = 0 n'est pas inversible : un corps exclut zéro pour la multiplication.")
        return

    inv_a, inv_b = a / norme, -b / norme
    with col_g:
        fig = base_figure("Dans Q[i], tout élément non nul a un inverse")
        fig.add_trace(go.Scatter(x=[0, a], y=[0, b], mode="lines+markers", name="z",
                                 line=dict(color=BLEU, width=2), marker=dict(size=8)))
        fig.add_trace(go.Scatter(x=[0, inv_a], y=[0, inv_b], mode="lines+markers", name="1/z",
                                 line=dict(color=ORANGE, width=2), marker=dict(size=8)))
        fig.add_trace(go.Scatter(x=[a, inv_a], y=[b, inv_b], mode="lines", name="produit = 1",
                                 line=dict(color=VERT, width=1.5, dash="dot")))
        fig.add_trace(go.Scatter(x=[1], y=[0], mode="markers", name="1",
                                 marker=dict(color=VERT, size=13, symbol="star")))
        fig.update_xaxes(range=[-3.5, 3.5], title="partie réelle", zeroline=True)
        fig.update_yaxes(range=[-3.5, 3.5], title="partie imaginaire", zeroline=True, scaleanchor="x")
        graphique(fig)

    st.latex(
        rf"z={a:.2f}+{b:.2f}i,\qquad \frac1z=\frac{{a-bi}}{{a^2+b^2}}={inv_a:.3f}{inv_b:+.3f}i"
    )
    st.success(
        f"a et b sont rationnels, donc {inv_a:.3f} et {inv_b:.3f} le sont aussi : "
        "l'inverse reste dans Q[i]. C'est ce qui fait de Q[i] un corps."
    )


def g_integre() -> None:
    x = np.linspace(-2.5, 2.5, 800)
    f = np.maximum(0, x)
    g = np.maximum(0, -x)
    with st.columns([2.4, 1])[0]:
        fig = base_figure("Deux fonctions non nulles dont le produit est nul")
        fig.add_trace(go.Scatter(x=x, y=f, mode="lines", name="f(x)=max(0,x)",
                                 line=dict(color=BLEU, width=2.5)))
        fig.add_trace(go.Scatter(x=x, y=g, mode="lines", name="g(x)=max(0,−x)",
                                 line=dict(color=ORANGE, width=2.5)))
        fig.add_trace(go.Scatter(x=x, y=f * g, mode="lines", name="f(x)g(x)=0",
                                 line=dict(color=VERT, width=3, dash="dash")))
        fig.update_yaxes(range=[-0.2, 2.5])
        graphique(fig)
    st.warning(
        "f et g sont non nulles, mais f(x)g(x)=0 pour tout x : ce sont des diviseurs de zéro. "
        "L'anneau F(R,R) n'est donc pas intègre, et il n'est pas un corps."
    )


# ---------------------------------------------------------------------------
# 5. Anneaux de Gauss et de rationnels
# ---------------------------------------------------------------------------
def g_gauss() -> None:
    col_g, col_d = st.columns([2.2, 1], gap="large")
    with col_d:
        a = st.slider("Partie réelle a", -4, 4, 2, 1, key="alg_g_gauss_a")
        b = st.slider("Partie imaginaire b", -4, 4, 1, 1, key="alg_g_gauss_b")

    points = [(i, j) for i in range(-4, 5) for j in range(-4, 5)]
    with col_g:
        fig = base_figure("Les entiers de Gauss Z[i] : un réseau dans le plan complexe")
        fig.add_trace(go.Scatter(
            x=[p[0] for p in points], y=[p[1] for p in points],
            mode="markers", name="Z[i]",
            marker=dict(color="rgba(76,141,255,0.45)", size=7),
        ))
        unites = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fig.add_trace(go.Scatter(
            x=[p[0] for p in unites], y=[p[1] for p in unites],
            mode="markers+text", text=["1", "−1", "i", "−i"], textposition="top center",
            name="unités", marker=dict(color=VERT, size=13, symbol="star"),
        ))
        fig.add_trace(go.Scatter(
            x=[a], y=[b], mode="markers+text", text=[f"{a}+{b}i"], textposition="top center",
            name="z", marker=dict(color=ORANGE, size=12),
        ))
        fig.update_xaxes(range=[-4.5, 4.5], title="Re", zeroline=True)
        fig.update_yaxes(range=[-4.5, 4.5], title="Im", zeroline=True, scaleanchor="x")
        graphique(fig)

    norme = a * a + b * b
    st.latex(rf"N({a}+{b}i)=a^2+b^2={norme}")
    if norme == 0:
        st.info("z = 0 n'est jamais inversible.")
    elif norme == 1:
        st.success(f"{a}+{b}i est une unité de Z[i] : son inverse est son conjugué.")
    else:
        st.warning(
            f"L'inverse dans C est ({a}−{b}i)/{norme}. Ses coordonnées ne sont pas "
            "entières en général : Z[i] n'est pas un corps. Par exemple 2 n'a pas d'inverse dans Z[i]."
        )


# ---------------------------------------------------------------------------
# 6. Groupes de transformations : exemples 2 et 3
# ---------------------------------------------------------------------------
def _grille_transforme(titre: str, transformation, x_min=-2, x_max=2, y_min=-2, y_max=2) -> go.Figure:
    fig = base_figure(titre, hauteur=450)
    # Grille d'origine, en gris.
    for t in np.linspace(x_min, x_max, 7):
        fig.add_trace(go.Scatter(x=[t, t], y=[y_min, y_max], mode="lines",
                                 line=dict(color="rgba(139,148,158,0.35)", width=1),
                                 showlegend=False, hoverinfo="skip"))
    for t in np.linspace(y_min, y_max, 7):
        fig.add_trace(go.Scatter(x=[x_min, x_max], y=[t, t], mode="lines",
                                 line=dict(color="rgba(139,148,158,0.35)", width=1),
                                 showlegend=False, hoverinfo="skip"))
    # Grille transformée.
    for t in np.linspace(x_min, x_max, 7):
        p1 = transformation(t, y_min)
        p2 = transformation(t, y_max)
        fig.add_trace(go.Scatter(x=[p1[0], p2[0]], y=[p1[1], p2[1]], mode="lines",
                                 line=dict(color=BLEU, width=1.8), showlegend=False, hoverinfo="skip"))
    for t in np.linspace(y_min, y_max, 7):
        p1 = transformation(x_min, t)
        p2 = transformation(x_max, t)
        fig.add_trace(go.Scatter(x=[p1[0], p2[0]], y=[p1[1], p2[1]], mode="lines",
                                 line=dict(color=BLEU, width=1.8), showlegend=False, hoverinfo="skip"))
    fig.update_xaxes(range=[-7, 7], title="X")
    fig.update_yaxes(range=[-7, 7], title="Y", scaleanchor="x")
    return fig


def g_affine() -> None:
    col_g, col_d = st.columns([2.2, 1], gap="large")
    with col_d:
        x = st.slider("x (facteur)", 0.2, 2.0, 1.2, 0.1, key="alg_g_aff_x")
        y = st.slider("y (translation)", -2.0, 2.0, 0.5, 0.1, key="alg_g_aff_y")
    with col_g:
        graphique(_grille_transforme(
            "Transformation (X,Y) ↦ (xX+y, xY+y)",
            lambda X, Y: (x * X + y, x * Y + y),
        ))
    st.info(
        f"La transformation associée à ({x},{y}) est une homothétie de rapport {x} "
        f"suivie d'une translation de {y}. La composition de deux telles transformations "
        "suit exactement la loi (x,y)∗(x',y')=(xx', xy'+y)."
    )


def g_ex2() -> None:
    col_g, col_d = st.columns([2.2, 1], gap="large")
    with col_d:
        x = st.slider("x", -1.5, 1.5, 0.4, 0.1, key="alg_g_ex2_x")
        y = st.slider("y", -1.5, 1.5, 0.6, 0.1, key="alg_g_ex2_y")
        xp = st.slider("x′", -1.5, 1.5, 0.3, 0.1, key="alg_g_ex2_xp")
        yp = st.slider("y′", -1.5, 1.5, -0.2, 0.1, key="alg_g_ex2_yp")
    resultat = (x + xp, y * np.exp(xp) + yp * np.exp(-x))
    inverse = (x + xp, yp * np.exp(x) + y * np.exp(-xp))
    with col_g:
        fig = base_figure("La loi de l'exercice 2 déforme le plan")
        # Petite grille de points
        points = [(i / 2, j / 2) for i in range(-2, 3) for j in range(-2, 3)]
        images = [(x + u, y * np.exp(u) + v * np.exp(-x)) for u, v in points]
        fig.add_trace(go.Scatter(x=[p[0] for p in points], y=[p[1] for p in points],
                                 mode="markers", name="points (x′,y′)",
                                 marker=dict(color="rgba(139,148,158,0.55)", size=7)))
        fig.add_trace(go.Scatter(x=[p[0] for p in images], y=[p[1] for p in images],
                                 mode="markers", name="images par (x,y)∗",
                                 marker=dict(color=BLEU, size=8)))
        fig.add_trace(go.Scatter(x=[resultat[0]], y=[resultat[1]], mode="markers+text",
                                 text=["(x,y)∗(x′,y′)"], textposition="top center",
                                 name="résultat", marker=dict(color=ORANGE, size=13)))
        fig.update_xaxes(title="abscisse", zeroline=True)
        fig.update_yaxes(title="ordonnée", zeroline=True)
        graphique(fig)
    st.latex(
        rf"(x,y)*(x',y')=({resultat[0]:.2f},\,{resultat[1]:.2f})"
        rf"\qquad (x',y')*(x,y)=({inverse[0]:.2f},\,{inverse[1]:.2f})"
    )
    st.info(
        "La transformation dépend de x et y : elle mélange translation et dilatation. "
        "En échangeant les deux couples, le résultat change : la loi n'est pas commutative."
    )


def g_ex1() -> None:
    g_loi_ex1()


def g_ex4() -> None:
    g_anneau()


def g_ex5() -> None:
    g_corps()


def g_ex6() -> None:
    g_integre()


def g_ex7() -> None:
    g_gauss()


def g_ex8() -> None:
    g_corps()
