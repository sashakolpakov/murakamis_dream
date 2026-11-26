# An original-source bound on one unselected right taper

Research proof, 4 November 2026. The author outward cover, independent written/code review and a
fresh 320-bit replay have passed. Completed certificates and frozen
manuscripts are unchanged.

This proves a geometric supporting-plane bound for an original
conditional block when one unselected outer coordinate lies on the
right taper and the other unselected coordinate lies in the plateau.
The phase need not be concave along the whole path. Its positive
curvature before .45 dominates the possible later loss.
Selected aliases and two simultaneous right-taper coordinates require
separate comparisons.

## 1. Original source, phase and target

Let \(\eta,\epsilon\in\{0,1\}\) denote the left and own outer types
minus three. Use the original normalized primitive
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad
 Q_\epsilon(s;a,b)
 =g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias.
 \tag{1}
\]
The original zero-lift conditional root is denoted \(s_*(a,b)\).
Define the allocated phase
\[
 \phi_{\eta\epsilon}(a,b)=Q_\epsilon(s_*;a,b)
          -(1+\eta/2)g(a)-(1+\epsilon/2)g(b).
 \tag{2}
\]
The [transition source theorem](research_mixed_transition_conditional_rectangles.md)
and [right-guard source theorem](research_mixed_right_guard_conditional_packets.md)
provide the full original canonical packet and the unique holomorphic
root on a neighborhood of every product used below. Their common
logarithms, factorial symbols and zero lift identify the branches on
the overlap. No branch is defined by exponentiating the period alone.

Let \(z^*=(a^*,b^*)\) be the corresponding actual conditional pair
at the original critical point of any finite cyclic three/four word.
The proved geometric enclosures are
\[
 \begin{array}{ll}
 .30<\Re z_j^*<.39,\quad -.03<\Im z_j^*<.02,
                                      &\text{type three},\\
 .27<\Re z_j^*<.33,\quad -.057<\Im z_j^*<-.02,
                                      &\text{type four}.
 \end{array}
 \tag{3}
\]
Either coordinate \(j\in\{1,2\}\) may be the taper coordinate.
For \(.45\le t\le.50\), set
\[
 \chi(t)=400(.5-t)^2,\qquad
 z_j=t+i\chi(t)\Im z_j^*,\qquad
 z_{3-j}=y+i\Im z_{3-j}^*,\quad .22\le y\le.45.
 \tag{4}
\]
Both coordinates are unselected. The full complex affine plane is
\[
 \Gamma(z)=\phi(z^*)+\phi_a(z^*)(a-a^*)+\phi_b(z^*)(b-b^*).
 \tag{5}
\]

**Theorem 1.** For every reference and target above,
\[
 \Re\phi(z)\le\Re\Gamma(z)
       -\frac{\|\Re(z-z^*)\|_2^2}{121}
       <\Re\Gamma(z)-\frac1{40000}.
 \tag{6}
\]
For the literal original conditional kernel \(C_{\epsilon,N}\) and
Fourier polynomial \(d_N\), the allocated modulus therefore satisfies
\[
 |C_{\epsilon,N}(a,b)|\,
 |d_N(a)|^{\eta/2}|d_N(b)|^{\epsilon/2}
 \le \operatorname{poly}(N)
       \exp N\!\left(\Re\Gamma(a,b)-\frac1{80000}\right).
 \tag{7}
\]
Here \(d_N(a)\) abbreviates \(d_N(e^{-2\pi ia})\), with the unchanged
original convention. The polynomial loss is uniform on the displayed
compact targets, for each fixed word. Both parities are retained.
Half-moduli in (7) are bookkeeping weights; derivative assertions are
made only for the resulting holomorphic products with integer powers.

## 2. A two-piece tilted Hessian certificate

