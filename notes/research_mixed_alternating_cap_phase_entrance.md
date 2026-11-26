# The actual cap phase approaches the alternating invariant germ

Research deduction, 7 November 2026. A long alternating prefix with
its original complete ordinary cap has a geometric local phase whose
outgoing Fourier gradient approaches the invariant alternating germ
exponentially. The cap is not assumed to start in that germ's basin.
The proof first uses the original conditional coordinates, where the
complete endpoint and every chain length are already localized, and
then changes the outgoing polarization on a fixed local disk.
The associated cap-initialized local coefficient is nonzero. No
assertion about the full cap message or its complementary integral
is made, and no numerical evaluation is used.

## 1. A half-chain which retains the original cap

Write \(g(z)=J(z)+i\pi(z-z^2)/2\). Use the original vertex,
contracted shared-edge, and complete-left-end actions
\[
 \begin{split}
 V_\epsilon(s,t)&=g(s+t)-\epsilon\{g(s)+g(t)\},\\
 G(t,b)&=g(t+b)-2g(t)-2g(b)+2\pi itb,\\
 E(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)
                +i\pi eu-i\pi(e-e^2)/2.
 \end{split}
 \tag{1}
\]
These are exactly the primitives and chirps in
[the absolute source calibration](research_mixed_geometric_action_calibration.md),
equations (16), (21)--(22); in particular no constant is reset.
For a prefix \(\epsilon_1,\ldots,\epsilon_m\), keep a fixed
external inverse leg \(b\) and set
\[
 \mathcal A_m(z;b)=E(s_1,u)
       +\sum_{j=1}^m V_{\epsilon_j}(s_j,t_j)
       +\sum_{j=1}^{m-1}G(t_j,s_{j+1})+G(t_m,b).
 \tag{2}
\]
The unknowns are \(u,s_1,t_1,\ldots,s_m,t_m\). The left
ordinary cap remains literal. The last term is the original
contracted incidence at the cut, with its second leg fixed; it is
not a new ordinary cap or a periodic identification.

Use \(E,U,Q,D_3,D_4\) from
[open-word localization](research_mixed_open_word_critical_localization.md)
and [the common Hessian theorem](research_mixed_open_word_hessian.md).
Thus \(s_1\in E\), \(u\in U\), and every other unknown leg
is in its typed disk, strictly inside \(Q\).

**Lemma 1.** For every prefix and every external
\(b\in D_{3+\beta}\), (2) has a unique original-log critical
point in this product. It is holomorphic in \(b\) near the
closed input disk. At all points of the larger convex product,
\[
 -\Re\mathcal A_{m,zz}''\succ\mu I,
                  \qquad \mu=6\pi/49.
 \tag{3}
\]
There is a constant \(C>\mu\), independent of the word and
length, bounding the operator norm of this Hessian on the product.

*Proof.* At the first vertex use the already proved ordinary-end
update, with its original \((e,t,u)\) equations. At every other
vertex use the original two-leg update from
[cyclic localization](research_mixed_cyclic_critical_localization.md),
with external inputs \(t_{j-1},s_{j+1}\), or \(t_{m-1},b\)
at the last vertex. The updates are disjoint and use old neighbor
values. Their typed image inclusions give a self-map of the compact
product, hence a fixed point. For \(m=1\) the ordinary-end map
alone is exactly the required system. These are the original
gradients of (2).

The Hessian proof for the open word applies with one endpoint.
The actual \(E(s_1,u)\) supplies the endpoint \(2\)-variable
bound \(6\pi/49\). Every other unknown leg has its two pair
incidences; the last one still has \(G(t_m,b)\), with \(db=0\).
The same pair and type-four own costs therefore give (3).
Accretivity along a straight complex segment proves uniqueness.
The nondegenerate Jacobian gives holomorphy, with branches agreeing
by uniqueness. The finitely many original local maps have strict
image margins on their compact input products, independent of
length; no new endpoint root construction is required.

Group \((u,s_1,t_1)\) at the first vertex and \((s_j,t_j)\)
at every other vertex. The Hessian is block tridiagonal. Each row
has a fixed bounded number of primitive derivatives, whose arguments
belong to the same compact regular strips. Their absolute row and
column sums have a common finite bound. Enlarging that bound gives
the asserted \(C>\mu\). \(\square\)

