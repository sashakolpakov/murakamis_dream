# The volume of a positive edge and its primitive action

For every positive configuration of the eight original edge tetrahedra,
their volume is
\[
 \boxed{\quad
 V_e(t,u)=2\pi\Re\psi(t,u)
       -2\{\Im t\,\Im r_t+\Im u\,\Im r_u\}.
 \quad}
 \tag{1}
\]
Here \(\psi\) is the original edge phase, normalized at completeness,
and \(r_t,r_u\) are its original marked meridian increments.
The identity holds throughout the positive edge domain. It is not
restricted to a filling path.

At a positive solution of the primitive filling equations, the
correction terms combine exactly with the quadratic crossing terms
and the linear filling charges. Thus the stationary action has the
absolute volume normalization, without a separate integration along
a common-charge cone path. One must still establish that the positive
cells with the prescribed marking realize the intended filled
manifold. This calculation does not replace that geometric assembly,
nor does it establish a quantum asymptotic.

## 1. The original shapes and branches

Use the
[positive edge domain](research_positive_edge_global_monotonicity.md)
and its strip coordinates \(P,Q\). Write
\[
 f(P)=\arctan(\tanh P),\qquad
 P=x+iy,\qquad f(P)=\alpha+i\beta,
 \tag{2}
\]
with \(|y|,|\alpha|<\pi/4\), and use the analogous notation for \(Q\).
The branches are fixed at \(P=Q=0\). The positive domain is
biholomorphic to the product of two unit disks, so the original
closed holomorphic period form has a single-valued primitive there.
We choose that primitive as
\[
 d\psi=-\frac1\pi(r_t\,dt+r_u\,du),\qquad
                   \psi(0,0)=\frac{4G}{\pi},
 \tag{3}
\]
where \(G=D(i)\) is Catalan's constant and \(D\) is the
Bloch--Wigner dilogarithm.

The ordered original shapes are
\[
                   (A,B,-1/A,-1/B),\qquad
                   (C,D_0,-1/C,-1/D_0).
 \tag{4}
\]
The symbol \(D_0\) denotes a tetrahedron shape; \(D(z)\) always
denotes its volume function. The exact coordinate expressions are
\[
 \begin{array}{ll}
 C=i e^{-2P},&
 B=i e^{2if(P)}=(C-1)/(C+1),\\[2mm]
 A=i e^{2Q},&
 D_0=i e^{2if(Q)}=(A+1)/(1-A).
 \end{array}
 \tag{5}
\]
They are obtained from the original ordered cross ratios in
[the corner geometry note](research_square_corner_flat_geometry.md),
Section 1. Every shape in (4) lies in the upper half-plane.
The two groups associated to \(P\) and \(Q\) are interleaved
between the original octahedra; regrouping their volumes does
not change their face attachments.

## 2. A differential calculation for four tetrahedra

The Bloch--Wigner function can be defined locally by
\[
 D(z)=\Im\operatorname{Li}_2(z)+\log|z|\arg(1-z).
 \tag{6}
\]
The expression is single valued after continuation. Differentiating,
using \(d\operatorname{Li}_2(z)=-\log(1-z)\,dz/z\), gives
\[
 dD(z)=\log|z|\,d\arg(1-z)-\log|1-z|\,d\arg z.
 \tag{7}
\]
The inversion identity \(D(1/z)=-D(z)\) follows either from
(6) or by differentiating its two sides using (7) and fixing
the constant at \(z=i\), where complex conjugation gives the
required sign.

Put
\[
                       H(z)=D(z)-D(-z).
 \tag{8}
\]
Then \(D(z)+D(-1/z)=H(z)\).
If \(w=(z-1)/(z+1)\), subtraction in (7) gives
\[
 dH(z)=\log|z|\,d\arg w-\log|w|\,d\arg z.
 \tag{9}
\]
The same transformation sends \(w\) to \(-1/z\). Hence
\[
                            dH(w)=dH(z).
 \tag{10}
\]
Only derivatives of arguments occur, so these equations require
no arbitrary argument constant.

