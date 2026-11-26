# The marked boundary geometry of an attached reflected pair

The closed reflected knot and a reflected pair attached to another
tangle have different primitive equations. This note proves the
geometric statement for the attached piece
\[
                  F_k=T(R^{-2k}T(R^{2k})),\qquad k\ge2.
                  \tag{1}
\]
Its original selected vertices have degrees one and two. The second
vertex retains one outgoing edge and its original free circle.
There is a positive realization in the original edge cells, with
both prescribed fillings, on one complex boundary disk independent
of \(k\). The proof uses an explicit trial point for the convex
filling energy. It does not assert a quantum asymptotic for (1).

## 1. The original equations and the result

Write the original path as \(v-w-b\), with \(b\) outside the
selected region. Put
\[
 t_v=t,\qquad t_w=s,\qquad t_b=u,\qquad
 n_v=2k,\qquad n_w=-2k.
\]
There are exactly two included original edges, \(vw\) and \(wb\).
The pure selected carriers are zero, so the original integer filling
coefficients are \(p_v=-k\), \(p_w=k\). A carrier at \(b\) belongs
to the eventual outside circle and is not inserted in this piece.

On the canonical positive edge branch define
\[
 r(x,y)=\operatorname{arsinh}\bigl(\tan(x/2)\cos(y/2)\bigr).
\]
The full primitive equations are
\[
 \begin{split}
 r(t,s)&=ik t-\pi i,\\
 r(s,t)+r(s,u)&=-ik s-\pi i.
 \end{split}                                                   \tag{2}
\]
The extra term \(r(s,u)\) records the outgoing edge. In the closed
two-vertex reflected problem that incidence is absent. In particular,
the closed solution \(s=-\overline t\) cannot be used in (2).

Let \(\psi\) be the original edge phase, with
\[
 \psi_x(x,y)=-\frac1\pi r(x,y),\qquad
                    \psi(0,0)=\frac{4G}{\pi},
 \tag{3}
\]
where \(G\) is Catalan's constant.

**Theorem 1.** For every real \(k\ge2\) and every complex
\(|u|<1/100\), equations (2) have a unique solution in the
canonical positive original-edge domain. It is holomorphic in
\(u\), its complex filling Jacobian is nonsingular, and
\[
                         \Im t<0,\qquad \Im s<0.              \tag{4}
\]
All four square factors of the two edge blocks remain in a
fixed compact subset of their open squares, independent of \(k\)
and \(u\).

For integer \(k\ge2\), this is the original marked geometric
piece (1), with both filled primitive slopes fixed, its main
cusps complete, and its original free interface retained. Its
pure boundary periods are
\[
 U_b=-2\pi S_k'(u),\qquad V_b=2iu,
 \quad
 S_k(u)=\operatorname{stat}_{t,s}
 \left[
 \psi(t,s)+\psi(s,u)+\frac{ik}{2\pi}(t^2-s^2)-i(t+s)
 \right].                                                     \tag{5}
\]
The selected critical point in (5) is the unique one in this
positive domain. At \(u=0\),
\[
 \operatorname{Vol}(B_k)=2\pi\Re S_k(0).                        \tag{6}
\]
Here \(B_k\) has its outside auxiliary cusp complete. This
is not the volume of the closed two-circle knot.

The response is even and has a uniform strictly negative real
curvature on the common disk: there is a constant \(c>0\),
independent of \(k\), such that
\[
                  -\Re S_k''(u)\ge c
                       \qquad (|u|<1/100).
 \tag{7}
\]
In particular,
\[
                   S_k''(0)=-\frac{\cos(s_k(0)/2)}{2\pi}.
                   \tag{8}
\]

For nonintegral real \(k\), the assertion concerns the primitive
equations and their positive cells. It does not identify a smooth
integer Dehn filling.

## 2. An elementary upper bound for the square energy

We use the exact coordinates of
[the convex filling variation](research_positive_filling_convex_variation.md).
One square has coordinates \(|A|,|y|<\pi/4\) and energy \(E\)
normalized by \(E(0,0)=0\), with
\[
 E_A=\tfrac12\operatorname{arsinh}(\tan(2A)\cos(2y)),
 \qquad
 E_y=\tfrac12\operatorname{arsinh}(\tan(2y)\cos(2A)).
 \tag{9}
\]
It is even in each variable and strictly convex. It is
nonnegative and extends continuously to the closed square,
where every side has energy \(G/2\). These facts, including
the normalization, are proved in
[the corner-energy calculation](research_positive_filling_corner_kkt.md),
Section 3.

