# Two actual flow cuts give a strict matrix and coherent Green complex

Research construction, 27 October 2026. Once two actual physical
edge positions a,b have been retained, their zero-extended array is
one matrix with independent row and column clocks. Both finite Green
currents, all boundary rows/columns/corners, and the original 1/N
co-source have an exact Laurent/coherent realization. This does not
identify a physical single-port Hopf action with matrix multiplication,
and does not assume that the geometric Gaussian commutes with the
construction.

The physical existence, four-port ordering and integral flow-chart
choice are supplied by
[the actual two-cut reconstruction](actual_two_cut_framing_port_reconstruction.md).
The second
cut is an INTERNAL IDENTITY edge: no new pivot is inserted there.
All original pivots, caps and scalar peripheral factors remain in
the actual array. Only a diagonal transport ALREADY present on that
edge may be absorbed in its definition.

## 1. The actual array, source and independent clocks

Let f(a,b) be a finite zero-extended array on Z^2 over the original
coefficient algebra, after the specified other finite sums. All flow
constraints and their zero entries are retained. On the head window
0<=a,b<N put J_ab=f(a,b), and n=N-1. The actual selected state is
head-supported, and its period is

\[
             \Phi(J)=\frac1N\sum_{a,b=0}^{n}J_{ab}.  \tag{1}
\]

There is no second factor 1/N. In particular this is the original
rank-one average matrix row Tr(eJ), e_ab=1/N, rather than Tr(J)/N.
The matrix is a reshaped DOUBLE-DIAGONAL four-port array, not an
ordinary open-knot endomorphism. No scalarity condition J=cI is
imposed on it.

Let A=diag(1,Q,...,Q^n). The two actual characters are exactly

\[
            A_1J=AJ,\qquad A_2J=JA.                \tag{2}
\]

Both remain independent before the final source pairing. Their
whole q-germs, including Q^N, are retained before root evaluation.

## 2. Exact shifts and every boundary term

Let Ue_j=e_(j+1), j<n, and Ue_n=0. Define endpoint rows and columns
r_+(b)=f(N,b), r_-(b)=f(-1,b),
c_+(a)=f(a,N), c_-(a)=f(a,-1), restricted to the other head index.
Then literal coordinate translations have the matrix formulas

\[
 \begin{split}
 \Pi S_a^+f&=U^tJ+e_n r_+,&
 \Pi S_a^-f&=UJ+e_0r_-,\\
 \Pi S_b^+f&=JU+c_+e_n^t,&
 \Pi S_b^-f&=JU^t+c_-e_0^t.
 \end{split}                                                   \tag{3}
\]

Here Pi is head-window restriction; these are coordinate-array
translations, not physical single-port raising/lowering actions.
The endpoint rows themselves translate and have endpoints. For
example

\[
 \Pi S_a^+S_b^+f=U^tJU+e_n r_+U+U^tc_+e_n^t
                                      +f(N,N)e_ne_n^t.          \tag{4}
\]

More generally choose L_+=U^t,L_-=U, R_+=U,R_-=U^t,
e_+=e_n,e_-=e_0 and t_+=N,t_-=-1. Then

\[
 \Pi S_a^\epsilon S_b^\eta f
 =L_\epsilon JR_\eta+e_\epsilon r_\epsilon R_\eta
     +L_\epsilon c_\eta e_\eta^t
     +f(t_\epsilon,t_\eta)e_\epsilon e_\eta^t.       \tag{5}
\]

The corner term is required for the two translations to commute.
Longer words keep the corresponding finite strips and corners;
there is no fixed finite head matrix representation of all
translations without this tail data.

The co-source versions of (3) are equally explicit:

\[
 \Phi(\Pi(S_a^+-1)f)=\frac1N\sum_{b=0}^n[f(N,b)-f(0,b)],
\]
\[
 \Phi(\Pi(S_a^--1)f)=\frac1N\sum_{b=0}^n[f(-1,b)-f(n,b)],       \tag{6}
\]

with the analogous two column formulas. A clock on an endpoint
uses Q^N or Q^(-1), not one substituted from its root value.
The exact Weyl relation S_a^+ A_1=Q A_1 S_a^+, and its three
counterparts, includes these endpoint coefficients.

