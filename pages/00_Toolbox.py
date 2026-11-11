# -*- coding: utf-8 -*-
"""
00_Toolbox.py — la boîte à outils d'algèbre.

15 notions pour lire le TD 3 :
loi interne, commutativité, associativité, neutre, symétrique, groupe,
groupe abélien, sous-groupe, anneau, anneau commutatif, distributivité,
corps, intégrité, sous-anneau/sous-corps, table de Cayley.

Chaque notion contient : énoncé formel, mots simples, visualisation,
exemple, contre-exemple, idée de preuve, « quand l'utiliser » et le lien TD.
"""

from __future__ import annotations

import sys
import textwrap
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
if str(RACINE) not in sys.path:
    sys.path.insert(0, str(RACINE))

import streamlit as st  # noqa: E402

from ui import badge, configurer_page, encadre, pied_page, titre_page  # noqa: E402
from algebra_graphs import (  # noqa: E402
    g_anneau,
    g_associativite,
    g_commutativite,
    g_corps,
    g_distributivite,
    g_gauss,
    g_groupe,
    g_integre,
    g_loi_ex1,
    g_neutre,
    g_sous_groupe,
    g_symetrique,
)

configurer_page("Boîte à outils", "🧰")


NOTIONS = [
    # ------------------------------------------------------------------ 1
    {
        "id": "loi",
        "famille": "Loi et axiomes",
        "titre": "Loi de composition interne",
        "enonce": r"""
Soit $E$ un ensemble. Une **loi de composition interne** sur $E$ est une application
$$ * : E\times E \longrightarrow E. $$
Autrement dit, pour tous $x,y\in E$, le résultat $x*y$ appartient encore à $E$.

On dit aussi que $E$ est **stable** pour la loi $*$.
""",
        "mots": r"""
Une loi interne, c'est une machine qui prend **deux** éléments de $E$ et qui rend **un** élément de $E$. Rien ne doit sortir de l'ensemble.

C'est la première chose à vérifier avant de parler d'associativité, de neutre ou de groupe. Si la loi n'est pas interne, tout le reste n'a pas de sens.
""",
        "preuve": r"""
La clôture se vérifie par un calcul : on prend $x,y\in E$, on écrit $x*y$, et on montre que le résultat est encore dans $E$.

Exemple : sur $\mathbb{N}$, l'addition est interne car la somme de deux entiers naturels est un entier naturel. La soustraction ne l'est pas : $1-2=-1\notin\mathbb{N}$.
""",
        "exemple": r"""
L'addition et la multiplication sont des lois internes sur $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ et $\mathbb{C}$.

Sur $\mathbb{R}^2$, $(x,y)*(x',y')=(x+x',y+y')$ est une loi interne : on reste dans $\mathbb{R}^2$.
""",
        "contre": r"""
Sur $\mathbb{N}$, la soustraction n'est pas interne : $1-2\notin\mathbb{N}$.

Sur $\mathbb{R}$, la division $x/y$ n'est pas une loi interne partout : elle n'est pas définie pour $y=0$.
""",
        "quand": r"""
Pour l'exercice 1 : avant de vérifier la commutativité ou l'associativité, il faut vérifier que le résultat reste dans $E$. C'est aussi le premier point de tout groupe ou anneau.
""",
        "td": "Exercices 1 à 4",
        "graph": g_loi_ex1,
    },
    # ------------------------------------------------------------------ 2
    {
        "id": "commutativite",
        "famille": "Loi et axiomes",
        "titre": "Commutativité",
        "enonce": r"""
La loi $*$ est **commutative** si
$$ \forall x,y\in E,\qquad x*y=y*x. $$
""",
        "mots": r"""
L'ordre des deux éléments ne change pas le résultat. On peut échanger $x$ et $y$ sans conséquence.

Pour la **prouver**, on développe les deux membres avec des lettres. Pour la **réfuter**, un seul couple $(x,y)$ qui donne deux résultats différents suffit.
""",
        "preuve": r"""
On écrit $x*y$ et $y*x$. Si les deux expressions sont littéralement égales, la loi est commutative.

Exemple : $x*y=\sqrt{x^2+y^2}$ est commutative car $x^2+y^2=y^2+x^2$.

Pour montrer qu'une loi n'est pas commutative, on exhibe un contre-exemple : deux éléments précis pour lesquels les deux calculs diffèrent.
""",
        "exemple": r"""
L'addition et la multiplication sur $\mathbb{R}$ sont commutatives.

La loi $x*y=\sqrt{x^2+y^2}$ de l'exercice 1 est commutative.

La composition dans $S_3$ n'est pas commutative.
""",
        "contre": r"""
La soustraction sur $\mathbb{Z}$ n'est pas commutative : $5-3\neq 3-5$.

La composition des permutations dans $S_3$ n'est pas commutative.

La loi de l'exercice 3 n'est pas commutative : $(2,0)*(1,1)=(2,2)$ mais $(1,1)*(2,0)=(2,1)$.
""",
        "quand": r"""
Pour l'exercice 1.1a, 1.2a, 2.2, 3.1 et 4.2a. Une loi commutative donne un groupe abélien, un anneau commutatif, etc.
""",
        "td": "Exercice 1 · Exercice 2.2 · Exercice 3 · Exercice 4",
        "graph": g_commutativite,
    },
    # ------------------------------------------------------------------ 3
    {
        "id": "associativite",
        "famille": "Loi et axiomes",
        "titre": "Associativité",
        "enonce": r"""
La loi $*$ est **associative** si
$$ \forall x,y,z\in E,\qquad (x*y)*z=x*(y*z). $$
""",
        "mots": r"""
On peut déplacer les parenthèses sans changer le résultat. Calculer d'abord $x*y$, ou d'abord $y*z$, revient au même.

C'est ce qui permet d'écrire $x*y*z$ sans parenthèses. Pour la **prouver**, il faut le faire avec des lettres ; pour la **réfuter**, un triplet suffit.
""",
        "preuve": r"""
On calcule les deux membres séparément, puis on compare.

Pour la loi $x*y=\sqrt{x^2+y^2}$ :
$$ (x*y)*z=\sqrt{(\sqrt{x^2+y^2})^2+z^2}=\sqrt{x^2+y^2+z^2}=x*(y*z). $$

Pour la loi $x*y=xy+(x^2-1)(y^2-1)$, le calcul avec des lettres montre que les deux membres ne sont pas toujours égaux. Un contre-exemple simple : $x=0$, $y=1$, $z=0$.
""",
        "exemple": r"""
L'addition et la multiplication sur $\mathbb{R}$ sont associatives.

La composition des fonctions est associative.

La loi $x*y=\sqrt{x^2+y^2}$ est associative.
""",
        "contre": r"""
La soustraction n'est pas associative : $(5-3)-1=1$ mais $5-(3-1)=3$.

La loi $x*y=xy+(x^2-1)(y^2-1)$ n'est pas associative : avec $(x,y,z)=(0,1,0)$,
$$ (0*1)*0=0*0=1\quad\text{alors que}\quad 0*(1*0)=0*1=0. $$
""",
        "quand": r"""
Pour l'exercice 1.2b, et pour vérifier qu'un ensemble muni d'une loi est un groupe ou un anneau.
""",
        "td": "Exercice 1.2 · Exercices 2, 3, 4",
        "graph": g_associativite,
    },
    # ------------------------------------------------------------------ 4
    {
        "id": "neutre",
        "famille": "Loi et axiomes",
        "titre": "Élément neutre",
        "enonce": r"""
Un élément $e\in E$ est **neutre** pour la loi $*$ si
$$ \forall x\in E,\qquad e*x=x*e=x. $$
""",
        "mots": r"""
C'est l'élément qui ne change rien : le « 0 » de l'addition, le « 1 » de la multiplication.

Quand il existe, il est **unique**. On le note souvent $0$ pour une loi additive et $1$ pour une loi multiplicative, mais ce ne sont que des noms.
""",
        "preuve": r"""
Pour prouver que $e$ est neutre, on calcule $e*x$ et $x*e$ et on montre que les deux valent $x$.

Pour l'unicité : si $e$ et $e'$ sont deux neutres, alors
$$ e=e*e'=e', $$
donc $e=e'$.
""",
        "exemple": r"""
$0$ est neutre pour l'addition sur $\mathbb{R}$ ; $1$ est neutre pour la multiplication.

Dans l'exercice 2, $(0,0)$ est neutre. Dans l'exercice 3 et l'exercice 4, $(1,0)$ est neutre.
""",
        "contre": r"""
Pour la loi $x*y=x+y+1$ sur $\mathbb{R}$, le neutre est $-1$, pas $0$ : $x*(-1)=x$.

Dans $\mathbb{N}$ muni de la soustraction, il n'y a pas de neutre (et la loi n'est même pas interne).
""",
        "quand": r"""
Pour l'exercice 1.1c, 1.2c, 2, 3 et 4.2c. Sans neutre, on ne peut pas définir le symétrique.
""",
        "td": "Exercice 1 · Exercices 2, 3, 4",
        "graph": g_neutre,
    },
    # ------------------------------------------------------------------ 5
    {
        "id": "symetrique",
        "famille": "Loi et axiomes",
        "titre": "Symétrique d'un élément",
        "enonce": r"""
On suppose que $*$ admet un neutre $e$. L'élément $x'\in E$ est **symétrique** de $x$ si
$$ x*x'=x'*x=e. $$
Dans une loi additive, on parle d'**opposé** ; dans une loi multiplicative, d'**inverse**.
""",
        "mots": r"""
Le symétrique, c'est l'élément qui « annule » $x$ et ramène au neutre. Pour l'addition, c'est $-x$ ; pour la multiplication, c'est $1/x$.

Dans un groupe, chaque élément a un symétrique, et il est unique.
""",
        "preuve": r"""
On cherche $x'$ en résolvant $x*x'=e$, puis on vérifie aussi $x'*x=e$.

Unicité dans un groupe : si $x'$ et $x''$ sont deux symétriques de $x$, alors
$$ x'=x'*e=x'*(x*x'')=(x'*x)*x''=e*x''=x''. $$
""",
        "exemple": r"""
Dans $(\mathbb{R},+)$, le symétrique de $x$ est $-x$.

Dans $(\mathbb{R}^*,\times)$, le symétrique de $x$ est $1/x$.

Dans l'exercice 2, le symétrique de $(x,y)$ est $(-x,-y)$.
""",
        "contre": r"""
Dans $(\mathbb{Z}/6\mathbb{Z},\times)$, $2$ n'a pas d'inverse : aucune classe $y$ ne vérifie $2y\equiv1\pmod6$.

Dans l'exercice 1.1, aucun élément de $\mathbb{R}^{+*}$ n'a de symétrique pour $x*y=\sqrt{x^2+y^2}$.
""",
        "quand": r"""
Pour l'exercice 1.1d, et pour montrer qu'un ensemble est un groupe (exercices 2 et 3).
""",
        "td": "Exercice 1.1d · Exercices 2 et 3",
        "graph": g_symetrique,
    },
    # ------------------------------------------------------------------ 6
    {
        "id": "groupe",
        "famille": "Structures",
        "titre": "Groupe",
        "enonce": r"""
Un ensemble $G$ muni d'une loi $*$ est un **groupe**, noté $(G,*)$, si :
1. $*$ est interne ;
2. $*$ est associative ;
3. $*$ admet un neutre $e$ ;
4. tout élément $x\in G$ admet un symétrique $x^{-1}$.
""",
        "mots": r"""
Un groupe, c'est une arithmétique complète : on peut calculer, regrouper les calculs comme on veut, et revenir en arrière avec l'inverse.

Les quatre points se vérifient **dans cet ordre**. Le neutre et l'inverse se lisent souvent bien sur une table de Cayley.
""",
        "preuve": r"""
On vérifie les quatre axiomes :
- clôture : $x*y\in G$ ;
- associativité : calcul avec des lettres ;
- neutre : on exhibe $e$ et on vérifie $e*x=x*e=x$ ;
- inverse : pour chaque $x$, on exhibe $x^{-1}$ et on vérifie $x*x^{-1}=x^{-1}*x=e$.
""",
        "exemple": r"""
$(\mathbb{Z},+)$, $(\mathbb{R}^*,\times)$, $(\mathbb{R}^2,+)$ et $(S_3,\circ)$ sont des groupes.

Dans le TD : $(\mathbb{R}^2,*)$ de l'exercice 2 et $(H,*)$ de l'exercice 3 sont des groupes.
""",
        "contre": r"""
$(\mathbb{N},+)$ n'est pas un groupe : $1$ n'a pas d'opposé dans $\mathbb{N}$.

$(\mathbb{Z},\times)$ n'est pas un groupe : $2$ n'a pas d'inverse dans $\mathbb{Z}$.

$(\mathbb{Z}/6\mathbb{Z},\times)$ n'est pas un groupe : $0$ n'a pas d'inverse.
""",
        "quand": r"""
Pour les exercices 2 et 3 : montrer qu'une loi est un groupe, puis chercher un sous-groupe.
""",
        "td": "Exercices 2 et 3",
        "graph": g_groupe,
    },
    # ------------------------------------------------------------------ 7
    {
        "id": "abelien",
        "famille": "Structures",
        "titre": "Groupe commutatif (abélien)",
        "enonce": r"""
Un groupe $(G,*)$ est **commutatif** (ou **abélien**) si, de plus,
$$ \forall x,y\in G,\qquad x*y=y*x. $$
""",
        "mots": r"""
C'est un groupe où l'ordre des éléments ne compte pas. Toutes les opérations habituelles ($+$, $\times$) sont commutatives, mais la composition des permutations ne l'est pas.
""",
        "preuve": r"""
On reprend les quatre axiomes du groupe, puis on ajoute la vérification de la commutativité.

Pour montrer qu'un groupe n'est pas abélien, on exhibe deux éléments $x,y$ tels que $x*y\neq y*x$.
""",
        "exemple": r"""
$(\mathbb{Z},+)$, $(\mathbb{R},+)$ et $(\mathbb{R}^*,\times)$ sont abéliens.

$(\mathbb{R}^2,+)$ de l'exercice 4 est abélien.
""",
        "contre": r"""
$(S_3,\circ)$ n'est pas abélien.

Dans l'exercice 3, $(2,0)*(1,1)=(2,2)$ mais $(1,1)*(2,0)=(2,1)$ : $H$ n'est pas abélien.

Dans l'exercice 2, $(1,0)*(0,1)=(1,e^{-1})$ et $(0,1)*(1,0)=(1,e)$ : $G$ n'est pas abélien.
""",
        "quand": r"""
Pour l'exercice 2.2, l'exercice 3.1 et l'exercice 4.1.
""",
        "td": "Exercice 2.2 · Exercice 3.1 · Exercice 4.1",
        "graph": g_commutativite,
    },
    # ------------------------------------------------------------------ 8
    {
        "id": "sous_groupe",
        "famille": "Structures",
        "titre": "Sous-groupe",
        "enonce": r"""
Soit $(G,*)$ un groupe et $H\subseteq G$. On dit que $H$ est un **sous-groupe** de $G$ si, muni de la même loi, $H$ est lui-même un groupe.

**Caractérisation pratique.** $H$ est un sous-groupe de $G$ si et seulement si :
1. $H\neq\varnothing$ ;
2. pour tous $x,y\in H$, $x*y^{-1}\in H$.
""",
        "mots": r"""
Un sous-groupe, c'est un petit groupe caché à l'intérieur d'un grand. Il doit contenir le neutre, être stable par la loi et contenir les inverses.

La caractérisation en une seule condition évite de revérifier l'associativité : elle est héritée du grand groupe.
""",
        "preuve": r"""
On vérifie les trois conditions : $H$ non vide, stable par $*$, stable par inverse. Le neutre s'obtient en prenant $x*x^{-1}$.

Pour l'exercice 3.2, $H_0=]0,+\infty[\times\mathbb{R}$ : il est non vide, stable par $*$ car le produit de deux réels strictement positifs est strictement positif, et l'inverse de $(x,y)$ est $(1/x,-y/x)\in H_0$.
""",
        "exemple": r"""
$2\mathbb{Z}=\{2k:k\in\mathbb{Z}\}$ est un sous-groupe de $(\mathbb{Z},+)$.

$\{0,3\}$ est un sous-groupe de $(\mathbb{Z}/6\mathbb{Z},+)$.

$]0,+\infty[\times\mathbb{R}$ est un sous-groupe de $(H,*)$ dans l'exercice 3.
""",
        "contre": r"""
$\mathbb{N}$ n'est pas un sous-groupe de $(\mathbb{Z},+)$ : il ne contient pas les opposés.

$\{0,1,2\}$ n'est pas un sous-groupe de $(\mathbb{Z}/6\mathbb{Z},+)$ : $2+2=4\notin\{0,1,2\}$.
""",
        "quand": r"""
Pour l'exercice 3.2. La caractérisation « non vide + $x*y^{-1}$ » est le réflexe à avoir.
""",
        "td": "Exercice 3.2",
        "graph": g_sous_groupe,
    },
    # ------------------------------------------------------------------ 9
    {
        "id": "anneau",
        "famille": "Structures",
        "titre": "Anneau",
        "enonce": r"""
Un ensemble $A$ muni de deux lois $+$ et $\times$ est un **anneau** si :
1. $(A,+)$ est un groupe abélien ;
2. $\times$ est associative ;
3. $\times$ est distributive sur $+$ à gauche et à droite :
$$ a\times(b+c)=a\times b+a\times c,\qquad (a+b)\times c=a\times c+b\times c. $$

S'il existe un neutre pour $\times$, on dit que l'anneau est **unitaire**.
""",
        "mots": r"""
Un anneau, c'est deux opérations qui vivent ensemble : on additionne, on multiplie, et la multiplication se distribue sur l'addition, comme dans les calculs habituels.

C'est la structure de $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, des polynômes, des matrices…
""",
        "preuve": r"""
On vérifie d'abord le groupe additif : neutre $0$, opposé $-x$, associativité et commutativité de $+$.

Ensuite, l'associativité de $\times$, puis les deux distributivités.
""",
        "exemple": r"""
$(\mathbb{Z},+,\times)$, $(\mathbb{Q},+,\times)$, $(\mathbb{R},+,\times)$ et $(\mathbb{C},+,\times)$ sont des anneaux commutatifs unitaires.

L'ensemble $A=\mathbb{R}\times\mathbb{R}$ de l'exercice 4, muni de $+$ et $*$, est un anneau commutatif unitaire.
""",
        "contre": r"""
$(\mathbb{N},+,\times)$ n'est pas un anneau : $(\mathbb{N},+)$ n'est pas un groupe.

L'ensemble des matrices $M_n(\mathbb{R})$ est un anneau non commutatif pour $n\ge2$.
""",
        "quand": r"""
Pour l'exercice 4.2d, l'exercice 6a, l'exercice 7a et l'exercice 8.
""",
        "td": "Exercice 4 · Exercice 6 · Exercice 7 · Exercice 8",
        "graph": g_anneau,
    },
    # ------------------------------------------------------------------ 10
    {
        "id": "anneau_commutatif",
        "famille": "Structures",
        "titre": "Anneau commutatif",
        "enonce": r"""
Un anneau $(A,+,\times)$ est **commutatif** si
$$ \forall a,b\in A,\qquad a\times b=b\times a. $$
""",
        "mots": r"""
C'est un anneau où l'ordre des facteurs ne change rien. $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ et $\mathbb{Q}[i]$ sont commutatifs ; les matrices ne le sont pas.
""",
        "preuve": r"""
On vérifie les axiomes d'anneau, puis on ajoute $a\times b=b\times a$ pour tous $a,b$.

Pour l'exercice 4, le calcul est immédiat : $xx'=x'x$ et $xy'+x'y=x'y+xy'$.
""",
        "exemple": r"""
$\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Z}[i]$, $\mathbb{Q}[i]$ et $A=\mathbb{R}\times\mathbb{R}$ (exercice 4) sont des anneaux commutatifs.

L'anneau $\mathcal{F}(\mathbb{R},\mathbb{R})$ de l'exercice 6 est commutatif.
""",
        "contre": r"""
$M_2(\mathbb{R})$ n'est pas commutatif : $\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&0\\1&0\end{pmatrix}\neq\begin{pmatrix}0&0\\1&0\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}$.

L'anneau des quaternions $\mathbb{H}$ n'est pas commutatif.
""",
        "quand": r"""
Pour l'exercice 4.2d, l'exercice 6a et l'exercice 7a.
""",
        "td": "Exercice 4 · Exercice 6 · Exercice 7",
        "graph": g_anneau,
    },
    # ------------------------------------------------------------------ 11
    {
        "id": "distributivite",
        "famille": "Structures",
        "titre": "Distributivité",
        "enonce": r"""
Dans un anneau, la multiplication est distributive sur l'addition :
$$ a\times(b+c)=a\times b+a\times c, $$
$$ (a+b)\times c=a\times c+b\times c. $$
""",
        "mots": r"""
La multiplication « se distribue » sur l'addition, exactement comme $2(3+4)=2\times3+2\times4$.

C'est cette règle qui permet de développer et de factoriser. Si elle tombe, ce n'est pas un anneau.
""",
        "preuve": r"""
On développe les deux membres et on compare. Dans $\mathbb{Z}/6\mathbb{Z}$, on compare les restes modulo 6.

Exemple : $2\times(3+4)=2\times1=2$ et $2\times3+2\times4=6+8=14\equiv2\pmod6$.
""",
        "exemple": r"""
Dans $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ et $\mathbb{C}$, la distributivité est la règle habituelle.

Dans $A=\mathbb{R}\times\mathbb{R}$ de l'exercice 4, elle se vérifie composante par composante.
""",
        "contre": r"""
La loi $x*y=xy+1$ sur $\mathbb{R}$ n'est pas distributive sur $+$ :
$$ a*(b+c)=a(b+c)+1\quad\text{alors que}\quad a*b+a*c=ab+1+ac+1, $$
les deux expressions diffèrent de $1$.
""",
        "quand": r"""
Pour l'exercice 4.2d, l'exercice 6a, l'exercice 7a et l'exercice 8.
""",
        "td": "Exercice 4 · Exercice 6 · Exercice 7 · Exercice 8",
        "graph": g_distributivite,
    },
    # ------------------------------------------------------------------ 12
    {
        "id": "corps",
        "famille": "Structures",
        "titre": "Corps",
        "enonce": r"""
Un **corps** $(K,+,\times)$ est un anneau commutatif unitaire tel que $1\neq0$ et tel que tout élément non nul admette un inverse pour $\times$ :
$$ \forall x\in K,\ x\neq0\ \Longrightarrow\ \exists y\in K,\ xy=yx=1. $$
""",
        "mots": r"""
Un corps, c'est un anneau où l'on peut diviser par tout élément non nul. $\mathbb{Q}$, $\mathbb{R}$ et $\mathbb{C}$ sont des corps.

Un corps est toujours intègre : si $xy=0$ et $x\neq0$, on multiplie par $x^{-1}$ et on trouve $y=0$.
""",
        "preuve": r"""
On vérifie les axiomes d'anneau commutatif, puis l'existence de l'inverse pour chaque élément non nul.

Pour $\mathbb{Q}[i]$ : si $z=a+bi\neq0$, alors
$$ \frac1z=\frac{a-bi}{a^2+b^2}, $$
et $a/(a^2+b^2)$, $-b/(a^2+b^2)$ sont rationnels.
""",
        "exemple": r"""
$\mathbb{Q}$, $\mathbb{R}$ et $\mathbb{C}$ sont des corps.

$\mathbb{Q}[i]=\{a+bi:a,b\in\mathbb{Q}\}$ est un corps (exercice 8).
""",
        "contre": r"""
$\mathbb{Z}$ n'est pas un corps : $2$ n'a pas d'inverse dans $\mathbb{Z}$.

$\mathbb{Z}[i]$ n'est pas un corps : $2$ n'a pas d'inverse dans $\mathbb{Z}[i]$.

$A=\mathbb{R}\times\mathbb{R}$ de l'exercice 4 n'est pas un corps : $(0,1)*(0,1)=(0,0)$.
""",
        "quand": r"""
Pour l'exercice 5.3, l'exercice 6c, l'exercice 7b et l'exercice 8.
""",
        "td": "Exercice 5 · Exercice 6 · Exercice 7 · Exercice 8",
        "graph": g_corps,
    },
    # ------------------------------------------------------------------ 13
    {
        "id": "integre",
        "famille": "Structures",
        "titre": "Anneau intègre",
        "enonce": r"""
Un anneau commutatif unitaire non nul $(A,+,\times)$ est **intègre** s'il n'a pas de diviseurs de zéro :
$$ \forall x,y\in A,\qquad xy=0\ \Longrightarrow\ x=0\ \text{ou}\ y=0. $$
""",
        "mots": r"""
Un anneau intègre, c'est un anneau où un produit nul force l'un des facteurs à être nul. C'est le cas de $\mathbb{Z}$ : si $ab=0$, alors $a=0$ ou $b=0$.

Un corps est intègre, mais un anneau intègre n'est pas forcément un corps : $\mathbb{Z}$ est intègre et n'est pas un corps.
""",
        "preuve": r"""
Pour montrer qu'un anneau est intègre, on suppose $xy=0$ et on prouve $x=0$ ou $y=0$.

Pour montrer qu'il ne l'est pas, on exhibe deux éléments non nuls dont le produit est nul.
""",
        "exemple": r"""
$\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Z}[i]$ et $\mathbb{Q}[i]$ sont intègres.

Tout corps est intègre.
""",
        "contre": r"""
$\mathbb{Z}/6\mathbb{Z}$ n'est pas intègre : $2\times3=6\equiv0$, avec $2\neq0$ et $3\neq0$.

$\mathcal{F}(\mathbb{R},\mathbb{R})$ n'est pas intègre : $f(x)=\max(0,x)$ et $g(x)=\max(0,-x)$ sont non nulles, mais $fg=0$.

$A=\mathbb{R}\times\mathbb{R}$ de l'exercice 4 n'est pas intègre : $(0,1)*(0,1)=(0,0)$.
""",
        "quand": r"""
Pour l'exercice 6b et l'exercice 7b.
""",
        "td": "Exercice 6 · Exercice 7",
        "graph": g_integre,
    },
    # ------------------------------------------------------------------ 14
    {
        "id": "sous_anneau",
        "famille": "Structures",
        "titre": "Sous-anneau et sous-corps",
        "enonce": r"""
Soit $B\subseteq A$. On dit que $B$ est un **sous-anneau** de $A$ si, muni des mêmes lois, $B$ est un anneau et si $1_A\in B$.

$B$ est un **sous-corps** de $K$ si $B$ est un sous-anneau et si tout $x\in B\setminus\{0\}$ a son inverse dans $B$.
""",
        "mots": r"""
Un sous-anneau, c'est un anneau plus petit, avec les mêmes opérations. Il doit contenir $0$ et $1$, être stable par $+$, par $-$ et par $\times$.

Un sous-corps doit en plus être stable par inverse.
""",
        "preuve": r"""
On vérifie : $0,1\in B$ ; stabilité par addition, par opposé et par multiplication. L'associativité et la distributivité sont héritées de $A$.

Pour un sous-corps, on ajoute : si $x\in B$ et $x\neq0$, alors $x^{-1}\in B$.
""",
        "exemple": r"""
$\mathbb{Z}$ est un sous-anneau de $\mathbb{Q}$ ; $\mathbb{Q}$ est un sous-corps de $\mathbb{R}$.

$\mathbb{Z}[i]$ est un sous-anneau de $\mathbb{C}$ ; $\mathbb{Q}[i]$ est un sous-corps de $\mathbb{C}$.
""",
        "contre": r"""
$\mathbb{N}$ n'est pas un sous-anneau de $\mathbb{Z}$ : il n'est pas stable par opposé.

$\mathbb{Z}[i]$ n'est pas un sous-corps de $\mathbb{C}$ : $2$ n'a pas d'inverse dans $\mathbb{Z}[i]$.
""",
        "quand": r"""
Pour l'exercice 7a et l'exercice 8 : on montre que $\mathbb{Z}[i]$ et $\mathbb{Q}[i]$ sont des sous-anneaux de $\mathbb{C}$, puis on regarde les inverses.
""",
        "td": "Exercice 7 · Exercice 8",
        "graph": g_gauss,
    },
    # ------------------------------------------------------------------ 15
    {
        "id": "table",
        "famille": "Méthodes",
        "titre": "Lire une table de Cayley",
        "enonce": r"""
Soit $E=\{e_1,\dots,e_n\}$ un ensemble fini muni d'une loi $*$. La **table de Cayley** de $*$ est le tableau à double entrée dont la case $(i,j)$ contient $e_i*e_j$.
""",
        "mots": r"""
C'est la « photo » de la loi. Sur une table, on lit très vite :
- la clôture : aucune case ne sort de l'ensemble ;
- le neutre : sa ligne et sa colonne recopient les étiquettes ;
- les inverses : chaque ligne contient le neutre ;
- la commutativité : la table est symétrique par rapport à la diagonale.

L'associativité, elle, ne se lit pas directement : il faut comparer $(x*y)*z$ et $x*(y*z)$.
""",
        "preuve": r"""
Pour construire la table, on calcule toutes les cases. Pour l'utiliser, on cherche le neutre, puis les inverses.

Attention : une table peut être remplie et ne pas être associative. La table ne remplace pas une preuve.
""",
        "exemple": r"""
La table de $(\mathbb{Z}/6\mathbb{Z},+)$ est symétrique, sa ligne $0$ recopie les étiquettes, et chaque ligne contient $0$ : c'est un groupe abélien.

La table de $S_3$ n'est pas symétrique : $S_3$ n'est pas abélien.
""",
        "contre": r"""
La table de $(\mathbb{Z}/6\mathbb{Z},\times)$ a un neutre $1$, mais la ligne de $0$ est pleine de $0$ : $0$ n'a pas d'inverse. Ce n'est pas un groupe.
""",
        "quand": r"""
Pour vérifier rapidement une loi sur un ensemble fini, et pour les exercices 1, 2 et 3 quand on teste des petits exemples.
""",
        "td": "Méthode transversale",
        "graph": g_commutativite,
    },
]

