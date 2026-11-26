# The finite first-four/next-four product at its selected height

Research deduction, 6 November 2026.

The proved next-four central gap extends to the literal product of the
two main horizontal currents with the complete selected Fourier
polynomial and the original outgoing halfweight. The whole finite
product reduces to five independent boundary-profile pairs per Fourier
alternative. The cap aliases, right cap cut, and all ordinary last-row
pairs require no further comparison.

The ordinary left cut has a different signed height cost from its
next-three counterpart. Section 4 gives a quantitative trial bound for
this cut, including its extra index factorial and a positive vertical
curvature term. Its uniform sign on the actual coupled references is
not established here. No root, source evaluation, or new interval cover
is used in this deduction.

## 1. The literal source and a sufficient finite-source theorem

Fix the actual critical reference of a mixed open word with \(m\ge3\),
first two types four, and every later type three or four. Use the
branches and action in the
[next-four central-gap theorem](research_mixed_first_four_next_four_central_gap.md).
Set
\[
 \begin{gathered}
 H=1/100,\quad z=y+iH,\quad b=v+ih_b,\quad y,v\in P=[.22,.45],\\
 -.051<h_e<-.019,\qquad -.102<h_s,h_b<-.001,\\
 z_*=a+ic,\qquad -.078<c<-.020.
 \end{gathered}
 \tag{1}
\]
The three unchanged heights belong to that same actual reference.
The outgoing target \(b\) is the second coordinate of the neighboring
ordinary block, rather than the next external input used to construct
its reference.

With \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), \(X=e^{-2\pi iz}\), and \(Y=e^{-2\pi ib}\),
define the literal finite kernels
\[
 \begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
       \frac{H_N(w,r^{-i})p_i(X)}{P_i^2},\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
 \mathcal K_N(w;X,Y)&=U_{1,N}(w,X)C_{1,N}(X,Y)d_N(X)X^{-N}.
 \end{split}
 \tag{2}
\]
These are the kernels of the
[exact conditional torus composition](research_mixed_conditional_torus_composition.md).
The outgoing allocation is the separate modulus factor
\(|d_N(Y)|^{1/2}\). It is not a holomorphic square root.
There is one complete \(d_N(X)\) at the selected common coordinate;
no Fourier factor has been divided out. Only the cap depends on the
ordinary color \(w\), whose complete value is \(-2\).

Write the original bare phases as
\[
 \begin{split}
 \Psi(e,z)&=S_{\rm cap}(e)+g(e+z)-g(z)-g(e)
                              -\frac{i\pi}{2}(e-e^2),\\
 Q_4(s;z,b)&=g(s+z)+g(s+b)-3g(s)-g(z)-g(b)+2\pi izs.
 \end{split}
 \tag{3}
\]
The first line equals the cap phase used in the earlier finite
reduction, after the identity
\(g(w)=J(w)+i\pi(w-w^2)/2\). In particular its original chirp
and additive calibration are retained. The joint phase is exactly
\[
 \mathcal F_4=\Psi+Q_4-g(z)-\tfrac12g(b).
 \tag{4}
\]
Set
\[
 M=\Re\mathcal F_4(e_*,s_*;z_*,b_*),\quad
 p=\partial_b\mathcal F_4(e_*,s_*;z_*,b_*),\quad
 \ell_b(v)=\Re p\,(v-\Re b_*).
 \tag{5}
\]

For the cap use
\[
 \begin{array}{ll}
 A_0(y)=\displaystyle\max_{.27\le x\le.49}\Re\Psi(x+ih_e,z),
       &A_L(y)=\Re\Psi(.27,z),\\
 A_R(y)=\Re\Psi(.49,z),&
 A_-(y)=\displaystyle\max_{.27\le x\le.49}
                         \Re\Psi(x-.055i,z)-.11\pi,\\
 A_+(y)=\displaystyle\max_{.27\le x\le.49}
                         \Re\Psi(x+.04i,z)-.08\pi.&
 \end{array}
 \tag{6}
\]
Every ordinary profile includes the same outgoing halfweight:
\[
 \begin{split}
 B_0(y,v)&=\max_{1/8\le x\le1/2}\Re Q_4(x+ih_s;z,b)
                                      -\tfrac12\Re g(b),\\
 B_L(y,v)&=\Re Q_4(1/8;z,b)-\tfrac12\Re g(b),\\
 B_R(y,v)&=\Re Q_4(1/2;z,b)-\tfrac12\Re g(b),\\
 B_1(y,v)&=-\tfrac12\Re g(b).
 \end{split}
 \tag{7}
\]
The last line is the allocated full last-row rate. It is not the
value of the central-strip branch at \(s=1\).
The two full selected Fourier rates are
\[
 W_{\rm fac}(y)=-\Re g(z)-2\pi H,\qquad
 W_{\rm force}(y)=0.
 \tag{8}
\]
They are upper-rate alternatives for the single literal polynomial
\(d_N(X)X^{-N}\), rather than a factorization of that polynomial.

