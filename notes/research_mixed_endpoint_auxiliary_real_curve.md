# The complete endpoint source on an auxiliary-real curve

Research deduction, 8 November 2026. An explicit complex private-index
curve joins real part \(1/8\) to the previously proved later incoming
point. Its original auxiliary critical point is real. An exact
factorization of the physical row force pays all lower-half rows,
including the revived rows past the private endpoint. Separate
upper-half estimates then give the complete endpoint asymptotic on a
fixed neighborhood of this whole curve.

This is a theorem about the specified complete endpoint coefficient.
It does not compare the outer-cap action on the new curve with the
outer critical action, or pay a whole outer-cap contour. No numerical
evaluation is used and earlier frozen notes are unchanged.

## 1. Original source and the explicit curve

Keep exactly the finite continuation in
[the complex-index theorem](research_complete_boundary_complex_index.md):
\[
 C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\qquad
 S_l=\prod_{j=1}^{l}2\sin(\pi j/N).
 \tag{1}
\]
The canonical sine factorial and ordinary Newton polynomials are
unchanged. In particular no row is removed when \(e\) leaves the
physical grid. At complete color use the original phase
\[
 F(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,
 \qquad J'(q)=\Log(2\sin\pi q).
 \tag{2}
\]

For a real parameter \(t\), define
\[
 \begin{gathered}
 t_-=(\sqrt3-1)/2,\qquad t_+=1/\sqrt2,\qquad t_-\le t\le t_+,\\
 T=t^2,\quad p(t)=1-2t^2+2it,\quad
 e(t)=\frac{\Log p(t)}{2\pi i}=E(t)-i\eta(t),\quad
 u_0(t)=\frac{\arctan t}{\pi},\quad
 \omega(t)=e^{2\pi iu_0(t)}=\frac{1+it}{1-it}.
 \end{gathered}                                                   \tag{3}
\]
Here \(\Log p\) has argument in \([\pi/4,\pi/2]\). In fact
\[
 \frac{d}{dt}\arg p(t)=\frac{2(1+2t^2)}{1+4t^4}>0,
 \qquad |p(t)|^2=1+4t^4.
 \tag{4}
\]
Thus \(E\) increases from \(1/8\) to \(1/4\), \(\eta>0\), and
\[
 0<\eta(t)\le\frac{\log2}{4\pi}<\frac3{50}.
 \tag{5}
\]
The last inequality follows from \(\log2<7/10\) and \(\pi>3\).
The endpoint depth is exactly the one in the later-point theorem;
it is not replaced by a smaller decimal cutoff.

The elementary identities
\[
 p=\frac{5\omega^2-2\omega+1}{(\omega+1)^2},\qquad
 \frac p\omega=
     \frac{1+t^2+2t^4+2it^3}{1+t^2}
 \tag{6}
\]
give \(0<u_0<E<1/2\). Indeed both \(p,\omega\) are in the
upper half-plane, their arguments lie in \((0,\pi/2]\), and
the second expression in (6) has positive real and imaginary
parts. Directly from the original logarithms,
\[
 e^{F_u(e,u_0)}
  =e^{i\pi e}\sin\pi(e-u_0)
                     \frac{\cos^2\pi u_0}{\sin^3\pi u_0}=1.
 \tag{7}
\]
To see the last equality without changing a branch, use
\(p(1-it)-(1+it)=2it^3\). Since \(0<E-u_0<1/2\),
\(\Arg\sin\pi(e-u_0)\in(-\pi/2,0)\), and hence the imaginary
part of \(F_u\) in (7) lies in \((-\pi/2,\pi/4)\). Its lift is
therefore zero. On every real segment \(0<u<E\),
\[
 -\Re F_{uu}(e,u)
 =\pi\Re\{2\tan\pi u+3\cot\pi u+\cot\pi(e-u)\}>0.
 \tag{8}
\]
This gives a simple original critical point. At \(t=t_+\), (3)
is exactly \(e_0=1/4-i\log2/(4\pi)\) and its original root
from [the later-point theorem](research_mixed_endpoint_later_incoming_point.md).
Continuation along the connected curve therefore fixes the same
endpoint branch and action \(S(e)=F(e,u_c(e))\), with \(u_c(e(t))=u_0(t)\).

**Theorem.** On a fixed open complex neighborhood of
\[
             \{(e(t),-2):t_-\le t\le t_+\},
 \tag{9}
\]
the whole finite source (1) has
\[
 C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}
                  (1+O_{\rm hol}(N^{-1})),\qquad A(e,w)\ne0.
 \tag{10}
\]
Both level parities and all fixed joint ordinary-color/index
derivatives of the normalized error are included on smaller
neighborhoods. The phase, coefficient, and Gaussian square root
are the original endpoint ones; no scalar is inserted or removed.

