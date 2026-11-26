# A paid physical collar at the true upper outgoing endpoint

Research deduction, 7 November 2026. The triangular support makes the
true upper outgoing collar a low retained-index source. Its complete
absolute row sum is below the original supporting plane with a fixed
gap. This uses the literal endpoint products and the already proved
endpoint-plane comparison; no contour height is changed.

The central outgoing faces and the opposite outgoing tail are not
estimated here. No new function, root, or source value is evaluated.

## 1. Exact source and reference allocation

Use the actual correlated family and original plane from
[the bare inner-source completion](research_mixed_fourier_right_cap_bare_inner_completion.md):
\[
 \eta\in\{0,1\},\quad a_*\in K_{3+\eta},\quad
 a=x+ih,\quad h=\Im a_*,\quad x\in P=[11/50,9/20],
 \quad y=x_0,\quad Y=e^{2\pi iy},\quad \rho=|Y|.
 \tag{1}
\]
Write \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), and \(X=e^{-2\pi ia}\).
The original physical row is
\[
 T_{j,l}
 =X^{-j}\frac{p_j(X)P_{j+l}}{P_j^3P_l}\,f_l(y),
 \qquad j,l\ge0,\quad j+l<N,
 \tag{2}
\]
where
\[
 f_l(y)=\frac{e^{-\pi i(N-1)y}}N
             Y^l\prod_{k=l+1}^{N-1}(1-Yr^k).
 \tag{3}
\]
All level parities, true endpoint values, and factors \(1/N\)
remain in (2)--(3).

The incoming height satisfies \(-.108\le h\le.068\).
The elementary bound in the
[retained-rate theorem](research_mixed_fourier_right_cap_coherent_retained_rate.md)
gives \(|X^{-1}|<2\). Its proof is
\[
 \log2>2(1/3+1/81)=56/81>594/875=.216(22/7).
 \tag{4}
\]
The established incoming halfweight upper rate is
\(-\eta\Re g(a)/2\), with an arbitrary fixed aggregate tolerance.
It is an upper bound for its actual modulus, not division by a
finite Fourier polynomial.

Keep exactly
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                              -\kappa(x-\Re a_*)^2,\qquad
 \kappa=1/2500000.
 \tag{5}
\]
The [proved endpoint payment](research_mixed_fourier_right_cap_endpoint_payment.md)
supplies the uniform inequality
\[
 2\pi(-h)_++\pi\Im y-\frac\eta2\Re g(a)
                         <B_\eta(x)-\frac{387}{70000}.
 \tag{6}
\]
All actions and the incoming marginal in (5) are unchanged.

## 2. A direct bound on every supported collar row

Fix \(\delta=1/1000\), and retain the complete set
\[
 \mathcal U_N=
 \{(j,l):j,l\ge0,\ j+l<N,\ l/N\ge1-\delta\}.
 \tag{7}
\]
If \(k=N-1-l\), then \(0\le j\le k<\delta N\).
In particular every retained row is in the exact low-index source
\(j<\lceil N/2\rceil\).

Set
\[
 f(\delta)=\delta\log\frac{e}{4\delta}.
 \tag{8}
\]
For \(0\le j\le\delta N\), the elementary factorial estimate gives
\[
 |P_j|^{-1}\le e^{Nf(\delta)}.
 \tag{9}
\]
Indeed \(2\sin(\pi m/N)\ge4m/N\) for \(m\le N/2\), so
\(|P_j|\ge(4/N)^j j!\ge(4j/(eN))^j\).
The function \(u\log(e/(4u))\) increases on \([0,\delta]\),
and the value at zero is understood continuously.

The remaining exact factors satisfy
\[
 |X^{-j}p_j(X)|
   =\prod_{m=1}^j|X^{-1}-r^m|\le3^j,\qquad
 \left|\frac{P_{j+l}}{P_l}\right|\le2^j.
 \tag{10}
\]
The first inequality is strict for \(j>0\); at \(j=0\) both
sides are one. No supported denominator vanishes. Formula (3), rewritten at
\(l=N-1-k\), gives
\[
 |f_l(y)|
 \le\frac{e^{-\pi(N-1)\Im y}}N
                         \left(\frac{1+\rho}{\rho}\right)^k.
 \tag{11}
\]
Here \(\rho=e^{-2\pi\Im y}\) was used exactly.
Thus all rows in (7), including \(j=0,l=N-1\), obey the common
upper rate
\[
 -\pi\Im y+\omega_\delta,\qquad
 \omega_\delta=
 3f(\delta)+\delta\log6+
                       \delta\log\frac{1+\rho}{\rho}.
 \tag{12}
\]
Their count is at most \(N^2\), so summing their absolute values
changes only a polynomial prefactor.

Every bound in (12) is elementary. Since \(\rho>3/5\),
\[
 \log250<6,\qquad \log6<2,\qquad
              \log\frac{1+\rho}{\rho}<\log(8/3)<1.
 \tag{13}
\]
For explicit witnesses, \(e^2>1+2+2+4/3+2/3=7\), hence
\(e^6>343>250\), and
\(e>1+1+1/2+1/6+1/24=65/24>8/3\).
Consequently
\[
                         \omega_\delta<\frac{24}{1000}=\frac3{125}.
 \tag{14}
\]

## 3. Payment by the original plane

The inherited bound \(\rho<123/200\) and the elementary integral
inequality \(\log u>(u-1)/u\), \(u>1\), give
\[
                 2\pi\Im y=-\log\rho
                    >\log(200/123)>\frac{77}{200}.
 \tag{15}
\]
Subtract the allocated collar rate
\(-\pi\Im y-\eta\Re g(a)/2+\omega_\delta\)
from (6). Equations (14)--(15) prove the strict uniform difference
\[
 B_\eta(x)-
 \left(-\pi\Im y-\frac\eta2\Re g(a)+\omega_\delta\right)
 >\frac{77}{200}+\frac{387}{70000}-\frac3{125}
 =\frac{25657}{70000}>\frac13.
 \tag{16}
\]
The nonnegative term \(2\pi(-h)_+\) was only dropped after this
exact comparison.

**Theorem.** For every prescribed \(\tau>0\), there are uniform
constants \(C_\tau,A_\tau,N_\tau\) such that, for all \(N\ge N_\tau\)
of either parity and all actual references and targets (1),
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}\sum_{(j,l)\in\mathcal U_N}|T_{j,l}|
 \le C_\tau N^{A_\tau}
       e^{N\{B_\eta(x)-25657/70000+\tau\}}.
 \quad}
 \tag{17}
\]
In particular, after choosing the tolerance and absorbing the
polynomial factor, the finite exponential gap can be taken to be
\(1/3\). The explicit spare margin is
\[
                     \frac{25657}{70000}-\frac13
                               =\frac{6971}{210000}>0.
 \]

This proves an actual low-index physical-source estimate, stronger
than a bound for its signed sum alone. It does not estimate the
real outgoing face \(q=9/20\), the intervening outgoing rows,
the lower outgoing endpoint, or the central contour corrections.
No part of the paid coherent high-index group is used termwise.