Define
\[
 \begin{split}
 \mathcal I_5&=\{(0,L),(0,R),(L,0),(L,L),(L,R)\},\\
 \mathcal D_5(y,v)&=
 \max_{(i,j)\in\mathcal I_5}\ 
 \max_{\sigma\in\{\mathrm{fac},\mathrm{force}\}}
 \{A_i(y)+B_j(y,v)+W_\sigma(y)-M-\ell_b(v)\}.
 \end{split}
 \tag{9}
\]

**Theorem 1.** For every \(\tau>0\) and each fixed ordinary-color
derivative order \(k\), both level parities satisfy
\[
 \begin{split}
 &|\partial_w^k\mathcal K_N(w;X,Y)|\,|d_N(Y)|^{1/2}\\
 &\quad\le C_{\tau,k}N^{D_{\tau,k}}
 \exp N\{M+\ell_b(v)+\max(-1/500,\mathcal D_5(y,v))+\tau\}.
 \end{split}
 \tag{10}
\]
The estimate holds for all sufficiently large levels on a sufficiently
small fixed ordinary-color disk about \(-2\), uniformly for \(y,v\in P\).
It retains the complete cap coefficient, every ordinary row, all
contour contributions, and the original outgoing allocation.

Consequently a uniform bound \(\mathcal D_5\le-\delta\), with
\(\delta>0\), on the actual coupled references and \(P^2\) would
give the whole weighted finite product a gap
\(\min(1/500,\delta)-\tau\). The five comparisons in (9) remain
unresolved in this note.

## 2. Complete cap and ordinary contour bounds

The cap's five-profile finite bound holds at (1):
\[
 |U_{1,N}(w,X)|\le C_\tau N^{D_\tau}
           \exp N\{\max(A_0,A_L,A_R,A_-,A_+)+\tau\}.
 \tag{11}
\]
Use the exact interpolation and residue coefficient \(+N\) of the
[finite next-three reduction](research_mixed_selected_four_three_finite_reduction.md),
Section 2. Those arguments for the cap do not use the next own type.
The positive-height tail argument explicitly permits \(H\le.014\);
the cap contains no incoming monomial \(X^{-i}\), so its reflected
positive-radius term \(2\pi H(i/N)\) is retained.
The wider original-height comparison in Section 5 of the
[last-row theorem](research_mixed_selected_four_three_last_rows.md)
gives \(A_0>199/250\) throughout the larger range \(-.108<c<-.02\).
It therefore pays both literal endpoint ceilings \(1/4,3/4\) here.
The private rectangle is unchanged, as are the real cuts and alias
penalties. This proves (11), including all real cap tails.

For the own-four ordinary contour use real cuts \(1/8,1/2\), lower
height \(-1/5\), and upper height \(5/4\), as in the
[own-four left-cut extension](research_mixed_four_left_cut_extension.md).
The original fixed contour gives
\[
 |C_{1,N}(X,Y)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{D_\tau}
       \exp N\{\max(B_0,B_L,B_R,B_1)+\tau\}.
 \tag{12}
\]
Here only pointwise contour comparisons are transported to the
positive incoming height; no unselected supporting plane is asserted
there. Indeed the outer height domain in that extension is
\([-.12,.12]^2\), containing \((H,h_b)\). Its horizontal-alias
comparisons, with outer constants canceled, give for every
\(x\in[1/8,1/2]\)
\[
 \begin{split}
 \Re Q_4(x-i/5;z,b)-2\pi/5
   &<\Re Q_4(x+ih_s;z,b)-1893\pi/25000,\\
 \Re Q_4(x+5i/4;z,b)-5\pi/2
   &<\Re Q_4(x+ih_s;z,b)-7/50.
 \end{split}
 \tag{13}
\]
These are literal comparisons to the same real coordinate on the
original main line. The extra allocated term in every \(B_j\) is
constant in this comparison.

The extension's argument bounds make the weighted vertical aliases
decrease away from their real-cut endpoints. Its real Hessian bound,
together with the half-index theorem, gives vertical convexity along
the zero-mode joins between \(0\) and \(h_s\). All joins are therefore
bounded by their real-cut and main-line endpoints. All factorial
arguments remain in the original regular strips on these fixed
compact contours, so the interpolation, original \(+N\) residue
coefficient, and both parities are unchanged.

