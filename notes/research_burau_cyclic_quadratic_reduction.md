# An exact cyclic reduction of the marked-source quadratic

22 November 2026. This note reduces the accepted Euclidean quadratic
from the full tensor state space to at most \(k(N-1)+1\) complex unknowns.
Its numerical minimum and source comparison remain unchanged. The
reduced Hessian has condition number at most ten. The construction uses
the cyclic space of the specified terminal vector, not a quotient
compatible with arbitrary inserted tangles.

## 1. The specified source

Fix a knot braid with \(b\ge2\) strands, \(k\ge1\) crossing occurrences,
and physical writhe \(w\). At every level \(N\ge2\), the complete
[Fourier-height source](research_burau_fourier_height_contraction.md)
supplies explicit data on a Euclidean space of dimension \(N^{2k}\):
\[
 L=k(N-1)+1,\qquad C^L=0,\qquad \|C\|\le\tfrac12,
 \qquad \|u\|\le1,\qquad u^*v=1,
\]
\[
 K_N=\zeta u^*(I-C)^{-1}v,\qquad
 \zeta=Q^{(b-1+w)/2},\quad Q=e^{2\pi i/N}.
 \tag{1}
\]
Here \(C\) is the contracted matrix denoted by \(C_R\) in that source.
Its terminal norm \(V=\|v\|>0\) is known explicitly:
\[
 V^2=\left(N\sum_{j=0}^{N-1}R^{2j}\right)^k,
 \qquad
 R=2\sum_{j=1}^{b-1}\binom{b-1}{j}j!4^{kj}+1.
 \tag{2}
\]
The original phases, marked cut, and complete Hermite channels have
already entered these specified data. No value of \(K_N\) is supplied.
For a real \(\tau\ge1\), the accepted quadratic is
\[
 J_\tau(x)=4\tau V^2\|(I-C^*)x-u\|^2+|v^*x|^2.
 \tag{3}
\]

## 2. A cyclic space of at most linear dimension

Let \(m\ge1\) be the least integer with \(C^mv=0\). It exists and
satisfies \(m\le L\). The vectors
\[
 v,Cv,\ldots,C^{m-1}v
 \tag{4}
\]
are linearly independent. Indeed, in a nonzero relation choose its
least nonzero coefficient, at index \(j\), and multiply by
\(C^{m-1-j}\). All higher terms vanish, leaving a nonzero multiple
of \(C^{m-1}v\), a contradiction.

Apply Gram--Schmidt to (4), choosing every new normalizing length
positive. Let \(Q_0:\mathbb C^m\to\mathbb C^{N^{2k}}\) be the resulting
isometric inclusion. Its range
\[
 \mathcal K=\operatorname{span}\{C^jv:0\le j<m\}
 \tag{5}
\]
is \(C\)-invariant, and its first column is \(v/V\). Set
\[
 B=Q_0^*CQ_0,\qquad a=VQ_0^*u,\qquad A_0=I-B^*.
 \tag{6}
\]
Then
\[
 B^m=0,\quad \|B\|\le\tfrac12,\quad
 a_0=1,\quad 1\le\|a\|\le V.
 \tag{7}
\]
For the first entry use \(a_0=v^*u=1\). Thus the forcing does not
vanish, although the closed source can vanish. The matrix \(B\) is
upper Hessenberg: its \(j\)-th column has no entries below index
\(j+1\). When \(j<m-1\), its entry at index \((j+1,j)\) is the
positive norm of the component of \(Cq_j\) orthogonal to
\(\operatorname{span}(q_0,\ldots,q_j)\), where \(q_j\) is column \(j\)
of \(Q_0\). These assertions
follow because \(C\) maps the first \(j+1\) vectors of (4) into the
first \(j+2\).

Invariance and the finite inverse give the exact source identity
\[
 \boxed{\quad K_N=\zeta a^*(I-B)^{-1}e_0.\quad}
 \tag{8}
\]
All powers in this formula are the original ordered source powers,
compressed after the whole word has been specified.

There is an equivalent construction from one positive Gram. Put
\(Y=[v,Cv,\ldots,C^{m-1}v]\) and factor
\(Y^*Y=T^*T\), where \(T\) is upper triangular with positive diagonal.
Let \(S e_j=e_{j+1}\), with \(S e_{m-1}=0\). Then
\[
 Q_0=YT^{-1},\qquad B=TST^{-1},\qquad
 a=VT^{-*}Y^*u.
 \tag{9}
\]
Indeed \(CY=YS\), and \(Q_0^*Q_0=I\). No inverse or division in
(4)--(9) involves \(K_N\). The stopping index uses only the vanishing
of an explicitly known cyclic vector.
In this factorization the positive subdiagonal entry is exactly
\(T_{j+1,j+1}/T_{j,j}\).

## 3. Exact elimination of the complementary variables

The reduced quadratic is
\[
 \boxed{\quad
 j_\tau(z)=4\tau\|A_0z-a\|^2+|z_0|^2,
 \qquad z\in\mathbb C^m.
 \quad}
 \tag{10}
\]
It has exactly the same minimum as (3), not merely the same
exponential rate.