For the estimates below we need slightly more than the quadratic
bound on \([-\pi/6,\pi/6]^2\).

**Lemma 2.** If \(4A^2,4y^2\le9/8\), then
\[
 E(A,y)\le\frac{A^2+y^2}{2}+\frac{A^4+y^4}{3}.                 \tag{10}
\]

**Proof.** For nonnegative \(A,y\), the first expression in
(9) decreases when \(y\) increases. Integration in \(A\), and
evenness, give
\[
                    E(A,y)\le E(A,0)+E(0,y).
\]
On an axis \(E_{AA}(A,0)=\sec(2A)\). We claim that
\(\sec x\le1+x^2\) for \(0\le x^2\le9/8\).
The alternating cosine bound gives
\[
 \cos x\ge1-\frac{x^2}{2}+\frac{x^4}{24}-\frac{x^6}{720}.
\]
For \(z=x^2\), multiplication by \(1+z\) leaves the excess
\[
 \frac{z}{720}(360-330z+29z^2-z^3).
\]
The cubic is decreasing on \(0\le z\le9/8\); at \(9/8\)
it equals \(12303/512>0\). Thus the claim follows.
Two integrations of \(\sec(2A)\le1+4A^2\) give
\(E(A,0)\le A^2/2+A^4/3\), proving (10).
\(\square\)

## 3. One feasible point for the whole family

To avoid confusion with the complex angles, write
\(\sigma_j=\Re t_j\), \(h_j=\Im t_j\), and
\(g_{j,e}=\Im r_{j,e}\). The original imaginary filling
conditions are
\[
 g_{v,vw}-k\sigma_v=-\pi,\qquad
 g_{w,vw}+g_{w,wb}+k\sigma_w=-\pi.                            \tag{11}
\]
At the outside vertex \(\sigma_b=\Re u\) is prescribed.

Choose the following trial values:
\[
 \begin{array}{c|c}
 \sigma_v=15\pi/(16k)&g_{v,vw}=-\pi/16\\
 \sigma_w=-4\pi/(5k)&g_{w,vw}=g_{w,wb}=-\pi/10\\
 \sigma_b=\Re u&g_{b,wb}=0 .
 \end{array}                                                   \tag{12}
\]
Both equations (11) hold exactly.

For an oriented edge \(j\ell\), the two square factors are
\[
 \begin{split}
 A_P&=\sigma_j/4-g_{\ell,e}/2,&
 A_Q&=\sigma_j/4+g_{\ell,e}/2,\\
 y_P&=g_{j,e}/2+\sigma_\ell/4,&
 y_Q&=g_{j,e}/2-\sigma_\ell/4.
 \end{split}                                                   \tag{13}
\]
For \(vw\), these are
\[
 \begin{split}
 A_P&=\frac{15\pi}{64k}+\frac{\pi}{20},&
 A_Q&=\frac{15\pi}{64k}-\frac{\pi}{20},\\
 y_P&=-\frac{\pi}{32}-\frac{\pi}{5k},&
 y_Q&=-\frac{\pi}{32}+\frac{\pi}{5k}.
 \end{split}
\]
For \(wb\), they are
\[
 A_P=A_Q=-\frac{\pi}{5k},\qquad
 y_P=-\frac{\pi}{20}+\frac{\Re u}{4},\quad
 y_Q=-\frac{\pi}{20}-\frac{\Re u}{4}.
\]
Each expression is affine in \(1/k\). Its maximum absolute
value on \(0\le1/k\le1/2\) occurs at an endpoint. Consequently
the eight absolute coordinate values are bounded by
\[
 \frac{107\pi}{640},\ \frac{43\pi}{640},\
 \frac{21\pi}{160},\ \frac{11\pi}{160},\
 \frac{\pi}{10},\ \frac{\pi}{10},\
 \frac{\pi}{20}+\frac1{400},\
 \frac{\pi}{20}+\frac1{400}.                                  \tag{14}
\]
These are strictly less than \(\pi/4\). Their doubled squares
are at most \(9/8\): the largest is bounded using
\[
 \left(\frac{107}{320}\frac{22}{7}\right)^2
                =\frac{1385329}{1254400}<\frac98.
\]
Thus (12) is strictly feasible for every \(k\ge2\) and
\(|\Re u|\le1/100\).