## 2. Exact monotonicity through every revived lower-half row

The zero-safe bound for every summand in (1) is the original rate
\[
 \begin{split}
 \mathcal V(x)&=2\int_0^x\log(2|\cos\pi s|)\,ds-2J(x),\\
 R(e,x)&=\mathcal V(x)-J(x)-\Re J_{\rm side}(e-x)+\pi\eta x.
 \end{split}                                                     \tag{11}
\]
The reflected primitive, polynomial factors, and reciprocal zeros
are exactly those proved in Sections 3--4 of the complex-index
theorem. The carrier \(+\pi\eta x\) remains present. Uniformly
through \(x=0,1\), the physical Newton zero and both parities,
each fixed ordinary-color derivative is bounded by a polynomial
times \(e^{NR(e,l/N)}\).

For \(0<x<1/2\), the same original derivative on both sides
of the reciprocal wall is
\[
 e^{R_x(e,x)}=e^{\pi\eta}
     \frac{|\sin\pi(e-x)|\cos^2\pi x}{\sin^3\pi x}.
 \tag{12}
\]
Here \(\eta>0\), so there is no logarithmic zero on this real
interval. Put \(z=\cot\pi x\) and \(y=tz\). Writing
\(K=\sinh\pi\eta\), the identities \(|p|=e^{2\pi\eta}\) and
(3) give
\[
 \begin{split}
 |p|(\sin^2\pi E+K^2)&=T(1+T),\\
 |p|(\cos^2\pi E+K^2)&=1-T+T^2,\\
 |p|\sin2\pi E&=2t.
 \end{split}                                                     \tag{13}
\]
Consequently the force has the exact factorization
\[
 \begin{split}
 e^{2R_x}-1&=\frac{(y-1)Q_T(y)}{T^2},\\
 Q_T(y)&=(1+T)y^5+(T-1)y^4+T^2(1+y+y^2+y^3).
 \end{split}                                                     \tag{14}
\]

We prove \(Q_T(y)>0\) for every \(y\ge0\) in the present range.
First \(T\ge1-\sqrt3/2>2/15\), since \(\sqrt3<26/15\).
For \(y\ge0\),
\[
 \partial_TQ_T(y)=y^5+y^4+2T(1+y+y^2+y^3)>0.
\]
At \(T=2/15\),
\[
 225Q_{2/15}(y)=255y^5-195y^4+4(1+y+y^2+y^3).
 \tag{15}
\]
For \(y\ge13/17\) the first two terms already have nonnegative
sum. For \(0\le y\le2/5\), the function
\(m(y)=y^4(195-255y)\) increases, and
\(m(y)\le1488/625<4\). On the intervening interval,
its global maximum is at \(y=52/85\), giving
\[
 m(y)\le39(52/85)^4<39(5/8)^4
       =24375/4096<156/25.
\]
There \(4(1+y+y^2+y^3)\ge4(1+2/5+4/25)=156/25\).
This proves the claimed positivity, without a root evaluation.

Since \(t\cot\pi x\) decreases strictly and equals one exactly
at \(x=u_0(t)\), (14) proves
\[
 R_x(e,x)>0\ (0<x<u_0),\qquad
 R_x(e,x)<0\ (u_0<x<1/2).
 \tag{16}
\]
Thus the entire lower-half row profile has its unique maximum
at the original saddle, and
\(R(e,u_0)=\Re S(e)\). This includes every revived row \(x>E\);
no physical termination has been imported off the grid.

## 3. The upper half is strictly smaller

