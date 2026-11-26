# Both complete left cap currents at the exact later incoming point

Research deduction, 8 November 2026. At the exact later incoming
point, the early auxiliary-real curve gives a positive bound for
every auxiliary row at the real private cut \(1/8\). Both weighted
vertical row rates decrease away from that real cut. Consequently
the entire left side of the height-one outer residue rectangle is
paid, including both signs and all real ordinary colors.

The proof uses the unconditional early-curve action comparison of
the later-point main-contour note. It does not assume that note's
main-path source premise. No numerical evaluation or frozen-note
edit is used. The lower right side and full outer assembly remain
separate.

## 1. Exact source and a calibrated positive curve-start bound

Use the exact finite interpolation and its carrier cancellation
from [the tall upper-alias theorem](research_mixed_cap_tall_upper_alias.md):
\[
\mathscr A_N(e,a,w)=
\sum_{l=0}^{N-1}\frac{e_l(w)}{S_l}\,
e^{i\pi Ne(l/N-a)}
\frac{G_N(N(a+e))}
     {G_N(Na)G_N(N(e-l/N))}.
                                                               \tag{1}
\]
At physical private indices it is precisely the original cap row.
All auxiliary indices \(0\le l<N\) remain.

Set
\[
E=\frac18,\qquad
t_L=\frac{\sqrt3-1}{2},\qquad
e_L=E-i\eta_L=\frac{\Log(1-2t_L^2+2it_L)}{2\pi i}.
\]
The exact later incoming point and its original cap action are
\[
X_0=-\frac13+\frac{2\sqrt2}{3}i,\quad
a_0=1-\frac{\Arg X_0}{2\pi},\quad
e_0=\frac14-\frac{i\log2}{4\pi},\quad
\mathcal T_0=\Psi(e_0,a_0,-2),\quad M_0=\Re\mathcal T_0.
                                                               \tag{2}
\]
In particular \(1/2<a_0<7/10\).

Sections 2--4 of
[the later-point main-contour proof](research_mixed_cap_later_point_main_contour.md)
prove, independently of its conditional source premise,
\[
M_0-\Re\Psi(e_L,a_0,-2)>\frac3{112},
\qquad
0<\eta_L<\frac1{49\pi}.
                                                               \tag{3}
\]
The first comparison retains the actual phase and its original
constant: the early curve rises by more than \(3/112\), continues
increasing to a departure point, and that departure point is
strictly below \(M_0\).

We need a positive source bound at \(e_L\), rather than merely
the whole signed endpoint packet. Put \(u=l/N\) and
\(w=-2\cos\theta\). Retain the all-real Newton entropy
\(V_\theta(u)\) of
[the zero-safe color tube theorem](research_mixed_newton_color_tubes.md).
The exact lower-side row rate of (1) is
\[
\begin{split}
R^-_\theta(E,a,u,H)
={}&V_\theta(u)-J(u)-\Re J_-(E-u-iH)\\
 &+\Re J_-(a+E-iH)-J(a)+\pi H(u-a).
\end{split}                                                     \tag{4}
\]
Here \(J_-\) is the original lower continuation, including its
reflected branch when \(E-u<0\). At \(H=0\) its continuous
real boundary value is used.

On the auxiliary-real curve, the complete-color auxiliary real
profile has its unique maximum \(\Re S(e_L)\) at a real
auxiliary critical point. This is the exact force factorization
and full physical-row comparison in Sections 2--3 of
[the auxiliary-real curve theorem](research_mixed_endpoint_auxiliary_real_curve.md).
For \(u\le1/2\), \(V_\theta(u)\le V_0(u)\) gives the same
positive-row upper comparison at every real color.

For completeness, the all-real upper half has the same needed
ceiling. With \(v=1-u\in[0,1/2]\), exact reflection gives its
inner endpoint row rate
\[
V_\theta(1-v)+J(v)-\Re J(e_L+v)+\pi\eta_L(2-v).
                                                               \tag{5}
\]
The Newton theorem gives \(V_\theta(1-v)\le0\), and \(J(v)\le0\).
The original sine-argument comparison therefore bounds (5) by
\(1/6+(5\pi/2)\eta_L\). The curve theorem proves this is below
\(11/36\), whereas \(\Re S(e_L)>1/2\).
Thus every upper-half row is also strictly below the same action.
In particular no upper-half complete-color entropy is substituted
for the weaker all-real bound.

The outer factors are independent of the auxiliary index.
We have therefore proved the full positive-majorant statement
\[
R^-_\theta(E,a_0,u,\eta_L)
 \le\Re\Psi(e_L,a_0,-2)
\quad(0\le u\le1,\ 0\le\theta\le\pi).
                                                               \tag{6}
\]
The original zero-safe factorial and Newton bounds realize (6)
for every finite row, with their uniform polynomial costs and
arbitrarily small fixed tolerances. This statement is stronger
than a modulus bound on the signed endpoint sum.

## 2. Transport to the real cut before summing

For \(H>0\), differentiation of (4) gives
\[
\partial_H R^-_\theta
=-\Im J_-'(E-u-iH)
 +\Im J_-'(a+E-iH)+\pi(u-a).
                                                               \tag{7}
\]
The first derivative has nonpositive imaginary part for
\(-7/8\le E-u\le1/8\).
For nonnegative real part this is the ordinary lower-strip
sine argument. For negative real part use the original exact
reflection
\[
J_-'(-d-iH)=J_+'(d+iH)-i\pi,\qquad 0<d\le7/8;
\]
its imaginary part is strictly negative as well.
The incoming argument has real part in \([5/8,33/40]\),
so its lower sine argument is nonnegative.
Consequently, throughout \(0<H\le\eta_L\),
\[
\partial_H R^-_\theta\ge\pi(u-a)\ge-\pi a.
                                                               \tag{8}
\]
At an argument zero on the boundary \(H=0\), integrate on
\(H>0\) and pass to the continuous primitive. The logarithmic
singularity is integrable; no bound for its pointwise
derivative is asserted there.