For the \(P\)-group in (4), take \(z=C\), \(w=B\). Its volume is
\[
 V_P=D(C)+D(-1/C)+D(B)+D(-1/B)=H(C)+H(B).
 \tag{11}
\]
The strip coordinates give
\[
 \log|C|=-2x,\quad d\arg C=-2\,dy,\qquad
 \log|B|=-2\beta,\quad d\arg B=2\,d\alpha.
 \tag{12}
\]
Equations (9)--(12) therefore imply
\[
                       dV_P=-8(x\,d\alpha+\beta\,dy).
 \tag{13}
\]

For the \(Q\)-group, take \(z=A\) and
\(w=(A-1)/(A+1)=-1/D_0\).
Since \(H(-1/z)=H(z)\), its volume is again \(H(z)+H(w)\).
Now
\[
 \log|A|=2x,\quad d\arg A=2\,dy,\qquad
 \log|D_0|=-2\beta,\quad d\arg D_0=2\,d\alpha.
 \tag{14}
\]
Substitution in (9), with \(w=-1/D_0\), gives the same formula:
\[
                       dV_Q=-8(x\,d\alpha+\beta\,dy).
 \tag{15}
\]
At the origin, each group consists of four shapes equal to \(i\)
and has volume \(4G\).

Let \(E(\alpha,y)\) be the normalized square energy from
[the convex variation](research_positive_filling_convex_variation.md),
so \(dE=x\,d\alpha+\beta\,dy\) and \(E(0,0)=0\).
The calculation proves the useful absolute identity
\[
                      V_P=4G-8E_P,\qquad
                      V_Q=4G-8E_Q.
 \tag{16}
\]
In particular the strict convexity of \(E\) is precisely strict
concavity of the corresponding four-tetrahedron volume in these
angle coordinates.

## 3. Converting to primitive boundary coordinates

Write
\[
 t=s_t+ih_t,\quad u=s_u+ih_u,\qquad
 r_t=k_t+ig_t,\quad r_u=k_u+ig_u.
 \tag{17}
\]
The exact linear period identities give
\[
       4\,d(E_P+E_Q)
            =k_t\,ds_t+k_u\,ds_u+h_t\,dg_t+h_u\,dg_u.
 \tag{18}
\]
Consequently (13) and (15) imply
\[
             dV_e=-2(k_t\,ds_t+k_u\,ds_u
                                      +h_t\,dg_t+h_u\,dg_u).
 \tag{19}
\]
On the other hand, (3) gives
\[
              2\pi\,d\Re\psi
                  =-2(k_t\,ds_t+k_u\,ds_u-g_t\,dh_t-g_u\,dh_u).
 \tag{20}
\]
Subtracting \(2\,d(h_tg_t+h_ug_u)\) produces (19).
At completeness \(h_t=h_u=0\), \(V_e=8G\), and
\(2\pi\psi(0,0)=8G\). The positive domain is connected.
This proves (1), including its absolute additive constant.

Thus the formula uses the original volume of eight ordered
tetrahedra. In particular one cannot replace
\(D(-1/z)\) by \(D(z)\) away from special configurations.
The difference \(H(z)=D(z)-D(-z)\) in (8) is what makes the
calculation valid on the full domain.

## 4. A stationary action on an arbitrary selected region