The same proof of (3) holds when \(b\) ranges over \(Q\);
existence here uses only its typed disk. Define the exact cut action
\[
                         H_m(b)=\mathcal A_m(z_m(b);b).
 \tag{4}
\]
Its derivative depends on just the last leg:
\(H_m'(b)=G_b(t_m(b),b)\).

## 2. A direct bound for propagation from the actual end

Here is the inverse estimate used below. Let \(A\) be any
averaged negative Hessian along a segment in the product of Lemma 1.
It is complex, block tridiagonal, and obeys
\(\Re A\succeq\mu I\), \(\|A\|_2\le C\). Put
\[
 \tau=\mu/C^2,\qquad q=\sqrt{1-\mu^2/C^2}<1.
 \tag{5}
\]
For every complex vector,
\(\|(I-\tau A)v\|^2\le(1-\mu^2/C^2)\|v\|^2\).
The block in \((I-\tau A)^k\) joining vertices \(i,j\)
vanishes for \(k<|i-j|\). The convergent geometric expansion
therefore gives the length-independent estimate
\[
 \|(A^{-1})_{ij}\|\le\frac{\tau}{1-q}q^{|i-j|}.
 \tag{6}
\]
This proof uses the full complex Hessian, not a real-Hessian inverse
or an assumption of entrywise positivity.

In particular, comparing a critical point with any trial whose
gradient is supported at the first vertex gives an outgoing error
at most a fixed constant times \(q^{m-1}\), provided that trial
residual has a uniform bound. No coordinate of the actual first
cap has to belong to the small alternating Fourier chamber.

There is also an immediate consequence for the already identified
complete-ended positive geometries. For an alternating open word,
keep its actual private endpoint legs and auxiliaries and replace
all internal legs by the exact alternating bulk values. This trial
stays in the common convex domain, and its residual is supported
at the two endpoint vertex groups. The bulk logarithmic equations
are exactly zero by
[joint coercivity, Section 4](research_mixed_three_four_joint_coercivity.md).
Thus every actual internal leg obeys
\[
 |z_j-z_{j,\mathrm{bulk}}|
            \le C_1(q^{j-1}+q^{m-j}).
 \tag{7}
\]
The constant is independent of length. By
[source-geometric identification](research_mixed_geometric_source_identification.md)
these are the actual positive geometries. Equation (7) alone is
not yet a cap-phase entrance: a fixed outgoing Fourier parameter
is different from a complete right ordinary boundary.

## 3. Compare the half-chain to the invariant tail

Take alternating prefixes ending in type four. Their first type may
be three or four. Let \(x_0=x_{34}\), and let \(b_*\) be the
type-three bulk inverse leg. Both bulk inverse legs are the exact
ones in (15) of the joint-coercivity theorem, strictly inside their
typed disks. Let \(s(y)\) be the invariant phase centered at
\(x_0\) from
[the invariant-germ theorem](research_mixed_alternating_interface_invariant_germ.md).

Retain the original incidence
\[
 \ell_b(x)=2\pi ibx-
 \frac{\operatorname{Li}_2(e^{2\pi ix}e^{-2\pi ib})
             -\operatorname{Li}_2(e^{2\pi ix})}{2\pi i}-\pi ix.
 \tag{8}
\]
At \((b,x)=(b_*,x_0)\), its wire derivative is \(q_3\),
whereas \(s'(0)=-q_3\). There is consequently a unique local
holomorphic solution \(y=y_\infty(b)\) of
\[
 s'(y)+\ell_{b,x}(x_0+y)=0,
                         \qquad y_\infty(b_*)=0.
 \tag{9}
\]
Indeed \(-\Re s''>0\), and the negative real wire Hessian of
the incidence is positive at this point, by the original joint
Hessian form. The sum in (9) is nondegenerate. Also
\[
 \ell_{b,x b}(x)=\frac{2\pi i}{1-e^{2\pi ix}e^{-2\pi ib}}
                    \ne0,
 \qquad y_\infty'(b_*)\ne0.
 \tag{10}
\]
Define
\[
 H_\infty(b)=s(y_\infty(b))+
                       \ell_b(x_0+y_\infty(b)).
 \tag{11}
\]
Its normalization is only for this comparison; it does not alter
the actual \(H_m\) or its eventual Fourier action constant.

Apply the invariant critical-input map repeatedly to
\(y_\infty(b)\), and recover the intermediate wire and two
index pairs of each original \(3,4\) packet. This constructs
an infinite left tail, tending to the bulk reference, which solves
every internal original stationary equation. All its legs stay in
small fixed neighborhoods of the bulk legs, uniformly in the
number of backward steps, after choosing a small disk
\(\mathcal B\) about \(b_*\). The actual original shared-wire
identity is
\[
 G(t,b)=\ell_t(x)+\ell_b(x),\qquad
 \ell_{t,x}(x)+\ell_{b,x}(x)=0.
 \tag{12}
\]
This identity holds on a full neighborhood of the independent
\((t,b)\) variables, not only on a geometric charge path. Indeed
the rational identities (17)--(18) of the calibration in Section 1
give equality of the exponentiated leg derivatives and the
exponentiated wire equation. All arguments are nonzero on the
local product. Their actual derivative differences have values in
\(2\pi i\mathbb Z\), and their zero lifts at the bulk point
make them zero on that product. The calibrated bulk value then
fixes the additive constant. Equivalently, Section 5 of
[the contracted-phase theorem](research_mixed_contracted_phase.md)
already proves (12) on a connected open neighborhood of its
calibration path to this bulk point. Thus the same original
constants and lifts apply to independent nearby legs. The infinite
tail consequently solves the contracted internal equations of (2).

For each finite prefix make a trial for (2) by using the last
\(m\) vertices of this invariant tail, except that its first
private leg \(s_1\) and auxiliary \(u\) are replaced by their
actual values from \(z_m(b)\). All other trial legs, including
\(t_1\), retain the invariant-tail values. This trial belongs
to the product of Lemma 1. Its gradient can be nonzero only in
the first vertex group: the next shared pair still sees the same
\(t_1\) as the infinite tail. Compactness of \(E,U,Q\) bounds
that residual independently of \(m\) and \(b\in\mathcal B\).
Equations (6), (4), and (12) now prove
\[
 \sup_{b\in\mathcal B}|H_m'(b)-H_\infty'(b)|
                                \le C_2 q^{m-1}.
 \tag{13}
\]
One first chooses a slightly larger closed disk for this comparison.
On a smaller fixed disk, Cauchy's formula proves the same exponential
convergence for every fixed derivative of these gradients. This is
a uniform holomorphic comparison with the actual cap, not only a
comparison at a sequence of geometric centers.

## 4. Recover the actual outgoing Fourier phase

By the envelope identity, the outgoing wire for the finite prefix
is determined by
\[
                  H_m'(b)=\ell_{b,b}(x_m(b)).
 \tag{14}
\]
Here the second subscript on the right denotes differentiation in
the inverse-leg argument of \(\ell\). Equation (10) makes (14)
solvable near \(x_0+y_\infty(b)\). Equation (13) and its first
derivative consequence show that
\(x_m(b)\to x_0+y_\infty(b)\) with derivatives, uniformly
on a fixed disk. Since \(y_\infty'(b_*)\ne0\), shrink the disk
once more: the inverse function theorem with a uniform small
perturbation supplies inverses \(b=b_m(x)\) on one fixed
disk \(\mathcal X\) about \(x_0\), for all sufficiently
large \(m\).

The original geometric Fourier phase of the finite prefix is
\[
 S_m(x)=H_m(b_m(x))-\ell_{b_m(x)}(x),\qquad
 S_m'(x)=-\ell_{b,x}(x)\big|_{b=b_m(x)}.
 \tag{15}
\]
This is not a new phase chosen to match a derivative. To verify
the identity, remove the last shared term from (2), fix its last
leg \(t=t_m\), and eliminate all other variables. Call the
result \(P_m(t)\). Its elimination Hessian is a principal block
of the accretive Hessian in Lemma 1, so it is nonsingular.
Then \(H_m=\operatorname{stat}_t[P_m(t)+G(t,b)]\).
Using (12), the associated critical system is exactly
\[
 P_m'(t)+\ell_{t,t}(x)=0,\qquad
 \ell_{t,x}(x)+\ell_{b,x}(x)=0.
 \tag{16}
\]
Thus (15) is \(\operatorname{stat}_t[P_m(t)+\ell_t(x)]\),
with the original constant. The local inverse above proves that
its remaining stationary elimination is nondegenerate: the full
system before this last polarization change is nonsingular, and
\(dx_m/db\ne0\). Equivalently this follows by the two scalar
Schur-complement identities for (16).

The finite-source origin of this polarization is
[the exact Fourier bridge](research_mixed_conditional_fourier_message_bridge.md),
equations (3), (8)--(9). The basis factor has precisely the phase
\(\ell_t(x)\); its accompanying factorial power supplies the
own terms already present in \(P_m\). Consequently the original
cap and word, rather than a substituted boundary vector, determine
(15). Equation (13) gives on a smaller fixed \(\mathcal X\)
\[
 \sup_{x\in\mathcal X}|S_m'(x)-s'(x-x_0)|
                                    \le C_3 q^{m-1}.
 \tag{17}
\]
All fixed higher gradient derivatives satisfy the same assertion
after a further fixed shrink. In particular the output momentum
and width converge, and the normalized phase
\(S_m(x_0+y)-S_m(x_0)\) eventually belongs to the open basin
of [the local entrance theorem](research_mixed_alternating_interface_local_entrance_basin.md).

Appending the next \(3,4\) pair now obeys the exact stationary
identity
\[
 S_{m+2}(x_0+y)=\operatorname{stat}_x
          [S_m(x_0+x)+\psi(x,y)].
 \tag{18}
\]
Associativity of the original stationary equations proves this
identity with its action constant, not just up to a gradient.
Thus the increments are exactly the \(C(h)\) of the basin theorem.
Prefixes ending in three have the analogous companion germ obtained
by one original three-vertex attachment; or one may cut one vertex
earlier at the four-ending interface. This does not change either
original cap or the intervening word.

## 5. The nonzero local coefficient and the remaining distinction

The roots used above lie in the original endpoint images and typed
ordinary block images. Those images lie in the smaller disks of
[local factor coverage](research_mixed_open_local_factor_coverage.md).
The external \(b\)-disk can be chosen inside the same reduced
type-three disk. Hence the first cap and every ordinary conditional
factor have their original nonzero local packets, by
[the completed local Gaussian theorem](research_mixed_open_local_gaussian.md)
and its reduced-disk source input. Its proof uses these actual
typed maps, and does not need a right ordinary boundary at a cut.
The last shared factor is the explicit nonzero factorial ratio
of [exact wire contraction](research_mixed_wire_exact_contraction.md),
with phase \(G\). Its arguments remain in their regular strips.

The common cut disk is a phase-domain statement, independent of
length. For the local symbols, the relevant endpoint and ordinary
image families are compact subsets of their proved source domains,
with only finitely many type choices. Compactness therefore gives
fixed small argument neighborhoods on which their symbols are
regular and nonzero. The cut disk may be shrunk once so that the
outgoing incidence is in its corresponding regular neighborhood.
The typed maps and the uniform response bound from (3) and (6)
keep the nearby arguments in those neighborhoods. This supplies a
common small outgoing disk; it does not make product error constants
uniform in the prefix length.

The original cap-initialized local term can therefore be formed
using these literal symbols and the unaliased choices of the wrapped
type-four factors. Its internal Gaussian determinants are nonzero
by Lemma 1 and the elimination in Section 4. Near the outgoing
interface the basis symbol for \(\ell_t(x)\) is regular and
nonzero, and the last determinant is nonzero as well. Thus the
resulting Fourier local current has a nonzero holomorphic leading
coefficient on a fixed smaller disk, for each sufficiently long
fixed prefix. Local contours may be transported with the stationary
eliminations. Both parities and the original scalar factors are
retained by the exact Fourier identity.

No length-uniform relative error for this current is asserted.
For any one sufficiently long fixed prefix, its normalized leading
coefficient has bounded logarithmic derivative on a smaller disk.
Further local paired attachments obey the amplitude estimate of
the basin theorem; after finitely many additional pairs they enter
its invariant bounded-log-derivative class. Every action increment
and nonzero amplitude scalar remains present.

This proves entrance for the geometric phase and the associated
nonzero local current of an actual cap-initialized alternating word.
It does not prove a packet asymptotic for the whole finite Fourier
message. The other wrapped terms, the complement of the chosen
conditional contours, the full Fourier input period, and propagated
finite-source errors still have to be controlled relative to this
same action. In particular the original cap is retained without
turning its local coefficient into an assumed whole-source lower
bound. No new knot-family or cofinite-filling statement follows.

## 6. An arbitrary three/four prefix before the alternating tail

The entrance depth for the phase is independent of the word
preceding the alternating tail. This enlarges the actual source
class without a new reference construction.

**Corollary 2.** Let \(P\) be any finite word in \(3,4\),
including the empty word. Retain its original complete left cap,
and append an alternating tail of \(L\) vertices ending in four.
Apply the half-chain construction (2) to this entire word, with
the same outgoing external leg near \(b_*\). There are a fixed
complex disk \(\mathcal X\) about \(x_0\), constants \(C_4<\infty\)
and \(0<q<1\), and an integer \(L_0\), all independent of
\(P\), such that its original geometric Fourier phase satisfies
\[
 \sup_{x\in\mathcal X}
   |S_{P,L}'(x)-s'(x-x_0)|\le C_4q^{L-1},
                                      \qquad L\ge L_0.
 \tag{19}
\]
Thus its normalized phase enters the same open basin after a
tail length independent of the prefix's length and letter order.
All fixed higher gradient derivatives converge on smaller fixed
disks. The full phase constant \(S_{P,L}(x_0)\) is retained;
no comparison of constants for different prefixes is asserted.

*Proof.* If \(P\) is empty, this is Sections 3--4. Otherwise
write \(k=|P|\). Lemma 1 gives the actual critical point for
the entire word, with the original first cap. Make a comparison
trial by keeping every variable of its first \(k\) vertices,
including the private leg and endpoint auxiliary, exactly at that
actual value. Replace only the last \(L\) vertex pairs by the
last \(L\) pairs of the invariant infinite tail constructed
in Section 3. The concatenation belongs to the same convex typed
product. The join need not alternate: all original ordered type
pairs are covered by Lemma 1 and its finite local-map inputs.

The trial gradient vanishes except possibly at vertex groups
\(k\) and \(k+1\). Earlier prefix groups still see their
unchanged actual neighbors. Later tail groups still see their
invariant-tail neighbors. Only the two groups incident to the
changed shared pair can acquire a residual. Their gradients are
uniformly bounded on the fixed compact source domains, independently
of \(k,L\) and the prefix. This remains true for \(k=1\),
where the first group contains the actual cap variables.

Average the full original Hessian between the actual point and
this trial. Lemma 1 and (6) apply to this matrix for every prefix,
with exactly the same \(\mu,C,q\). Its last block has distances
\(L\) and \(L-1\) from the two possible residual groups.
Consequently the actual last-leg error is at most
\(C_5(q^L+q^{L-1})\). The outgoing derivative is still the
same local expression \(G_b(t_m,b)\). This proves the analogue
of (13), uniformly in \(P\), on the same fixed external-leg
disk. Cauchy estimates and the local inverse-polarization argument
of Section 4 therefore give (19) and a uniform \(L_0\).
All original constants are kept by (15)--(16). \(\square\)

For each fixed word \(P\) and fixed sufficiently long tail,
Section 5 gives the nonzero cap-initialized local coefficient,
because the source-image and symbol statements already cover
arbitrary ordered three/four words. The coefficient and finite-source
error constants may depend on the entire prefix. In particular
the corollary does not permit its length to grow with \(N\),
assert uniform amplitude entrance depths for all prefixes, or
replace the remaining full-message estimate by (19). It also
does not cover other crossing powers, signed short pieces or
branching tangles merely by calling them a finite prefix.

## 7. A finite core outside the accretive class

The preceding proof uses the original three/four Hessian bound on
the entire word. For a general fixed short piece this bound cannot
be assumed. The exact linear obstruction can nevertheless be
isolated in a finite Schur complement. This supplements the existing
[positive-region Schur theorem](research_positive_edge_global_monotonicity.md#6-eliminating-a-positive-filled-region-preserves-the-comparison);
it does not construct a nonlinear attached solution.

### The accretive tail and its finite sections

Let \(T\) be a bounded complex symmetric block-tridiagonal operator
on \(\ell^2(\mathbb N;\mathbb C^d)\), with
\[
 \Re T\succeq\mu I,\qquad \|T\|\le C,\qquad C>\mu>0.
 \tag{20}
\]
Let \(T_n\) be its principal section on the first \(n\)
blocks. With \(\tau,q\) as in (5), both \(I-\tau T\)
and \(I-\tau T_n\) have norm at most \(q<1\). Thus their
geometric series prove invertibility directly, including on the
infinite Hilbert space. Accretivity also gives
\(\|T^{-1}\|,\|T_n^{-1}\|\le1/\mu\). The proof of (6)
gives the same block decay for both inverses, with
\(c_q=\tau/(1-q)\).

Write \(g_n=(T_n^{-1})_{11}\), \(g_\infty=(T^{-1})_{11}\).
A product contributing to the \((1,1)\) block of a tridiagonal
matrix power cannot leave the first \(n\) blocks and return
in fewer than \(2n\) steps. The corresponding Neumann terms
are therefore identical up to degree \(2n-1\). Bounding the
two remaining series separately proves
\[
             \|g_n-g_\infty\|\le 2c_q q^{2n}.
 \tag{21}
\]
This statement concerns principal sections of the specified operator.
If coefficients or a far-end boundary condition are changed, their
effect must be included through a resolvent identity or an independent
convergence bound; (21) is not a claim about arbitrary finite matrices
with the same accretivity constant.

### The finite transversality condition

Let \(B=B^T\) be an \(r\)-dimensional core block, with no
positivity assumption, and let \(E\) be its coupling to the
first tail block. If \(\iota_1\) inserts that block, the
joined matrices and their core Schur complements are
\[
 \mathbb K_n=
 \begin{pmatrix}B&E\iota_1^*\\\iota_1E^T&T_n\end{pmatrix},
 \qquad \Sigma_n=B-Eg_nE^T,\qquad
 \Sigma_\infty=B-Eg_\infty E^T.
 \tag{22}
\]
All couplings use the original bilinear transpose. The same formula
defines \(\mathbb K_\infty\) on the finite core plus the
infinite tail.

**Proposition 3.** The joined infinite operator is invertible if
and only if \(\Sigma_\infty\) is invertible. This is equivalent
to absence of a nonzero compatible square-summable linearized
deformation. If \(\Sigma_\infty\) is invertible, all sufficiently
large \(\mathbb K_n\) are invertible with uniformly bounded
inverses. Their response at tail block \(j\) to a core forcing
\(f\) obeys
\[
 \|y_j\|\le
  2c_q\|E^T\|\|\Sigma_\infty^{-1}\|
                   q^{j-1}\|f\|.
 \tag{23}
\]
The threshold in this assertion and its prefactor may depend on
the fixed core.

*Proof.* Eliminate the invertible tail block. Exact block
factorization proves the first equivalence. If
\(\Sigma_\infty v=0\), the corresponding kernel vector is
\[
              (v,-T^{-1}\iota_1E^Tv).
 \tag{24}
\]
Its tail decays exponentially by (6), and a nonzero full kernel
vector must have \(v\ne0\). This proves the deformation
interpretation, including a possible deformation supported entirely
in the core.

Equation (21) bounds
\(\|\Sigma_n-\Sigma_\infty\|
 \le2c_q\|E\|\|E^T\|q^{2n}\).
For large \(n\), the perturbation of the invertible finite matrix
is smaller than \(1/(2\|\Sigma_\infty^{-1}\|)\), so
\(\|\Sigma_n^{-1}\|\le2\|\Sigma_\infty^{-1}\|\).
Together with \(\|T_n^{-1}\|\le1/\mu\), the block inverse
formula gives a uniform bound for the full inverse. For core
forcing, its solution is exactly
\[
 v=\Sigma_n^{-1}f,\qquad
 y=-T_n^{-1}\iota_1E^T\Sigma_n^{-1}f.
 \tag{25}
\]
This and (6) prove (23).
More generally the tail-to-tail inverse is
\[
 T_n^{-1}+T_n^{-1}\iota_1E^T\Sigma_n^{-1}
                               E\iota_1^*T_n^{-1}.
 \tag{26}
\]
Its correction between blocks \(i,j\) is bounded by a fixed
core-dependent constant times \(q^{i+j-2}\). Thus local tail
response retains exponential decay with distance as well.
\(\square\)

At a specified nonlinear limiting attachment, (22) is its
linearized transversality test: the short piece must have no
compatible deformation decaying into the tail. The candidate
attachment, regular original lifts and the needed nonlinear
neighborhood have to be established separately. Pointwise
nondegeneracy of every finite truncation is insufficient, as the
following exact example shows.

### A boundary resonance despite every finite matrix being positive

Put \(\alpha=(3-\sqrt5)/2\), so
\(0<\alpha<1\) and \(\alpha+\alpha^{-1}=3\).
Take the scalar tail \(T_n\) with diagonal \(3\) and its two
off-diagonals equal to \(-1\). It obeys \(I\preceq T_n\preceq5I\),
as does the infinite tail. Set \(B=\alpha\), \(E=-1\).
The elementary continuant recurrence
\(D_n=3D_{n-1}-D_{n-2}\), \(D_0=1,D_1=3\), gives
\[
 \begin{split}
 D_n&=\alpha^{-n}\frac{1-\alpha^{2n+2}}{1-\alpha^2},\\
 g_n&=\frac{D_{n-1}}{D_n}
     =\alpha\frac{1-\alpha^{2n}}{1-\alpha^{2n+2}},\\
 \Sigma_n&=\alpha-g_n
     =\frac{\alpha^{2n+1}(1-\alpha^2)}{1-\alpha^{2n+2}}>0,
 \qquad \Sigma_\infty=0.
 \end{split}
 \tag{27}
\]
Every finite joined matrix is therefore positive definite. However
\((T_n^{-1})_{n1}=1/D_n\), so the response to unit core forcing
has last coordinate
\[
                         y_n=\frac1{D_n\Sigma_n}
                                      =\alpha^{-n-1}.
 \tag{28}
\]
There is no end-forgetting estimate. The infinite kernel is the
square-summable vector \((1,\alpha,\alpha^2,\ldots)\),
whose only missing equation in a finite section leaves a residual
at its last block. This is a linear model, not a source claimed
to arise from an original tangle. It proves precisely why finite
nondegeneracy, even finite positivity, cannot replace (22).

### What original positive geometry actually discharges

Suppose an attachment of a fixed original filled region to the
limiting tail has already been constructed, all its original edge
tetrahedra are positive, its finite core stays in a compact positive
domain, and the tail stays uniformly in a compact positive domain.
In the original angular coordinates,
[positive-edge monotonicity, Theorem 3 and Corollary 4](research_positive_edge_global_monotonicity.md)
then gives a positive Hermitian part for the edge-period Jacobians.
Summing incidences gives a common positive floor for the joined
operator: the core has finitely many strict margins and the tail
has a uniform one. Real signed filling powers add purely imaginary
diagonal terms, and do not change this conclusion.

The infinite Schur identity applied to
\((v,-T^{-1}\iota_1E^Tv)\) consequently makes
\(\Re(v^*\Sigma_\infty v)>0\) for \(v\ne0\).
Thus the transversality condition is automatic at such an
existing compact positive attachment, even with signed powers
and branching inside the fixed core. Passing to another regular
local geometric chart preserves nondegeneracy; it does not assert
that its particular Hessian remains accretive. The required
attachment and regular cut polarization are still existence and
domain statements. The rigidity theorem alone does not continue
an arbitrary short piece from complete boundary angles to the
alternating boundary.

There is an actual limitation to this positive chart. Its original
period range gives \(|c_v|<(d_v+|n_v|)/2\). A unit-charge
vertex of original degree two and zero power violates this strict
inequality regardless of the length of a neighboring tail. Hence
that presentation cannot be covered by an argument requiring all
of its original edge tetrahedra to stay positive. This is a chart
obstruction, not an unresolved isotopy assertion or a counterexample
to a source or volume theorem; applicable exact tangle reductions
are unchanged. The arbitrary three/four-prefix corollary above
has no such additional attachment premise, because its actual
half-chain existence was proved by the original typed maps.
