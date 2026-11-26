# Source-normalized transport of the actual q-Hahn partner near the fold

Written proof, 24 November 2026.

The original generic q-Hahn columns have scalar normalizers which vanish
near the channel fold. Keeping those normalizers inside the degree
recurrence cancels the large coefficients at every nonresonant row.
Only finitely many resonant rows retain a polynomial cost. This gives
a relative upper bound with a linear scaled-channel exponent, on every
fixed compact of the full strict physical tube.

The normal is the original difference of two generic highest-weight
\(N-1\) derivatives. No root-only derivative, interpolated normal, or
complex continuation of the integer channel is substituted.

## 1. Exact source and statement

Let \(N\ge3\), \(d=N-1\), \(q_0=e^{\pi i/N}\), and choose integers
\[
 0\le j<l,\qquad j+l=d,\qquad s=l-j.
 \tag{1}
\]
For \(q=q_0e^\epsilon\), keep \(N,t,u\) fixed when differentiating, and put
\[
 Q=q^2,\quad B=Q^{-N},\quad A=B^{-1},\quad x=q^d,\quad
 t=N\tau,\quad u=N\nu,\quad T=Q^t,\quad \sigma=q^t,\quad X=Q^{-u}.
 \tag{2}
\]
All powers use \(\log q=\pi i/N+\epsilon\). Write
\((a;Q)_k=\prod_{r=0}^{k-1}(1-aQ^r)\). The actual generic column is
\[
 C_m(q;t,u)=x^u F_m(Q,B;X,T),\qquad
 F_m=\sum_{k=0}^m
 \frac{(Q^{-m};Q)_k(B^2Q^{m+1};Q)_k(X;Q)_kQ^k}
 {(BQ;Q)_k(T^{-1};Q)_k(Q;Q)_k}.
 \tag{3}
\]
The variable \(B\) can temporarily be independent in rational identities.
Its value in the original source is always \(Q^{-N}\).
This is the finite generic source of [S] and [C], rather than a
deformation of its root specialization chosen afterward.

The paired normal, with its original Casimir gap and sign, is
\[
 w_{j,l}(t,u)=
 \frac{D C_j(q_0;t,u)-D C_l(q_0;t,u)}{-2N\Delta_j},
 \qquad
 \Delta_j=q_0^{2j+1}-q_0^{-2j-1},\qquad D=q\partial_q.
 \tag{4}
\]
In particular the large generic partner in (4) is retained.

Let
\[
 {\cal P}=\{(\tau,\nu)\in\mathbb C^2:
       \tfrac12<\Re\tau<1,\quad 0<\Re\nu<\Re\tau\}.
 \tag{5}
\]
For every compact \(K\Subset{\cal P}\), there are constants
\(\eta_K>0\), \(C_K\ge1\), and \(N_K\) such that, for all \(N\ge N_K\)
and all actual pairs (1) with \(1\le s\le\eta_KN\),
\[
 \boxed{\quad
 \left|\frac{w_{j,l}(N\tau,N\nu)}
 {C_j(q_0;N\tau,N\nu)}\right|
       \le C_K N^{100} C_K^s,\qquad (\tau,\nu)\in K .
 \quad}
 \tag{6}
\]
The denominator is nonzero, and both numerator and denominator are
holomorphic on a neighborhood of \(K\), for these sufficiently large
levels. Constants are uniform over all admissible integer pairs;
their parity restriction is exactly \(j+l=N-1\).

Consequently every window \(s=o(N)\) has subexponential relative cost.
For a fixed \(0<\delta\le\eta_K\), the corresponding upper exponential
cost is at most \(\delta\log C_K\), which tends to zero with \(\delta\).
These are upper bounds, not a leading normal amplitude.

## 2. The monic recurrence and its source normalization

