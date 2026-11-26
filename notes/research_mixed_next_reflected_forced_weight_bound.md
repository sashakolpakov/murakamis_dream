# The complete forced weight on the reflected lower-right domain

Private research proof, 8 November 2026. The original Fourier
polynomial has arbitrarily small exponential rate on the whole
closed upper half-annulus inside the unit disk. The statement
includes the negative real radius and the positive real radius.
Its neighborhood is chosen after the exponential tolerance.

This controls the entire forced weight in the reflected
lower-right source at every actual depth. It leaves the original
prefix and the reversed conditional observation coupled. No estimate
for that remaining product, numerical evaluation, or change to a
frozen source is made.

## 1. Original finite weight and the half-annulus

Let \(N\ge2\), \(D=N-1\), \(r=e^{-2\pi i/N}\), and
\(P_b=(r;r)_b\). Keep the unique polynomial
\[
 \deg d_N\le D,\qquad d_N(r^b)=P_b^{-1},\qquad 0\le b<N.
\tag{1}
\]
Its full exact recurrence is
\[
 d_N(r^{-1}Y)=(1-Y)d_N(Y)
                     +\frac{Y}{N^2}\sum_{k=0}^D Y^k.
\tag{2}
\]
The last term is not discarded.

For \(0<r_0<1\), set
\[
 \mathcal K_{r_0}
   =\{Y:r_0\le|Y|\le1,\ \Im Y\ge0\}.
\tag{3}
\]

**Theorem.** For every \(\tau>0\), there are a bounded open
neighborhood \(\mathcal U_\tau\) of \(\mathcal K_{r_0}\),
separated from zero, and constants \(C_\tau,B_\tau\) such that
\[
 \sup_{Y\in\mathcal U_\tau}|d_N(Y)|
                   \le C_\tau N^{B_\tau}e^{\tau N}.
\tag{4}
\]
This holds at both level parities. Every fixed complex derivative
has the corresponding bound on a smaller neighborhood of
\(\mathcal K_{r_0}\).

In particular, on the closed set (3) the upper exponential rate
is at most zero. The theorem does not assert that one fixed
neighborhood works for every arbitrarily small \(\tau\).

## 2. The sign of the original primitive, including the negative axis

On \(0<\Re y<1\), use the original primitive and logarithmic lift
\[
 g'(y)=\operatorname{Log}(1-e^{-2\pi iy}),\qquad
 g(y)=\frac{\operatorname{Li}_2(e^{-2\pi iy})-\pi^2/6}{2\pi i}
 \quad(\Im y\le0).
\tag{5}
\]
The second equality is
[Fourier-weight continuation, equation (22)](research_mixed_fourier_weight_continuation.md),
with its additive constant fixed in the original strip.

For \(Y=Re^{i\theta}\), \(0<R\le1\), \(0<\theta<\pi\),
the same defining integral gives
\[
 \Im\operatorname{Li}_2(Re^{i\theta})
    =-\int_0^R\frac{\operatorname{Arg}(1-te^{i\theta})}{t}\,dt>0.
\tag{6}
\]
Here \(1-te^{i\theta}\) has negative imaginary part, so its
continuous argument is strictly negative. There is no change
of logarithmic lift. At \(\theta=0,\pi\), the imaginary part
in (6) extends to zero. Continuity follows, including \(R=1\),
from the uniformly absolutely convergent series
\(\sum_{k\ge1}Y^k/k^2\) on the closed unit disk.

For
\[
y=q+ih,\qquad 1/2\le q<1,\qquad
\log r_0/(2\pi)\le h\le0 ,
\]
one has \(\theta=2\pi(1-q)\). Equations (5)--(6) give
\[
 \Re g(y)\ge0.
\tag{7}
\]
Equality holds on the negative radius \(q=1/2\).
This radius is an interior real coordinate of the original
strip; it is not a limiting use of that strip at an endpoint.
The sign is strictly positive for \(1/2<q<1\), and tends
continuously to zero at the positive radius.

The original absolute, rather than relative, Fourier estimate is
\[
 |d_N(e^{-2\pi iy})|
 \le C_{E,\varepsilon}N^{-1/2}
 \exp N\left(
 \max\{-\Re g(y),\,2\pi\max(\Im y,0)\}+\varepsilon\right)
\tag{8}
\]
for every compact \(E\subset\{0<\Re y<1\}\) and every
\(\varepsilon>0\). This is the estimate immediately preceding
Theorem 1 in Section 5 of
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md).
Its proof includes the exact interpolation remainder and all
four sides of the residue rectangle. In particular (8) does
not assume that \(d_N\) is relatively close to an inverse
factorial when the latter is exponentially small.

By (7), the maximum in (8) is zero on every closed substrip
with \(1/2\le q\le1-\alpha\), for \(\alpha>0\).
By continuity it is arbitrarily small on a sufficiently
small fixed neighborhood of that substrip. This covers
the whole negative real radius uniformly, including \(-1\).

## 3. Close the positive radius with the full forced recurrence

