# The original crossing-circle curves in the mixed two-crossing complement

The complete-volume identity for
\[
 Z_N(u)=\operatorname{can}\!\left(T(R^{-2}T(R^2))\right)(-2\cos u)
\]
was established in [the positive subdivision note](research_mixed_two_crossing_positive_subdivision.md).
To fill its remaining crossing circle, one also needs to compare
the source's boundary parameter with the original peripheral curves.
This note transports those curves through an explicit ideal
triangulation and computes their complete Euclidean periods exactly.

There is a definite sign in the calculation. The longitude obtained
by following the crossing-circle oval clockwise in the original
diagram has period ratio \(1+1/Y\). The longitude in the source's
two-pyramid collar has ratio \(-1-1/Y\). The comparison determines
the two primitive bases up to simultaneous reversal and excludes any
unrecorded shear. The full deformed holonomy comparison is proved
separately by the original diagram's group presentation; Section 6
explains how the two arguments fit together.

## 1. Curves in the original diagram

Use the nine-crossing PD diagram, crossing-ball numbering and
orientation calibration of Sections 1–2 of the positive subdivision
note:
\[
\begin{split}
 &(12,5,13,6),\ (6,13,7,0),\ (4,7,5,8),\ (8,3,9,4),\\
 &(2,11,3,12),\ (1,16,2,17),\ (10,15,11,16),\\
 &(14,9,15,10),\ (17,0,14,1).
\end{split}                                                   \tag{1}
\]
The first four crossings describe the rational word, the fifth
is the retained positive carrier, and the last four describe its
crossing circle. The oval consists of arcs \(14,15,16,17\).
It has no self-crossing. Its blackboard parallel is therefore
its preferred longitude. We orient that parallel clockwise,
following the four crossings of the oval in their cyclic order.

Each crossing contributes four tetrahedra. Write \((t,v)\) for
the cusp triangle at vertex \(v\) of tetrahedron \(t\). A normal
curve is recorded by four signed integers
\((a_0,a_1,a_2,a_3)\): \(a_f\) is the flux leaving the triangle
through the side in face \(f\), and \(a_v=0\). The sum is zero.
Opposite sides of a glued face have opposite flux.

The following meridian circles arc \(17\) once. The longitude
follows the oval once. Unlisted triangles have zero flux.

| Curve | Triangle \((t,v)\) | Signed flux |
|---|---|---|
| \(\mu\) | \((20,3)\) | \((0,-1,1,0)\) |
| \(\mu\) | \((21,2)\) | \((0,1,0,-1)\) |
| \(\mu\) | \((33,3)\) | \((-1,0,1,0)\) |
| \(\mu\) | \((34,2)\) | \((1,0,0,-1)\) |
| \(\lambda_{\rm PD}\) | \((20,3)\) | \((1,0,-1,0)\) |
| \(\lambda_{\rm PD}\) | \((23,2)\) | \((-1,0,0,1)\) |
| \(\lambda_{\rm PD}\) | \((24,3)\) | \((1,0,-1,0)\) |
| \(\lambda_{\rm PD}\) | \((27,2)\) | \((-1,0,0,1)\) |
| \(\lambda_{\rm PD}\) | \((30,2)\) | \((0,-1,0,1)\) |
| \(\lambda_{\rm PD}\) | \((31,3)\) | \((0,1,-1,0)\) |
| \(\lambda_{\rm PD}\) | \((34,2)\) | \((0,-1,0,1)\) |
| \(\lambda_{\rm PD}\) | \((35,3)\) | \((0,1,-1,0)\) |

Following the positive flux of the longitude crosses diagram
arcs in the order \(16,15,14,17\). Following the meridian visits
the two crossing ends of arc \(17\) and returns along its other
side. These are respectively the once-parallel and once-transverse
curves on the tubular neighborhood of that component. They have
intersection number of absolute value one and form its primitive
peripheral basis. The choice is diagrammatic; it is not inferred
from a software cusp-shape display.

## 2. Transport through local moves

For this calculation we use a different simplification sequence
from the volume certificate. It starts with two edge collapses,
both disjoint from the entire auxiliary cusp. They remove a
finite–finite edge and then a finite–main-cusp edge. Consequently
the auxiliary triangles and both curves in Section 1 are unchanged.
The remaining 26 tetrahedra are reduced to eight by 56 ordinary
\(2\leftrightarrow3\) moves.

