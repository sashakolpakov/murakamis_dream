# Local factor coverage in the original one-cap open source

Research deduction, 5 November 2026. The two endpoint factors, terminal
conditional factor and exact diagonal weights now have their required
local packets at every original open critical point. The remaining
unproved local inputs are at most five ordinary conditional factors
near the two ends. This note identifies them, extracts smaller common
attached disks from the existing witnesses, and records the local
Gaussian consequence whenever those factor inputs are available.
It does not assert whole-source dominance.

## 1. Exact factors and the common smaller disks

For a fixed word \(3+\epsilon_1,\ldots,3+\epsilon_m\), put
\(k=\sum\epsilon_j\). Retain the exact one-cap integrand
\[
 U_{\epsilon_1,N}(w_L,X_1)
 \prod_{j=2}^m C_{\epsilon_j,N}(X_{j-1},X_j)
 H_N(w_R,X_m^{-1})
 \prod_{j=1}^m d_N(X_j)^{\epsilon_j}(1+X_j^{-N})^{\epsilon_j},
 \qquad X_j=e^{-2\pi it_j},                              \tag{1}
\]
with scalar \(\kappa_N^{m+k}N^{m+k}\), from
[the original torus composition](research_mixed_conditional_torus_composition.md).
The private endpoint legs are \(s_1,t_m\); the conditional row
at vertex \(j\ge2\) is \(s_j\).

Define
\[
 D'_3=\{|z-(.35-.01i)|\le.083\},\qquad
 D'_4=\{|z-(.30-.052i)|\le.060\}.                         \tag{2}
\]
Every **nonprivate** leg of the actual open critical point lies
strictly in its corresponding disk (2). For ordinary vertices
\(2\le j\le m-1\), this is the full one-block image estimate
in Proposition 1 of
[the critical-domain theorem](research_mixed_cyclic_critical_height_bounds.md).
Its proof bounds the whole original bidisk map, so its use here
does not repeat an open word periodically.

For the two attached endpoint legs, the new assertion is an exact
extraction from the
[existing endpoint maps](research_mixed_open_word_critical_localization.md).
On every one of their 5,258 retained witnesses, let \(c\) be the
attached center and \(r\) the complex disk radius. The focused
checker verifies, with rational arithmetic,
\[
 0<r<R_\epsilon,\qquad
 |c-c_\epsilon|^2<(R_\epsilon-r)^2,
 \quad (R_0,R_1)=(.083,.060).                            \tag{3}
\]
This covers all 3,347 type-three and 1,911 type-four endpoint disks,
with both possible external types. It reuses the complete validated
root trees; there is no new root proposal or parameter cover.
The private legs are not included in (2).

## 2. What is already a complete local finite source

The following statements concern neighborhoods of the actual finite
factors, not just the existence of their critical points.

* The [complete first-cap packet](research_mixed_complete_first_cap_packet.md)
  supplies \(U_{\epsilon_1,N}\), including all its private rows and
  whole ordinary color, near the actual attached image \(t_1\).
  It includes the separate one-vertex outgoing point.
* At the right private leg, the exact identity
  \(H_N(w,e^{2\pi ie})=G_N(Ne)\mathcal C_N(e,w)\), with the
  original sine factorial \(G_N\), and the
  [endpoint rectangle packet](research_mixed_endpoint_cap_rectangle.md)
  give
  \[
   H_N(w,e^{2\pi ie})=
   N^{-1}\sqrt{2\sin\pi e}\,\mathcal A(e,w)
      e^{N[J(e)+S(e,w)]}(1+O(N^{-1})).                   \tag{4}
  \]
  The coefficient is nonzero on the actual private image.
* For \(m\ge2\), the
  [terminal conditional packet](research_mixed_terminal_conditional_packet.md)
  supplies \(C_{\epsilon_m,N}(t_{m-1},t_m)\) on an ambient
  neighborhood of the four actual endpoint graphs. No such factor
  occurs when \(m=1\).
