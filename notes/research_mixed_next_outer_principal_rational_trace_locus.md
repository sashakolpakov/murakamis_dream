# A rational parametrization of the original paired principal trace locus

Private exact-source algebra, 8 November 2026. No mathematical numerical
evaluation, root test, saved-value calculation, or frozen-source edit is
used.

The original degree-eleven period characteristic has a rational trace
parametrization. On the complete physical middle arc, it replaces the
implicit characteristic by one degree-eleven polynomial in the new
parameter, without exceptional roots. The original signed outgoing
transpose is retained. This does not locate the resulting outgoing
image relative to the actual reference region, prove principal
avoidance there, or estimate a finite difference inverse.

## 1. The original characteristic pair

Use precisely the symbols of
[the paired Newton characteristic theorem, (23)--(30)](research_mixed_next_outer_paired_newton_characteristics.md).
Write
\[
\begin{split}
\mathsf X-2&=\frac{(x-1)^2(z+1)}x,\\
\mathsf Y-2&=\frac{(x-1)^2(z+1)}{xz},\\
\mathsf V-2&=-\frac{(x-1)^2(z+1)^2}{z},
\end{split}                                                       \tag{1}
\]
and
\[
V_0=\mathsf Y,\quad V_1=\mathsf V,\quad
V_{n+1}=8-\mathsf X V_n-V_{n-1}.
                                                                    \tag{2}
\]
The two principal equations are
\[
\begin{split}
\mathfrak b(x,z)
  &=(V_3^2-1)V_2+(\mathsf X-8)V_3+10=0,\\
Z&=\mathfrak j^{\mathrm t}(x,z)
 =\frac{3x-2+(x-1)z-(x-1)^2/z}{x^2}.
\end{split}                                                       \tag{3}
\]
The second equation is the signed transpose. Its normalization
includes the original factor \((-q)^b\); it is not the unsigned
conditional characteristic.

The physical arc is
\[
\mathcal X=\{e^{2\pi i t}:1/2\le t\le5/6\}
 =\{x:|x|=1,\ \Im x\le0,\ \Re x\le1/2\}.
                                                                    \tag{4}
\]
In particular \(x\ne0,1\). The original cleared characteristic
\(\mathsf P(x,z)=x^5z^3\mathfrak b(x,z)\) has degree eleven
in \(z\), with nonzero constant term on this arc.

## 2. Polynomial parametrization

For a new complex parameter \(p\), define the ordinary polynomials
\[
\begin{gathered}
A=p(p^2+p+2),\qquad B=p^2+1,\qquad C=p+1,\\
D=AB-C,\qquad E=AD+B,\qquad F=D+AE .
\end{gathered}                                                     \tag{5}
\]
All six polynomials in this note are evaluated at the same \(p\).
Direct algebra gives
\[
\begin{gathered}
CD+B^2=A^2,\qquad D^2-BE=-A^2,\qquad E^2-DF=A^2,\\
F=(A^2+2)D+C,\qquad
D=(p^2+p+1)(p^3+2p-1).
\end{gathered}                                                     \tag{6}
\]
For the first identity, \(BC+p-1=A\) and
\(B^2-C^2=A(p-1)\), so
\[
CD+B^2=ABC-C^2+B^2=A(BC+p-1)=A^2.
\]
The next two follow without expansion:
\[
D^2-BE=D(D-AB)-B^2=-CD-B^2,\qquad
E^2-DF=E(E-AD)-D^2=BE-D^2.
\]
The last two identities follow from \(AB=D+C\) and the
displayed definition of \(D\).

**Theorem.** Fix any \(x\in\mathcal X\). The solutions of
\(\mathfrak b(x,z)=0\) are in one-to-one correspondence with
the roots of the degree-eleven polynomial
\[
                         xF(p)-D(p)=0.                            \tag{7}
\]
At every such root \(A,D,E,F\) are nonzero, and the exact
correspondence and outgoing parameter are
\[
\boxed{\qquad
x=\frac D F,\qquad z=-\frac{A^2}{E^2},\qquad
Z=F^2+1-\frac{AF}{E}.
\qquad}                                                           \tag{8}
\]
There are no extra roots or unremoved exceptional denominators
in (7) for \(x\in\mathcal X\). No selected stationary branch
is imposed.

### Derivation from the original trace surface

The source theorem gives the invariant surface
\[
\mathcal F(X,Y,V)
 =X^2+Y^2+V^2+XYV-8(X+Y+V)+28=0.                  \tag{9}
\]
It is invariant under permutation and under replacement
\(Y\mapsto8-XV-Y\), since these are the two roots of
its monic quadratic in \(Y\). Thus (2) preserves the
surface.

