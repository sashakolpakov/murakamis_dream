# Unipotent transport of the actual q-Hahn normal near the fold

Written proof, 24 November 2026.

The actual q-Hahn source has an exact constant column at magnetic input
zero. This supplies a value/difference form of its channel recurrence.
After a real rescaling of the difference, the nonresonant transfers
are close to the identity in operator norm. Their accumulated cost is
quadratic in the scaled channel separation.

All columns and normal derivatives below retain the original generic
highest-weight \(N-1\) source. The result is a relative upper bound for
its paired normal, not a nonzero leading amplitude or a closed-source
lower bound.

## 1. The source, the normal, and the bound

Let \(N\ge3\), \(d=N-1\), \(q_0=e^{\pi i/N}\), and take actual integers
\[
 0\le j<l,\qquad j+l=d,\qquad s=l-j.
 \tag{1}
\]
Set \(q=q_0e^\epsilon\), with \(\log q=\pi i/N+\epsilon\), and write
\[
 Q=q^2,\quad B=Q^{-N},\quad x=q^d,\quad
 t=N\tau,\quad u=N\nu,\quad T=Q^t,\quad
 \sigma=q^t,\quad X=Q^{-u},\quad z=\sigma Q^{-u}.
 \tag{2}
\]
The exact finite generic column is
\[
 C_m(q;t,u)=x^u\sum_{k=0}^m
 \frac{(Q^{-m};Q)_k(B^2Q^{m+1};Q)_k(X;Q)_kQ^k}
 {(BQ;Q)_k(T^{-1};Q)_k(Q;Q)_k},
 \quad (a;Q)_k=\prod_{r=0}^{k-1}(1-aQ^r).
 \tag{3}
\]
The original normal and its actual Casimir divisor are
\[
 w_{j,l}(t,u)=\frac{D C_j(q_0;t,u)-D C_l(q_0;t,u)}
 {-2N\Delta_j},\qquad
 D=q\partial_q,\qquad
 \Delta_j=q_0^{2j+1}-q_0^{-2j-1}.
 \tag{4}
\]
The derivative keeps \(N,t,u\) fixed and hence follows the actual
family \(B=Q^{-N}\), including the large partner.

Let
\[
 {\cal P}=\{(\tau,\nu)\in\mathbb C^2:
           \tfrac12<\Re\tau<1,\quad 0<\Re\nu<\Re\tau\}.
 \tag{5}
\]
**Theorem.** For every compact \(K\Subset{\cal P}\), there are
\(C_K\ge1\), \(A_K\ge0\), \(\eta_K>0\), and \(N_K\) such that
\[
 \boxed{\quad
 \left|\frac{w_{j,l}(N\tau,N\nu)}
 {C_j(q_0;N\tau,N\nu)}\right|
 \le C_K N^{A_K}
       \exp\!\left(C_K\frac{s^2}{N}\right)
 \quad}
 \tag{6}
\]
for \(N\ge N_K\), \(1\le s\le\eta_KN\), and \((\tau,\nu)\in K\).
The columns and normal are holomorphic near \(K\) at these levels,
and the denominator is nonzero.

In particular \(s\le M\sqrt N\), with fixed \(M\), has polynomial
relative cost. Every \(s=o(N)\) still has subexponential upper cost.
At a fixed \(0<\delta\le\eta_K\), the upper exponential cost for
\(s\le\delta N\) is at most \(C_K\delta^2\). This last statement
allows exponential growth at each fixed positive \(\delta\).

## 2. Exact recurrence and the constant source anchor