Let \(S\) be any finite selected set in an original circle tree,
and include each original edge incident to \(S\) exactly once.
Boundary variables at unselected ends are denoted \(u_b\).
Assume all these edge configurations are positive, with their
original branch and marking. Define
\[
 \Psi(\mathbf t,\mathbf u)=\sum_e\psi(t_{v(e)},t_{w(e)}),
 \tag{21}
\]
where a boundary endpoint uses its \(u_b\).
For each selected vertex take a real crossing power \(n_v\)
and a real filling charge \(c_v\), and impose the original
logarithmic equations
\[
             \sum_{e\ni v}r_{v,e}
                    =\frac{i n_v}{2}t_v-\pi i c_v.
 \tag{22}
\]
Equivalently,
\(\Psi_{t_v}+in_vt_v/(2\pi)=ic_v\).
Let
\[
 \mathcal S=
 \Psi+\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
                                    -i\sum_{v\in S}c_vt_v.
 \tag{23}
\]
This is evaluated at a solution of (22); no assertion about
its quantum coefficient is part of the notation.

**Theorem.** The sum \(V_{\rm cells}\) of the original positive
tetrahedron volumes satisfies
\[
 V_{\rm cells}
    =2\pi\Re\mathcal S
       -2\sum_{b\notin S}\Im u_b
                       \sum_{\substack{e\ni b\\e\text{ included}}}
                                      \Im r_{b,e}.
 \tag{24}
\]
In particular, when the outside angles are complete,
\[
                         V_{\rm cells}=2\pi\Re\mathcal S.
 \tag{25}
\]

**Proof.** Sum (1) over the included edges.
At a selected vertex put \(s_v=\Re t_v\) and \(h_v=\Im t_v\).
The imaginary part of (22) gives
\[
                  \sum_{e\ni v}\Im r_{v,e}
                                  =n_vs_v/2-\pi c_v.
 \tag{26}
\]
Its contribution to the correction in (1) is therefore
\[
              -n_vs_vh_v+2\pi c_vh_v
         =2\pi\Re\left\{\frac{in_vt_v^2}{4\pi}-ic_vt_v\right\}.
 \tag{27}
\]
Boundary incidences give the remaining terms of (24).
No limiting operation is used. \(\square\)

All original carrier conventions remain in force:
\(n_v=\eta_v-2p_v\) when the power comes from the original
integral filling coefficient \(p_v\) and carrier \(\eta_v\).
Equation (23) uses that \(n_v\) once. It does not introduce
another carrier term per incident edge.

## 5. The geometric and analytic obligations left by this identity

The result calibrates the action whenever the specified positive
configuration is available. If its original face attachments and
primitive peripheral curves realize a complete filling, the cell
volume in (25) is the hyperbolic volume of that filled manifold:
the tetrahedron interiors partition its nonsingular part, and the
filled cores have volume zero. This is an implication with the
geometric realization stated as a hypothesis.

For example, the
[negative-corridor criterion](research_negative_corridor_variational_bounds.md)
gives a positive primitive solution at unit charges when all
selected crossing magnitudes are at least four, independently
of the path length. Formula (25) now gives its absolute
cell-volume anchor directly. The existence of a common-charge
cone path is not needed for that calculation.
The separate
[pointwise marked-completion theorem](research_positive_point_marked_completion.md)
verifies the face assembly, full primitive periods and solid-torus
completion for every positive critical point with the required
strict core signs. It therefore supplies the actual marked
hyperbolic-volume interpretation for this corridor class.

Neither this identity nor existence and uniqueness of the positive
solution supplies the coefficient of its saddle in the original
root-of-unity period. The whole-source estimate and noncancellation
problem remain separate.

## 6. An explicit holomorphic primitive

The period normalization can also be checked without integrating
along a selected path. On the full strip \(|\Im P|<\pi/4\), define
\[
 F(P)=\frac{\pi P}{4}
   +\frac{i}{4}\left\{
        \operatorname{Li}_2(-i e^{-2P})
                 -\operatorname{Li}_2(i e^{-2P})\right\}
   -\frac G2.
 \tag{28}
\]
The two dilogarithm arguments lie respectively in the lower and
upper half-planes, so they avoid the principal cut \([1,\infty)\).
Differentiation gives
\[
 F'(P)=\frac\pi4+\frac i2
             \log\frac{1+i e^{-2P}}{1-i e^{-2P}}
                  =\arctan(\tanh P)=f(P).
 \tag{29}
\]
The branch identity is fixed at \(P=0\) and continued on the
strip. Also \(F(0)=0\), because
\(\operatorname{Li}_2(i)-\operatorname{Li}_2(-i)=2iG\).