PAR_ID = {notion["id"]: notion for notion in NOTIONS}
NUMERO = {notion["id"]: index + 1 for index, notion in enumerate(NOTIONS)}


# ---------------------------------------------------------------------------
# Barre latérale
# ---------------------------------------------------------------------------
def _sans_accent(texte: str) -> str:
    decompose = unicodedata.normalize("NFD", texte)
    return "".join(c for c in decompose if unicodedata.category(c) != "Mn").lower()


st.sidebar.markdown("### 🧰 Boîte à outils")
st.sidebar.caption("15 notions · 4 familles")

recherche = st.sidebar.text_input("Rechercher une notion", placeholder="groupe, anneau, neutre...")

if recherche.strip():
    mots_clefs = _sans_accent(recherche).split()
    notions_filtrees = [
        notion
        for notion in NOTIONS
        if all(
            mot in _sans_accent(
                f"{notion['titre']} {notion['famille']} {notion['td']} {notion['mots']}"
            )
            for mot in mots_clefs
        )
    ]
else:
    notions_filtrees = list(NOTIONS)

if not notions_filtrees:
    st.sidebar.warning("Aucune notion ne correspond à cette recherche.")
    notions_filtrees = list(NOTIONS)

ids_disponibles = [notion["id"] for notion in notions_filtrees]
selection_courante = st.session_state.get("alg_notion")
if selection_courante and selection_courante not in ids_disponibles:
    ids_disponibles.insert(0, selection_courante)
