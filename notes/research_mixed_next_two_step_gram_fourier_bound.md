# A complete two-step conditional bound from the original Gram matrix

Private finite-source theorem, 9 November 2026. The next two-step
conditional polynomial has an explicit exponential upper profile,
uniform over all its physical incoming rows and compact complex
output sets. The proof uses the original positive three-crossing
Gram matrix, without assigning positivity to the following four-type
kernel. It retains the full output degree and the endpoint coefficient
identified in the exact propagation note.

After the original positive Newton-to-Chebyshev transition, the
entire Fourier-weighted envelope has its unique maximum at the
half-input, zero-frequency endpoint. This bounds the complete
propagated right contribution. Comparison of its explicit ceiling
with the next geometric action is not asserted. No mathematical
numerical evaluation, import, compilation, or frozen-source edit
is used.

## 1. Original finite sources and the explicit profiles

Use the conventions and the whole two-step source in
[exact Fourier propagation, (1)--(8)](research_mixed_next_attachment_fourier_propagation.md):
\[
\begin{gathered}
D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
P_j=(r;r)_j,\quad S_j=|P_j|,\quad p_j(W)=(rW;r)_j,\\
C_{\beta,N}(Y,W)
 =\sum_{j=0}^D\frac{Y^{-j}p_j(Y)p_j(W)}{P_j^{2+\beta}},
 \qquad \beta\in\{0,1\},\\
C^{(2)}_{0\beta,N}(Y,W)
 =\sum_{a=0}^D C_{0,N}(Y,r^a)C_{\beta,N}(r^a,W)
 =N\operatorname{CT}_Z[C_{0,N}(Y,Z)C_{\beta,N}(Z,W)] .
\end{gathered}                                                     \tag{1}
\]
There is no old-four weight on this intermediate cycle. In
particular the two-step polynomial in (1) is not a selected
sector or a composition of truncated conditional packets.

Let
\[
J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
J(0)=J(1/2)=J(1)=0,\qquad c=-2J(1/6)>0 .
                                                                    \tag{2}
\]
Define on the whole closed real interval
\[
V(a)=-2J((1-a)/2)-J(a),\qquad 0\le a\le1.
                                                                    \tag{3}
\]
For every complex \(W\), define
\[
\begin{split}
B_\beta(W)
 &=\max_{0\le s\le1}
       \left\{\int_0^s\log|1-We^{-2\pi iu}|\,du
                                      -(1+\beta)J(s)\right\}\\
 &=\max_{0\le v\le1}
       \left\{(1+\beta)J(v)
             +\int_v^1\log|W-e^{-2\pi iu}|\,du\right\}.
\end{split}                                                       \tag{4}
\]
The logarithmic zeros in these integrals are integrable.
Both profiles are continuous on compact output sets. The second
formula follows from \(v=1-s\), \(J(1-v)=-J(v)\), and
\[
|1-We^{-2\pi iu}|=|W-e^{2\pi iu}|.
\]
Thus \(B_0\) is exactly the profile \(\mathcal B\) in
[the original forcing Gram bound, (23)](research_mixed_next_actual_forcing_gram_bounds.md).
That source also proves
\[
B_0(e^{-2\pi ix})=V(x),\qquad
\max_{0\le x\le1}V(x)=c .
                                                                    \tag{5}
\]
Since \(\max J=J(5/6)=c/2\), (4) implies
\[
                 B_1(W)\le B_0(W)+c/2 .                          \tag{6}
\]
These are positive upper profiles; they are not selected critical
actions of the two-step kernel.

