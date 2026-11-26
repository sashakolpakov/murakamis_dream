# The finite first-four/next-three product at its selected height

Research deduction, 6 November 2026. The proved central comparison
bounds the literal product of the two main horizontal currents, with
the complete selected Fourier polynomial. The other currents and all
real rows reduce to nineteen joint boundary profiles per Fourier
alternative. No sign for these nineteen profiles is asserted.

Two analytic reductions are useful here. The whole type-four cap tail
reduction remains valid at the positive selected height, and its
literal endpoint ceilings are below its main horizontal profile.
The ordinary type-three horizontal aliases are below their own main
line pointwise, so they introduce no additional joint test. No root,
source evaluation, or numerical cover is used in this deduction.

## 1. Exact source and the common reference

Fix the actual reference of a word of length at least three beginning
with types four and three. Use the notation and original lifts of the
[central gap theorem](research_mixed_first_four_next_three_central_gap.md).
In particular
\[
\begin{gathered}
 H=7/625,\qquad z=y+iH,\quad b=v+ih_b,
 \qquad y,v\in P=[11/50,9/20],\\
 e_*=e_R^*+ih_e,\quad s_*=s_R^*+ih_s,\quad
 z_*=a+ic,\quad b_*=b_R^*+ih_b,\\
 -.051<h_e<-.019,\quad -.065<h_s,h_b<.068,
 \qquad -.070<c<-.020.
\end{gathered}
\tag{1}
\]
All starred quantities belong to the same coupled critical point.
The target \(b\) is the outgoing own-three leg; it is not the next
external input used to construct that critical point.

With \(r=e^{-2\pi i/N}\), \(P_i=(r;r)_i\),
\(p_i(X)=(rX;r)_i\), and \(X=e^{-2\pi iz}\),
\(Y=e^{-2\pi ib}\), the exact two-factor source is
\[
\begin{split}
 \mathcal K_N(w;X,Y)
 &=U_{1,N}(w,X)C_{0,N}(X,Y)d_N(X)X^{-N},\\
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
                 \frac{H_N(w,r^{-i})p_i(X)}{P_i^2},\\
 C_{0,N}(X,Y)&=\sum_{j=0}^{N-1}
                 \frac{X^{-j}p_j(X)p_j(Y)}{P_j^2}.
\end{split}
\tag{2}
\]
These are the finite kernels in the
[exact torus composition](research_mixed_conditional_torus_composition.md).
There is one complete \(d_N\) at the common type-four coordinate,
and no outgoing halfweight at the type-three coordinate \(b\).
The two allocated halves at \(z\) have already been recombined in
(2); no Fourier factor is divided out. The ordinary color \(w\)
belongs only to the original cap, and its complete value is \(-2\).

Write the bare phases as
\[
\begin{split}
 \Psi(e,z)&=S(e)+J(e+z)-J(z)-i\pi ez-g(e),\\
 Q(s;z,b)&=g(s+z)+g(s+b)-2g(s)-g(z)-g(b)+2\pi izs.
\end{split}
\tag{3}
\]
Here \(S(e)\) is the complete endpoint action on the original
canonical branch. Thus the joint phase in the central theorem is
\(\mathcal F=\Psi+Q-g(z)\). Define
\[
 M=\Re\mathcal F(e_*,s_*;z_*,b_*),\qquad
 p=\mathcal F_b(e_*,s_*;z_*,b_*),\qquad
 \ell_b(v)=\Re p\,(v-b_R^*).
\tag{4}
\]
The two full selected Fourier rates are
\[
 W_{\rm fac}(y)=-\Re g(z)-2\pi H,
 \qquad W_{\rm force}(y)=0.
\tag{5}
\]
Indeed the original
[Fourier continuation bound](research_mixed_fourier_weight_continuation.md)
gives the upper rate
\(\max\{-\Re g(z),2\pi H\}\) for the whole \(d_N(X)\);
the literal monomial \(X^{-N}\) subtracts \(2\pi H\).
The alternatives in (5) are bounds for this single polynomial,
not an exact decomposition into two new finite factors.

## 2. The cap: four boundary profiles and no endpoint profile

For each \(y\), put
\[
\begin{array}{ll}
 A_0(y)=\displaystyle\max_{.27\le x\le.49}
                   \Re\Psi(x+ih_e,z),&
 A_L(y)=\Re\Psi(.27,z),\\
 A_R(y)=\Re\Psi(.49,z),&
 A_-(y)=\displaystyle\max_{.27\le x\le.49}
                   \Re\Psi(x-.055i,z)-.11\pi,\\
 A_+(y)=\displaystyle\max_{.27\le x\le.49}
                   \Re\Psi(x+.04i,z)-.08\pi.&
\end{array}
\tag{6}
\]
The real cuts in \(A_L,A_R\) have height zero. The private
height \(h_e\) occurs only in the main profile \(A_0\).

