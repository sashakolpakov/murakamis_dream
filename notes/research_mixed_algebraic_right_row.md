# An exact polynomial for the maximizing raw right-boundary row

Research deduction, 5 November 2026. Once the real right angle has
been fixed at \(1/2\), its continuous raw row maximum is determined
by a quartic or sextic with exactly one positive root. Polynomial
signs locate that root relative to any trial row; in particular,
several physical cases have a sharper quarter-row bracket. This
concerns the complete absolute upper envelope, not the value or
noncancellation of the original finite sum.

The earlier
[angular candidate theorem](research_mixed_angular_support_candidates.md)
holds the row fixed and varies its other angle. Its quadratic/sextic
is a different equation. The special real endpoint maxima in
[the two-right theorem](research_mixed_two_right_source_bound.md),
equations (7)--(8), are recovered by the present equation. No
Weyl identity, finite Fourier transport or new torsor interpretation
is claimed.

## 1. The literal reduced row and its signed-height parameter

Use the original real primitives
\[
 J(t)=\Re g(t),\qquad
 G_H(t)=\Re g(t-iH),\qquad
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
                                                               \tag{1}
\]
Let the other target be \(z=y+ih\), put \(H=|h|\), and let
\(d=1\) when this target is the first argument of the kernel.
The part of the original raw exponent depending on its row is
\[
\begin{split}
 E(u)&=J(u+1/2)+G_H(y+u)-(2+\epsilon)J(u)+\lambda u,\\
 \lambda&=2\pi(h_+-dh),\qquad
 r=e^{-2\pi H},\qquad L=e^{2\lambda},\qquad \epsilon\in\{0,1\}.
\end{split}                                                     \tag{2}
\]
All Fourier alternatives, half allocations and selected monomials
at the fixed target are independent of \(u\). They remain in the
source bound but do not change this maximizing row.

The height/orientation table is
\[
\begin{array}{c|cc}
 &d=0&d=1\\ \hline
 h<0&L=1&L=r^{-2}\\
 h>0&L=r^{-2}&L=1\\
 h=0&L=1&L=1 .
\end{array}                                                     \tag{3}
\]
In particular the formula \(L=e^{-4\pi dh}\) alone applies on
the negative-height sheet, not on the positive-height sheet.

The algebraic statement below holds for
\[
              0\le y\le1/2,\qquad 0<r\le1,\qquad L>0.           \tag{4}
\]
For the literal full-row application we use (3) and \(H\le.057\).
The [complete right-row theorem](research_mixed_complex_right_row_reduction.md)
then disposes of every upper row before maximizing (2) on
\([0,1/2]\). Its strict concavity proof also applies directly to
(2): \(E''\le-2\pi\), and the derivative tends to \(+\infty\)
and \(-\infty\) at the two row endpoints. The possible logarithmic
zeros at \(H=0,y=0\) or \(1/2\) are endpoint limits; there are
no zeros inside \(0<u<1/2\).

## 2. Polynomial equivalence and uniqueness without root proposals

Set
\[
\begin{split}
 A&=\cos(2\pi y),\qquad B=\sin(2\pi y)\ge0,\qquad w=\tan(\pi u)>0,\\
 P&=1+r^2-2rA,\qquad Q=4rB,\qquad R=1+r^2+2rA,\\
 F_\epsilon(w)
   &=4^{1+\epsilon}w^{4+2\epsilon}
                   -L(P+Qw+Rw^2)(1+w^2)^\epsilon .
\end{split}                                                     \tag{5}
\]
The symbol \(R\) in (5) is a polynomial coefficient, not the
contour's right taper.