**Theorem 1.** Fix a compact set \(\mathcal K\subset\mathbb C\)
and any \(\epsilon>0\). There are constants \(C_\epsilon,A_\epsilon\)
such that, for both parities, every \(0\le b\le D\), every
\(W\in\mathcal K\), and all sufficiently large \(N\),
\[
\boxed{\quad
|C^{(2)}_{0\beta,N}(r^b,W)|
 \le C_\epsilon N^{A_\epsilon}
       \exp N\{\,2c+V(b/N)+B_\beta(W)+\epsilon\,\},
             \qquad\beta=0,1 .
\quad}                                                           \tag{7}
\]
This includes \(b=0,D\), every literal row, and the entire
degree-\(D\) output polynomial.

## 2. Exact feature factorization and all incoming endpoints

Put
\[
f_j(W)=p_j(W)/P_j,\quad
\mathbf f(W)=(f_j(W))_{j=0}^D,\quad
\mathsf F_{ja}=f_j(r^a),\quad
\mathsf D_\beta=\operatorname{diag}(P_j^{-\beta}) .
                                                                    \tag{8}
\]
The original finite products give, for every \(|Y|=1\),
\[
Y^{-j}\frac{p_j(Y)}{P_j}=\overline{f_j(Y)} .
                                                                    \tag{9}
\]
For example conjugating each factor of \(p_j(Y)\) and \(P_j\)
gives respectively
\((-1)^jY^{-j}r^{-j(j+1)/2}p_j(Y)\) and
\((-1)^jr^{-j(j+1)/2}P_j\), proving (9).

Consequently the complete physical matrix
\[
K=(C_{0,N}(r^a,r^b))_{a,b=0}^D=\mathsf F^*\mathsf F
\]
and the two-step source obey exactly
\[
C^{(2)}_{0\beta,N}(r^b,W)
 =\mathbf f(r^b)^*(\mathsf F\mathsf F^*)
                              \mathsf D_\beta\mathbf f(W).
                                                                    \tag{10}
\]
Thus
\[
|C^{(2)}_{0\beta,N}(r^b,W)|
 \le \sqrt{K_{bb}}\,\|K\|\,
                         \|\mathsf D_\beta\mathbf f(W)\|_2 .
                                                                    \tag{11}
\]
Only \(K\) and \(\mathsf F\mathsf F^*\) are assigned positivity.
The phases in \(\mathsf D_1\) remain in (10); the bound (11)
does not make \(C_1\) positive.

The original exact similarity and the proved one-crossing norm,
as recorded in the forcing Gram theorem, (6) and (17), give
\[
K=\mathsf U(\mathsf M^*\mathsf M)\mathsf U^*,\qquad
\|K\|\le C N^A e^{2Nc},
\quad \mathsf U=\operatorname{diag}((-q)^{-a}).
                                                                    \tag{12}
\]
Here \(\mathsf M\) is the original crossing matrix on the full
Newton algebra. No semisimple quotient or replacement norm is used.

At each physical row the support zero gives the positive identity
\[
K_{bb}
 =\sum_{j=0}^{D-b}
           \left(\frac{S_{b+j}}{S_bS_j}\right)^2 .
                                                                    \tag{13}
\]
The endpoint-uniform factorial estimate
\(\log S_\ell=NJ(\ell/N)+O(\log N)\), \(0\le\ell\le D\),
from [the positive transition source, Section 5](research_mixed_next_outgoing_positive_chebyshev_transition.md),
therefore bounds each summand by its original entropy
\[
2N\{J(a+t)-J(a)-J(t)\}+O(\log N),
       \qquad a=b/N,\quad t=j/N,\quad 0\le t\le1-a .
\]
For \(0<a<1\), differentiation in \(t\) shows that
\[
J(a+t)-J(a)-J(t)
\]
increases up to \(t=(1-a)/2\) and decreases thereafter:
\[
\sin\pi(a+t)-\sin\pi t
          =2\sin(\pi a/2)\cos(\pi(t+a/2)).
\]
Its maximum equals \(V(a)\) in (3), using
\(J((1+a)/2)=-J((1-a)/2)\). Continuity includes \(a=0,1\).
The at most \(N\) summands in (13) hence give
\[
                       \sqrt{K_{bb}}
                         \le C N^A e^{NV(b/N)} .                \tag{14}
\]
This is uniform through the last physical row \(b=D\).
It uses no approximation of a zero numerator by a nonzero one.

