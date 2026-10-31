# A real-root preserving q-derivative on the original protected-Green degree range

31 October 2026. analytical research theorem.
The theorem below gives new positive structure for the FULL
spectator polynomial. It does not claim that truncation preserves roots,
that the full polynomial is integrable against the Green moment law, or
that the original signed coefficient is bounded by \(\Phi_D\).

## 1. The exact finite operator

Put \(N\ge3\), \(\theta=\pi/N\), \(q=e^{i\theta}\), \(s_j=2\sin(j\theta)\), and
\(S_a=\prod_{j=1}^a s_j\). Let \(0\le a<N\) and \(D=N+a-1\). On polynomials define

\[
\begin{gathered}
E=z\frac{d}{dz},\qquad
\partial_qP(z)=\frac{P(qz)-P(q^{-1}z)}{iz},\\
\partial_qz^k=s_kz^{k-1}.
\end{gathered}\tag{1}
\]

The removable value at z=0 is understood polynomially. Thus

\[
\partial_q^aP(z)
=\sum_{k\ge a}p_k\left(\prod_{j=0}^{a-1}s_{k-j}\right)z^{k-a}.
\tag{2}
\]

Terms with k<a are zero. Terms with N<=k<=N+a-1 are also EXACTLY
zero, since their product contains s_N. No limiting sine quotient is
used. For a<=k<=N-1 all factors in (2) are strictly positive.

**Theorem.** If \(P\) is a real polynomial of degree at most \(D\) with nonnegative
coefficients and all its zeros nonpositive real, then \(\partial_q^aP\) is
either zero or has nonnegative coefficients and all its zeros nonpositive
real. Its degree is at most \(N-a-1\).

This theorem concerns the compound a-th derivative. The intermediate
single q-derivatives need not preserve nonpositive roots once the degree
exceeds N. A zero output is possible, for example P=z^D when a>0.

## 2. Elementary proof by Euler's sine product

We first record two ordinary operations on the cone of nonnegative
polynomials with nonpositive real zeros.

* Ordinary differentiation, multiplication by z, and fixed-degree
  reversal \(\operatorname{Rev}_DP(z)=z^DP(1/z)\) preserve this cone, or give zero.
  Reversal is allowed when degree P<D, in which case it adds zeros at 0.
* For r<0, E-r preserves this cone. For r>D, r-E also preserves it
  on degree-at-most-D polynomials.

Here is a self-contained verification of the second assertion. For
c>0 and a polynomial P whose d zeros are distinct and strictly negative,
the derivative of t^c P(-t) has at least one positive zero between 0
and its first positive zero, and between each consecutive pair of its
positive zeros. Its nontrivial polynomial factor is
c P(-t)+t d/dt P(-t), of degree d. Thus cP+EP has all its d roots
negative and has nonnegative coefficients. Repeated or zero roots follow
by perturbing the roots and taking coefficient limits. Finally

\[
\operatorname{Rev}_D(r-E)P
=(r-D+E)\operatorname{Rev}_DP.\tag{3}
\]

which proves the assertion for r>D. This proof retains all polynomial
degrees; there is no assumption about a quantum inner product.

The bottom and top multiplier blocks are respectively

\[
\begin{aligned}
B_a(E)&=\prod_{j=0}^{a-1}(E-j)=z^a\partial_z^a,\\
T_a(E)&=\prod_{j=0}^{a-1}(N+j-E)
=\operatorname{Rev}_D B_a(E)\operatorname{Rev}_D.
\end{aligned}\tag{4}
\]

Each WHOLE block preserves the cone. Individual factors of T_a or
B_a whose zero lies inside [0,D] are not being asserted to do so.
The two blocks commute, being polynomials in E.

For k in the finite set {0,...,D}, Euler's sine product gives

\[
\begin{aligned}
\prod_{j=0}^{a-1}s_{k-j}
&=\left(\frac{2\pi}{N^2}\right)^a
 \prod_{j=0}^{a-1}(k-j)(N+j-k)
 \prod_{j=0}^{a-1}\left(1+\frac{k-j}{N}\right)\\
&\quad\cdot
 \prod_{n=2}^{\infty}\prod_{j=0}^{a-1}
 \left(1-\frac{k-j}{nN}\right)
 \left(1+\frac{k-j}{nN}\right).
\end{aligned}\tag{5}
\]