The bare full real-row rate is
\[
 E_4(t;z,b)=\int_0^t\log|1-e^{-2\pi i(z+x)}|\,dx
       +\int_0^t\log|1-e^{-2\pi i(b+x)}|\,dx
       -3J(t)-2\pi Ht.
 \tag{14}
\]
The original sine-ratio left-tail estimate bounds every \(0\le t\le1/8\)
by its cut. Its proof holds on the full outer height rectangle and
retains the incoming chirp in (14). The
[right-tail endpoint theorem](research_mixed_right_tail_endpoint_bound.md)
applies since \(|H|,|h_b|<.108\), and gives
\[
 \max_{1/2\le t\le1}E_4(t)=\max\{E_4(1/2),E_4(1)\},
 \qquad E_4(1)=2\pi(-H)_++2\pi(h_b)_+=0.
 \tag{15}
\]
This includes wrapped, revived and endpoint rows with zero-safe
limits. Finally \(h_b<0\), so the original unselected Fourier bound
on \(Y\) has upper rate \(-\Re g(b)/2\). Adding it yields exactly
(7) and (12).

The original factorial symbols, complete cap packet and zero-safe
row estimates persist on a small ordinary-color disk. Choose their
total rate tolerance below the prescribed \(\tau\); half-grid cuts
and polynomial prefactors are absorbed in that same tolerance.
Only \(U_{1,N}\) depends on the color. Cauchy's formula on a smaller
disk gives each fixed ordinary-color derivative. This proves the
finite estimates with the scope stated in Theorem 1.

## 3. The proved joint entries and the five remaining pairs

The two main profiles have independent private real indices but share
all outer targets and the same actual reference. Identity (4) and the
central theorem therefore give, pointwise in \(y,v\),
\[
 A_0+B_0+W_\sigma<M+\ell_b-1/500.
 \tag{16}
\]
In particular the product of the literal two zero-mode horizontal
currents, each including its coefficient \(+N\), multiplied by the
whole \(d_N(X)X^{-N}\) and the modulus allocation \(|d_N(Y)|^{1/2}\),
has upper rate \(M+\ell_b-1/500+\tau\). This concerns defined
currents of the exact residue formulas.

The [cap-alias comparison](research_mixed_selected_cap_alias_transport.md)
and [right-cap-cut comparison](research_mixed_selected_cap_right_rows.md)
apply without changing their domains, because \(H=.01<.014\).
They give
\[
 A_-<A_0-1/4,\qquad A_+<A_0-1/50,\qquad
 A_R<A_0-1/1250.
 \tag{17}
\]
These pointwise inequalities may be added to any fixed ordinary
profile and either Fourier alternative. Thus only \(A_0,A_L\)
need independent comparisons.

Section 5 of the last-row theorem applies to either next type, every
\(0\le H\le7/625\), and the original attached range
\(-.108<c<-.02\). It retains the outgoing halfweight on both sides
of the height transport. In the current notation it gives all five
inequalities
\[
 A_i+B_1+W_\sigma
 <M+\ell_b-2\kappa_0(y-a)^2
                -\kappa_0(v-\Re b_*)^2-3/100,
 \quad i\in\{0,L,R,-,+\},\quad \kappa_0=1/2500000.
 \tag{18}
\]
It also controls the literal whole cap times the high-index ordinary
tail \(j\ge\lceil39N/50\rceil\), with denominator \(P_j^3\),
the original outgoing halfweight, and finite gap \(1/40\).

Equations (16)--(18) leave precisely the five pairs (9) per Fourier
alternative. Multiplying (11), (12) and the original full Fourier
upper bound proves (10). An ordinary left-cut comparison
\(B_L\le B_0\), if proved pointwise on the actual references, would
reduce the independent list further to
\[
                    (0,R),\qquad(L,0),\qquad(L,R).
 \tag{19}
\]
No such next-four comparison is imported from the next-three proof.

## 4. A signed quantitative trial for the ordinary left cut

Here is a direct sufficient inequality for that remaining reduction.
It uses the type-four phase and its actual negative heights.
Put
\[
 x_1=1/8,\qquad x_0=11/50,\qquad
 d_0=19/200,\qquad m_0=69/400.
 \tag{20}
\]
For real \(x\in[x_1,x_0]\), the exact marginal of (3) is
\[
 \Re Q_{4,s}(x;z,b)
 =\log\frac{|\sin\pi(x+z)\sin\pi(x+b)|}
                   {2\sin^3\pi x}+\pi(h_b-H).
 \tag{21}
\]
Both the factor \(2\sin^3\pi x\) and the last term are essential.
Dropping the imaginary parts inside the sine moduli gives a lower
bound. The resulting logarithm is convex in \(x\): each
\(\log\sin\pi(x+w)-\log\sin\pi x\) is convex here, and the
additional term \(-\log(2\sin\pi x)\) is convex as well.
The shifted real parts lie in \([.345,.67]\), whose sine exceeds
the sine on \([.125,.22]\). Jensen's integral inequality gives
\[
 \Re Q_4(x_0;z,b)-\Re Q_4(x_1;z,b)
 \ge C_4(y,v)+\pi d_0(h_b-H),
 \quad
 C_4=d_0\log\frac{\sin\pi(m_0+y)\sin\pi(m_0+v)}
                              {2\sin^3\pi m_0}.
 \tag{22}
\]

