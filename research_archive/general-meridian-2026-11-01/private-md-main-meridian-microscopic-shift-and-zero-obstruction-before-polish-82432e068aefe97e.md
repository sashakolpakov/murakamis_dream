# The actual complete-point shift ratio and nearby zeros

31 October 2026. Private mathematical continuation. This strengthens the
already recorded obstruction to a uniform main-meridian WKB expression
for the reduced ADO state. It uses the now-proved positive volume rate,
the exact ordinary-color anchor, and an explicit degree bound from the
original finite crossing matrices. It does not construct a replacement
knot invariant or identify a classical A-polynomial factor.

## 1. The state and the exact microscopic shift

Fix a zero-framed knot K for which the actual all-level theorem gives

\[
 q_N=e^{\pi i/N},\qquad
 \frac1N\log|K_N(K)|\longrightarrow v=\frac{V}{2\pi}>0.
 \tag{1}
\]
This includes the covered strict long-twist knots and the knots obtained
from them by the ordered net-weight normalization. The knot and all
integer twist weights are fixed before N grows.

Let F_N(M) be the actual reduced literature ADO state, in the marked
coordinate

\[
 x=q_N^\alpha,\qquad M=-q_Nx.
 \tag{2}
\]
The actual quotient-color theorem states

\[
 F_N(-q_N^j)=C_j(q_N),\quad 1\le j\le N,\qquad
 F_N(1)=K_N(K),\qquad C_1(q)=1.
 \tag{3}
\]
Here F_N is the reduced, zero-framed state. It is not an unnormalized
state, and no crossing Cartan or framing monomial is omitted from it.

The source proof in `notes/even_meridian_norm_descent.md`, Sections 1--2,
gives, at every level and both parities,

\[
 F_N(-M)=F_N(M).
 \tag{4}
\]
For specificity, its exact insertion is a function of Y=M^2, and its
N-fold cyclic norm is one. The residual framing exponent there is
\(\kappa_D=w-b+1\), which is even for a b-strand braid closing to a
knot: its permutation has sign \((-1)^{b-1}=(-1)^w\). Thus the framing
norm \(q_N^{-N\kappa_D}=(-1)^{\kappa_D}\) equals one. Alternatively,
the source's exponent of x is even term by term after the conserved
position coboundary is summed. This is the precise reason that (4)
has no additional sign. It applies to the zero-framed reduced state,
not to the full modified state, whose parity is different at even N.

Combining (3)--(4) proves the actual identity

\[
 F_N(q_N)=F_N(-q_N)=1,
 \qquad
 \frac{F_N(q_N)}{F_N(1)}=\frac1{K_N(K)}.
 \tag{5}
\]
The denominator is nonzero for all sufficiently large N by (1). Hence

\[
 \lim_{N\to\infty}\frac1N
     \log\left|\frac{F_N(q_N)}{F_N(1)}\right|=-v.
 \tag{6}
\]
The shift in (5) is the genuine meridian shift M->q_N M. In squared
coordinates, writing \(f_N(Y)=F_N(M)\), it is Y->Q_NY with
\(Q_N=q_N^2\), and \(f_N(Q_N)=1\). There is no parity exception.

The qualitative failure of a uniform nonzero WKB amplitude across these
two points was already explained in `regularized_kashaev_period.md`,
Section 7, and `formal_a_curve_period_torsor.md`, Section 3. Equation
(6) supplies its exact exponential rate for the knots now covered by
the volume theorem. Sections 2--3 give a further quantitative consequence
for the zeros of the actual Laurent polynomial.

## 2. An explicit linear Laurent-degree bound

Choose any fixed braid presentation of K with b strands and L crossings.
Let L_+ and L_- count its positive and negative crossings, so
\(L=L_++L_-\) and \(w=L_+-L_-\). Put d=N-1.

Use precisely the finite lift of `finite_sum_annihilator.md`, Section 1.
After removing the common Cartan scalar, the positive crossing is
\(\widetilde R=D\Theta\), where the diagonal D has x-power
\(x^{-a-b}\). A nonzero summand of \(\Theta\) shifts an input (a,b)
to (a-k,b+k), with

\[
 0\le a,b\le d,\qquad 0\le k\le\min(a,d-b).
 \tag{7}
\]
The product of k unrolled E factors has Laurent x-exponents between
-k and k. The diagonal sees the same conserved sum a+b before and
after the shift. Thus every positive crossing entry has exponents in

