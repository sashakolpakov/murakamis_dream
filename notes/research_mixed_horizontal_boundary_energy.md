# Explicit energy for the remaining real boundary displacement

Research deduction, 5 November 2026. The horizontal completion after
the first collar leaves a single real force. The ordinary pair form
gives a stronger way to pay that force than a constant Hessian bound:
retain the first coordinate's actual logarithmic factorial curvature.
The resulting one-variable maximum has an explicit clipped critical
point. The complete finite-source hypotheses remain necessary.

## 1. The comparison domain and the first wire

Use the source-admissible horizontal domain \(\mathcal D\), fixed
cut \(h\), action \(\Psi_h\), and force \(p=\Re P_2\) from
[the horizontal completion reduction](research_mixed_first_collar_horizontal_completion.md).
Write the actual second reference as \(a+ic\), and let its type
be \(3+\beta\), where \(\beta\in\{0,1\}\). Put
\[
 \lambda=1+\beta/2,\qquad y_2=a+d_2,
 \qquad \widehat z_2=y_2+ic.
 \tag{1}
\]
Write \(y^0=(a_2,\ldots,a_{h-1})\) for the vector of reference
real coordinates, so the scalar \(a\) is \(a_2\).
All heights in the horizontal comparison stay fixed. In particular
this is the comparison before transporting the second height back
to its physical collar value.

In addition to the complete-source conditions of the cited reduction,
require along every admitted horizontal segment
\[
              \Re(s_3+\widehat z_2)\ge1/2,
 \tag{2}
\]
where \(s_3\) is the original conditional index for edge three.
The three arguments remain in the common rectangle \(Q\) of that
reduction. For an ordinary third block, condition (2) holds throughout
the original reduced-disk conditional images: the
[first-wire extraction](research_mixed_reduced_disk_pair_sums.md)
proves the stronger lower bound \(109/200\), in both orientations.
This does not extend the source image to an independent rectangle.
For a terminal third block, require (2) separately unless it is
already supplied by an applicable endpoint-image estimate.

## 2. The retained diagonal survives complex elimination

Write \(C(z)=\Re\cot\pi z\). Before eliminating the index \(s\),
the allocated conditional action has \(J\)-part
\[
 V(s,A)+V(s,B)-\epsilon J(s)
                   -\frac\beta2J(A)-\frac\epsilon2J(B),
 \quad V(u,v)=J(u+v)-J(u)-J(v).
 \tag{3}
\]
Its remaining polynomial has purely imaginary Hessian. If
\(\Re(s+A)\ge1/2\), the pair form is
\[
 -\Re V''(s,A)
 =\pi C(s)|ds|^2+\pi C(A)|dA|^2
                     -\pi C(s+A)|ds+dA|^2.
 \tag{4}
\]
Here \(C(s),C(A)>0\), and \(C(s+A)\le0\), since the real
sum is also less than one. The other pair retains the previously
proved bound \(-\Re V''(s,B)\succ(\pi/8)I\).
Consequently the Hermitian real part of the full negative Hessian
is bounded below by
\[
 \lambda\pi C(A)|dA|^2+\frac\pi8|dB|^2
                          +\pi\{C(s)+1/8\}|ds|^2.
 \tag{5}
\]
The own-type terms omitted from the right side are nonnegative.

For completeness, this diagonal bound survives the *complex* Schur
complement. Given a retained displacement \((dA,dB)\), choose
\(ds\) to solve the eliminated linear equation for the full
complex negative Hessian. Its first matrix component then vanishes.
Pairing with the conjugate displacement identifies the remaining
quadratic form with the Schur form. Taking real parts in (5) and
discarding the nonnegative \(|ds|^2\) term proves
\[
 -\Re\phi_{\beta\epsilon}''
 \succeq\operatorname{diag}\{\lambda\pi C(A),\pi/8\}.
 \tag{6}
\]
No replacement of a complex Schur complement by the Schur complement
of its real part is being made.

In the post-pair chain, edge three supplies (6), and every subsequent
edge retains the ordinary \(\pi/8\) lower bound. Thus
\[
 -D_y^2\Re\Psi_h(y)
 \succeq\operatorname{diag}
       \{\lambda\pi C(y_2+ic),\pi/8,\ldots,\pi/8\}.
 \tag{7}
\]
The fixed cut contributes no displacement. This estimate is
independent of the number of later coordinates.

## 3. The explicit one-variable energy