The original edge phase therefore has the explicit expression
\[
 \boxed{\quad
 \psi(t,u)=\frac1\pi\left[
 4G-2(P+Q)\{f(P)+f(Q)\}+4\{F(P)+F(Q)\}
                         \right].
 \quad}
 \tag{30}
\]
To verify it, use the exact strip identities
\[
 t=2\{f(P)+f(Q)\},\quad u=-2i(P-Q),\quad
 r_t=P+Q,\quad r_u=i\{f(Q)-f(P)\}.
 \tag{31}
\]
Differentiating (30) gives (3), and its complete value is
\(4G/\pi\). Thus (30) is the same original branch used in (1).
It provides a separate expression for numerical or symbolic
checks of the volume identity.

## 7. Reproducing the finite comparisons

The separate
[checker](../experiments/check_positive_edge_volume_identity.py)
compares the eight original Bloch--Wigner volumes with (1) and
the explicit primitive (30), including points well outside the
small complete chart. At selected points it also integrates
the original meridian differential independently.
It includes stationary boundary-correction checks for (24).

    .venv/bin/python experiments/check_positive_edge_volume_identity.py \
      --precision 120 --output /tmp/positive-edge-volume-replay.json

The [saved replay](../repro/results/research-positive-edge-volume-identity-root.json)
contains 24 edge comparisons, eight independently integrated
period comparisons, and four stationary correction comparisons.
Its script SHA256 is
1ab9a944c378fbc3fdd99c0aa48c23656b9d1487ed30816dffb5b270892ac98a.
These finite comparisons check the conventions; the differential
proof above establishes the identities on the entire domain.

## 8. A quantitative comparison for other primitive charges

The volume identity also gives a comparison on the entire closed
angle domain, without constructing a filling path for the competing
charges. Keep a fixed selected region, the original real powers
\(n_v\), zero outside angles, and the original edge-angle relations.
Assume there is an interior solution at unit charges with
\(t_v^*=s_v^*+ih_v^*\), where \(h_v^*<0\).
The pointwise completion theorem supplies its marked hyperbolic
interpretation when \(n_v=\eta_v-2p_v\) for the original integral
slopes.

For every included edge use the two square coordinates of (16).
Collect them in the real vector
\[
 X=(A_{P,e},y_{P,e},A_{Q,e},y_{Q,e})_e,\qquad
 \mathcal E(X)=4\sum_e(E_{P,e}+E_{Q,e}).
 \tag{32}
\]
The coordinates retain a shared real angle \(s_v\) at each vertex.
They obey
\[
 \sum_{e\ni v}g_{v,e}-\frac{n_v}{2}s_v=-\pi c_v
 \quad(v\in S),\qquad s_b=0\quad(b\notin S).
 \tag{33}
\]
Here the charges \(c_v\) are allowed to be any real numbers.
The comparison also allows closed squares, and does not require
matching the imaginary angles of the competing cells. This larger
domain is useful for an upper bound. Define its continuous volume
function by
\[
 V_{\rm ang}(X)=8G\,|E_{\rm inc}|-2\mathcal E(X).
 \tag{34}
\]
On positive configurations it is the sum of the original eight
tetrahedron volumes, by (16). Equation (34) defines its continuous
extension to the closed squares.

Let \(X^*\) be the unit-charge solution, and put
\[
 \delta=\min_\nu\{\pi/4-|X_\nu^*|\}>0,\qquad
 \kappa=\frac{\delta}{\pi}\sin^2\delta.
 \tag{35}
\]