The total energy for prescribed outside angle is
\[
 \mathcal E
       =4\sum_{\text{four squares}}E(A,y)
                              -(\Im u)g_{b,wb}.               \tag{15}
\]
The last term vanishes at (12). Applying (10), then
\(\pi<22/7\), to (14) gives the rational bound
\[
 \mathcal E_{\rm trial}
 \le\frac{10300525426199761}{5900697600000000}
 <\frac74.                                                     \tag{16}
\]
The computation here is simply
\(2\sum z_j^2+\frac43\sum z_j^4\), with \(z_j\) the eight
bounds in (14).

Any point on the boundary of the square domain has at least
one square of energy \(G/2\). Moreover
\(|g_{b,wb}|\le\pi/2\). Therefore, when
\(|\Im u|\le1/100\),
\[
 \mathcal E_{\rm boundary}
 \ge2G-\frac{\pi}{200}
 >\frac95-\frac{11}{700}
 =\frac{1249}{700}>\frac74.                                   \tag{17}
\]
For the elementary bound \(G>9/10\), retain the first four
terms of its alternating series:
\(G>1-1/9+1/25-1/49>9/10\).

The energy extends continuously to the compact closed feasible
polytope. Equations (16)--(17) force its minimum into the open
domain. Strict convexity makes that minimum unique. The
Euler--Lagrange equations in the convex variation note give
exactly (2), including matching the full imaginary angles.

The same estimates give uniform separation from the square
boundary. At the minimum,
\[
 4\sum E\le\frac74+\frac{\pi}{200}<2G.
 \tag{18}
\]
Since every individual \(E\) is nonnegative and takes the
constant value \(G/2\) on its boundary, continuity and
compactness give a fixed compact subset of the open square
containing every factor at every such minimum.

## 4. Core orientation and the holomorphic response

The following sign observation applies more generally than
the present two-vertex path.

**Lemma 3.** At an interior solution of the positive filling
variation with real powers and strictly positive charges \(c_j\),
every selected angle has \(\Im t_j<0\).
Outside complex angles may be prescribed.
This holds for every finite original circle-tree incidence
network, with any selected subset and arbitrary selected
degrees, provided each selected vertex has an included
incident edge. It does not require a path, reflection
symmetry, a common sign of the powers, or complete outside
angles.

**Proof.** Fix a selected vertex \(j\). In the unconstrained
energy vary only its real angle \(\sigma_j\) and all its
incidence coordinates \(g_{j,e}\). Simultaneously reversing
these variables preserves every incident edge energy.
For the first endpoint of (13), the two square pairs are
interchanged and both coordinates negated; for the second
endpoint the pairs are interchanged. Evenness of \(E\)
therefore proves the symmetry. The outside linear term in
(15) is unchanged.

The original square domain is convex in these variables.
Its restricted energy is strictly convex, and the vertex
vector is nonzero because
\(\sum g_{j,e}-n_j\sigma_j/2=-\pi c_j\ne0\).
Evenness and strict convexity make its radial derivative at
that vector strictly positive. The exact edge differentiation
identity identifies this derivative with
\[
 \sigma_j\sum_e\Re r_{j,e}+h_j\sum_e g_{j,e}
 =\sigma_j\left(-\frac{n_jh_j}{2}\right)
       +h_j\left(\frac{n_j\sigma_j}{2}-\pi c_j\right)
 =-\pi c_jh_j.
 \tag{19}
\]
The first equality uses imaginary-angle matching, and the
second uses the real and imaginary filling equations.
Thus \(h_j<0\).
\(\square\)

The radial variation used here need not preserve the
filling constraint. It computes a derivative of the
unconstrained energy at a solution, where the full filling
equations can then be substituted in (19).
The earlier weak sign argument at possible corner
minima in
[the negative-corridor analysis](research_negative_corridor_variational_bounds.md),
Proposition 2, uses the same symmetry. Strict interior
convexity gives the stronger conclusion here without its
degree or power-sign restrictions.

Apply the lemma with both charges one. This proves (4),
including at complex \(u\).