**Lemma 1.** At the selected height in (1), the complete cap has
the uniform upper rate
\[
 |U_{1,N}(w,X)|\le C_\tau N^{B_\tau}
     \exp N\{\max(A_0,A_L,A_R,A_-,A_+)+\tau\}.
\tag{7}
\]
This holds on a fixed sufficiently small ordinary-color disk, for
both parities and every fixed ordinary-color derivative, with a
possibly different polynomial prefactor.

*Proof.* The exact retained-row interpolation is (4) of the
[complete cap contour criterion](research_mixed_cap_outer_contour_reduction.md):
\[
 D_N(e)^{-1}\mathcal C_N(e,w)
 \frac{\widehat P_N(N(e+z))}
      {\widehat P_N(Nz)\widehat P_N(Ne)}.
\tag{8}
\]
The complete endpoint packet is uniform on a neighborhood of
\([.27,.49]+i[-.055,.04]\). The outgoing height \(H<.021\)
lies within the larger domain of the
[bare cap Hessian lemma](research_mixed_first_cap_plateau_phase.md),
so \(-\Re\Psi_{ee}>0\) on the entire private rectangle.
The sums \(e+z\) have real parts in \([.49,.94]\), strictly
inside the factorial regular strip. Thus (8), the coefficient
\(+N\) of its zero mode, and its original alias kernels remain
valid without changing the interpolation.

Deform that zero mode to height \(h_e\). Vertical convexity
bounds each joining current by its real-cut and main-line endpoints.
On either half of a vertical alias side, subtraction of the linear
penalty \(2\pi|\Im e|\) preserves convexity. Hence the real
cuts and the two horizontal aliases in (6) control every vertical
alias, including its height-zero endpoint.

