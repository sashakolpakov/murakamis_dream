# The exact turn kernel in the physical middle weight

21 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

The faithful middle-weight model has an explicit triangular change of
coordinates: it is the transpose of the already known Newton crossing,
with its common scalar removed. This identifies the genuine turn with
a finite Euler kernel. Its four boundary rows and columns collapse by
finite binomial identities, including the exact rows for both original
closings.

The cyclic intertwiner itself is already present in the canonical-graph
calculation. The purpose here is to identify it with the cyclic-column
matrix of the middle-weight model and derive the resulting turn kernel
and endpoint factors. No geometric contour or volume estimate follows
from the change of coordinates alone.

## 1. The physical block and the known intertwiner

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\[
 x=-q^{-1},\qquad \kappa=q^{d^2/2},\qquad
 F_r=(Q;Q)_r,\qquad
 s_r=\prod_{j=1}^r2\sin(\pi j/N),\qquad F_0=s_0=1.
\]
Write
\[
 (z;Q)_m=\prod_{j=0}^{m-1}(1-zQ^j),\qquad
 \nu_r=(-1)^rQ^{r(r+1)/2},\qquad
 {r\brack a}_Q=\frac{F_r}{F_aF_{r-a}}\quad(0\le a\le r<N).
\]
All these factorial denominators are nonzero. The physical middle space
has the ordered basis
\[
 v_a=|a,d-a\rangle,\qquad 0\le a\le d.
\]
Let \(A=\Omega_d\) be its original pair Casimir. The actual balanced
single-head generators and coproduct are
\[
 E|a\rangle=(Q^{-a}-1)|a-1\rangle,\quad
 F|a\rangle=(1-Q^{a+1})|a+1\rangle,\quad
 K|a\rangle=xQ^{-a}|a\rangle,
\]
\[
 E_t=E_1K_2+E_2,\qquad F_t=F_1+K_1^{-1}F_2,\qquad
 K_t=K_1K_2,\qquad
 \Omega=F_tE_t+qK_t+q^{-1}K_t^{-1}.
 \tag{1}
\]
Missing endpoint arrows are zero. On the middle weight \(K_t=1\).
Expanding (1) gives the symmetric tridiagonal matrix
\[
 A_{a+1,a}=A_{a,a+1}=-(1-Q^{a+1})^2,
\]
\[
 A_{aa}=c_0-q(1-Q^a)^2-q^{-1}(1-Q^{a+1})^2
        =4qQ^a-q(1+Q)Q^{2a},\qquad c_0=q+q^{-1}.
 \tag{2}
\]
For example, the two return paths in \(F_tE_t\) contribute
\(xQ(1-Q^a)^2=-q(1-Q^a)^2\) and
\(x^{-1}Q^{-1}(1-Q^{a+1})^2=-q^{-1}(1-Q^{a+1})^2\).
The two adjacent paths give the first formula in (2). Thus this is
the physical Casimir of the middle-weight model, in the same
coordinates as the existing canonical-graph identity.

Put
\[
 c_r=q^{2r+1}+q^{-2r-1},\qquad
 b_r(z)=s_r^{-2}\prod_{j=0}^{r-1}(c_j-z).
\]
The full boundary algebra is \(H_N=\mathbb C[z]/(2T_N(z/2)+2)\),
where \(T_N\) is the Chebyshev polynomial of the first kind. It
includes every first derivative at its double roots. Its cyclic-column
matrix and Newton multiplication matrix are
\[
 C=[b_0(A)v_0\ \cdots\ b_d(A)v_0],\qquad
 Z_{\rm Newt}e_r=c_re_r-s_{r+1}^2e_{r+1},
 \tag{3}
\]
with the last raised term zero. Here \(e_r\) denotes a standard
coordinate vector; the columns of \(C\) are written in the physical
basis \(v_a\).

**Proposition 1.** The cyclic-column matrix is
\[
 \boxed{\quad
 C_{ar}=\nu_a(-q)^{r-a}{r\brack a}_Q
       =(-1)^rq^{r(a+1)}\frac{s_r}{s_as_{r-a}}
       \quad(0\le a\le r\le d),
 \quad}
 \tag{4}
\]
and is zero for \(a>r\). Consequently
\[
 C=\kappa^{-1}T_1^{\mathsf T},\qquad
 C^{-1}=\overline C,\qquad C_{dd}=1,
 \tag{5}
\]
where \(T_1\) is the original Newton crossing matrix, including
its scalar \(\kappa\).

