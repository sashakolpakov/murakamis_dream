# The complete quartic branches and their representation-volume gap

This note identifies all eight intersections of the actual adjacent
three-crossing source curve with the complete boundary value. Each
intersection gives a regular representation of the same marked
partially filled exterior. The geometric intersection has a strict
volume gap over all the other representations. The statement uses the
representation-volume theorem already proved in this repository; it is
not a new rigidity theorem.

This does not prove a lower bound for the original boundary
polynomial. In particular, it does not construct an observable
adjoint mode of its finite source operator.

## 1. The original region and the eight intersections

Use the original pendant path \(v-w-b\), with powers \(-3,-3\)
on the degree-one and degree-two vertices and the last circle
unfilled. Denote its complete partially filled exterior by \(M\).
Its positive marked geometry and its complete volume \(V>0\)
are proved in
[the geometric branch calculation](research_three_crossing_pendant_geometric_branch.md).
The selected angles there are \(\alpha,\beta\); the free angle is
\(u\). The pure free boundary has no additional carrier.

Put
\[
\begin{split}
v(\tau)&=(\tau-2)^2(\tau^2-2\tau+2),\\
z(\tau)&=4-5\tau+4\tau^2-\tau^3,\\
h(\tau)&=\tau^5-7\tau^4+20\tau^3-32\tau^2+30\tau-14,\\
f_\epsilon(\tau)&=v(\tau)-2\epsilon i,\qquad \epsilon\in\{1,-1\}.
\end{split}                                                    \tag{1}
\]
These are exactly the two complete-boundary quartics in Section 5 of
[the actual boundary-current calculation](research_three_crossing_boundary_current.md).
The four roots of \(f_+\) lie in the four disjoint radius-\(1/1000\)
disks with centers
\[
 (2610+416i)/1000,\quad(624-683i)/1000,\quad
 (1822-1037i)/1000,\quad(944+1303i)/1000.                         \tag{2}
\]
The exact Rouché proof is already given in the geometric-branch
note. All roots are simple. The roots of \(f_-\) are their complex
conjugates. The two lists are disjoint because \(f_+-f_-=-4i\).
In particular all eight roots have positive real part.

Write \(\tau_{\mathrm g}\) for the last root in (2). It gives the
actual oriented geometric representation of \(M\).

## 2. Rational half-angle cosines and the full filling products

For any root of \(f_\epsilon\), define
\[
 c=\frac{2\epsilon i}{h},\qquad
 d=\frac{2\epsilon(\tau-1)}{h},\qquad
 q=\frac{i(\tau+1)}{\tau-1},\qquad q_0=\frac1d.                  \tag{3}
\]
The symbols \(q,q_0\) here are geometric edge square roots, not the
finite-level quantum parameter. Direct polynomial reduction gives
\[
 c^2=\frac{2-\tau}{4},\qquad d^2=\frac{2-z}{4},\qquad
 d=i(1-\tau)c,\qquad q^2+1=c^{-2}+d^{-2}.                       \tag{4}
\]
One convenient identity proving the first equality is
\[
                 -\frac{(2-\tau)h(\tau)^2}{16}=1
                     \quad\pmod {f_\epsilon}.                 \tag{5}
\]
Thus both half-angle cosines are rational on each quartic.

Choose square roots \(s^2=1-c^2\) and \(t^2=1-d^2\), and put
\[
 a=s/c,\qquad b=t/d,\qquad
 e^{i\alpha/2}=c+is,\qquad e^{i\beta/2}=d+it.                   \tag{6}
\]
Retain the free half-angle sign \(\cos(u/2)=\epsilon\): take
\(u=0\) for \(\epsilon=1\) and \(u=2\pi\) for \(\epsilon=-1\).
Both have the same complete boundary eigenvalue and the same
finite Casimir value \(-2\). Resetting this half-angle sign would
lose the second list.