The exact reflected identity underlying the later-point and
[bridge-tail theorem](research_mixed_endpoint_bridge_real_tails.md)
holds for every \(0<E<1/2\) before any monotonicity estimate is
applied. With \(v=1-x\in[0,1/2]\), it is
\[
 R(e,1-v)=2J(1/2-v)+3J(v)-\Re J(e+v)
                              +\pi\eta+\pi(1-v)\eta.
 \tag{17}
\]
The first two terms are nonpositive. Here \(E+v\in[1/8,3/4]\).
On that interval the sine argument has absolute value at most
\(\pi/2\), so vertical integration and the elementary global
\(-J(s)<1/6\) give
\[
                  R(e,x)<1/6+5\pi\eta/2\quad(1/2\le x\le1).
 \tag{18}
\]
This avoids using the bridge-tail theorem's later restriction
\(E>1/6\) for its stronger comparison with \(J(e)\).

For lower bounds on the actual maximum, evaluate its full real
profile at \(x=E\). The right-hand boundary branch has
\(\Re J(-i\eta)=-\pi\eta/2\); hence (16) gives
\[
 \Re S(e)>R(e,E)
   =-2J(1/2-E)-3J(E)+\pi\eta(1/2+E)
   >-2J(1/2-E)-3J(E).
 \tag{19}
\]

If \(1/8\le E\le1/6\), monotonicity of \(J\) gives
\[
 -J(E)\ge-J(1/8)>1/8,\qquad
 -J(1/2-E)\ge-J(3/8)>1/16.
\]
The first strict inequality follows by integrating
\(\log(2\sin\pi s)\le\log(2\pi s)\) and using \(\pi/4<1\).
For the second, \(2\sin(3\pi/8)>\sqrt3\) and \(\log3>1\)
give the bound by integration on \([3/8,1/2]\). Thus
\(\Re S>1/2\). From the equation \(\Re p=1-2t^2\), the
radius at \(E=1/6\) is \(4/(1+\sqrt7)<10/9\). Both \(E\)
and the radius increase with \(t\). Equation (18) therefore gives
\[
 R(e,x)<1/6+(5/4)\log(10/9)<11/36<1/2
 \quad(E\le1/6,\ x\ge1/2).
 \tag{20}
\]

If \(1/6\le E\le1/4\), the original Catalan-series witness
in [the fixed-cut calculation, equations (11)--(12)](research_mixed_next_half_face_fixed_cut_obstruction.md)
gives \(-J(1/4)>14/99\). Also
\[
 -J(1/3)>\frac1{12}\{\log\sqrt3+\log2\}>\frac1{10}.
 \tag{21}
\]
Indeed \(\log(2\sin\pi s)\) is strictly concave; its integral
on \([1/3,1/2]\) exceeds the endpoint trapezoid in (21).
The elementary logarithmic inequalities
\(\log2>2/3,\ \log3>13/12\), obtained from the positive
\(2\operatorname{atanh}\) series, make that trapezoid greater
than \(29/288>1/10\). By monotonicity of \(J\), (19) yields
\[
 \Re S(e)>3(14/99)+2/10=103/165.
 \tag{22}
\]
Meanwhile (18), \(\eta\le\log2/(4\pi)\), and \(\log2<7/10\)
give the upper-half ceiling \(29/48\). In particular
\[
 \Re S(e)-R(e,x)>103/165-29/48=53/2640>0
 \quad(E\ge1/6,\ x\ge1/2).
 \tag{23}
\]
Equations (20) and (23) pay the entire original upper half.

## 4. Fixed finite cuts, both aliases, and the complete Gaussian

At a base parameter \(t\) set
\[
 \alpha(t)=u_0(t)/2,\qquad \beta(t)=(u_0(t)+E(t))/2,
 \quad L_N=\lceil N\alpha\rceil,\quad M_N=\lceil N\beta\rceil,
 \quad \alpha_N=(L_N-1/2)/N,\quad\beta_N=(M_N-1/2)/N.
 \tag{24}
\]
The strict separations \(0<\alpha<u_0<\beta<E<1/2\) are
uniform on the compact parameter interval (3). By (16), all
lower rows \(l<L_N\) reduce to the first real cut, and all
upper rows \(M_N\le l<N/2\) reduce to the second. Both cuts
have a strict own-action gap. Equations (20)--(23) pay every
remaining row. Continuity and compactness give a common positive
gap; the half-grid shifts cost only the original polynomial
factorial errors and an arbitrarily small fixed allowance.

