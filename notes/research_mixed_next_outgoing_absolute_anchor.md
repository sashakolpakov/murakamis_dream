# An absolute rate from the terminating outgoing row

Private finite-source theorem, 9 November 2026. The local resolvent
comparison extends through the last physical row. Its missing frozen
link becomes small precisely where that row ceases to be distant.
Consequently the exact terminal value \(C_{D,N}=1\) fixes an absolute
exponential rate for the complete outgoing polynomial, including its
half-input boundary value.

This is a statement about the original complete finite sum. It does
not estimate its signed contraction with the inner periods. The rate
below is defined by the terminating recurrence; no continuation of
the original factorial action past its proved sheet domain is assumed.
The task attachment and the current progress front were reread.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. Complete source, frozen inverse, and statement

Keep the exact source of the
[trailing determinant theorem](research_mixed_next_outgoing_trailing_determinants.md):
\[
\begin{gathered}
D=N-1,\quad M=\lceil N/2\rceil,\quad \theta=\pi/N,\quad
q=e^{i\theta},\quad r=q^{-2},\\
s_j=2\sin(j\theta),\qquad S_b=\prod_{j=1}^{b}s_j,\qquad S_D=N,\\
C_{b,N}(Z)=
 \sum_{k=0}^{D}
 \frac{(r^b)^{-k}(r^{b+1};r)_k(rZ;r)_k}{(r;r)_k^2}.
\end{gathered}                                                     \tag{1}
\]
At a physical index the literal stop is \(D-b\).
Every numerator zero is retained, and \(C_{D,N}=1\) exactly.
Work uniformly on the closed containing region
\[
\mathfrak Z=
\left\{\rho e^{-i\alpha}:
 4/5\le\rho\le8/7,\quad3\pi/5\le\alpha\le39\pi/50\right\}.
                                                                    \tag{2}
\]
In particular the actual complete \(343\) reference family of
length at least five is included.

For \(1/2\le a\le1\), set
\[
\begin{gathered}
t=t(a)=\frac{\pi a-\pi/2}{2},\qquad
\sigma(a)=2\sin(\pi a)=2\cos(2t),\qquad \tau(a)=\sigma(a)^{3/2},\\
V(a,Z)=3e^{it}+2e^{-3it}+Ze^{5it}.
\end{gathered}                                                     \tag{3}
\]
Let \(\mathcal H^0(a,Z)\) be the half-line operator
\[
(\mathcal H^0f)_k
 =\tau e^{-it}f_{k-1}+Vf_k+\tau e^{it}f_{k+1},
 \qquad k\ge0,\quad f_{-1}=0.
                                                                    \tag{4}
\]
Its invertibility on this entire closed parameter set is proved
below. Define
\[
m(a,Z)=\bigl((\mathcal H^0(a,Z))^{-1}\bigr)_{0,0}.                  \tag{5}
\]
This definition also applies at \(a=1\), where \(\tau=0\).
It fixes the branch without choosing an unproved continuation
of a critical value.

For \(a<1\), write
\[
Y(a)=e^{-2\pi ia},\quad A(a)=Y(a)(Y(a)-1),\quad
w(a)=-e^{5it(a)},\qquad
\mathcal L(a,Z)=-A(a)w(a)m(a,Z).                                  \tag{6}
\]
Define the real anchored rate
\[
\mathcal E(a,Z)
 =-\int_a^1\log|\mathcal L(x,Z)|\,dx
 =-\int_a^1\log\{\sigma(x)|m(x,Z)|\}\,dx.
                                                                    \tag{7}
\]
The endpoint singularity is integrable.

**Theorem.** There are positive constants \(c,C\), independent of
\(N,b,Z\), such that for all sufficiently large levels and both
parities:

