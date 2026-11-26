# The joint zero mode of the terminal type-three Newton sum

Research deduction, 5 November 2026. The real part of the reduced
two-variable terminal phase has a uniformly negative Hessian on a fixed product
containing every actual type-three critical point. Its entire horizontal
zero-mode rectangle therefore lies below the original terminal
supporting plane, even when the external real target ranges independently
over the plateau. This controls a coherent two-variable current.
It does not discard the mixed joining currents, aliases, or remaining
real triangular support.

## 1. Original phase and the fixed product

Retain the exact source and original logarithmic lifts of
[the terminal Newton reduction](research_mixed_terminal_three_newton_reduction.md).
At the complete ordinary color its phase is
\[
\begin{split}
\mathcal T(a;t,u)={}&-2J(1/2-u)-2J(u)
 +g(t+a)+g(t+u)-3g(t)\\
 &-2g(u)-g(a)+i\pi u+2\pi iat,\qquad
 g(v)=J(v)+i\pi(v-v^2)/2 .
\end{split}
\tag{1}
\]
Here \(t=i/N\) is the original transform index and \(u=l/N\)
the Newton index before contour deformation. The exact physical
support is \(i+l<N\). In particular the real rectangle below is
strictly inside that triangle.

Set
\[
\begin{split}
\mathcal A&=[11/50,9/20]+i[-3/25,3/25],\\
\mathcal T_0&=[1/5,9/20]+i[-3/25,3/25],\\
\mathcal U_0&=[1/10,2/5]+i[-3/25,3/25].
\end{split}
\tag{2}
\]
On this product every primitive in (1) is regular:
\(\Re(t+a)\in[.42,.90]\), \(\Re(t+u)\in[.30,.85]\),
and \(\Re(1/2-u)\in[.10,.40]\).
There is no branch change at a new external target.

Write \(V(x,y)=J(x+y)-J(x)-J(y)\). Up to \(i\pi\) times a
quadratic polynomial with real coefficients, (1) is exactly
\[
 V(t,a)+V(t,u)-J(t)-3J(u)-2J(1/2-u).
\tag{3}
\]
Thus the displayed quadratic phase has zero entrywise real Hessian.
Both the extra own-index term and the Newton terms in (3) must
be retained.

## 2. A joint quantitative Hessian bound

**Lemma 1.** On the whole product (2),
\[
                  -\Re\mathcal T''\succ\frac{3\pi}{50}I_3.
\tag{4}
\]
The variables are ordered as \((a,t,u)\).

*Proof.* Put
\[
\begin{gathered}
b=\Re\cot\pi a,\quad p=\Re\cot\pi t,\quad
q=\Re\cot\pi u,\quad v=\Re\tan\pi u,\\
c=\Re\cot\pi(t+u),\qquad d=\Re\cot\pi(t+a).
\end{gathered}
\]
Here \(b,p,q,v>0\). Differentiating (3) gives
\[
-\frac1\pi\Re\mathcal T''
 =
\begin{pmatrix}
 b-d&-d&0\\
 -d&3p-c-d&-c\\
 0&-c&4q+2v-c
\end{pmatrix}.
\tag{5}
\]
Its three diagonal entries minus the sums of absolute off-diagonal
entries are
\[
 b-2d_+,\qquad 3p-2c_+-2d_+,\qquad 4q+2v-2c_+,
 \qquad x_+=\max(x,0).
\tag{6}
\]

For every individual variable \(x+ih\) in (2),
\[
\Re\cot\pi(x+ih)
 =\frac{\sin(2\pi x)}{\cosh(2\pi h)-\cos(2\pi x)}
 >C(x):=\frac{\sin(2\pi x)}{13/10-\cos(2\pi x)}.
\tag{7}
\]
We used \(\cosh(6\pi/25)<13/10\).
The derivative of \(C\) has the sign of
\((13/10)\cos(2\pi x)-1\). Hence its only possible interior
critical point on \((0,1/2)\) is a maximum. It decreases on
\([1/5,9/20]\), since \(\cos(2\pi/5)<31/100\).
The following strict endpoint bounds suffice:
\[
\begin{array}{c|rrrrrr}
 x&1/10&1/5&1/4&3/10&2/5&9/20\\ \hline
 C(x)>&19/20&19/20&3/4&7/12&1/4&13/100 .
\end{array}
\tag{8}
\]
For a shifted sum of real part \(s\ge1/2\), its cotangent has
nonpositive real part. When \(0<s<1/2\), its positive real
cotangent is at most \(\cot\pi s\). We use
\[
\begin{array}{c|rrrrr}
s&3/10&7/20&2/5&21/50&47/100\\ \hline
\cot(\pi s)<&3/4&13/25&1/3&13/50&1/10 .
\end{array}
\tag{9}
\]