if "alg_notion" not in st.session_state or st.session_state["alg_notion"] not in ids_disponibles:
    st.session_state["alg_notion"] = ids_disponibles[0]

notion_id = st.sidebar.selectbox(
    "Choisir une notion",
    ids_disponibles,
    format_func=lambda identifiant: f"{NUMERO[identifiant]:02d} · {PAR_ID[identifiant]['titre']}",
    key="alg_notion",
)

if "alg_vues" not in st.session_state:
    st.session_state["alg_vues"] = []
vues = st.session_state["alg_vues"]
if notion_id not in vues:
    vues.append(notion_id)

if "alg_comprises" not in st.session_state:
    st.session_state["alg_comprises"] = {}
comprises = st.session_state["alg_comprises"]

st.sidebar.markdown("---")
st.sidebar.progress(
    len(set(vues)) / len(NOTIONS),
    text=f"{len(set(vues))} / {len(NOTIONS)} notions explorées",
)
st.sidebar.caption(
    "Conseil : cherche d'abord un exemple, puis le contre-exemple, puis reviens à l'énoncé formel."
)


# ---------------------------------------------------------------------------
# En-tête
# ---------------------------------------------------------------------------
titre_page(
    "Boîte à outils",
    "Les 15 notions du TD 3 : loi interne, axiomes, groupe, sous-groupe, anneau, corps, intégrité. "
    "Pour chacune : l'énoncé, les mots simples, une table ou un dessin, un exemple et un contre-exemple.",
    "ALGÈBRE 1 · CP1 · RÉFÉRENTIEL",
)