**Lemma 1.** Consider the two triangulations of an abstract
bipyramid in a \(2\leftrightarrow3\) move. Suppose two signed
normal chains, one before and one after the move, are closed
across internal cusp-triangle edges. Suppose their signed
fluxes agree at every individual boundary-edge incidence of
the cusp patch at each of the five abstract vertices. They
represent the same peripheral homology class after replacement.

**Proof.** The cusp patch at each abstract vertex is a disk.
Move intersection points along its boundary edges so that the
two chains have the same boundary. Their difference is an
absolute cycle in that disk and hence bounds. Do this at all
five vertices and glue to the unchanged exterior chain.
The five abstract vertices must remain separate during this
argument. Several may represent the same global cusp, and
some exterior faces may subsequently be paired to one another.
Equality is required before making those identifications. \(\square\)

The certificate labels these five vertices, matches all six
exterior faces, checks every individual boundary flux, and
checks closure in the new triangles. It also checks that all
curve coefficients outside the move are unchanged. Self-paired
boundary faces cannot conceal opposite errors.

The stored chains are witnesses. The verifier does not call a
native peripheral-update routine or infer preservation from a
claimed triangulation isomorphism. The local check certifies
oriented \(H_1\) classes. That is enough for peripheral
eigenvalue periods; it does not certify a based word in the
entire fundamental group.

## 3. Exact complete geometry after transport

Let \(X\) be the upper nonreal root of
\[
 X^3+2X^2+1=0,\qquad Y=1+2X+2X^2.                            \tag{2}
\]
Set
\[
 a=1-\frac1X,\qquad b=X(1-X),\qquad l=-\frac2{Y-1}.
\]
In the recorded final ordering the eight shapes are
\[
 \left(\frac a2,\ X,\ \frac a2,\ a,\
                  \frac{b-1}{b},\ l,\ l,\ b\right).           \tag{3}
\]
The verifier reconstructs all eight edge equations from the
face pairings, checks their products in
\(\mathbb Q[X]/(X^3+2X^2+1)\), and checks that every edge angle
sum is \(2\pi\). All 24 shape parameters
\(z,1/(1-z),(z-1)/z\) have positive imaginary part. These
inequalities use rational isolating intervals for the real and
imaginary parts of \(X\); the enclosure of \(\pi\) comes from
Machin's identity and rational alternating-series bounds.

At a tetrahedron with ideal vertices \((\infty,0,1,z)\), use
these coordinates on the four cusp triangles:
\[
\begin{array}{c|ccc}
v&\multicolumn{3}{c}{\text{coordinates at the other vertices}}\\ \hline
0&1:0&2:1&3:z\\
1&0:0&2:1&3:1/z\\
2&0:0&1:-1&3:1/(z-1)\\
3&0:0&1:-1/z&2:1/(1-z).
\end{array}                                                  \tag{4}
\]
A face pairing induces an affine similarity \(z\mapsto Lz+T\).
The verifier constructs scale factors satisfying
\(p_{\rm next}=p_{t,v}L\) on every cusp edge, including every
cycle of the dual graph. Thus all linear cusp holonomies are
one. The positive solution (3), the torus links, exact edge
winding and these cusp equations give the complete structure
on the original diagram complement.

## 4. The original complete periods

In the common developed scale, an oriented cusp edge contributes
\(T/p_{\rm next}\). If \(a_{t,v,f}\) is the signed flux of a
transported curve, its translation is
\[
 \frac12\sum_{t,v,f}a_{t,v,f}\frac{T_{t,v,f}}{p_{\rm next}}.     \tag{5}
\]
The factor \(1/2\) accounts for counting each glued edge from
both adjacent triangles. Reversing an edge changes both the
flux and its translation sign.

Substitution gives the exact identities
\[
\begin{split}
 \operatorname{trans}(\mu)&=-\frac{X^2+7X+7}{2},\\
 \operatorname{trans}(\lambda_{\rm PD})&=X^2-X-5.
\end{split}                                                   \tag{6}
\]
Consequently
\[
 \boxed{\displaystyle
 \frac{\operatorname{trans}(\lambda_{\rm PD})}
      {\operatorname{trans}(\mu)}
 =1+\frac1Y=\frac{-6X^2-14X+18}{17}.}                          \tag{7}
\]
No numerical cusp modulus or census-manifold identification
is used here.

## 5. Comparison with the two-pyramid collar