For the signed height correction define the real cotangent
\[
 a(t,h)=\Re\cot\pi(t+ih)
       =\frac{\sin2\pi t}{\cosh2\pi h-\cos2\pi t},
 \qquad
 U(t,K)=\max\{\cot\pi t,a(t,K)\},\quad K\ge0.
 \tag{23}
\]
For \(|h|\le K\), one has \(a(t,h)\le U(t,K)\).
At the real trial \(x_0\), the exact imaginary derivative is
\[
 \begin{split}
 I_4:=\Im Q_{4,s}(x_0;z,b)
 ={}&\pi(y-v-.28)\\
 &+\pi\int_0^H a(x_0+y,\eta)\,d\eta
  +\pi\int_0^{h_b}a(x_0+v,\eta)\,d\eta.
 \end{split}
 \tag{24}
\]
The term \(-.28\pi\) comes from the extra \(-g(s)\).
Since \(H\ge0\) and \(h_b<0\), a valid signed lower bound is
\[
 \begin{split}
 I_4/\pi\ge L_4:={}&y-v-.28\\
 &+H\min\{\cot\pi(x_0+y),a(x_0+y,H)\}
   +h_b U(x_0+v,|h_b|).
 \end{split}
 \tag{25}
\]
The negative height in the last term selects an upper cotangent
bound. In particular a negative shifted cotangent gives a favorable
positive contribution there.

There is also a quantitative vertical remainder. Put
\[
 \begin{split}
 K_z&=\max\{H,|h_s+H|\},\qquad K_b=|h_s+h_b|,\\
 \mu_4&=\pi\{3a(x_0,h_s)-U(x_0+y,K_z)-U(x_0+v,K_b)\}.
 \end{split}
 \tag{26}
\]
For every index height between \(h_s\) and zero, direct
differentiation gives
\[
 \partial_h^2\Re Q_4(x_0+ih;z,b)
 =\pi\{3a(x_0,h)-a(x_0+y,h+H)-a(x_0+v,h+h_b)\}
 \ge\mu_4.
 \tag{27}
\]
This lower bound is positive on the full height rectangle (1).
Indeed the elementary inequalities
\[
 \sin(.44\pi)>49/50,\quad \cos(.44\pi)>9/50,\quad
 \cosh(.204\pi)<49/40,\quad \cot(.44\pi)<1/5
 \tag{28}
\]
give \(a(x_0,h_s)>196/209\) and both upper shifted
cotangents less than \(1/5\). Hence
\(\mu_4>2522\pi/1045>12\pi/5\).
The trigonometric bounds follow from the sine cubic and cosine
quadratic at \(.06\pi\), with \(157/50<\pi<22/7\);
the hyperbolic bound is the one used in the correlated endpoint proof.

Taylor's integral formula, (24)--(27), and \(-h_s>0\) imply
\[
 \Re Q_4(x_0+ih_s;z,b)-\Re Q_4(x_0;z,b)
 \ge-\pi h_s L_4+\frac{\mu_4}{2}h_s^2.
 \tag{29}
\]
Combining this with (22) proves the explicit trial inequality
\[
 \boxed{\quad
 B_0-B_L\ge
 \mathcal L_4(y,v;h_s,h_b,H):=
 C_4+\pi\{d_0(h_b-H)-h_sL_4\}
                         +\frac{\mu_4}{2}h_s^2.
 \quad}
 \tag{30}
\]
The outgoing \(-\Re g(b)/2\) cancels because it is included on
both sides. Formula (30) permits either the displayed correlated
curvature \(\mu_4\), or the weaker uniform value \(12\pi/5\).
No moving index maximum or source-root calculation enters this bound.

A proof of \(\mathcal L_4\ge0\) on every actual reference and
\(P^2\) would suffice to replace the five-pair defect by the
three-pair defect (19). Such a sign has not been proved here.
The next-three signed-tangent inequalities do not establish it:
the own-factorial angle in (24), the denominator in (21), and the
negative height range have all changed. Theorem 1 consequently
retains the five independent comparisons, with the actual-reference
correlation and original outgoing tangent intact.