st.markdown(
    badge("Loi et axiomes · 5", "bleu")
    + badge("Structures · 6", "vert")
    + badge("Corps et intégrité · 3", "orange")
    + badge("Méthode · 1", "violet"),
    unsafe_allow_html=True,
)

with st.expander("Lexique : les mots techniques de ce TD", expanded=False):
    st.markdown(
        textwrap.dedent(
            r"""
            | Terme | Sens simple |
            |---|---|
            | **Loi interne** | Une machine qui prend deux éléments de $E$ et rend un élément de $E$. |
            | **Magma** | Un ensemble muni d'une loi interne (sans autre axiome). |
            | **Neutre** | L'élément qui ne change rien : $e*x=x*e=x$. |
            | **Symétrique** | L'élément qui ramène au neutre : $x*x'=e$. |
            | **Groupe** | Loi interne + associative + neutre + inverses. |
            | **Abélien** | Groupe commutatif. |
            | **Sous-groupe** | Un groupe contenu dans un autre, avec la même loi. |
            | **Anneau** | Groupe abélien pour $+$, multiplication associative et distributive sur $+$. |
            | **Unitaire** | L'anneau possède un neutre $1$ pour la multiplication. |
            | **Corps** | Anneau commutatif où tout élément non nul est inversible. |
            | **Intègre** | Anneau sans diviseurs de zéro : $xy=0\Rightarrow x=0$ ou $y=0$. |
            | **Table de Cayley** | Tableau à double entrée qui donne tous les produits $x*y$. |
            """
        ).strip()
    )