Put \(H=-\phi''\), a complex symmetric two-by-two matrix. The source
root is already holomorphic on the following independent products:
\[
 \begin{array}{c|c|c}
 &\text{moving coordinate, early}&\text{moving coordinate, late}\\ \hline
 3 &[.22,.45]+i[-.03,.02]&[.45,.50]+i[-.03,.02]\\
 4 &[.22,.45]+i[-.057,0]&[.45,.50]+i[-.057,0].
 \end{array}
 \tag{8}
\]
The other coordinate is in
\([.22,.45]+i[-.03,.02]\) for type three and
\([.22,.45]+i[-.057,-.02]\) for type four.
These are genuine independent products, not just the target graph.

For a real tilt \(\theta\), let \(D_j(\theta)\) be diagonal, equal to
one in the stationary-height coordinate and to \(1+i\theta\) in
coordinate \(j\).

**Lemma 2.** Throughout the products (8),
\[
 \begin{split}
 \Re H_{jj}&>1/100,\\
 \Re[D_j(\theta)^T H D_j(\theta)]&>\tfrac18 I
                                      &&\text{in the early product},\\
 \Re[D_j(\theta)^T H D_j(\theta)]&>-\tfrac25 I
                                      &&\text{in the late product},
 \end{split}
 \tag{9}
\]
for \(-1/5\le\theta\le3/10\) when the moving leg is type three,
and \(0\le\theta\le7/20\) when it is type four.

Here is the exact derivative and coverage content of the certificate.
With \(d=2+\epsilon\), write
\[
 \begin{split}
 q&=\pi[\cot\pi(s+a)+\cot\pi(s+b)-d\cot\pi s]
                                                   +\epsilon\pi i,\\
 v_a&=\pi\cot\pi(s+a)+\pi i,\qquad
 v_b=\pi\cot\pi(s+b)-\pi i,\\
 W_{aa}&=\pi\cot\pi(s+a)-(1+\eta/2)\pi\cot\pi a+\eta\pi i/2,\\
 W_{bb}&=\pi\cot\pi(s+b)-(1+\epsilon/2)\pi\cot\pi b
                                                   +\epsilon\pi i/2.
 \end{split}
 \tag{10}
\]
The condensed Hessian is exactly
\[
 H=-\operatorname{diag}(W_{aa},W_{bb})
             +q^{-1}(v_a,v_b)^T(v_a,v_b).
 \tag{11}
\]
Thus the chirps and both half-factorial allocations are included.

For each of the sixteen choices of types, moving coordinate and early
or late region, the checker covers all sixteen parameter-side
products. On each rational cell an affine Newton self-map encloses
the original logarithmic root. Its point test and inherited global
uniqueness fix the same branch as (1). The checker encloses (10)--(11)
and tests (9) at both tilt endpoints. A real symmetric two-by-two
matrix exceeds the stated scalar bound because both shifted diagonal
entries and its determinant are strictly positive.

These are 256 distinguished-boundary products. Their rational binary
trees cover each parameter square exactly once. At fixed real
\(\theta\) and real vector \(v\), the scalar
\(\Re(v^TD_j^THD_jv)\) is separately harmonic in \(a,b\).
Successive minimum principles therefore extend the matrix bounds
from the covered sides to each full product. The same principle
extends \(\Re H_{jj}>1/100\).
This use of the distinguished boundary comes after the independent
whole-product root theorem.

Finally, as a matrix-valued function of real \(\theta\),
\[
 \frac{d^2}{d\theta^2}
 \Re[D_j(\theta)^THD_j(\theta)]
              =-2\Re H_{jj}\,e_je_j^T\le0.
 \tag{12}
\]
Matrix concavity makes the two endpoint bounds valid at every
intermediate tilt. No sampling of the tilt is used.

## 3. Integrating across the loss of concavity

Write \(r=\Re z_j^*\), \(h=\Im z_j^*\). The straight segment from
the original reference to (4) has constant tilt
\[
 \theta=\frac{-h[1-\chi(t)]}{t-r}.
 \tag{13}
\]
The intervals in Lemma 2 contain this exact value. For completeness,
put \(d=.5-t\), \(A=.5-r\). To bound
\(|h|(1-400d^2)/(A-d)\) by \(T\), it suffices that
\[
 400|h|d^2-Td+TA-|h|>0.
 \tag{14}
\]
The unconstrained minimum is
\(TA-|h|-T^2/(1600|h|)\).
It is positive for the three worst cases
\[
 (|h|,A,T)=(.03,.11,.30),\quad
             (.02,.11,.20),\quad(.057,.17,.35).
 \tag{15}
\]
They give respectively the positive type-three, negative type-three
and positive type-four tilt bounds. At \(h=0\), the tilt is zero.
Monotonicity in \(|h|\) and \(A\) justifies these worst choices.
The code checks all three strict rational minima.

