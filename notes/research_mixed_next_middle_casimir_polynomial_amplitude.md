# The exact middle amplitude as a polynomial in the Casimir variable

Private written source proof, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source
edit is used.

The normalized middle amplitude has a polynomial bound on the
whole real Casimir interval. A fixed complex neighborhood costs
an arbitrarily small exponential rate, with the neighborhood
depending on that rate. The outgoing variable retains the exact
upper-half-plane growth bound. All finite products and the genuine
physical cutoff remain inside the polynomial.

## 1. Exact polynomial and statement

Use the original level and endpoints
\[
 q=e^{\pi i/N},\qquad \kappa=q^{(N-1)^2/2},\qquad
 L=\lfloor N/6\rfloor,\qquad U=\lfloor N/2\rfloor-1,\qquad
 d_N^{\rm amp}=U-L,
\]
\[
 s_n=2\sin(\pi n/N),\qquad S_a=\prod_{\nu=1}^a s_\nu,\qquad
 c_n=2\cos((2n+1)\pi/N).
 \tag{1}
\]
The symbol \(d_N^{\rm amp}\) is only a degree; it is not the
forced factorial polynomial \(d_N\). All statements below concern
sufficiently large \(N\), of either parity.

For independent complex variables \(\xi,T\), define
\[
\begin{split}
 \widehat{\mathcal R}_{n,N}(\xi,T)
   &=e^{i\pi/N}
       \frac{(\xi-c_n)
              (e^{i\pi n/N}-T e^{-i\pi n/N})}{i s_n^3},\\
 \widehat P_{\ell,N}(\xi,T)
   &=\prod_{h=0}^{\ell-1}
                    \widehat{\mathcal R}_{U-h,N}(\xi,T),\\
 \mathscr A_N(\xi,T)
   &=\sum_{\ell=0}^{d_N^{\rm amp}}\widehat P_{\ell,N}(\xi,T).
\end{split}
 \tag{2}
\]
The empty product is one. Every denominator is fixed and nonzero:
only \(L+1\le n\le U<N/2\) occurs. Each product has degree at most
\(\ell\) in each variable, and \(\mathscr A_N\) has bidegree at
most \((d_N^{\rm amp},d_N^{\rm amp})\).

Indeed
\[
 \sin\pi(x-\eta)\sin\pi(x+\eta+1/N)
  =\frac{\cos(2\pi\eta+\pi/N)-\cos(2\pi x+\pi/N)}2.
 \tag{3}
\]
Consequently the exact function of
[the outgoing half-disk theorem](research_mixed_next_middle_outgoing_half_disk_amplitude.md)
satisfies
\[
 \mathscr A_N(2\cos(2\pi\eta+\pi/N),T)
       =\mathcal A_N(\eta,T).
 \tag{4}
\]
In particular the physical Casimir value at \(\eta=j/N\) is
exactly \(\xi=c_j\), with its \(1/N\) shift retained.

Write
\[
 \mathbb D_+=\{T:|T|\le1,\ \Im T\ge0\}.
\]

**Theorem.** There are constants \(C,A\), independent of the
level and parity, such that
\[
 \boxed{\quad
 \sum_{\ell=0}^{d_N^{\rm amp}}
             |\widehat P_{\ell,N}(\xi,T)|
 \le C N^A\max\{1,|T|^{d_N^{\rm amp}}\},
 \qquad -2\le\xi\le2,\quad \Im T\ge0.
 \quad}
 \tag{5}
\]
For every \(\tau>0\), there is a fixed \(\delta_\tau>0\) and
a constant \(C_\tau\) such that
\[
 \boxed{\quad
 \sum_{\ell=0}^{d_N^{\rm amp}}
             |\widehat P_{\ell,N}(\xi,T)|
 \le C_\tau N^A e^{\tau N}
                      \max\{1,|T|^{d_N^{\rm amp}}\},
 \quad
 \operatorname{dist}(\xi,[-2,2])\le\delta_\tau,\quad
 \Im T\ge0 .
 \quad}
 \tag{6}
\]
In particular the same estimates hold for
\(|\mathscr A_N|\). Every fixed \(\xi\)-derivative of
\(\mathscr A_N\) satisfies (6), with its own constant, on the
smaller tube of radius \(\delta_\tau/2\).

