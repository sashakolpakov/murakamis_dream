# A limitation of the scalar half-face comparison

Research deduction, 7 November 2026. The complete half-cap and conditional
asymptotics identify an actual product action. A natural attempt to compare
it with the next ordinary reference combines a scalar cap ceiling, a real
conditional supporting tangent, and the existing radius-dependent action
floor. Those particular bounds do not prove the required inequality on
the whole containing type-four box. An explicit interior box point leaves
a positive deficit, even with the sharper cap ceiling.

The point is not asserted to lie on the actual following-reference image.
Nor is an upper envelope treated as a lower bound for a signed source.
This is a limitation of the proposed boxwise comparison, not a failure of
the original source estimate. No root, action, or saved certificate is
evaluated, and the frozen source theorems are unchanged.

## 1. The original selected comparison

Use the canonical ordinary-next reference and exact allocation in
[the selected-plateau theorem, equations (3)--(8)](research_mixed_next_filtered_selected_plateau.md).
The first three flags are \((0,1,\beta)\), \(\beta\in\{0,1\}\), and
\[
 (a_*,s_*,y_*,t_*,z_*)=(r_1,s_2^*,r_2,s_3^*,r_3).
 \tag{1}
\]
The external coordinate is \(c=s_4^*\in K_3\cup K_4\). The input
to the initial \(34\) half-chain is instead \(t_*\), and
\(y_*=q_{34}(t_*)\), as specified in
[the allocated-action theorem](research_mixed_next_allocated_action_floor.md).
These coordinates must not be interchanged.

Write \(P=[11/50,9/20]\), \(H=1/100\), and retain
\[
 y=x+iH,\quad x\in P,\quad Y=e^{-2\pi iy},\qquad
 z=v+i\Im z_*,\quad v\in P,\quad Z=e^{-2\pi iz}.
 \tag{2}
\]
At the incoming half face the literal density, before its integration
in the first incoming coordinate, is
\[
 U_{0,N}(w,-1)C_{1,N}(-1,Y)
                 d_N(Y)Y^{-N}C_{\beta,N}(Y,Z).
 \tag{3}
\]
Its outgoing modulus allocation is \(|d_N(Z)|^{\beta/2}\). No outgoing
factor is inserted when \(\beta=0\). The complete finite factors,
both Fourier alternatives, and the original integration densities remain
those of the source theorem; their polynomial powers do not change the
exponential comparisons below.

Let \(M_{\rm half}\) be the original complete-cap action, and let
\(\Theta(y)\) be the whole conditional critical action. The
[joint source theorem](research_mixed_half_face_joint_source_packet.md)
gives at complete color
\[
 U_{0,N}(-2,-1)C_{1,N}(-1,Y)
       =N^{-2}\mathcal D(1/2,-2,y)
           e^{N\{\mathcal T(1/2,-2)+\Theta(y)\}}
                 (1+O_{\rm hol}(N^{-1})),\qquad \mathcal D\ne0,
 \tag{4}
\]
where \(\Re\mathcal T(1/2,-2)=M_{\rm half}\).
This concerns the whole two-factor source, including all private and
conditional rows, aliases, and connecting currents.

For the actual reference put
\[
 \begin{split}
 A_*&=\Re\mathcal P_{34}(-2,y_*)+\tfrac12\nu(y_*),
       \qquad \nu(y)=-\Re g(y),\\
 a_0&=\Re y_*,\qquad
 p=\Re\{g'(s_*+y_*)-\tfrac32g'(y_*)\}.
 \end{split}
 \tag{5}
\]
These are the absolute action and marginal before the next transfer,
with the original halfweight. Let \(B_3(x,v)\) and
\(\Lambda_{123}(z)\) be the third-factor plane and the full outgoing
affine action from the same source. Their established comparison is
\[
 \begin{split}
 |C_{\beta,N}(Y,Z)|\,
 |d_N(Y)Y^{-N}|^{1/2}|d_N(Z)|^{\beta/2}
 &\le \operatorname{poly}(N)
       e^{N\{B_3(x,v)+7/250+\tau\}},\\
 A_*+p(x-a_0)+B_3(x,v)&\le\Lambda_{123}(z).
 \end{split}
 \tag{6}
\]
It retains the whole conditional polynomial and both Fourier alternatives.
The other selected halfweight has upper rate
\[
 h_{m sel}(x)=\tfrac12\max\{\nu(x+iH)-2\pi H,0\}.
 \tag{7}
\]
Consequently a sufficient strict comparison using (6) is
\[
 M_{\rm half}+\Re\Theta(x+iH)+h_{m sel}(x)+\frac7{250}
                  <A_*+p(x-a_0),\qquad x\in P.
 \tag{8}
\]
This states exactly the remaining scalar comparison within this method.
It neither identifies the outgoing coordinate \(z\) with \(y_*\)
nor divides through a possible zero of the outgoing Fourier weight.