1. Every complete ratio is nonzero and
\[
\frac{C_{b,N}(Z)}{C_{b-1,N}(Z)}
 =\mathcal L(b/N,Z)\bigl(1+\epsilon_{b,N}(Z)\bigr),
\qquad |\epsilon_{b,N}|\le C/N,\qquad M\le b\le D.
                                                                    \tag{8}
\]
2. Put \(a_{b,N}=\max\{b/N,1/2\}\). For \(M-1\le b\le D\),
\[
c\,\frac{S_b}{N}
 \exp\left[-N\int_{a_{b,N}}^1\log|m(x,Z)|\,dx\right]
\le |C_{b,N}(Z)|
\le
C\,\frac{S_b}{N}
 \exp\left[-N\int_{a_{b,N}}^1\log|m(x,Z)|\,dx\right].
                                                                    \tag{9}
\]
In particular, uniformly over that whole range,
\[
\log|C_{b,N}(Z)|
 =N\mathcal E(a_{b,N},Z)+O(\log N).                              \tag{10}
\]
3. At the original half-input boundary,
\[
c\,N^{-1/2}e^{N\mathcal E(1/2,Z)}
 \le |C_{M-1,N}(Z)|
 \le C\,N^{-1/2}e^{N\mathcal E(1/2,Z)}.
                                                                    \tag{11}
\]
The exact sine-product multiplier in (9) at this boundary is
\[
\frac{S_{M-1}}{N}
 =\begin{cases}
 (2N)^{-1/2},&N\ \text{even},\\
 N^{-1/2},&N\ \text{odd}.
 \end{cases}                                                       \tag{12}
\]
The constants in (11) absorb the bounded half-step integration
cost, not an unidentified exponential anchor.

These two-sided bounds do not assert a limiting leading coefficient
or an \(O(N^{-1})\) relative asymptotic for a complete transfer.

## 2. The frozen inverse at the degenerate endpoint

The
[full-tail energy theorem, equation (16)](research_mixed_next_outgoing_full_tail_weighted_energy.md)
provides a fixed smooth real function \(\beta(t)\), with
\(-1\le\beta\le3\), for which
\[
\Re V-\beta(t)\Im V-2\tau>51/350
                  \qquad(0\le t\le\pi/4,\ Z\in\mathfrak Z).
                                                                    \tag{13}
\]
The off-diagonal part of (4) is self-adjoint. Thus the real
quadratic form of \((1+i\beta(t))\mathcal H^0\) is at least
\(51/350\) times the squared norm. The same inequality holds
for the real quadratic form of its adjoint. The first inequality
gives closed range and injectivity; the second makes the range
dense. Hence the range is all of the half-line Hilbert space,
and the inverse norm is uniformly bounded.

When \(\tau>0\), unitary conjugation removes \(e^{\pm it}\).
The homogeneous characteristic is
\[
\tau\xi^2+V\xi+\tau=0.
\]
It has no unit-circle root by (13), and its two roots have
product one. The square-summable solution gives
\[
\tau^2m^2-Vm+1=0,\qquad |\tau m|<1.                              \tag{14}
\]
In particular \(m\ne0\).
At \(a=1\), direct substitution in (3) gives
\[
V(1,Z)=e^{i\pi/4}(1-Z),\qquad
m(1,Z)=\frac{e^{-i\pi/4}}{1-Z}\ne0.                              \tag{15}
\]
The inequality (13) also proves nonvanishing of this diagonal,
independently of the explicit formula.

The coefficients of (4) are continuously differentiable in
\(a\) on the closed interval: \(\sigma^{3/2}\) has a bounded
continuous derivative through \(\sigma=0\).
The inverse identity and the uniform inverse norm therefore
give a uniform \(C^1\) bound for \(m\). Compactness, continuity,
(14), and (15) give
\[
0<c_m\le|m(a,Z)|\le C_m<\infty,\qquad
|\partial_a\log|m(a,Z)||\le C_m.                                \tag{16}
\]
Here no branch of a complex logarithm is needed.
The same argument gives holomorphic dependence on \(Z\) in a
fixed neighborhood of (2), if that dependence is required.

Equations (6),(15) show the precise terminal degeneration:
\[
\frac{\mathcal L(a,Z)}{1-a}
 \longrightarrow-\frac{2\pi i}{1-Z}\qquad(a\uparrow1).
                                                                    \tag{17}
\]
It is a simple zero of the frozen unsigned ratio. Formula (17)
is derived from the actual recurrence normalization, rather than
from an extrapolated action expression.

## 3. Uniform finite freezing all the way to \(D\)