With \(V_3\) fixed, introduce three further trace iterates
\[
W_0=\mathsf X,\quad W_1=V_2,\quad
W_2=8-V_3V_2-\mathsf X,\quad W_3=8-V_3W_2-V_2 .
                                                                    \tag{10}
\]
Exactly \(W_3=\mathfrak b-2\). On \(\mathfrak b=0\),
the invariant surface becomes
\[
 \mathcal F(V_3,W_2,-2)
       =(V_3-W_2)^2-8(V_3+W_2)+48=0.
\]
Set
\[
                         p=(V_3-W_2)/4 .                         \tag{11}
\]
This parametrizes the conic without an additional square root:
\[
V_3=2+(p+1)^2=2+C^2,\qquad
W_2=2+(p-1)^2 .
                                                                    \tag{12}
\]
Reverse (10) to obtain
\[
V_2=10-V_3W_2=1-2p^2-p^4=2-B^2,\qquad
\mathsf X=8-V_3V_2-W_2=2+A^2.                   \tag{13}
\]
The last equality follows, for example, by expanding its
nonconstant part as
\[
p^6+2p^5+5p^4+4p^3+4p^2
                   =p^2(p^2+p+2)^2.
\]
Reversing (2), with (6), gives the remaining original traces:
\[
                 \mathsf V=2+D^2,\qquad
                 \mathsf Y=2-E^2.                                \tag{14}
\]
Indeed
\[
8-(2+A^2)(2-B^2)-(2+C^2)=2+D^2,
\]
using \(A^2-B^2+C^2=ABC\); and
\[
8-(2+A^2)(2+D^2)-(2-B^2)=2-E^2,
\]
using \(D^2-BE=-A^2\).

For \(x\in\mathcal X\), every original root has \(z\ne0\).
Also \(z=-1\) is not a root: (1)--(2) would make all three
original traces and every \(V_n\) equal to two, and
\(\mathfrak b=4\). Consequently each of
\(\mathsf X-2,\mathsf Y-2,\mathsf V-2\) is nonzero.
Equations (13)--(14) therefore imply \(A,D,E\ne0\).

The ratio of the first two lines of (1) gives
\(z=-A^2/E^2\). The original parametrization also satisfies
\[
\mathsf X+\mathsf Y+\mathsf V-6
          =\frac{x-1}{x}(\mathsf V-2).
\]
Its left side is \(A^2-E^2+D^2=-ADE\), by (6).
Dividing by \(D\ne0\) yields \(F=D+AE=D/x\), proving
the first two equations of (8). In particular \(F\ne0\).

### Converse and denominator audit

The polynomials \(D,F\) have no common zero. In fact
\(D=0\) implies \(F=C\) by (6); if also \(F=0\), then
\(p=-1\), whereas direct substitution gives \(D(-1)=-4\).
For fixed \(x\ne0,1\), a root of (7) therefore has
\(D,F\ne0\). If \(A=0\) or \(E=0\), the relation
\(F=D+AE\) would give \(F=D\), forcing \(x=1\).
Thus all four required denominators and numerators are
nonzero at every root of (7).

Set \(x=D/F\) and \(z=-A^2/E^2\). The identities (6) give
\[
 x-1=-\frac{AE}{F},\qquad
 z+1=\frac{DF}{E^2}.                                               \tag{15}
\]
Substitution into (1) recovers exactly
\((\mathsf X,\mathsf Y,\mathsf V)
 =(2+A^2,\,2-E^2,\,2+D^2)\).
The reversed recurrences above then give \(W_3=-2\),
and hence \(\mathfrak b=0\).
The inverse (11) recovers \(p\) uniquely, proving the
asserted correspondence.
Finally \(A,D,E,F\) are monic of degrees \(3,5,8,11\);
the polynomial (7) has degree eleven and leading
coefficient \(x\ne0\).

### The signed outgoing map

Substitute (15) and \(z=-A^2/E^2\) directly into the second
line of (3). It gives
\[
Z=\frac{F(D-2AE)+A^3F/E+E^4}{D^2}.
\]
Use \(A^2-E^2=-DF\) from (6). The numerator becomes
\[
D^2+(A^2-E^2)^2+\frac{AD}{E}(A^2-E^2)
       =D^2+D^2F^2-\frac{AD^2F}{E}.
\]
This is exactly the last equation of (8). In particular the
map has not replaced the signed transpose by either the
unsigned recurrence or its reciprocal shift.

## 3. The remaining actual avoidance question

Define the compact parameter locus
\[
\begin{split}
\Gamma=\{p\in\mathbb C:\quad
 &|D|^2=|F|^2,\quad
 \Im(D\overline F)\le0,\\
 &\Re(D\overline F)\le\tfrac12|F|^2\}.
\end{split}                                                       \tag{16}
\]
The denominator audit shows that \(F\) does not vanish
on this set and that (16) is exactly \(D/F\in\mathcal X\).
It is bounded: \(D/F\to0\) as \(p\to\infty\), so a sequence
in (16) cannot escape to infinity. It is closed by its
displayed polynomial equalities and inequalities, hence compact.
Also \(A,E\ne0\) throughout \(\Gamma\), by the same audit.

For the original exceptional set of
[the principal Bezout criterion](research_mixed_next_outer_principal_bezout_criterion.md),
the theorem proves the exact image description
\[
\boxed{\qquad
\Sigma=\left\{F(p)^2+1-\frac{A(p)F(p)}{E(p)}:
                                      p\in\Gamma\right\}.
\qquad}                                                           \tag{17}
\]
This is a complete real algebraic parameter test, not a
choice of geometric component.

For the actual complete words in powers three and four beginning
\(343\), of length at least five, the
[original outgoing source domain](research_mixed_next_middle_weighted_outgoing_kernel.md)
has \(Z_*=e^{-2\pi i z_*}\), with
\(\Re z_*\in[3/10,39/100]\) and
\(\Im z_*\in(-3/100,1/50)\), together with its original
coupled-reference constraints. No inequality proved above
excludes that region from (17). In particular
\(|D|=|F|\) alone does not furnish a sign for the real or
imaginary part of the outgoing map. Uniform avoidance,
avoidance of an individual actual reference, and any
resulting finite-operator estimate remain unproved.