Combining (3), (6), and (8), and using
\(\pi a_0\eta_L<1/70\), gives
\[
\begin{split}
R_\theta(E,a_0,u,0)
&\le R^-_\theta(E,a_0,u,\eta_L)+\pi a_0\eta_L\\
&<M_0-\frac3{112}+\frac1{70}
 =M_0-\frac1{80}.
\end{split}                                                     \tag{9}
\]
Here \(R_\theta(\cdot,0)\) is the common upper/lower real
boundary rate. Equation (9) bounds each literal auxiliary row
before any cancellation or summation, uniformly at all real
ordinary colors.

## 3. Both exact weighted vertical rates decrease

For \(H>0\), write
\[
\rho=e^{-2\pi H},\quad
A=\Arg(1-\rho e^{2\pi i(E-u)}),\quad
B=\Arg(1-\rho e^{2\pi i(a+E)}).
                                                               \tag{10}
\]
These are the disk logarithms, with arguments in
\((-\pi/2,\pi/2)\). Since \(1/2<a+E<1\), one has \(B>0\).

Define the upper bare rate using the upper factorial branch,
\[
\begin{split}
R^+_\theta(E,a,u,H)
={}&V_\theta(u)-J(u)-\Re J_+(E-u+iH)\\
 &+\Re J_+(a+E+iH)-J(a)+\pi H(a-u).
\end{split}                                                     \tag{11}
\]
The exact upper and lower cotangent penalties are both
\(2\pi H\). Their weighted rates \(W^\pm_\theta=R^\pm_\theta-2\pi H\)
satisfy
\[
\begin{split}
\partial_H W^+_\theta&=-2\pi(1-a)+A-B,\\
\partial_H W^-_\theta&=-2\pi(1-u)+A-B.
\end{split}                                                     \tag{12}
\]
These identities follow from the original upper and lower
primitive formulas; in particular the lower carrier is not
replaced by the upper one.

For the upper sign, \(A<\pi/2\) and \(B>0\), so
\[
\partial_H W^+_\theta<-\pi/10
\qquad(1/2\le a\le7/10).
                                                               \tag{13}
\]
For the lower sign, distinguish the actual auxiliary ranges.
If \(u\le E\) or \(u\ge E+1/2\), then \(A\le0\), so
\(\partial_H W^-_\theta<0\), including \(u=1\) because \(B>0\).
In the intervening range \(E<u<E+1/2=5/8\),
\[
\partial_H W^-_\theta
<-2\pi(1-u)+\pi/2\le-\pi/4.
                                                               \tag{14}
\]
Thus every weighted row decreases with height magnitude
on both signs. No uniform lower decay slope near \(u=1,H=\infty\)
is needed; the contours here have bounded height.

The continuous real upper rates agree at \(H=0\).
Equations (9), (13), and (14) prove
\[
W^\pm_\theta(E,a_0,u,H)<M_0-1/80,
\qquad 0\le H\le1,\quad 0\le u\le1.
                                                               \tag{15}
\]
This includes the complete small-height portions as well as the
long sides. It does not require an endpoint packet on those sides.

## 4. Both complete finite currents and local ordinary derivatives

Use the left half-grid convention of the main-contour proof:
\[
L_N=\lfloor N/8\rfloor+1,\qquad
\ell_N=(L_N-1/2)/N=1/8+O(N^{-1}).
                                                               \tag{16}
\]
On the vertical line \(e=\ell_N\pm iH\), the exact cotangent
remainder is bounded by \(2e^{-2\pi NH}\), including \(H=0\).
The residue density remains \(+N\), with the original
orientations. Constant modes and their unweighted main joins
are kept separate.

The real upper exponent in (4), (11) is uniformly continuous
in \(E,a,u,H\) on the bounded sets used here, with the original
reflected real values at zeros. An \(O(N^{-1})\) shift has the
usual \(O(\log N/N)\) primitive cost. The exact finite bounds
therefore preserve (15) at \(\ell_N\), for every auxiliary row.
They include the true ends, every reciprocal zero and both
parities. Summing the \(N\) auxiliary rows and integrating
either side costs only polynomial factors.

**Theorem.** Both entire weighted left-side currents of the
original outer cap rectangle, from the real cut to heights
\(+1\) and \(-1\), have modulus at most
\[
C N^B e^{N(M_0-1/160)}
                                                               \tag{17}
\]
at \(a=a_0\), uniformly for \(-2\le w\le2\), along both
level parities and for all sufficiently large \(N\).
The same rate holds for each fixed ordinary derivative,
with polynomial costs.

The ordinary derivative statement uses the original zero-safe
Newton color tubes before summing the positive source bound.
Those tubes also preserve the strict reserve on fixed small
complex ordinary-color neighborhoods. Incoming perturbations
preserve the uniform real-rate bound on these fixed base
contours; no critical-point asymptotic is needed on the sides.
Normalize near complete color by the original holomorphic
\(e^{N\mathcal T(a,w)}\) continued from (2). On a sufficiently
small fixed complex neighborhood, Cauchy's formula on smaller
neighborhoods gives every fixed normalized mixed derivative,
for example with gap \(1/320\).

The complete upper and lower horizontal aliases at heights
\(\pm1\) are already paid by their separate source theorems.
The upper right side is independently paid as well.
This theorem supplies both missing weighted left sides
locally at the exact later incoming point. The right lower
side and the final complete-cap assembly are not inferred
from it, nor is an extension to the entire real incoming arc.