For \(I_b=[b,D]\), let \(G^{(b)}=(\mathcal J_{I_b,N}-ZI)^{-1}\)
be the exact inverse from the trailing determinant theorem.
Put
\[
K_b=\operatorname{diag}_{j\in I_b}\sqrt{S_j},\quad
w_j=\exp i\{(5j/2+1/4)\theta-\pi/4\},\quad W_b=\operatorname{diag}(w_j),
\]
\[
H_{b,N}=W_bK_b(\mathcal J_{I_b,N}-ZI)K_b^{-1}.
                                                                    \tag{18}
\]
Number its rows from zero. The exact formulas of the
[finite-ratio theorem, equations (9)--(12)](research_mixed_next_finite_outgoing_ratio_transport.md)
are valid through \(D\):
\[
(H_{b,N}^{-1})_{0,0}=G^{(b)}_{b,b}/w_b,\qquad
|(H_{b,N}^{-1})_{0,k}|\le C_0e^{-\gamma k},
                                                                    \tag{19}
\]
\[
\begin{split}
V_{j,N}
 &=3e^{i(t_j+\theta/4)}
   +2\cos\theta\,e^{-i(3t_j+3\theta/4)}
   +Ze^{i(5t_j+\theta/4)},\\
h_{j,N}&=s_{j+1}^{3/2}e^{i(t_j-3\theta/4)}.
\end{split}                                                       \tag{20}
\]
The upper off-diagonal entry is \(h_{j,N}\), and the lower one
is its conjugate. The bound in (19) comes from the natural-last-row
extension in the trailing determinant theorem; it is not a
middle-only estimate. In particular no metric involving \(S_N=0\)
is introduced.

Fix \(b\), put \(n=D-b\), and let
\[
f=(\mathcal H^0(b/N,Z))^{-1}\mathbf e_0.
\]
Its norm and all its coordinates are uniformly bounded by
Section 2. On row \(k\), the differences between (20) and the
frozen coefficients are bounded by \(C(k+1)/N\). This follows
from the bounded derivatives of the trigonometric terms and
the Lipschitz property of \(x^{3/2}\) on \([0,2]\); no inverse
sine occurs. Restricting \(f\) to \(0,\ldots,n\), its residual
therefore satisfies the sharper terminal estimate
\[
\left|
 \bigl(H_{b,N}f|_{[0,n]}-\mathbf e_0\bigr)_k
\right|
 \le \frac{C(k+1)}N+C\tau(b/N)\mathbf1_{\{k=n\}}.
                                                                    \tag{21}
\]
The final term is exactly the omitted frozen upper link
\(-\tau e^{it}f_{n+1}\). This retains its small coefficient,
unlike the distant-end estimate used on the middle interval.

Applying (19) before summing yields
\[
\left|(H_{b,N}^{-1})_{0,0}-m(b/N,Z)\right|
 \le \frac CN\sum_{k=0}^{n}(k+1)e^{-\gamma k}
             +C\tau(b/N)e^{-\gamma n}.                           \tag{22}
\]
Since \(b=N-1-n\),
\[
\sigma(b/N)=2\sin\frac{(n+1)\pi}{N}
 \le \frac{2\pi(n+1)}N.
\]
Consequently
\[
\tau(b/N)e^{-\gamma n}
 \le \frac{(2\pi)^{3/2}}{N^{3/2}}
                (n+1)^{3/2}e^{-\gamma n}
 \le C N^{-3/2}.                                                \tag{23}
\]
The last constant is finite because a fixed exponential dominates
that fixed power. Equations (22)--(23) prove
\[
(H_{b,N}^{-1})_{0,0}=m(b/N,Z)+O(N^{-1})
                         \qquad(M\le b\le D),                   \tag{24}
\]
including \(n=0\).

The exact unsigned ratio is
\[
\frac{C_{b,N}}{C_{b-1,N}}
 =-A_b w_b(H_{b,N}^{-1})_{0,0},\qquad
A_b=A(b/N),\qquad w_b=e^{i\theta/4}w(b/N).
                                                                    \tag{25}
\]
All denominators are nonzero by the exact trailing determinant
theorem. Combining (16),(24),(25) proves (8). Although \(A_b\)
tends to zero at the last rows, it is an exact common factor
in (25). Thus the absolute \(O(N^{-1})\) error in \(m\) gives
the stated relative error in the ratio without dividing by
\(A_b\).

## 4. Multiplication from the literal terminal value

Taking real logarithms of moduli in (8) gives, uniformly in
every physical index,
\[
\log|C_{j,N}/C_{j-1,N}|
 =\log s_j+\log|m(j/N,Z)|+O(N^{-1}).
\]
There are at most \(N\) terms. Since \(C_{D,N}=1\), their
backward product gives
\[
\log|C_{b,N}|
 =\log(S_b/N)-\sum_{j=b+1}^{D}\log|m(j/N,Z)|+O(1),
                           \qquad M-1\le b\le D.                \tag{26}
\]
The empty sum at \(b=D\) is included. The \(O(1)\) is real,
uniform above and below; it cannot hide an exponential anchor.