## 3. Zero-safe control of the complete output feature vector

The remaining factor in (11) is exactly
\[
\|\mathsf D_\beta\mathbf f(W)\|_2^2
       =\sum_{j=0}^D\frac{|p_j(W)|^2}{S_j^{2+2\beta}} .
                                                                    \tag{15}
\]
In particular the \(j=D\) term is retained.

Here is the uniform treatment of numerator zeros. On
\(\mathcal K\times[0,1]\), replace
\(\log|1-We^{-2\pi iu}|\) by its truncation from below at
\(-L\). For fixed \(L\) this is a continuous majorant, uniformly
continuous on the compact product. Its Riemann sums converge
uniformly, also for partial intervals \([0,j/N]\). The integral
excess over the untruncated logarithm tends uniformly to zero
as \(L\to\infty\): near \(|W|=1\) there is at most one
logarithmic angular singularity per period, with a uniform
integrable logarithmic majorant; away from that annulus the
integrand is bounded below. This is the zero-safe product
argument of the forcing Gram theorem, Section 3, now applied
to the prefix product in (15).

Choosing \(L\) and then \(N\), for each prescribed \(\epsilon>0\),
gives uniformly in \(j,W\)
\[
\log|p_j(W)|
 \le N\int_0^{j/N}\log|1-We^{-2\pi iu}|\,du+N\epsilon
\]
with any further fixed polynomial allowance absorbed into the
constants. If the product itself vanishes, the upper bound is
automatic. Apply the uniform factorial estimate to the nonzero
\(S_j\). Definition (4) and the finite row count imply
\[
\|\mathsf D_\beta\mathbf f(W)\|_2
 \le C_\epsilon N^{A_\epsilon}
                           e^{N(B_\beta(W)+\epsilon)} .
                                                                    \tag{16}
\]
This proves Theorem 1 from (11)--(14), after allocating the
tolerance. The proof is uniform in both parities and every row,
not only on compact subsets of the scaled index interval.

For reference, the profiles also give the simple whole-disk ceilings
\[
B_\beta(W)\le (1+\beta/2)c+\log^+|W|,\qquad \beta=0,1 .
                                                                    \tag{17}
\]
For \(\beta=0\), the functions in the second line of (4),
with \(v\) fixed, are subharmonic in \(W\). On \(|W|=1\)
they are at most \(c\), by (5); the maximum principle
gives the same inside the disk. For \(R=|W|\ge1\), subtract
\((1-v)\log|W|\) from the fixed-\(v\) potential in the second
line of (4). The result is harmonic outside the unit disk,
is at most \(c\) on its boundary, and tends to
\(J(v)\le c/2\) at infinity. The exterior maximum principle
therefore bounds that potential by
\(c+(1-v)\log R\le c+\log R\).
Then (6) proves the \(\beta=1\) assertion. Only the explicit
profile (4), rather than (17), is used below.

## 4. Exact endpoint maximization of the Fourier envelope

Retain the entropy from the original positive transition:
\[
\mathcal H(x,t)
 =J(2x)-J(x-t)-J(x+t)-2J(1/2+x),
                       \qquad0\le t\le x\le1/2 .
                                                                    \tag{18}
\]
It is continuous through all endpoints. The selected charged action
in the incoming-color observation theorem satisfies
\[
\Gamma'(\delta)=-K_\delta,\qquad
0\le K_\delta<2/5,\qquad
\Gamma(0)-\Gamma(1/2)<34/275<1/8 .
                                                                    \tag{19}
\]
The last inequality is from
[the full paired-contour action comparison, (7)--(12)](research_mixed_next_outer_far_nodes_and_paired_contour.md).
Thus
\[
0\le\Gamma(1/2-t)-\Gamma(1/2)
                    \le\min\{2t/5,\,1/8\}.
                                                                    \tag{20}
\]