Here are the complete row estimates from (6).
The intervals in the first column refer to real parts. In the last
three rows the positive \(2v\) is not needed.
\[
\begin{array}{c|c|c}
\text{row}&\text{interval}&\text{strict lower bound}\\ \hline
a&[.22,.30]&7/12-2(13/50)=19/300\\
a&[.30,.45]&13/100\\ \hline
t&[.20,.25]&3(3/4)-2(3/4)-2(13/50)=23/100\\
t&[.25,.30]&3(7/12)-2(13/25)-2(1/10)=51/100\\
t&[.30,.40]&3/4-2/3=1/12\\
t&[.40,.45]&39/100\\ \hline
u&[.10,.20]&4(19/20)-2(3/4)=23/10\\
u&[.20,.30]&4(7/12)-2/3=5/3\\
u&[.30,.40]&1 .
\end{array}
\tag{10}
\]
For example, in the first \(a\)-row, \(t+a\) has real part
at least .42, giving \(d_+<13/50\). In the second \(a\)-row
that sum has real part at least .50, so \(d_+=0\).
For the successive \(t\)-rows, the least possible real parts of
\(t+u\) are .30, .35, .40, .50; those of \(t+a\) are
.42, .47, .52, .62. For the \(u\)-rows the least real parts
of \(t+u\) are .30, .40, .50. These exhaust all signs and
endpoints. Every lower bound in (10) exceeds \(3/50\).

The real symmetric matrix (5) therefore has every eigenvalue
greater than \(3/50\), by the row-sum bound. This proves (4).
\(\square\)

The [exact rational scalar checker](../experiments/check_mixed_terminal_three_joint_concavity_constants.py)
verifies (7)--(10) using alternating sine/cosine Taylor bounds,
a positive cosh-series remainder, and rational arithmetic.
Its [saved result](../repro/results/research-mixed-terminal-three-joint-concavity-constants.json)
contains 31 passed inequalities. This is a scalar verification of
the constants, not a root or source cover.

## 3. The actual fixed-height supporting plane

Let \(a_*=A+ih_a\) be an actual external reference of a terminal
type-three block in an open word of length at least two.
Write \(t_*=T+ih_t\), \(u_*=U+ih_u\) for its actual attached
and auxiliary coordinates. The
[critical-curve identity](research_mixed_terminal_three_critical_curve.md),
equations (17)--(20), proves with the original logarithmic lifts that
\[
\mathcal T_t(a_*;t_*,u_*)=\mathcal T_u(a_*;t_*,u_*)=0,\quad
\mathcal T(a_*;t_*,u_*)=\mathcal P_0(a_*),\quad
\mathcal T_a(a_*;t_*,u_*)=\mathcal P_0'(a_*).
\tag{11}
\]
This identifies the full complex action, rather than just an
exponentiated critical equation. The actual ranges are strictly
inside (2). In particular
\[
 .278<T<.391,\quad -.072<h_t<.021,\qquad
 .218<U<.242,\quad .049<h_u<.077.
\tag{12}
\]

Let \(\nu\in\{0,1\}\) be the external type minus three and put
\[
\mathcal T_\nu(a;t,u)=\mathcal T(a;t,u)-\frac\nu2g(a),\qquad
\Pi_{0,\nu}=\mathcal P_0-\frac\nu2g .
\tag{13}
\]
Its additional negative real Hessian is
\((\nu\pi/2)\Re\cot\pi a\,da^2\ge0\); thus (4) also holds
for \(\mathcal T_\nu\).

**Theorem 2.** Fix the three actual heights, and take independent
real targets
\[
 a=y+ih_a,\qquad t=x+ih_t,\qquad u=z+ih_u,
 \quad y\in[.22,.45],\ x\in[.20,.45],\ z\in[.10,.40].
\]
Then
\[
\begin{split}
\Re\mathcal T_\nu(a;t,u)
\le{}&\Re\Pi_{0,\nu}(a_*)+
       \Re\Pi_{0,\nu}'(a_*)(y-A)\\
&-\frac{3\pi}{100}\bigl((y-A)^2+(x-T)^2+(z-U)^2\bigr).
\end{split}
\tag{14}
\]
*Proof.* The horizontal line segment from the reference to the target
stays inside (2). Integrate (4) twice along that segment, and use
(11) to cancel both internal first derivatives. The only surviving
linear term is the external tangent in (14). \(\square\)