## 3. A whole Laurent kernel retains the tails strictly

Define the finite Laurent polynomial

\[
             \mathscr F_f(x,y)=\sum_{a,b\in\mathbb Z}f(a,b)x^ay^b.
                                                               \tag{7}
\]

This map is injective and has the exact operator dictionary

\[
 S_a^+\leftrightarrow x^{-1},\quad S_a^-\leftrightarrow x,
 \quad S_b^+\leftrightarrow y^{-1},\quad S_b^-\leftrightarrow y,
\]
\[
 A_1\leftrightarrow[x\mapsto Qx],\quad
 A_2\leftrightarrow[y\mapsto Qy],\quad
 a\leftrightarrow x\partial_x,\quad b\leftrightarrow y\partial_y.
                                                               \tag{8}
\]

Consequently arbitrary ordered clock/shift words and every retained
polynomial Green moment are transported exactly. External meridian
Ore operators act on the coefficient algebra with their original
order. Q derivatives of a dilation include its Euler chain-rule
term; the source's normal terms are not frozen before differentiation.
If an external Ore shift changes a chosen source/basis frame L,
its transported operator is L_after O sigma(L_before^(-1)), with
the specified semilinear coefficient action. It is not ordinary
conjugation by a frame which the Ore shift has changed.

For head-supported states (1) is exactly

\[
 \Phi_{full}(f)=\frac{\mathscr F_f(1,1)}N
  =\frac1N\operatorname{Res}_{x=1}\operatorname{Res}_{y=1}
       \frac{\mathscr F_f(x,y)\,dx\,dy}{(x-1)(y-1)}. \tag{9}
\]

The same expression on currents sums ALL their finite tails. It
equals the head row plus the explicit outside-window sum divided
by N. Thus it kills both full zero-extended differences, while
(6) records exactly the boundary removed by restricting to the
head. No cyclic interpretation of either actual coordinate is used.

## 4. Explicit two-current complex and its contraction

Write d_x=x^(-1)-1,d_y=y^(-1)-1. The actual two-flow Green complex
on finite Laurent kernels has

\[
 d_1(P,Q)=d_xP+d_yQ,\qquad
 d_2(H)=(d_yH,-d_xH),\qquad\Phi_{full}d_1=0.        \tag{10}
\]

All actual finite certificate identities map to this complex
coefficientwise. Define P_xF=F(1,y), P_yF=F(x,1), and

\[
 H_xF=\frac{F-P_xF}{x^{-1}-1},\qquad
 H_yF=\frac{F-P_yF}{y^{-1}-1}.                       \tag{11}
\]

The quotients are Laurent POLYNOMIALS: their numerator vanishes
at the indicated source point. In the original array, for example,
H_af(a,b)=-sum_(k>=a)[f(k,b)-delta_(k,0)sum_u f(u,b)]; this is
a finite sequence. Put

\[
 h_0(F)=(H_xF,P_xH_yF),\qquad h_1(P,Q)=-H_xQ.       \tag{12}
\]

Direct substitution gives

\[
 d_1h_0F=F-F(1,1),\quad
 h_0d_1+d_2h_1=I,\quad h_1d_2=I.                   \tag{13}
\]

Thus both currents and their common corner/syzygy have a specified
finite contracting homotopy. There is no inferred Gaussian or
Stokes operation in this identity.

If the section is chosen as the literal matrix identity, let
E_N(x,y)=sum_(a=0)^n(xy)^a, so Phi(E_N)=1, and let
Gamma=h_0(E_N-N). Replace h_0 by

\[
            h_0^{I}(F)=h_0(F)-\Gamma\Phi_{full}(F). \tag{14}
\]

Then d_1h_0^I=I-E_N Phi_full, while the other identities remain
unchanged. The 1/N in the original source is therefore preserved
by the pointed complex; it has not become 1/N^2. This section is
a specified homotopy anchor, not a claim that every physical
two-cut tangle has identity matrix.

## 5. Global P1 kernel and the literal source/co-source

The core polynomial (7) has bidegree at most (n,n), hence is a
section of O(n) external_tensor O(n) on P1_x times P1_y. A single
matrix operator kernel uses the dual coordinate w=y^(-1):