The remaining boundary is the positive segment \([r_0,1]\).
[Lemma 1 of the lower-radial theorem](research_mixed_next_lower_radial_seam.md)
proves that, for every tolerance \(\varepsilon>0\), there is
a fixed complex neighborhood of this entire segment on which
\[
                       |d_N(Y)|\le C_\varepsilon N^B e^{\varepsilon N}.
\tag{9}
\]
Its proof is important here: it uses (8) on a small positive
real-coordinate strip and then iterates the complete recurrence
(2). On the intervening rotations one has a fixed \(q_0<1\)
with \(|1-r^kY|\le q_0\), and the full forcing is bounded by
\[
 \left|\frac{r^kY}{N^2}\sum_{\nu=0}^D(r^kY)^\nu\right|
       \le N^{-1}\max(1,|Y|)^N .
\tag{10}
\]
The resulting geometric sum retains every forcing term.
Thus (9) covers \(Y=1\), rather than extrapolating (8)
through a logarithmic boundary point.

To assemble (4), first apply (9) with tolerance \(\tau/3\).
Its open neighborhood contains all radii in (3) whose angles
are sufficiently close to zero, by compactness of \([r_0,1]\).
Choose \(\alpha>0\) so this includes \(1-\alpha\le q\le1\).
The remaining compact substrip
\[
[1/2,1-\alpha]+i[\log r_0/(2\pi),0]
\]
lies strictly inside the original strip. Choose a small
neighborhood on which the maximum in (8) is less than
\(\tau/3\), and then use \(\varepsilon=\tau/3\) there.
The two neighborhoods cover (3). A smaller bounded open
neighborhood with closure in their union may be chosen
away from zero. Taking the larger of the finite constants
proves (4), after adjusting it for finitely many smaller
levels if necessary.

Apply Cauchy's formula on a further smaller neighborhood
to prove the derivative assertion. The neighborhood depends
on \(\tau\) throughout this construction.

## 4. Exact consequence for the complete reflected source

Use the complete finite source and reflection conventions of
[the exact lower-complement reflection theorem](research_mixed_next_lower_complement_exact_reflection.md):
\[
\begin{gathered}
 A_N(Y,Z)=E_N(Y)d_N(Y)C_{\beta,N}(Y,Z),\\
 E_N^\sharp(V)=V^D E_N(V^{-1}),\qquad
 d_N^\sharp(V)=V^D d_N(V^{-1}),\\
 C_{\beta,N}^{\leftarrow}(V,Z)
                  =V^{-D}C_{\beta,N}(V^{-1},Z),\\
 \widehat A_N(V,Z)
      =V E_N^\sharp(V)d_N^\sharp(V)
                              C_{\beta,N}^{\leftarrow}(V,Z).
\end{gathered}
\tag{11}
\]
Here \(E_N\) is either the full actual prefix \(F_{34,N}\) or
its exact old \(11/12\) filtered polynomial. No estimate or
positivity assumption about that prefix is needed for this
corollary.

Let
\[
 \mathcal K_{r_0}^{-1}
    =\{V:1\le|V|\le r_0^{-1},\ \Im V\le0\}.
\]
Inversion of a sufficiently small neighborhood in (4) gives
\[
 \boxed{\quad
 |V|^{-D}|d_N^\sharp(V)|
       =|d_N(V^{-1})|
       \le C_\tau N^{B_\tau}e^{\tau N}.
 \quad}
\tag{12}
\]
All reversed forcing and the exceptional physical value
\(d_N^\sharp(1)=1\) remain exactly as in the reflection theorem.
Equation (12) is not a homogeneous approximation to that weight.

The selected inverse power of the reflected full source now
has the exact factorization
\[
 V^{-N}\widehat A_N(V,Z)
  =\bigl(V^{-D}d_N^\sharp(V)\bigr)
                         E_N^\sharp(V)C_{\beta,N}^{\leftarrow}(V,Z).
\tag{13}
\]
Consequently
\[
 \boxed{\quad
 |V^{-N}\widehat A_N(V,Z)|
 \le C_\tau N^{B_\tau}e^{\tau N}
             |E_N^\sharp(V)C_{\beta,N}^{\leftarrow}(V,Z)|.
 \quad}
\tag{14}
\]
This is a zero-safe multiplicative estimate and holds for
every \(Z\). The right side still contains the actual
coupled prefix and observation. No factor depending
exponentially on the actual radial depth has been charged
for the full Fourier weight.

For the actual lower period, take
\[
 r_0=e^{-51\pi/250},\qquad
 -51/500\le h_y<0,\qquad 1/2\le q\le1 .
\tag{15}
\]
This inner radius is greater than \(1/2\):
\(51\pi/250<561/875<2/3<\log2\).
Under \(\zeta=1-(q+ih_y)\), (12)--(14) apply on the
entire reflected interval \([0,1/2]-ih_y\), at its
actual height. The exact original \(+N\) measure and
the sign of the paired meromorphic integral are those
of equations (24)--(26) in the reflection theorem.

The result therefore removes a separate exponential
Fourier-weight cost throughout the full requested depth.
A bound for \(E_N^\sharp C_{\beta,N}^{\leftarrow}\),
with its original correlations and Fourier sectors, is
still required to pay the remaining lower-right integral.
No bound for that product or complete attachment
asymptotic is asserted.