**Lemma.** On the full closed triangle in (18),
\[
\boxed{\quad
V(1/2+x)+\mathcal H(x,t)+\Gamma(1/2-t)
             \le V(1/2)+\Gamma(1/2),
\quad}                                                           \tag{21}
\]
with equality only at \(x=t=0\).

First the exact derivative of (3) is
\[
V'(a)=-\log(2\sin(\pi a/2)).
\]
For \(1/2\le a\le1\), it follows that
\[
V(1/2)-V(1/2+x)\ge\tfrac12(\log2)x>x/3
                                  \qquad(x>0).
                                                                    \tag{22}
\]
Here \(\log2>2/3\) follows from
\(\log2=2\int_0^{1/3}(1-u^2)^{-1}\,du>2/3\).

For \(0\le t<x<1/2\), the original entropy has
\[
\mathcal H(x,0)=\mathcal H_t(x,0)=0,\qquad
\mathcal H_{tt}(x,t)
 =-\frac{\pi\sin(2\pi x)}
          {\sin^2(\pi x)-\sin^2(\pi t)}
 \le -2\pi\cot(\pi x).
\]
Twice integrating gives
\[
-\mathcal H(x,t)\ge\pi\cot(\pi x)t^2
                     \ge\frac{1-2x}{x}\,t^2 .
                                                                    \tag{23}
\]
The last inequality uses
\(\cos(\pi x)\ge1-2x\) by concavity on \([0,1/2]\),
and \(\sin(\pi x)\le\pi x\). Continuity extends (23) to
\(t=x\) and \(x=1/2\); at the latter endpoint both displayed
lower bounds are zero.

If \(0<t\le1/4\), (22)--(23) and the arithmetic-geometric
mean inequality imply
\[
\begin{split}
V(1/2)-V(1/2+x)-\mathcal H(x,t)
 &>x/3+t^2/x-2t^2\\
 &\ge2t/\sqrt3-2t^2
 >t-2t^2\ge t/2>2t/5 .
\end{split}                                                       \tag{24}
\]
If \(t\ge1/4\), use \(1-2x\ge0\) and obtain
\[
\begin{split}
V(1/2)-V(1/2+x)-\mathcal H(x,t)
 &>x/3+1/(16x)-1/8\\
 &\ge1/(2\sqrt3)-1/8>1/8 .
\end{split}                                                       \tag{25}
\]
The final inequality is exactly \(\sqrt3<2\).
Equations (20), (24), and (25) prove strict inequality for
\(t>0\). If \(t=0\), then \(\mathcal H(x,0)=0\) and
(22) proves strict inequality for \(x>0\). At \(x=t=0\)
the two sides agree. This proves the lemma without optimizing
any numerically sampled profile.

In particular, for every fixed \(W\), the maximum of the explicit
full Gram/Fourier envelope is exactly
\[
\begin{split}
&\max_{0\le t\le x\le1/2}
 \{2c+B_\beta(W)+V(1/2+x)
                       +\mathcal H(x,t)+\Gamma(1/2-t)\}\\
&\hspace{25mm}=2c+B_\beta(W)+V(1/2)+\Gamma(1/2).
\end{split}                                                       \tag{26}
\]
This is a maximum of a proved upper profile. It is not an
asymptotic equality for a signed finite coefficient.

## 5. The complete propagated right contribution