The tube in (6) depends on \(\tau\). This is not a claim that
one fixed complex tube has an arbitrarily small rate. There is
no nonvanishing or limiting-factor assertion on the enlarged
real interval or its tube.

## 2. Polynomial control before completing the Casimir interval

First take real \(0\le\eta\le1/2\) and \(T\in\partial\mathbb D_+\).
The real primitive and comparison from the half-disk theorem are
\[
\begin{split}
 J(x)&=\int_0^x\log|2\sin\pi s|\,ds,\\
 V_\eta(x)&=J(x+\eta)+J(x-\eta)-2J(x),\\
 K_T(x)&=\int_x^{1/2}
       \log\frac{|1-T e^{-2\pi is}|}{2\sin\pi s}\,ds,\\
 \Psi_T(x;\eta)&=-V_\eta(x)+K_T(x).
\end{split}
 \tag{7}
\]
The original
[real-period comparison, Lemma 2](research_three_crossing_real_period_newton_bound.md)
gives \(V_\eta(x)\ge0\) on
\(0\le\eta\le1/2,\ 0\le x\le1/2\), including \(\eta=0\).
The boundary argument in Section 2 of the half-disk theorem
does not use a lower bound on \(\eta\). It proves
\[
 K_T(x)\le0,\qquad
 1/6\le x\le1/2,\quad T\in\partial\mathbb D_+.
 \tag{8}
\]
For clarity, on the upper semicircle this follows from the
translated logarithmic-sine intervals; on the nonnegative
diameter the integrand is nonpositive; on the negative diameter
its integral is bounded by \(H(x)\le0\), with
\(H(1/6)=H(1/3)=J(1/3)<0\).
Thus
\[
 \Psi_T(x;\eta)\le0
 \tag{9}
\]
on the whole displayed real set. Strictness is unnecessary here.

The zero-safe finite mesh estimate in
[the exact analytic-amplitude theorem, Section 3](research_mixed_next_middle_exact_analytic_amplitude.md)
and the circle-factor version in Section 3 of the half-disk
theorem give, for \(x=(U-\ell)/N\),
\[
 \log\left|
   \widehat P_{\ell,N}(2\cos(2\pi\eta+\pi/N),T)\right|
 \le N\Psi_T(x;\eta)+C\log N.
 \tag{10}
\]
This estimate is uniform through every numerator zero and at
\(\eta=0,1/2\). An exact sampled zero only improves its upper
bound. Its denominators lie in the fixed regular interval
between \(L/N\) and \(1/2\).

If \(x=L/N<1/6\), its distance from \(1/6\) is less than
\(1/N\). Moving that integration endpoint, moving \(U/N\) to
\(1/2\), and removing the explicit \(1/N\) numerator shift each
cost at most \(C\log N\) in (10), by the same uniform
integrated-log modulus of continuity. This also covers
\(\ell=0\); that product is exactly one.
Equations (9)--(10) therefore imply a bound
\[
 \left|
   \widehat P_{\ell,N}(2\cos(2\pi\eta+\pi/N),T)\right|
 \le C N^{A_0}
 \tag{11}
\]
uniformly in every exact \(\ell\), the whole real \(\eta\)
interval, and the boundary of the half-disk. Each product is a
polynomial in \(T\). Maximum modulus extends (11) to the
filled half-disk, before any products are summed.

Put \(a_N=\cos(\pi/N)\). The real map
\(\eta\mapsto2\cos(2\pi\eta+\pi/N)\), \(0\le\eta\le1/2\),
has image exactly
\[
 I_N=[-2,2a_N].
 \tag{12}
\]
The point \(-2\) occurs inside that parameter interval. Hence
(11) controls each polynomial in \(\xi\) on all of \(I_N\),
not merely its physical samples.

## 3. Completing the small missing real interval