Keep the monic recurrence and its exact normalization from [F]:
\[
 C_m=x^u\frac{\sigma^m\kappa_m}{D_m(T)}R_m(z),\quad
 D_m(T)=\prod_{r=0}^{m-1}(T-Q^r),\quad
 \kappa_m=\frac{(B^2Q^{m+1};Q)_m}{(BQ;Q)_m},
 \tag{7}
\]
\[
 R_{n+1}=(z+\alpha_n)R_n+\beta_nR_{n-1}.
 \tag{8}
\]
The rational formulas and their full integer-degree justification are
given in [F, equations (9)--(10)], with the original proofs in [S,N].
The actual consecutive scalar ratio is
\[
 \rho_n=\frac{\kappa_{n+1}}{\kappa_n}
 =\frac{(1-B^2Q^{2n+1})(1-B^2Q^{2n+2})}
 {(1-B^2Q^{n+1})(1-BQ^{n+1})},\qquad
 a_n=\frac{\sigma\rho_n}{T-Q^n}.
 \tag{9}
\]
Thus the exact actual-column recurrence on the generic circle is
\[
 C_{n+1}=a_n(z+\alpha_n)C_n+
                  a_na_{n-1}\beta_nC_{n-1}.
 \tag{10}
\]
These coefficients depend on \(q,t\); their only magnetic dependence
in (10) is the displayed \(z\).

There is an additional exact normalization in (3):
\[
                      C_m(q;t,0)=1\quad\hbox{for every }m.
 \tag{11}
\]
Indeed \(X=1\) makes every summand with \(k\ge1\) vanish, and
\(x^0=1\). Substitution in (10), where now \(z=\sigma\), gives
\[
 a_n(\sigma+\alpha_n)+a_na_{n-1}\beta_n=1.
 \tag{12}
\]
This is a generic rational identity, prior to taking the root.
Define
\[
 \delta C_n=C_n-C_{n-1},\qquad
 \varepsilon_n=a_n(z-\sigma),\qquad
 b_n=a_n(\sigma+\alpha_n)-1=-a_na_{n-1}\beta_n.
 \tag{13}
\]
The value and its difference therefore obey exactly
\[
 \delta C_{n+1}=\varepsilon_n C_n+b_n\delta C_n,\qquad
 C_{n+1}=(1+\varepsilon_n)C_n+b_n\delta C_n.
 \tag{14}
\]
No root collision identity has been differentiated to obtain this
system. In particular (11) is not an assumed normalization of an
independent solution.

## 3. The source-specific unipotent estimate

Choose \(\eta_K\) and a slightly larger compact neighborhood as in [F],
with
\[
 0<\eta_K<\min\left(\tfrac14,\inf_K(\Re\tau-\tfrac12)\right).
 \tag{15}
\]
All estimates below are on the genuine generic circle
\(|\epsilon|=\varrho_N=c_KN^{-8}\).
For every integer \(n\), put
\[
 r_n=1+|2n-N|,\qquad
 {\cal B}_N=\{n:|2n-N|\le4\}.
 \tag{16}
\]
Among the used rows \(j\le n<l\), at most five are bad.
At every other used row [F] proves, on that circle,
\[
 |a_n|+|a_{n-1}|\le C_K(r_n/N)^2,\quad
 |\alpha_n|\le C_K(N/r_n)^2,\quad
 |\beta_n|\le C_K(N/r_n)^4.
 \tag{17}
\]
It follows immediately that
\(|\varepsilon_n|\le C_K(r_n/N)^2\).
The decisive improvement is the estimate for \(b_n-1\).

At the root \(B=1\), set \(y=Q_0^n\). The exact diagonal coefficient is
\[
 \alpha_n=
 -\frac{2(1+Q_0T)y}{\sigma(1+y)(1+Q_0y)}.
 \tag{18}
\]
This is the root formula of [S,F] at every nonresonant degree.
Combining it with (9), and canceling \(1-Q_0^2y^2\), gives
\[
 a_n\alpha_n=
 -\frac{2(1+Q_0T)y(1-Q_0y^2)}
 {(T-y)(1-Q_0y)(1+y)}.
 \tag{19}
\]
All denominators other than \(1+y\) stay uniformly separated from
zero in this near-fold range. Also
\(|1+y|\asymp r_n/N\) at a nonbad row.

In (19), replace \(Q_0\) by \(1\) while holding \(y,T\) fixed.
The result is \(-2(1+T)y/(T-y)\). Its difference from \(2\) is
\[
             -\frac{2T(1+y)}{T-y}=O_K(r_n/N).
 \tag{20}
\]
The error in this replacement is \(O_K(1/r_n)\):
\(|Q_0-1|=O(N^{-1})\), and the only small denominator is
\(1+y\). Explicitly,
\(1-Q_0y^2=(1-y^2)+(1-Q_0)y^2\); all remaining factors and their
differences have uniformly bounded denominators.
Since \(a_n\sigma=O_K((r_n/N)^2)\), equations (13),(19)--(20) give
the root estimate
\[
             |b_n(0)-1|
                  \le C_K(r_n/N+1/r_n).
 \tag{21}
\]