Use \(M=\lceil N/2\rceil\), \(U=D-M\) and the exact identities
in the propagation note:
\[
\begin{split}
f^{(2,\beta)}_{k,N}(W)
 &=(-1)^{M+k}\sum_{d=k}^U
 q^{M+d}\beta_{d,k,N}C^{(2)}_{0\beta,N}(r^{M+d},W),\\
(\mathsf T_{0\beta}\mathcal R_N^+)(w,W)
 &=\frac1{\kappa^2N}\sum_{k=0}^U
                   f^{(2,\beta)}_{k,N}(W)\mathcal O_{N,k}(w).
\end{split}                                                       \tag{27}
\]
The original positive transition weights satisfy the uniform bound
\[
\beta_{d,k,N}\le CN^A e^{N\mathcal H(d/N,k/N)}
\]
at both parities, including \(d=k=0\) and \(d=U\).
The full Hermite observation obeys, for every \(\epsilon>0\),
\[
\sup_{w\in[-2,2]}|\mathcal O_{N,k}(w)|
 \le C_\epsilon e^{N(\Gamma(1/2-k/N)+\epsilon)}.
                                                                    \tag{28}
\]
All original normals, odd simple nodes, and both Fourier sectors
remain inside (27)--(28).

**Corollary 2.** For every compact \(\mathcal K\subset\mathbb C\)
and every \(\epsilon>0\),
\[
\boxed{\quad
\sup_{w\in[-2,2]}
 |(\mathsf T_{0\beta}\mathcal R_N^+)(w,W)|
 \le C_\epsilon N^{A_\epsilon}
 e^{N\{\,2c+B_\beta(W)+V(1/2)+\Gamma(1/2)+\epsilon\,\}},
 \quad W\in\mathcal K,\quad\beta=0,1 .
\quad}                                                           \tag{29}
\]
The same bound holds for the sum of the absolute complete mode
contributions in the second line of (27).

Indeed Theorem 1 and the transition bound give the exponent
in (26), with \(x=d/N\), \(t=k/N\), and an arbitrarily small
allocated tolerance. At odd levels
\[
(M+d)/N=1/2+d/N+1/(2N).
\]
The derivative \(V'\) is bounded on \([1/2,1]\), so this
shift costs only \(O(1)\) in the exponent, uniformly through
\(b=D\). At even levels there is no shift. Apply (21) and
(28), then sum the at most \(N^2\) terms. The exact scalar
\(\kappa^{-2}/N\) has modulus \(1/N\). All these finite costs
are retained or absorbed into the stated polynomial. This
proves (29).

The propagated polynomial still has the nonzero top output
coefficient of the exact propagation theorem. Nothing in
(10)--(29) deletes it. Likewise no finite conditional row,
small-index forcing, or terminal value has been removed.

This replaces an unspecified next-source majorant by an explicit,
proved full-polynomial bound. It does not show that the ceiling
in (29) is below the next reference action. The earlier physical
half-input anchor controls
\(\mathcal E(1/2,Z_*)+\Gamma(1/2)\) for the one-step
conditional source. It does not identify that action with
\(2c+V(1/2)+B_\beta(W)\). A sharper source estimate or a
new comparison with the correct next action would be needed
to obtain a next-attachment gap. The other terms
\(\mathsf T_{0\beta}E_N^-\) and the complementary next local
contour are not bounded by this corollary.

## Frozen source versions

- Exact next-attachment propagation and endpoint coefficients:
  07704e4c973619426b5f6d3090a2b5a49b55ec58a6f4d7afc1827f0c761c3b82.
- Original positive Gram representation, full operator norm, and
  zero-safe output profile:
  77354837ae73521349d7cc3834797c4c81dcae11f69ef1aa705223dec85ad5e8.
- Full positive transition and uniform sine-factorial bounds:
  68aad94365bf6a9f6ff8e3070e74c3e147ccabaf6845118c82adfe89a4fe1fab.
- Complete incoming-color Fourier observation:
  5bf182877bb6905b67d68f3aafb57ec5f015b57467a9b1fb7fbff2cff2108c49.
- Original charged-action derivative and total loss:
  4ef9ae846444c092aee5a85a36db81f8646307f3bb8d2591ccb678bed6c2bea7.

