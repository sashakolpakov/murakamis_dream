# A complete physical two-step diagonal asymptotic

Private finite-source theorem, 9 November 2026. A sharper exclusion
of the frozen spectral cut extends the complete outgoing polynomial
to every compact lower unit arc with angular coordinate
\(1/8<y<1/2\). This pays the entire complement of the positive
diagonal base cycle identified in the preceding critical-curve note.

The resulting asymptotic concerns the complete original
\(C^{(2)}_{00,N}(r^M,r^M)\), at both parities, with its actual
physical half-input shift. It supplies a selected complete base
cycle for a possible later complex-output continuation. It does
not itself make that continuation or replace a missing finite
second-factor theorem by a real-parameter packet.
No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, test, or frozen-source edit is used.

## 1. A sharper unit-circle exclusion

Use the notation and exact finite recurrence of
[the complete lower-unit-arc theorem](research_outgoing_packet_lower_unit_arc.md):
\[
\begin{gathered}
D=N-1,\quad M=\lceil N/2\rceil,\quad r=e^{-2\pi i/N},\quad
P_j=(r;r)_j,\quad S_j=|P_j|,\\
C_{b,N}(Z)=\sum_{j=0}^D
 \frac{r^{-bj}(r^{b+1};r)_j(rZ;r)_j}{P_j^2}.
\end{gathered}                                                     \tag{1}
\]
All physical zeros are retained; the literal stop is \(D-b\).
For \(1/2\le a\le1\), write
\[
t=(\pi a-\pi/2)/2,\quad \sigma=2\cos2t,\quad k=\sigma^3,
\quad V=3e^{it}+2e^{-3it}+Ze^{5it}.
\]
That theorem already identifies every unit-circle intersection
of the frozen spectral interval for \(t<\pi/4\). It must have
\[
Z=e^{-i\alpha(t)},\qquad
\alpha(t)=5t-\pi-\varphi(t),\quad
\varphi(t)=\arcsin I_t,\quad
I_t=\sin t(1-4\cos2t),\quad |\varphi|\le\pi/4.                    \tag{2}
\]
Its proof retains both exact tests \(|A-d|^2<1\) and
\(|A+d|^2>1\), where \(A=3e^{it}+2e^{-3it}\) and
\(d=2\sigma^{3/2}\). Thus (2) is the only possible
intersection; it is not merely one candidate.

We sharpen its angular range to
\[
                         -\pi\le\alpha(t)<\pi/4.                 \tag{3}
\]
The lower bound is the already proved inequality
\(\varphi(t)\le5t\). For the upper bound split the interval.

If \(0\le t\le\pi/10\), then
\(\alpha\le5t-\pi+\pi/4\le-\pi/4\).
For \(\pi/10\le t\le\pi/6\), the exact identity
\[
I_t+\sin5t
   =2\sin t\,\cos2t\,(2\cos2t-1)\ge0
\]
compares \(\varphi(t)\) with \(5t-\pi\), both in
\([-\pi/2,\pi/2]\). Since sine is increasing there, it gives
\(\varphi(t)\ge5t-\pi\), and hence \(\alpha(t)\le0\).

Now let \(\pi/6\le t\le\pi/4\). If \(I_t\ge0\),
then \(\varphi\ge0\), so \(\alpha\le5t-\pi\le\pi/4\);
equality is impossible, because at \(t=\pi/4\) one has
\(\varphi=\pi/4\). If \(I_t\le0\), put \(c=\cos2t\).
Then \(1/4\le c\le1/2\), and
\[
I_t^2=\tfrac12(1-c)(1-4c)^2\le1/4.
\]
Indeed its derivative on this interval is
\((4c-1)(9-12c)/2\ge0\), and its value at \(c=1/2\)
is \(1/4\). Thus \(\varphi\ge-\pi/6\). Moreover
\[
t\le\tfrac12\arccos(1/4)<13\pi/60,
\]
because
\(\cos(13\pi/30)=\sin(\pi/15)<\pi/15<22/105<1/4\).
It follows that
\(\alpha\le5t-\pi+\pi/6<\pi/4\), completing (3).

No representative in (3), even modulo \(2\pi\), belongs
to \((\pi/4,\pi)\). The terminal coefficient \(k(1)=0\)
is still treated by its scalar equation
\(V(1,Z)=e^{i\pi/4}(1-Z)\ne0\).