The identities at the zero coefficients hold by the same entire-function
product, without division by those zero factors. All remaining linear
factors have their roots OUTSIDE [0,D]: the n=1 root is j-N<0;
for n>=2 the roots are j-nN<0 and j+nN>D. The last strict inequality
uses a<N. Thus each finite product of the remaining factors, applied
as a polynomial in E after the two blocks in (4), preserves the cone.
Every coefficient multiplier in its nonzero range is positive.

The paired infinite product converges for each k, hence uniformly on
the finite coefficient set. The limit polynomial is therefore in the
same closed cone, or zero. For completeness, its closedness follows
by polynomial convergence and Hurwitz on each compact subset off the
nonpositive real axis; degree loss can only send roots to infinity.
Formula (5) says the limiting polynomial is exactly

\[
z^a\partial_q^aP(z).\tag{6}
\]

Removing its forced z^a proves the theorem. The support and degree
claims follow directly from (2). For a=0 the assertion is the identity
operator and the empty products are one.

No finite numerical sample, scalar orthogonal-polynomial identification,
or external multiplier-sequence theorem is needed in this proof.

## 3. The original odd endpoint spectator really satisfies the hypotheses

Consider an original simple marked source with R ports, R ordinary face
variables and two protected variables. Let a selected Green coupon have
ordered faces (x,b,c,y), with y protected and x,b,c distinct ordinary
faces. Assume every other coupon is its actual CROSS endpoint at sigma=-2.
We do not change any source diagram, matching, mark, or face demand.

At odd N=2k+1, d=N-1 and M=k-1. The exact endpoint coupon is

\[
\begin{aligned}
P_{e,\mathrm{CROSS}}(-2)
 &=N^2D_k(x_e,b_e,y_e)D_k(x_e,c_e,y_e),\\
D_k(x,b,y)&=\det\left[bI+\frac{x}{2}H_-+\frac{y}{2}H_+\right].
\end{aligned}\tag{7}
\]

after removal of its fixed common raw unit sign. The physical matrices
H_-,H_+ are positive-definite Hermitian. For variables with positive
imaginary parts, the imaginary part of the matrix in (7) is positive
definite. Its determinant is nonzero, so each factor is real stable.
It has nonnegative coefficients by its positive mixed-minor expansion.

Products and identification of shared variables preserve real stability.
Derivatives and specialization of variables to a real boundary value
preserve it or give zero; these follow by the one-variable Gauss--Lucas
argument, approximation from the upper half-plane and Hurwitz. In
particular extraction of any fixed nonnegative power, performed as a
derivative followed by specialization at 0, is allowed. All protected
variables are specialized to0 before extraction.

Let the exact residual spectator be

\[
P(x,b,c)=
\left[\prod_{\substack{f\ \mathrm{ordinary}\\f\notin\{x,b,c\}}}L_f^d\right]
\prod_{e\ne\mathrm{Green}}P_{e,\mathrm{CROSS}}(-2;L).
\tag{8}
\]

It is zero or a nonnegative real-stable polynomial, homogeneous of
degree 2d: (R-1)d-(R-3)d=2d. Its full coefficients retain every shared
ordinary target already extracted in (8). There is no independent
optimization of different occurrences of a face.

At the original lower node a<=M the input determinant has expansion

\[
D_a(x,b,0)=\sum_{v=0}^a d_{a,v}x^{a-v}b^v,
\qquad d_{a,v}\ge0.\tag{9}
\]

For each v define the actual binary residual

\[
P_v(x,c)=[b^{d-v}]P(x,b,c).\tag{10}
\]

It has degree d+v=N+v-1, not degree d in general. It is zero or
nonnegative real stable. Consequently P_v(1,z) has only nonpositive
real roots, including possible zero roots; this follows from real
coefficients, upper-half-plane nonvanishing, and coefficient positivity.
Since \(v\le a\), its degree is at most \(N+a-1\), exactly the range of the theorem.
Thus each FULL polynomial

