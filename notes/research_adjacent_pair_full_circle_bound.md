# A uniform bound for the complete lower circle

Research lemma, 2 November 2026.

The finite adjacent-pair sum can be extended from its triangular
index set to a rectangle: the additional lattice terms vanish.
Once this extension is made, each lower contour in the first variable
traverses a complete circle. The exact normalization of the factorials
then cancels its main part. The estimate below is uniform in the
second variable, including its vertical endpoint contours.

This lemma concerns the lower first-variable contour. The upper
contour and the two combined vertical sides still require their own
estimates.

## 1. The exact form and the parameter region

Use the exact summand \(f_N(x,y;u)\) and the functions
\(C_N,\Phi_N,R_N\) of
[the cyclotomic normalization](research_adjacent_pair_cyclotomic_gauge.md).
Fix \(\epsilon=10^{-6}\), and set
\[
 h_y=\frac{\log7}{4\pi},\qquad
 h_a=\frac{\log2}{4\pi},\qquad
 \mathcal Y=\{y:\epsilon\le\Re y\le1/2-\epsilon,
                         -h_y\le\Im y\le h_a\}.
\]
The endpoints of the actual half-grid intervals can differ from
these limits by \(O(N^{-1})\). All bounds below hold on a fixed
slightly larger rectangle, after enlarging constants and reducing
the final strict margin.

Let \(a_N=-1/(2N)\). For \(y\in\mathcal Y\), consider
\[
 I_N(y,u)=\int_{a_N}^{a_N+1}
   \frac{f_N(t-i,y;u)}{e^{2\pi iN(t-i)}-1}\,dt.
 \tag{1}
\]
This includes every lower Fourier mode, through the original
rational denominator. Put
\[
 w=e^{-2\pi ix},\quad Y=e^{2\pi iy},\quad r=e^{-2\pi},
 \quad \rho=\sqrt2\,r.
\]
On (1), \(|w|=r\) and
\(|w/Y|\le\rho<1/256\). The latter bound follows, for example,
from \(\pi>3\) and \(\log2<7/10\).

The exact formula already proved for this summand is
\[
 \frac{f_N(x,y;u)}{e^{2\pi iNx}-1}\,dx
 =-\frac{C_N(y,u)}{2\pi i}
       \frac{e^{\Phi_N(w,Y)}e^{x\log R_N(w,Y)}}{1-w^N}\,dw.
 \tag{2}
\]
The logarithm of \(R_N\) vanishes at \(w=0\). Without the
factor \(e^{x\log R_N}\), the form on the right is holomorphic
on the entire disk \(|w|<\min(1,|Y|)\). Its integral on the
complete circle is therefore zero. The angular lift in (1) has
bounded \(|x|\), uniformly in \(N\).

## 2. A bound for the coefficient

At zero boundary angle the exponential rate of \(C_N\) is
\[
 V(y)=-6J(y)+J(2y)+i\pi y^2-i\pi/6.
 \tag{3}
\]
Here \(J'(z)=\log(2\sin\pi z)\), with its continuation from
\(0<z<1\). Uniform factorial estimates on the fixed rectangle give
\[
 |C_N(y,0)|\le C N^A e^{N\Re V(y)}.
 \tag{4}
\]
Only an upper bound is needed; no nonvanishing assertion is used.

For \(0\le a\le1\), the upper-half-plane formula for \(J\)
and its conjugate on the lower half-plane imply
\[
 |\Re J(a+ib)|\le
       \frac\pi2 |b|\,|1-2a|+\frac\pi{12}.
 \tag{5}
\]
Indeed the dilogarithm series is bounded in absolute value by
\(\sum_{k\ge1}k^{-2}=\pi^2/6\); its boundary values follow
by continuity. Applying (5) to \(y=a+ib\) and \(2y\), with
\(0\le a\le1/2\), gives
\[
 \Re V(y)\le5\pi |b|+\frac{7\pi}{12}
 \le\frac54\log7+\frac{7\pi}{12}<\frac{13}{3}.
 \tag{6}
\]
The final inequality uses \(\log7<2\) and \(\pi<22/7\).

For every real \(u\in[-\pi,\pi]\), the
[Newton boundary estimate](research_uniform_factorial_and_boundary_decay.md)
does not increase this upper exponent. Thus (4), with the bound
\(13/3\), holds uniformly in the entire real boundary period.
It also holds with a slightly larger constant exponent on a
sufficiently thin fixed complex strip in \(u\). This follows
from the same reciprocal-factorial estimate and continuity of its
real primitive across its moving zeros.

## 3. Cancellation and its error

The convergent series in the exact normalization give
\[
 |\log R_N|\le\frac{4\rho^N}{1-\rho^N},
 \qquad
 |\Phi_N|\le\frac{2N\rho}{1-\rho}+C\rho^N.
 \tag{7}
\]
The constant in the second inequality is uniform for
\(y\in\mathcal Y\). To check its term proportional to \(N\),
use \(\sum_{k=0}^{N-1}k/N=(N-1)/2\) on the four logarithms
in the exact cyclic formula. The remaining logarithm and
dilogarithm terms are bounded by \(C\rho^N\).

Subtract the zero integral of the holomorphic form from (2).
For the resulting error, use
\[
 |e^{x\log R_N}-1|
 \le |x|\,|\log R_N|e^{|x||\log R_N|}.
\]
The circle length and \((1-w^N)^{-1}\) are uniformly bounded.
Equations (4), (6), and (7) therefore bound the exponential rate
of (1) by
\[
 \frac{13}{3}+\frac{2\rho}{1-\rho}+\log\rho
 <\frac{13}{3}+\frac2{255}-\frac{16}{3}
 =-1+\frac2{255}<-\frac12.
 \tag{8}
\]
Here \(\rho<1/256\) and \(\log2>2/3\) were used.
Consequently, for all sufficiently large \(N\),
\[
 \boxed{\displaystyle
 |I_N(y,u)|\le C N^A e^{-N/2}}
 \tag{9}
\]
uniformly on the stated rectangle and real angular period. A
slightly weaker negative exponent holds on a fixed thin complex
strip in \(u\) and for the actual half-grid endpoint perturbations.
No parity condition on \(N\) occurs in this argument.

## 4. Use in the iterated residue formula

On the lower first-variable contour, the second-variable paths
have upper height \(h_a\) and lower height \(-h_y\). These
paths, their endpoints, and their residue kernels do not depend
on \(\Re x\). Hence one can first perform the complete circle
integral (1), at each fixed point of the second-variable contour.
Its horizontal correction kernels are uniformly bounded, and its
vertical endpoint kernel has absolute value at most one.
Polynomial factors of \(N\) are absorbed into (9).

Thus (9) bounds all four terms containing the lower
first-variable correction, including the term whose second
variable is on a vertical endpoint. One need not estimate the
absolute value of the uncancelled integrand on these surfaces.
This conclusion depends on the exact rectangular extension; it
does not apply to a triangular row ending at a moving diagonal.