## 2. The proposed conditional tangent and both weight alternatives

Here is a direct proof of the real tangent used in the comparison.
For real \(0<t,x<1/2\), set
\[
 q(t,x)=\Re Q(t;1/2,x),\qquad
 f(t,x)=q(t,x)-\tfrac12J(x),\qquad c_0=-J(1/4)>0,
 \tag{9}
\]
where \(Q\) is the original unmarked type-four conditional phase.
Put \(u=\cot\pi t>0\), \(v=\cot\pi x>0\), and
\(B=(uv-1)/(u+v)=\cot\pi(t+x)\). Its real Hessian is
\[
 \pi^{-1}q''=
 \begin{pmatrix}-1/u-3u+B&B\\B&B-v\end{pmatrix}.
 \tag{10}
\]
The first diagonal of its negative is positive because \(B<u\).
The determinant of that negative matrix equals
\[
 \frac{v^2/u+2uv^2+1/u+3u+v}{u+v}>0.
 \tag{11}
\]
Thus \(q\) is strictly concave on the full real square. The negative
Hessian of \(f\) adds the positive entry \(\pi v/2\) to its second
diagonal, so \(f\) is strictly concave too. At \(t=x=1/4\),
\[
 q=5c_0,\quad q_t=0,\quad q_x=\tfrac12\log2,
 \qquad f=\tfrac{11}{2}c_0,\quad f_x=\tfrac14\log2.
 \tag{12}
\]
Their supporting tangents give
\[
 \begin{split}
 q(t,x)&\le5c_0+\tfrac12\log2\,(x-1/4),\\
 f(t,x)&\le\tfrac{11}{2}c_0+\tfrac14\log2\,(x-1/4).
 \end{split}
 \tag{13}
\]

These real bounds also give legitimate upper estimates for the complex
conditional action on (2). First, the strict horizontal concavity and
vertical convexity in
[the complete conditional theorem, Lemma 2](research_mixed_half_face_complete_conditional_packet.md)
imply
\[
 \Re\Theta(x+iH)\le
          \max_{0<t<1/2}\Re Q(t;1/2,x+iH).
 \tag{14}
\]
Indeed, on its fixed retained interval the maximum over the real part
of \(t\) is a convex function of its height. At the critical height
its unique interior maximizer is the original critical point, and its
height derivative vanishes. This is its minimum; evaluating at height
zero proves (14).

For a real row the only change from \(x\) to \(x+iH\) is its exact
outgoing numerator integral. Its angles lie in \([.22,.95]\), and
their doubled-angle cosines are at most \(\cos(\pi/10)<24/25\).
For example \(\sqrt5<9/4\) gives
\(\cos^2(\pi/10)<29/32<(24/25)^2\).
The original bound \(R=e^{2\pi H}<175/164\) yields
\[
 \frac{1+R^{-1}}2>\frac{339}{350}>\frac{24}{25}.
\]
Hence, on each such angle,
\[
 |1-Re^{i\theta}|\le R|1-e^{i\theta}|.
 \tag{15}
\]
Squaring reduces this to
\((1-R)(1+R-2R\cos\theta)\le0\).
After integration, the radius cost is at most
\(t\log R\le\pi H\). The original incoming chirp is unchanged.

The selected halfweight bound in the selected-plateau proof is
\[
 h_{m sel}(x)\le
       \max\{-J(x)/2-3\pi H/4,0\}.
 \tag{16}
\]
Combining (13)--(16) with the cap ceiling
\[
 \widehat M=\frac{203}{200}-\frac{1303}{7680000},
             \qquad M_{\rm half}<\widehat M,
 \tag{17}
\]
from [the cap action theorem](research_mixed_half_face_cap_action_upper.md)
produces the two proposed costs, before subtracting the right side of
(8):
\[
 \begin{split}
 L_{m fac}(x)&=
   \widehat M+\tfrac{11}{2}c_0
      +\tfrac14\log2\,(x-1/4)+\frac{\pi H}{4}+\frac7{250},\\
 L_{m force}(x)&=
   \widehat M+5c_0
      +\tfrac12\log2\,(x-1/4)+\pi H+\frac7{250}.
 \end{split}
 \tag{18}
\]
Both alternatives are retained. These are upper envelopes, not asserted
values of the complete product or of either Fourier term.

## 3. An exact containing-box obstruction for those costs