The original edge returns have the following exponentials:
\[
 e^{r_v}=d(q+a),\qquad e^{r_{w,v}}=c(q+b),\qquad
 e^{r_{w,b}}=\epsilon(q_0+b),\qquad e^{r_b}=q_0d=1.             \tag{7}
\]
They obey the two exact identities
\[
\begin{split}
 d(q+a)&=-(c-is)^3=-e^{-3i\alpha/2},\\
 \epsilon c(q+b)(q_0+b)&=-(d-it)^3=-e^{-3i\beta/2}.
\end{split}                                                    \tag{8}
\]
For the first, \(qd=c(1+\tau)\), while
\(- (c-is)^3=c(1+\tau)+i(1-\tau)s\).
For the second, reduce its constant and \(t\) coefficients using
\(t^2=1-d^2\). The required identities are exactly
\[
\begin{split}
 \epsilon c(qd+1-d^2)/d^2&=d(1+z),\\
 \epsilon c(qd+1)/d^2&=i(1-z).
\end{split}                                                    \tag{9}
\]
Their numerators vanish modulo \(f_\epsilon\). These are full
exponentiated returns, not merely the squared stationary equations.
Logarithmic lifts are still retained separately.

## 3. Regular original cells and the marked representation

No root of either quartic is a zero of
\[
 h,\quad \tau,\quad \tau-1,\quad \tau+1,\quad \tau-2,\quad
 \tau+2,\quad z-2,\quad z+2,\quad z-6.                          \tag{10}
\]
This follows by the exact polynomial gcds recorded in the verifier.
Consequently \(c,d,q,q_0\) are nonzero, neither selected angle has
\(e^{2i\alpha}=1\) or \(e^{2i\beta}=1\), and
\[
 q^2+1\ne0,\qquad q_0^2+1\ne0,\qquad
 a^2+1\ne0,\qquad b^2+1\ne0.                                  \tag{11}
\]

The original eight shapes of an edge with tangents \(a,b\) and
square root \(q\) are
\[
 (A,B,-1/A,-1/B,C,D,-1/C,-1/D),
\quad
 A=\frac{q+a}{b-i},\ C=\frac{q-a}{b-i},\
 B=-\frac{q-b}{a+i},\ D=-\frac{q+b}{a+i}.                       \tag{12}
\]
Use (12) for \((a,b,q)\) and \((b,0,q_0)\).
The relations \(q^2-a^2=1+b^2\) and
\(q^2-b^2=1+a^2\) prove that none of their numerators vanishes.
No shape is \(1\) or \(-1\): substituting, for example,
\(q+a=\pm(b-i)\) into \(q^2=1+a^2+b^2\) would force
\((a+i)(b-i)=0\) or \((a-i)(b-i)=0\), respectively.
The other cases follow by the same sign changes and interchange.
Thus every tetrahedron in (12) is regular.

The full original face chart is also regular, not just its
simplified cross ratios. Its additional factors are
\(q\pm i\), \(q\pm a\), \(q\pm b\), and their analogues for the
second edge. Equations (10)--(11) exclude all their zeros.
The factorizations of the apex differences and the original face
maps are those in Section 3 of
[marked positive-point completion](research_positive_point_marked_completion.md).
They are rational identities and remain valid here without a
positivity assumption.

**Proposition 1.** Each root in (1) gives a regular representation
\(\rho_\tau:\pi_1(M)\to\mathrm{PSL}_2(\mathbb C)\), with complete
main and free auxiliary peripheral images and the original
selected primitive fillings.

**Proof.** The rational original face identities give a face
cocycle on the unchanged marked cut complex. All its charts are
regular by the preceding argument. The primitive periods before
filling have multipliers
\[
 e^{U_j}=\exp(2\sum r_j-i\eta_j t_j),\qquad
 e^{V_j}=e^{2it_j},\qquad -3=\eta_j-2p_j.
\]
Equations (8) therefore give
\[
                  \exp(U_j+p_jV_j)=1.                         \tag{13}
\]
The retained longitude has two distinct fixed points by (10).
The meridian fixes its retained common flag and commutes with it,
so the primitive filling product fixes both points. Its multiplier
one in (13) makes it the identity in the projective group.
This is the same algebraic descent argument as Section 9 of
[the original signed volume identity](research_positive_edge_volume_identity.md);
no positive metric is asserted for these other roots.

The free longitude has multiplier one and its return is \(1\)
by (7). Its original complete leaf maps are parabolic, as are
the main-meridian maps. Their nontrivial translation factors
are \(2i/(q-i)\), or the corresponding \(q_0\) expression,
which are nonzero. In particular the complete peripheral
images meet the hypotheses of the representation-volume theorem.
The original cuts, carriers and slopes have not been changed.
\(\square\)

