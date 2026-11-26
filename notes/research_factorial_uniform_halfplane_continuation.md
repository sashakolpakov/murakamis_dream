# Uniform factorial asymptotics across the extended rectangle

Research lemma, 2 November 2026. The rectangular adjacent-pair
contour uses numerator arguments with \(\Re(x+y)\) greater
than one. Their imaginary parts stay strictly positive.
The canonical factorial has the same uniform asymptotic
there, with an explicitly continued branch. No estimate is
inferred merely from finite-level holomorphy.

## 1. The branch on the upper half-plane

For \(\Im z>0\), define
\[
 J_+(z)=\frac{i\pi}{2}z(1-z)
       +\frac{i}{2\pi}
             \{\operatorname{Li}_2(e^{2\pi iz})-\pi^2/6\}.
 \tag{1}
\]
The dilogarithm uses its convergent series in the unit disk.
Then
\[
 J_+'(z)=\log(1-e^{2\pi iz})+\frac{i\pi}{2}-i\pi z,
 \tag{2}
\]
which agrees with the original logarithm of \(2\sin\pi z\)
on \(0<\Re z<1\). Formula (1) also fixes its additive
constant. In particular
\[
 J_+(z+1)=J_+(z)-i\pi z,\qquad
 J_+'(z+1)=J_+'(z)-i\pi .
 \tag{3}
\]
The lower branch is \(J_-(z)=\overline{J_+(\bar z)}\).

## 2. Uniform asymptotic on any fixed upper compact set

**Lemma.** Let \(K\) be a compact subset of \(\Im z>0\).
For the original normalized factorial,
\[
 G_N(Nz)=
       \exp\!\left\{NJ_+(z)+\frac12\log N
                                  +\frac12J_+'(z)\right\}
                 (1+O_K(N^{-1})).
 \tag{4}
\]
The error is holomorphic and uniform on \(K\), and its
fixed derivatives have the same order on smaller compact
sets. Equivalently its prefactor is the continued branch
of \(\sqrt{2N\sin\pi z}\).
The conjugate assertion holds on lower compact sets.
For every fixed bounded offset \(c\), uniformly on such
a compact set,
\[
 G_N(Nz+c)=
   \sqrt{2N\sin\pi z}\,
     e^{NJ_\pm(z)}e^{cJ_\pm'(z)}
                     (1+O_K(N^{-1})).
 \tag{5}
\]

**Proof.** The [exact finite derivative](research_exact_cyclotomic_factorial.md)
is
\[
 \frac{d}{dz}\log G_N(Nz)
  =\sum_{k=0}^{N-1}F_z(k/N),\qquad
 F_z(t)=\pi(z-t)\cot\pi(z-t).
 \tag{6}
\]
It holds on the whole upper half-plane by continuation
from the defining Gamma product. The factorial is
nonzero there, so its logarithm is fixed by continuation
from the original strip.

The function \(F_z(t)\) and its fixed derivatives are
uniformly bounded for \(0\le t\le1\) and \(z\) in any
fixed upper compact set. The elementary Euler summation
formula consequently gives
\[
 \sum_{k=0}^{N-1}F_z(k/N)
 =N\int_0^1F_z(t)\,dt+\frac{F_z(0)-F_z(1)}2+O_K(N^{-1}).
 \tag{7}
\]
Here
\[
 \int_0^1F_z(t)\,dt=J_+'(z),\qquad
 F_z(0)-F_z(1)=\pi\cot\pi z=J_+''(z).
 \tag{8}
\]
For the first identity, differentiating its left side
gives \(F_z(0)-F_z(1)=\pi\cot\pi z\), the derivative of
\(J_+'(z)\). Their difference is constant. As
\(\Im z\to+\infty\), both are
\(-i\pi(z-1/2)+o(1)\), so that constant is zero.

It follows from (6)--(8) that
\[
 \frac{d}{dz}
 \left[\log G_N(Nz)-NJ_+(z)-\tfrac12J_+'(z)\right]
                                      =O_K(N^{-1}).
 \tag{9}
\]
Choose an anchor in \(0<\Re z<1\), \(\Im z>0\).
The original factorial asymptotic there fixes the
bracket in (9) to
\(\tfrac12\log N+O(N^{-1})\).
Join \(K\) to that anchor by bounded paths in a larger
fixed upper compact set and integrate (9).
This proves (4), with its actual constant and branch.
Cauchy's estimate on a slightly larger compact set
proves the derivative assertion. Conjugation proves
the lower version, and Taylor expansion at \(z+c/N\)
proves (5). \(\square\)

The exact \(N\)-shift provides a direct check on the
continued normalization:
\[
 G_N(N(z+1))=-2\sin(\pi Nz)G_N(Nz)
 =-i e^{-i\pi Nz}(1-e^{2\pi iNz})G_N(Nz).
 \tag{10}
\]
For \(\Im z\ge\eta>0\), the parenthesis is
\(1+O(e^{-2\pi N\eta})\). Equations (3)--(4) give
exactly the same multiplier: the action supplies
\(e^{-i\pi Nz}\), and the continued square root supplies
\(-i\). Thus crossing \(\Re z=1\) introduces neither an
unrecorded real constant nor a new choice of square root.

## 3. Application to the adjacent-pair contours

On every upper-\(x\) contour in the full-period identity,
\[
 \Im x=h_x,\qquad -h_y\le\Im y\le h_y,\qquad
                 h_x-h_y>0.
 \tag{11}
\]
Consequently the numerator argument \(z=x+y\) lies in
a fixed compact subset of the upper half-plane, even
when its real part crosses one. Lemma (4) supplies
the uniform expansion and upper bounds used on that
entire rectangle and its \(y\)-endpoint contours.
The \(x\)-denominator is also covered by (4).
The other factorials use their original regular-strip
or reciprocal-factorial estimates.

On the combined left side,
\(x=-1/(2N)+is\), a separate midpoint bound is required
at \(s=0\). The exact arguments there are
\[
 G_N(Nis-1/2),\qquad G_N(N(y+is)-1/2).
 \]
They are covered by the midpoint estimate in
[the uniform factorial note](research_uniform_factorial_and_boundary_decay.md).
The half-plane lemma is not being used at a zero
imaginary height where its compact-set hypothesis
would fail.
