# A calibrated first-collar comparison for a four-three prefix

Research deduction, 5 November 2026. The first-collar comparison extends
to every actual open word beginning \((4,3)\). The full first Fourier
weight is retained. The new analytic input is an asymmetric domain for
the quadratic conditional root; it avoids applying the earlier
half-cotangent hypothesis to a type-four endpoint outside that domain.
No new root search or parameter cover is used.

## 1. The actual pair and its weight

Let the word have length at least two. Write its first two retained
references as \(r_1=a+ih,r_2=b+ic\). The
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give
\[
 .246<a<.350,\qquad -.108<h<-.020.
 \tag{1}
\]
For the second coordinate one may use
\[
 .267<b<.438,\qquad -.065<c<.068.
 \tag{2}
\]
For length two this is the private right type-three rectangle
\((.376,.438)+i(-.019,.037)\). Otherwise the second vertex is
ordinary. Proposition 1 of the
[universal block-image theorem](research_mixed_cyclic_critical_height_bounds.md)
bounds the whole typed input bidisk, so its type-three disk and height
bounds apply to this actual open block. This gives (2), without
periodically repeating the open word.

Let \(\mathcal T_1\) be the original complete first-cap phase and
\(\phi_{00}\) the type-three conditional phase with no halfweights.
Define
\[
 \Phi_{43}(r_1,r_2)=
       \mathcal T_1(r_1,-2)+\phi_{00}(r_1,r_2)-g(r_1),
 \quad M_{43}=\Re\Phi_{43},\quad
 P=\partial_2\phi_{00}(r_1,r_2).
 \tag{3}
\]
This is also
\((\mathcal T_1-g(r_1)/2)+\phi_{10}\).
The two descriptions allocate the same full first weight.
The actual original critical equation is
\[
 \mathcal T_1'(r_1,-2)+\partial_1\phi_{00}(r_1,r_2)
                          -g'(r_1)=0.
 \tag{4}
\]
Consequently the supporting plane of this pair is
\[
                        M_{43}+\Re[P(z_2-r_2)].
 \tag{5}
\]
The second tangent remains present.

The literal source to be bounded, for either first selection
\(\sigma\in\{0,1\}\), is
\[
 U_{1,N}(w,X)\,C_{0,N}(X,e^{-2\pi iz_2})\,
                        d_N(X)X^{-N\sigma},
 \quad X=e^{-2\pi ix},\quad 0\le x\le\rho,
 \quad z_2=b+ik,\quad
 k\in[\min(0,c),\max(0,c)].
 \tag{6}
\]
The first target is real, so its selected monomial has unit modulus.
The second vertex is type three and has no Fourier weight or selection.
The interval in (6) includes all its physical attenuation beside this
collar.

## 2. A wider domain for the quadratic root

**Lemma 1.** Let \(P_0=p+i\alpha,Q_0=q+i\beta\), where
\[
 p,q>0,\qquad 0\le\alpha\le A,\quad |\beta|\le B,\qquad
 A+B+\frac{(A-B)^2}{4}<1.
 \tag{7}
\]
The quadratic
\[
 S^2+(P_0+Q_0)S-1+i(Q_0-P_0)=0
 \tag{8}
\]
has exactly one root with \(\Re S>0\), and that root has
\(|\Im S|<1\). It is simple and continues the original real-parameter
root. On compact sets of (7) it is holomorphic on a neighborhood.

*Proof.* Continue from \(\alpha=\beta=0\) along the straight path
in these two imaginary parts. A root on the imaginary axis,
\(S=iv\), must satisfy
\[
 v=\frac{p-q}{p+q}\in(-1,1).
 \]
