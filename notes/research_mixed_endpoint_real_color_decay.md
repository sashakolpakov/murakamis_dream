# Real outside-color decay for the literal mixed endpoint factors

Research deduction, 5 November 2026. The original endpoint coefficient,
and both whole first caps, admit a strict real outside-color loss at
their complete-color action. This is an estimate of their exact finite
sources, including the physical and revived rows. It does not continue
a small-color asymptotic to the entire real color interval. No new
numerical comparison is needed.

## 1. Exact source and the factorwise input

Use the original sine factorial, Newton polynomials and phases from
[the endpoint rectangle theorem](research_mixed_endpoint_cap_rectangle.md):
\[
\begin{split}
 C_N(e,w)&=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\\
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\qquad
 E_c=[.27,.49]+i[-.055,.04].
\end{split}                                                    \tag{1}
\]
All roots and logarithms retain the original branches. Set
\(D(\theta)=1-\cos\theta\). The exact Newton interpolation is
\[
 \mathcal E_N(u,\theta)=
 \frac{N}{G_N(Nu)^2
 G_N((N-1)/2-Nu+N\theta/(2\pi))
 G_N((N-1)/2-Nu-N\theta/(2\pi))}.
                                                               \tag{2}
\]
It equals \(e_l(-2\cos\theta)\) at every \(u=l/N\).
On any compact rectangle
\(0<\alpha\le\Re u\le\beta<1/2\), \(|\Im u|\le H\),
the [factorial boundary inequality](research_uniform_factorial_and_boundary_decay.md),
Sections 3--4, proves directly that
\[
 |\mathcal E_N(u,\theta)|\le C N^A
 e^{N\{\Re V_0(u)-c_0D(\theta)\}},\qquad
 V_0(u)=-2J(1/2-u)-2J(u),
                                                               \tag{3}
\]
uniformly for \(-\pi\le\theta\le\pi\), where one may take
\[
 c_0=\min_{\alpha\le x\le\beta,\ |h|\le H}
             \frac{\sin(2\pi x)}{4\pi\cosh^2(\pi h)}>0.
                                                               \tag{4}
\]
The reflected reciprocal factorial keeps both exponential terms.
Consequently (3) includes every moving zero and both signs of the
index height; it is not a quotient by a complete-color Newton value.

For physical rows use the full real-color entropy of
[the zero-safe Newton theorem](research_mixed_newton_color_tubes.md):
\[
 \begin{split}
 |e_l(-2\cos\theta)|&\le C N^A e^{N V_\theta(l/N)},\\
 0\le V_\theta(x)&\le V_0(x)\quad(0\le x\le1/2),\\
 V_\theta(x)&\le0\quad(1/2\le x\le1).
 \end{split}                                                   \tag{5}
\]
The last line is deliberately weaker than the complete-color upper-half
entropy. The latter is negative and need not majorize other real colors.

## 2. The whole endpoint coefficient and the original H polynomial

**Theorem 1.** There are \(c,C>0\) and \(A<\infty\) such that
\[
 |C_N(e,-2\cos\theta)|
 \le C N^A e^{N\{\Re S(e)-cD(\theta)\}}
       \qquad(e\in E_c,\ -\pi\le\theta\le\pi).
                                                               \tag{6}
\]
The estimate also holds on a sufficiently small fixed neighborhood of
\(E_c\), with possibly smaller \(c\). Separately, for every compact
real interval \(I\subset(0,1)\), (6) holds uniformly for physical
indices \(e=j/N\in I\), with constants depending on \(I\).
Both parities and all fixed ordinary-color derivatives obey the same
exponents with polynomial cost.

*Proof on the rectangle.* Keep the precise cuts and contours of the
endpoint rectangle theorem: \(a=1/20\), \(b=\Re e-1/100\),
and the original upper critical height \(\Im u_c(e)\), together
with its lower reflected contour and every vertical current. These
wire contours lie in a compact rectangle of the kind used in (3).
The complete-color proof bounds their weighted absolute densities by
\(\operatorname{poly}(N)e^{N\Re S(e)}\); its nonprincipal
currents have strict gaps. Insert (3) into the exact interpolated
summand before integrating. All other factorial factors and residue
kernels are independent of \(\theta\). Every retained contour
therefore gains the same \(c_0D(\theta)\) loss. The exact constant
residue coefficient remains \(+N\).

For omitted physical rows below \(1/2\), (5) gives the original
complete-color upper entropy. The first two real-tail comparisons of
the endpoint rectangle theorem therefore retain their gaps, at least
\(1/5\) and \(1/50\) before a common small tolerance.

