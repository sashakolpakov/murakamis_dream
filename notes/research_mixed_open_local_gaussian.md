# A nonzero local Gaussian for every open word in three and four

Research corollary, 5 November 2026. The reduced-disk conditional
source closes the finite local-factor gaps in the earlier coverage
audit. This is a theorem about the unaliased local contribution of
the original one-cap representation. It does not estimate its full
outgoing contour.

## 1. Every original local factor is covered

Fix any finite word \((3+\epsilon_1,\ldots,3+\epsilon_m)\),
\(m\ge1\), and put \(k=\sum_j\epsilon_j\). Use the original
open critical point and the exact one-cap finite source of
[the local coverage audit](research_mixed_open_local_factor_coverage.md),
equation (1). Its scalar is \(\kappa_N^{m+k}N^{m+k}\).
Every \(d_N\) is the actual Fourier polynomial, and every factor
\(1+X_j^{-N}\) remains in this exact representation.

**Lemma 1.** Every factor of its unaliased term has a holomorphic,
nonzero local source packet at the original critical point, with
both ordinary colors near \((-2,-2)\), for both level parities.

*Proof.* The coverage audit supplies the first cap \(U_{\epsilon_1,N}\),
the last ordinary endpoint factor \(H_N\), the terminal conditional
factor \(C_{\epsilon_m,N}\) when \(m\ge2\), and all exact
diagonal weights. It also proves that every nonprivate leg is strictly
inside the disk of its own type,
\[
 P_3=\{|z-(.35-.01i)|\le.083\},\qquad
 P_4=\{|z-(.30-.052i)|\le.060\}.                       \tag{1}
\]
This uses the ordinary block image theorem and all 5,258 retained
endpoint witnesses, without repeating the open word periodically.

Consider any ordinary vertex \(2\le j\le m-1\). Its two
external legs are \(a=t_{j-1}\) and \(b=s_{j+1}\), both
nonprivate, including at \(j=2\) or \(j=m-1\). They lie in
(1). The original critical equations and their unique block branch
identify its inner legs with \((s(a,b),t(a,b))=(s_j,t_j)\).
The [reduced-disk source theorem](research_mixed_reduced_disk_conditional_packets.md)
therefore supplies the literal complete factor
\(C_{\epsilon_j,N}(t_{j-1},t_j)\), including every finite row.
Its ambient neighborhood follows from the nonzero derivative of
\((a,b)\mapsto(a,t(a,b))\), as proved there and in the coverage
audit. Thus it supplies independent nearby source variables, not
only values on a stationary image. The six type families and their
two orientations include all ordered external types.

There are no ordinary vertices when \(m=1,2\); their endpoint
factors were already covered. For each fixed word, intersect the
finitely many source neighborhoods and the ordinary-color critical
germ from the open Hessian theorem. Their original nonzero symbols
and branches agree on overlaps by uniqueness. This proves the lemma.
\(\square\)

The conditions on the five possible boundary-buffer factors in the
earlier audit are consequently discharged for every word. That
audit and its records remain unchanged; the new input is the
complete reduced-disk source, not a bound extrapolated from a
larger rectangle.

## 2. Exact local normalization

Let \(\mathcal F_m(y,t;w_L,w_R)\) be the original full action
from [the open Hessian theorem](research_mixed_open_word_hessian.md),
with
\[
 y=(s_1,\ldots,s_m,u_L,u_R),\qquad
 t=(t_1,\ldots,t_m).
                                                               \tag{2}
\]
There are \(m+2\) eliminated and \(m\) retained variables,
including \(m=1\). Write
\(\Phi_m(t)=\mathcal F_m(y(t),t)\),
\(H=-\mathcal F_m''\), and
\[
 H_{\mathrm{eff}}=-\Phi_m''
   =H_{tt}-H_{ty}H_{yy}^{-1}H_{yt},\qquad
 \det H=\det H_{yy}\det H_{\mathrm{eff}}.                \tag{3}
\]
The established complex Schur argument gives
\(\Re H_{\mathrm{eff}}\succ(6\pi/49)I\) at the undeformed
ordinary colors. Nondegeneracy and the source neighborhoods persist
for nearby ordinary colors.

**Theorem 2.** For every fixed finite word, the term obtained by
choosing \(1\) from each \(1+X_j^{-N}\), integrated over a
sufficiently small fixed local horizontal box through the original
critical point, has asymptotic
\[
 \kappa_N^{m+k}N^{-3/2}\,
 \frac{(2\pi)^{m/2}b_m(t^*)}
      {\sqrt{\det H_{\mathrm{eff}}(t^*)}}
 e^{N\mathcal F_m(z^*)}(1+O(N^{-1})),                    \tag{4}
\]
with nonzero coefficient and the original Gaussian branch. The
phase and coefficient have holomorphic ordinary-color germs near
\((-2,-2)\); equivalently one may transport the local contour
inside its source neighborhood when the colors move. Both level
parities and all fixed asymptotic orders are retained.

Here \(b_m\) is exactly the product of the first-cap symbol,
the terminal ordinary symbol, all bare conditional symbols and
\(a_0(t_j)^{-\epsilon_j}\), as defined in equation (11) of the
coverage audit. Its phase identity is the original one:
the sum of the \(U,C,H,d_N\) phases equals \(\Phi_m\),
including all endpoint chirps and own factorial terms. There is no
new additive calibration constant.

*Proof.* Lemma 1 removes the only conditional hypothesis from
Section 4 of the coverage audit. Its Gaussian and normalization
calculation now applies to every word. Explicitly the powers before
the outer Gaussian are
\[
 (m+k)-1-\epsilon_1/2
 -\frac{m-1+k-\epsilon_1}{2}-1-k/2=(m-3)/2;
 \qquad (m-3)/2-m/2=-3/2.                               \tag{5}
\]
All factors in \(b_m\) are nonzero by their literal source
theorems; (3) makes the remaining determinant nonzero. Strict
horizontal concavity gives the stated local stationary-phase
expansion. The proof applies without a cyclic incidence convention
at \(m=1,2\). \(\square\)

For ordinary derivative orders \(a,b\), the local leading power is
\(N^{a+b-3/2}\). Its additional phase factors are
\[
 \left(-\frac{\tan\pi u_L}{4\pi}\right)^a
 \left(-\frac{\tan\pi u_R}{4\pi}\right)^b,              \tag{6}
\]
which are nonzero; signed jets retain the signs in the original
torus identity. This is a germ statement for each fixed word and
fixed derivative orders, with no word-length-uniform error claimed.

## 3. What is still separate

Selecting one term from the wrapped factors does not remove the
other selected Fourier integrals from the exact source. This theorem
does not control those terms or the rest of the outgoing integration
contour, and does not rule out a competing contribution to the full
sum. The required whole ordinary-boundary strips, the marked
action-to-volume identification, and stability for arbitrary short
partial fillings also remain separate. In particular no new knot
family or finite-exclusion theorem follows from the local statement
alone.

The focused assembly checker binds the completed coverage and
reduced-disk author/replay pairs, checks their exact common domains
and complete six-family coverage, and rechecks the normalization
identities. It proposes no roots and reruns no numerical cover.

```sh
python3 experiments/check_mixed_open_local_gaussian.py
python3 experiments/check_mixed_open_local_gaussian.py --input repro/results/research-mixed-open-local-gaussian.json --output repro/results/research-mixed-open-local-gaussian-replay.json
```