**Theorem 2.** Every closed-square assignment satisfying the same
real matching equations and (33) obeys
\[
 \boxed{\quad
 V_{\rm ang}(X)
 \le V_{\rm ang}(X^*)+
           2\pi\sum_{v\in S}h_v^*(c_v-1)
           -2\kappa\|X-X^*\|_2^2 .
 \quad}
 \tag{36}
\]
In particular, if all \(c_v\ge1\), any increase in a charge has a
strict volume cost. With the actual core lengths
\(\ell_v=-2h_v^*\), this cost is at least
\(\pi\sum_v\ell_v(c_v-1)\).

**Proof.** At the unit solution, (18) and the real parts of
the primitive equations give
\[
 \begin{split}
 d\mathcal E_{X^*}(X-X^*)
 &=\sum_{v\in S}h_v^*
       \left(\sum_{e\ni v}\Delta g_{v,e}
                         -\frac{n_v}{2}\Delta s_v\right)\\
 &=-\pi\sum_{v\in S}h_v^*(c_v-1).
 \end{split}
 \tag{37}
\]
The outside terms vanish: their real angles stay zero, and their
imaginary angles at \(X^*\) are zero. This calculation keeps every
incidence of the original region.

For clarity, the explicit quadratic remainder in the supporting
inequality follows from the square Hessian
\[
 E''(A,y)=\frac1{\sqrt{1-\sin^2(2A)\sin^2(2y)}}
 \begin{pmatrix}
  \cos(2y)/\cos(2A)&-\sin(2A)\sin(2y)\\
  -\sin(2A)\sin(2y)&\cos(2A)/\cos(2y)
 \end{pmatrix}.
 \tag{38}
\]
Its determinant is one. On
\(\lvert A\rvert,\lvert y\rvert\le\pi/4-\delta/2\),
its trace is at most \(2/\sin^2\delta\), so
\(E''\ge(\sin^2\delta/2)I\).

Write \(D=X-X^*\). Every coordinate of \(D\) has magnitude at
most \(\pi/2\). For \(0\le r\le r_0=\delta/\pi\), the segment
\(X^*+rD\) lies in the smaller square just used. Hence
\(\mathcal E''\ge2\sin^2\delta\,I\) on this initial segment.
Convexity holds on the rest of the segment. The integral form
of the supporting-plane remainder therefore gives
\[
 \begin{split}
 \mathcal E(X)-\mathcal E(X^*)
             -d\mathcal E_{X^*}D
 &\ge2\sin^2\delta\,(r_0-r_0^2/2)\|D\|_2^2\\
 &\ge\kappa\|D\|_2^2.
 \end{split}
 \tag{39}
\]
For a boundary endpoint, apply the inequality first along the
open segment and pass to its endpoint using continuity of the
square energy. Combining (34), (37) and (39) proves (36).
\(\square\)

If a competitor is itself an actual positive critical point
for the charges \(\mathbf c\), the earlier volume identity gives
\[
 \Re\mathcal S_{\mathbf c}
 \le \Re\mathcal S_{\mathbf1}
       -\sum_v |h_v^*|(c_v-1)
       -\frac{\kappa}{\pi}\|X-X^*\|_2^2
                    \qquad(\mathbf c\ge\mathbf1).
 \tag{40}
\]
This compares the normalized original actions, including their
additive constants. Every nontrivial integer charge vector with
\(c_v\ge1\) therefore has a gap of at least
\(\min_v|h_v^*|\) in its real action. At unit charges, (36)
also bounds every point outside a fixed angle neighborhood
strictly below the geometric volume.

The compared configurations have the same original edge relations.
They change only the primitive filling charges. This is not a
bound for arbitrary shifted internal edge equations or for a
different tetrahedral subdivision. In particular it does not
apply to the [wrong-edge alias face counterexample](positive_geometric_alias_volume_counterexample.md).
The earlier [Legendre contour construction](general_legendre_rivin_contour.md)
already separates positive peripheral competitors from those
other faces. The explicit core-length bound (36) supplies that
comparison here in the original circle-tree coordinates.

