# Uniform full-dilogarithm ray moments and finite transfer inverses

Fix the full function and its marked negative ray from [F]. The ray
moments have size comparable to \(N^{-1}\), uniformly over every
physical degree, for all sufficiently large levels. The top degree
has an additional endpoint contribution, which is retained below.
The resulting finite nilpotent transfer and its inverse have
subexponential operator bounds. No lower bound for a closed scalar
observation is inferred.

## 1. The original moments and the uniform profile

Let \(N\ge2\), \(d=N-1\), \(\epsilon\in\{1,-1\}\), and
\(Q=\exp(2\pi i/N)\). The signed ray part of the literal moment
functional [F, Section 4a] is
\[
 j_{\epsilon,a}
 =-\frac{\epsilon(-1)^{N-a}}{2\pi i}
   \int_0^1\Psi_\epsilon(\log r+i\epsilon\pi)
                         r^{N-a-1}\,dr,
 \qquad 0\le a<N.                                      \tag{1}
\]
Thus the original coefficient is its shifted-circle contribution
plus (1). This sign convention retains the minus sign of the
radial part of the full moment functional.

Put
\[
 b=N-a,\qquad
 \phi(r)=-\frac{\operatorname{Li}_2(-r)}{2\pi},\qquad
 c=\frac{\log2}{2\pi},\qquad c_0=\frac1{2\pi}.
 \tag{2}
\]
The uniform assertion is
\[
\begin{split}
 I_{\epsilon,b,N}
 &:={\int_0^1\Psi_\epsilon(\log r+i\epsilon\pi)r^{b-1}\,dr}\\
 &=\frac{\sqrt2\,e^{i\epsilon N\pi/24}}{b+i\epsilon Nc}
   -\frac{\mathbf1_{b=1}}{i\epsilon Nc_0}
   +O(N^{-3/2}),\qquad 1\le b\le N.                    \tag{3}
\end{split}
\]
The error is uniform in the integer \(b\) and in \(\epsilon\).
In particular there are constants \(c_*,C_*>0\) and \(N_0\) such that
\[
 \frac{c_*}{N}\le |j_{\epsilon,a}|\le\frac{C_*}{N}
 \quad(N\ge N_0,\ 0\le a<N).                          \tag{4}
\]
No assertion excluding coefficient zeros at the finitely many smaller
levels is made.

### The actual quantum remainder

