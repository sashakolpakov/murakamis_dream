# A complete upper outer-cap alias at fixed height

Research deduction, 8 November 2026. The complete upper horizontal
alias of the original type-three cap can be placed at private
height one and bounded directly from its literal finite endpoint
sum. No endpoint saddle packet is needed on that line. The result
holds for every real ordinary color and includes all auxiliary rows.

This pays one complete outer current. It does not pay the longer
vertical sides of a rectangle reaching that line, the lower alias,
or the outer main path. No numerical evaluation or frozen-note
change is used.

## 1. Exact finite interpolation and cancellation of its carriers

Retain the notation and the exact cap interpolation of
[the original outer-contour source](research_mixed_cap_outer_contour_reduction.md):
\[
\begin{split}
C_N(e,w)&=\sum_{l=0}^{N-1}
 \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\\
D_N(z)&=\exp\!\left\{\frac{\pi i}{2}
                  [N(z-z^2)-z]\right\},\qquad
\Pi_N(z)=D_N(z)G_N(Nz),\\
\mathscr A_N(e,a,w)&=
 D_N(e)^{-1}C_N(e,w)\frac{\Pi_N(a+e)}{\Pi_N(a)}.
\end{split}                                                     \tag{1}
\]
The physical values of the last line are exactly
\(H_N(w,r^{-j})p_j(e^{-2\pi ia})/P_j\) at \(e=j/N\).
Every term of \(C_N\) is retained, even when it revives away
from a physical private index.

The defining polynomial in \(D_N\) gives the exact identity
\[
\frac{D_N(a+e)}{D_N(a)D_N(e)}=e^{-i\pi Nae}.
\]
Consequently the full row, not just its leading symbol, is
\[
\mathscr A_N(e,a,w)=
\sum_{l=0}^{N-1}
\frac{e_l(w)}{S_l}\,
e^{i\pi Ne(l/N-a)}
\frac{G_N(N(a+e))}
     {G_N(Na)G_N(N(e-l/N))}.
                                                               \tag{2}
\]
This formula keeps the original incoming and endpoint carriers.
There is no additional power of \(N\) or unimodular scalar.

Let
\[
\frac12\le a\le\frac7{10},\qquad e=E+i,\qquad
\frac18\le E\le\frac{49}{100}.
                                                               \tag{3}
\]
The same estimates below hold after an \(O(N^{-1})\) change
of either real endpoint of the \(E\)-interval. All numerator
and reciprocal arguments in (2), other than \(a\), have
imaginary part exactly one. They therefore lie in fixed
compact subsets of the original upper half-plane factorial
domain, including when \(\Re(a+e)>1\) or \(\Re(e-l/N)<0\).

## 2. The actual continued primitive at height one

Use the precisely normalized upper primitive from
[the uniform half-plane continuation, equations (1)--(5)](research_factorial_uniform_halfplane_continuation.md):
\[
J_+(z)=\frac{i\pi}{2}z(1-z)
 +\frac{i}{2\pi}
       \left\{\operatorname{Li}_2(e^{2\pi iz})-\frac{\pi^2}{6}\right\}.
                                                               \tag{4}
\]
For real \(x\), put \(\rho=e^{-2\pi}\). Its convergent defining
series, used here only as an analytic inequality, gives
\[
\left|\Re J_+(x+i)-\pi(x-\tfrac12)\right|
 \le\frac{\rho}{2\pi(1-\rho)}.
                                                               \tag{5}
\]
This is uniform for all real \(x\); the constant term in (4)
is purely imaginary. In particular, for \(u\in[0,1]\),
\[
\Re J_+(a+E+i)-\Re J_+(E-u+i)
\le\pi(a+u)+\epsilon_0,\qquad
\epsilon_0=\frac{\rho}{\pi(1-\rho)}<\frac1{297}.
                                                               \tag{6}
\]
For the last strict bound, \(\pi>3\) and
\[
e^{2\pi}>e^6>
 1+6+18+36+54=115>100
\]
imply \(\rho<1/100\). This is a finite elementary witness;
no value of a primitive, source sum, or stored result is evaluated.

The cited factorial theorem supplies the full uniform
asymptotic, hence upper and reciprocal lower bounds, for
the two upper arguments in (6). The denominator \(G_N(Na)\)
uses the original compact real-strip asymptotic. The continued
factorial has not been replaced by an arbitrary interpolation.
In particular its full-period factor
\(1-e^{2\pi iNz}\), when an argument crosses a period, is
already included in that theorem; it is not set equal to one
as a finite identity.

## 3. A positive bound for every auxiliary row