\[
Q_v(z)=\partial_q^aP_v(1,z).\tag{11}
\]

is zero or nonnegative and negative-rooted, with degree at most \(N-a-1\).

There is a stronger combined statement: include the ACTUAL input
determinant before extracting the b target. Define

\[
\begin{aligned}
F_a(x,c)&=[b^d]D_a(x,b,0)P(x,b,c)\\
&=\sum_{v=0}^a d_{a,v}x^{a-v}P_v(x,c).
\end{aligned}\tag{11a}
\]

Both factors before this extraction are real stable, so F_a is zero
or a nonnegative real-stable binary polynomial. Its degree is exactly
d+a=N+a-1 when it is nonzero. Therefore the SINGLE full polynomial

\[
Q_a(z)=\partial_q^aF_a(1,z).\tag{11b}
\]

is zero or negative-rooted with nonnegative coefficients. This combines
all input b-loads with their original weights; it is not an unsupported
assertion that an arbitrary positive sum of stable polynomials stays
stable. The multiplication and coefficient extraction in (11a) prove
the required stability directly.

This is a genuine original-source statement for arbitrary valence of
the selected Green faces: no two-port internal-demand reduction is
used. It does require the stated CROSS endpoint exterior. An unextracted
fan can have larger c degree; adding arbitrary signed exterior coupons
need not preserve real stability. No assertion about that broader
maximal-component situation follows from (11).

The same reasoning works whenever an actual protected-source extraction
has the stated degree bound and stable exterior. If b is also protected,
only v=0 remains and the direct two-variable degree count gives d;
this optional specialization adds no new moment or spectral claim.

## 4. Exact Green pairing and the two surviving cutoff issues

For the source variables and node above, keep the original Green law
X=X_(N,a), m=M-a, and the original total cutoff in the parent degree c.
Its exact moments are

\[
\begin{gathered}
\mathbb E X^r=A_r=
\prod_{i=1}^r\frac{s_{a+i}}{s_{2a+i+1}},
\qquad r\in\{0,\ldots,m\},\\
\mathbb E X^t<\infty
\quad\Longleftrightarrow\quad -a-1<t<N-2a-1.
\end{gathered}\tag{12}
\]

The real interval in (12) is the OPEN Mellin domain; integer moments
used by the original source have 0<=r<=m. In the protected outer case,
the original sine-binomial identity gives

\[
H_r(W_a(x,0))=B_a(r)x^r,\qquad
B_a(r)=\frac{S_{a+r}}{S_aS_r}.
\]

Here \(P_{v,\le M}\) truncates \(P_v(1,z)\) in \(z\); later \(F_{a,\le M}\)
likewise truncates \(F_a(1,z)\). The normalized original pairing obeys exactly

\[
\begin{aligned}
\mathcal L_a(P_v)
&=\sum_{r=0}^m(-1)^rA_rB_a(r)[z^{a+r}]P_v(1,z)\\
&=\frac1{S_a}\mathbb E\!\left[
 \partial_q^a(P_{v,\le M})(-X)\right].
\end{aligned}\tag{13}
\]

The b and x degree targets have not disappeared: after the term
x^(a-v)b^v in (9), the b target is exactly (10); homogeneity of P_v
makes every term in (13) have total x degree d. Thus, with all original
ordinary demands imposed, the normalized nodal Green/CROSS coefficient is

\[
\begin{gathered}
\mathcal B_{a,N}=(-1)^m\gamma_{N,a}
 \sum_{v=0}^a d_{a,v}\mathcal L_a(P_v),\\
\gamma_{N,a}=\frac{N}{s_{2a+1}s_{m+1}},
\qquad N\ \mathrm{odd}.
\end{gathered}\tag{14}
\]

Equivalently, using the single actual stable polynomial (11a),

\[
\mathcal B_{a,N}
=\frac{(-1)^m\gamma_{N,a}}{S_a}
 \mathbb E\!\left[\partial_q^a(F_{a,\le M})(-X)\right].
\tag{14a}
\]

