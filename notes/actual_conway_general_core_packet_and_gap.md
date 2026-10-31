# A general quarter bound and the full core estimate for strict Conway trees

31 October 2026. Reviewed research proof. The assertions concern every fixed
literal strict cylindrical tree, not only the completed grammar of the
published manuscript. The alias part of the original invariant remains
separate. No change to that manuscript's theorem is made here.

## 1. Exact scope and inputs

Let the original closed expression be \(C(FG)\), where each of \(F,G\)
is any finite expression in the physical leaf \(h\), the actual turn
\(T\), and ordered product. Delete only its forced final gate, whose
coefficient is one; retain the exact relation \(r_F+r_G=N-1\).
Assume the reduced positive wire polytope has a strict state. Thus all
original leaf labels are in \((0,1/2)\), and every retained gate has
\(\max(x,y)<z<x+y<1\). Write \(H\ge2\) for the number of leaves.

The exact compiler, boundary barrier and angle-map proof in
[the exact source compiler](actual_conway_single_leaf_source_composition.md), §§1–3, apply to
this arbitrary strict syntax. They give a primitive lattice of dimension
\(K=2H-3\), a compact reduced polytope \(P\), and a unique strict
complete maximizer \(y_*\). All wire labels are affine in the primitive
variables; their finite versions include the original fixed integer
offsets from \(d=N-1\). Set
\[
 A(y)=\sum_{i=1}^{H}g(a_i(y))+\sum_{v=1}^{H-2}m(x_v(y),y_v(y),z_v(y)),
 \qquad F_0=A(y_*),
\]
where \(g(a)=J(2a)-4J(a)\) and
\(J(u)=\int_0^u\log(2\sin\pi t)\,dt\).

Each original leaf has a fixed physical sign \(\epsilon_i\in\{0,\pm1\}\).
At every physical color its exact core/alias split is performed in the
original full Hermite–Newton algebra, before any products or turns. Let
\(\mathcal A^{\mathrm{core}}_N(\mathbf h)\) be the literal scalar with
every leaf replaced by its core. This is a summand of the actual source,
not a new definition of the knot invariant. A core is zero if its color
deficit exceeds the original low-core range.

The additional exact inputs are the port types and product equations of
[the strict-mask geometry](actual_conway_general_strict_mask_geometry.md), the high and quarter
finite-source packet theorems, and the uniform all-color coefficient
bounds proved in [the uniform all-color proof](../manuscript/sections/B2-global-core-envelope.tex).
In particular the global core bound is \(\exp N(\widetilde g+o(1))\)
with uniform \(o(1)\), not a global polynomial-prefactor estimate.

## 2. Every complete closed-tree leaf is at or above one quarter