By the uniform derivative bound in (16),
\[
\sum_{j=b+1}^{D}\log|m(j/N,Z)|
 =N\int_{a_{b,N}}^1\log|m(x,Z)|\,dx+O(1).                       \tag{27}
\]
For \(b=M-1\) the first grid point is \(M/N\).
Its displacement from \(1/2\) is at most \(1/(2N)\); the last
missing endpoint at \(1\) also costs only \(O(1)\).
Thus (27) holds at both parities without defining \(m\) left
of \(1/2\). Equations (26)--(27) prove (9).

For completeness the exact sine product has the uniform
Riemann estimate
\[
\log(S_b/N)
 =-N\int_{a_{b,N}}^1\log(2\sin\pi x)\,dx+O(\log N).
                                                                    \tag{28}
\]
For \(b\ge M\), the integrand is decreasing on \([1/2,1)\).
Left/right integral comparison through \(D/N\) has error at
most its endpoint variation, \(O(\log N)\).
On the last interval, the elementary bounds
\[
4(1-x)\le2\sin(\pi x)\le2\pi(1-x)
                              \qquad(1/2\le x\le1)
\]
give
\[
N\int_{D/N}^{1}\log(2\sin\pi x)\,dx=-\log N+O(1).
\]
These facts prove (28) uniformly, including \(b=D\).
The remaining case \(b=M-1\) follows from (12) and the identity
\[
\int_{1/2}^{1}\log(2\sin\pi x)\,dx=0.                            \tag{29}
\]
For example (29) follows by symmetry and the double-angle
identity applied to the integrable logarithm on \([0,\pi/2]\).
Equations (9),(28) give (10).

Finally, reflection of the factors \(s_j=s_{N-j}\) and
\(S_D=N\) yields
\[
S_{M-1}^2=N/2\quad(N\ {\rm even}),\qquad
S_{M-1}^2=N\quad(N\ {\rm odd}),
\]
because the even middle factor is \(s_{N/2}=2\), whereas
the odd full product consists of two equal halves.
This proves (12). By (29),
\[
\mathcal E(1/2,Z)=-\int_{1/2}^{1}\log|m(x,Z)|\,dx.
\]
Substitution in (9) proves the absolute boundary estimate (11).

## 5. Relation to the proved action and the remaining signed source

On the original middle interval \(1/2\le a\le5/6\), for the
actual parameter rectangle of the finite-ratio theorem, its
selected-root identification says
\[
\mathcal L(a,Z)=e^{\partial_a\mathcal S(a,z_*)}.
\]
Hence the rate just proved obeys
\[
\partial_a\mathcal E(a,Z)=\Re\partial_a\mathcal S(a,z_*),
\qquad
\mathcal E(a,Z)-\Re\mathcal S(a,z_*)
 =\mathcal E(1/2,Z)-\Re\mathcal S(1/2,z_*).
                                                                    \tag{30}
\]
This records exactly what is licensed by that source.
Identifying the constant on the right with zero would require
a separate proof of the original action's terminal normalization
and sheet continuation. No such identification is used in
Sections 1--4.

The complete transfer still contains, with its original scalar,
\[
\frac1{\kappa_N^2N}
 \sum_{b=M}^{D}(-q)^b\lambda_b C_{b,N}(Z_*),
\qquad
\lambda_b=\phi_N(R^3e_bQ_N^{\rm full}).
                                                                    \tag{31}
\]
The trailing determinant theorem proves that this is the remaining
lower-boundary observation after the already paid errors, not
an additional positive sum that may be discarded.
The absolute outgoing normalization (11) removes the unknown
outgoing anchor. It does not estimate the correlated sum (31),
its Green numerator, or the inner periods' cancellation.
No free-boundary transfer theorem, new normalized jets, or
short-partial-filling stability is inferred.

## Frozen source bindings

- Finite outgoing ratio transport:
  2bf8a2f401b3472da0d250c97403fa776396e3dd524bd149a9209b6f8eacdeaf.
- Exact trailing determinants and natural last row:
  8564c705a0c8cd96cb7211c10166a522dde511bda27a94ac18a7cdafccf0b47f.
- Full-tail weighted energy:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Original selected outgoing sheet:
  850d97273259d39b0fc0ecf89bedaddceb97b13555c38a95d1f3e9fa7643067d.
- Quantitative selected action:
  77ffb14e6f3a3408b4aee3594d1c205b9db61fccdbf011181de9f86c26e9dbd5.

The proof uses only exact finite identities, uniform analytic
inequalities, and written integral comparison. No numerical
evaluation, saved-value calculation, or replay was performed.