* Every four-weighted nonprivate \(t_j\) is in the original
  \(D_4\), while the private type-four leg satisfies
  \(t_m\in(.333,.363)+i(-.051,-.019)\). Both are contained in
  the rectangle \([.236,.364]+i[-.116,.012]\) of
  [the exact Fourier-weight theorem](research_mixed_fourier_weight_continuation.md),
  Corollary 2. Hence the **actual polynomial** satisfies locally
  \[
   d_N(e^{-2\pi it})=
   N^{-1/2}a_0(t)^{-1}e^{-Ng(t)}(1+O(N^{-1})),\qquad
   a_0(t)=\sqrt{2\sin\pi t}\,e^{-i\pi t/2}.             \tag{5}
  \]
  Its difference from the original inverse factorial is exponentially
  small. This does not delete the separate factor \(1+X^{-N}\).

All these inputs also cover the one-vertex normalization. In that case
(1) contains only \(U\), \(H\), and the prescribed diagonal weight.

## 3. An exact test for the remaining ordinary factors

For \(2\le j\le m-1\), there are two already proved routes.
Define the index predicates
\[
\begin{split}
 B(i)&:\quad \epsilon_i=0\quad\text{or}\quad 4\le i\le m-3,\\
 R(i)&:\quad
 [\epsilon_i=0\ \text{and}\ 3\le i\le m-2]
 \quad\text{or}\quad
 [\epsilon_i=1\ \text{and}\ 4\le i\le m-3].
\end{split}                                                   \tag{6}
\]
The following are sufficient coverage tests:
\[
 \boxed{\quad
 [B(j-1)\ \text{and}\ B(j+1)]
 \quad\text{or}\quad
 [R(j-1)\ \text{and}\ R(j)].\quad}                    \tag{7}
\]