For every real ordinary color \(-2\le w\le2\), the literal
Newton product gives
\[
 |e_l(w)|\le\frac{4^l}{S_l^2}.
                                                               \tag{7}
\]
The original uniform physical sine-factorial estimate is
\[
S_l=\exp\{NJ(l/N)+O(\log N)\},\qquad 0\le l<N.
                                                               \tag{8}
\]
It holds through both true ends. Also
\[
-J(u)\le\frac16\quad(0\le u\le1),\qquad
J(a)\ge0\quad(\tfrac12\le a\le\tfrac7{10}),
                                                               \tag{9}
\]
by the original sine-chord and reflection identities. These
are, for example, equations (8) and (13) in
[the complex-index source](research_complete_boundary_complex_index.md).

Set \(u=l/N\). The carrier in (2) has modulus
\(\exp\{\pi N(a-u)\}\). Combining (6)--(9) with the
uniform factorial bounds gives, for every literal row,
\[
\begin{split}
\frac1N\log|\text{row in (2)}|
&\le u\log4-3J(u)-J(a)+2\pi a+\epsilon_0
                        +O(\log N/N)\\
&\le \log4+\frac12+2\pi a+\epsilon_0
                        +O(\log N/N).
\end{split}                                                     \tag{10}
\]
The inequalities are upper bounds also at any Newton zero.
Summing the \(N\) nonnegative row bounds changes only the
polynomial prefactor.

This elementary estimate is deliberately a whole-source
bound. It uses no compact-index endpoint asymptotic, no
termination at a nonphysical index, and no positivity
assertion about the signed endpoint sum.

## 4. The exact horizontal alias and its own-action gap

Choose any retained physical private interval whose half-grid
endpoints \(c_N,d_N\) lie in a fixed \(O(N^{-1})\) enlargement
of \([1/8,49/100]\). In the original cotangent residue identity,
let \(\mathcal H^+_N\) be its upper horizontal alias on
\([c_N,d_N]+i\), with its original orientation. The constant
mode is kept separate. On this line the exact cotangent
remainder has modulus at most
\[
\frac{2e^{-2\pi N}}{1-e^{-2\pi N}}.
                                                               \tag{11}
\]
The residue density is still \(+N\). Thus (10)--(11) imply
an upper exponential rate for the entire alias of at most
\[
\log4+\frac12-2\pi(1-a)+\epsilon_0
<\frac75+\frac12-\frac{3\pi}{5}+\frac1{297}
<\frac1{10}+\frac1{297}<\frac18.
                                                               \tag{12}
\]
Here \(\log2<7/10\) and \(\pi>3\) suffice. Polynomial
factorial errors, the finite \(l\)-sum, the contour length,
and the factor \(N\) in the residue formula have all been
included in the polynomial cost.

**Theorem.** For every \(\tau>0\), there are \(C_\tau,B_\tau\)
such that the complete original upper horizontal alias satisfies
\[
\sup_{\substack{1/2\le a\le7/10\\-2\le w\le2}}
|\mathcal H_N^+(a,w)|
\le C_\tau N^{B_\tau}e^{N(1/8+\tau)}
                                                               \tag{13}
\]
along both integer parities, with the same conclusion for
any of the retained intervals just specified.

The actual cap action \(\mathcal T(a)\) obeys
\[
\Re\mathcal T(a)>h(1-a)>\frac{41}{60}
                                                               \tag{14}
\]
by [the wall-action comparison](research_mixed_cap_wall_action_gap.md)
and [wrapped-row transport](research_mixed_cap_wrapped_row_transport.md).
The raw reserve in (13)--(14) is greater than
\(41/60-1/8=67/120>1/2\). After fixing one small tolerance
and absorbing polynomial factors, the complete upper alias
therefore has a finite own-action gap \(1/2\).

For fixed ordinary derivatives on \([-2,2]\), apply Markov's
inequality to each complete Newton polynomial in (7) before
summing the positive bound. This costs only powers of \(N\).
For small complex ordinary-color disks about \(-2\), the
polynomial interval bound and the usual degree-\(O(N)\)
ellipse estimate cost an arbitrarily small fixed exponential
tolerance. All factorial arguments on the upper line stay
in their proved compact domains under small complex
incoming perturbations. Keeping the base endpoints and paths
fixed, these bounds persist on fixed neighborhoods.
After multiplication by \(e^{-N\mathcal T(a,w)}\), Cauchy's
estimate on smaller neighborhoods gives every fixed mixed
jet, for example with finite gap \(1/3\).
No cutoff or reference-dependent contour is differentiated.

The new upper line is not, by itself, a complete outer
contour deformation. Any replacement of a shorter alias
rectangle by this one retains the intervening left and
right vertical currents. Their estimates, and the lower
alias and central path, remain independent obligations.
