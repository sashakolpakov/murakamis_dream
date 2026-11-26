# The original critical curve of the prepared three-four cap

Research deduction, 7 November 2026. The original complete-cap critical
equations reduce to one explicit rational Fourier closing map. On the
proved cap rectangle, a simple endpoint chamber condition forces every
logarithmic lift to be zero. Any admitted preimage of the alternating
Fourier parameter is unique and unramified. This identifies an exact
one-variable existence problem; it does not prove that the required
preimage exists, or a whole finite-source asymptotic. No numerical
evaluation is used.

## 1. Original equations and the Fourier closing map

Use the exact source and unchanged primitives of
[the prepared-cap source theorem](research_mixed_prepared_three_four_cap_source.md).
At complete ordinary color put
\[
\begin{split}
 B(s,u)&=-2J(1/2-u)-3J(u)-J(s-u)+i\pi su
                                  -\frac{i\pi}{2}(s-s^2),\\
 \widehat F(u,s,t,p,q;y)&=B(s,u)+g(s+t)+g(t+p)+g(p+q)\\
 &\hspace{12mm}-2g(t)-3g(p)-g(q)+2\pi itp+\ell_q(y).
\end{split}
\tag{1}
\]
Thus eliminating the original endpoint root \(u=u_c(s)\) gives
exactly \(\mathcal F_{\mathrm{cap}}\) of that theorem, with its
original additive constant. Define
\[
 U=e^{-2\pi iu},\quad Z=e^{-2\pi is},\quad
 T=e^{-2\pi it},\quad P=e^{-2\pi ip},\quad Q=e^{-2\pi iq},
 \qquad Y=e^{2\pi iy}.
\tag{2}
\]
Here \(U\) is the reciprocal of the endpoint parameter in
[rational critical transport](research_mixed_rational_critical_transport.md).
The endpoint reduction and the ordinary transfer below are already
proved there; the last Fourier closing equation is the additional
operation required by this prepared source.

All logarithms in the following formulas are the original ones. The
endpoint derivative and the other four derivatives are
\[
\begin{split}
 \widehat F_u={}&2\Log\cos\pi u+\Log\sin\pi(s-u)
                                      -3\Log\sin\pi u+i\pi s,\\
 \widehat F_s={}&\Log(1-ZT)-\Log(1-Z/U)+2\pi iu,\\
 \widehat F_t={}&\Log(1-ZT)+\Log(1-TP)-2\Log(1-T)+2\pi ip,\\
 \widehat F_p={}&\Log(1-TP)+\Log(1-PQ)-3\Log(1-P)+2\pi it,\\
 \widehat F_q={}&\Log(1-PQ)-\Log(1-Q)-\Log(1-YQ)+2\pi iy.
\end{split}
\tag{3}
\]
The sine and cosine logarithms on the first line continue from positive
real arguments. Their constants cancel as \(2+1-3=0\).
The remaining logarithms are principal on their stated strips. In
particular, the first-cap derivative follows from the exact independent
leg identity in [endpoint action calibration](research_mixed_endpoint_action_calibration.md),
not from an exponentiated replacement of its action.

Exponentiating (3) at a critical point gives
\[
\begin{split}
 (U+1)^2(U-Z)&=Z(U-1)^3,&
 U-Z&=1-ZT,\\
 (1-ZT)(1-TP)&=P(1-T)^2,&
 (1-TP)(1-PQ)&=T(1-P)^3,\\
 Y(1-PQ)&=(1-Q)(1-YQ).&&
\end{split}
\tag{4}
\]
The chirp contributes the displayed \(P\) and \(T\) factors.
Solving successively defines rational functions
\[
\begin{split}
 Z(U)&=\frac{(U+1)^2}{U^2-2U+5},\\
 T(U)&=\frac{1+Z(U)-U}{Z(U)},\\
 P(U)&=\frac{1-Z(U)T(U)}
                   {(1-T(U))^2+T(U)(1-Z(U)T(U))},\\
 Q(U)&=\frac{1-T(U)(1-P(U))^3/(1-T(U)P(U))}{P(U)},\\
 \mathcal Y(U)&=\frac{1-Q(U)}
                         {1+Q(U)-P(U)Q(U)-Q(U)^2}.
\end{split}
\tag{5}
\]
At an original regular critical point every displayed denominator is
nonzero. For example, the denominator defining \(P\) equals
\((1-ZT)/P\), and the final denominator equals \((1-Q)/Y\).
The remaining exclusions follow from the original sine strips.
Conversely, on the set where these rational expressions and their
logarithm arguments are regular and nonzero, (5) implies (4).