**Theorem 1.** The unique maximizing row \(u_*\in(0,1/2)\)
is
\[
                 u_*=\pi^{-1}\arctan w_*,
 \qquad F_\epsilon(w_*)=0,\qquad w_*>0.                       \tag{6}
\]
The polynomial \(F_\epsilon\) has exactly one positive root,
which is simple. For every \(w_0>0\),
\[
\begin{array}{c|ccc}
 F_\epsilon(w_0)&<0&=0&>0\\ \hline
 w_0\text{ versus }w_*&w_0<w_*&w_0=w_*&w_0>w_*\\
 E'(\pi^{-1}\arctan w_0)&>0&=0&<0 .
\end{array}                                                     \tag{7}
\]
No complex polynomial root is being identified with a conditional
stationary phase in this statement.

**Proof.** On the open row interval,
\[
 E'(u)=\log(2\cos\pi u)
      +\log|1-r e^{-2\pi i(y+u)}|
      -(2+\epsilon)\log(2\sin\pi u)+\lambda .
                                                               \tag{8}
\]
All factors inside these logarithms are strictly positive.
The tangent substitution gives the exact identities
\[
 |1-r e^{-2\pi i(y+u)}|^2
      =\frac{P+Qw+Rw^2}{1+w^2},\qquad
 e^{2E'(u)}
      =\frac{L(P+Qw+Rw^2)(1+w^2)^\epsilon}
                  {4^{1+\epsilon}w^{4+2\epsilon}} .
                                                               \tag{9}
\]
Thus exponentiating and squaring introduces no sign ambiguity,
and stationarity is precisely \(F_\epsilon(w)=0\).

For completeness, uniqueness follows directly from the coefficients,
without a root count theorem. They obey
\[
 P=(1-r)^2+2r(1-A)\ge0,\quad Q\ge0,\quad
 R=(1-r)^2+2r(1+A)\ge0,\quad P+R=2(1+r^2)>0 .
                                                               \tag{10}
\]
Writing \(n=4+2\epsilon\), the nonzero coefficients \(a_j\) in
\((P+Qw+Rw^2)(1+w^2)^\epsilon=\sum_{j=0}^{n-2}a_jw^j\)
are nonnegative. In increasing powers they are
\[
 \epsilon=0:\ (P,Q,R),\qquad
 \epsilon=1:\ (P,Q,P+R,Q,R).                                  \tag{11}
\]
At least one is positive. Consequently
\[
 T(w):=\sum_{j=0}^{n-2}a_jw^{j-n}
\]
is strictly decreasing from \(+\infty\) to zero on \(w>0\).
The equation \(4^{1+\epsilon}=LT(w)\) has exactly one
solution. Also
\(F_\epsilon'(w_*)=-Lw_*^nT'(w_*)>0\), proving simplicity
and the root-side signs in (7). Equation (9) gives the derivative
signs. The endpoint signs of \(E'\), or its already established
strict concavity, identify that root as the global row maximum.

This includes \(r=1,y=0\), where \(P=Q=0\) and the displayed
polynomial has an additional zero at \(w=0\). That zero is outside
the open substitution domain and is never a candidate in (6).
At \(r=1,y=1/2\), \(Q=R=0\); the same proof applies.
\(\square\)

For rational trial \(w_0>0\), (7) is a polynomial sign test in
the physical parameters \(r,A,B\). When \(L=r^{-2}\), multiply
by the positive quantity \(r^2\) to clear its denominator.
For general real parameters the coefficients need not be algebraic
numbers: the assertion is algebraicity over those retained
parameters. Certified interval signs can likewise locate the root
on a whole parameter box. A numerical polynomial root proposal
without such validation is not a certificate.

## 3. Exact quarter-row decisions

Put \(N_0=1+r^2+2rB\). At \(w=1\),
\[
 e^{2E'(1/4)}=\frac{LN_0}{2^{1+\epsilon}},\qquad
 F_\epsilon(1)=2^{1+\epsilon}
                     \{2^{1+\epsilon}-LN_0\}.                \tag{12}
\]
It follows that \(u_*\) is above, equal to, or below \(1/4\)
according as \(LN_0-2^{1+\epsilon}\) is positive, zero,
or negative.

Two uniform physical cases are especially useful:

* If \(\epsilon=1,L=1\), then \(u_*\le1/4\).
  Equality holds exactly when \(r=1\) and \(y=1/4\).
* If \(\epsilon=0,L=r^{-2}\), then \(u_*\ge1/4\).
  Equality holds exactly when \(r=1\) and
  \(y\in\{0,1/2\}\).

Indeed the exact nonnegative decompositions are
\[
 4-N_0=(1-r)(3+r)+2r(1-B),\qquad
 N_0-2r^2=(1-r)(1+r)+2rB .                                  \tag{13}
\]
They also give all the asserted equality cases. The two remaining
physical combinations have the explicit tests
\[
\begin{array}{c|c}
(\epsilon,L)&\text{sign quantity}\\ \hline
(0,1)&r^2+2rB-1=2r\{B-\sinh(2\pi H)\},\\
(1,r^{-2})&1+2rB-3r^2 .
\end{array}                                                     \tag{14}
\]
The second row has been multiplied by \(r^2>0\).

For the moving minimum \(y=t\in[.12,.22]\), the first row of
(14) is strictly positive whenever \(H\le.057\). In fact,
the [uniform row bracket](research_mixed_right_boundary_row_bracket.md)
proved \(r>2/3\), while
\[
 \sin(2\pi t)>\frac12,\qquad
 \sinh(2\pi H)=\frac{r^{-1}-r}{2}<\frac5{12}<\frac12 .
                                                               \tag{15}
\]
The sine inequality follows from
\(1/12<.12\le t\le.22<5/12\).
Therefore an own-type-three raw edge at any moving minimum has
\[
                         1/4<u_*<2/5                         \tag{16}
\]
for both physical \(L\) choices. On the other hand, an own-type-four
raw edge with \(L=1\) has
\[
                         1/5<u_*\le1/4.                      \tag{17}
\]
For a moving minimum (17) is strict at its upper endpoint, since
\(t<1/4\). In particular an unselected type-four A endpoint on
the second side of a raw edge has \(\epsilon=1,d=0,h\le0\),
and hence (17). The second row of (14), rather than an unsupported
uniform quarter choice, is retained for the other own-type-four
orientation/height combinations.

The concavity and height-only monotonicity in the
[raw derivative theorem](research_mixed_raw_row_stationarity.md)
remain valid on any subinterval of its old bracket.
Thus (16) allows the two derivative trial rows \(1/4,2/5\);
(17) allows \(1/5,1/4\), with the same orientation-dependent
height-only endpoint choice. On a domain where another polynomial
trial sign is certified uniformly, the bracket can be sharpened
in the same way without altering the shared outer variables.
No nonnegativity of the resulting whole minimum-flow derivative
is implied by this refinement.

## 4. Verification and source scope

The focused checker proves the tangent identities, both expanded
polynomials, all divided-equation coefficient identities, the
quarter decisions and their nonnegative decompositions, the signed
height table, and the rational inequalities used in (15). It binds
the completed full-row and derivative theorems and their saved
records. There are no new root proposals, parameter cells, row
samples or cyclic-word enumerations.

The raw polynomial retains the same row maximizer for every actual
selected or forcing alternative because those alternatives differ
only by row-independent terms. Those terms must be restored when
evaluating the source ceiling. All finite rows and both level
parities remain covered by the earlier full-row reduction; no
assumption that \(N/4\) is an integer is used.

The conclusion is an exact description of a continuous absolute
upper envelope. It is neither a lower bound for the original
oscillatory kernel, nor an identification of this real row with a
zero-logarithmic-lift complex saddle. It proves no full-period
noncancellation or new knot-family statement.

    python3 experiments/check_mixed_algebraic_right_row.py
    python3 experiments/check_mixed_algebraic_right_row.py --input repro/results/research-mixed-algebraic-right-row.json --output /tmp/research-mixed-algebraic-right-row-replay.json