Consequently every conclusion of the lower-unit-arc theorem
extends to an arbitrary compact arc
\[
                     Z=e^{-2\pi iy},\qquad1/8<y<1/2.             \tag{4}
\]
To be explicit, the spectral exclusion selects the unique
nonzero root \(km^2-Vm+1=0\) with \(|km^2|<1\).
On each compact set (4), it has a common holomorphic
neighborhood and a uniform strict contraction margin.
The exact backward finite Riccati induction therefore constructs
all nonzero denominators before determinant ratios are used.
The original ratio multiplication and terminal normalization
give
\[
C_{b,N}(Z)=\frac{S_b}{N}
 \exp\left\{-N\int_{b/N}^1\log h(a,Z)\,da\right\}
 \mathcal B(b/N,Z)(1+O_{\rm hol}(N^{-1})),
\quad M-1\le b\le D,                                             \tag{5}
\]
with precisely the original \(h,\mathcal B\) and all fixed
normalized outgoing derivatives. Their logarithm is continued
from the old overlapping arc. No energy estimate outside its
original domain has been assumed. The proof is the exact
backward construction of the cited theorem; (3) replaces
only its spectral exclusion range.

## 2. A strict bound on the omitted real arcs

Retain the original sine entropy and positive column profile
\[
J(x)=\int_0^x\log(2\sin\pi v)\,dv,\qquad
V(a)=-2J((1-a)/2)-J(a)=-2J(a/2),\quad0\le a\le1.                 \tag{6}
\]
The last equality is sine duplication and reflection.
In particular \(V\) increases up to \(a=1/3\) and decreases
thereafter.

One exact comparison is
\[
                              V(1/6)<V(1/2).                    \tag{7}
\]
Indeed, pairing the integral from \(1/12\) to \(1/4\) about
\(1/6\) gives
\[
\begin{split}
J(1/4)-J(1/12)
 &=\int_0^{1/12}
 \log\{(2\sin\pi(1/6+v))(2\sin\pi(1/6-v))\}\,dv\\
 &=\int_0^{1/12}\log(1-4\sin^2\pi v)\,dv<0 .
\end{split}
\]
Its integrand is finite and negative except at zero. Equation
(6) proves (7).

Let \(\mathcal S_{\rm h}(y)\) be the original half-input
conditional action. The
[critical-curve theorem](research_mixed_next_half_input_two_step_critical_curve.md)
proves that \(E(y)=\Re\mathcal S_{\rm h}(y)\) has a unique
nondegenerate maximum \(e_0=E(y_0)\) on \(0<y<1/2\), with
\(39/100<y_0<2/5\). At \(y=1/2\), its original index root is
\(\xi=1/4\). Substitution in its calibrated phase gives
\[
\mathcal S_{\rm h}(1/2)
 =2g(3/4)-2g(1/4)-2g(1/2)+\pi i/4
 =-4J(1/4)=2V(1/2).
\]
The root and action extend regularly to this point. Strict
decrease of \(E\) on \((y_0,1/2)\) therefore gives
\[
                              e_0>2V(1/2).                      \tag{8}
\]

The physical Gram identity is exact:
\[
K_{ab}=C_{0,N}(r^a,r^b)=\mathbf f(r^a)^*\mathbf f(r^b),
\qquad f_j(Z)=(rZ;r)_j/P_j.
\]
Cauchy--Schwarz and the endpoint-uniform column bound in
[the complete Gram theorem, (13)--(14)](research_mixed_next_two_step_gram_fourier_bound.md)
give, uniformly over all \(0\le a\le D\),
\[
|C_{M,N}(r^a)|\le\sqrt{K_{MM}K_{aa}}
 \le CN^A\exp N\{V(M/N)+V(a/N)\}
 \le CN^A\exp N\{V(1/2)+V(a/N)\}.                               \tag{9}
\]
The last inequality retains the favorable odd half-step
\(M/N\ge1/2\).

By (7)--(8), the right side of (9) has a fixed strict
rate gap below \(e_0\) when \(a/N\le1/6\).
Choose a sufficiently small fixed \(\epsilon_1>0\) such that
\[
y_0<1/2-\epsilon_1,\qquad
V(1/2)+V(1/2-\epsilon_1)<e_0.
\]
This is possible by (8) and continuity. Monotonicity of
\(V\) gives the same strict gap for every
\(a/N\ge1/2-\epsilon_1\), through the last physical node.
Thus both omitted real arcs are paid by a complete physical
bound; no zero or endpoint row is omitted.

