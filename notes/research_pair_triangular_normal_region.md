# An exponentially smaller first-normal region in the internal pair

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The value of a Newton polynomial \(e_j\) vanishes at every physical
row \(a<j\). Its first normal usually does not vanish there. This
note keeps those normals explicitly and bounds the part of the
two-vertex source where both rows satisfy \(a<j\), for
\(j/N\le1/4\) or \(j/N\ge49/100\). The bound is uniform in the two crossing powers.
Together with the geometric power comparison, it removes this
part of the original source for every fixed positive pair of
powers at least three.

The region with only one row below \(j\), and the remaining shared
indices \(1/4<j/N<49/100\), are not estimated here.

## 1. The original first normal below the triangular value support

Put
\[
 \theta=\pi/N,\quad s_k=2\sin(k\theta),\quad
 S_k=\prod_{h=1}^k s_h,\quad S_0=1,\quad
 c_a=2\cos((2a+1)\theta),
 \]
\[
 e_j(z)=S_j^{-2}\prod_{h=0}^{j-1}(c_h-z),\qquad
 L=\lfloor(N-1)/2\rfloor,\qquad \eta=(-1)^{N-1}.
 \tag{1}
\]
Let \(\mathcal L_N(z)=\sum_{k=0}^L e_k(z)e_k(-2)\) be the
low-index complete-end kernel. Its physical values are
\[
                  \mathcal L_N(c_a)=F_{a,N}(-2),
             \qquad F_{a,N}(w)=K_N(c_a,w).
 \tag{2}
\]
Every high-index polynomial vanishes at a physical value, so (2)
holds at both parities.

For \(0\le a<j\le L\), one has the exact identity
\[
 \boxed{\quad
 e_j'(c_a)=(-1)^{j-a}
       \frac{S_{j+a}S_{j-a-1}}{s_{2a+1}S_j^2}.
 \quad}
 \tag{3}
\]
To prove it, differentiate the single vanishing factor \(c_a-z\)
in (1). For \(h\ne a\),
\[
 c_h-c_a=-4\sin((h+a+1)\theta)\sin((h-a)\theta).
 \]
There are \(j-a-1\) negative factors. The absolute product is
\[
 \prod_{\substack{0\le h<j\\h\ne a}}|c_h-c_a|
      =\frac{S_{j+a}S_{j-a-1}}{s_{2a+1}}.
 \]
The additional minus sign from the derivative gives (3).
All factorial indices in this calculation are less than \(N\).