The real part of (8) there is at most
\[
 -1-v^2+(1-v)A+(1+v)B
 \le A+B-1+\frac{(A-B)^2}{4}<0.
 \tag{9}
\]
Thus no root crosses the imaginary axis. On the two horizontal
sides \(S=u\pm i\), with \(u>0\), the imaginary parts of (8) are
respectively
\[
 u(2+\alpha+\beta)+2q>0,\qquad
 u(-2+\alpha+\beta)-2p<0.
\]
Here (7) implies \(A+B<1\). Thus a root cannot cross either
horizontal side. At their imaginary-axis corners the same formulas
are nonzero. On a compact
continuation path roots cannot escape to infinity. The original
real-parameter theorem supplies exactly one right-half-plane root
in the strip at the starting point. Root counts and the two strip
barriers preserve this assertion. Finally
\(\Re(2S+P_0+Q_0)>0\), so this root is simple.
Uniqueness glues the holomorphic continuations. \(\square\)

For the boxes (1)--(2), the explicit cotangent formula and fixed
outward scalar comparisons give
\[
\begin{split}
 0&\le\Im\cot\pi(a+it)<61/100 &&(h\le t\le0),\\
 |\Im\cot\pi(b+ic)|&<37/100,\\
 \frac{61}{100}+\frac{37}{100}
       +\frac14\left(\frac{61}{100}-\frac{37}{100}\right)^2
                         &=\frac{1243}{1250}<1.
\end{split}
 \tag{10}
\]
For precision the first two scalar upper bounds are
\[
 \frac{\sinh(.216\pi)}
      {\cosh(.216\pi)-\cos(.492\pi)}<.61,\qquad
 \frac{\sinh(.136\pi)}
      {\cosh(.136\pi)-\cos(.534\pi)}<.37.
 \tag{11}
\]
The modulus decreases with the real coordinate on these intervals.
It increases with the absolute height: for the first box use
\(\cos(.492\pi)\cosh(.216\pi)<1\); for the second the cosine
is negative. These are whole-box comparisons, not sampled extrema.
The real parts of both cotangents are positive.

The root in Lemma 1 is therefore defined along the entire first
vertical segment, with the second argument fixed at \(b+ic\).
Its strip inverse satisfies \(0<\Re s_*<1/2\), so all original
arguments \(s_*+a+it,s_*+b+ic\) stay in their regular strips.
The original zero logarithmic lift continues from real arguments.
At the actual reference it equals the original conditional root:
that root lies in the same cotangent chamber, where uniqueness applies.

## 3. The first negative height helps the phase

For \(\phi_{00}\), the original lifted gradient identities are
\[
 \partial_1\phi_{00}=\log_{\rm R}(S+P_0)-\log_{\rm R}(S-i),
 \qquad
 \partial_2\phi_{00}=\log_{\rm R}(S+Q_0)-\log_{\rm R}(S+i).
 \tag{12}
\]
They are the identities in the
[acute-gradient proof](research_mixed_acute_gradient_height_transfer.md),
continued within the domain just proved. All four logarithms have
positive-real-part arguments. If \(S=u+iv\), the imaginary
numerators of the two ratios in (12) are respectively
\[
 u(1+\alpha)+p(1-v)>0,\qquad
 u(\beta-1)-q(v+1)<0.
 \tag{13}
\]
Hence throughout the first segment
\(\Im\partial_1\phi_{00}>0\), and at the actual reference
\(-\pi<\Im P<0\). In particular, lowering the first height from
zero to \(h<0\) increases the real phase.

At first height zero, the second vertical segment is within the
old half-cotangent domain. Vertical convexity and the real acute
gradient bound there give
\[
 \Re\phi_{00}(r_1,r_2)
 \ge f_{00}(a,b)-\frac{\pi}{2}(-c)_+.
 \tag{14}
\]
The rectangle \([.246,.350]\times[.267,.438]\) lies strictly
inside the same six-corner convex hexagon used in the
[three-three collar proof](research_mixed_three_cap_collar_comparison.md),
Section 2. Its original saved phase floors and real concavity give
\(f_{00}(a,b)>11/25\).