**Proof.** The symmetric physical block (2) and the full intertwiner
\[
 A\,T_1^{\mathsf T}=T_1^{\mathsf T}Z_{\rm Newt}
 \tag{6}
\]
are the existing canonical-graph identity, Section 4. We check the
coordinate identification and endpoints explicitly. The proposed
matrix in (4) has \(Ce_0=v_0\). Its three interior entry ratios are
\[
 \frac{C_{a-1,r}}{C_{ar}}
   =qQ^{-a}\frac{1-Q^a}{1-Q^{r-a+1}},\qquad
 \frac{C_{a+1,r}}{C_{ar}}
   =qQ^a\frac{1-Q^{r-a}}{1-Q^{a+1}},
\]
\[
 \frac{C_{a,r+1}}{C_{ar}}
   =-q\frac{1-Q^{r+1}}{1-Q^{r-a+1}}.
 \tag{7}
\]
These follow directly by canceling factorials. For an entry
\(0\le a\le r\), clear the denominators in
\(AC=CZ_{\rm Newt}\). Writing \(u=Q^a\), \(t=Q^{r-a+1}\),
and dividing by \(q\) leaves
\[
 \begin{split}
 0={}&[4u-(1+Q)u^2-Q^{-1}ut-(ut)^{-1}](1-t)\\
 &-u^{-1}(1-u)^3
   -u(1-Qu)(1-t/Q)(1-t)
   +(ut)^{-1}(1-ut)^3.
 \end{split}
 \tag{8}
\]
Indeed the second and last terms together are
\[
 (1-t)[(ut)^{-1}-3u+u^2(1+t)],
\]
after which (8) factors to zero. Zero off-diagonal coefficients
retain this verification at \(a=0\), at \(a=r\), and at \(r=d\),
except for the one cleared zero denominator \(a=0,r=d\).
At that corner \(C_{1d}/C_{0d}=x\), and
\[
                 A_{00}-x(1-Q)^2=c_0=c_d,
\]
which is the required entry. For \(a=r+1\), equality reduces to
\(\nu_{r+1}=-Q^{r+1}\nu_r\); entries with \(a>r+1\) vanish
on both sides. This proves (6) without deleting any endpoint.

The true cyclic-column matrix in (3) also intertwines \(A\) and
\(Z_{\rm Newt}\), and has first column \(v_0\). The Newton recurrence
determines all successive columns, because \(s_{r+1}\ne0\) for
\(r<d\). Thus (4) is exactly (3).

The alternative expression in (4) uses
\({r\brack a}_Q=q^{a(r-a)}s_r/(s_as_{r-a})\). It identifies
the transpose of the known Newton crossing, as stated in (5).
The finite Pascal inverse is
\[
 (C^{-1})_{ar}
  =\nu_r^{-1}q^{r-a}Q^{(r-a)(r-a-1)/2}{r\brack a}_Q.
 \tag{9}
\]
Multiplication verifies (9) by the finite binomial identity
\(\sum_{h=0}^{m}(-1)^hQ^{h(h-1)/2}{m\brack h}_Q
 =(1;Q)_m\), which is zero for \(1\le m<N\).
Using \(\overline{{r\brack a}_Q}
 =Q^{-a(r-a)}{r\brack a}_Q\), (9) equals \(\overline C\).
Finally \(\nu_d=1\), proving \(C_{dd}=1\). \(\square\)

## 2. Exact closings and a finite Euler form

For a whole Hopf box \(f(A)\), put \(y=f(A)v_0=C\alpha\),
where \(\alpha\) is its complete Newton coefficient vector.
The original marked cap and Frobenius closing are particularly simple:
\[
 \boxed{\quad
 m^{\rm pkt}(y)=\sum_{a=0}^d x^ay_a,\qquad
 \phi^{\rm pkt}(y)=y_d.
 \quad}
 \tag{10}
\]
For the first identity, multiply (4) by \(x^a=(-q)^{-a}\)
and sum in \(a\). The \(r\)-th result is
\[
 (-q)^r\sum_{a=0}^r(-1)^aQ^{a(a-1)/2}{r\brack a}_Q
                  =\mathbf1_{r=0}.
\]
Thus \((x^a)_aC=e_0^{\mathsf T}\). The second identity follows
from triangularity and \(C_{dd}=1\):
\(e_d^{\mathsf T}C^{-1}=e_d^{\mathsf T}\).
These are exactly the two reconstructed original rows. Every recorded
external framing or normalization line remains unchanged.