Let \(v=\Re(z-z^*)\). Along \(z(\lambda)=z^*+\lambda D_j(\theta)v\)
the other coordinate stays in its plateau product. The moving height
is between \(h\) and \(h\chi(t)\), so the appropriate products (8)
contain the whole segment. If \(t>.45\), the final part in the late
product has fractional length
\[
 q_*=\frac{t-.45}{t-r}
       \le\frac{.05}{.50-.39}=\frac5{11}.
 \tag{16}
\]
For \(t=.45\) take \(q_*=0\). Taylor's exact integral remainder and
(9) give
\[
 \begin{split}
 \Re[\phi(z)-\Gamma(z)]
 &\le-\frac{\|v\|_2^2}{2}
       \left[\frac18-\left(\frac18+\frac25\right)q_*^2\right]\\
 &\le-\frac{\|v\|_2^2}{121}.
 \end{split}
 \tag{17}
\]
The exact bracket at \(q_*=5/11\) is \(2/121\).
Moreover \(\|v\|_2\ge t-r>.45-.39=.06\), and
\[
                    \frac{(.06)^2}{121}>\frac1{40000}.
 \tag{18}
\]
This proves (6). It is the integrated comparison that is used;
pointwise concavity on the whole late product is not asserted.

## 4. Returning to the whole finite kernel

Every target in (4), and the compact products used along its path,
lies in the joined source domain of the transition and right-guard
theorems. Consequently the literal original \(C_{\epsilon,N}\)
has a uniform polynomial-times-exponential bound with rate
\(\Re[Q_\epsilon(s_*)-g(a)-g(b)]\). All its original real-row tails,
cotangent aliases and vertical currents have already been included
in that source theorem.

For an unselected type-four target, its height is nonpositive and its
real part lies in \((0,.5]\). The actual Fourier-polynomial bound gives,
for every fixed \(\delta>0\),
\[
 |d_N(e^{-2\pi iz})|
 \le \operatorname{poly}(N)
   \exp N\{\max[-\Re g(z),0]+\delta\}
 = \operatorname{poly}(N)e^{N[-\Re g(z)+\delta]}.
 \tag{19}
\]
The last equality uses \(-\Re g(z)\ge0\) on this half-strip, including
the endpoint .5 where it vanishes. The forcing term is therefore
retained even at that endpoint; no relative factorial approximation
is assumed there. The two allocated half-weights cost at most
\(\delta\) in total. Choose \(\delta<1/80000\) and combine (19)
with (6) to obtain (7).

The half-moduli themselves are not holomorphic. Fixed derivatives of
the original integer-power products follow by the original source
packet, the uniform Fourier-polynomial bound on a sufficiently small
complex neighborhood, and Cauchy's inequality, shrinking the strict
gap if necessary. This does not assert a derivative of a chosen
square root of a modulus.

For a fixed cyclic word, the original complex linear terms in (5)
cancel when all its local planes are summed, by the actual zero-lift
critical equations. Thus (7) can be combined with already proved
bounds for other block targets. The present note does not cover
adjacent simultaneous right-taper legs, selected outer aliases or
the remaining left target region, and alone makes no claim of a
full cyclic-source asymptotic.

## 5. Reproduction

    python3 experiments/certify_mixed_right_taper_tilt.py --precision 192

The author run passed 256 parameter-side products with 39,758 accepted
cells, 75,420 visits and five exact rational comparisons. The script
checks original logarithmic affine self-maps, both tilted matrix
endpoints, every binary cover, and start/end provenance immutability.
The right-guard and transition source theorems are explicit inputs;
their source acceptance checks are not duplicated here.