No quantum contour has been changed in this argument. To use
(40) for the finite source, its competing contributions must
first be represented in these original positive cells, with
their amplitudes and boundary terms retained. The volume
comparison does not establish that representation or the
coefficient of the geometric contribution.

## 9. The signed identity on regular continuations

Positivity was needed to interpret every tetrahedron volume as
positive and to obtain the convex comparison above. It is not
needed for the differential identity itself. This distinction
allows a comparison of other regular critical values on the same
marked source branch.

Consider any regular analytic continuation of the original edge
from its complete configuration. All shape parameters and face
maps are retained in their original order. The continuation avoids
zero, one and infinity for every tetrahedron shape, as well as the
singularities of the original face charts. Continue the angle
logs, the meridian logs and \(\psi\) along this path. They are not
reset to principal values at its endpoint. Define
\[
 V_e^{\rm sgn}=
 D(A)+D(B)+D(-1/A)+D(-1/B)
 +D(C)+D(D_0)+D(-1/C)+D(-1/D_0).
 \tag{41}
\]
Here the Bloch--Wigner function assigns its usual signed volume;
some terms may be negative or zero.

**Proposition 3.** On every such continued branch,
\[
 V_e^{\rm sgn}=2\pi\Re\psi
       -2\{\Im t\,\Im r_t+\Im u\,\Im r_u\}.
 \tag{42}
\]

**Proof.** The differential (7), inversion identity and calculation
(9)--(10) hold without a half-plane restriction. Locally along
the continuation choose the continued logarithms
\[
 C=i e^{-2P},\qquad A=i e^{2Q},\qquad
 B=i e^{2if(P)},\qquad D_0=i e^{2if(Q)}.
 \tag{43}
\]
The rational relations (5) and the period identities (31)
continue from the complete point. The functions denoted by
\(f(P)\) and \(f(Q)\) in (43) are the continued branches, not
new principal inverse tangents. Thus (12)--(15) and (18)--(20)
remain identities of real differentials in each local chart.
In particular
\[
 dV_e^{\rm sgn}
   =d\!\left[2\pi\Re\psi
                    -2(\Im t\,\Im r_t+\Im u\,\Im r_u)\right].
 \tag{44}
\]
The two sides agree at completeness. Integration along the
specified path proves (42). Overlapping logarithmic charts
use the same continued periods. A winding change in an
individual term of (42) is therefore not an independent
normalization freedom. The argument also applies when a
shape crosses the real axis away from zero and one, since
the Bloch--Wigner function and its differential extend there.
\(\square\)