For all revived rows \(x=l/N\ge1/2\), put \(v=1-x\),
\(h=\Im e\), and use only \(V_\theta(x)\le0\).
The same reciprocal reflection as in
[the endpoint extension criterion](research_mixed_endpoint_packet_extension_criterion.md),
Section 2, gives their real upper rate
\[
 \begin{split}
 R_\theta(e,1-v)
 &\le J(v)-\Re J(e+v)+\pi|h|-\pi(1-v)h\\
 &\le-\Re J(e)+2\pi h_-+(\pi/2)h_+.
 \end{split}                                                   \tag{7}
\]
Indeed \(J(v)\le0\). Also \(\Re J(e+v)\ge\Re J(e)\)
for \(1/6<\Re e<1/2\), \(0\le v\le1/2\): before the
half point its horizontal derivative is positive, and above the half
point its real value is nonnegative while \(\Re J(e)<0\).
These are the same branch and vertical comparisons used in that
criterion. The rectangle's third certified gap puts (7) at least
\(1/3\) below \(\Re S(e)\). Thus the entire omitted sum has
some uniform gap \(\delta>0\), for all real outside colors.
Since \(D\le2\), take \(2c<\delta\) and \(c\le c_0\).
This proves (6) after polynomial factors and half-grid shifts are
included. All strict gaps, root chambers and rate bounds persist on
a sufficiently small fixed neighborhood of the closed rectangle;
the complete-color contour remains the one used for this upper bound.

*Proof on compact physical intervals.* Below \(e=1/2\), the
original physical sum has \(l\le j\), so all its real rows use
the first inequality in (5). Insert (3) on the existing interior
contours of [the real-index theorem](research_complete_boundary_coefficient_asymptotic.md)
and absorb its omitted-row gap as above.

