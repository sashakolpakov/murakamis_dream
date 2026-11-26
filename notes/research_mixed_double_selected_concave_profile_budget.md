# A concave trial bound for every remaining double-selection profile

Research deduction, 6 November 2026. Every remaining profile for two
selected first coordinates is jointly concave on its original real
product. The complete private cap rectangle and the original ordinary
index cuts are included. Consequently one exact real trial and outward
bounds on its value and gradient give a rigorous upper bound for the
whole target maximum. A floating optimizer may propose the trial, but
its convergence, stationarity or accuracy is not a proof premise.
No new root, parameter cover or numerical estimate is used here.

## 1. Original phases, reference and target boxes

Keep the actual first-three flags \((1,1,\beta)\), \(\beta=0,1\),
with length \(m\ge4\), reference \(r=(e_*,a_*,u_*,z_*,v_*,b_*)\),
and original phases of the
[double-selected last-row reduction](research_mixed_double_selected_last_rows.md).
The original allocated phase and its sole boundary derivative are
\[
 \begin{split}
 F(r)&=\Psi(e_*,a_*)+Q_1(u_*;a_*,z_*)+Q_\beta(v_*;z_*,b_*)
                    -g(a_*)-g(z_*)-\tfrac\beta2g(b_*),\\
 p_R&=g'(v_*+b_*)-(1+\beta/2)g'(b_*).
 \end{split}
 \tag{1}
\]
All five internal derivatives of \(F\) vanish at the original
reference. No alternative slope, phase calibration or logarithmic
lift is chosen.

Set \(P=[11/50,9/20]\), \(H=1/100\). The cap choice
\(j\in\{0,L\}\) is its original main line or real left cut.
The outgoing choice \(k\in\{0,R\}\) is its original main line
or real half row. Write the target variables in order \((e,a,u,z,v,b)\).
Their real product is
\[
 K_{j,k}=E_j\times P\times[1/8,1/2]\times P\times V_k\times P,
 \quad E_0=[.27,.49],\ E_L=\{.27\},
 \quad V_0=[\ell_\beta,.5],\ V_R=\{.5\},
 \quad\ell_0=.15,\ \ell_1=.125.
 \tag{2}
\]
The corresponding fixed heights are
\[
 \begin{array}{c|cccccc}
 &e&a&u&z&v&b\\ \hline
 \Im&h_e^{(j)}&H&\Im u_*&H&h_v^{(k)}&\Im b_*
 \end{array},\qquad
 h_e^{(0)}=\Im e_*,\ h_e^{(L)}=0,\quad
 h_v^{(0)}=\Im v_*,\ h_v^{(R)}=0.
 \tag{3}
\]
Thus the real cuts do not retain their former imaginary heights.
Coordinates fixed by (2) have no active optimization variable.
For outgoing type four the pointwise half-row theorem already removes
\(k=R\); keeping it below is harmless and states the common curvature
fact.

For \(\nu_1,\nu_2\in\{0,1\}\), define the holomorphic target
expression and its real defect by
\[
 \begin{split}
 \Phi_{\nu_1,\nu_2}(e,a,u,z,v,b)
   ={}&\Psi(e,a)+Q_1(u;a,z)+Q_\beta(v;z,b)
       -\nu_1g(a)-\nu_2g(z)-\tfrac\beta2g(b)\\
     &+2\pi i(\nu_1a+\nu_2z),\\
 f_{j,k,\nu_1,\nu_2}(x;r)
   ={}&\Re\{\Phi_{\nu_1,\nu_2}(w(x;r))-F(r)
                                     -p_R(w_b-b_*)\}.
 \end{split}
 \tag{4}
\]
The value 1 denotes factorial and 0 denotes forced. The real part of
the last target term is exactly \(-2\pi H(\nu_1+\nu_2)\).
The outgoing allocation \(-\beta g(b)/2\) is retained in both
the target and original marginal. Formula (4) is precisely the
corresponding term in the finite profile envelope after maximizing
over its independent active indices and retained real targets.

## 2. Concavity on the full original product

**Theorem 1.** Each function in (4) is strictly concave in its active
real variables throughout (2), at the heights (3). Its negative
real Hessian is bounded below by \(\mu I\), with
\(\mu=1/1250000\), on the active coordinates. The statement
requires neither a barrier restriction nor a moving target root.

*Proof.* The
[whole cap Hessian theorem](research_mixed_first_cap_plateau_phase.md),
Lemma 1, proves the bare-phase estimate
\[
 -\Re\Psi''\succ\frac\pi{200}I_2
 \quad\text{on}\quad
 ([.27,.49]+i[-.055,.04])\times(P+i[-.108,.021]).
 \tag{5}
\]
It explicitly proves the bare phase as well as the version with an
extra outgoing halfweight. Its domain contains both cap choices in
(2)--(3), including \(a\) at positive height \(H\). In that
proof the canonical endpoint action itself obeys
\[
                       -\Re S''(e)>\pi/43
 \tag{6}
\]
throughout the whole private rectangle. This follows from the original
endpoint negative real Hessian and its accretive Schur complement;
the small corner \(\Re(e+a)<.5\) has a stronger private bound
that pays the positive summed cotangent. Thus (5) does not presume
that the summed real part is always above one half, and does not
extrapolate the narrower optimized private rectangle.