For the first alternative, the ordinary two-leg map at vertex \(j\)
has external legs \(a=t_{j-1}\), \(b=s_{j+1}\). Every type-three
external leg is in \(D'_3\), by Section 1. A type-four external
vertex in \([4,m-3]\) has both legs in
\(P_4=(.27,.33)+i(-.057,-.001)\), by the existing five-window
theorem and [open-window inheritance](research_mixed_open_word_window_inheritance.md).
Thus the full
[correlated conditional-image packet](research_mixed_conditional_critical_images.md)
applies, with its own type arbitrary.

This composed packet gives an ambient kernel germ. In fact, for the
two-by-two original block Jacobian \(J_b\), the implicit response is
\[
 t_b=-\frac{(J_b)_{ss}}{\det J_b}
             \{\pi\cot\pi(t+b)+i\pi\}\ne0.             \tag{8}
\]
The determinant is nonzero by the block accretivity theorem;
\(-\Re(J_b)_{ss}>1/8\) by the conditional contour lemma; and
\(\cot z+i\) has no finite zero in the regular strip.
Consequently \((a,b)\mapsto(a,t(a,b))\) is locally invertible.
The composed source neighborhood is therefore a genuine neighborhood
of the two independent arguments of \(C_j\). This step does not
infer transverse source control from a one-dimensional image alone.

For the second alternative in (7), both actual parameters
\(t_{j-1},t_j\) are in the independent central source rectangles:
type-three legs in \((.30,.39)+i(-.03,.02)\), type-four legs in
\(P_4\). The
[central conditional theorem](research_mixed_central_conditional_rectangles.md)
then supplies the packet directly, with strict room in its real
interval \([.25,.40]\).

In particular all factors with \(5\le j\le m-3\) are covered
uniformly in the word. The only possible unresolved ordinary factors
are
\[
 j\in\{2,3,4,m-2,m-1\}\cap\{2,\ldots,m-1\},           \tag{9}
\]
and (7) often removes some of these as well. There are no ordinary
factors for \(m=1,2\). These are sufficient tests, not claims
that a factor outside them fails. A general packet for ordinary
block images over \(D'_3,D'_4\) would remove all of (9) without
enumerating open words. The older full-disk revived-row obstruction
does not apply to these smaller disks; nor does that exclusion itself
prove the needed packet.

## 4. The resulting local Gaussian, when every factor is covered

Suppose each ordinary index satisfies (7), or its original conditional
packet is otherwise independently established near the actual point.
Select the term of (1) with no \(X_j^{-N}\) factors. For a small
fixed real box about \(\Re(t_1^*,\ldots,t_m^*)\), at the critical
heights, its integral has a nonzero Gaussian contribution.

To state its normalization, eliminate
\(y=(s_1,\ldots,s_m,u_L,u_R)\) from the original full action
\(\mathcal F_m(y,t)\) in
[the open Hessian theorem](research_mixed_open_word_hessian.md),
and write \(\Phi_m(t)=\mathcal F_m(y(t),t)\). There are
\(m+2\) eliminated and \(m\) retained coordinates, also for
\(m=1\). With \(H=-\mathcal F_m''\),
\[
 H_{\rm eff}=-\Phi_m''=H_{tt}-H_{ty}H_{yy}^{-1}H_{yt},
 \qquad \det H=\det H_{yy}\det H_{\rm eff}.              \tag{10}
\]
The original bound \(\Re H\succ(6\pi/49)I\) implies
\(\Re H_{\rm eff}\succ(6\pi/49)I\) by the complex Schur
identity. Thus the horizontal local maximum is strict and both
determinants are nonzero, with their original Gaussian branches.

Let \(B_U\) be the first-cap coefficient, \(B_{C,j}\) the bare
conditional coefficient after division by both marked factorials,
and \(B_H\) the coefficient in (4). Put
\[
 b_m(t)=B_U(t_1)B_H(t_m)
          \prod_{j=2}^m B_{C,j}(t_{j-1},t_j)
          \prod_j a_0(t_j)^{-\epsilon_j}.                \tag{11}
\]
Every factor is nonzero. Direct addition of the original phases in
(1) gives exactly \(\Phi_m\), including the endpoint chirps and
the full own factorial terms. The powers before the outer Gaussian are
\[
 m+k-1-\epsilon_1/2
 -\frac{m-1+k-\epsilon_1}{2}-1-k/2=(m-3)/2.             \tag{12}
\]
The \(m\)-variable Gaussian therefore gives
\[
 \kappa_N^{m+k}N^{-3/2}
 \frac{(2\pi)^{m/2}b_m(t^*)}{\sqrt{\det H_{\rm eff}(t^*)}}
 e^{N\mathcal F_m(z^*)}(1+O(N^{-1})).                   \tag{13}
\]
The coefficient and phase continue holomorphically in the two ordinary
colors near \((-2,-2)\). At the critical point their phase derivatives
are \(-\tan(\pi u_L)/(4\pi)\) and
\(-\tan(\pi u_R)/(4\pi)\), both nonzero. Fixed ordinary derivative
orders \(a,b\) therefore give power \(N^{a+b-3/2}\) and the
corresponding nonzero product of these two factors. Signed jets have
the signs prescribed by the exact torus identity.

This proves a local contribution, not the full integral. The selected
Fourier terms in (1), the remaining outgoing angular domain, possible
competing currents, whole ordinary boundary strips, and the marked
geometric identification still need their respective arguments.
In particular (13) is not yet available for every mixed open word
from the current factor list alone, and it proves no new knot family
or arbitrary short-filling theorem.

## 5. Reproduction

The focused checker extracts (3) from all existing endpoint witnesses,
binds the source inputs, and verifies the exact phase/power algebra.
It does not rerun a root or source cover.

```sh
python3 experiments/check_mixed_open_local_factor_coverage.py
python3 experiments/check_mixed_open_local_factor_coverage.py --input repro/results/research-mixed-open-local-factor-coverage.json --output repro/results/research-mixed-open-local-factor-coverage-replay.json
```