Put
\[
 D_m(T)=\prod_{r=0}^{m-1}(T-Q^r),\qquad
 \kappa_m=\frac{(B^2Q^{m+1};Q)_m}{(BQ;Q)_m},\qquad
 z=\sigma Q^{-u}.
 \tag{7}
\]
For generic parameters define the monic polynomial \(R_m\) by
\[
 R_m(z)=\frac{D_m(\sigma^2)}{\sigma^m\kappa_m}
           F_m(Q,B;z/\sigma,\sigma^2).
 \quad\text{Thus}\quad
 C_m=x^u a^{\rm src}_m R_m(z),\qquad
 a^{\rm src}_m=\frac{\sigma^m\kappa_m}{D_m(T)}.
 \tag{8}
\]
The exact leading coefficient and finite degree recurrence in [S,N] give
\[
 R_{n+1}=(z+\alpha_n)R_n+\beta_nR_{n-1},\qquad
 R_0=1,\quad R_1=z+\alpha_0.
 \tag{9}
\]
For clarity, their rational coefficients are specified completely by
\[
 \begin{split}
 \Lambda_n&=AQ^{-n}+BQ^{n+1},\\
 b_n&=\frac{(1+A)+Q\sigma^2(1+B)
       -Q^{-n}(Q\sigma^2+A)-Q^n(BQ\sigma^2+1)}{\sigma},\\
 d_n&=Q^{1-n}+Q^n-1-Q,\\
 \mathfrak u_n&=\frac{b_n}{\Lambda_n-\Lambda_{n-1}}\quad(n\ge1),\\
 \mathfrak v_n&=\frac{b_{n-1}\mathfrak u_n+d_n}
                         {\Lambda_n-\Lambda_{n-2}}\quad(n\ge2),\\
 \alpha_n&=\mathfrak u_{n+1}-\mathfrak u_n,\qquad
 \beta_n=\mathfrak v_{n+1}-\mathfrak v_n-\alpha_n\mathfrak u_n,
 \end{split}
 \tag{10}
\]
where \(\mathfrak u_0=\mathfrak v_0=\mathfrak v_1=0\).
These are rational identities for every integer degree, including
degrees beyond the small channel. One way to justify that range,
as in [N], is to fix the recurrence index and clear denominators.
The residual is a finite Laurent polynomial in \(B,Q,\sigma,z\),
independent of the source size. Its vanishing at \(B=Q^{-N}\) for
all sufficiently large source sizes separates its finite
\(Q\)-exponent supports and forces the rational identity. A
small-channel slice count at the present fixed \(N\) is not being
applied to its large partner.

The exact consecutive scalar ratio simplifies to
\[
 \rho_n:=\frac{\kappa_{n+1}}{\kappa_n}
 =\frac{(1-B^2Q^{2n+1})(1-B^2Q^{2n+2})}
 {(1-B^2Q^{n+1})(1-BQ^{n+1})}.
 \tag{11}
\]
This follows directly by canceling the ranges \(n+1,\ldots,2n\)
and \(n+2,\ldots,2n+2\) in the two finite products.
Set
\[
 a_n=\frac{\sigma\rho_n}{T-Q^n}
       =\frac{a^{\rm src}_{n+1}}{a^{\rm src}_n}.
 \tag{12}
\]
Multiplying (9) by its actual scalar gives the recurrence used here:
\[
 \boxed{\quad
 C_{n+1}=a_n(z+\alpha_n)C_n
                 +a_na_{n-1}\beta_n C_{n-1}.
 \quad}
 \tag{13}
\]
The common factor \(x^u\) cancels between consecutive degrees.
Equation (13) is first used off the root, where all its monic
factors are defined. It does not assert that those individual
monic factors extend holomorphically across the fold.

## 3. Initial control on a genuine generic circle

Fix a slightly larger compact neighborhood of \(K\) inside \({\cal P}\),
and choose
\[
 0<\eta_K<\min\left(\tfrac14,\inf_K(\Re\tau-\tfrac12)\right).
 \tag{14}
\]
Decrease it for that neighborhood if necessary. For \(s\le\eta_KN\),
all indices from \(j-1\) to \(l+1\) lie near \(N/2\).
Every extra divisor \(T=Q^r\), \(j\le r<l\), is then uniformly
separated from this neighborhood. Its real scaled index is less
than \(1/2+\eta_K/2\), whereas \(\Re\tau\) stays farther to the right.
The original small-column divisors are separated as well.

Use the circle
\[
                   |\epsilon|=\varrho_N=c_KN^{-8}.
 \tag{15}
\]
The original generic determinant construction in [S] and its
full-physical extension [P, section 6] give, on the entire disk,
\[
 \left|\frac{C_j(q;t,u)}{C_j(q_0;t,u)}\right|\le C_K,
 \qquad
 \left|\frac{R_{j-1}(z(q))}{R_j(z(q))}\right|\le C_K.
 \tag{16}
\]
Here is the relevant distinction in the enlarged domain.
The root determinant has a uniformly bounded inverse by the
rotated positive-half-plane realization in [P]. For each adjacent
pair one freezes the larger of its two root entries and sets
the other generic entry to retain the exact product \(-\beta_n(q)\).
That frozen entry is uniformly bounded below. Freezing one specified
upper entry everywhere would fail at its possible zeros.
The generic perturbation is \(O_K(N^7|\epsilon|)\).
The last inverse cofactor is precisely \(R_{j-1}/R_j\).
This proves the two controls used in (16), with all original scalar
factors restored. It also proves that \(C_j(q_0)\ne0\) on \(K\).

