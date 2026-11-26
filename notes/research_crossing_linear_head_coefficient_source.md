# One source phase controls a linear number of centered coefficients

Written research proof, 22 November 2026.

A fixed small activity disc determines a linear number of nonzero
coordinates of the original crossing output. Their coefficient
circles have one contributing saddle, selected by an explicit
quadratic equation with its original logarithmic lift. The proof
estimates each entire circle and transfers the actual source error
on that same circle.

## 1. The original output and the assertion

Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 p=e^{-2\pi i/N},\quad \eta=(-1)^d,\quad \kappa=q^{d^2/2}.
 \tag{1}
\]
Use the complete centered basis, with
\(\phi(f_i f_j)=\delta_{ij}\) and \(U_t=\sum_{j=0}^d t^jf_j\).
For \(H=e^{-2\pi ih}\), \(K=e^{-2\pi ik}\), the actual output is
\[
 x_N=f_0U_{-H}U_{-K},\qquad
 \Phi_N(C,H,K)=\phi(U_{-C}x_N),\qquad
 c_{n,N}:=[C^n]\Phi_N=(-1)^n(x_N)_n .
 \tag{2}
\]
Thus \(c_{n,N}\) is an original physical coefficient, up to the
displayed sign. This is not evaluation at distinct Casimir roots.
Define
\[
 \begin{split}
 J(t)&=\int_0^t\log|2\sin\pi u|\,du,\\
 V(h,k)&=J(h+k)-2J(h)-2J(k),\\
 \Omega&=\{h,k>0:\ h+k<1,\ V(h,k)>0\},\\
 \Gamma_{0,N}&=\frac{\kappa^2}{N^2}
 \frac{\mathfrak F_N(N(1-h)-1/2)^2
       \mathfrak F_N(N(1-k)-1/2)^2}
      {\mathfrak F_N(N(1-h-k))}.
 \end{split}
 \tag{3}
\]
The factorial, phase and marks are those in [O,D].

All power series in \(C\) below are anchored at zero. Set
\[
 \begin{split}
 a(C)&=-\frac{2\operatorname{Li}_2(C)
          -\operatorname{Li}_2(HC)-\operatorname{Li}_2(KC)}
          {2\pi i},\\
 \alpha(C)&=[(1-HC)(1-KC)]^{-1/2},\qquad \alpha(0)=1,\\
 z&=a'(0)=\frac{2-H-K}{-2\pi i}.
 \end{split}
 \tag{4}
\]
For small real \(t>0\), let \(C_t\) be the analytic branch
\[
 C_t a'(C_t)=t,\qquad
 C_t=t/z+O(t^2),\qquad
 \beta_t=C_ta'(C_t)+C_t^2a''(C_t)=t+O(t^2).
 \tag{5}
\]
The square root of \(\beta_t\) below is
\(\sqrt t\,\sqrt{\beta_t/t}\), with the second root continued
from one at \(t=0\).

**Theorem.** Fix a compact \(\mathcal K\subset\Omega\).
There are a fixed complex neighborhood \(\mathcal U\) of
\(\mathcal K\), numbers \(t_0,\delta>0\), and an integer \(n_*\)
such that, uniformly for \((h,k)\in\mathcal U\) and integers
\(n_*\le n\le t_0N\), with \(t=n/N\),
\[
 \boxed{\quad
 c_{n,N}=
 \Gamma_{0,N}
 \frac{\alpha(C_t)e^{Na(C_t)}C_t^{-n}}
      {\sqrt{2\pi N\beta_t}}
 \left(1+O(n^{-1})+O(e^{-\delta N})\right).
 \quad}
 \tag{6}
\]
The constants are uniform when \(n\to\infty\) while \(n/N\to0\).
For every fixed integer \(m\ge0\),
\[
 c_{m,N}=\Gamma_{0,N}\frac{(Nz)^m}{m!}
                         (1+O_m(N^{-1})+O(e^{-\delta N})).
 \tag{7}
\]
In particular, after choosing \(t_0\) and \(n_*\) as in the proof,
all the coordinates \(c_{n,N}\), \(0\le n\le\lfloor t_0N\rfloor\),
are nonzero for every sufficiently large integer level.
Both parities, composite levels, original phases and all
Hermite directions are included.

## 2. An analytic comparison before the central branch