Let \(P_{\rm rev}v_a=v_{d-a}\). The genuine packet turn is
\[
                         \mathcal J=C P_{\rm rev}C^{-1}.
 \tag{11}
\]
There is an explicit finite Euler realization of (11), rather than
an unspecified change of frame. Define the strict weighted shift
\[
 \mathsf Lv_r=(1-Q^r)v_{r-1},\qquad \mathsf Lv_0=0,
\]
\[
 V_Q(B)=\sum_{h=0}^d\frac{B^h}{F_h},\qquad
 P_Q(B)=\sum_{h=0}^d
             \frac{(-1)^hQ^{h(h-1)/2}B^h}{F_h}.
\]
For \(B^N=0\), these two polynomials are inverses. Formula (4) gives
\[
 C=D_\nu V_Q(-q\mathsf L),\qquad
 \boxed{\quad
 \mathcal J=D_\nu V_Q(-q\mathsf L)\,
       P_{\rm rev}\,P_Q(-q\mathsf L)D_\nu^{-1}.
 \quad}
 \tag{12}
\]
Here \(D_\nu=\operatorname{diag}(\nu_a)\); no endpoint phase is
dropped. If a strict unit shift is preferred, set
\(\mathsf Sv_r=v_{r-1}\) for \(r\ge1\), \(\mathsf Sv_0=0\),
and \(D_F=\operatorname{diag}(F_r)\).
Then \(\mathsf L=D_F^{-1}\mathsf SD_F\). These factorial frames
must remain in the corresponding Euler coefficient periods.

## 3. A single finite kernel for the turn

**Proposition 2.** Every entry of the physical middle turn is
\[
 \boxed{\quad
 \mathcal J_{ab}=(-q)^{d-a-b}
 \sum_{t=0}^{\min(d-a,b)}
 (-1)^tQ^{t(t-1)/2-(a+b)t}
             {a+t\brack a}_Q{b\brack t}_Q .
 \quad}
 \tag{13}
\]

**Proof.** In the product \(CP_{\rm rev}\overline C\), set
\(t=d-r\), where \(r\) is the column index of the first factor.
Its range is exactly \(0\le t\le\min(d-a,b)\). Use
\[
 {d-t\brack a}_Q
       =\nu_a^{-1}Q^{-at}{a+t\brack a}_Q,
 \tag{14}
\]
which follows by reflecting the \(a\) numerator factors through
\(Q^N=1\). Also
\(\overline{{b\brack t}_Q}=Q^{-t(b-t)}{b\brack t}_Q\).
The remaining phase in the summand is
\[
 (-q)^{d-a-b}\nu_t^{-1}Q^{-at-t(b-t)}
 =(-q)^{d-a-b}(-1)^t
                        Q^{t(t-1)/2-(a+b)t}.
\]
This proves (13). Every factorial index is below \(N\); the formula
is a finite sum, not a specialization of an infinite summation.
\(\square\)

## 4. All four endpoint collapses

The finite kernel has exact endpoint values
\[
 \boxed{\begin{aligned}
 \mathcal J_{a0}&=(-q)^{d-a},&
 \mathcal J_{db}&=(-q)^{-b},\\
 \mathcal J_{ad}&=(-q)^{-a}F_{d-a},&
 \mathcal J_{0b}&=(-q)^{d-b}\nu_b^{-1}F_b .
 \end{aligned}}
 \tag{15}
\]
The first two have just the \(t=0\) term in (13). At \(a=0\),
the finite binomial theorem gives
\[
 \sum_{t=0}^b(-1)^tQ^{t(t-1)/2-bt}{b\brack t}_Q
             =(Q^{-b};Q)_b=\nu_b^{-1}F_b.
\]
For \(b=d\), first use \({d\brack t}_Q=\nu_t^{-1}\);
the remaining sum is
\(\sum_{t=0}^{d-a}Q^{-at}{a+t\brack a}_Q\).
Put \(m=d-a\). Reflection gives
\[
 {a+t\brack a}_Q
      =(-1)^tQ^{-mt+t(t-1)/2}{m\brack t}_Q.
\]
Because \(a+m=d\), the sum becomes
\[
 \sum_{t=0}^{m}(-1)^tQ^{t(t+1)/2}{m\brack t}_Q
                        =(Q;Q)_m=F_m.
\]
This proves the last two identities without an infinite-series
argument or a missing endpoint.

