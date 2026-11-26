# Whole-polynomial seams and fractional Euler time

Private written proof, 19 November 2026.

A change of Fourier radius acts on the entire finite polynomial by an
exact small rescaling. It therefore transports an already established
local WKB unit without an additional seam remainder. It does not
establish that unit after an unknown crossing. The second result below
identifies a concrete limitation of a proposed way to fill that gap:
fractional powers of the actual nilpotent Euler factor need not have
polynomial norm at complex times of size \(1/N\). This holds in both
the physical coefficient Euclidean metric and the original binomial
metric. A coarser exponential bound on bounded time disks does hold.

The sole complete proof direct F supplies the literal capped arrows
and the ordered physical crossing. All seam, logarithm, and norm
arguments used here are proved below.

## 1. Exact transport of the entire polynomial

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
For \(r\ne0\), define the finite Fourier evaluation matrix
\[
 \mathcal F(r)_{j,a}=N^{-1/2}(rQ^j)^a,\qquad
 \mathcal F(r)^{-1}_{a,j}=N^{-1/2}(rQ^j)^{-a},
 \quad 0\le a,j<N.
 \tag{1}
\]
If \(r'=re^{\alpha/N}\), its exact change of sample coordinates is
\[
 \mathcal E(r',r)_{j,k}
 =\frac1N\sum_{a=0}^d e^{\alpha a/N}Q^{(j-k)a}.
 \tag{2}
\]
The finite sum defines all removable values of the expression
\((1-e^\alpha)/[N(1-e^{\alpha/N}Q^{j-k})]\).
For every actual polynomial \(P_N(z)=\sum_{a=0}^d p_a z^a\),
\[
 \mathcal E(r',r)\bigl(P_N(rQ^k)\bigr)_k
       =\bigl(P_N(r'Q^j)\bigr)_j.
 \tag{3}
\]
Indeed multiplication of (1) recovers each coefficient, and its
new multiplier is \(e^{\alpha a/N}\). Thus the underlying polynomial
operation is exactly
\[
 D_\alpha P_N(z)=P_N(e^{\alpha/N}z).
 \tag{4}
\]
Its coefficient matrix is diagonal. Its norm and inverse norm are
at most \(e^{|\alpha|}\) in either diagonal coefficient metric used
below. Also \(\mathcal E=\mathcal F(1)D_\alpha\mathcal F(1)^{-1}\),
so the same bounds hold in Euclidean sample coordinates.

Tensor products give (3)--(4) for any fixed number of ports.
An incoming dual row uses the inverse, contravariant adapter; a
Laurent monomial is multiplied by the exponential of its signed
exponent. No occupation is reduced modulo \(N\), and no degree-\(N\)
or wrap term is added. These statements concern the entire finite
polynomial, not a separate estimate for each entry of (2).

All source adapters remain explicit. If a matrix is expressed as
\(W'=\mathcal F_{\rm out}W\mathcal F_{\rm in}^{-1}\), then for any
original source coupon \(Q_{\rm src}\),
\[
 \operatorname{Tr}(Q_{\rm src}W)
 =\operatorname{Tr}\bigl(
     \mathcal F_{\rm in}Q_{\rm src}\mathcal F_{\rm out}^{-1}W'\bigr).
 \tag{5}
\]
Internal inverse frames cancel in their actual order. Unequal endpoint
frames leave the adapter in (5). The original pivot, crossing scalars,
and framing line are part of this identity.

For completeness, suppose on a buffered complex chart the actual
polynomial has an initialized expansion
\[
 P_N(z,M)=\gamma_N(M)e^{NS(z,M)}A(z,M)(1+\epsilon_N(z,M)),
 \qquad \epsilon_N=O(N^{-1}),
 \tag{6}
\]
where \(S,A,A^{-1}\) have uniform holomorphic bounds on the buffer,
and the indicated remainder is bounded there. For bounded
\(\alpha\), Taylor expansion with \(\mathcal D=z\partial_z\) gives
\[
 P_N(e^{\alpha/N}z,M)
 =\gamma_N(M)e^{NS(z,M)}A(z,M)
           e^{\alpha\mathcal D S(z,M)}(1+O(N^{-1})).
 \tag{7}
\]
Specifically, \(N(S(e^{\alpha/N}z)-S(z))
=\alpha\mathcal D S+O(N^{-1})\), and the amplitude ratio is
\(1+O(N^{-1})\). These estimates hold also at \(z=0\), using
holomorphic dilation rather than a choice of \(\log z\).
For several ports the new multiplier is
\(\exp(\sum_j\alpha_j z_j\partial_{z_j}S)\), a unit.

The same argument handles any fixed number of seams whose dilations
stay in the buffer. If the whole-meridian family is holomorphic on
\(|N\mu|\le\eta'\), \(M=e^\mu\), with the bounds in (6) there, then
on \(|N\mu|\le\eta<\eta'\) every fixed derivative of the normalized
remainder in (7) satisfies
\[
 N^{-\ell}\partial_\mu^\ell O(N^{-1})=O(N^{-1}).
 \tag{8}
\]
This is Cauchy's estimate in \(N\mu\). On a fixed meridian buffer
the unscaled derivatives have the same \(O(N^{-1})\) bound.
If \(\alpha\) moves, its actual buffered derivatives must also be
retained. Equations (3)--(5) themselves are exact for all such
families and all true fixed-\(q\) meridian jets.

Thus whole-polynomial transport removes a separate seam estimate
once (6) is known. It does not supply (6), move an original contour,
or control a number of continuation steps growing with \(N\).

## 2. The actual capped Euler factor and its fractional powers

Use F's physical basis \(w_a\), \(0\le a\le d\), and \(x=-M/q\).
The arrows are
\[
 \begin{split}
 E(M)w_a&=(MQ^{-a}-M^{-1})w_{a-1}\quad(a>0),&
 E(M)w_0&=0,\\
 Fw_a&=(1-Q^{a+1})w_{a+1},&Fw_d&=0,\\
 Kw_a&=xQ^{-a}w_a.
 \end{split}\tag{9}
\]
Put \(f_n=(Q;Q)_n\), \(f_0=1\), and \(X(M)=E_1(M)F_2\).
Exactly \(X(M)^N=0\). F's positive checked crossing and its inverse
have the ordered factors
\[
 R^+=\kappa P D\Theta_+,\qquad
 R^-=\kappa^{-1}\Theta_-D^{-1}P,\qquad
 D w_{a,b}=x^{-a-b}Q^{ab}w_{a,b},
 \tag{10}
\]
where \(P\) exchanges the two heads, \(\kappa(M)\) is the original
crossing scalar, and
\[
 \Theta_+=\sum_{n=0}^{d}\frac{(-1)^nq^{n^2}X^n}{f_n},
 \qquad
 \Theta_-=\Theta_+^{-1}
          =\sum_{n=0}^{d}\frac{q^nX^n}{f_n}.
 \tag{11}
\]
The present norm test concerns this actual Euler factor. It does not
delete the Cartan factor, flip, or scalar from a physical crossing.

For a nilpotent \(Z^N=0\), let
\(E_N(Z)=\sum_{n<N}Z^n/f_n\). Direct coefficient comparison gives
\(E_N(QZ)=(I-Z)E_N(Z)\). Taking finite nilpotent logarithms and
comparing degrees \(1,\ldots,d\) proves
\[
 \log E_N(Z)=\sum_{n=1}^{d}\frac{Z^n}{n(1-Q^n)}.
 \]
Since \(\Theta_+=E_N(qX)^{-1}\), it follows that
\[
 L_N(M):=\log\Theta_+(M)
   =-\sum_{n=1}^{d}\frac{q^n X(M)^n}{n(1-Q^n)}.
 \tag{12}
\]
Only nonzero denominators \(1-Q^n\), \(0<n<N\), occur. The top
coefficient of the Euler difference equation vanishes because
\(Z^N=0\); the actual cap is used, not removed.

Define the exact fractional family
\[
 B_N(t,M)=\exp(tL_N(M)).
 \tag{13}
\]
It is a finite polynomial in the nilpotent \(X(M)\), entire in
complex \(t\), with \(B_N(0)=I\), \(B_N(1)=\Theta_+\),
\(B_N(-1)=\Theta_-\), and \(B_N(t+s)=B_N(t)B_N(s)\).
These algebraic identities alone give no small-time norm estimate.

## 3. A literal exponential derivative in two physical metrics

First set \(M=1\). Compare two tensor metrics: coefficient Euclidean,
where the \(w_a\) are orthonormal, and the original binomial metric
\[
 \|w_a\|_{\rm bin}^2=\binom da^{-1}.
 \tag{14}
\]
Let \(k\ge1\), \(N=4k+1\), and \(d=4k\). In the matrix entry
from \(w_{3k,k}\) to \(w_{k,3k}\), only \(X^{2k}\) in (12) can
contribute. Its absolute value is exactly
\[
 \left|(L_N(1))_{k,3k;\,3k,k}\right|
 =\frac{\displaystyle
          \prod_{j=k+1}^{3k}|1-Q^j|^2}
        {2k\,|1-Q^{2k}|}
 \ \ge\ \frac{2^{2k}}{4k}.
 \tag{15}
\]
Indeed \(j/N\) lies strictly between \(1/4\) and \(3/4\), so
\(|1-Q^j|=2\sin(\pi j/N)\ge\sqrt2\); there are \(2k\)
squared factors, and the denominator is at most \(4k\).
Every intermediate lowering and raising arrow remains within
the literal cap. The input and output in (15) have equal binomial
norms, since their two occupations are exchanged. Consequently
in either metric
\[
 \|L_N(1)\|_{\rm op}
       \ge \frac{2^{(N-1)/2}}{N-1},
 \qquad N\equiv1\pmod4,\quad N\ge5.
 \tag{16}
\]

Cauchy's inequality for the entire matrix function \(B_N(t,1)-I\)
on the circle of radius \(1/N\) now gives
\[
 \sup_{|t|=1/N}\|B_N(t,1)-I\|_{\rm op}
 \ \ge\ \frac{\|L_N(1)\|_{\rm op}}N
 \ \ge\ \frac{2^{(N-1)/2}}{N(N-1)}.
 \tag{17}
\]
In particular, in either specified metric there do not exist fixed
constants \(A>0\), \(p\ge0\), \(C\ge0\), and \(t_0>0\) such that
\[
 \|B_N(t,1)\|_{\rm op}\le A N^p e^{CN|t|}
 \quad\text{for every sufficiently large }N
       \text{ and every }|t|\le t_0.
 \tag{18}
\]
Otherwise the left side of (17) would be at most \(AN^p e^C+1\).
The subsequence in (16) contradicts that bound.
The same contradiction applies if (18) is imposed directly on
\(B_N-I\). The assertion is about a fixed complex time disk;
it does not assert the corresponding lower bound along real time.
More precisely, for every fixed \(T>0\),
\[
 \liminf_{\substack{N\to\infty\\N\equiv1\ (4)}}
 \frac1N\log\sup_{|t|\le T}\|B_N(t,1)\|_{\rm op}
       \ge\frac{\log2}{2}.
 \tag{18a}
\]
Use (17) and \(\|B-I\|\le\|B\|+1\). Although \(B_N(0)=I\),
the exponential rate of this disk supremum cannot tend to zero
with its fixed positive radius.

There is also an explicit scalar distinction between matrix
invertibility and a uniform unit. In either metric let \(e_{\rm in}\)
and \(e_{\rm out}\) be the normalized input and output of (15), and
put \(v_N=(e_{\rm in}+e_{\rm out})/\sqrt2\). Since every positive
power of \(X\) transfers occupation in only one direction,
\[
 F_N(t):=\langle v_N,B_N(t,1)v_N\rangle
   =1+\tfrac12(B_N(t,1))_{{\rm out},{\rm in}}.
 \tag{18b}
\]
This polynomial has degree at most \(2k\) and
\(|F_N'(0)|\ge2^{2k}/(8k)\). Write its nonzero roots as
\(z_1,\ldots,z_D\), counted with multiplicity. Since \(F_N(0)=1\),
factoring gives \(F_N'(0)=-\sum_{\nu=1}^D z_\nu^{-1}\).
Thus at least one root obeys
\[
 |z_\nu|\le D/|F_N'(0)|\le16k^2\,2^{-2k}.
 \tag{18c}
\]
The matrix \(B_N\) remains invertible at that root. This is a
specified finite physical expectation, not a coherent geometric
packet or an original closing-source assertion.

## 4. The coarser bounded-time estimate that does survive

For each fixed \(T,\eta>0\), there is a constant \(C_{T,\eta}\),
independent of \(N\), such that in either metric
\[
 \sup_{\substack{|t|\le T\\|N\mu|\le\eta}}
      \bigl(\|B_N(t,e^\mu)\|_{\rm op}
            +\|B_N(t,e^\mu)^{-1}\|_{\rm op}\bigr)
       \le e^{C_{T,\eta}N}.
 \tag{19}
\]
Harmless constants can be absorbed by increasing the exponential
constant for \(N\ge2\).

To prove this without a meridian-frame conditioning loss, first
bound the literal arrows. At the root their Euclidean norms are
at most \(2\). In the binomial metric the normalized \(E\) arrow
has modulus
\[
 |1-Q^a|\sqrt{(N-a)/a}
 \le (2\pi/N)\sqrt{a(N-a)}\le\pi.
 \]
For \(F\), write \(j=a+1\); its modulus is
\(|1-Q^j|\sqrt{j/(N-j)}\le\pi\), using
\(\sin(\pi j/N)\le\pi(N-j)/N\).
The unweighted lowering shift \(Lw_a=w_{a-1}\) has norms
\(1\) and \(\sqrt{N-1}\), respectively. Since exactly
\[
 E(M)=M E(1)+(M-M^{-1})L,
 \tag{20}
\]
and \(|M-M^{-1}|\le C_\eta/N\) on the stated collar,
\(\|X(M)\|_{\rm op}\le C_\eta\) in both metrics, uniformly in \(N\).
The bottom of \(L\) is zero.

Fix \(0<\rho<1\), and consider the scalar polynomial
\[
 \ell_N(z)=-\sum_{n=1}^{d}\frac{q^n z^n}{n(1-Q^n)}.
 \]
On \(|z|=\rho\) it has modulus at most \(C_\rho N\).
For \(n\le N/2\), use \(|1-Q^n|\ge4n/N\) and sum
\((N/4)\sum \rho^n/n^2\). For \(n>N/2\), use
\(|1-Q^n|\ge4(N-n)/N\); that part is bounded by
\(\frac12\rho^{N/2}\sum_{j<N}j^{-1}\).
Thus the Taylor coefficients of the entire scalar function
\(\exp(t\ell_N(z))=\sum_{n\ge0}b_{n,N}(t)z^n\) satisfy
\[
 |b_{n,N}(t)|\le \rho^{-n}e^{TC_\rho N}
       \quad (|t|\le T).
 \tag{21}
\]
Nilpotence makes the matrix substitution exactly
\[
 B_N(t,M)=\sum_{n=0}^{d}b_{n,N}(t)X(M)^n.
 \]
Applying (21) and summing the finite geometric majorant
\(\sum_{n<N}(C_\eta/\rho)^n\) proves (19); use \(-t\) for
the inverse. No infinite series in a non-small matrix was used.

The family is holomorphic in \(t\) and \(\mu\). On smaller buffered
time disks and scaled meridian collars, Cauchy's inequalities give,
for every fixed \(j,\ell\),
\[
 \|\partial_t^j\partial_\mu^\ell B_N(t,e^\mu)\|_{\rm op}
 +\|\partial_t^j\partial_\mu^\ell B_N(t,e^\mu)^{-1}\|_{\rm op}
       \le C_{j,\ell}N^\ell e^{C N}.
 \tag{22}
\]
These are the true fixed-\(q\) derivatives of the capped arrows (9).
They do not omit the moving meridian dependence of a crossing,
seed, or source coupon.

The coefficient recovery in (21) has an exponential cost even
when \(t\) is small; (17) proves that a uniform replacement by
(18) is impossible. In contrast, small Euler activity replaces
\(X^n\) by \(\lambda^nX^n\), damping high transfer degrees.
Differentiating fractional time at zero retains every term of
(12) at first order. These are different analytic regimes.

## 5. Consequence for whole-word continuation, and coverage

An initialized ordinary polynomial can pass through a finite
Fourier seam by (7) with its exact source adapter (5).
One cannot infer a local unit for an uninitialized crossing
from that fact, from finite matrix invertibility, or from
splitting (13) into \(O(N)\) small complex-time pieces and
postulating polynomial step norms. Equations (15)--(18) disprove
that last norm postulate for the actual physical Euler factor.
They do not prove a zero of the physical crossing at \(t=1\),
exclude a selected nonlower coherent chart, or decide the
coefficient of a faithful point in the original closing cycle.

The exact seam principle and one-port profile propagation are
already covered by
[actual Fourier port polynomials and profiles](actual_fourier_port_polynomials_and_profiles.md).
That is a coverage reference, not an imported proof here.
Re-evaluating the entire physical polynomial does not license
the simultaneous raw four-full-\(\Psi\) continuation discussed
there. The meridian argument-shift adapter in
[the Euler half-step note](actual_euler_meridian_half_step.md)
is a different family from (13). The new quantitative assertion
is the literal two-metric fractional-time test (15)--(18c),
together with its compatible finite upper bound (19).

## Complete proof direct

* F: [actual meridian source frames](research_actual_meridian_source_frames.md),
  506 lines, SHA256
  6f58fba195ba5e8208e1d5180a1d684b933f9f5d50eb28efc56609580fe29976.

The entire matching final and complete F were freshly read
nontruncated in this author sequence; every used implication was
checked, and both hashes were renewed at author freeze.
Only written mathematics and text/hash operations were used;
no mathematical programs, tests, or builds were run.
Frozen notes and the progress ledger were not edited.
