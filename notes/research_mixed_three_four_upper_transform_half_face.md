# A paid upper-transform half face for the ordinary three/four pair

Research deduction, 7 November 2026. The raw upper transform
triangle of the terminal-four source is strictly smaller than the
actual coupled \((3,4)\) action at incoming real part \(1/2\).
This uses the already completed raw-half comparison at \(9/20\)
and an analytic transport with the complete first cap. No new
numerical evaluation or source replay is used.

The lower transform rows are not estimated here. Nor is a bound
for the first cap beyond real part \(1/2\) inferred.

## 1. Actual source and the existing initial comparison

Use the [original ordinary pair](research_mixed_three_four_ordinary_pair_target.md)
and its actual attached type-three leg
\[
 a_*=A+iH,\qquad .278<A<.391,\qquad -.072<H<.021.
 \tag{1}
\]
Its two bare actions are \(L=\mathcal T_0\) and
\(\Pi=\mathcal P_1\), with
\[
 L'(a_*)+\Pi'(a_*)=0,\qquad
 M=\Re\{L(a_*)+\Pi(a_*)\},\qquad \kappa=\frac1{2500000}.
 \tag{2}
\]
The first-cap plane through the entire interval
\([.22,.5]\), proved in
[upper-target completion](research_mixed_cap_upper_target_completion.md),
is
\[
 B_U(x)=\Re L(a_*)+\Re L'(a_*)(x-A)-\kappa(x-A)^2.
 \tag{3}
\]
It bounds the complete original \(U_{0,N}\), with any fixed
positive rate tolerance, polynomial prefactors and fixed ordinary
jets. The same source proves \(|\Re L'(a_*)|<1\).

Put \(R=e^{2\pi H}\) and
\[
 Q_{x,H}(t)=\int_0^t
       \log|R^{-1}-e^{-2\pi i(x+s)}|\,ds .
 \tag{4}
\]
This is the complete rate of \(X^{-i}p_i(X)\), including
its chirp, at \(X=e^{-2\pi i(x+iH)},\ t=i/N\).
Let \(M_4(1/2)\) be the real private/Newton entropy maximum
of [the terminal-four right-triangle theorem](research_mixed_terminal_four_right_triangle.md),
equations (6)--(7). Its full physical triple-row rate obeys
\[
 R_1(x+iH;t,e,u)
 \le M_4(1/2)+Q_{x,H}(1/2)
                -\log(80/63)(t-1/2),\qquad t\ge1/2 .
 \tag{5}
\]
All actual support walls and numerator zeros are retained.

The raw-half family of
[whole terminal-four completion](research_mixed_terminal_four_full_completion.md),
Condition C, has been discharged on this actual reference family
by [the whole plateau theorem](research_mixed_full_unselected_plateau.md),
Section 1. In particular, at \(x_0=9/20\),
\[
\begin{split}
 M_4(1/2)+Q_{x_0,H}(1/2)
 &\le B_V(x_0)-\frac1{20000},\\
 B_V(x)&=\Re\Pi(a_*)+\Re\Pi'(a_*)(x-A)-\kappa(x-A)^2 .
\end{split}
 \tag{6}
\]
The global entropy maximizer lies inside the raw comparison's
original private ranges. Thus (6) is the existing absolute
upper-triangle comparison, not an inference from a bound for
the coherent modulus of \(V_{1,N}\).

## 2. A uniform transport of the coupled half face

**Lemma 1.** On the actual height range (1), for
\(9/20\le x\le1/2\),
\[
 \partial_xQ_{x,H}(1/2)<-\log3<-\frac{13}{12}.
 \tag{7}
\]

*Proof.* The elementary exponential bounds give
\[
                         \frac35<R<\frac76.
 \tag{8}
\]
Indeed \(.144\pi<1/2\), and
\(e^{1/2}<1+1/2+(1/2)^2/[2(1-(1/2)/3)]
 =33/20<5/3\).
Also \(.042\pi<7/50\), so
\(R<e^{7/50}<1/(1-7/50)=50/43<7/6\).

The function \(R+R^{-1}\) is convex. Its maximum on
\([3/5,7/6]\) is at an endpoint, so
\[
              u_R=\frac{(R-1)^2}{4R}\le\frac1{15}.
\]
For \(x\) in the stated interval,
\[
 \cos^2\pi x\le\sin^2(\pi/20)<\frac{121}{4900},
 \qquad \sin^2\pi x>\frac{4779}{4900}.
 \tag{9}
\]
Differentiation of the integral, or its absolutely continuous
primitive at a logarithmic endpoint, gives
\[
 \exp\{2\partial_xQ_{x,H}(1/2)\}
 =\frac{|1+Re^{-2\pi ix}|^2}{|1-Re^{-2\pi ix}|^2}
 =\frac{u_R+\cos^2\pi x}{u_R+\sin^2\pi x}
 <\frac{1/15+121/4900}{1/15+4779/4900}<\frac19.
 \tag{10}
\]
The quotient increases with \(u_R\) because
\(\cos^2\pi x<\sin^2\pi x\). The last rational comparison
is equivalent to \(8/15<3690/4900\).
If \(R=1,x=1/2\), the derivative is \(-\infty\);
the integrated assertion follows by continuity.
Finally
\(\log3=2\operatorname{atanh}(1/2)>
2(1/2+(1/2)^3/3)=13/12\).
\(\square\)

Define the coupled half-face majorant
\[
                    E(x)=B_U(x)+M_4(1/2)+Q_{x,H}(1/2).
 \tag{11}
\]
Since \(x>A\), equation (3) gives \(B_U'(x)<1\).
Lemma 1 therefore yields \(E'(x)<-1/12\) almost everywhere.
Equations (2) and (6) give
\[
 E(9/20)\le M-2\kappa(9/20-A)^2-\frac1{20000}.
\]
Integration to \(1/2\), including any logarithmic endpoint,
proves
\[
              E(1/2)<M-\frac1{20000}-\frac1{240}
                          <M-\frac1{250}.
 \tag{12}
\]
The coupled decrease keeps the original cap marginal;
its sign has not been discarded.

## 3. The corresponding finite source sector

Let \(\mathfrak V_{1,N}^{\ge1/2}(w,X)\) be the sum of the
absolute values of the original triple summands (3) in the
right-triangle theorem, restricted to \(i/N\ge1/2\).
It includes the complete private/Newton support of each such
row. The original zero-safe product and Newton bounds, (5),
and the complete first-cap plane imply, at
\(X=e^{-2\pi i(1/2+iH)}\),
\[
 |U_{0,N}(w_L,X)|\,
       \mathfrak V_{1,N}^{\ge1/2}(w_R,X)
       \le C N^b e^{N(M-1/500)}
 \tag{13}
\]
on sufficiently small fixed ordinary-color disks about \(-2\),
for all large \(N\) of either parity. Choose one total source
and color tolerance below \(1/500\) in the raw gap (12).
The polynomial number of rows and all endpoint prefactors
are absorbed in \(N^b\). For fixed ordinary derivatives, use
the same individual polynomial Cauchy estimates before forming
the positive majorant. The even row \(i=N/2\) is included;
at odd levels all indices satisfying \(i/N\ge1/2\) are retained.

The [radius comparison](research_mixed_incoming_half_circle_radius_comparison.md)
also gives
\(Q_{x,H}(1/2)\le Q_{1/2,H}(1/2)\) for
\(1/2\le x\le1\). Hence the terminal majorant alone has
the same half-face ceiling throughout that incoming semicircle.
Equation (13) includes the first cap only at \(x=1/2\);
no corresponding whole-circle first-cap estimate is asserted.

In particular (13) removes the upper transform triangle from
the remaining half-face test. The coherent inner-cap coefficients
of the lower transform rows, their absolute outer sum, and the
complete coupled contour away from this face remain separate.
No nonzero whole-pair packet or new knot-family theorem follows
from this sector bound alone.