The exact noncentral unit of [D] is
\[
 A_N(C)=\exp\sum_{\substack{m\ge1\\N\nmid m}}
       \frac{2q^{-m}-H^m-K^m}{m(p^m-1)}C^m .
 \tag{8}
\]
The proof of [D, equation (21)] gives more than a comparison
on a slit Gamma sector: on a full fixed disc it gives
\[
 \Phi_N(C,H,K)=\Gamma_{0,N}A_N(C)(1+E_N(C,H,K)),\qquad
 \sup|E_N|\le C e^{-\delta_0N}.
 \tag{9}
\]
This is a single-valued analytic identity. The \(C^N\Log C\)
central factor of the canonical Gamma section is not inserted
into the coefficient circle.

Shrink \(\mathcal U\) and the disc if necessary, and choose
constants \(L\ge1\), \(\rho>0\) with
\[
 |H|,\ |K|\le L,\qquad L\rho<1,\qquad
 |z|\ge z_0>0,
 \tag{10}
\]
so that (9) holds on a neighborhood of \(|C|\le\rho\).
The last condition is available on the real compact set:
the equality \(H+K=2\) for unit \(H,K\) would force
\(H=K=1\), excluded by its strict positive angles.
It persists on a smaller complex neighborhood.

Uniformly on a still smaller fixed disc,
\[
             A_N(C)=\alpha(C)e^{Na(C)}(1+O(N^{-1})).
 \tag{11}
\]
Here is a direct derivation including the terms near multiples
of \(N\). For \(1\le m\le N/2\),
\[
 \begin{split}
 \frac1{p^m-1}&=-\frac{N}{2\pi im}-\frac12+O(m/N),\\
 q^{-m}&=1-\frac{\pi im}{N}+O(m^2/N^2).
 \end{split}
 \]
The constants are uniform on this interval. Substitution yields
\[
 \frac{2q^{-m}-H^m-K^m}{m(p^m-1)}
 =N\frac{2-H^m-K^m}{-2\pi im^2}
       +\frac{H^m+K^m}{2m}
       +O\!\left(\frac{1+L^m}{N}\right).
 \tag{12}
\]
The constant term uses the half-step \(q^{-m}\); omitting it
would change the amplitude. The first two series on the right
sum to \(Na(C)\) and \(\log\alpha(C)\).

For every remaining nonresonant \(m\),
\(|p^m-1|\ge4/N\). Consequently the part \(m>N/2\) of
the original logarithmic series on any fixed smaller disc
is \(O(Ns^{N/2})\) for some \(s<1\).
The corresponding tails of \(Na\) and \(\log\alpha\) have
the same exponential bound, with a possible additional
polynomial factor. Terms \(m\in N\mathbb Z\), absent from
(8), occur only in these exponentially small tails.
The errors in (12) sum absolutely to \(O(N^{-1})\).
This proves (11), uniformly on complex parameter compact sets.
Its error is analytic, with the corresponding fixed-derivative
bounds on smaller discs.

## 3. The selected quadratic and the entire-circle gap