We give the explicit polynomial continuation needed between
\(2a_N\) and \(2\). Fix \(T\in\mathbb D_+\) and \(\ell\), and
write \(p(\xi)=\widehat P_{\ell,N}(\xi,T)\).
Its degree is at most \(\ell\le d_N^{\rm amp}<N/3\).
Map \(I_N\) to \([-1,1]\) by
\[
 z=\frac{\xi+1-a_N}{1+a_N}.
 \tag{13}
\]
The Chebyshev expansion of this complex polynomial has constant
coefficient of modulus at most \(\|p\|_{I_N}\) and every other
coefficient of modulus at most \(2\|p\|_{I_N}\). These bounds
follow directly from the cosine-integral formulas for those
coefficients and hold for complex coefficients as well.

For real \(-2\le\xi\le2\), the new coordinate lies in
\[
 -1\le z\le z_N=\frac{3-a_N}{1+a_N}
          =1+2\tan^2\frac{\pi}{2N}.
 \tag{14}
\]
If \(\alpha_N=\operatorname{arcosh}z_N\), then
\[
 \alpha_N=2\operatorname{arsinh}
                       \left(\tan\frac{\pi}{2N}\right)
       \le \frac{2\pi}{N}.
 \tag{15}
\]
Indeed \(\operatorname{arsinh}u\le u\), and
\(\tan v\le2v\) for \(0\le v\le\pi/4\), using
\(\sin v\le v\) and \(\cos v\ge1/2\).
For every Chebyshev polynomial of degree \(k\le\ell\),
\[
 |T_k(z)|\le e^{k\alpha_N}\le e^{2\pi/3}
       \qquad(-1\le z\le z_N).
 \tag{16}
\]
It follows from (11) and the at most \(\ell+1\) coefficients
that
\[
 \sup_{[-2,2]}|p|
       \le C N^{A_0+1}.
 \tag{17}
\]
The original missing interval of width \(2(1-a_N)\) has
therefore cost only a polynomial factor. In particular there
is no fixed-rate loss at the real Casimir endpoint.
Summing (17) over the at most \(N\) products proves
\[
 \sum_{\ell=0}^{d_N^{\rm amp}}|\widehat P_{\ell,N}(\xi,T)|
       \le C N^{A_0+2},
       \qquad \xi\in[-2,2],\quad T\in\mathbb D_+.
 \tag{18}
\]

## 4. A fixed spectral tube with arbitrarily small rate

For a specified \(\tau>0\), put \(h=3\tau\),
\(a=\cosh h\), and \(b=\sinh h\). Let the filled ellipse
\(\mathcal E_h\) in the \(z=\xi/2\) plane have semiaxes
\(a,b\), and choose
\[
 \delta_\tau=b(1-a^{-1})>0.
 \tag{19}
\]
The tube \(\operatorname{dist}(\xi,[-2,2])\le\delta_\tau\)
lies inside this ellipse after division by two. To see this,
write \(z=x+e\), \(-1\le x\le1\), \(|e|\le\delta_\tau/2\).
The Euclidean norm after the linear map
\((\Re z,\Im z)\mapsto(\Re z/a,\Im z/b)\) is at most
\[
 \frac1a+\frac{|e|}{b}
 \le \frac1a+\frac{1-a^{-1}}2
       =\frac{1+a^{-1}}2<1.
 \tag{20}
\]

The Chebyshev coefficients on \([-2,2]\), controlled by
(17), now give
\[
 |p(\xi)|\le C N^{A_0+2} e^{h\ell}
       \le C N^{A_0+2}e^{\tau N}
       \qquad(\xi/2\in\mathcal E_h).
 \tag{21}
\]
Here \(|T_k(z)|\le e^{hk}\) throughout the filled ellipse:
on its boundary use
\(z=(\zeta+\zeta^{-1})/2\), \(|\zeta|=e^h\), and
\(T_k(z)=(\zeta^k+\zeta^{-k})/2\), then apply maximum
modulus to the polynomial in \(z\).
Summing the at most \(N\) products proves (6) on
\(\mathbb D_+\), with a fixed exponent \(A=A_0+3\).
The same exponent also accommodates (18).

## 5. Exact outgoing reflection and derivative scope