The intended closing value is exactly
\[
 K=(1+2a-4a^2)^{-1},\qquad y=x_0,
\tag{6}
\]
where \(a\) is the already isolated original quartic root in
[the alternating interface](research_three_four_source_interface.md).
Its original branch identification with \(e^{2\pi ix_0}\) is
proved in [the power-three reference packet](research_three_vertex_mixed_reference_packet.md),
equation (2). No new algebraic branch of \(K\) is selected here.

## 2. An explicit filter forces the original zero lifts

Retain the compact rectangle of the prepared-cap source theorem:
\[
\begin{split}
 E_c&=[27/100,49/100]+i[-55/1000,1/25],\\
 T_c&=[11/50,1/2]+i[-3/100,3/200],\\
 R_c&=[1/5,21/50]+i[-11/200,3/200].
\end{split}
\tag{7}
\]
Suppose the nonzero rational coordinates in (5) have lifts satisfying
\[
 (s,t,p,q)\in E_c\times T_c\times R_c^2,
 \qquad 0<\Re u<\Re s<1/2,\qquad \Im u>0.
\tag{8}
\]
The displayed real intervals fix the coordinate lifts uniquely.
For the output require \(0<\Re y<1/5\) and \(\Im y>0\),
as holds on a sufficiently small neighborhood of \(x_0\).
All single and sum factorial arguments in (3) have real part in
\((0,1)\), while \(0<\Re(q-y)<1/2\). Hence the
incidence logarithm also has its original principal branch.

**Proposition 1.** If (4) and (8) hold on these regular branches, all
five original derivatives in (3) vanish. Moreover \(u=u_c(s)\).

*Proof.* For \(r>0\) and \(0<x<1\), elementary argument geometry
gives
\[
 \min\{0,\pi(1-2x)\}\le
       \Arg(1-r e^{-2\pi ix})
       \le\max\{0,\pi(1-2x)\}.
\tag{9}
\]
The inequalities are strict except at \(x=1/2\), where the
argument is zero. Indeed the point \(1-r e^{-2\pi ix}\)
moves along a ray from the positive real number one, and its argument
lies strictly between the arguments at the two ends of that ray.

First set \(x=\Re u\), \(e=\Re s\). Since \(\Im u>0\),
\[
 -\pi x<\Arg\cos\pi u<0,
 \qquad 0<\Arg\sin\pi u<\pi/2-\pi x.
\]
Also \(0<e-x<1/2\), so
\(-\pi/2+\pi(e-x)<\Arg\sin\pi(s-u)
 <\pi/2-\pi(e-x)\). Consequently
\[
 -2\pi+2\pi e<\Im\widehat F_u<\pi/2+\pi x<\pi.
\tag{10}
\]
The first equation in (4) makes its exponential one; thus this
derivative is zero. At fixed \(s\), on the convex chamber
\(0<\Re u<\Re s\), \(\Im u>0\),
\[
 -\Re B_{uu}
 =\pi\Re\{2\tan\pi u+3\cot\pi u+\cot\pi(s-u)\}>0.
\tag{11}
\]
Every summand has positive real part in the indicated strips.
Integration on a complex segment proves injectivity of \(B_u\).
The already proved \(u_c(s)\) lies in this chamber, so the two
roots coincide.

Next, \(0<\Arg(1-Z/U)<\pi\),
\(-\pi<\Arg(1-ZT)<\pi\), and \(0<2\pi\Re u<\pi\).
Thus \(-2\pi<\Im\widehat F_s<2\pi\).
For clarity the bounds for the remaining rows, from (9), are
\[
\begin{array}{c|cc}
 &\text{lower bound for }\Im\widehat F_j/\pi
 &\text{upper bound for }\Im\widehat F_j/\pi\\ \hline
 t&-29/25&51/50\\
 p&-9/5&34/25\\
 q&-41/25&3/5 .
\end{array}
\tag{12}
\]
These are strict bounds, and each lies inside \((-2,2)\).
Here are the cancellations that keep the lower bounds inside that
interval. Write \(s_R,t_R,p_R,q_R,y_R\) for real parts.
In (9), the possible positive-argument allowances for \(s+t,t+p,p+q\)
are respectively \(1/50,4/25,1/5\), after division by \(\pi\).
Thus their arguments have lower bounds \(1-2(s_R+t_R)-1/50\),
\(1-2(t_R+p_R)-4/25\), and
\(1-2(p_R+q_R)-1/5\).
Combining with the single-leg upper argument bounds gives
\[
\begin{split}
 \Im\widehat F_t/\pi&>-2s_R-9/50\ge-29/25,\\
 \Im\widehat F_p/\pi&>-34/25+2p_R-2q_R\ge-9/5,\\
 \Im\widehat F_q/\pi&>-6/5-2p_R+2q_R\ge-41/25.
\end{split}
\tag{13}
\]
For the last row use the additional argument upper bound
\(1-2(q_R-y_R)\) for \(1-YQ\); the \(y_R\) terms
cancel. The upper bounds in (12) follow by dropping the negative
single-leg arguments, and using respectively
\(1/50+4/25+2p_R\), \(4/25+1/5+2t_R\), and
\(1/5+2y_R\). Equations (4) place every row in
\(2\pi i\mathbb Z\), so all four vanish. \(\square\)

