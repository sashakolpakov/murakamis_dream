# The original factorial below the real axis

Research proof, 4 November 2026. This note proves continuation and boundary
estimates for the same factorial interpolation used in the original finite
sum. In particular, the estimates remain valid when a shifted index crosses
one full period. They do not by themselves evaluate that sum.

## 1. The interpolation and its full-period identity

For an integer \(N\ge2\), write \(r=e^{-2\pi i/N}\). Use the sine
interpolation from [the factorial construction](exact_factorial_interpolation_and_complex_contours.md):
\[
 G_N(w)=\left(\frac{2\pi}{N}\right)^w\Gamma(w+1)
 \prod_{k=1}^{\infty}
 \frac{\Gamma(Nk+w+1)}{\Gamma(Nk-w)(Nk)^{2w+1}},
 \qquad
 P_N(w)=e^{-i\pi w(w+1)/(2N)+i\pi w/2}G_N(w).                 \tag{1}
\]
The letter \(P_N\) here denotes the interpolation, not a new finite
polynomial. Positive-base powers have real logarithms. On
\(-1<\Re w<N\), this function is holomorphic and nonzero, and
\[
 P_N(0)=1,\qquad P_N(w+1)=(1-r^{w+1})P_N(w),\qquad
 P_N(j)=(r;r)_j\quad(0\le j<N).                              \tag{2}
\]
The infinite product also defines a holomorphic nonzero function on each
open half-plane \(\Im w>0\), \(\Im w<0\). All possible Gamma poles and
reciprocal-Gamma zeros are on the real axis. Local uniform convergence
follows from the same \(O(k^{-2})\) logarithmic remainder as in the
original strip. These definitions agree on their overlaps.

Iterating (2) exactly \(N\) times gives the meromorphic identity
\[
             P_N(w+N)=(1-e^{-2\pi i w})P_N(w).                \tag{3}
\]
The factor on the right is retained, including its zeros. There is no
division by it in the estimates below.

## 2. Uniform asymptotics on the whole lower half-plane

Define
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad a(z)=e^{-i\pi/4}\sqrt{1-e^{-2\pi iz}}
                      \qquad(\Im z<0).                      \tag{4}
\]
Here the dilogarithm is its convergent power series in the unit disk.
The square root is the analytic one with positive real part before
multiplication by \(e^{-i\pi/4}\). Thus both functions are single-valued
on the whole lower half-plane; \(a\) is nonzero.

**Theorem 1.** For every compact \(K\Subset\{\Im z<0\}\), uniformly
on \(K\),
\[
 P_N(Nz)=\sqrt N\,a(z)e^{Ng(z)}
       \exp\left\{\frac{\pi\cot\pi z}{12N}+O_K(N^{-3})\right\}.
                                                                    \tag{5}
\]
All fixed derivatives of the remainder have the same uniform order
on smaller compact sets. No restriction \(0<\Re z<1\) is imposed.

To prove this, apply the Gamma Stirling expansion directly to (1),
as in the strip proof. The arguments \(Nz\), \(N(k+z)\),
\(N(k-z)\) remain in closed sectors avoiding the negative real axis.
For the finitely many small \(k\), this follows from compactness and
the strictly negative imaginary part of \(z\). For all larger \(k\)
it follows from positive real parts. The summed remainders are
\(O_K(N^{-3})\): the large-\(k\) remainders are bounded by
\(C_KN^{-3}k^{-3}\), and the finitely many others have the same
order with a larger constant.

The leading terms and coefficients are the analytic continuations of
those in the original strip proof. This assertion concerns the explicit
Stirling expressions, not analytic continuation of an unproved error
estimate. Indeed their derivatives are the continued sine product and
cotangent partial fractions. On the connected lower half-plane they
agree with (4)--(5) on its intersection with \(0<\Re z<1\), and hence
everywhere. Equivalently, the continued sine primitive satisfies
\[
 J_-'(z)-i\pi z+i\pi/2=\log(1-e^{-2\pi iz}),
\]
which identifies the leading marked primitive with \(g\), including
its constant. The half-logarithm gives
\(\sqrt{2\sin\pi z}\,e^{-i\pi z/2}=a(z)\) with this same continued
branch. Cauchy's formula proves the derivative assertion. Higher
orders follow by retaining further Stirling terms.

Consequently (5) applies without a wall at \(\Re(s+a)=1\) or
\(\Re(s+b)=1\) on any fixed negative horizontal line, for real outer
parameters \(a,b\). The exact identity (3) remains valid throughout;
below the axis its multiplier is \(1+O(e^{-cN})\) on compact sets.

## 3. Exact moduli at the two ends of the original index range

