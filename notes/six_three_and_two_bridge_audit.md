# A certified state beyond twist knots, and the two-bridge obstruction

Research note, 25 October 2026. The state definition remains the published
Faddeev integral, with the independently proved analytic and annihilator
results in [literature_state_volume.md](literature_state_volume.md) and
[general_annihilator_and_volume.md](general_annihilator_and_volume.md).
This note supplies new complete finite certificates for the knot 6_3. It
does not prove the all-two-bridge or all-alternating assertion.

## 1. The folded layering is explicit

We use the combinatorics of the appendix of Guéritaud--Futer,
[arXiv:math/0406242](https://arxiv.org/abs/math/0406242), as construction
data. Its volume-maximization theorem is not an assumption in the geometric
certificate below.

Label the four punctures of every level sphere 0,1,2,3. Its three pairs
of opposite edges have classes

    0: (01,23),     1: (02,13),     2: (03,12).

For an R/L word Omega of length c>=2, set m_0=0, m_1=1, and

    m_(i+1)=m_(i-1)                  if Omega_i=Omega_(i+1),
             3-m_(i-1)-m_i          otherwise.

Layer i, 1<=i<c, flips the two edges in class m_i and contains two
tetrahedra. For an old edge ab, its tetrahedron has bottom faces abc,abd
and top faces acd,bcd, where {a,b,c,d}={0,1,2,3}. Intermediate faces
are glued by their physical puncture labels. At either end fold along
class m_0 or m_c: the faces opposite a and b are identified by the
transposition (ab), fixing their common edge.

This gives every face permutation without solving hyperbolic equations.
Topologically each layer is the product between the two triangulations
of the four-punctured sphere. The end fold attaches the rational clasp:
its two paired triangles are a regular neighborhood of the meridional
disk in the end rational tangle. Thus the construction is the usual
two-bridge diagram specified by Omega. For Omega=RLRL the syllable
lengths are (1,1,1,1); including the end crossings gives Conway
[2,1,1,2], whose continued fraction is 13/5. This is 6_3.

The algorithm is implemented in
[layered_two_bridge.py](../experiments/layered_two_bridge.py). Optional
Regina/SnapPy comparisons give the expected combinatorial isomorphism
signatures and knot names. The construction itself does not depend on
that recognition.

## 2. A proper ordering and the preferred longitude for 6_3

For RLRL there are six tetrahedra. In layer order, choose vertex orders

    0123, 0123, 0213, 0123, 0213, 0213.

The resulting face rows and signs are

    (f0,f1,f2,f3),    +
    (f1,f4,f3,f5),    +
    (f6,f2,f4,f7),    +
    (f0,f8,f9,f5),    -
    (f10,f9,f11,f7),  -
    (f6,f10,f8,f11),  - .

Equal labels are glued preserving the order of their three vertices.
The face matrix defined in the preceding notes has determinant -1.

Here is an independent preferred-longitude certificate. Use the explicit
normal cusp cycles alpha and beta recorded in
[certify_six_three.py](../experiments/certify_six_three.py). Their dual
cellular chains have linking numbers 1,1 under an integral primitive
generator of H^1(M;Z). The cellular Smith calculation gives H_1(M)=Z,
and their oriented cusp intersection is -1. Moreover

    [beta-alpha] = boundary_2 * (-3,1,-2,1,3,-1)^T.       (2.1)

The matrix boundary_2 is recomputed by walking once around each global
edge; no presentation of the knot group is assumed. Equation (2.1) is
an integral chain identity, not just a numerical vanishing of holonomy.
It proves that l=beta-alpha is a primitive, nullhomologous peripheral
class, hence the preferred longitude up to sign.

For reproducibility, in physical angle coordinates (a_j,b_j,c_j) the
normal-curve rows are

    alpha: (0,0,-1 | 1,0,0 | 0,0,0 | 0,0,-1 | 0,0,0 | 0,0,0),
    l:     (-1,0,1 | -1,1,1 | 1,-2,0 | 1,0,1 | 1,0,0 | 0,-1,-1).

An optional exact combinatorial isomorphism to SnapPy's marked 6_3
triangulation calibrates alpha to its standard meridian and l to its
negative standard longitude. The differences of the angle rows are
given as rational combinations of the tetrahedron/edge constraints
with zero affine constant. Thus the calibration retains the logarithmic
branch as well as the homology classes. This software calibration is
recorded separately from the integral preferred-longitude proof (2.1).

The common face/edge Gaussian is

    G = [ 1  1  1  1  0  0 ]
        [ 1  1  1  1  0  0 ]
        [ 1  1 -1  0 -1 -1 ]
        [ 1  1  0  2 -1 -1 ]
        [ 0  0 -1 -1  0 -1 ]
        [ 0  0 -1 -1 -1  0 ].

Every edge row and the separately certified longitude row satisfy A=B G.
Omit the first of the six edge rows and append l. Then

    det B=2,   B^(-1)A=G,
    p=2B^(-1)e_6=(1,1,-1,1,-1,-1)^T,
    gamma=0,
    c_0/pi=(-2,-2,1,-1,2,2)^T.                           (2.2)

The edge identity can also be obtained from the general independent
[Stokes proof](face_edge_stokes_identity.md). The preferred-longitude
identity here is checked with its actual normal-curve row.

## 3. Complete positive shapes by rational arithmetic

Use an all-positive tetrahedron vertex convention for the following
shape computation. The exact vertex maps from the preceding layering
to this convention are identities except that vertices 2 and 3 are
interchanged in tetrahedra 2 and 3, with tetrahedra numbered from zero.
The shapes in this convention are

    (a,a,b,b,c,c),
    P(c)=c^6-3c^5+5c^4-4c^3+2c^2-c+1=0,
    a=-c^5+2c^4-3c^3+2c^2-c+1,
    b=-c^5+3c^4-5c^3+4c^2-c.                            (3.1)

These are native geometric shape parameters. For the signs used in
Section 2, the positive literature shape at each newly selected quad is
its uniform inverse conjugate. This preserves angles and Bloch--Wigner
volume. The convention is made explicit in the subsequent singular-face
note; the native quad modulus itself should not be inserted in a
Gaussian with the opposite global orientation.

There is exactly one root c in the disc

    |c-c_*|<r,  c_*=(841164+1200143 i)/10^6, r=10^(-5).

To certify this, write P(c_*+w)=sum_{k=0}^6 p_k w^k. The exact rational
inequality checked in the script is

    |p_0|_1+sum_(k=2)^6 |p_k|_1 r^k
         < (r/20) max(|Re p_1|,|Im p_1|),                (3.2)

where |z|_1=|Re z|+|Im z|. The right side is at most
|p_1|r/20. On |w|=r the remainder from p_1 w is therefore strictly
smaller than |p_1 w|. Rouché's theorem gives one root, including
multiplicity. The actual rational ratio to the displayed derivative
lower bound is less than 0.043491; the proof uses the exact inequality
(3.2).

Taylor expansion of a(c),b(c) on the same disc gives rational rectangular
enclosures. In particular all three shapes have 0<Re z<1 and Im z>0.
The exact polynomial certificate reduces the numerator of every
multiplicative edge equation to zero modulo P. For example three of
the equations in paired variables are

    a^2 b^2 c=1,
    (a^2 b-a^2-a+1)(a^2 b-a^2+a-1)=0,
    (bc-c^2+c-1)(bc+c^2-3c+1)=0.

The full six edge equations and two imported peripheral equations are
recorded in the script. Independently, the multiplicative equations
for the normal cycles alpha and l from Section 2 also reduce to zero
modulo P. No peripheral completeness conclusion is inferred merely
from numerically small residuals.

It remains to fix logarithmic branches. For each enclosure of z=x+iy,
bound

    Arg z=atan(y/x),  Arg z'=atan(y/(1-x)),
    Arg z''=pi-Arg z-Arg z'.

All bounds are rational: range-reduce atan with its elementary inversion
and pi/4 identities, then use 24 terms of the alternating power series
on [-1/2,1/2]. Machin's identity supplies a rational enclosure of pi.
The resulting edge sums lie in (pi,3pi), while the two normal peripheral
sums lie in (-pi,pi). Their exponentials are exactly 1, so the sums are
respectively 2pi and zero. Every dihedral angle is greater than 69/100
radians; this last inequality is checked between rational bounds.

Thus the six positive ideal tetrahedra glue without edge cone defects.
Both generators of the cusp have trivial complex linear holonomy.
Consistently scaled horospheres therefore glue to a compact flat torus,
which is complete. This constructs a complete positive geometric
triangulation. The numerical values, included only to locate the root,
are

    a=0.1588360981+1.2001426273 i,
    b=0.2327856159+0.6413907459 i,
    c=0.8411639019+1.2001426273 i.

## 4. The resulting literature state and volume theorem

Let h=b_quantum^2/(1+b_quantum^2)^2; b_quantum denotes the quantum
parameter rather than the middle shape in (3.1). Put
v=(-2,-2,1,-1,2,2)^T and let G,p be as in (2.2). The specified printed
literature state is now the completely explicit five-dimensional integral

    J_6_3(h,x)=-(2pi sqrt(h))^(-6)
       integral_(p.y=x)
         exp[(-i y^T G y/2+pi v^T y)/(2pi h)]
         product_(j=1)^6 Phi_(b_quantum)(y_j/(2pi sqrt(h)))
         dy_2 ... dy_6.                                  (4.1)

Choose the horizontal contour through the geometric saddle at x=0 and
continue it for small x. The printed and oriented coarea conventions
coincide here because p_1^2=1; the leading minus sign is p_1/det(script-A).
The full tensor level phase is the one in the preceding phase audit;
it is not silently used to rescale (4.1).

All hypotheses of Theorem 5.1 of the literature-state note have now
been checked independently. Consequently

    lim_(h->0+) -2pi h log|J_6_3(h,0)|
       =2[D(a)+D(b)+D(c)]=Vol(S^3\6_3).                   (4.2)

Here D is Bloch--Wigner volume. Its approximate value is
5.6930210912813007651. The positivity/concavity proof also makes J_6_3
nonzero for all sufficiently small h; this is an actual complex state
asymptotic, not a formal critical-value calculation.

The independent annihilator theorem gives a nonzero minimal quantum
A-operator for this same state in the Andersen--Malusà b-shift convention.
With t_0=x/(2pi sqrt(h)), its variables are

    q=exp(2pi i b_quantum^2),
    Q=exp(-2pi b_quantum t_0),    E:t_0 -> t_0-i b_quantum,
    E Q=q Q E.

The peripheral matrices give, exactly,

    A_alpha-B_alpha G=p^T,
    B_alpha B^(-1)e_6=0.

Hence x=-H_alpha at the classical constrained saddle, with no longitude
mixing, and its classical branch is

    Q=exp(H_alpha),     E=exp(H_l/2).

For the calibrated standard longitude, H_l=-H_longitude. Thus the branch
uses the inverse square root of the standard longitude eigenvalue ratio;
an SL(2) lift still needs its sign convention. This is recorded rather
than identified with unqualified variables M,L.

The geometric peripheral factor divides the classical symbol of the
minimal annihilator by the proved saddle argument. An explicit full
coefficient list, absence of additional classical factors, and equality
with a Jones-defined AJ operator have not been established. No generic
factor has been canceled by specializing Q=1.

## 5. Why the uniform two-bridge extension still requires work

The simplest extension would assert that every canonical layered
triangulation has a compatible proper ordering. This fails for the
explicit canonical triangulation of 6_2: all 16 global branchings have
singular script-A. The exhaustive search constructs each admissible
local total order, enforces order agreement on every glued face, and
reaches the end of its finite tree; this is not a failed bounded random
search. Similar singularities occur in the examples 7_3,7_4,7_5,7_7.

Even the repeated alternating word is insufficient: RLRL is proper,
but all 280 branchings of RLRLRLRL (the 10_45 canonical layering) are
singular. Thus a periodic Farey pattern alone does not supply the
missing theorem.

These facts concern this matrix chart. They are not obstructions to
other geometric triangulations or to a more general oscillatory
description of the literature tensor. A uniform constructive change
of chart, a suitable certified geometric move sequence, or a direct
analysis that allows a singular face matrix is required by that approach.
The subsequent [singular-face note](singular_faces_and_six_two.md) supplies
such a direct Fourier reduction under explicit rank conditions, and a
complete application to 6_2. Uniform membership and global state
identifications remain to be proved.

Reproduce the exact certificate with

    python3 experiments/certify_six_three.py

and the separate topology/marking calibration with

    .venv/bin/python experiments/certify_six_three.py --topology

The new scripts also record finite branching and face-matrix diagnostics
in `two_bridge_results.json` and `layered_two_bridge_results.json`.