In particular the output-index-\(d\) row in (15)
is exactly the marked-cap row in (10), as required by
\(\phi^{\rm pkt}\mathcal J=m^{\rm pkt}\).
One factual norm consequence in the physical Euclidean basis is
\[
 \|\mathcal Je_0\|^2=\|e_d^{\mathsf T}\mathcal J\|^2=N,\qquad
 \|\mathcal Je_d\|^2=\|e_0^{\mathsf T}\mathcal J\|^2
                         =\sum_{r=0}^d|F_r|^2.
 \tag{16}
\]
Thus the physical kernel contains the full sine-factorial weights;
it is not a flat Fourier matrix. Equation (16) is not a bound for a
whole knot or for a received geometric packet.

## 5. The correctly transported boundary metric

The physical coordinates have a specified full positive Gram matrix:
\[
 G_{\mathcal M}=(C^{-1})^*C^{-1}=C^{\mathsf T}\overline C,
 \qquad \|y\|_{G_{\mathcal M}}=\|C^{-1}y\|_2.
 \tag{17}
\]
It is the original Euclidean Newton metric expressed on the middle
weight. Consequently
\[
 \mathcal J^*G_{\mathcal M}\mathcal J=G_{\mathcal M}.
 \tag{18}
\]
Both source rows in (10) have exactly unit dual norm for this metric:
their products with \(C\) are \(e_0^{\mathsf T}\) and
\(e_d^{\mathsf T}\). These statements follow by direct substitution
in (11) and (17); no unknown closed period defines the Gram.
There is no assertion that this Gram is diagonal or has polynomial
condition number in the flat physical coordinates.

If every packet, gate and root row is transported by \(C\), using
\(G_{\mathcal M}\) and its tensor-product metric, this is an isometric
change of the original Newton problem. In particular, if \(M\) denotes
the bilinear Newton product, its transported map is
\(C M(C^{-1}\otimes C^{-1})\), and a source row becomes
\(\ell C^{-1}\). Their Hilbert--Schmidt norms, normalization budgets,
residual energy and exact minimized value are unchanged when measured
in the transported metrics. The positive energy is therefore the
previous Newton energy in different coordinates, not a new growth
estimate. The flat-coordinate factorial norms in (16) cannot be added
as new source or volume contributions.

## 6. The remaining analytic duty

The packet model is faithful to all repeated-root normals. The turn
in (11)--(15) is the actual fixed-root turn, and (10) retains both
original source rows. Its Newton version is unitary reversal; its
physical version includes the explicit Euler and factorial frames.
No bound for their changes of norm is inferred from that reversal.

The previously proved modular relation already reduces redundant
twist/turn words. The regular-bend calculation already specifies the
actual parameter-dependent cups and caps. Neither should be replaced
by a new convention here. In particular, differentiating a generic
quantum parameter requires its actual bend family; these fixed-root
formulas alone do not give such derivatives.

What remains for the geometric application is to transport the
complete marked contour through (12) or (13), including the strict
shift endpoints and factorial frames, and prove the required estimate
for the resulting actual packet and prescribed closing. An isolated
endpoint norm or the finite sum does not prove that the selected
geometric contribution survives an arbitrary short component.

Individual non-Hopf face factors still act as full middle-block
matrices, in their original order. Only a whole Hopf box is identified
with its polynomial packet. The source rows in (10) are not an
extension of the all-array averaged physical trace to arbitrary
inserted matrices.

The turn studied here acts on cyclic middle-weight packets. A
recoupling matrix in a highest-weight multiplicity frame is a different
typed operator until its boundary and source adapters have been supplied.

## Complete proof sources and coverage

All three complete proof texts were read at matching pins. The physical
intertwiner is existing work; the finite turn kernel and endpoint
calculations are derived above.

| Source | SHA-256 |
|---|---|
| [Faithful middle-weight model](research_conway_middle_weight_face_model.md) | 1813a5ec78bda1df746e53227bc3d9e36c4b3d230bd648a10537a387db87ebac |
| [Original full Newton crossing and source](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| [Existing physical cyclic intertwiner](actual_newton_twist_canonical_graph.md) | 387681510416839fd3407f730ab701c7c1c8855b73da66497756721234d4f6d9 |

The complete [coherent turn reduction](actual_newton_coherent_turn_reduction.md)
and [regular-bend comparison](research_rivin_jones_regular_bends_and_newton_turn.md)
were also read for coverage. Their modular and parameter-family
statements are not new assertions of this note.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or edit to a previous final was performed.