The bare ordinary phase is
\[
 Q_\epsilon(s;a,b)=V(s,a)+V(s,b)-\epsilon g(s)+2\pi ias,
 \qquad V(s,a)=g(s+a)-g(s)-g(a).
 \tag{7}
\]
The [whole-pair estimate](research_mixed_horizontal_zero_mode_support.md)
and [half-index extension](research_mixed_half_index_contour.md)
give
\[
 -\Re Q_\epsilon''\succ\mu I_3
 \quad\text{for}\quad
 s\in[.15,.5]+i[-.108,.068],\quad
 a,b\in P+i[-.12,.12].
 \tag{8}
\]
For own type four, the
[smaller-cut proof](research_mixed_four_left_cut_extension.md),
Section 2, extends this to \(\Re s\in[.125,.15]\).
As made explicit in Section 2 of the
[second-selection concavity theorem](research_mixed_second_selected_horizontal_concavity.md),
its Schur estimate needs only both outer coefficients to be at least
one. Setting both to one proves (8) for the bare \(Q_1\), not
only for an additionally allocated phase. The extra small-index
factorial is retained; separate unweighted pair positivity there is
not being assumed.

The actual ordinary heights satisfy
\(\Im u_*\in(-.102,-.001)\) and
\((\Im v_*,\Im b_*)\in(-.065,.068)^2\) or
\((-.102,-.001)^2\), according to \(\beta\). Every height in
(3), including the real half-row height zero, is therefore covered
by (8). Sum (5), the two estimates (8), and the nonnegative
negative real Hessians of
\(-\nu_1g(a)-\nu_2g(z)-\beta g(b)/2\).
The latter are nonnegative because their real parts lie in
\(P\subset(0,.5)\). The chirps and affine subtraction have zero
real horizontal Hessian. Before fixing any coordinate, every active
direction has reserve greater than \(\mu\).

For a left cap or outgoing half row, apply these same whole-height
bounds at its new height zero and then restrict to the principal
submatrix on the active real coordinates. This is not a restriction
of a theorem that required the old negative height. Principal
submatrices preserve the stated positive lower bound. This proves
all four profile cases and all four Fourier pairs. \(\square\)

## 3. A single exact trial eliminates every real target

Write the active product as \(K=\prod_i[l_i,r_i]\), deleting
fixed coordinates from (2). Choose any exact real trial
\(y\in K\), with the same fixed heights (3). For its original
real gradient set \(p_i=\partial_i f(y;r)\).

**Proposition 2.** One has
\[
 \max_{x\in K}f(x;r)
 \le f(y;r)+\sum_i\max\{p_i(l_i-y_i),\ p_i(r_i-y_i)\}.
 \tag{9}
\]

*Proof.* Concavity gives
\(f(x;r)\le f(y;r)+\nabla f(y;r)\cdot(x-y)\).
The supremum of this affine function on a product is the sum of its
one-dimensional endpoint maxima. \(\square\)

The curvature constant is used only to establish concavity; it does
not divide an error or a residual. In particular an approximate
optimizer with small gradient is useful as a trial without proving
that it is a critical point, or using its reported function value
as an upper bound.

For a whole certified reference cell, suppose rigorous enclosures give
\[
 f(y;r)\le U_0,\qquad p_i\in[p_i^-,p_i^+]
 \quad\text{for every actual reference in that cell}.
 \tag{10}
\]
Since \(l_i-y_i\le0\le r_i-y_i\), an exact rational
upper replacement for (9) is
\[
 \boxed{\quad U_0+
       \sum_i\max\{p_i^-(l_i-y_i),\ p_i^+(r_i-y_i)\}.\quad}
 \tag{11}
\]
All data in (10) must be evaluated using that same reference cell,
its original outgoing tangent and its original action. Rounded
rational proposals are checked for membership in (2). One may choose
a different fixed rational trial for each profile or reference cell;
(9) is pointwise in the reference and makes no differentiability
claim about this choice. Input intervals containing several references
do not authorize selecting a new independent reference midpoint.

For completeness the active real derivatives of (4) are the real
parts of
\[
 \begin{array}{c|l}
 e&S'(e)+g'(e+a)-g'(e)+i\pi(e-1/2)\\
 a&g'(e+a)+g'(u+a)-(2+\nu_1)g'(a)+2\pi iu\\
 u&g'(u+a)+g'(u+z)-3g'(u)+2\pi ia\\
 z&g'(u+z)+g'(v+z)-(2+\nu_2)g'(z)+2\pi iv\\
 v&g'(v+z)+g'(v+b)-(2+\beta)g'(v)+2\pi iz\\
 b&g'(v+b)-(1+\beta/2)g'(b)-p_R .
 \end{array}
 \tag{12}
\]
Rows fixed by a profile are omitted. Here
\(S'(e)=-J'(e-u_c(e))+i\pi u_c(e)\), with the original
canonical endpoint branch. The private action and its derivatives
may be evaluated by the original explicit auxiliary radical; they
are not supplied by convergence of a new critical-point solve.

## 4. Scope of the remaining boundary test

The last-row theorem already pays all eight omitted outgoing-last
terms with gap greater than \(3/1000\). The remaining envelope has
sixteen profiles for \(443\) and eight for \(444\). Formula
(11) bounds each of them on an entire certified reference cell,
including all free real targets and both original Fourier choices.
No independent marginal maximum is substituted for the coupled
trial value.

A full reference-domain sign still requires every cell of a complete
admitted reference cover, or an applicable complete-boundary extension,
to pass its corresponding rigorous inequality. The concavity theorem
and trial rule alone assert no remaining negative sign. Any boundary
extension must retain the original sole boundary marginal \(p_R\)
and the reference-dependent unselected heights; the cap and internal
selected coordinates do not create new boundary tangents.

This note proves a global target bound that can be checked using
saved canonical reference enclosures. It contains no numerical pass,
no new original-source calculation and no simultaneous-selection
or full filling-volume conclusion.