The initial consecutive actual columns have a modest additional cost.
Since \(2j\le N-2\), neither numerator factor of \(\rho_{j-1}\)
in (11), with indices \(2j-1,2j\), vanishes at the root.
Each has modulus at least \(c/N\). Its denominator factors lie
near index \(N/2\) and are uniformly separated from zero.
The bounded, nonzero factor \(\sigma/(T-Q^{j-1})\) therefore gives
\[
 |a_{j-1}^{-1}|\le C_KN^2,\qquad
 \left|\frac{C_{j-1}(q;t,u)}{C_j(q_0;t,u)}\right|
       \le C_KN^2
 \tag{17}
\]
on (15). These estimates persist on the disk, since the change
in \(a_{j-1}\) is \(O_K(N|\epsilon|)\), much smaller than \(N^{-2}\).
Only sufficiently large \(N\) is needed; then \(j\ge1\).

## 4. Uniform nonresonant transfers

For a recurrence row \(j\le n<l\), write
\[
 q_n^{\rm dist}=1+|2n-N|,\qquad
 {\cal B}_N=\{n:|2n-N|\le4\}.
 \tag{18}
\]
There are at most five bad rows in \({\cal B}_N\). Outside this set,
all required root gaps for (10), including those with index \(n+1\),
are nonzero.

At the root put \(\theta=\pi/N\) and
\(c=-\cos((t+1)\theta)\). The exact coefficients reduce to
\[
 \alpha_n=\frac{c}{\cos(n\theta)\cos((n+1)\theta)},\qquad
 \beta_n=
 \frac{\sin^2(n\theta)[\cos^2(n\theta)-c^2]}
 {\cos^2(n\theta)\sin((2n-1)\theta)\sin((2n+1)\theta)}.
 \tag{19}
\]
Although first derived on the small side in [S], these root
formulas hold at every nonresonant degree. Fixing \(n\), they are
rational identities in \(q,\sigma\) at \(B=1\): their cleared
residual vanishes for all sufficiently large primitive source
roots, and identically in \(\sigma\). The distinct \(q_0\)
accumulate at \(1\), so that Laurent-polynomial residual is zero.
This argument extends the identity, not an estimate through a pole.
For example the diagonal formula follows directly at \(B=1\) from
\(\mathfrak u_n=-(1+Q\sigma^2)(1-Q^n)/
[\sigma(1-Q)(1+Q^n)]\), fixing its sign.

For \(n\notin{\cal B}_N\), the trigonometric distances in (19) give
\[
 |\alpha_n(0)|\le C_K(N/q_n^{\rm dist})^2,\qquad
 |\beta_n(0)|\le C_K(N/q_n^{\rm dist})^4.
 \tag{20}
\]
In contrast, the two numerator factors of (11) vanish quadratically
in the scaled distance from the fold. Since its denominator factors
are units near index \(N/2\), both neighboring actual scalar ratios obey
\[
 |a_n(0)|+|a_{n-1}(0)|
                  \le C_K(q_n^{\rm dist}/N)^2.
 \tag{21}
\]
The shift from \(n\) to \(n-1\) is harmless outside the bad set.