On the remaining compact interval
\([1/6,1/2-\epsilon_1]\), the full source (5), the interior
sine-factorial expansion, and the original phase matching give
\[
|C_{M,N}(e^{-2\pi iy})|
 \le CN^A e^{NE(y)}.                                             \tag{10}
\]
This interval is strictly inside the new arc (4).
The unique strict maximum \(y_0\) pays its complement of
any fixed sufficiently small neighborhood of \(y_0\).
Combining (9)--(10), for such a neighborhood there is
\(\delta_*>0\) with
\[
\sum_{\substack{0\le a\le D\\|a/N-y_0|>\epsilon}}
          |C_{M,N}(r^a)|^2
       \le CN^A e^{2N(e_0-\delta_*)}.                             \tag{11}
\]
All constants work at both parities.

## 3. The whole positive base cycle and its normalization

The complete original two-step diagonal is
\[
C^{(2)}_{00,N}(r^M,r^M)
       =(K^2)_{MM}=\sum_{a=0}^D|C_{M,N}(r^a)|^2.                \tag{12}
\]
At even levels the two arguments are \(-1\); at odd levels
both remain \(r^M\). There is no external factor of \(N\),
\(\kappa\), or a new crossing phase in (12).

Set
\[
d_0=-E''(y_0)>0,\qquad
\delta_N=M-N/2\in\{0,1/2\},
\]
and use the original analytic action near half input
\[
\mathcal S(a,y)=J(a)-\int_a^1\log h(v,e^{-2\pi iy})\,dv .
\]
Define the two nonzero symbols
\[
a_{\rm par}(y)
 =\sqrt2\,\mathcal B(1/2,e^{-2\pi iy})
       \exp\{\delta_N\partial_a\mathcal S(1/2,y)\}.                \tag{13}
\]
These are the symbols of the physical row \(M\), not of
the different row \(M-1\).

The local physical Gaussian already proved in
[the critical-curve theorem, (28)--(30)](research_mixed_next_half_input_two_step_critical_curve.md),
together with the complete complement bound (11), gives
\[
\boxed{\quad
C^{(2)}_{00,N}(r^M,r^M)
 =N^{-1/2}|a_{\rm par}(y_0)|^2
        \sqrt{\frac{\pi}{d_0}}\,
       e^{2N\Re\mathcal S_{\rm h}(y_0)}
                         (1+O(N^{-1/2})).
\quad}                                                         \tag{14}
\]
This is a full finite-source asymptotic, not only a local
integral or a lower bound. The coefficient is positive and
nonzero at both parities. The exact odd input and output shifts
are retained by (12)--(13). The relative error is asserted
for these physical diagonal values; no complex derivative
claim is implicit.

The rational curve of the preceding theorem gives an
unramified original-log phase branch at this base. Equation
(14) now shows that the complete actual positive cycle
selects its action and coefficient. Continuation toward a
non-diagonal ordinary complex \(W\) is still separate:
one must retain the original strip lifts, establish the
complete second factor at the resulting complex parameters,
and control the deformed cycle's full complement. Positivity
of (12) does not persist in that problem. The \(\beta=1\)
source also retains its complex \(P_j^{-1}\) weight.
No comparison with the actual four-block conditional action,
propagated remainder gap, or closed-word volume theorem is
claimed here.

## Frozen source bindings

- Exact original lower-unit-arc recurrence, spectral cut, finite
  inverse construction, and amplitude:
  ec77eea9959e496b98c52274d249c056af6c3a656a5bb4fad0534c70efefdca8.
- Selected rational curve, unique diagonal maximum, original
  constants, both-parity physical Gaussian:
  6d62635e470aebe2c32d6d3f862a5a9379590f4e4951e467fb4ffb7c76c256a7.
- Complete physical Gram matrix, endpoint column norms and scalar:
  be5dc00fde7c062f7b6ad0e7b8859b2e9dd5d564f16bce0aea75de9dba12cb6e.
- Whole-strip original half-input root and phase:
  623ebfda0574d46a7e10e851d27a9fd48a8910543691a58a8d819a882878be47.