For \(1/2\le e<1\), use the contours of
[the full-index theorem](research_complete_boundary_full_index_interval.md).
For an upper-half physical row \(u=1/2+x\le e\), put
\(a=e-1/2\). Its new upper rate satisfies
\[
 V_\theta(u)-J(u)-J(e-u)
 \le J(1/2-x)-J(a-x)\le-J(a).
                                                               \tag{8}
\]
The last inequality follows by integrating the increasing function
\(J'\) on \((0,1/2)\), exactly as in that theorem's (21).
The original selected rate satisfies \(\Re S(e)>-J(a)\).
The omitted lower-half rows still use (5), and retained contours use
(3). Compactness gives common constants, including across \(e=1/2\).
No packet is extrapolated to the index endpoints zero and one.

Finally each finite source is an ordinary polynomial of degree at most
\(N-1\). For such a polynomial, a real estimate
\(C N^A e^{N(M-cD(\theta))}\) implies
\[
 |Q_N(-2\cos(\theta+i v))|
 \le C N^A e^{N\{M-cD(\theta)+(1+c)|v|\}}.
                                                               \tag{9}
\]
To see this, multiply its angular Laurent polynomial by
\(z^{N-1}e^{-Ncz}\), \(z=e^{i\theta}\), and use the disk
maximum principle; evenness handles the other half-plane. An ordinary
color circle of radius \(N^{-2}\) changes an inverse-cosine angle by
\(O(N^{-1})\), uniformly including both quadratic branch points.
Cauchy's formula then costs only \(N^{2k}\) for the fixed ordinary
derivative of order \(k\), with only an \(O(1)\) additive change
in the logarithmic exponent.
This proves the derivative assertion without dividing a finite zero.
\(\square\)

The exact original polynomial, not merely its physical samples, satisfies
\[
 H_N(w,e^{2\pi ie})=G_N(Ne)C_N(e,w).
                                                               \tag{10}
\]
This is [the terminal identity](research_mixed_terminal_right_endpoint_reduction.md),
equation (1), also obtained directly by applying the factorial functional
equation to each Pochhammer term. Hence (6) gives
\[
 |H_N(-2\cos\theta,e^{2\pi ie})|
 \le C N^A e^{N\{\Re[J(e)+S(e)]-cD(\theta)\}}
                                                               \tag{11}
\]
on \(E_c\), and on every compact real physical-index interval.
The same ordinary derivatives are permitted. This is a calibrated
endpoint rate, not its positive Newton triangle ceiling.

## 3. Both complete caps inherit the real-color loss

Use the literal whole cap
\[
 U_{\alpha,N}(w,X)=\sum_{i=0}^{N-1}
       \frac{H_N(w,r^{-i})(rX;r)_i}{(r;r)_i^{1+\alpha}},
 \qquad\alpha=0,1.
                                                               \tag{12}
\]
For the actual attached image set \(K_{3+\alpha}\) of
[the complete cap theorem](research_mixed_complete_first_cap_packet.md),
let \(\mathcal T_\alpha(z,w)\) be its original calibrated phase.
There are a fixed complex neighborhood \(\mathcal O\) of that set
and \(c_U>0\) such that
\[
 |U_{\alpha,N}(-2\cos\theta,e^{-2\pi iz})|
 \le C N^A e^{N\{\Re\mathcal T_\alpha(z,-2)-c_U D(\theta)\}}
 \quad(z\in\mathcal O,\ -\pi\le\theta\le\pi).
                                                               \tag{13}
\]
For every actual first-cap reference of a word of length \(m\ge2\),
write \(z_*=a+ic_*\), and retain the allocated supporting plane
\(B_L(z_*;y)\) of
[the completed cap plateau theorem](research_mixed_first_cap_plateau_completion.md).
Uniformly for independent \(y\in P=[.22,.45]\),
\[
 |U_{\alpha,N}(-2\cos\theta,e^{-2\pi i(y+ic_*)})|
 |d_N(e^{-2\pi i(y+ic_*)})|^{\alpha/2}
 \le C N^A e^{N\{B_L(z_*;y)-c_U D(\theta)\}}.
                                                               \tag{14}
\]
The constants may be decreased to make both assertions simultaneous.
All fixed ordinary-color derivatives satisfy the same rates.

*Proof.* On the entire original private rectangle \(E_c\), replace
the endpoint packet upper bound by (6). Every retained cap density,
join and alias thus keeps its original complete-color exponent with
the extra \(cD(\theta)\) loss. This step uses the whole exact
\(C_N\), not its local leading term or an arbitrarily restricted
Newton sum. The other factors in (12) are color independent.

For the compact portions of the physical private tails use the
physical-index assertion of Theorem 1. Their upper rates are the
original \(R_\alpha(s,z)\), so all monotonicity and cut comparisons
in [the real-tail theorem](research_mixed_outer_cap_real_tails.md)
and its [full-plateau extension](research_mixed_first_cap_plateau_phase.md)
remain valid for every real color.

The literal extreme rows require a separate check. For \(s=i/N\le.01\),
all physical Newton indices obey \(l/N\le s<1/2\); (5) preserves
the original ceiling \(1/4\). For \(s=1-\delta\ge.99\), the
unallocated coefficient entropy is bounded by
\[
 V_\theta(u)+J(u+\delta)-J(u)
 \le b_2+\delta\log2,\qquad
 b_2=\max_{0\le u\le1/2}V_0(u)<3/5.
                                                               \tag{15}
\]
Here \(u\le s\), and (5) gives \(V_\theta(u)\le b_2\) on
both halves. The same exact outgoing-product estimate therefore gives
the original ceiling \(3/4\), uniformly in the real color. These
two endpoint sectors keep a strict gap: the local cap action exceeds
one, and the full-plateau bare plane exceeds \(79/100\).
The compact tails and all other noncentral cap currents have the
completed original strict gaps. Absorb every color-independent gap
by reducing \(c_U\), using \(D\le2\), and take one common finite
tolerance smaller than the remaining margins. On real colors the
factorial and zero-safe product estimates have polynomial errors at
their stated rates, so the final bounds have exactly the exponents
shown in (13)--(14).

For \(\alpha=1\) the actual outgoing height is negative. Its original
unselected Fourier halfweight is precisely the one used in (14).
The convex remainder of \(\Re g\) pays it as in the completed
plateau theorem, without changing the color loss. No Fourier factor
is divided out. The degree argument (9), with this fixed color-independent
weight carried along, gives all ordinary derivatives. \(\square\)

## 4. A local complex outside strip and the remaining global obligation

On a smaller neighborhood in (13), its existing nonzero holomorphic
cap packet has the original angular Hessian
\[
 \left.\partial_\theta^2
  \mathcal T_\alpha(z,-2\cos\theta)\right|_{\theta=0}
       =-\frac{\tan(\pi u_*(z))}{2\pi},\qquad
                     \Re\tan(\pi u_*(z))>0.
                                                               \tag{16}
\]
Combining (13), (16), and the one-variable patching proof in
[the outside-color stability reduction](research_mixed_open_source_stability_reduction.md)
gives a fixed thin angular strip with the stronger bound
\[
 |U_{\alpha,N}(-2\cos(\theta+i v),e^{-2\pi iz})|
 \le C N^A e^{N\{\Re\mathcal T_\alpha(z,-2)
                      -c'(1-\cos\theta)+Bv^2\}}.
                                                               \tag{17}
\]
This local-in-\(z\) assertion includes both cap types and every actual
open-word endpoint image. Equation (14) supplies the real outside-color
loss on the larger fixed-height plateau, without asserting a moving
critical packet there.

These estimates settle an actual endpoint-factor obligation: all its
original contour currents and omitted physical rows keep a calibrated
complete-color ceiling, and the surviving part has a uniform ordinary
outside-angle loss. They do not by themselves bound the rest of a
mixed open word on all retained selections and nonplateau coordinates.
In particular they do not imply a whole-word outside-color gap from
the value of a cancelling complete-color contraction, do not extend
the outgoing target to its full period, and do not supply the marked
geometric boundary germ required for arbitrary short-filling stability.