Changing a square-root sign in (6) does not change the signed
shape sum. Under \(a\mapsto-a\), \(A,C\) interchange and
\((B,D)\mapsto(-1/D,-1/B)\); under \(b\mapsto-b\),
\((A,C)\mapsto(-1/C,-1/A)\) and \(B,D\) interchange.
Thus the full list (12) is permuted. These are retained
decoration changes, not additional values of the regulator.

For conjugate roots in the two lists, (3) gives
\[
 c_-=\overline{c_+},\quad d_-=-\overline{d_+},\quad
 q_-=-\overline{q_+},\quad(q_0)_-=-\overline{(q_0)_+}.
 \tag{14}
\]
Choosing \(a_-=-\overline{a_+}\) and
\(b_-=-\overline{b_+}\) in (12) conjugates every shape.
Their signed volumes are therefore negatives.

## 4. The strict gap and what it does not establish

Let \(D_{\mathrm{BW}}\) be the Bloch--Wigner dilogarithm and set
\[
              \mathcal V(\tau)=
                  \sum_{\text{sixteen original shapes}}
                                    D_{\mathrm{BW}}(z).        \tag{15}
\]
The original oriented chain and the axis extensions over the
two filled solid tori identify (15) with
\(\operatorname{Vol}(\rho_\tau)\). Added tetrahedra on either
core axis have zero volume. This is the chain normalization
in Section 9 of the signed-volume note. In particular
\[
 \mathcal V(\tau_{\mathrm g})=V,\qquad
 \mathcal V(\overline{\tau_{\mathrm g}})=-V.                    \tag{16}
\]

**Theorem 2.** There is a number \(\delta>0\) such that
\[
 |\mathcal V(\tau)|\le V-\delta
 \quad\text{for all six roots }\ 
             \tau\ne\tau_{\mathrm g},\overline{\tau_{\mathrm g}}.
 \tag{17}
\]
Thus the oriented geometric value has a strict gap over all
seven other values.

**Proof.** The original inner longitude has projective squared
trace \(\tau^2\): its multiplier is \(e^{2i\alpha}\) and
its determinant-one lifts have trace
\(\pm2\cos\alpha=\mp\tau\). This is an invariant of the
original marked representation, not of its tetrahedron
decoration.

If a constant sequence with representation \(\rho_\tau\)
had volume \(V\), the
[near-maximal-volume theorem](research_near_maximal_representation_volume.md)
would conjugate a subsequence to the complete oriented
holonomy. Continuity of this squared trace would force
\(\tau^2=\tau_{\mathrm g}^2\). The disjoint disks (2) and
their conjugates, all in the positive real half-plane,
then force \(\tau=\tau_{\mathrm g}\). Apply the same argument
after conjugating the target orientation for volume \(-V\).
It forces \(\tau=\overline{\tau_{\mathrm g}}\).
The universal bound and finiteness of the eight-root list
give the positive minimum in (17). \(\square\)

For any original regular logarithmic continuation reaching one
of these critical representations, the calibrated action obeys
\(2\pi\Re S=\mathcal V(\tau)\). The integer charge and all
continued logarithms must be retained as in the signed-volume
note. Consequently (17) bounds those regular critical action
values as well. It does not identify an arbitrary interpolation
phase with such an action.

The source still has to reach the geometric branch with a
nonzero coefficient. Neither (17) nor the finite operator's
small singular values prove this. An adjoint construction for
\(A_Nf=\zeta_N e_D\) must control the actual boundary forcing
\(\overline{\mathbf e(w)}\) and its endpoint observation.
The transported small-residual mode that only recovers
\(f_D\) does not meet that requirement. Endpoint, escaping
and nonregular source strata also remain outside (17).

## 5. Reproduction

The focused exact checker is
[check_three_crossing_quartic_representation_gap.py](../experiments/check_three_crossing_quartic_representation_gap.py).
It verifies both quartics, the rational half-angle identities,
the two complete filling products, and every excluded polynomial
factor in (10). The
[saved exact result](../repro/results/research-three-crossing-quartic-representation-gap.json)
records eighteen rational identities and eighteen excluded-factor
gcds, as well as the script and dependency hashes. It does not
numerically infer the strict gap or an asymptotic coefficient.