For an optimized open port put
\[
 B=\cot(\pi b),\quad \kappa=e^{-f'(b)},\quad
 X^2=\frac{1+B^2}{1+\kappa},\quad Y^2=\kappa X^2,\quad X,Y>0.
\]
Then \(X^2+Y^2-B^2=1\). The exact strict types are
\[
 L:(B,X,Y)=(B,B,1),\quad
 H:(B,X,Y)=(-Y,1,Y),\quad
 A:-Y<B<X.
\]
A turn exchanges \(X,Y\) and negates \(B\). A product has a common
child \(X\), \(S=B_1+B_2>0\), and
\[
 B_o=\frac{B_1B_2+X^2-1}{S},\qquad Y_o=\frac{Y_1Y_2}{S}.
\]

At the cylindrical root the two \(B\)'s are opposite and their ordered
metrics agree, so their \(X,Y\) agree. In type \(AA\),
\(|B|<\min(X,Y)\), whence the quadratic identity gives \(X,Y<1\).
In \(AL\), the \(L\) port has \(Y=1\), and the \(A\) inequality
\(-1<-X\) gives \(X<1\). In \(AH\), the \(H\) port has \(X=1\),
and the \(A\) inequality \(Y<1\) gives the other bound. In \(LH\)
the explicit forms force \(X=Y=1\). These exhaust all strict root pairs.

For the downward product step set \(c=1-X^2\). The identity
\[
 (B_1^2+c)(B_2^2+c)-(B_1B_2-c)^2=c(B_1+B_2)^2
\]
gives \(Y_o^2-B_o^2=1-X^2\), hence \(X_o=X\). Every child type has
\(B_i\le X\); positivity of \(S\) gives \(B_i>-B_j\ge-X\).
Consequently \(Y_i^2=1+B_i^2-X^2\le1\). Starting with the root bounds,
products and turns therefore give \(X,Y\le1\) at every port. At an
original leaf, \(X=\cot\pi a\), so
\[
                        \boxed{\quad 1/4\le a_i(y_*)<1/2.\quad}
\tag{1}
\]
Equality is allowed. It is a regular angle state, even though the two
source recurrence roots there have equal modulus. The [quarter packet
theorem](actual_conway_quarter_index_color_packet.md) treats that boundary using the actual finite source anchor.

## 3. Gate curvature controls every primitive direction

Let \(V(a,b,c)=-\pi[J(a)+J(b)+J(c)]\), \(a+b+c=1\), be the ideal
tetrahedron volume. Its Hessian is strictly negative on nonzero tangent
vectors of the positive angle simplex. For a strict gate set
\(p=z-x\), \(q=z-y\), \(r=x+y-z\), \(w=1-x-y\). The exact identity is
\[
 \pi m(x,y,z)=V(y,x,w)+V(p,q,2r+w)+V(p+q,r,r+w).
\tag{2}
\]
All three triples are positive and sum to one. If a tangent has zero
quadratic form in the first atom, then \(\delta x=\delta y=0\).
Zero quadratic form in the second then forces \(\delta z=0\).
The third atom has nonpositive Hessian and cannot undo this conclusion.
Thus **each strict gate has a negative-definite Hessian in its three
wire variables**, including when one input is above one half.

For \(H\ge3\), the collection of all retained gate-label maps is
injective on the primitive tangent space. To see this, contract the unary
turn chains, retaining their affine complements. Every leaf or product
output in a nontrivial root subtree occurs at a retained gate. Its
variation is therefore zero if all gate variations are zero. The only
possible uncovered wire is a root subtree consisting of one leaf and
turns; the other subtree is nontrivial, and the root complementary
relation sets that leaf variation to zero as well. Both subtrees can be
single leaves only when \(H=2\).

It follows that the sum of the retained gate Hessians is negative
definite on the full primitive space whenever \(H\ge3\). This uses
the actual wire graph and its unit closing relation; it does not add a
spurious root gate or assume leaf curvature where it has disappeared.

## 4. The all-core majorant has the same unique geometric maximum

Put
\[
 \widetilde g(a)=g(\max(a,1/4)),\qquad
 \bar g_{\epsilon}(a)=
 \begin{cases}g(a),&\epsilon=0,\\ \widetilde g(a),&\epsilon=\pm1,
 \end{cases}
\]
and define on the original closed polytope
\[
 \bar A_\epsilon(y)=\sum_i\bar g_{\epsilon_i}(a_i(y))+
                         \sum_v m(x_v(y),y_v(y),z_v(y)).
\tag{3}
\]
Both leaf functions are concave. The plateau extension is continuously
differentiable at \(1/4\), because \(g'(a)=2\log\cot\pi a\) vanishes
there. By (1), every leaf has the same value and first derivative at
\(y_*\) in (3) as in the complete action. Therefore
\(\bar A_\epsilon(y_*)=F_0\) and \(d\bar A_\epsilon(y_*)=0\).
Concavity gives \(\bar A_\epsilon\le F_0\) on all of \(P\).

For \(H\ge3\), the gate curvature from §3 gives a strictly quadratic
local loss. Indeed, in a small compact strict neighborhood the sum of
gate terms lies below its tangent by \(c\|y-y_*\|^2\), \(c>0\), and
every leaf term lies below its tangent by concavity. The tangent linear
terms cancel by stationarity. Thus
\[
 \bar A_\epsilon(y)\le F_0-c\|y-y_*\|^2
\tag{4}
\]
there, without differentiating the plateau twice. A second global maximum
would give a constant segment to \(y_*\), contradicting (4). Compactness
therefore gives a strictly positive gap outside any fixed neighborhood
of \(y_*\).

For \(H=2\), at least one pure leaf gives the same strictness: after
the turns and the strict root relation both original leaf coordinates
are one common \(a\), and the majorant is either \(2g(a)\) or
\(g(a)+\widetilde g(a)\), uniquely maximized at \(a=1/4\).
If both leaves are odd, the majorant is \(2\widetilde g(a)\) and is
flat for \(a\le1/4\). This case is excluded from this core theorem.
It has two main components: both odd leaves have endpoint pairing \(X\),
turns preserve \(X\), and \(X X=I\) closes to two components. Thus every
strict two-leaf **knot** pattern has a pure leaf and is included.

## 5. Uniform estimates for the literal complete core sum

Fix a small rectangular primitive window \(B\) around \(y_*\), with
closure in the strict polytope. In exact finite coordinates its wires
are \(r_w=NL_w(k/N)+\delta_w\), with the original integer offsets.
Choose \(0<\beta<1/2\) larger than every leaf label on this window.

For every physical core color, the global coefficient estimate is
\[
 |c^{\epsilon}_{N,h,r}|\le
   \exp N\{\bar g_\epsilon(r/N)+e_N\},\qquad e_N\longrightarrow0,
\tag{5}
\]
uniformly in \(h,r\). The pure case follows from its exact factorial
formula and the positive color deficit. The signed case is the
collision-safe frozen-block bound, including its terminal source and
singular lower endpoint. Gate factorial errors are uniformly
\(O(\log N)\). Fixed affine offsets change continuum rates uniformly
by \(o(1)\), even at feasible endpoints, by uniform continuity of
\(J\) on its closed interval.

There are polynomially many states for the fixed tree. Apply the strict
compact gap in §4 to (5), then absorb the finitely many \(e_N\)'s and
uniform offset errors into half that gap. The contribution of **all
core states outside \(B\)** is therefore
\[
                O\!\left(N^C e^{N(F_0-\gamma)}\right),
\tag{6}
\]
uniformly over the whole physical color cube. This bound concerns an
absolute sum of those states; no cancellation or discarded channel is
needed to obtain it.

For the endpoint comparison, first divide every exact finite wire by
\(d=N-1\); its full array then lies in \(P\) exactly. Its \(r/N\)
coordinates differ by \(O(1/N)\), and uniform continuity compares the
rates at two admissible arrays. No \(J\) is evaluated beyond its closed
domain. Shrinking or enlarging the fixed window by \(O(1/N)\) preserves
the same positive outside gap.

Inside \(B\), the signed recurrence's strict far-color estimate applies
for \(r\le\beta N\), including \(r/N=1/4\). Its proof uses a strict
spectral interval above \(\max(\beta,1/4)\), which every backward path
crosses. Hence if one physical deficit is at least \(\delta N\), for
fixed \(\delta>0\), its rate loses a uniform positive amount relative
to \(\widetilde g\). For a pure leaf the exact loss is
\[
 \Delta(a,t)=J(a-t)+J(a+t)-2J(a)>0
 \quad(0<t\le a<1/2),
\]
or the core coefficient is zero when \(h>r\). Compactness of the window
and the fixed lower bound on \(t\) give the pure uniform loss too.
Together with (6) this proves
\[
 \max_{\exists i:\,h_i>\delta N}
 |\mathcal A^{\mathrm{core}}_N(\mathbf h)|
 \le N^C e^{N(F_0-\gamma_\delta)}.
\tag{7}
\]
Colors outside the core's original support contribute zero, not an
uncontrolled analytic continuation.

## 6. The exact local packet and the remaining alias obligation

On \(B\), continue only the paired color factorials of the exact finite
core coefficients. This gives the finite even holomorphic window
\(\mathcal C_N(\boldsymbol\chi)\), after removal of the known unit phase
\(\eta_N=\exp(i\pi(N-1)\sum_i\epsilon_i/4)\). By (1), each leaf
lies in a high-index neighborhood or in the proved quarter neighborhood.
Use the corresponding exponentially accurate **actual-source** index
interpolant. Their errors, summed over polynomially many window states,
are \(\operatorname{poly}(N)e^{N(F_0+C\|\chi\|^2-c_0)}\), so shrinking
the fixed color polydisk makes them negligible before any complex saddle.

The interpolated phase is the sum of the selected \(f_{\epsilon_i}\)
and the unchanged gate actions. Its complete wire Hessian is invertible.
The original finite cotangent rectangles and Gaussian calculation apply
in the same primitive coordinates, retaining all offsets and boundary
currents. There are \(H\) leaf factors of order \(N^{1/2}\), \(H-2\)
gate factors of order \(N^{-3/2}\), and \(K=2H-3\) Gaussian variables.
Consequently
\[
 \mathcal C_N(\chi)=N^{3/2}a_\epsilon(\chi)e^{N\Phi_\epsilon(\chi)}
                                      (1+O(N^{-1})),\qquad a_\epsilon(0)\ne0.
\tag{8}
\]
All square roots, offsets and chirps are inherited from the source.
At completeness the signed/pure amplitude ratio is
\(\prod_{\epsilon_i\ne0}\sqrt{\sin\pi a_i}\,e^{-i\epsilon_i\pi a_i/2}\),
which is nonzero also at a quarter leaf. Separate evenness gives
\[
 \partial_i\partial_j\Phi_\epsilon(0)=
 -\frac{2\pi c_i}{1-\epsilon_i i c_i}\delta_{ij},\qquad
 c_i=\cot\pi a_i>0.
\tag{9}
\]
In particular its real part is strictly negative, giving a fixed joint
complex Gaussian envelope for the exact finite window. Estimates (6)–(8)
give the original all-core source comparison in the small physical
color corridor and its far-color complement, at both parities and all
sufficiently large levels.

The actual source is
\(\mathcal A_N=\mathcal A_N^{\mathrm{core}}+\mathcal A_N^{\mathrm{alias}}\),
where the second term is the sum of all nonempty alias sectors with their
original signs. Thus for every strict knot pattern the missing global
source input has been reduced to
\[
 \sup_{\text{all physical colors}}
 |\mathcal A_N^{\mathrm{alias}}(\mathbf h)|
           \le N^C e^{N(F_0-\gamma)}
\tag{10}
\]
for some fixed \(\gamma>0\), or to an equally sufficient estimate after
the exact filling pairing. A separate bound for every sector is sufficient
but not logically necessary. Pointwise positive alias envelopes can fail
to prove (10); their failure is not a lower bound on the actual alias.

Once (10) is proved for a class, the [general marked-mask construction](actual_conway_general_mask_marked_filling.md)
identifies \(U_i=-2\pi i\chi_i\), \(V_i=-2\partial_i\Phi_\epsilon\),
and the original primitive filling action with the actual knot complement
volume. The proved entire Fourier–Hermite filling transfer then gives the
full original-invariant volume limit for independently long fixed signed
twists. This is a reduction of the remaining conjectural step, not an
assertion that (10) holds for every strict tree.

## Internal review and scope

The marked-geometry reviewer read the full argument in §§1–6 and
independently checked the endpoint comparison using the exact denominator
\(N-1\). Two source reviewers independently checked the quarter bound,
gate rank and resulting core gap, including the two-leaf exception. These
are internal analytical reviews, not external peer review or formal
verification. No numerical asymptotic is a proof input. The theorem
concerns the literal all-core source for strict knot patterns; it does
not assume that every nonempty alias sector has a gap.

For the root-star family, the [full-jet localization](actual_conway_root_star_full_jet_localization.md)
and [root-character Fourier contraction](actual_conway_root_character_fourier_contraction.md)
supply the additional alias estimate. Arbitrary turned children still
require that separate global argument. The published completed-root
manuscript is unchanged by these companion research notes.