For an actual reference, the available radial action floor is
\[
 \begin{split}
 A_*&>A_{m rad}(y_*):=\mathfrak C(R)+\tfrac12\nu(y_*),
           \qquad R=e^{2\pi\Im y_*},\\
 \mathfrak C(R)&=\frac{350711}{192000}
                 -\frac6{25}b(R)+\frac{b(R)^2}{20},\qquad
 b(R)=\frac12\log\frac2{1+R^2}.
 \end{split}
 \tag{19}
\]
The following-disk theorem proves this floor at its actual image, not
at a freely substituted canonical reference. We test the stronger
proposed simplification that would verify
\(L_{\rm fac}(x)<A_{m rad}(y)+p(x-\Re y)\) throughout the
containing type-four domain.

Take
\[
 y_\square=\frac3{10}-\frac{i}{10},\qquad
                    x_\square=\frac3{10},\qquad
                    R_\square=e^{-\pi/5}.
 \tag{20}
\]
This point is strictly inside
\[
 O_4=P_4\cap\{.24\le\Re y\le.36,\ -.102\le\Im y\le-.001\},
 \quad P_4=\{|y-(.30-.052i)|\le.060\}:
\]
its distance from the disk center is \(.048<.060\).
No assertion identifies (20) with an actual value \(q_{34}(t_*)\).
The marginal term vanishes at this test point for every real \(p\).

The positive exponential series and \(\pi>25/8\) show
\[
 e^{\pi/5}>1+\frac58+\frac{25}{128}
             =\frac{233}{128}>\frac{20}{11},
          \qquad R_\square<\frac{11}{20}.
 \tag{21}
\]
Therefore
\[
 b(R_\square)>\frac12\log\frac{800}{521}
       >\frac{279}{1321}>\frac{21}{100}.
 \tag{22}
\]
Here \(\log v>2(v-1)/(v+1)\) was used. The quadratic in (19)
decreases for \(0\le b\le(\log2)/2<7/20\). Since
\(350711/192000<1827/1000\), (22) gives
\[
 \mathfrak C(R_\square)
   <\frac{1827}{1000}-\frac{126}{2500}
                                     +\frac{441}{200000}.
 \tag{23}
\]

The original primitive identity in
[Fourier weight continuation, equation (22)](research_mixed_fourier_weight_continuation.md)
is
\(g(y)=[\operatorname{Li}_2(e^{-2\pi iy})-\pi^2/6]/(2\pi i)\).
For \(R<1\), its convergent series implies
\[
 \frac12\nu(y)\le\frac1{4\pi}\sum_{n\ge1}\frac{R^n}{n^2}
       \le\frac1{4\pi}\left(R+\frac{R^2}{4(1-R)}\right).
 \tag{24}
\]
Using (21) and \(\pi>25/8\), the last expression is less than
\(517/9000<23/400\). Adding (23) proves
\[
                  A_{m rad}(y_\square)
                         <\frac{367261}{200000}.
 \tag{25}
\]
This is an upper bound on the proposed lower-floor function, not on
the actual canonical action.

For the left side of the proposed comparison, the alternating Catalan
bound used in the half-face source theorem gives \(c_0>14/99\).
Also \(\log2>2/3\) and \(\pi>25/8\). Consequently (18), at (20),
gives
\[
 L_{m fac}(x_\square)>
 \frac{203}{200}-\frac{1303}{7680000}
          +\frac{77}{99}+\frac1{120}+\frac1{128}+\frac7{250}.
 \tag{26}
\]
Subtracting the right side of (25) from the right side of (26)
gives exactly
\[
                 \frac{568909}{1267200000}>\frac1{2500}.
 \tag{27}
\]
The final cross-product comparison is
\(568909>506880\). Thus
\[
 \boxed{\quad
 L_{m fac}(x_\square)
       -A_{m rad}(y_\square)>rac1{2500}.
 \quad}
 \tag{28}
\]
Already this one alternative prevents the proposed envelope comparison
from holding over the entire containing box. No mathematical quantity
in this deduction was numerically evaluated.

## 4. What the deduction does and does not rule out

Equation (28) rules out closing (8) by these particular scalar envelopes
and checking their sign on every point of the containing \(O_4\) box.
The other ordinary coordinates and their exact critical relations have
not been assigned at (20). It is therefore not an obstruction on the
actual canonical family, and it is not an upper bound on its true action.

There are two further independent losses in the proposed simplification:
\(\widehat M\) and the supporting tangent in (18) are upper bounds,
while (19) is only a lower bound for the genuine action. A positive
difference of these bounds says nothing about the sign of the difference
of the actual actions. The exact comparison (8) can still hold through
the correlated reference image, sharper conditional curvature or cap
bounds, a sharper original action floor, or a coupled source estimate.

The complete half-face asymptotics, the exact incoming nonstationarity,
and the remaining incoming contour obligations are unchanged. In
particular this note pays neither the original vertical connector nor
an entire Fourier sector, and it implies no knot-family conclusion.