The actual complete collar in Section 9 of the subdivision
note has four side maps
\[
 f_j(z)=-Yz+c_j,\qquad
 (c_0,c_1,c_2,c_3)=(1+Y,1-Y,Y-1,-1-Y).
\]
Its locally labelled curves are
\[
 \mu_{\rm loc}=f_0f_1^{-1},\qquad
 \lambda_{\rm loc}=f_3f_0^{-1},
\]
with translations \(2Y\) and \(-2(Y+1)\). They form a
primitive basis. Indeed, the two quadrilateral cusp patches
have total area \(4\operatorname{Im}Y\) in this common scale,
and
\[
 \left|\operatorname{Im}
   \bigl(\overline{2Y}\,[-2(Y+1)]\bigr)\right|
                         =4\operatorname{Im}Y.
\]
Their translation subgroup therefore has index one.

Put \(\tau=-1-1/Y\). Its irreducible polynomial is
\[
                  17\tau^3+58\tau^2+72\tau+32=0.              \tag{8}
\]
The reduction modulo \(3\) has no root, proving irreducibility.

**Lemma 2.** Under the marked identification of the two
complete triangulations,
\[
 \mu=\epsilon\mu_{\rm loc},\qquad
 \lambda_{\rm PD}=-\epsilon\lambda_{\rm loc},
                       \qquad \epsilon\in\{1,-1\}.           \tag{9}
\]
There is no longitude shear or multiple of a primitive curve.

**Proof.** The recorded topological moves identify both
complete structures with the same oriented diagram complement.
Finite-volume hyperbolic rigidity identifies their complete
holonomies under this marking; see
[Prasad's strong rigidity theorem](https://repository.ias.ac.in/36364/1/36364.pdf).
Write
\[
 \mu=p\mu_{\rm loc}+q\lambda_{\rm loc},\qquad
 \lambda_{\rm PD}=r\mu_{\rm loc}+s\lambda_{\rm loc}.
\]
Both bases are primitive, so \(ps-qr=\pm1\). Equation (7)
gives
\[
 -\tau=\frac{r+s\tau}{p+q\tau},\qquad
 q\tau^2+(p+s)\tau+r=0.
\]
Its degree forces \(q=r=0\), \(s=-p\), and then \(p=\pm1\).
\(\square\)

The simultaneous sign in (9) does not change an unoriented
filling slope. The relative sign does matter: it reverses
the coefficient of a longitude when translating between
the two conventions.

## 6. From the complete periods to the marked deformation

The source's marked periods are
\[
 U=-2\pi S'(u)-iu,\qquad V=2iu,\qquad
 e^{-2\pi S'(u)}=\frac{Y(u)+e^{iu}}{1+Y(u)e^{iu}}.              \tag{10}
\]
At \(u=0\), its local collar ratio is \(\tau\). The source
uses the disk path \(\lambda=W_2^{-1}W_0\), crossing white
face \(0\) and returning through white face \(2\). The PD
longitude in Section 1 was independently oriented clockwise.
Equation (9) does not authorize changing the original disk
convention to make two formulas agree.

The [original collar representation proof](research_mixed_word_collar_representation.md)
now supplies the full comparison. It traces all four interface
arcs in the PD diagram, retains the carrier above the oval,
and gives a complete relative Wirtinger presentation. In its
notation the original meridian is \(\mu=h^{-1}\), while the
disk longitude is \(L=ba=rl\). The rational-word cap family
is exhaustive at the geometric point. Its complete cusp
polynomial, together with (7), selects exactly the geometric
representation and its auxiliary generator. The marked
gluing-germ theorem then identifies the entire holomorphic
period functions (10).

Thus the first-order calculation here is one input to that
argument. It does not replace the ordered group presentation.
The same proof gives the volume conjecture for the literal
mixed word followed by any sufficiently long fixed odd final
crossing power.

## 7. Reproduction

Run the single verifier:

    .venv/bin/python experiments/verify_mixed_peripheral_transport.py

An independent run can avoid replacing the saved report:

    .venv/bin/python experiments/verify_mixed_peripheral_transport.py \
      --output /tmp/mixed-peripheral-review.json

The files are:

- [Verification script](../experiments/verify_mixed_peripheral_transport.py).
- [Move and curve witnesses](../repro/fixtures/research-mixed-peripheral-transport.json).
- [Exact results](../repro/results/research-mixed-peripheral-transport.json).

The report records SHA256 hashes of the script, its fixture,
and the original diagram fixture. It checks the 56 peripheral
Pachner moves, every individual boundary flux, the complete
structure and (6)–(7). The full marked-germ proof cited in
Section 6 has its own exact representation verifier.