One loop makes the role of the boundary correction explicit.
Keep \(Q\) fixed and wind once around \(P_0=i\pi/4\), avoiding
that point and every other chart singularity. Since
\(f'(P)=\operatorname{sech}(2P)\) has residue \(1/(2i)\) there,
the continued quantities satisfy
\[
 \Delta f(P)=\pi,\qquad
 \Delta F(P)=\pi(P-P_0),\qquad
 \Delta\psi=2P-2Q-4P_0.
 \tag{44a}
\]
The middle identity follows by integrating \(f\,dP\) by parts
and evaluating the residue of \(P f'(P)\).
The real part of \(\psi\) generally changes. But
\(\Delta r_u=-i\pi\), \(\Delta t=2\pi\), and
\(\Im u=-2\Re(P-Q)\). These changes cancel exactly in
(42), as the unchanged signed shape volume requires.

Sum this identity on an original circle tree, along one common
regular network continuation from completeness. Suppose the
outside angles remain zero and the selected equations are
\[
 \sum_{e\ni v}r_{v,e}
              =\frac{i n_v}{2}t_v-\pi i c_v,\qquad c_v\in\mathbb Z.
 \tag{45}
\]
The same algebra as (26)--(27), without a sign assumption on
the shapes, proves
\[
       \sum_e V_e^{\rm sgn}=2\pi\Re\mathcal S_{\mathbf c}.
 \tag{46}
\]
In (46) every original edge is included. Complete edges outside
the selected region contribute their original constant \(8G\).

There is a direct representation interpretation when the filled
peripheral matrices have distinct fixed points. In addition to
the regularity above, assume
\[
             e^{2it_v}\ne1\quad(v\in S),\qquad
             n_v=\eta_v-2p_v,\quad p_v\in\mathbb Z.
 \tag{47}
\]
The original rational face identities give an equivariant
development of the same cut triangulation and a representation
of its exterior group. This is an algebraic face-cocycle
construction; it does not require positive developed tetrahedra.
The original peripheral matrix words still have multipliers
\[
 U_v=2\sum_{e\ni v}r_{v,e}-i\eta_vt_v,\qquad V_v=2it_v.
 \tag{48}
\]
Equation (47) makes the longitude semisimple with two distinct
fixed points. The original cusp decoration is a common retained
fixed point of the longitude and meridian. Since the meridian
also commutes with the longitude, it fixes the other point as
well. The retained common flag is essential here: commutation
alone in \(\mathrm{PSL}_2(\mathbb C)\) would permit an interchange
of the two fixed points when the longitude has multiplier
\(-1\). By (45),
\(U_v+p_vV_v=-2\pi i c_v\), so their primitive filling product
has multiplier one and fixes both points. It is the identity
in \(\mathrm{PSL}_2(\mathbb C)\), not merely a matrix with a
unit eigenvalue. Thus the representation descends to the
original marked filling \(M=Y(\mathbf p)\).

The original oriented ideal chain computes the signed sum in
(46). It computes the representation volume on the filling as
well: replace the old cusp map by the equivariant axis map,
using a face-compatible conical homotopy whose boundary volume
tends to zero, then extend the same boundary triangulation
over the filling solid torus with its vertices on that axis.
Every added tetrahedron has zero volume. The details and the
\(O(Y^{-2})\) boundary estimate are proved in
[the peripheral representation-volume calculation](general_peripheral_representation_volume_bound.md),
Section 2, and
[the filling-chain normalization](general_source_regulator_hyperbolic_equality.md),
Section 6. The original chain and peripheral curves are the
ones used here; no new regulator constant is chosen.

Consequently, when \(M\) is hyperbolic, the proved
[representation-volume inequality](general_peripheral_representation_volume_bound.md)
gives
\[
       |2\pi\Re\mathcal S_{\mathbf c}|
                     =|\operatorname{Vol}(\rho)|
                     \le\operatorname{Vol}(M).
 \tag{49}
\]
This is a bound for the specified regular continued critical
values, with their full original logarithmic branches.
It gives neither a strict gap nor the coefficient of a
critical point in the quantum period.

The hypotheses matter. A singular face chart, an escaping
decoration, or a selected longitude with multiplier one is
not disposed of by this argument. In the last case, the
exponentiated filling relation alone need not kill a
nontrivial unipotent matrix. Nor has every term obtained
by a different quantum interpolation been identified with
a regular continuation in (41)--(48). Those comparisons
and the original relative integration cycle remain part
of the source theorem.

The [action-comparison checker](../experiments/check_circle_tree_action_comparisons.py)
compares the quantitative supporting inequality at 24 angle
assignments, the signed identity at four configurations outside
the positive domain, and the logarithmic loop (44a) by direct
contour integration. The [saved record](../repro/results/research-circle-tree-action-comparisons-root.json)
uses 110-digit arithmetic; its input critical points are stored
to forty significant digits in the separate corridor record.
Those finite checks verify the formulas and branch conventions,
not the general representation-volume theorem.

    python3 experiments/check_circle_tree_action_comparisons.py \
      --precision 110 --output /tmp/circle-tree-action-comparisons.json