\[
 \mathcal K_J(z,w)=\sum_{a,b=0}^nJ_{ab}z^a w^{-b-1}\,dw.
                                                               \tag{15}
\]

In the monomial identification of the actual head basis with
H^0(P1,O(n)), its input factor is the explicit Serre-dual Cech
class in H^1(P1,O(-n-2)). The ACTUAL head ket and row are
psi(w)=sum_(b=0)^n w^b and evaluation at z=1 divided by N. Thus

\[
       \Phi(J)=\frac1N\operatorname{Res}_{w=0}
                                     \mathcal K_J(1,w)\psi(w). \tag{16}
\]

This keeps the original uniform ket/dual, rather than replacing
them by binomial coherent weights or compact ordinary trace.
If a binomial-normalized coherent frame is desired, its diagonal
source and dual adapter must be carried explicitly. No positivity,
metric isometry or asymptotic phase is inferred from this vector
space identification.

Both clocks and the shifts act on (15) as in (8); for the input
clock its action is the ONE-FORM pullback w->w/Q, which includes
the differential factor. This avoids a spurious factor Q in
the right clock. On the coefficient of dw the input index b is
-w partial_w-1; the missing -1 would give the wrong moment.
Matrix composition, when it is actually used, is exactly

\[
 \mathcal K_{JH}(z,w)=\operatorname{Res}_{u=0}
                                \mathcal K_J(z,u)\mathcal K_H(u,w),
\]

with the input/output differential factors retained. It is not
pointwise multiplication of symbols, nor a claim that the physical
four-port tangle composes by the reshaped matrix product.

The full tails in (7) are meromorphic sections with possible poles
only at zero and infinity in each coordinate. Keep them as such,
or as the corresponding relative Cech cochains with their explicit
boundary rows. Projecting them to the finite H^0/Serre quotient
would discard the terms (3)--(6). The whole residue (9) is regular
on these finite Laurent sections and preserves them. This gives
one global meromorphic matrix/coherent Green complex for both
actual coordinate currents, with no hypothetical extra Fr flag.

Here is an explicit principal-part/Cech description of the tails.
For O(n) on U_0 and U_infinity use the transition z^n and write
every finite meromorphic section uniquely as

\[
 p(z)=p_{<0}(z)+p_{[0,n]}(z)+p_{>n}(z).
\]

The first and last summands are respectively the finite principal
parts at zero and infinity; the middle one is H^0(O(n)). This is
the global-section form of
0->O(n)->O(n)(*0+*infinity)->principal_parts->0. Exactness is
immediate from the displayed Laurent splitting. Two coordinates
give N-by-N core, four strips and four corner principal parts.
The two one-step rules are, for a core polynomial,

\[
 \Pi(z^{-1}p)=\frac{p-p(0)}z,\qquad
 \Pi(zp)=zp-p_nz^{n+1}.                            \tag{16a}
\]

The discarded monomials are precisely the outgoing principal
parts; the incoming ones give the last row or first row in (3).
Tensoring these splits gives the explicit corner formula (5).
Thus this is a strict global meromorphic/relative-Cech lift of
the actual finite tail data, rather than an appeal to a different
cohomology class with the same scalar value. Its source evaluates
ALL nine regions at (1,1) with the one factor 1/N.

## 6. One-cut restriction and the physical Hopf distinction

Closing the second identity cut gives the original one-cut array
p_a=sum_b J_ab, hence C_one=diag(p_a) and

\[
        \Phi(J)=\operatorname{Tr}(C_{one})/N.        \tag{17}
\]

The second clock and current cannot in general be reconstructed
from C_one: matrices with zero row sums can have nonzero weighted
row sums after right multiplication by A. Keeping J avoids exactly
that loss. Neither its two clocks nor its arbitrary off-diagonal
entries are subject to an ordinary open-knot Schur condition.

The ACTUAL physical single-port Hopf actions of the four-port
tangle need not descend to J. They can create off-diagonal port
bands, whose source uses the corresponding original cut pairing.
Equations (2)--(8) concern simultaneous coordinate translations of
the scalar/charge-zero flow array, not that separate Hopf diagram.
The necessary port-band current extension is therefore retained
as an additional map; it is not asserted by this matrix reshape.
Their exact bands and current audit are recorded in
[the physical port-band calculation](two_cut_port_band_current_audit.md).