The complex derivative of each positive edge return has
positive definite Hermitian real part, by
[the global positive-edge theorem](research_positive_edge_global_monotonicity.md),
Theorems 1 and 3. Subtracting the purely imaginary filling
diagonal leaves that real part unchanged. The selected
Jacobian is therefore invertible. The holomorphic implicit
function theorem gives local solutions of (2); their
uniqueness makes them agree on overlaps. They form a single
holomorphic solution on \(|u|<1/100\).

The compact containment from (18) also supplies a uniform
positive lower bound for the real part of the full edge
derivative, in all three original vertex coordinates.
The boundary-response derivative is its Schur complement
after the two filling terms are added. If its block matrix
is
\[
 H=\begin{pmatrix}A&B\\B^T&D\end{pmatrix},\qquad \Re H\ge c_0I,
\]
then, with \(x=-A^{-1}By\),
\[
 \Re\{y^*(D-B^TA^{-1}B)y\}
 =\Re\{(x,y)^*H(x,y)\}\ge c_0|y|^2.
 \tag{20}
\]
The imaginary diagonal may grow with \(k\); it does not
change this bound. The response is
\(r(u,s_k(u))=-\pi S_k'(u)\), so (20) proves (7).

Replacing \(u\) by \(-u\) leaves (2) unchanged and the
positive domain invariant. Uniqueness gives even
\(t_k(u),s_k(u),S_k(u)\). The envelope identity is
\(S_k'(u)=\psi_u(s_k(u),u)\). Since the mixed derivative
vanishes at \(u=0\), it gives (8).

## 5. Original peripheral curves and the absolute volume

At integer \(k\), use the two actual original edge blocks
and their original annular composition, in the order \(v-w-b\).
The positive-point completion theorem applies at \(u=0\):
all original edge tetrahedra are positive, (4) supplies
positive core lengths, and (2) consists of the full marked
logarithmic filling equations. Thus the completed piece is
the actual filling of the original exterior along
\(\mu_v-k\lambda_v\) and \(\mu_w+k\lambda_w\).
All main cusps and the outside auxiliary cusp are complete.
The theorem's absolute cell-volume identity gives exactly
(6), including both linear charge terms in (5).
See
[the marked completion theorem](research_positive_point_marked_completion.md),
Theorem 1, and
[the original positive-cell volume identity](research_positive_edge_volume_identity.md).

For nearby \(u\), the same original face maps are nonsingular.
The incoming and outgoing doubled disk triangles have the
ordered ratios
\[
 (-Q^{-1},-Q,-Q^{-1}),\qquad
 (-Q,-Q^{-1},-Q),\qquad Q=e^{iu},
 \tag{21}
\]
as in the original equation \(\mathrm{ctg:pants}\) and the
[marked one-child composition](research_large_power_turn_marked_geometry.md),
Sections 1--2. The primitive meridian traverses the original
annular sectors; the disk longitude is their common
primitive longitudinal curve. No outside half-turn or
carrier is discarded. The actual logarithmic periods are
therefore (5), with both old filled periods held fixed.
The main cusp translations remain the original complete
ones. Continuation from \(u=0\), together with (4), preserves
the filled tube orientation and primitive winding.

If this piece is attached to an outside circle with carrier
\(\eta_b\) and filling coefficient \(p_b\), its contribution
to the pure meridian is \(U_b\). After summing all incident
pieces, insert that outside carrier once:
\[
 U_{\rm total}=-2\pi\sum_{\rm pieces}S_{\rm piece}'(u)
                         -i\eta_bu,\qquad V_{\rm total}=2iu.
 \tag{22}
\]
Thus the original outside power remains
\(n_b=\eta_b-2p_b\). This is the same marked attachment used
by the established composition theorems. The theorem does
not omit additional incidences at either selected vertex:
their original degrees must be one and two.

## 6. Independently signed powers

The energy argument does not require reflection symmetry.

**Corollary 4.** Let \(a,b\) be independently chosen real
powers with \(|a|,|b|\ge4\). For the original pendant piece
\[
                           T(R^bT(R^a)),
\]
the conclusions of Theorem 1 hold on the same outside disk
\(|u|<1/100\), with equations and phase
\[
 \begin{split}
 r(t,s)&=\frac{ia}{2}t-\pi i,\\
 r(s,t)+r(s,u)&=\frac{ib}{2}s-\pi i,\\
 S_{a,b}(u)&=\operatorname{stat}_{t,s}
 \left[\psi(t,s)+\psi(s,u)
                  +\frac{i}{4\pi}(at^2+bs^2)-i(t+s)\right].
 \end{split}                                                   \tag{23}
\]
For integer powers, retain the original carriers
\(\eta_v,\eta_w\) and fill along the original coefficients
\[
                     p_v=(\eta_v-a)/2,\qquad
                     p_w=(\eta_w-b)/2 .
\]
The statement assumes the original admissible parity
choices, so these coefficients are integers. It includes
the same ordered free interface and absolute volume
\(2\pi\Re S_{a,b}(0)\).

**Proof.** Keep the incidence values in (12), but set
\[
                 \sigma_v=\frac{15\pi}{8a},\qquad
                 \sigma_w=\frac{8\pi}{5b}.
 \tag{24}
\]
Then \(g_v-a\sigma_v/2=-\pi\) and
\(\sum g_w-b\sigma_w/2=-\pi\).
In the first edge the square coordinates come in pairs
\(x+c,x-c\), with
\[
 (|x|,|c|)\le(15\pi/128,\pi/20)
 \quad\hbox{or}\quad
 (|x|,|c|)\le(\pi/10,\pi/32).
\]
For each pair,
\[
 \begin{split}
 (x+c)^2+(x-c)^2&=2(x^2+c^2),\\
 (x+c)^4+(x-c)^4&=2(x^4+6x^2c^2+c^4).
 \end{split}
\]
Both expressions increase with \(|x|\) and \(|c|\).
The maximum absolute coordinate still satisfies the
bound used in Lemma 2. The outside edge has the same
bounds as (14). Consequently (16)--(18) hold unchanged.
The remaining arguments use only real filling powers,
positive unit charges, and the actual two incidences;
they therefore prove (23) with the same uniform domain
and response bound. The original carrier terms are
retained by the marked completion theorem.
\(\square\)

**Corollary 5.** In Theorem 1 of
[the positive-point marked completion](research_positive_point_marked_completion.md),
the separate hypothesis \(\Im t_v<0\) is redundant.
It suffices that every original edge block be positive
on its canonical branch and that the original full
unit-charge logarithmic filling equations hold.

**Proof.** Express the positive solution in its interior
square coordinates. Its matching and filling equations
are exactly the Euler--Lagrange equations of the convex
variation. Apply Lemma 3 with every selected charge
equal to one. It supplies all strict core signs required
by the marked completion theorem. All other hypotheses
of that theorem, including the original integer slopes,
complete outside angles and retained primitive
markings, are unchanged.
\(\square\)

## 7. Scope for source estimates

The piece \(F_1=T(R^{-2}T(R^2))\) has a separately proved
[pure marked geometric chart](research_mixed_pure_carrier_geometry.md),
using its positive subdivision and original disk seam.
It need not lie in the original positive two-edge chart
used here. Combining that single fixed chart with Theorem 1
gives a common smaller boundary disk for all integer
\(k\ge1\), with the original primitive interface retained.
Orientation reversal supplies the mirrored pieces with
the correspondingly transported original markings.

For \(k=1\), the full quantum boundary theorem is already
proved in
[the mixed two-crossing boundary theorem](research_mixed_two_crossing_boundary_theorem.md).
For large \(k\), the established large-power turn theorem
also applies. The present argument supplies geometry for
every intermediate \(k\); it does not supply the missing
original-cycle analysis there.

In particular, the closed reflected identity
\(\varphi(R^{-2k}T(R^{2k}))\), its sharp norm growth, and its
fixed Casimir insertion limits are different source
statements. They do not imply an asymptotic expansion for
the retained boundary polynomial of (1). The extra edge
and the term \(r(s,u)\) in (2) must remain in any such proof.

## 8. Exact arithmetic record

The rational arithmetic in (11), (14), and (16)--(18) is
reproduced by
[the energy checker](../experiments/check_attached_reflected_pair_energy.py).
It uses only exact fractions and records its own hash and
the note's hash in
[the saved result](../repro/results/research-attached-reflected-pair-energy.json).
An independent output can be selected without overwriting
that record:

~~~sh
python3 experiments/check_attached_reflected_pair_energy.py --output /tmp/attached-reflected-energy.json
~~~

The checker verifies the finite constants in the written
proof. It does not replace the convex existence, primitive
marking, or holomorphic continuation arguments.