The full-strip estimate [F,(7a)] and its stated logarithmic derivative
estimate give, on this particular ray,
\[
 \Psi_\epsilon(\log r+i\epsilon\pi)
 =\sqrt{1+r}\,e^{i\epsilon N\phi(r)}(1+e_{\epsilon,N}(r)),
 \qquad
 \sup_{r>0}\bigl(|e_{\epsilon,N}|+|r e'_{\epsilon,N}|\bigr)
 \le C/N.                                             \tag{5}
\]
The derivative bound follows by Cauchy's estimate on a smaller fixed
logarithmic strip. The same chosen function and branch occur in (1)
and (5). Also [F,(13b)] gives the exact identity
\[
             |\Psi_\epsilon(\log r+i\epsilon\pi)|=\sqrt{1+r}.
 \tag{6}
\]
We use no uniform ordinary derivative of \(e_{\epsilon,N}\) at zero.

Indeed, split the error in replacing the integrand in (1) by the
leading expression in (5) at \(r_0=N^{-2}\). On \([0,r_0]\), (5)
or (6) bounds its integral by \(C N^{-2}\), uniformly for \(b\ge1\).
On \([r_0,1]\) set
\(A_b(r)=r^{b-1}\sqrt{1+r}\,e_{\epsilon,N}(r)\).
Its supremum is \(O(N^{-1})\), and
\[
 \int_{r_0}^1|A_b'(r)|\,dr\le C\log N/N.             \tag{7}
\]
The derivative of \(r^{b-1}\) has integral at most one; the only
logarithmic loss is \(\int_{r_0}^1dr/(Nr)\) from (5).
Now
\[
 \phi'(r)=\frac{\log(1+r)}{2\pi r},\qquad
 c\le\phi'(r)\le c_0\quad(0\le r\le1),              \tag{8}
\]
and \(\phi''\) is bounded, with removable values at zero.
One integration by parts against \(e^{i\epsilon N\phi}\), using
(7)--(8), bounds the upper-interval error by
\(C\log N/N^2\). Consequently
\[
 I_{\epsilon,b,N}
 =\int_0^1 r^{b-1}\sqrt{1+r}\,e^{i\epsilon N\phi(r)}dr
       +O(\log N/N^2),                              \tag{9}
\]
uniformly in every physical degree. This retains both original
endpoints; it is not a replacement of the full moment by a bare
circle coefficient.

### The two ranges of physical degrees

First let \(1\le b\le\sqrt N\), and write
\(a_b(r)=r^{b-1}\sqrt{1+r}\). Its endpoint first derivatives and
the \(L^1\) norm of its second derivative are \(O(b)\).
For \(b=1,2\) this is checked directly; for \(b\ge3\), the largest
term has integral
\((b-1)(b-2)\int_0^1r^{b-3}dr=b-1\).
The other terms are bounded in the same way. The derivatives of
\(\phi\) through third order are bounded on this interval, and
\(\phi'\) is bounded away from zero. Two integrations by parts give
\[
 \int_0^1a_b(r)e^{i\epsilon N\phi(r)}dr
 =\frac{\sqrt2 e^{i\epsilon N\pi/24}}{i\epsilon Nc}
   -\frac{\mathbf1_{b=1}}{i\epsilon Nc_0}
   +O(b/N^2).                                        \tag{10}
\]
Here \(\phi(0)=0\), \(\phi(1)=\pi/24\), and
\(a_b(0)=\mathbf1_{b=1}\). Replacing the first denominator in
(10) by \(b+i\epsilon Nc\) changes it by \(O(b/N^2)\).
This proves (3) in the first range.

For \(b>\sqrt N\), set
\[
 \delta=(b-1)/N,\qquad
 \Phi(r)=\delta\log r+i\epsilon\phi(r),\qquad
 A(r)=\sqrt{1+r}.
\]
Since \(\Phi'=\delta/r+i\epsilon\phi'\) never vanishes on the
positive interval, integration by parts gives the endpoint term
\[
 \frac{\sqrt2 e^{i\epsilon N\pi/24}}{b-1+i\epsilon Nc}
\]
and remainder
\[
 -\frac1N\int_0^1e^{N\Phi(r)}
                  \left(\frac{A(r)}{\Phi'(r)}\right)'dr.
 \tag{11}
\]
The endpoint at zero vanishes. On \([1/2,1]\), the differentiated
factor in (11) is uniformly bounded, so this part is
\(O(1/(Nb))\). On \((0,1/2]\), use
\(|\Phi'|\ge\delta/r\) to bound that factor by
\(C\delta^{-2}\). Its integral is bounded by
\(C\delta^{-2}2^{-b}/(Nb)\), which is smaller than \(N^{-3/2}\)
in the stated range. Finally replacing \(b-1\) by \(b\) in the
endpoint denominator costs \(O(N^{-2})\). Together with (9), this
proves (3) for all \(b\).

For \(b\ge2\), the modulus of the displayed main term in (3) is
at least \(\sqrt2/(N\sqrt{1+c^2})\). For \(b=1\), the lower
triangle bound, multiplied by \(N\), tends to
\[
                    \sqrt2/c-1/c_0>0.
\]
The upper bounds are uniform as well. The error in (3) is smaller
than these bounds at all sufficiently large levels, proving (4).

## 2. Exact finite normalization and the endpoint seam

Define the nonzero common phase and scale
\[
 \zeta_{\epsilon,N}
 =-\frac{\epsilon(-1)^N\sqrt2}{2\pi i}
                       e^{i\epsilon N\pi/24},\qquad
 h_a=\frac{N(-1)^a}{\zeta_{\epsilon,N}}j_{\epsilon,a}.
 \tag{12}
\]
Its modulus is \(\sqrt2/(2\pi)\), independent of level.
For \(0\le a\le d-1\), equation (3) gives
\[
 h_a=\frac1{1-a/N+i\epsilon c}+O(N^{-1/2}).            \tag{13}
\]
Consequently \(|h_0|\) is bounded above and below, all \(h_a\)
are bounded, and
\[
 |h_a-h_{a-1}|\le C N^{-1/2}\quad(1\le a<d),\qquad
 |h_d-h_{d-1}|\le C.                                \tag{14}
\]
The last difference is deliberately separate. It contains the
\(b=1\) contribution in (3), including its level-dependent phase.
It is not set to zero or estimated by the first bound in (14).

Let \(T\) act on any finite-dimensional Hilbert space, with
\(\|T\|_2\le1\) and \(T^N=0\). Put
\[
 \mathcal J_{\epsilon,N}(T)=\sum_{a=0}^d j_{\epsilon,a}T^a,
 \qquad H(S)=\sum_{a=0}^d h_aS^a.
\]
Then exactly
\[
       \mathcal J_{\epsilon,N}(T)
                  =\frac{\zeta_{\epsilon,N}}N H(-T).  \tag{15}
\]
For all sufficiently large \(N\), these maps are invertible and
\[
 \boxed{\displaystyle
 \|\mathcal J_{\epsilon,N}(T)\|_2\le C,
 \qquad
 \|\mathcal J_{\epsilon,N}(T)^{-1}\|_2
                      \le C N e^{C\sqrt N}.}         \tag{16}
\]

To prove the inverse bound, work modulo \(S^N=0\). The exact identity
\[
 (1-S)H(S)=h_0\left(1+\sum_{a=1}^d b_aS^a\right),
 \qquad b_a=(h_a-h_{a-1})/h_0                         \tag{17}
\]
has \(|b_a|\le\eta_N=C/\sqrt N\) for \(a<d\), and \(|b_d|\le C\).
For \(B_<(S)=\sum_{a=1}^{d-1}b_aS^a\), the coefficient of degree
\(n\ge1\) in \((1+B_<)^{-1}\) is bounded by
\[
 \sum_{k=1}^n {n-1\choose k-1}\eta_N^k
                      =\eta_N(1+\eta_N)^{n-1}.       \tag{18}
\]
This counts the ordered positive compositions of \(n\); all series
are finite modulo \(S^N\). The last seam contributes exactly
\(-b_dS^d\) to the inverse, because its product with every positive
power of \(S\) vanishes. Thus the sum of absolute coefficients
of the inverse in (17) is at most
\(C(1+\eta_N)^d+C\le C e^{C\sqrt N}\).
Multiplication by \(1-S\), whose norm is at most two, proves the
inverse estimate in (16). The direct bound follows from (4) by
summing \(N\) coefficients. This proof does not assume normality
or diagonalizability of \(T\).

## 3. Actual atom scope

The original unit-color transfers in [F, Section 5] have precisely
\(\|T\|\le1\), \(T^N=0\). Their unit geometric phases are retained
by replacing \(T\) by the corresponding unit multiple. In particular
the original \(u\)-ray is \(\mathcal J_{-,N}(Q^{-1}T)\), while
the \(v\)-ray is \(\mathcal J_{+,N}(T)\). Formula (15) keeps the
additional \((-1)^a\) phase explicitly rather than dropping it.

The original reciprocal-factorial ray diagonal has entries
\(Q^{-a}j_{-,a}\), and the reflected factorial ray diagonal has
entries \(NQ^{d-a}j_{+,d-a}\). By (4), for all sufficiently large
levels their norms and inverse norms satisfy respectively
\[
 \|D_{\rm rec}\|\le C/N,\quad \|D_{\rm rec}^{-1}\|\le CN,
 \qquad
 \|D_{\rm fac}\|+\|D_{\rm fac}^{-1}\|\le C.          \tag{19}
\]
These are the literal factors and index reflection of [F,(15)].
Any fixed composable product of these ray maps and fixed unitary
maps therefore has norm and inverse norm at most
\(N^M e^{C\sqrt N}\), with constants depending on the fixed product.
The assertion is about those invertible atomic maps. Original cups,
projections, marked covectors and subsequent contractions remain
their specified maps; (16)--(19) give no lower bound for their
scalar observation. Mixed circle/ray patterns may still retain
exponential source factors.

The estimates concern the full function's selected moments at radius
one and the original nilpotent finite atoms. They do not identify a
negative-ray chain with a geometric thimble, prove an off-root
identity, or extend an odd-level tetrahedral state to even levels.

## Complete direct source

- [F] [Full-dilogarithm coefficient cycles](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_modular_dilog_circle_and_boundary_source.md),
  SHA256 48649230d0552bac1a38c8d31a784e1ad4102172ed73916fdfc275aa9775dd7e.
  The entire proof was read. The fixed full function, uniform
  full-strip remainder and logarithmic derivatives, exact ray
  modulus, and original atomic reflection formulas are used.

The entire underlying defining-integral proof in
`literature_state_volume.md` was also read; its unchanged hash is
ae6117e059081c1cbd298ac65690294a6209a5b2d79b5b84ea5758789bd34946.
No mathematical program or numerical experiment was used.