To prove this, use the orthogonal decomposition
\(\mathcal K\oplus\mathcal K^\perp\). Invariance gives block matrices
\[
 C=\begin{pmatrix}B&E\\0&D\end{pmatrix},\qquad
 I-C^*=\begin{pmatrix}A_0&0\\-E^*&I-D^*\end{pmatrix},
 \qquad v=\binom{Ve_0}{0}.
 \tag{11}
\]
Write \(u=(u_0,u_1)\) and \(x=(x_0,x_1)\). For every fixed \(x_0\),
the second residual in (3) can be made exactly zero by the unique choice
\[
 x_1=(I-D^*)^{-1}(u_1+E^*x_0).
 \tag{12}
\]
This inverse exists since \(\|D\|\le1/2\). The remaining objective is
\(4\tau V^2\|A_0x_0-u_0\|^2+V^2|(x_0)_0|^2\).
The substitution \(z=Vx_0\), with \(a=Vu_0\), proves
\[
 \min_xJ_\tau(x)=\min_zj_\tau(z)=:\mu_\tau.
 \tag{13}
\]
Formula (12) is a proof of the elimination. It need not be computed
to use the reduced problem or its trial certificates. Restricting
the original variable to \(\mathcal K\), without eliminating its
complement, would generally give a different objective.

## 4. Source comparison, phase, and certificates

Set
\[
 s=e_0^*A_0^{-1}a=\zeta\overline{K_N},\qquad
 \eta_\tau=\frac{\|(I-B)^{-1}e_0\|^2}{4\tau}.
 \tag{14}
\]
This is the same \(\eta_\tau\) as in the full problem: its vector
\((I-C)^{-1}v=VQ_0(I-B)^{-1}e_0\) lies in \(\mathcal K\).
In particular \(0<\eta_\tau\le1/\tau\). Completing the square in
\(r=A_0z-a\) gives
\[
 \mu_\tau=\frac{|K_N|^2}{1+\eta_\tau},\qquad
 \mu_\tau\le|K_N|^2\le(1+\tau^{-1})\mu_\tau,
 \qquad (z_*)_0=\frac{s}{1+\eta_\tau}.
 \tag{15}
\]
Thus \(K_N=\zeta(1+\eta_\tau)\overline{(z_*)_0}\), including its
original complex phase. These identities include zero sources and
all even or composite levels. If \(m=1\), all the same formulas hold
with \(B=0\).

The complex quadratic coefficient and its bounds are
\[
 P_0=4\tau A_0^*A_0+e_0e_0^*,\qquad
 \tau I\preceq P_0\preceq(9\tau+1)I.
 \tag{16}
\]
Consequently the real Hessian condition number is at most ten.
The unique minimizer solves
\(P_0z_*=4\tau A_0^*a\). For any trial \(z\), let
\[
 g_0(z)=4\tau A_0^*(A_0z-a)+e_0z_0.
\]
Exact quadratic completion gives the dimension-independent bound
\[
 \boxed{\quad
 [j_\tau(z)-\tau^{-1}\|g_0(z)\|^2]_+
 \le |K_N|^2\le(1+\tau^{-1})j_\tau(z).
 \quad}
 \tag{17}
\]
Indeed \(j_\tau(z)-\mu_\tau=g_0(z)^*P_0^{-1}g_0(z)\).
The scalar normal in the residual space
\(\mathbb C^m\oplus\mathbb C\) is
\[
 n=\binom{-(2\sqrt\tau)^{-1}A_0^{-*}e_0}{1},\qquad
 n^*\binom{2\sqrt\tau(A_0z-a)}{z_0}=s,\qquad
 \|n\|^2=1+\eta_\tau.
 \tag{18}
\]
Thus the entire normal, rather than just its value, also has a
description in at most \(L+1\) coordinates.

## 5. What the size reduction does and does not control

For each fixed braid the problem (10) has at most \(k(N-1)+1\)
complex unknowns and degree two. Its numerical minimum, relative
factor \(1+1/N\) when \(\tau=N\), and ordinary Euclidean conditioning
are unchanged. No evaluated value of \(K_N\) is supplied or used as a divisor.
The reduced Hessian has no exponential norm scale; the forcing \(a\)
can have the exponential size bounded in (7).

Constructing the cyclic basis can still be difficult. For example
\[
 \|Y\|_{\rm HS}^2\le\tfrac43V^2,
\]
but no lower bound on the least eigenvalue of \(Y^*Y\) is asserted.
The entries of \(Y^*u\) are exact coherent power coefficients; their
sum, after conjugation and the original phase, gives \(K_N\).
Computing them can therefore require contractions as hard as the
original problem. This is not an end-to-end linear-time algorithm,
a local boundary-width estimate, or a lower geometric growth bound.
In particular the normalization \(a_0=1\) does not imply that the
complete closing in (8) is nonzero.

The reduction concerns the fixed original closing. It does not provide
smaller packets compatible with arbitrary independent inserted
crossings, turns, or boundary normals. All original Hermite information
is used in (1); only its fixed cyclic source response is retained after
(5). No semisimple quotient or changed closing is substituted.

The sole entire direct proof source is the Fourier-height note above,
read at SHA-256
`bd72b2891707846966ccb30e910ca58dc7d9243e692046694cee88b98321e350`.
The complete [filtered Conway compiler](research_filtered_conway_observation_compiler.md)
and [two-sided source-quotient theorem](actual_source_two_sided_quotients.md)
were read for coverage. They concern different context budgets and
operator compatibility. No novelty is claimed for cyclic subspaces,
Gram--Schmidt, or quadratic elimination; the assertion here is their
exact application to (1)--(3), with its source and conditioning.

Only written mathematics and text/hash operations were used. No program,
test, numerical experiment, build, git operation, or earlier-final edit
was performed.