Define the real function and its increment above its tangent by
\[
 \begin{split}
 G_c(y)&=\Re g(y+ic),\\
 B_c(y,a)&=G_c(y)-G_c(a)-G_c'(a)(y-a).
 \end{split}
 \tag{8}
\]
On \(0<y<1/2\),
\(G_c''(y)=\pi C(y+ic)>0\). In particular \(B_c\ge0\).
Integrate (7) along the actual horizontal segment, retaining the
reference gradient \((-p,0,\ldots,0)\). This gives
\[
 \Re\{\Psi_h(y^0+d)-\Psi_h(y^0)\}
 \le-pd_2-\lambda B_c(a+d_2,a)
                   -\frac\pi{16}\sum_{j=3}^{h-1}d_j^2.
 \tag{9}
\]
Equivalently, the exact completion energy \(V_h\)
of the cited reduction satisfies
\[
                         V_h(t)\ge\lambda B_c(a+t,a).
 \tag{10}
\]

Let \(I=[l,u]\Subset(0,1/2)\) contain the projection of the
admitted horizontal domain onto coordinate two. The following explicit
criterion is therefore sufficient for a strict first-collar loss:
\[
 \mathcal W(p;a,c,I):=
 \max_{y\in I}\{-p(y-a)-\lambda B_c(y,a)\}<\delta,
 \tag{11}
\]
where \(\delta\) is the appropriate unrounded reserve from the
horizontal completion theorem. Once (11) holds, choose the one total
finite-source tolerance smaller than \(\delta-\mathcal W\).
All admitted later coordinates are already paid for in (9); they
are not charged again against this reserve.

The interval \(I\) may be a relaxation of the actual projection.
Its use in the scalar maximum does not assert that finite-source
estimates hold at every independently chosen tuple in \(I\).
Those estimates are required only on the original domain
\(\mathcal D\).

## 4. The maximizer is given by one algebraic equation

Set
\[
 R=e^{2\pi c},\qquad
 D_a^2=|1-Re^{-2\pi ia}|^2,
 \qquad T=D_a^2e^{-2p/\lambda}.
 \tag{12}
\]
The branch of \(g'\) does not affect its real part, and
\[
 G_c'(y)=\log|1-Re^{-2\pi iy}|,
 \quad |1-Re^{-2\pi iy}|^2=1+R^2-2R\cos(2\pi y).
 \tag{13}
\]
The latter expression is strictly increasing on \((0,1/2)\).
The function maximized in (11) is strictly concave. Its unique
maximizer \(y_*\) is consequently obtained as follows:
\[
 y_*=
 \begin{cases}
 l,&T\le1+R^2-2R\cos(2\pi l),\\
 u,&T\ge1+R^2-2R\cos(2\pi u),\\
 \displaystyle\frac1{2\pi}
       \arccos\frac{1+R^2-T}{2R},&\text{otherwise}.
 \end{cases}
 \tag{14}
\]
Thus (11) requires evaluation at just this point, with no optimization
over the other coordinates and no search over word lengths. The
criterion still involves the true force \(p\), the reference
height, and the unchanged action increment (8). Their signs or sizes
have not been assumed favorable.

If the exponentiated marked parameters and \(e^{2p}\) are
algebraic, the right side of the cosine equation in (14) is algebraic:
\(\lambda\) is rational and all roots in (12) are the positive
real ones. This locates the candidate by algebraic data. It does not
make the action comparison (11) automatic.

For a second type-four coordinate, an even simpler sufficient test
uses an existing scalar bound. For this test take
\(I\subset[.24,.363]\), with \(-.102\le c\le0\).
The
[fixed-contour theorem](research_mixed_four_fixed_contour_transport.md)
proves \(C(y+ic)>1/3\) on the required second-four real and
height intervals. With \(\lambda=3/2\), (9) then contains
\((\pi/4)d_2^2\). Hence
\[
                  \mathcal W(p;a,c,I)\le p^2/\pi.
 \tag{15}
\]
The earlier constant-Hessian estimate was \(4p^2/\pi\).
No assertion that either quantity is always below \(\delta\)
is made here. The nonquadratic test (11)--(14) retains more information
and can be strictly better than either constant bound.

This deduction removes the need to estimate the entire horizontal
completion afresh once its source domain and first-wire sign are
known. It does not establish that domain, pay the boundary force in
every actual geometry, or prove the remaining open-source theorem.