For the retained indices use the exact ordinary Newton
interpolant \(\mathcal E_N(u,w)\) from
[the original coefficient proof, equations (8)--(12)](research_complete_boundary_coefficient_asymptotic.md).
The exact row is
\[
 f_N(e,u,w)=
     \frac{e^{i\pi Neu}\mathcal E_N(u,w)}
                {G_N(Nu)G_N(N(e-u))}.
 \tag{25}
\]
It has the original physical values and is jointly holomorphic
on a fixed small rectangle around \([\alpha,\beta]\), uniformly
along the compact curve. All its primitive real parts remain in
the regular strips. At \(w=-2\), its full symbol is
\[
 f_N=N^{-2}
   \frac{e^{NF(e,u)}}
   {(2\sin\pi u)^{3/2}(2\sin\pi(e-u))^{1/2}}
                      (1+O_{\rm hol}(N^{-1})).
 \tag{26}
\]

On the retained real segment the original imaginary derivative is
\[
 \Im F_u(e,x)=\Arg\sin\pi(e-x)+\pi E
                                  \in(-\pi/2,\pi/4).
 \tag{27}
\]
Choose a fixed small \(h_1>0\) so that on every corresponding
rectangle with heights \(\pm h_1\), one has
\(|\Im F_u|<\pi\), and the two complete cut sides retain a
fixed part of their real cut gaps. The compact strict separations
in (24) allow one common choice. The \(O(N^{-1})\) cut shifts
preserve these properties for large \(N\).

Apply the original exact cotangent residue identity to (25).
Its residues are exactly the rows \(L_N\le l<M_N\), with
density \(+N\). Both horizontal aliases have their exact loss
\(2\pi h_1\), so (16) and (27) bound each by
\[
       \Re F(e,x\pm ih_1)-2\pi h_1
                              \le\Re S(e)-\pi h_1.
 \tag{28}
\]
Both whole vertical sides, including their upper and lower
cotangent remainders, lie on the paid cut sides. The half-grid
kernels are bounded there. Splitting off the constant modes
retains the original two orientations; their paths may be brought
to the real segment with both unweighted cut joins retained.
Those joins are paid by the same cut-side bound. Thus all four
vertical half-sides, both horizontal aliases, and both unweighted
joins are included.

The remaining constant mode is \(N\int_{\alpha_N}^{\beta_N}f_N\,du\).
It has the original real saddle \(u_0\), the unique nondegenerate
maximum by (8) and (16). Its nonzero leading coefficient is
\[
 A(e,-2)=
 \frac{\sqrt{2\pi}}{\sqrt{-F_{uu}(e,u_0)}}
 \frac1{(2\sin\pi u_0)^{3/2}(2\sin\pi(e-u_0))^{1/2}},
 \tag{29}
\]
with the original accretive square root. The powers are precisely
\(N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}\). The first odd Gaussian
correction vanishes. All other source groups have a fixed
exponential gap, proving (10) on the curve.

For complex continuation, fix the base cuts, integer row sets,
alias rectangle and main path before varying \(e,w\). The
discarded rows obey the same zero-safe original upper estimates,
including every reciprocal zero and the odd Newton zero. The
ordinary-color estimate from the full-index theorem changes their
rate by at most \(C\sqrt{|w+2|}\), so preserves the gaps on a fixed
small color disk. The local critical point and nonzero symbol
continue inside the regular retained chart; its short contour
adjustment and all existing cut joins keep their strict gaps.
This gives the holomorphic relative error on a fixed neighborhood
of each base point. A finite cover gives (9)--(10) uniformly,
and Cauchy's formula on smaller neighborhoods gives every fixed
mixed derivative. No derivative of the cuts in (24) is asserted.

## 5. What this adds to the outer-contour problem

The curve (3) is an explicit whole-source route from private
real part \(1/8\) to the exact later cap point. At its left
endpoint, (20) gives
\(\eta<1/(18\pi)<1/54<11/200\), within the depth of the
[proved lower private side](research_mixed_next_lower_private_cut_source.md).
At its right endpoint it overlaps the later-point packet, hence
the already proved actual cap-path packet. It does not merely
invoke holomorphy between these sets: Sections 2--4 pay every
original auxiliary row and contour current.

To use this route as an outer private contour, its original outer
factor and carrier must still be included and its outer phase must
be compared with the actual cap action along the connecting curve
and all remaining outer joins. This note proves no such comparison,
no whole outer-cap asymptotic, and no filled-source conclusion.
