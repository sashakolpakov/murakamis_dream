# Three blocks of three crossings, with the original outside boundaries

Research proof, 4 November 2026. Frozen manuscripts and the established
length-at-least-four results are unchanged.

This proof uses the original two caps and one retained vertex together.
It does not enlarge the prepared-cap packet to the displaced three-block
critical wire. The wire exterior is reduced by an exact full-period
identity, and the central six-variable contour keeps every connecting
current.

## 1. Original source and statement

Use the original matrices, trace pairing and half-band cardinal vector:
\[
 A=JM^3=A^T,\qquad W_N(x,w)=v(w)^TAh(x),\qquad
 Z_{3,N}(w_L,w_R)=v(w_L)^TA^3v(w_R).
 \tag{1}
\]
These identities hold in the full original algebra, including both
values and first normals at repeated spectral roots; see
[the all-level trace identities](research_quantum_cap_primitive_source.md#2-the-actual-crossing-and-turn-substitutions)
and [the exact traced-vertex formula](research_traced_three_vertex_endpoint.md#1-the-original-traced-vertex).
Let \(L=\lfloor N/40\rfloor\), \(\widetilde A=A-E_{40}\), and
\(\widetilde V_N(x,y)=h(x)^T\widetilde A h(y)\). Both matrices
\(A,\widetilde A\) are symmetric. Write
\[
 x_h=\frac16+iY_h,\quad Y_h=\frac{\log2}{2\pi},\quad
 P=[-1/8,7/8]+iY_h,\quad I=[7/50,1/5]+iY_h,
 \quad B=[1/4,9/20].
 \tag{2}
\]
The source with its middle corner removed is exactly
\[
 \widetilde Z_{3,N}
 =N^2\int_{P^2}W_N(x,w_L)\widetilde V_N(x,y)W_N(y,w_R)\,dx\,dy
 =v(w_L)^TA\widetilde AAv(w_R).
 \tag{3}
\]
In particular the original first and last caps are not corner-deleted.
The identity \(N\int_Ph(x)h(x)^Tdx=I_N\) gives (3) at both parities.
At even levels each individual half-band factor is antiperiodic; the
products being integrated have period one.

**Theorem 1.** On a fixed ordinary-color neighborhood of
\((w_L,w_R)=(-2,-2)\), the original source (1) has the nonzero packet
\[
 Z_{3,N}(w_L,w_R)
 =C_{N,3}^2\kappa N^{-3/2}a_3(w_L,w_R)
       e^{N\mathcal S_3(w_L,w_R)}(1+O(N^{-1})),\qquad a_3\ne0.
 \tag{4}
\]
The carrier conventions are the original ones. The error is uniform
on smaller neighborhoods, with every fixed ordinary derivative and
both level parities. Its complete-color action is the original
positive three-block marked partial filling, with the two outside
ends complete:
\[
 M_3:=\Re\mathcal S_3(-2,-2)
       =\frac{\operatorname{Vol}(M_3^{\mathrm{marked}})}{2\pi}
       >\frac{63519}{20000}=3.17595.
 \tag{5}
\]
There are constants \(d,b,h_0>0\) such that, for real outside angles,
\[
 |Z_{3,N}(-2\cos(u+iv),-2\cos(u'+iv'))|
 \le CN^q\exp N\{M_3-d(2-\cos u-\cos u')+b(v^2+v'^2)\},
 \quad |v|,|v'|<h_0.
 \tag{6}
\]
Every fixed ordinary outside derivative has the same exponential
bound with polynomial cost. This is an original scalar-source theorem.
Its identification with a knot invariant requires the original
component and filling conditions; no such identification is inferred
from (1) alone.

## 2. Exact removal of the wire exterior

Put \(E=P\setminus I\), and let \(\mathcal B_N(y,w)=v(w)^TA^2h(y)\).
Closing one entire period, before taking an absolute value, gives
\[
 N\int_PW_N(x,w)\widetilde V_N(x,y)\,dx
     =\mathcal B_N(y,w)-v(w)^TAE_{40}h(y).
 \tag{7}
\]
The [whole-period prepared-source theorem](research_three_prepared_cap_period_bound.md)
bounds the first term by \(\operatorname{poly}(N)e^{1.91164N}\)
at the complete ordinary color and its fixed derivatives. The rate
\(1.91165\) is available on a sufficiently small fixed complex
ordinary-color neighborhood. The separate
[Fourier-corner theorem](research_three_chain_fourier_corner_transfer.md#4-a-larger-deleted-corner-for-a-larger-source-domain)
bounds the second term by rate \(1.715\), uniformly in the outgoing
real wire period.

The same \(1.91164\) upper bound for \(\mathcal B_N\) holds for
**all real outside colors**, with fixed ordinary derivatives. This is
an implication of its written source proof, although its stated theorem
only mentions completeness and a small complex neighborhood. Here is
the explicit deduction. Lemma 1, equation (5), of
[the free-boundary observation proof](research_free_boundary_half_charge_observation.md)
gives the unchanged low-kernel exponent \(\Re\Psi(t)\) for every
real outside angle; its equation (11) retains the original physical
values and first normals. Lemma 1 of
[the outside-boundary proof](research_three_chain_outside_boundary_decay.md)
checks their application to every preparation contour, radical and
corner. Thus the three rows in Section 3 of the period-bound proof
remain, uniformly in the real outside color:

| Retained preparation piece | Cap upper rate | Vertex upper rate | Sum |
| --- | ---: | ---: | ---: |
| Central wire | 1.26465 | .64699 | 1.91164 |
| Exterior wire at \(Y_h\) | 1.264 | \(2c<.646132\) | <1.910132 |
| Both wire joins | 1.2638 | .64699 | 1.91079 |

Its Fourier-corner restoration is below 1.715 uniformly on the real
ordinary-color interval. This proves the asserted all-real bound;
it is not inferred from analytic continuation of a complete-end
asymptotic. In particular the slightly weaker rate 1.91165 used below
is valid for all real outside colors as well.

The original cap on \(E\) has rate below \(1.264\),
by the sharpened exterior certificate used in the prepared-source
proof. Hence each of the two integrals on \(E\times P\) and
\(P\times E\), with its full opposite period performed first, has
rate below \(3.17565\).

The exact inclusion--exclusion identity is
\[
 \int_{P^2}-\int_{I^2}
       =\int_{E\times P}+\int_{P\times E}-\int_{E^2}.
 \tag{8}
\]
On \(E^2\), the retained vertex has its termwise whole-torus bound
\(2c<.646132\), and both original caps have rate \(1.264\).
Thus this last term has rate below \(3.174132\). Every wire exterior
in (8) is strictly below (5). The use of (7) is essential: no bound
for a full-period canceled sum is applied to an arbitrary wire subset.
Likewise no restricted ordinary-boundary corner estimate is needed.
All corner terms introduced in (7) retain their Fourier endpoint.

## 3. Original cap remainders and the full real-index complement

On the remaining wires \(I^2\), first keep their heights equal to
\(Y_h\). Open each original cap with the fixed half-grid angular cut
\(T_N=41/20+O(N^{-1})\) and fixed bottom height
\[
 H_0=\frac{24961509}{25000000}=.99846036.
 \tag{9}
\]
This is the same original full-trace reduction as
[the cap complementary-contour proof](research_three_cap_wire_complement.md#3-one-fixed-trace-rectangle-through-the-factorial-walls).
The new outward certificate checks all nine domains: the positive
central bottom, negative bottom, positive bottom beyond \(1.8\),
both folded verticals split at height \(2\pi Y_h\), omitted physical
rows, and the removed outside radical. It proves
\[
 \begin{array}{c|c}
 \text{whole cap and its central positive bottom}&<1.267\\
 \text{each other angular current or physical tail}&<1.26\\
 \text{removed outside radical}&<2/3.
 \end{array}
 \tag{10}
\]
The reflected primitive retains both cosine factors. The trace
midpoints retain their half-residue/folded terms, the odd simple node
retains its value, and the original first normals are bounded before
any asymptotic replacement. Only a polynomial upper exponent for the
low complete kernel is needed away from its selected critical point.
All colors on the fixed angular rectangle lie in a compact subset
of \(\Re(-2\cos t)<2\).

We remove the full real-index complement before any index contour
change. The exact retained summands have the absolute envelope
\[
 \mathscr E(s,t)=\log2+\mathcal J(s+t)-(s+t)\log2-\ell(s)-\ell(t),
 \qquad
 \ell(s)=\int_{-s/2}^{s/2}\log|1-\tfrac12e^{2\pi iu}|\,du,
 \tag{11}
\]
where \(s=i/N,t=j/N\), \(s+t<1\), and
\(\max(s,t)>1/40\). This upper bound is uniform in both real wire
phases and applies termwise, including the finite endpoint factors.
It follows from the sliding-interval minimum in
[the global retained bound](research_three_vertex_global_wire_bound.md).

**Lemma 2.** The real-index complement of \(B^2\) has rate below
\(.6413\), uniformly on the whole wire torus at height \(Y_h\).

*Proof.* Write \(p=s+t\). For \(p\le1/3\), the elementary
bound \(\ell(s)\ge-s\log2\) gives
\(\mathscr E\le\log2+\mathcal J(p)\). The latter function has
its maximum on \([1/40,1/3]\) at an endpoint. The estimates
\[
 \mathcal J(1/40)\le\tfrac1{40}\{\log(\pi/20)-1\},\qquad
 \mathcal J(1/3)=-c/3<-8/75
 \tag{12}
\]
put both endpoint rates below \(.623\).
For \(1/3\le p\le1/2\), increase the smaller index, which is at
most \(1/4\). Its envelope derivative is strictly positive because
\[
 \sin^2(\pi p)\ge3/4>5/4-\cos(\pi/4)
      \ge|1-\tfrac12e^{\pi i\min(s,t)}|^2.
 \tag{13}
\]
Continuing until \(p=1/2\) therefore only increases the envelope.
Convexity of \(\ell\) shows that the maximum on this last line is
at \((1/4,1/4)\).

On the full convex region \(p\ge1/2\), the envelope is concave:
\[
 -D^2\mathscr E
 =\operatorname{diag}(\ell''(s),\ell''(t))
                   -\pi\cot(\pi p)\begin{pmatrix}1&1\\1&1\end{pmatrix}.
 \tag{14}
\]
On \(B^2\), each diagonal entry exceeds \(7/5\). Indeed
\(\ell''(s)=\pi\sin(\pi s)/(5/2-2\cos(\pi s))\) decreases on
\([1/4,9/20]\), and its value at \(9/20\) is greater than \(7/5\).
The established global maximum is \((1/3,1/3)\), of value \(2c\).
A ray from this point to a point outside \(B^2\) first meets its
boundary at distance at least \(1/12\); integrating (14) up to
that first boundary gives loss at least \(7/1440\). Concavity
prevents the envelope from increasing afterwards. Consequently
\[
 \sup_{(s,t)\notin B^2}\mathscr E(s,t)
 \le\max\{.623,2c-7/1440\}<.6413.
 \tag{15}
\]
Uniform finite-product errors and the number of summands are
polynomial. Original half-grid cut offsets change the exponent only
by \(O(N^{-1}\log N)\). This proves the lemma. \(\square\)

Using (10), the discarded real-index complement in the full two-cap
source has rate below \(2(1.267)+.6413=3.1753\).
For the retained real indices in \(B^2\), expand the two exact cap
reductions into their central positive bottoms and their remainders.
One remainder is bounded by \(1.26\). Pair the other positive bottom
with the retained vertex before taking absolute values: the coherent
one-cap plus retained phase has a concave supporting-plane upper
\(1.914\) at the initial heights (9), as checked in the separate
[central-current certificate](research_three_chain_three_central_currents.md#5-a-coherent-upper-estimate-for-an-angular-remainder). Thus every one-remainder term is below
\(3.174\). Two remainders may instead use the termwise retained
bound \(2c\), giving rate below \(3.166132\). This order never
multiplies estimates whose original cancellations have been removed.

## 4. The six-variable central integral

For the surviving two positive cap bottoms set
\[
 G(x,y,\tau,\sigma,s,t)
 =b(x,\tau)+\Psi(\tau)+\frac{3i\tau^2}{4\pi}-i\tau
  +b(y,\sigma)+\Psi(\sigma)+\frac{3i\sigma^2}{4\pi}-i\sigma
  +F(s,t;x,y)-\pi i(x+y).
 \tag{16}
\]
Here \(b,\Psi\) are the original continued factorial and complete-edge
phases, and \(F\) is the literal retained two-index phase with the
exact Pochhammer interpolation. All additive constants are retained.
Its initial real box is
\[
 (\Re x,\Re y)\in[.14,.20]^2,\quad
 (\Re\tau,\Re\sigma)\in[0,1.8]^2,\quad(s,t)\in B^2,
 \tag{17}
\]
with imaginary heights \((Y_h,Y_h,-H_0,-H_0,0,0)\).

The two finite index sums are represented by their exact half-grid
cotangent rectangles \(B+i[-.01,.01]\), retaining all products of
vertical and horizontal sides. Convexity in the imaginary index
coordinates reduces the vertical products to their height corners.
The [central-current theorem](research_three_chain_three_central_currents.md)
proves the following bounds on the coherent
phase, rather than on three independently maximized factors:
\[
 \begin{array}{c|c}
 \text{every product containing an index vertical}&<3.17\\
 \text{all four horizontal index products}&<3.182\\
 \text{initial wire and angular translation faces}&<3.174.
 \end{array}
 \tag{18}
\]
Each nonconstant cotangent mode costs \(2\pi(.01)\), so its rate
is below \(3.12\). The constant terms combine with coefficient
\(+N^2\). The real vertical sides connecting their horizontal
principal planes to index height zero are already included in (18).

The original three-variable period system has its positive solution
\[
 3t_j+2i\sum_{k=j-1,j+1}
       \operatorname{asinh}\{\tan(t_j/2)\cos(t_k/2)\}=2\pi,
 \quad j=1,2,3,\qquad t_0=t_4=0.
 \tag{19}
\]
A fresh complex Newton self-map uses the exact length-three rational
centers of the all-length geometric proof. Its known positive root
lies strictly within the new uniqueness ball, identifying all
unexponentiated lifts. The separate central checker evaluates the
original action and verifies (5), all branch domains and the face
distances. Approximate coordinates, for orientation only, are
\[
 \begin{split}
 t_1=t_3&\simeq1.526265809475-.974414420048i,\\
 t_2&\simeq1.648467454856-1.045002014313i,\\
 x_c=y_c&\simeq.179656179658+.098814696942i,\\
 s_c=t_c&\simeq.345347013844-.004576857612i.
 \end{split}
 \tag{20}
\]
These identify the critical point of (16) by the exact source/geometric
stationarity identities; no numerical near-stationarity is used as
a coefficient argument.

The strict Hessian estimate in
[the joint concavity proof](research_three_vertex_joint_concavity.md)
adds edgewise to give, throughout the relevant chamber,
\[
 -\Re D^2G\ \ge
 (3/4+\pi/5)(dx^2+dy^2)+(3/4)(ds^2+dt^2)
                         +(d\tau^2+d\sigma^2)/(20\pi).
 \tag{21}
\]
It holds for every height on the segment from (17) to (20). At the
critical heights every real boundary face is below \(M_3-1/4000\).
Translate the entire principal six-dimensional rectangle simultaneously.
Holomorphy changes (21) into convexity along this imaginary translation;
on each prism face the upper exponent is bounded by the maximum of
its initial bound (18) and its final critical-height bound. All wire,
angular and index connecting currents are therefore strictly below
\(M_3\). No independent rectangular combination of unrelated heights
is asserted. The half-grid offsets and smooth local cutoff preserve
the strict gaps.

On the final plane (21) gives the unique global real maximum. Only
near that point is a nonzero complete-edge asymptotic symbol used.
On the rest, the factorial symbols and the literal low complete kernel
have their uniform polynomial upper exponents. All six local symbols
are holomorphic and nonzero. The two wire contractions give \(N^2\);
each original unsummed cap density has power \(N^{-1/2}\), and the
retained index density, including its \(+N^2\) cotangent factor,
has power \(N^{1/2}\). The resulting \(N^{3/2}\) density and six
Gaussian integrations give \(N^{-3/2}\). Their unit factors are
exactly \(C_{N,3}^2\kappa\). The determinant square root has the
original analytic lift, and the coefficient of this principal local
piece is one. Every other piece has a strict exponential gap, so it
cannot cancel this nonzero coefficient.

Finally the two-ordinary-boundary corner estimate gives
\[
 |Z_{3,N}-\widetilde Z_{3,N}|
   \le\operatorname{poly}(N)e^{N(5c+M_\infty+27/200)}
   <\operatorname{poly}(N)e^{3N}.
 \tag{22}
\]
This is a bound on the full original contracted source and suffices
here, after the retained contour has been completed. It restores
exactly (1), with all original ordinary jets. The connected open
[action/volume calibration](research_three_chain_action_volume_calibration.md)
identifies (16) with the original marked action up to its prescribed
purely imaginary constant, proving the equality in (5).

## 5. Free outside colors and the full boundary period

All noncritical bounds above remain valid uniformly for real outside
colors. The precise justification is the source argument of
[Lemma 1 of the outside-boundary proof](research_three_chain_outside_boundary_decay.md#1-the-ordinary-boundary-in-the-preparation-contours):
the literal low kernel on every noncritical cap contour has the same
polynomial upper exponent \(\Re\Psi(\tau)\), uniformly in the real
outside angle; removed physical values and first normals have their
uniform real-color bounds; the odd simple node uses its value only.
The original radical and corner errors are also uniform in these
colors. The whole-period estimate in (7) is obtained by the same
source decomposition and these uniform bounds, so it retains its
rate \(1.91165\) for all real outside angles. This is an upper
bound deduced from its proof, not a claim that a complex kernel is
maximized by its complete-end value.

Near the selected point (20), both end angles lie strictly inside the
free-edge whole-period domain \(0<\Re\tau<\pi/2\),
\(0<-\Im\tau<1.07\), \(|\cos(\tau/2)|<1\). Thus each actual
outer edge subtracts a positive multiple of \(1-\cos u\) from the
local density exponent. Every other piece already has a strict
complete-color gap. Decrease the angular-loss constant so that the
sum of the two possible losses, with \(1-\cos u\le2\), fits below
all these gaps. This gives the real-period version of (6).

Small complex outside perturbations preserve all strict contour
inequalities, and the critical equations and local amplitudes move
holomorphically. This proves the actual local packet (4). Its outside
angular Hessian at completeness is diagonal, with entries
\(-\cos(t_1/2)/(2\pi)\) and \(-\cos(t_3/2)/(2\pi)\); separate
evenness makes the internal-to-outside first derivatives zero, hence
there is no Schur correction. The factor is fixed by equation (27) of
[the free-edge proof](research_pair_free_boundary_kernel.md#7-whole-outside-period-decay-and-a-complex-strip):
\(\psi(t,u)-\psi(t,0)=-\cos(t/2)u^2/(4\pi)+O(u^4)\).
It also follows directly from the unsummed end edge:
\(b_{uu}(y,0)=-J''(1/2-y)/(2\pi^2)=-\tan(\pi y)/(2\pi)\),
with \(\tan(\pi y_*)=\cos(t/2)\). Their real parts are strictly negative.
The original polynomial has separate outside degrees at most \(N-1\).
The usual Laurent-polynomial extension away from the complete point,
combined with this local quadratic bound near it, proves the thin
quadratic strip (6). Cauchy estimates on ordinary-color circles of
radius \(N^{-2}\), also at the ramified endpoints, give all fixed
ordinary derivatives with polynomial cost. This establishes the
full-boundary conclusion without inferring off-color estimates from
complete-color jets alone.

Uniformly negative power-three chains follow by exact conjugation of
the original real trace algebra and reflection of the marked action.
Arbitrary sign changes inside the path are not covered here.

## 6. Reproduction

The cap certificate and its independent reflected-primitive replay are
new files. They leave every earlier prepared-source artifact unchanged.
The central certificate separately checks the original period root,
action, supporting planes and final Hessian face gaps. The replayers
check exact coverage and current proof/script hashes; sampled finite
levels are not used as substitutes for the all-level identities.

```sh
python3 experiments/check_three_chain_three_central_currents.py --precision 192
python3 experiments/replay_three_chain_three_central_currents.py --precision 256
python3 experiments/certify_three_chain_three_complements.py --precision 192
python3 experiments/replay_three_chain_three_complements.py --precision 256
```

The [cap author](../experiments/certify_three_chain_three_complements.py) and
[record](../repro/results/research-three-chain-three-complements.json), and
the [independent replay](../experiments/replay_three_chain_three_complements.py)
and [record](../repro/results/research-three-chain-three-complements-replay.json),
retain the nine exact rectangle covers. The author checks 8,315 leaves;
the independent reflected-primitive replay refines these to 9,059 leaves.
The central proof has its own freshly checked original three-variable
root, 28 current planes and one coherent angular-remainder plane.