This estimate persists on the actual generic circle.
We use the generic quotient estimates, not a derivative of (18).
At a nonbad row they give
\[
 a_n'=O_K(N),\qquad \alpha_n=O_K(N^2),\qquad
 \alpha_n'=O_K(N^5),\qquad \sigma'=O_K(N)
 \tag{22}
\]
on the small disk; primes mean \(\partial_\epsilon\).
The factors \(a_n,\sigma\) are bounded there. Differentiating the
generic expression \(b_n=a_n(\sigma+\alpha_n)-1\) now gives
\(b_n'=O_K(N^5)\). Its change on the \(N^{-8}\) circle is
\(O_K(N^{-3})\), absorbed in (21).
We have consequently proved the uniform nonbad estimates
\[
 |\varepsilon_n|\le C_K(r_n/N)^2,\qquad
 |b_n-1|\le C_K(r_n/N+1/r_n).
 \tag{23}
\]
The real scale \(r_n\) records the degree's distance to the fold;
it does not change the complex magnetic variables.

## 4. A bounded value/difference frame

For every \(j\le n\le l\), define
\[
 h_n=\frac{r_n}{N}+\frac1{r_n},\qquad
 Y_n=\begin{pmatrix}C_n\\ \delta C_n/h_n\end{pmatrix}.
 \tag{24}
\]
These weights are positive and \(h_n\ge2/\sqrt N\).
Throughout the near-fold interval they are bounded above by a
fixed constant. The neighboring ratios satisfy
\[
 \max\left(\frac{h_n}{h_{n+1}},
           \frac{h_{n+1}}{h_n}\right)\le1+\frac{C}{r_n}.
 \tag{25}
\]
To check this directly, \(|r_{n+1}-r_n|\le2\), and their ratio is
between \(1/3\) and \(3\). For \(h(r)=r/N+1/r\),
\(|\partial_r\log h(r)|\le1/r\).
Integrating on an interval of length at most two proves the
individual bounds for \(r_n\ge3\); the finitely many values
\(r_n=1,2\) satisfy them after increasing the absolute constant.

In this frame (14) becomes the exact matrix equation
\[
 Y_{n+1}=
 \begin{pmatrix}
 1+\varepsilon_n&b_nh_n\\
 \varepsilon_n/h_{n+1}&b_nh_n/h_{n+1}
 \end{pmatrix}Y_n .
 \tag{26}
\]
At a nonbad row its induced maximum norm is at most
\[
                         1+C_Kh_n.
 \tag{27}
\]
Indeed the first absolute row sum is at most
\(1+|\varepsilon_n|+(1+C_Kh_n)h_n\).
For the second row, (23),(25) give
\[
 |\varepsilon_n|/h_{n+1}\le C_K r_n/N,\qquad
 |b_n|h_n/h_{n+1}\le(1+C_Kh_n)(1+C/r_n).
 \tag{28}
\]
Use \(r_n/N\le h_n\), \(1/r_n\le h_n\), and the uniform upper
bound for \(h_n\). Both row sums are then bounded by (27).
This argument allows arbitrary complex phases.

At a bad row \(r_n\le5\) and \(r_{n+1}\le7\), so both frame changes
are uniformly bounded. The original actual-column transfer from [F]
costs at most \(C_KN^{16}\) on the circle. The same safe bound
therefore holds in (26), with at most five such factors.

The full accumulated nonbad cost is controlled by
\[
 \sum_{n=j}^{l-1}h_n
       \le C\frac{s^2}{N}+C\bigl(1+\log(s+2)\bigr).
 \tag{29}
\]
For the first sum use \(r_n\le s+2\), so
\(\sum r_n/N\le s(s+2)/N\le3s^2/N\).
For the second, each positive integer value of \(r_n\) occurs at
most twice; hence \(\sum1/r_n\le2\sum_{m=1}^{s+2}1/m\).
This proves (29), with no loss proportional to \(s\).

## 5. Initial field, full-source Cauchy estimate, and scope

The full-physical determinant and its last inverse cofactor give
the initial bounds from [F, equations (16)--(17)]:
\[
 |C_j(q)/C_j(q_0)|\le C_K,\qquad
 |C_{j-1}(q)/C_j(q_0)|\le C_KN^2.
 \tag{30}
\]
They use the actual scalar ratio, whose initial inverse is
\(O_K(N^2)\), and the full-physical larger-entry freezing from [P].
Thus \(h_j^{-1}\le\sqrt N/2\) implies
\(\|Y_j/C_j(q_0)\|_\infty\le C_KN^3\).
Multiplying (26), using the at most five bad rows and (27),(29),
gives constants \(a_K,C_K\) such that
\[
 |C_l(q)/C_j(q_0)|
       \le C_KN^{a_K}\exp(C_Ks^2/N)
                  \quad (|\epsilon|=\varrho_N).
 \tag{31}
\]
The compact-dependent polynomial power includes the harmonic
factor \((s+2)^{C_K}\) in (29), besides the explicit initial and
bad-row powers. A universal numerical exponent is not asserted.

Apply Cauchy's formula to the full finite columns (3).
They are holomorphic throughout this disk: factorial indices
are less than \(N\), and (15) keeps all \(T\) divisors separated.
The singular monic factors have already canceled in that finite
source. The derivatives therefore cost only the additional
factor \(\varrho_N^{-1}=O_K(N^8)\). Finally
\(2N|\Delta_j|=4N\sin(\pi s/N)\ge8s\ge8\).
Together with the corresponding small-column derivative bound,
this proves (6), with a larger compact-dependent \(A_K\).

The previous source-normalized estimate [F] bounded each regular
transfer by a fixed constant. The exact source anchor (11), the
explicit root formula (19), and the weighted difference frame
instead retain its near-unipotent form. This is why the scaled
cost improves from linear to quadratic.

The closest flux rescaling in [V] concerns a different source:
a positive anchored four-coherent scalar on its physical half-grid.
It proves a terminal fold value and does not estimate this generic
q-Hahn derivative. Here no positivity of the column or of a flux
is assumed, and both generic partner derivatives remain in (4).

The theorem retains actual integer channels and both level parities.
It does not provide a complex-channel interpolation, a nonzero
normal amplitude, a bound for the complete contracted coupon, or
a contributing original geometric cycle. In particular polynomial
cost on the Gaussian channel scale does not prove that the needed
short-filled geometric configuration lies there, or that its
original cap projection is nonzero. No knot-volume lower bound
or finite-exception theorem is claimed.

The complete selected texts are:

| Label | Complete text | SHA256 |
| --- | --- | --- |
| F | [Source-normalized fold transport](research_q_hahn_source_normalized_fold_transport.md), 380 lines | 18a92c8fd3ccc93b5489476aaad1e5f0c9eed8001568ec431c259356db5f687f |
| S | [Actual small-channel generic normals](actual_q_hahn_small_channel_generic_normals.md), 261 lines | 9eaf5750927cacbc9ad3d5d3b3b75b883083d4cf16afa1ca21c03f6376a53fb4 |
| N | [Actual near-fold complex partner bound](actual_q_hahn_near_fold_complex_partner_bound.md), 263 lines | d2e3199cd649f1724dc888ad82e8849e9cc2313151f9567c625f21ae16bb6a6d |
| P | [Actual full physical complex packet](actual_q_hahn_full_physical_complex_packet.md), 338 lines | 28b7088c4cc947f05d2e395759b77c1232e150dba734d6dca3610548f15b1e0c |
| C | [Actual partner normal collision](actual_q_hahn_partner_normal_collision.md), 223 lines | afa5f4035f8cc4540da49ff0a4c9a279c67aba4fdaf3e3fc8d481798b2f1c268 |
| V | [Four-coherent fold value transport](research_four_coherent_fold_value_transport.md), 332 lines | 082ac7f012677c1b68db44393953db44987c71e1721eb9f763901747fea3be7e |

The argument uses written mathematics, complete source reads, and
metadata hashes. No mathematical program, numerical experiment,
test, build, earlier-final edit, or manuscript change was made.