The [complete-cap theorem](research_mixed_complete_first_cap_packet.md)
gives \(\Re\mathcal T_1(r_1,-2)>1\).
Moreover \(-\Re g(r_1)>0\), by the radial dilogarithm formula
(22) in the
[Fourier-weight theorem](research_mixed_fourier_weight_continuation.md),
since \(0<a<1/2\) and \(h<0\). Thus (3) and (14) imply
\[
                  M_{43}>1+\frac{11}{25}
                                      -\frac{\pi}{2}(-c)_+.
 \tag{15}
\]
Dropping the positive weight contribution in this lower bound does
not remove it from the actual phase or stationarity identity.

## 4. The full finite collar

Use \(M_0(C)\) and \(\Delta_\rho=\rho\log2-J(\rho)\) from the
three-three collar proof. The already proved full cap and row bounds
give the upper rate
\[
 \frac{433}{500}+M_0(2\pi k_+)+2\Delta_\rho+\omega(\rho)+\eta,
 \tag{16}
\]
for (6). Here \(\eta>0\) is one arbitrarily small total source
and color tolerance. The term \(\omega(\rho)\to0\) is the
uniform upper rate of the **actual** first \(d_N\) polynomial
from equation (8) of
[the boundary-strip bound](research_mixed_boundary_strip_bounds.md).
Its endpoint forcing is retained. There is no division by \(d_N\).

Since \(-\pi<\Im P<0\), the same convex attenuation argument as
for the three-three prefix yields
\[
 M_0(2\pi k_+)+\frac{\pi}{2}(-c)_+
                    +(k-c)\Im P<.326+.068\pi.
 \tag{17}
\]
For \(c\le0\), the tangent term is nonpositive and
\((-c)/2<.0325<.068\). For \(c\ge0\), convexity in \(k\)
reduces to \(k=0,c\). The inherited bounds
\(M_0(0)<.326,\ M_0(.146\pi)<.526\), monotonicity of \(M_0\),
and \(.526<.326+.068\pi\) prove (17).
This includes the entire physical height interval.

The raw seam reserve before collar costs is consequently
\[
 1+\frac{11}{25}-\frac{433}{500}-.326-.068\pi
                              >\frac{17}{500}.
 \tag{18}
\]
Choose a fixed \(0<\rho\le.001\) small enough that
\(2\Delta_\rho+\omega(\rho)<1/100\), and then use a total
tolerance \(\eta<1/250\).

**Theorem 2.** For every fixed open word beginning \((4,3)\),
there is a fixed collar of the preceding size and a small ordinary
color neighborhood on which, for either \(\sigma\in\{0,1\}\),
\[
 \left|U_{1,N}(w,X)C_{0,N}(X,e^{-2\pi iz_2})
                              d_N(X)X^{-N\sigma}\right|
 \le C N^A
    \exp N\{M_{43}+\Re[P(z_2-r_2)]-1/50\}.
 \tag{19}
\]
The estimate includes both parities and every fixed ordinary
derivative on a smaller color neighborhood. It is uniform in (6).
The collar is fixed before \(N\to\infty\); no uniform limit as its
size changes with the level is asserted.

The strict reserve also permits a small fixed change of the second
real coordinate, at the expense of decreasing the displayed gap,
with the same reference tangent. This is a calibrated boundary-pair
estimate. Its remaining second incidence, the middle completion, and
the other end of the source still need their separate comparisons.
No global open-word or arbitrary-short filling theorem follows.

## Reproduction

The focused checker
[`check_mixed_four_three_cap_collar.py`](../experiments/check_mixed_four_three_cap_collar.py)
verifies the exact strip and gradient identities, the fixed outward
scalar bounds, the inherited six-corner phase floors, and current
source provenance. It does not recompute any conditional root or
parameter cover:

```sh
python3 experiments/check_mixed_four_three_cap_collar.py --precision 256
```

Its author record is
[`research-mixed-four-three-cap-collar.json`](../repro/results/research-mixed-four-three-cap-collar.json).