\[
 [-a-b-k,-a-b+k]\subset[-2d,0].
 \tag{8}
\]
Indeed a+b+k<=2d follows from k<=d-b, and -a-b+k<=0 follows
from k<=a. The actual inverse is \(\Theta^{-1}D^{-1}\), with the same
allowed shifts and the same x-degree range of its E factors. Every
negative crossing entry therefore has exponents in

\[
 [a+b-k,a+b+k]\subset[0,2d].
 \tag{9}
\]
Permutation and transpose conventions only permute these entries.
There is no denominator depending on x in this matrix formula: the
factorial denominators depend on q and are nonzero at q_N. Products,
sums and the finite trace cannot enlarge the resulting exponent interval.

The residual zero-framing factor is x^(wd). Each of the b-1 pivotal
traces contributes the same x-power x^(-d); its remaining dependence
on the head index is a power of q. Thus the full fixed shift is
x^(d(w-b+1)). Combining it with (8)--(9) puts the support of F_N in

\[
 [-d(L+b-1),\ d(L-b+1)].
 \tag{10}
\]
The substitution x=-q_N^{-1}M multiplies coefficients by nonzero scalars
and leaves this exponent interval unchanged. The removed common Cartan
was already canceled by the exact zero-framing normalization; it must
not be inserted a second time into (10).

Let m_N and n_N be the least and greatest actual nonzero Laurent
exponents after any cancellations. Then

\[
 D_N=n_N-m_N\le 2L(N-1).
 \tag{11}
\]
This bound is for the actual reduced state and holds at every level.
The number of state-sum terms need not be bounded to prove it.
By (4), all actual exponents are even, so the corresponding Laurent
spread in Y=M^2 obeys

\[
 D_N^{Y}\le L(N-1).
 \tag{12}
\]
For a positive-volume knot L>0. Also D_N>0 for all sufficiently large
N: a Laurent monomial has equal modulus at 1 and q_N and cannot satisfy
(1) and (5).

## 3. Actual zeros approach the complete point at distance O(1/N)

Define

\[
 \delta_N=|q_N-1|=2\sin\frac{\pi}{2N},\qquad
 r_N=\min\{|z-1|: F_N(z)=0,\ z\ne0\}.
 \tag{13}
\]
For sufficiently large N the zero set in (13) is nonempty. Indeed
\(P_N(M)=M^{-m_N}F_N(M)\) is a degree-D_N polynomial with nonzero
constant term and D_N>0. Neither 1 nor q_N is a root.

Factor P_N with multiplicities as \(a_N\prod_{j=1}^{D_N}(M-z_j)\).
Since |q_N|=1, the Laurent monomial has exactly unit modulus between
the two evaluation points. If r_N>delta_N, the triangle inequality gives

\[
 \begin{aligned}
 \log\left|\frac{F_N(q_N)}{F_N(1)}\right|
 &=\sum_{j=1}^{D_N}\log\frac{|q_N-z_j|}{|1-z_j|}\\
 &\ge D_N\log\left(1-\frac{\delta_N}{r_N}\right).
 \end{aligned}
 \tag{14}
\]
There is no generic-position or simple-root assumption. By (5), the
left side is -log|K_N|. Solving (14) yields

\[
 r_N\le
 \frac{\delta_N}{1-|K_N|^{-1/D_N}}
 \le\frac{\delta_N}{1-|K_N|^{-1/[2L(N-1)]}}.
 \tag{15}
\]
If r_N<=delta_N, the second bound in (15) holds automatically, because
|K_N|>1 for large N. Thus it is an unconditional eventual bound.
Using (1), (15) implies

\[
 \limsup_{N\to\infty} N r_N
 \le \frac{\pi}{1-\exp(-V/(4\pi L))}.
 \tag{16}
\]
This is a proof about zeros of the actual knot state, not an artificial
family having the same scalar growth.

The exact squared-meridian descent improves the displayed constant.
Apply the same argument to f_N(Y), the point Q_N, and the degree bound
(12). A zero \(\zeta_N\) satisfies

\[
 \limsup N|\zeta_N-1|
 \le\frac{2\pi}{1-\exp(-V/(2\pi L))}.
 \tag{17}
\]
Choose its square root z_N near 1. Evenness says that this is a zero of
F_N, and
\(|z_N-1|=|\zeta_N-1|/|z_N+1|\), with \(|z_N+1|\to2\).
Consequently

\[
 \boxed{\displaystyle
 \limsup_{N\to\infty} N r_N
 \le \frac{\pi}{1-\exp(-V/(2\pi L))}.}
 \tag{18}
\]
Any fixed braid presentation gives a valid L in these bounds; the proof
does not require a minimal-crossing presentation. The statements do not
count the zeros in this shrinking disk, describe their limiting angles,
or identify their algebraic factors with the classical A-polynomial.