For the real private rows write
\[
 R_1(t,z)=\Re S(t)+\int_0^t
                  \log|1-e^{-2\pi i(z+x)}|\,dx-J(t).
\tag{9}
\]
This is the literal positive-radius numerator. In particular
\[
 \int_0^t\log|1-e^{2\pi H-2\pi i(y+x)}|\,dx
 =2\pi Ht+\int_0^t
             \log|1-e^{-2\pi H-2\pi i(y+x)}|\,dx .
\tag{9a}
\]
The cap has no incoming \(X^{-i}\); its factor \(e^{2\pi Hi}\)
is retained, not canceled. The full-row estimates are those of
Section 5 of the cap phase lemma. Their monotonicity extends to
the present positive height as follows. On \(0<t\le.27\),
\(y+t\in[.22,.72]\) and
\(\cos 2\pi(y+t)<1/5\). The numerator radius is now
\(e^{2\pi H}>1\), so the numerator modulus exceeds one.
The old bounds \((\Re S)'(.27)>27/50\),
\((\Re S)''<0\), and \(J'(.27)<41/100\) still give
\(R_1'>13/100\) on the lower compact tail.

For \(t\ge1/2\), the exact old identity
\((\Re S)'-J'\le-\log4\) gives
\[
 R_1'(t,z)\le-\log4+\log(1+e^{2\pi H})<0.
\tag{10}
\]
For \(.49\le t\le.5\), use instead
\((\Re S)'<-3/5\) and \(J'>3/5\). The same conclusion
follows from \(1+e^{2\pi H}<9/4\) and
\(\log(9/4)<6/5\). These elementary inequalities hold even
for \(H\le.014\): \(2\pi H<.09\) and
\(e^{.09}\le(1-.09)^{-1}<5/4\); also
\(e^{6/5}>1+6/5+(6/5)^2/2>9/4\).
At numerator zeros one uses the continuous integrated logarithm.

The original endpoint bounds near \(t=0,1\) already permit
positive outgoing heights up to \(.021\), and thus apply here.
Explicitly, at \(i/N\le.01\) their Newton entropy estimate uses
\(|p_i(X)|\le(1+e^{.042\pi})^i\), which includes the present
positive radius and gives the literal rate ceiling \(1/4\).
At \(i/N\ge.99\), the exact complete-product identity gives
\[
 |p_i(X)|\le 2e^{2\pi NH}(20/19)^{N-i},\qquad
 \frac35+2\pi H+\frac1{100}\log(40/19)<\frac34.
\tag{10a}
\]
Here the reciprocal factors have modulus at least \(19/20\)
on their stated angles, the original endpoint entropy is below
\(3/5\), and the extra reciprocal factorial has nonpositive
rate on this interval. In particular the \(2\pi H\) endpoint
charge is explicitly paid. The last scalar inequality follows
even with \(H=.021\), using \(\pi<22/7\) and
\(\log(40/19)<4/5\).
Consequently the complete lower and upper tails have rates at most
\(\max(A_L,1/4)\) and \(\max(A_R,3/4)\), respectively.

Both constants are strictly below \(A_0\). To prove this without
any new action evaluation, retain the actual \(e_*\) and first
vary \(z=y+ic\) horizontally. The exact marginal is
\[
 \Psi_z(e_*,z)=g'(e_*+z)-g'(z),\qquad
 \Re\Psi_z=
 \log\left|\frac{\sin\pi(e_*+z)}{\sin\pi z}\right|
                                      +\pi h_e.
\tag{11}
\]
The real sums lie in \((.553,.813)\), their heights have
modulus less than \(.121\), and \(|c|<.07\). Thus
\[
 \frac{10}{21}<
 \left|\frac{\sin\pi(e_*+z)}{\sin\pi z}\right|
 <\frac{11}{5},\qquad |\Re\Psi_z|<1.
\tag{12}
\]
For the ratio bounds, both real sine factors exceed \(1/2\),
while their upper bounds are
\(\cosh(.121\pi)<11/10\) and
\(\cosh(.07\pi)<21/20\). The positive cosh series, with
successive terms bounded geometrically, proves these bounds using
\(\pi<22/7\). The logarithm estimates
\(\log(10/21)>-3/4\), \(\log(11/5)<4/5\)
follow from the positive exponential series through degrees three
and four, respectively. Finally \(|\pi h_e|<17/100\),
which proves the last inequality of (12).

The [original actual cap value](research_mixed_cap_real_cut_gaps.md)
exceeds one. Since
\(|y-a|<51/250\), (12) gives
\(\Re\Psi(e_*,y+ic)>199/250\).
For every height between \(c\) and \(H\), the original arguments
give
\(\Im g'(e_*+z)<0<\Im g'(z)\), because the summed real
part lies in \((1/2,1)\) and \(y\in(0,1/2)\).
Equation (11) therefore shows strict increase when the height is
raised. We have proved the pointwise bound
\[
             A_0(y)>199/250=3/4+23/500.
\tag{13}
\]
The literal endpoint ceilings introduce no additional profile.

The packet in (8), zero-safe tail bounds, and Fourier kernels are
uniform on their stated fixed compact domains. Half-grid cuts cost
an arbitrarily small rate tolerance. The same is true on a small
fixed color disk, by the complete endpoint packet and its full-row
color bounds. Combining all pieces proves (7); Cauchy's formula
gives fixed color derivatives on a smaller disk. This argument
retains the whole inner endpoint coefficient before the outer
private sum. \(\square\)

## 3. The ordinary factor: three real-row profiles suffice

Define
\[
\begin{split}
 B_0(y,v)&=\max_{.15\le x\le.5}\Re Q(x+ih_s;z,b),\\
 B_L(y,v)&=\Re Q(.15;z,b),\qquad
 B_R(y,v)=\Re Q(.5;z,b),\\
 B_1(y,v)&=2\pi(h_b)_+.
\end{split}
\tag{14}
\]
The last expression is the limiting full last-row rate; it is not
the value of the central-strip branch of \(Q\) at \(s=1\).

**Lemma 2.** Uniformly on (1),
\[
 |C_{0,N}(X,Y)|\le C_\tau N^{B_\tau}
       \exp N\{\max(B_0,B_L,B_R,B_1)+\tau\}.
\tag{15}
\]

*Proof.* Keep the original conditional contour with real cuts
\(.15,.5\), and horizontal aliases at \(\pm.2i\).
The [pointwise alias proof](research_mixed_horizontal_alias_transport.md)
allows all outer heights in \([-.12,.12]\). Its derivative
inequalities extend to real index \(.5\), as explained in the
[half-index extension](research_mixed_half_index_contour.md).
They therefore apply at the selected incoming height \(H\),
without invoking an unselected supporting-plane theorem there.
Specifically, at each real \(x\in[.15,.5]\),
\[
\begin{split}
 \Re Q(x-.2i;z,b)-.4\pi
 &\le\Re Q(x+ih_s;z,b)-557\pi/6250,\\
 \Re Q(x+.2i;z,b)-.4\pi
 &\le\Re Q(x+ih_s;z,b)-267\pi/6250.
\end{split}
\tag{16}
\]
These bounds are independent of the cap private index and remain
valid after adding either full Fourier alternative (5).
In particular a double horizontal alias is bounded by the
corresponding cap-only alias and the ordinary main line.

The same global bounds
\(-29\pi/25<\Im Q_s<29\pi/25\)
make every weighted ordinary vertical alias decrease away from
its real-cut endpoint. The zero-mode joins lie between heights
zero and \(h_s\). The ordinary pair Hessian on that compact strip
is positive in negative real part, by the half-index theorem,
also at incoming height \(H\). Thus the joins are vertically
convex and bounded by their real-cut and main-line endpoints.

The full real-row rate is
\[
 E(t;z,b)=\int_0^t\log|1-e^{-2\pi i(z+x)}|\,dx
       +\int_0^t\log|1-e^{-2\pi i(b+x)}|\,dx
       -2J(t)-2\pi Ht.
\tag{17}
\]
Its left tail increases to \(.15\) by the full-plateau sine
ratio argument in Section 6 of the
[ordinary contour reduction](research_mixed_horizontal_asymmetric_contour.md).
The [right-tail endpoint theorem](research_mixed_right_tail_endpoint_bound.md)
applies because \(|H|,|h_b|<.108\). It gives
\(\max_{.5\le t\le1}E(t)=\max(E(.5),E(1))\).
The cuts equal their \(Q\) values, and
\(E(1)=2\pi(-H)_++2\pi(h_b)_+=B_1\).
This includes every wrapped or revived real row, with zero-safe
limits. The exact residue coefficient remains \(+N\).
The original interpolation, its polynomial factors, and half-grid
rounding now give (15) with one tolerance. \(\square\)

## 4. The known literal current and the nineteen remaining profiles

For fixed \(y,v\), the two main maxima vary over independent
private indices but share all outer targets and the same reference.
Consequently the central theorem says precisely
\[
 A_0(y)+B_0(y,v)+W_\sigma(y)
       <M+\ell_b(v)-1/500,
       \qquad \sigma\in\{\mathrm{fac},\mathrm{force}\}.
\tag{18}
\]
No separate maximization over incompatible reference data is used.

Let \(U_N^{\rm hor}\) and \(C_N^{\rm hor}\) denote the
actual zero-mode horizontal integrals of (8) and of the original
conditional interpolation, including their respective \(+N\)
coefficients. They are evaluated at the fixed heights \(h_e,h_s\),
with the same half-grid real endpoints as the exact residue formulas.
They are defined currents, not approximations obtained by deleting
all other terms of the finite sums.

**Corollary 3 (the literal main-current product).** For every
\(\tau>0\), both parities and every fixed ordinary-color
derivative obey
\[
 \left|\partial_w^k\{
 U_N^{\rm hor}(w,X)C_N^{\rm hor}(X,Y)
                           d_N(X)X^{-N}\}\right|
 \le C_{\tau,k}N^{B_{\tau,k}}
     e^{N\{M+\ell_b(v)-1/500+\tau\}}.
\tag{19}
\]
The estimate holds on a sufficiently small fixed ordinary-color
disk. The complete endpoint packet bounds (8) uniformly there;
the conditional factor has no ordinary-color argument. Equation
(18), the full Fourier upper bound (5), compact-contour integration,
and one total tolerance prove (19). Fixed derivatives follow on a
smaller color disk. In particular this is a bound for a specified
literal current of the original source, with both Fourier branches
retained. It is not yet a bound for (2).

For a concrete complete-source criterion, let
\(\mathcal A=\{0,L,R,-,+\}\),
\(\mathcal B=\{0,L,R,1\}\), and put
\[
 \mathcal D(y,v)=
 \max_{\substack{i\in\mathcal A,\ j\in\mathcal B\\
                         (i,j)\ne(0,0)}}
 \max_\sigma
 \{A_i(y)+B_j(y,v)+W_\sigma(y)-M-\ell_b(v)\}.
\tag{20}
\]
There are nineteen pairs in (20), each with the same two Fourier
alternatives. Equivalently they are the following seven grouped
comparison families, with all indicated maxima still present:

| Cap profile | Ordinary profile | Number of pairs |
|---|---|---:|
| \(A_0\) | \(B_L,B_R,B_1\) | 3 |
| \(A_L\), separately \(A_R\) | each of \(B_0,B_L,B_R,B_1\) | 8 |
| \(A_-\), separately \(A_+\) | each of \(B_0,B_L,B_R,B_1\) | 8 |

Multiplying (7), (15), and the whole Fourier bound yields the
proved finite inequality
\[
 |\partial_w^k\mathcal K_N(w;X,Y)|
 \le C_{\tau,k}N^{B_{\tau,k}}
 \exp N\{M+\ell_b(v)+
                     \max(-1/500,\mathcal D(y,v))+\tau\}.
\tag{21}
\]
Thus a uniform negative bound for the nineteen explicit profiles
would complete this selected two-factor source comparison. The
already completed unselected cut certificates do not supply that
bound at height \(H\). The central gap alone does not control
their real-height endpoints, and vertical convexity bounds a join
by both endpoints rather than by its shifted endpoint alone.

All bounds here concern only the two factors (2), so no positive
error is accumulated per later vertex. The outgoing tangent (4)
is retained for subsequent gluing. Target derivatives transverse
to the displayed real plateau would require an ambient source
estimate; they are not claimed by (19) or (21). Other selections,
nonplateau targets, a next type-four block, and length two remain
outside this reduction.