The target \(a\) may be outside the original endpoint-map disk.
No critical point at that target is used. In particular (14) implies
the requested original quadratic plane with
\(\kappa_*=1/2500000\), leaving a strictly stronger quadratic
loss in both integration variables.

## 4. The controlled finite current and its unestimated joins

Use half-grid cuts tending to
\[
I_t=[1/5,9/20],\qquad I_u=[1/10,2/5].
\tag{15}
\]
Choose each lower cut inside its interval, at distance at most \(1/N\)
from the lower endpoint, and each upper cut inside at distance at most
\(1/N\) from the upper endpoint. All four cuts are in
\((\mathbb Z+1/2)/N\). The rectangular lattice sub-sum is defined by
these inward cuts; any omitted edge rows remain part of the real
complement. The product stays strictly inside \(t+u<1\) and
\(u<1/2\), without requiring an expansion of the proved Hessian box.

Here is the exact simultaneous interpolation. Let \(G_N\) be the
prescribed sine factorial of
[the exact factorial construction, Sections 1 and 4](exact_factorial_interpolation_and_complex_contours.md),
and define its negative-root mark
\[
 \mathfrak P_N(v)=
 \exp\!\left\{\frac{i\pi}{2}((N-1)v-Nv^2)\right\}G_N(Nv).
 \tag{15a}
\]
It equals \(P_j\) at \(v=j/N\). Its exact difference equation gives
\(\mathfrak P_N(a+i/N)/\mathfrak P_N(a)=p_i(e^{-2\pi ia})\).
For the ordinary color write \(w=-2\cos\zeta\), and use the
[exact Newton interpolation, equation (8)](research_complete_boundary_coefficient_asymptotic.md#2-exact-interpolation-and-ordinary-boundary-derivatives):
\[
 \mathcal E_N(u,\zeta)=
 \frac{N}{G_N(Nu)^2
 G_N((N-1)/2-Nu+N\zeta/(2\pi))
 G_N((N-1)/2-Nu-N\zeta/(2\pi))}.
 \tag{15b}
\]
It equals the original \(e_l(w)\) at \(u=l/N\), is even in
\(\zeta\), and is therefore holomorphic in \(w\) near \(-2\).
The interpolated full double summand, including its literal factor
\(N\), is
\[
 \mathcal I_N(a;t,u,\zeta)=
 N e^{i\pi(N-1)u} e^{2\pi iNat}\mathcal E_N(u,\zeta)
 \frac{\mathfrak P_N(a+t)\mathfrak P_N(t+u)}
      {\mathfrak P_N(a)\mathfrak P_N(u)^2\mathfrak P_N(t)^3}.
 \tag{15c}
\]
At every retained physical pair it equals exactly the summand in
the terminal Newton identity. The factor \(e^{i\pi(N-1)u}\)
is the original positive lift of \((-q)^{-l}\). No triangular zero
outside the chosen rectangle is replaced by a nonzero off-grid term.

Section 4 of the factorial construction proves a uniform symbol on
**every compact subset** of \(0<\Re v<1\), not only at imaginary
height at most .12. This applies simultaneously to \(a+t\) and
\(t+u\), whose imaginary parts can reach \(\pm.24\), and to all
denominators in (15c). The midpoint arguments in (15b) are covered
by the same formula with their bounded offset \(-1/2\).
For small fixed \(\zeta\) they remain in compact regular strips.
The Newton symbol and its ordinary-color scope are established in
equation (9) of the cited coefficient proof and
[Section 7 of the whole-color theorem](research_complete_boundary_full_index_interval.md#7-the-whole-boundary-polynomial-near-the-complete-color).
Consequently, uniformly on this entire product,
\[
 \mathcal I_N=
 N^{-2}\mathcal A(a,t,u)
 e^{N\{\mathcal T(a;t,u)+V(u,\zeta)-V(u,0)\}}
 (1+O(N^{-1})),
 \tag{15d}
\]
where
\[
\begin{split}
 V(u,\zeta)&=-2J(u)-J(1/2-u+\zeta/(2\pi))
                         -J(1/2-u-\zeta/(2\pi)),\\
 \mathcal A(a,t,u)&=
 e^{i\pi(t-u)/2}
 \frac{\sqrt{2\sin\pi(a+t)}\sqrt{2\sin\pi(t+u)}}
 {(2\sin\pi u)^2(2\sin\pi t)^{3/2}
                         (2\sin\pi a)^{1/2}} .
\end{split}
 \tag{15e}
\]
All sine roots continue from their positive real values. The amplitude
is holomorphic and nonzero on the indicated compact product, and the
normalized error has uniform fixed derivatives on smaller neighborhoods.
The perturbation \(V(u,\zeta)-V(u,0)\) is even, holomorphic and uniformly
small as \(w\to-2\). This supplies the joint exponential upper rate
from the literal source, rather than inferring it from the finite
Newton identity alone.

Apply the [marked residue identity, Section 5](exact_factorial_interpolation_and_complex_contours.md#5-the-original-finite-sum-has-a-marked-residue-cycle)
to (15c) on this rectangular lattice block. Equivalently apply twice
the exact kernel \(K_N(v)=(1-e^{-2\pi iNv})^{-1}\), with the
orientation and coefficient proved in
[the coefficient contour proof, equations (16)--(18)](research_complete_boundary_coefficient_asymptotic.md#4-exact-summation-aliases-and-the-nonzero-coefficient).
There are no interpolation poles in the product of the two rectangles,
so the successive residue operations are legitimate. Their product
retains the constant-mode coefficient \(+N^2\), in addition to the
literal prefactor \(N\) already in the Newton identity. Shift the two
constant-mode paths to the horizontal segments
\(I_t+ih_t\), \(I_u+ih_u\).
The resulting horizontal-horizontal current has, by (14), upper
rate
\[
\Re\Pi_{0,\nu}(a_*)+\Re\Pi_{0,\nu}'(a_*)(y-A)
                       -\kappa_*(y-A)^2+\eta
\tag{16}
\]
for every prescribed \(\eta>0\). This assertion includes its original
polynomial powers: contour lengths and the displayed factors of \(N\)
only change a polynomial prefactor. A small fixed ordinary-color
disk changes the phase uniformly on this compact product and uses
part of \(\eta\). Cauchy's formula supplies fixed ordinary-color
derivatives on a smaller disk. For \(\nu=1\), the actual external
height is negative, so the original relative Fourier theorem
legitimates the halfweight in (13); no independent positive-height
Fourier branch is substituted.

This is a bound for the stated horizontal-horizontal current,
not yet for its rectangular lattice sub-sum. There are exact joining
terms. Their geometry can be stated without hiding an iterated
error term. For the constant modes, write each original real segment
as its shifted horizontal segment plus the two oriented vertical
joins at its real cuts. Their product has nine terms: the controlled
horizontal-horizontal current, four horizontal-vertical currents,
and four vertical-vertical currents.

Convexity in each height follows from (4). Thus the zero-mode joining
terms are bounded by the maximum of (16) and the following explicit
families, with the same neighboring allocation:
\[
\begin{array}{ll}
\Re\mathcal T_\nu(a;c_t,z+ih_u),
 &c_t\in\{.20,.45\},\quad z\in I_u,\\
\Re\mathcal T_\nu(a;x+ih_t,c_u),
 &c_u\in\{.10,.40\},\quad x\in I_t,\\
\Re\mathcal T_\nu(a;c_t,c_u),
 &c_t\in\{.20,.45\},\quad c_u\in\{.10,.40\}.
\end{array}
\tag{17}
\]
Indeed each vertical coordinate is bounded by its two endpoint
heights, zero and the actual height. The fully shifted endpoints
are controlled by (14); the other endpoint combinations are exactly
(17). This retains the mixed currents, including both flattened
heights at the four real corners. Their comparison with (16) has
not been proved here.

For the actual inward half-grid cuts, replace each \(c_t,c_u\) in
(17) by its \(N\)-dependent value. The phase and the whole-color
perturbation have uniformly bounded first derivatives on the compact
regular product just specified. The difference from (17) is therefore
\(O(N^{-1})\), uniformly over the actual references and targets.
It contributes a bounded exponential factor, or can be paid by any
prescribed part of \(\eta\) for large \(N\). This does not assume
continuity of an unspecified finite function in an \(N\)-dependent
neighborhood.

The additional-frequency parts of either residue identity also remain.
They include one-index and two-index aliases, with the original
penalties \(2\pi|\Im t|\), \(2\pi|\Im u|\), or their sum.
No cancellation of an inner error against an outer chirp is assumed.
Every point of the remaining physical triangle outside (15) likewise
still needs a bound, except the independently discarded end-index and
low/high-Newton sectors already proved. The fixed joint supporting
plane (14) settles the coherent central horizontal current; the
explicit mixed faces (17), alias currents, and surviving real
complement are the remaining tasks for this contour.