We need these bounds on the actual circle, not only at its center.
The only spectral differences in (10) factor as
\[
 \begin{split}
 \Lambda_m-\Lambda_{m-1}
     &=(1-Q)AQ^{-m}(1-B^2Q^{2m}),\\
 \Lambda_m-\Lambda_{m-2}
     &=(1-Q^2)AQ^{-m}(1-B^2Q^{2m-1}).
 \end{split}
 \tag{22}
\]
At nonbad rows all the differences required for
\(\mathfrak u_n,\mathfrak v_n,\mathfrak u_{n+1},\mathfrak v_{n+1}\)
have modulus at least \(c/N^2\), persisting on a small \(N^{-3}\) disk.
The elementary coefficients in (10) are \(O_K(1)\) and their
\(\epsilon\)-derivatives are \(O_K(N)\). The quotient rule gives
\(\mathfrak u'=O_K(N^5)\), \(\mathfrak v'=O_K(N^7)\), and hence
\(\alpha_n'=O_K(N^5)\), \(\beta_n'=O_K(N^7)\).
Thus their changes on (15) are \(O_K(N^{-3})\) and \(O_K(N^{-1})\).
These are absorbed in (20), since \(q_n^{\rm dist}\le N\).
Likewise \(a_n'=O_K(N)\) directly from (11),(12), so the
change \(O_K(N^{-7})\) is absorbed in (21).

Combining these retained source ratios with (20) yields
\[
 |a_n(z+\alpha_n)|+
          |a_na_{n-1}\beta_n|\le C_K,\qquad n\notin{\cal B}_N,
 \tag{23}
\]
on the circle. This is the cancellation lost by propagating only
the monic recurrence and subsequently bounding its normalizers.

## 5. The finite resonant cost and the actual normal

At a bad row the last factor of a resonant difference (22) is
\(1-Q^{-N}=1-e^{-2N\epsilon}\). On (15) it has modulus at least
\(cN\varrho_N\). Its first factor has size at least \(c/N\).
All other required gaps remain at least \(c/N^2\). Therefore every
gap is at least \(c_K\varrho_N\) on the circle, just as in [N].
The exact formulas (10) then give
\[
 |\alpha_n|\le C_K\varrho_N^{-1},\qquad
 |\beta_n|\le C_K\varrho_N^{-2}.
 \tag{24}
\]
The scalar ratios \(a_n,a_{n-1}\) themselves are uniformly bounded
there, including bad rows: the denominators in (11),(12) are units
and all their numerators are bounded. A bad two-component transfer
in (13) consequently costs at most \(C_KN^{16}\).

Starting with (16),(17), propagate the actual recurrence (13) through
exactly \(s\) rows. There are at most five bad transfers, so
\[
 \left|\frac{C_l(q;t,u)}{C_j(q_0;t,u)}\right|
                      \le C_K N^{82} C_K^s
                      \qquad (|\epsilon|=\varrho_N).
 \tag{25}
\]
No product of singular monic factors is differentiated.
The full finite formula (3) is holomorphic inside the circle:
its factorial indices are less than \(N\), and its \(T\) divisors
are separated by (14). All apparent monic poles have therefore
already canceled in the original source.

Cauchy's formula applied to these full columns, with \(t,u,N\) fixed,
now gives
\[
 \left|\frac{D C_l(q_0)}{C_j(q_0)}\right|
       \le C_KN^{90}C_K^s,\qquad
 \left|\frac{D C_j(q_0)}{C_j(q_0)}\right|\le C_KN^8.
 \tag{26}
\]
Finally the actual gap in (4) satisfies
\(2N|\Delta_j|=4N\sin(\pi s/N)\ge8s\ge8\).
Equations (4),(26) prove (6), with room in the exponent \(100\).

## 6. Consequences, scope, and complete inputs

Taking logarithms of (6) gives
\[
 \log|w_{j,l}/C_j|
       \le100\log N+(s+1)\log C_K.
 \tag{27}
\]
Thus all \(s=o(N)\), rather than only \(s\log N=o(N)\), have
subexponential relative upper cost on the same fixed magnetic compact.
Uniformly for \(s\le\delta N\), its upper exponential cost is at
most \(\delta\log C_K+o(1)\). At a fixed positive \(\delta\), this
still permits exponential cost; subexponential cost there is not asserted.
The original scalar ratios remove the nonresonant fold-distance cost.

The old near-fold estimate [N] and its enlargement in [P] paid
\(N^{16}\) at every intervening row. The improvement here comes from
the exact actual-source recurrence (13). The normalizer zeros are
used before taking absolute values, with finitely many resonances
kept explicit. This does not replace the generic derivative in (4)
by a derivative of a root collision identity.

The result concerns actual integer channels and fixed complex
magnetic compacts. It does not continue the channel to a complex
parameter, prove a nonzero leading normal amplitude, or control
the complete q-Hahn coupon after its remaining factors and
contractions. It does not place a short-filled geometric saddle
in this corridor or establish its coefficient in the original
closed source. No volume or finite-exception conclusion follows here.

The complete proof inputs, including the closest previous bounds,
are the following four texts:

| Label | Complete text | SHA256 |
| --- | --- | --- |
| S | [Actual small-channel generic normals](actual_q_hahn_small_channel_generic_normals.md), 261 lines | 9eaf5750927cacbc9ad3d5d3b3b75b883083d4cf16afa1ca21c03f6376a53fb4 |
| N | [Actual near-fold complex partner bound](actual_q_hahn_near_fold_complex_partner_bound.md), 263 lines | d2e3199cd649f1724dc888ad82e8849e9cc2313151f9567c625f21ae16bb6a6d |
| P | [Actual full physical complex packet](actual_q_hahn_full_physical_complex_packet.md), 338 lines | 28b7088c4cc947f05d2e395759b77c1232e150dba734d6dca3610548f15b1e0c |
| C | [Actual partner normal collision](actual_q_hahn_partner_normal_collision.md), 223 lines | afa5f4035f8cc4540da49ff0a4c9a279c67aba4fdaf3e3fc8d481798b2f1c268 |

Only written mathematics, text reads, and metadata hashes were used.
No mathematical program, numerical experiment, test, or build was run.
Earlier final notes and frozen manuscripts are unchanged.