st.info(
    "**Comment travailler ?** Lis l'énoncé formel, puis les mots simples, puis manipule la table. "
    "Ne coche « j'ai compris » que si tu peux refaire l'exemple et le contre-exemple sans regarder."
)


# ---------------------------------------------------------------------------
# Notion affichée
# ---------------------------------------------------------------------------
notion = PAR_ID[notion_id]


def _md(texte: str) -> str:
    return textwrap.dedent(texte).strip()


st.markdown(f"## {NUMERO[notion_id]:02d}. {notion['titre']}")
st.markdown(
    badge(notion["famille"], "bleu") + badge("TD : " + notion["td"], "violet"),
    unsafe_allow_html=True,
)

encadre("violet", "L'énoncé formel", texte=_md(notion["enonce"]))
encadre("bleu", "En mots simples", texte=_md(notion["mots"]))

st.markdown("### Voir pourquoi")
notion["graph"]()

col_exemple, col_contre = st.columns(2, gap="large")
with col_exemple:
    encadre("vert", "Un exemple", texte=_md(notion["exemple"]))
with col_contre:
    encadre("orange", "Un contre-exemple", texte=_md(notion["contre"]))

encadre("vert", "Pourquoi c'est vrai (idée de preuve)", texte=_md(notion["preuve"]))
encadre(
    "violet",
    "Quand l'utiliser ?",
    texte=_md(notion["quand"]) + f"\n\n**Dans le TD :** {notion['td']}.",
)

cle_comprise = f"alg_ok_{notion_id}"
if cle_comprise not in st.session_state:
    st.session_state[cle_comprise] = bool(comprises.get(notion_id, False))
comprise = st.checkbox(
    "J'ai compris : je peux expliquer cette notion et donner un exemple sans le texte.",
    key=cle_comprise,
)
comprises[notion_id] = comprise

if comprise:
    st.success("Bien. Va maintenant l'utiliser dans un exercice : c'est là que la mémoire se fixe.")

pied_page()