Put \(w_0=-1/2+iNy\), with \(y\) real. In (1), the Gamma factors
in each numerator and denominator are complex conjugates, and
\((Nk)^{2w_0+1}\) has modulus one. Euler's Gamma reflection formula
therefore gives
\[
 |G_N(w_0)|^2=\frac{N}{2\cosh(\pi Ny)},\qquad
 |P_N(w_0)|^2=\frac{N}{1+e^{2\pi Ny}}.                       \tag{6}
\]
For the first equality use
\(|\Gamma(1/2+it)|^2=\pi/\cosh\pi t\). For the second,
\(w_0(w_0+1)=-1/4-N^2y^2\) is real, so the marked prefactor
has squared modulus \(e^{-\pi Ny}\). Applying (3) also gives
\[
 |P_N(N-1/2+iNy)|^2=N(1+e^{2\pi Ny}).                       \tag{7}
\]
These formulas include \(y=0\). They avoid a nonuniform Stirling
approximation at a factorial endpoint.

For real \(0<a,b<1/2\), set \(d=2+\epsilon\), where
\(\epsilon=0,1\), and define the literal interpolated row
\[
 T_N(s;a,b)=e^{2\pi iNa s}
       \frac{P_N(N(s+a))P_N(N(s+b))}{P_N(Ns)^d}.             \tag{8}
\]
The canonical finite source is exactly \(\sum_{j=0}^{N-1}T_N(j/N;a,b)\).
This follows from (2); it retains the two original outer factorials.

Let \(l_N=-1/(2N)\) and \(r_N=1-1/(2N)\). Formula (3) gives
\[
 \frac{T_N(r_N+iy)}{T_N(l_N+iy)}
 = e^{2\pi iNa}
   \frac{(1+t e^{-2\pi iNa})(1+t e^{-2\pi iNb})}{(1+t)^d},
 \qquad t=e^{2\pi Ny}.                                     \tag{9}
\]
It follows that
\[
              |T_N(r_N+iy)|\le(1+t)^{-\epsilon}
                           |T_N(l_N+iy)|\le|T_N(l_N+iy)|.    \tag{10}
\]
Only reality of \(a,b\) is used: their multiples by \(N\) need not
be integers. Zeros of the two numerator factors cause no difficulty.

**Lemma 2.** Fix \(K\Subset(0,1/2)^2\) and \(Y>0\). There are
\(C,N_0\) such that, for \((a,b)\in K\), \(-Y\le y\le0\)
and \(N\ge N_0\), both endpoint rows satisfy
\[
 |T_N(l_N+iy)|, |T_N(r_N+iy)|
 \le C N^{-\epsilon/2}e^{N H(y;a,b)},\quad
 H(y;a,b)=\Re g(a+iy)+\Re g(b+iy)-2\pi ay.                  \tag{11}
\]
This is exactly the lower-boundary real phase
\(\Re Q_\epsilon(iy+0^+;a,b)\), since \(\Re g(iy)=0\) for
\(y\le0\), with its continuous value at zero.

For the proof, both numerator arguments have scaled forms
\(a-1/(2N)+iy\), \(b-1/(2N)+iy\) in fixed compact subsets of the
original regular strip. Its uniform asymptotic formula bounds each
numerator by a constant times \(\sqrt N\) and its exponential in
(11). The shift by \(-1/(2N)\) changes that exponential by a bounded
factor, because \(g'\) is uniformly bounded there. Formula (6),
with \(0<t\le1\), bounds the denominator above and below by fixed
multiples of \(N^{d/2}\). The chirp has modulus \(e^{-2\pi Nay}\).
This proves the left estimate, and (10) proves the right one.

## 4. Exact reflection, including the shifted walls

The sine interpolation satisfies
\(G_N(\overline w)=\overline{G_N(w)}\), directly from (1).
Its marked prefactor therefore gives the exact identity
\[
 \frac{|P_N(N(x+iy))|}{|P_N(N(x-iy))|}
             =e^{\pi Ny(2x-1)+\pi y}.                      \tag{12}
\]
Combining the three factorial ratios and the chirp in (8) yields
\[
 \frac{|T_N(x-iy;a,b)|}{|T_N(x+iy;a,b)|}
 =\exp\left(2\pi Ny\{a-b+\epsilon(x-1/2)\}
                                  +\epsilon\pi y\right).  \tag{13}
\]
These identities hold wherever the quotients are defined; they may
also be written as multiplicative equalities across zeros. In the
residue rectangle used for (8), the denominator interpolation has
no zeros or poles. The identities do not reset a dilogarithm branch
at a shifted wall.

On any compact real parameter set, for \(0\le x\le1\),
\(|a-b+\epsilon(x-1/2)|\le\Lambda<1\). Thus a lower-horizontal
bound can be transferred to the upper cotangent remainder with the
strict exponential reserve \(2\pi N(1-\Lambda)y\), for \(y>0\).
The slight extension to \([l_N,r_N]\) costs only a bounded factor.
This is an estimate for both remainders of the original cotangent
kernel. The separate zero-mode integral, its deformation through a
critical point and its nonzero coefficient still require proof.

Reproduction: the exact identities and their powers of \(N\) are checked by

    python3 experiments/check_lower_half_factorial_continuation.py

The compact Stirling estimates and contour implications are the written
arguments above; a finite symbolic check is not an asymptotic theorem.