## 4. What this rules out, including the full normalization

There cannot be a fixed complex neighborhood U of M=1 on which every
sufficiently large F_N is nonvanishing. Thus the unrevised sufficient
ratio premise in Section 3 of the private main-meridian interface note,
when U contains the complete point, is impossible for the actual reduced
state with positive volume. Already (5)--(6) exclude a nonzero finite
limit for its one-step ratio at 1. The zero theorem strengthens that
pointwise contradiction to failure of any fixed zero-free neighborhood.
The same conditional ratio lemma remains correct on another domain;
its premise at the complete point must not be assumed for F_N.

A scalar normalization independent of M does not change the ratio in
(5) or any zero. Nor does a fixed rational/algebraic gauge that is a
holomorphic nonzero unit on a common neighborhood of (q,M)=(1,1):
its ratio at the two points tends to one, and it cannot remove the
zeros in (18). A gauge with moving zeros or poles requires its whole
lattice and normalization to be retained; it is not covered by this
unit assertion.

In particular the actual full modified factor is not such a unit:

\[
 d_N(M)=\eta_N\frac{M-M^{-1}}{M^N-M^{-N}},\qquad
 \eta_N=i^{N+3},\qquad d_N(1)=\eta_N/N.
 \tag{19}
\]
At M=q_N it has a simple pole. Since F_N(q_N)=1, that pole is not
canceled in \(\mathcal N_N=d_NF_N\). Its exact residue is

\[
 \operatorname{Res}_{M=q_N}\mathcal N_N(M)
   =\frac{\eta_N(1-q_N^2)}{2N}\ne0.
 \tag{20}
\]
Indeed the denominator derivative at q_N is -2N q_N^{-1}.
This works at every N>=2 and both parities. The complete value remains
\(\eta_N K_N/N\), finite and exponentially large. Thus the full-state
normalization does not furnish a uniformly holomorphic nonzero scalar
packet across the complete point and its first shifted point either.
Its shift quotient is meromorphic, with a pole at M=1 for each
sufficiently large level. This matches the exact gauge
\(-q_N^{-1}(q_N^2M^2-1)/(M^2-1)\); no sign was discarded.

## 5. The regularized affine state is the remaining candidate

The existing regular-period theorem supplies a canonical correction,
not an arbitrary scalar normalization. With Y=M^2, let P_N^ord be the
unique degree-at-most-N-2 polynomial matching the ordinary orbit values
at Q_N^j, 1<=j<N. Then

\[
 S_N(Y)=\frac{Y^N-1}{Y-1},\qquad
 R_N^{reg}(Y)=\frac{f_N(Y)-P_N^{ord}(Y)}{S_N(Y)}.
 \tag{21}
\]
This is a Laurent polynomial. The ordinary-color bound gives
\(P_N^{ord}(1)/N=O_K(N^{b-1})\), and hence

\[
 R_N^{reg}(1)=K_N/N-P_N^{ord}(1)/N,
 \qquad \frac1N\log|R_N^{reg}(1)|\longrightarrow v.
 \tag{22}
\]
There is no fixed ordinary-color anchor for R_N^reg(Q_N): it depends
on meridian derivatives of the original f_N and P_N^ord. The exact
obstruction (5) has therefore not been transferred to this regular
state. Neither has a uniform shift-ratio theorem been proved for it.

A specified all-level annihilator gives the existing rootwise affine
recurrence \(A_N R_N^{reg}=b_N\), after its recorded rational gauge
and denominator clearing. Its source b_N has fixed Laurent support
and polynomially bounded coefficients. A sufficient next statement
would be a fixed-domain, nonzero geometric shift-ratio limit for this
actual regular state, together with a locally uniform exponential
lower bound making b_N/R_N^reg tend to zero. Dividing the finite affine
equation by R_N^reg would then give its homogeneous classical symbol
on the limiting ratio. The preferred longitude, gauge and source
would still have to be identified. Equation (22) alone supplies none
of those neighborhood estimates.

This continuation preserves the complete scalar volume theorem and
the pointed quantum A-period/Gram formulations. It corrects the choice
of candidate for a complete-point scalar WKB or shift-ratio theorem:
the actual reduced F_N has an exponential one-step drop and nearby
zeros; the actual full state has nearby poles. Their canonical regular
affine component is a different, explicitly sourced object.