The endpoint condition in (8) is a sufficient explicit branch filter;
it is not permission to use a different root of the endpoint quadratic.
Proposition 1 proves that this filter identifies the already continued
complete endpoint branch.

## 3. Uniqueness and nonramification of an admitted preimage

**Proposition 2.** On a sufficiently small fixed neighborhood of
\(Y=K\), at most one regular preimage in (5) satisfies (8).
At every such preimage \(\mathcal Y'(U)\ne0\). Consequently
an admitted preimage, if established at \(K\), has a unique
holomorphic continuation for nearby Fourier outputs and nearby
ordinary colors.

*Proof.* By Proposition 1, admitted preimages are zeros of the original
collapsed four-variable phase. The prepared-cap source theorem proves
strict accretivity of its negative Hessian throughout the convex
product (7), uniformly for nearby outputs and ordinary colors.
Integrating that Hessian proves uniqueness; its invertibility gives
local continuation. The scalar endpoint branch is already unique.

There is a stronger differential fact than invertibility alone. Let
\(H=\mathcal F_{\mathrm{cap},(s,t,p,q)}''\) at an admitted
point. It is tridiagonal, with the three adjacent entries
\[
 H_{st}=\frac{2\pi iZT}{1-ZT},\qquad
 H_{tp}=\frac{2\pi i}{1-TP},\qquad
 H_{pq}=\frac{2\pi iPQ}{1-PQ}.
\tag{14}
\]
All are nonzero. Also
\[
 \partial_y\widehat F_q=\frac{2\pi i}{1-YQ}\ne0,
 \qquad
 (H^{-1})_{s,q}=-\frac{H_{st}H_{tp}H_{pq}}{\det H}.
\tag{15}
\]
Implicit differentiation therefore gives \(s_y\ne0\).
At the endpoint,
\[
 B_{us}=\frac{2\pi i}{1-Z/U}\ne0,
 \qquad u_c'(s)=-B_{us}/B_{uu}\ne0
\tag{16}
\]
by (11). Hence \(U_y=-2\pi iUu_c'(s)s_y\ne0\).
Differentiating the exact identity
\(\mathcal Y(U(y))=e^{2\pi iy}\) proves
\[
                  \mathcal Y'(U)U_y=2\pi iY\ne0.
\tag{17}
\]
No global inverse branch of the rational curve is asserted.
Continuation in ordinary color uses the original holomorphic endpoint
action and the same Hessian, rather than formula (5), which was derived
only at complete color. \(\square\)

## 4. What this resolves and what it does not

For the actual prepared source the missing local existence assertion is
now exactly: \(\mathcal Y(U)=K\) has a regular preimage with
the coordinate lifts (8). Such a preimage automatically has every
original zero logarithmic lift, is the original endpoint branch, and
is unramified. This is more specific than selecting an arbitrary root
of a cleared-denominator polynomial.

The existing endpoint theorem with a typed external inverse leg does
not prove that assertion. It localizes a half-chain before changing
the outgoing polarization. The
[cap phase entrance theorem](research_mixed_alternating_cap_phase_entrance.md)
performs that change near \(x_0\) only for sufficiently long
alternating suffixes, not for this two-letter prefix. No existing
result here establishes the required preimage at \(K\).

If that preimage is proved, the source theorem already gives the
nonzero local current with its own action, determinant and
\(\kappa^3N^{-1}\) normalization. All physical complements,
joins and aliases for the complete prepared cap remain separate.
Nothing in this rational reduction changes the full-kernel theorem,
the whole-message entrance requirement, or a knot-family statement.