For every complex \(\xi\), each product in (2) has the form
\[
 \widehat P_{\ell,N}(\xi,T)
  =c_{\ell,N}(\xi)
       \prod_{h=0}^{\ell-1}
                    (T-e^{2\pi i(U-h)/N}).
 \tag{22}
\]
Its coefficient may vanish and is never divided out. If
\(\Im T\ge0\), \(|T|>1\), then
\(T^\#=1/\overline T\in\mathbb D_+\), and exactly
\[
 |\widehat P_{\ell,N}(\xi,T)|
      =|T|^\ell|\widehat P_{\ell,N}(\xi,T^\#)|.
 \tag{23}
\]
The same complex \(\xi\) is used on both sides. Applying
(18),(21) to \(T^\#\) and summing proves (5),(6) on the
whole upper half-plane.

For each fixed nonnegative integer \(p\), Cauchy's formula on
a circle of radius \(\delta_\tau/2\) gives
\[
 |\partial_\xi^p\mathscr A_N(\xi,T)|
 \le C_{\tau,p}N^A e^{\tau N}
                    \max\{1,|T|^{d_N^{\rm amp}}\},
 \quad
 \operatorname{dist}(\xi,[-2,2])\le\delta_\tau/2,\quad
 \Im T\ge0 .
 \tag{24}
\]
All constants are uniform in \(T\) because the same factor on
the right of (6) applies on that circle.

For the original outgoing index \(T=e^{2\pi it}\), the result
can be written
\[
 |\mathscr A_N(\xi,e^{2\pi it})|
 \le C_\tau N^A
       \exp\{N[\tau+(2\pi/3)(-\Im t)_+]\},
 \quad 0\le\Re t\le1/2,
 \tag{25}
\]
on the tube of (19). For real \(\xi\in[-2,2]\), the
\(\tau\) in (25) can be omitted, using (5).
No upper or lower restriction on \(\Im t\) is imposed.

There is also a sharper direct angular statement, at every
height. The same Chebyshev coefficients from (17) and the exact
identity \(T_k(\cos(\theta+i\sigma))=\cos(k(\theta+i\sigma))\)
give
\[
 \boxed{\quad
 \sum_{\ell=0}^{d_N^{\rm amp}}
    |\widehat P_{\ell,N}(2\cos(\theta+i\sigma),T)|
 \le C N^A e^{d_N^{\rm amp}|\sigma|}
                       \max\{1,|T|^{d_N^{\rm amp}}\},
 \quad \theta,\sigma\in\mathbb R,\quad\Im T\ge0.
 \quad}
 \tag{26}
\]
Indeed the \(k\)-th Chebyshev term has modulus at most
\(e^{k|\sigma|}\), and each product has \(k\le\ell\).
There are at most \(N\) coefficients for each of at most
\(N\) products. This proves (26) first on \(\mathbb D_+\);
the exact reflection (23) gives the rest. Thus the Casimir
angular cost is at most \(N|\sigma|/3\), and no angular
subinterval has been excluded. This is a bound for this
amplitude, not for an independently multiplied polynomial.

## 6. Exact source use and limitations

For the original physical \(0\le j,k\le U\), the exact identity
remains
\[
 W_{jk,N}
   =q^{-(k+1)U}
      \frac{S_U^3}{S_{U-j}S_{U+j+1}S_{U-k}}\,
             \mathscr A_N(c_j,e^{2\pi ik/N}).
 \tag{27}
\]
Every literal stop at \(\max(L,j,k)\), both parity amplitudes,
and the genuine \(L\)-endpoint are already encoded in this
identity. The passage to the Casimir polynomial does not
extend the physical factorial expression to \(j>U\).

The
[restored middle reduction](research_mixed_next_three_restored_middle_large_indices.md)
therefore keeps (27) inside its exact coupled sum and its
complete Hermite trace, with the original
\(\kappa(-q)^D/N\) scalar. Its already paid small-index
subsets and physical-band restoration are unchanged. No
coefficientwise approximation of \(\mathscr A_N\), and no
discarded long-product tail, is used here.

This theorem supplies a polynomial amplitude on the whole
Casimir interval and a controlled complex spectral extension.
It does not estimate the other endpoint factorials, outgoing
polynomial, chirps, full terminal kernel, or their coupled
observation. It does not pay a new contour, its endpoints or
aliases, and proves no suppression or noncancellation of the
remaining transfer. In particular no uniform nonvanishing or
geometric-factor limit at the formerly excluded
\(\eta=0,T=1\) corner is asserted.