At a double physical root the original trace contribution is
\[
 \eta\{(4-c_a^2)f'(c_a)-c_a f(c_a)\}.
 \tag{4}
\]
For \(f=R^n e_j\mathcal L_N\) and \(a<j\), the value of \(e_j\)
is zero. Thus only its first normal remains; derivatives of the
crossing and of the outside factor do not enter this contribution.
Since \(4-c_a^2=s_{2a+1}^2\), define its exact sum by
\[
 U_{n,j,N}
   =\eta\sum_{a=0}^{j-1}(-1)^{j-a}R(c_a)^nD_{a,j,N},
 \qquad
 D_{a,j,N}
   =s_{2a+1}F_{a,N}(-2)
                \frac{S_{j+a}S_{j-a-1}}{S_j^2}>0.
 \tag{5}
\]
The original crossing value has modulus one. Formula (5) is an
alternating sum with the actual quadratic crossing phase retained.
It is not a positive expression for the trace.

All rows \(a<j\le L\) are double physical roots. In particular, the
odd simple endpoint \(a=L\) does not occur in (5), so (4) requires
no modification here.

## 2. A monotone magnitude bound at every low index

First omit the bounded sine factor in (5), and write
\(E_{a,j,N}=D_{a,j,N}/s_{2a+1}\).
For \(a\le j-2\), division of consecutive terms gives
\[
 \frac{E_{a+1,j,N}}{E_{a,j,N}}
  =\frac{F_{a+1,N}(-2)}{F_{a,N}(-2)}\,
     \frac{s_{j+a+1}}{s_{j-a-1}}>1
                   \qquad(j\le L).
 \tag{6}
\]
The physical-row ratio is strictly greater than one by the original
positive recurrence at \(w=-2\). The sine ratio is also greater than
one, even when its larger index exceeds \(N/2\), because
\[
 \sin((j+a+1)\theta)-\sin((j-a-1)\theta)
       =2\cos(j\theta)\sin((a+1)\theta)>0 .
\]
Using \(s_{2a+1}\le2\), it follows that
\[
 |U_{n,j,N}|
 \le 2jE_{j-1,j,N}
   =2jF_{j-1,N}(-2)\frac{S_{2j-1}}{S_j^2}.
 \tag{7}
\]
This bound is independent of \(n\); no estimate of a derivative
of the crossing was needed.

Let
\[
 J(x)=\int_0^x\log(2\sin\pi v)\,dv,\qquad
 C(x)=J(2x)-2J(x)+\psi(\pi-2\pi x,0),
                       \quad 0\le x\le1/2.
 \tag{8}
\]
Here \(J\) is real on this interval and \(\psi\) has the original
complete-edge normalization \(\psi(0,0)=4G/\pi\).
The uniform sine-factorial estimate, the
[absolute physical-row theorem](research_physical_row_riccati_transport.md#6-absolute-normalization-from-the-original-first-row),
and its [extension through the last row](research_last_physical_row_riccati.md)
give, including both ends of the index interval,
\[
               |U_{n,j,N}|\le C_0N^A e^{NC(j/N)} .
 \tag{9}
\]
Changing \(2j\) to \(2j-1\), or the physical half-grid angle to
\(\pi-2\pi j/N\), costs \(O(\log N)\) in the exponent. The
logarithmic endpoint singularities are integrable and the same
uniform estimates cover \(j=1\).

The function in (8) is strictly increasing on \((0,1/4]\), since
\[
 C'(x)=2\log(2\cos\pi x)
                  +2\operatorname{asinh}(\cot\pi x)>0 .
 \tag{10}
\]
Using \(J(1/2)=0\) and \(J(1/4)=-G/(2\pi)\), its largest value is
\[
                  C(1/4)=\psi(\pi/2,0)+G/\pi<251/200.
 \tag{11}
\]
A rational verification of the last bound is given below.

There is a second useful interval. Write \(x=1/2-\epsilon\), where
\(0\le\epsilon\le1/100\). Reflection of \(J\), the bound
\(2\sin(\pi v)\ge4v\) for \(0\le v\le1/2\), and monotonicity of
the real complete-end phase give
\[
 \begin{split}
 C(1/2-\epsilon)
 &=-J(2\epsilon)
       +2\int_0^\epsilon\log(2\cos\pi v)\,dv
       +\psi(2\pi\epsilon,0)\\
 &\le M_\infty+2\epsilon\{1-\log(4\epsilon)\}\\
 &<\frac76+\frac1{50}\left(1+\frac{13}4\right)
      =\frac{751}{600}<\frac{251}{200}.
 \end{split}
\]
At \(\epsilon=0\) use the continuous limit. The middle expression
increases with \(\epsilon\) on this interval. The rational comparisons
use \(M_\infty<7/6\) and \(\log25<13/4\).

## 3. The two first-normal factors are below the geometric rate

In the low-index pair source, expand its middle edge in the original
Newton basis. Define
\[
 \mathcal I_N=\{1\le j\le L:
                 j/N\le1/4\ \hbox{or}\ j/N\ge49/100\}.
\]
The contribution with
\[
                  j\in\mathcal I_N,\qquad a<j,\quad b<j
 \]
at the two selected physical rows is exactly
\[
       \mathcal U_{n,p,N}
           =\sum_{j\in\mathcal I_N}U_{n,j,N}U_{p,j,N}.
 \tag{12}
\]
There is no complex conjugation in (12). Both original first
normals and both crossing phases remain present.

**Theorem 1.** For every fixed pair of integers \(n,p\ge3\), at both
level parities,
\[
 |\mathcal U_{n,p,N}|
       \le C N^A e^{(251/100)N}
       \le C N^A e^{N(M_{n,p}-1/100)} .
 \tag{13}
\]
Here \(M_{n,p}\) is the original geometric rate with the two outside
ends complete.

**Proof.** The two interval bounds just proved bound each product in (12), and
there are at most \(N\) products. For the geometric comparison,
[the convex block-contraction theorem](research_edge_cut_energy_comparison.md#6-it-suffices-to-insert-two-vertices-of-power-three),
Proposition 6, decreases the convex minimum when either of the two
powers is increased from three. The fixed three-edge normalization
is \(M=3M_\infty-F/\pi\); therefore
\[
                         M_{n,p}\ge M_{3,3}>63/25.
 \tag{14}
\]
The last strict inequality is the certified geometric action in
[the original mixed-packet proof](research_internal_pair_three_mixed_packet.md):
its half-action is greater than \(63/50\).
Since \(63/25-251/100=1/100\), (13) follows.

The estimate removes an actual portion of the physical trace.
It does not assign the same bound to all factorial-wall currents
in a complex contour decomposition. The terms with exactly one
row below \(j\), and the indices \(1/4<j/N<49/100\), remain to be treated.

## 4. Rational constants and finite checks

For an entirely rational upper bound in (11), use
\[
 \psi(\pi/2,0)=\frac{2\sqrt2}{\pi}
 \sum_{r=0}^{\infty}
 \left(\frac1{(8r+1)^2}+\frac1{(8r+3)^2}
       -\frac1{(8r+5)^2}-\frac1{(8r+7)^2}\right).
 \tag{15}
\]
This follows from the Fourier series
\(J(x)=-\sum_{k\ge1}\sin(2\pi kx)/(2\pi k^2)\).
Each grouped term in (15) is positive. After the first \(B\ge2\)
groups, discarding the two negative terms and comparing with an
integral bounds the tail by \(1/(32(B-1))\).
For \(G\), the alternating sum through \(k=20\) in
\(\sum_{k\ge0}(-1)^k/(2k+1)^2\) is an upper bound.
Taking \(B=100\), \(\sqrt2<99/70\), and \(\pi>333/106\)
proves (11) by rational arithmetic. The same bounds for \(G\) and
\(\pi\) give \(4G/\pi<7/6\). Finally the first ten positive Taylor
terms of \(e^{13/4}\) already exceed \(25\), proving the logarithmic
comparison used at the other endpoint.

The accompanying checker verifies these comparisons, the saved
action enclosure in (14), and (3)--(7) against direct finite Newton
products at both parities:

~~~sh
python3 experiments/check_pair_triangular_normal_region.py
~~~

Its [saved record](../repro/results/research-pair-triangular-normal-region.json)
distinguishes the exact rational comparisons from the finite
high-precision normalization checks.

## 5. The remaining region must retain its cancellation

There is an additional useful fact about (5). On every fixed real
interval \(\alpha\le j/N\le\beta<1/2\), with \(\alpha>0\),
\[
 U_{n,j,N}
   =-\eta R(c_{j-1})^nD_{j-1,j,N}\bigl(1+O(N^{-1})\bigr).
 \tag{16}
\]
The estimate is uniform in real crossing powers, since only their
unit physical moduli are used. Indeed the original row ratios obey
\(F_{a+1}(-2)/F_a(-2)\ge1+\kappa_\beta\) for all \(a<j\): the
recurrence gives the lower bound \(1+(c_0+2)/A_a\), and \(A_a\)
is uniformly bounded for \(a<\beta N\). By (6), all backward ratios
of \(E_{a,j,N}\) are therefore at most
\((1+\kappa_\beta)^{-1}<1\). The first backward ratio from
\(a=j-1\) is moreover \(O(N^{-1})\), since its sine quotient is
\(s_1/s_{2j-1}\). Summing the remaining geometric majorant, and
using \(s_{2j-1}\ge c_{\alpha,\beta}>0\), proves (16).

Thus the final-row approximation to the two-normal sum has a
quadratic crossing phase with power \(n+p\). Its formal analytic
phase is
\[
 \mathcal F_{n+p}(x)
   =2C(x)+\frac{i(n+p)}{4\pi}(\pi-2\pi x)^2 .
 \tag{17}
\]
The half-grid shifts remain in the exact source; (17) records only
the exponential phase. With \(t=\pi-2\pi x\), its stationary equation is
\[
 \log(2\sin(t/2))+\operatorname{asinh}(\tan(t/2))
                       =\frac{i(n+p)t}{4}.
 \tag{18}
\]
Neither (16) nor this equation proves an asymptotic for the coherent
sum in \(j\). An \(O(N^{-1})\) error relative to each real summand
can be much larger than their sum after cancellation.

The [finite diagnostic](../experiments/probe_pair_triangular_cancellation.py)
evaluates the entire exact two-normal sector
\(\sum_{j=1}^L U_{3,j,N}^2\), without replacing (5) by (16).
At odd levels \(33,65,129,257\), its logarithmic moduli divided by
\(N\) are approximately
\[
                  2.3210,\quad2.5355,\quad2.6643,\quad2.7390.
\]
The full geometric pair rate is approximately \(2.52756\).
These finite values do not prove a larger limiting rate; in
particular a comparison at one finite level would not exclude a
polynomial prefactor. They do show why the unestimated two-normal
band should remain grouped with the mixed and value contributions,
instead of being assigned an unproved absolute gap.

For comparison, the formal equation (18) at \(n+p=6\) has a
stationary point near \(t=0.45245+0.27612i\), with real formal action
near \(2.76000\). Its coefficient in the exact finite sum has not
been established. The discarded tail in a real-summand approximation
and the original cycle would both have to be controlled to use it.

Run the reproducible finite calculation with

~~~sh
python3 experiments/probe_pair_triangular_cancellation.py
~~~

Its [saved data](../repro/results/research-pair-triangular-cancellation-diagnostic.json)
are explicitly marked as diagnostics. They do not change the proved
gap for the two index intervals in Theorem 1.