The finite two-flow certificate now has an exact global coherent
and sourced relative complex. Establishing that the nondegenerate
geometric Gaussian pushforward is a map into this complex, with
the same marked endpoint/carry data, remains a theorem to prove.
No such commutation, nonzero selected geometric contribution or
volume limit is inferred here.

## 7. An exact band involution and the identity-cut residue sign

A nontrivial geometric deck which fixes BOTH position clocks cannot
be an exact source-preserving involution on the bare matrix J.
Indeed the two operators L_A,R_A have jointly simple eigenvectors
E_ab. A linear map commuting with both is a Schur multiplier
E_ab->w_ab E_ab. Since Phi(E_ab)=1/N, preserving the original
source forces every w_ab=1. An anti-source map similarly gives
only -I. This is a fixed-level obstruction, not a prohibition on
a transform with nontrivial internal/band multiplicity or only
semiclassically fixed clocks.

The retained PHYSICAL PORT BANDS have such multiplicity. In the
actual band convention put

\[
 J^{\mu,\nu}_{a,b}=T_{a+\mu,b+\nu;a,b},\qquad
 (\mathcal I J)^{\mu,\nu}_{a,b}
                       =J^{-\mu,-\nu}_{a+\mu,b+\nu}. \tag{18}
\]

This is simply input/output transpose of the full four-port tensor.
It is exactly involutive and preserves the actual full source
N^(-1) sum_(mu,a,b) J^(mu,0)_(a,b), with zero-extended bounds.
It is not asserted to be a symmetry of the actual knot word.
It exchanges input/output clocks; the CENTERED clocks
Q^(a+mu/2), Q^(b+nu/2) are fixed exactly. Their square-root mark
is the original q with q^2=Q. They restrict to the physical
position clocks on the zero band. Simultaneous coordinate
translations in a,b commute with this involution.

The finite Laurent band kernel and its exact transformation are

\[
 F_T(x,y;\xi,\eta)=\sum J^{\mu,\nu}_{a,b}x^ay^b\xi^\mu\eta^\nu,
 \qquad F_{\mathcal IT}(x,y;\xi,\eta)
                               =F_T(x,y;x/\xi,y/\eta).          \tag{19}
\]

The original second identity-cut co-source is the eta constant
term of F_T(1,1;1,eta)/N. Its period form is

\[
              \theta_T=F_T(1,1;1,\eta)\frac{d\eta}{N\eta}.
\]

For inversion iota(eta)=eta^(-1) the natural ONE-FORM identity is

\[
                     \iota^*\theta_T=-\theta_{\mathcal IT}.     \tag{20}
\]

Thus the scalar coefficient source is even, but its Cech residue
orientation line is canonically odd: inversion exchanges zero
and infinity, and Res_infinity(theta_T)=-Res_0(theta_T). This
sign follows from the literal identity-cut residue, rather than
from an assigned choice of geometric orientation.

Equations (18)--(20) give a candidate source sign line for a
geometric deck with anti-invariant density. To use it one must
still prove that the geometric deck lifts to this actual port
involution and transport the whole R/word and source frames.
Transposition swaps left and right insertions and reverses
operator order; no unchanged single-port Hopf row or unproved
Weyl symmetry is inferred. The fixed-clock bare-matrix obstruction
and the full-band candidate are distinct, exact statements.

[Exact shifts, source, global-kernel and two-current audit](../experiments/audit_two_cut_matrix_green_and_coherent_source.py).
The [results](../experiments/two_cut_matrix_green_and_coherent_source_results.json)
pass fourteen root/whole-Q families N=2,...,8 and 742 head-plus-tail
matrix units. They check every signed shift/corner, whole boundary
clock, literal 1/N source and both current homotopies. An additional
1956 physical four-port matrix units check the candidate band
involution, centered clocks and source; the residue orientation
sign is checked symbolically. These tests do not identify that
involution with the geometric deck or establish a Gaussian map.