All input determinant coefficients have been included in F_a. The
factor 1/S_a is exact and can have exponential size; it is not absorbed
into the polynomially bounded gamma.

This is the already fixed original nodal block normalization
\(R_aD_{a,m}=\gamma_{N,a}D_a\). The common raw source sign and the UNUSED
Green scalar \(\zeta_N(u)\), present when the nodal block is interpolated
back into the original numerator, remain outside this displayed block.
Equation (14) does not evaluate or cancel that scalar at a sampled zero.

Although Q_v in (11) is negative-rooted, the polynomial in (13) is
its initial degree segment:

\[
\partial_q^a(P_{v,\le M})(z)
=Q_v(z)-\sum_{s=M+1}^{N-1}
 \bigl([z^s]P_v(1,z)\bigr)
 \frac{S_s}{S_{s-a}}z^{s-a}.
\tag{15}
\]

Terms absent from the actual P_v are zero. Thus the upper band
N<=s<=N+a-1 vanishes for algebraic reasons, but the ACTUAL cutoff
current M<s<N remains. Truncation can destroy negative-rootedness;
no root claim is made for the left side of (15).

Nor can (15) be integrated termwise after dropping the cutoff.
Its full degree can be N-a-1, whereas the moment threshold in (12)
is N-2a-1. Some currents therefore need unavailable moments, even
though every term in the original truncated (13) is integrable.
For a=0 the top degree N-1 is itself at the excluded threshold.
The identity is a polynomial identity at finite X, not a license
for subtracting divergent expectations.

The same exact cutoff identity and moment warning apply to the combined
F_a,Q_a in (11a)--(14a); this is the version retaining the entire input
polynomial before any absolute value.

## 5. A genuine full-polynomial phase identity, with its exact limitation

If the combined \(Q_a\) is nonzero, write \(Q_a(z)=Kz^\ell\prod_j(z+\lambda_j)\),
where \(\lambda_j>0\) and \(K>0\). For any \(r>0\) put \(p_j=r/(r+\lambda_j)\).
Then its actual phase ratio is exactly

\[
\begin{aligned}
\frac{|Q_a(re^{i\phi})|}{Q_a(r)}
&=\prod_j\left[1-4p_j(1-p_j)\sin^2(\phi/2)\right]^{1/2}\\
&\le \exp\left[-2\sin^2(\phi/2)\sum_jp_j(1-p_j)\right].
\end{aligned}\tag{16}
\]

The zero-root monomial has modulus one in this ratio. The variance is
also exactly

\[
\left(r\frac{\partial}{\partial r}\right)^2\log Q_a(r)
=\sum_jp_j(1-p_j).\tag{17}
\]

In particular the negative-axis value admits a genuine factor-by-factor
cancellation formula, before any absolute value is taken on its
coefficients. This uses the SAME actual fully extracted polynomial,
not an independently chosen positive majorant.

Equations (15) and (12) are the precise remaining obstacles to using
(16) inside the original Green expectation. In addition, no uniform
order-N lower bound on (17) has been proved from the original exterior
constraints. Thus the theorem establishes a general actual-source
positive structure, but neither an absolute \(\Phi_D\) bound nor a signed
Green contraction.

## Inputs

The [original odd endpoint product](actual_cross_cofactor_factorization.md),
sections 2–3, supplies (7). The [physical positive matrices](actual_q_hahn_boundary_model_curvature.md),
sections 1 and 3, supply the determinant stability. The
[original maximal-Green block](research_maximal_green_component_block_transport.md),
sections 4–5, retains the unused scalar and exact targets. The
[sine-binomial and moment theorem](research_green_tail_sine_binomial_moment_transform.md)
supplies the finite signed kernel and exact Mellin domain. The
[original algebraic period](research_green_tail_algebraic_period_and_mellin_rate.md),
sections 2–3, supplies the complete scalar and coefficient pairing.

The theorem concerns exact real-root structure with the stated zero bands, original targets, Mellin cutoff and phase. It does not assert an asymptotic coefficient theorem.