The implicit function theorem applied to \(Ca'(C)=t\),
using (10), gives (5) uniformly on \(\mathcal U\).
Choose \(t_0>0\) small enough that every circle
\(C=C_te^{i\theta}\), \(-\pi\le\theta\le\pi\), is contained
in (9)--(11)'s fixed disc, and
\(\Re(\beta_t/t)\ge1/2\).

The saddle has an explicit algebraic description. Its
logarithmic equation is
\[
 \frac{2\Log(1-C_t)-\Log(1-HC_t)-\Log(1-KC_t)}
      {2\pi i}=t.
 \tag{13}
\]
Writing \(T=e^{-2\pi it}\), exponentiation gives
\[
 (1-HC_t)(1-KC_t)=T(1-C_t)^2,
 \quad
 (HK-T)C_t^2+(2T-H-K)C_t+1-T=0 .
 \tag{14}
\]
It is the root tending to zero and satisfying (13).
The quadratic by itself would not record the integer
logarithmic lift. It is a local coefficient-saddle relation,
not a knot peripheral polynomial.
Direct differentiation also gives
\[
 \beta_t=\frac{-2C_t/(1-C_t)
                 +HC_t/(1-HC_t)+KC_t/(1-KC_t)}
                {2\pi i}.
 \tag{15}
\]

Write \(a(C)=\sum_{m\ge1}a_mC^m\) and \(b_m=a_mC_t^m\).
The saddle equation says \(\sum m b_m=t\). For \(m\ge2\),
\[
 e^{im\theta}-1-m(e^{i\theta}-1)
 =(e^{i\theta}-1)^2
          \sum_{j=0}^{m-2}(m-1-j)e^{ij\theta}.
 \tag{16}
\]
Its magnitude is at most \(m(m-1)(1-\cos\theta)\).
Analytic coefficient bounds and \(C_t=O(t)\) give
\(\sum_{m\ge2}m^2|b_m|\le Ct^2\). Therefore
\[
 \begin{split}
 \Re[a(C_te^{i\theta})-a(C_t)-it\theta]
 &\le-[t-Ct^2](1-\cos\theta)\\
 &\le-\tfrac12t(1-\cos\theta)
                         \quad(-\pi\le\theta\le\pi),
 \end{split}
 \tag{17}
\]
after decreasing \(t_0\).
This is a bound on the complete original coefficient circle,
uniform also for complex \((h,k)\in\mathcal U\).
No complementary arc or cyclic alias is discarded.

## 4. Uniform coefficient integration, including \(t\to0\)

Let \(\pi_{n,N}=[C^n]A_N(C)\).
Cauchy's exact coefficient integral on the selected circle is
\[
 \pi_{n,N}=\frac{C_t^{-n}}{2\pi}
       \int_{-\pi}^{\pi}A_N(C_te^{i\theta})e^{-in\theta}
                                                        d\theta .
 \tag{18}
\]
Define
\[
 f_t(\theta)=
  \frac{a(C_te^{i\theta})-a(C_t)-it\theta}{t}.
 \tag{19}
\]
It extends analytically to \(t=0\), where
\(f_0(\theta)=e^{i\theta}-1-i\theta\).
On a fixed neighborhood of \(\theta=0\), all its derivatives
are uniformly bounded,
\[
 f_t(0)=f_t'(0)=0,\quad f_t''(0)=-\beta_t/t,\quad
 \Re(\beta_t/t)\ge1/2,\quad
 \Re f_t(\theta)\le-\tfrac12(1-\cos\theta)
 \tag{20}
\]
on the real circle.
The amplitude \(\alpha(C_te^{i\theta})\) and its derivatives
are uniformly bounded and its value at zero is bounded
away from zero.

Put \(n=Nt\) in (18). For \(n\to\infty\), split at
\(|\theta|=n^{-2/5}\).
Equation (20) makes the complementary integral
\(O(e^{-cn^{1/5}})\) relative to its fixed amplitude scale.
On the central interval, expand the phase through fourth
order and the amplitude through second order.
The cubic phase term and linear amplitude term are odd
against the even complex Gaussian; their integrals on
the symmetric interval vanish. Fourth-order phase,
squared cubic phase, and the remaining amplitude terms
have Gaussian moments \(O(n^{-1})\) relative to the leading
integral. Uniform bounded higher derivatives and
\(\Re(\beta_t/t)\ge1/2\) bound the Taylor remainders by
the same order. The interval can be extended to the
real line with exponentially small error.
The complex Gaussian has its square root continued from
one for \(\beta_t/t\).

The \(O(N^{-1})\) analytic error in (11) is also harmless:
by (17) its absolute integral is \(O(N^{-1}n^{-1/2})\)
times the central exponential scale.
Consequently, uniformly as \(n\to\infty\) with \(0<t\le t_0\),
\[
 \pi_{n,N}
 =\frac{\alpha(C_t)e^{Na(C_t)}C_t^{-n}}
           {\sqrt{2\pi N\beta_t}}\,
                 (1+O(n^{-1})+O(N^{-1})).
 \tag{21}
\]
Since \(n\le t_0N\), the last error is absorbed into
\(O(n^{-1})\). In particular the coefficient is nonzero
once \(n\ge n_*\), with \(n_*\) a sufficiently large
fixed integer and \(N\) sufficiently large.

The same gap gives the absolute-integral bound
\[
 \int_{-\pi}^{\pi}|A_N(C_te^{i\theta})|\,d\theta
       \le C e^{N\Re a(C_t)}n^{-1/2}.
 \tag{22}
\]
Use (9) on this same coefficient circle. Its source error,
divided by \(|\Gamma_{0,N}\pi_{n,N}|\), is
\(O(e^{-\delta_0N})\), by (21)--(22).
Thus no generic coefficient bound with an uncontrolled
radius-to-the-power-\(n\) cost is used. This proves (6).

## 5. The bounded indices and the complete retained head

For each fixed \(m\), (12) gives
\([C]\log A_N=Nz+O(1)\) and
\([C^j]\log A_N=O_m(N)\) for \(2\le j\le m\).
In the coefficient of \(\exp(\log A_N)\), the unique term
with \(m\) logarithmic factors has leading part \((Nz)^m/m!\);
every other partition has at most \(m-1\) factors.
Hence
\[
 \pi_{m,N}=(Nz)^m/m!+O_m(N^{m-1}).
 \tag{23}
\]
For the source error in (9), use the circle \(|C|=\gamma/N\)
with any fixed \(\gamma>0\). The series (8) bounds \(A_N\)
there by \(e^{C\gamma}\). Cauchy's estimate bounds its
coefficient error by
\(C_m|\Gamma_{0,N}|N^m e^{-\delta_0N}\).
Equation (23) and \(|z|\ge z_0\) prove (7), including
\(m=0\). The finitely many indices \(m<n_*\) are therefore
nonzero uniformly for large \(N\). Together with (21)
this proves nonvanishing of the entire stated linear head.

One may state the actual-source comparison more precisely:
uniformly for all \(0\le n\le\lfloor t_0N\rfloor\),
\[
       c_{n,N}=\Gamma_{0,N}\pi_{n,N}
                                  (1+O(e^{-\delta N})).
 \tag{24}
\]
For \(n\ge n_*\) this was (21)--(22); the finite remaining
indices follow from the preceding shrinking-circle estimate.
If \(P_D\) is coordinate orthogonal projection onto
\(f_0,\ldots,f_D\), in the declared centered coefficient
norm, put \(v_D=\sum_{n=0}^D(-1)^n\pi_{n,N}f_n\).
For \(D\le t_0N\), (24) implies
\[
 \|P_Dx_N-\Gamma_{0,N}v_D\|
       \le C e^{-\delta N}|\Gamma_{0,N}|\|v_D\|.
 \tag{25}
\]
This is an explicit head-vector approximation with its
source phase. It does not estimate the omitted coordinates.

An arbitrary covector can annihilate this nonzero head.
For the special phase-aligned rows
\(\ell_n=e^{i\theta}t_n\overline{(v_D)_n}/|(v_D)_n|\),
\(t_n\ge0\), supported in the head, (24) does give
\[
 \ell(x_N)=e^{i\theta}\Gamma_{0,N}
       \sum_{n=0}^D t_n|(v_D)_n|\,
                                  (1+O(e^{-\delta N})).
 \tag{26}
\]
This follows by summing the coordinate error with nonnegative
weights. The phases are specified by the canonical coefficients,
not by an unknown original scalar. No assertion that a general
literal Conway co-source lies in this cone is made.

## Complete proof sources and scope

Both complete proof texts were read at renewed matching pins:

| Label | Complete source | SHA-256 |
|---|---|---|
| D | [Fixed small activity disc, 288 lines](research_crossing_origin_disc_normalization.md) | 821bcc32af228845e93b2b8dcf91ea3c9f10226cfb1df75ecea90c68ab4e0ae8 |
| O | [Origin normalization, 385 lines](research_crossing_origin_fourier_normalization.md) | 6a516e08422f1645b6bea4281662b4c6db1465114de8eed610fb775607e6d3c8 |

The complete-boundary coefficient asymptotic, fixed and
sublinear Casimir observation theorems, germ-truncation note,
and crossing-reduced three-circle calculation were checked
for coverage. They concern different coefficient systems or
local contraction hypotheses. No novelty is claimed for
coefficient-circle stationary phase as a general method.
Here the exact normalized source (9), explicit phase and
entire-circle bound select a linear number of coordinates
in this original centered module.

The count \(t_0N\) is not fixed, and it is not the fixed degree
of a variational objective. A short component is not assumed
to have a bounded centered degree or a phase-aligned head.
The original full cap, turn, inverse edge metric and omitted
coordinates can still participate in cancellations. No
arbitrary-tree gluing, filled-knot volume or finite-exception
theorem follows.

Only written mathematics and text/hash inspection were used.
No program, numerical experiment, test, build, git action or
earlier-final file edit was performed.
