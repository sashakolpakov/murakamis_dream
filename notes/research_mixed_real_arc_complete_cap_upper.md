# A complete cap upper bound on the real incoming arc

Research deduction, 7 November 2026. The complete original
type-three cap has exponential upper rate strictly below
\[
              \widehat M=\frac{203}{200}-\frac{1303}{7680000}
\]
throughout \(1/2\le a\le7/10\). A fixed coherent contour
handles the initial part of the arc. The later part uses a
positive estimate of the individual private rows, with their
complete endpoint coefficients retained.

The proof includes rows beyond the incoming wall and both
parities. It does not infer a contraction of a signed sum
from a termwise multiplier, and does not continue the cap's
relative asymptotic throughout the arc. No numerical evaluation
is used.

## 1. The entire finite cap and its source bounds

Use the literal source
\[
 \begin{gathered}
 U_{0,N}(w,X)=\sum_{j=0}^{N-1}
             H_N(w,r^{-j})\,\frac{p_j(X)}{P_j},\\
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(X)=(rX;r)_j,\qquad X=e^{-2\pi ia}.
 \end{gathered}                                                   \tag{1}
\]
Every \(H_N\) is the complete original endpoint polynomial.
The ordinary color ranges over \([-2,2]\). Let
\[
 \lambda(e)=\Re S(e),\qquad h(e)=\lambda(e)+J(e),\qquad
 b_0=\frac{101}{125},\quad b_1=\frac{433}{500},\quad
                              B_0=b_1+\frac16=\frac{1549}{1500}.
                                                                    \tag{2}
\]
The source statements used below are the same ones traced in
[the coherent far-arc theorem, Sections 1--3](research_mixed_next_coherent_cap_far_arc.md)
and
[the wrapped-private theorem, Section 2](research_mixed_next_wrapped_private_sector.md):

* On compact physical private intervals, the complete \(H_N\)
  has rate \(h(e)\), uniformly at all real ordinary colors,
  with zero-safe numerator bounds and polynomial costs.
* The two true private ends have a separate positive row-sum
  ceiling \(3/5\) on \(|X|\le1\). They are not estimated by a
  compact-index asymptotic.
* Writing \(v=1-a\), the compact-row rate is
\[
 h(e)+B_v(e),\qquad
 B_v(e)=J(e-v)+J(v)-J(e).
                                                                    \tag{3}
\]
  The continuous primitive here is the original one-periodic
  real primitive. One has \(h(e)\le b_0\), and
  \(B_v(e)\le0\) when \(e\ge v\). Thus the complete wrapped
  private part has rate at most \(b_0\), including nonphysical
  incoming values and all numerator zeros.

For \(0<e<v\), (3) is the regular rate
\[
 \phi_a(e)=\lambda(e)+J(a+e)-J(a).                                \tag{4}
\]
The original concave-tangent bound
\(\lambda(e)<b_1\) is proved in
[the cap seam bounds, Section 2](research_mixed_cap_seam_source_bounds.md).
Consequently at the half face
\[
             \phi_{1/2}(e)\le b_1+\max J<B_0
                                  \qquad(0<e<1/2).              \tag{5}
\]
This is an upper bound on each coherent private row, before
the rows are summed.

The complete half-cap theorem defines its actual own action
\(M_{\rm half}\) and proves
\[
                  \frac{47}{50}<M_{\rm half}<\widehat M.
                                                                    \tag{6}
\]
The upper bound is
[the cap-action theorem](research_mixed_half_face_cap_action_upper.md);
its constants and original action normalization are unchanged.

## 2. Re-cutting the proved half-face contour

Use the same exact interpolation as the whole half-cap proof,
\[
 \mathscr A_N(e,a,w)=D_N(e)^{-1}C_N(e,w)
                         \frac{\Pi_N(a+e)}{\Pi_N(a)},\qquad
 \Psi(e,a)=S(e)+J(e+a)-J(a)-i\pi ea.                              \tag{7}
\]
The endpoint coefficient is the complete \(C_N\) on
\[
                   E_c=[.27,.49]+i[-.055,.04].
\]
Keep the lower private cut \(c_L=.27\), but replace its
upper cut by
\[
                              c_R=.43.                         \tag{8}
\]
The main private height remains the original half-face height
\(h_+=\Im e_+\). The two horizontal alias heights remain
\(-.055,.04\).

Here is the new real-cut comparison. The whole half-cap
theorem gives
\[
             .34<\Re e_+<.35,\qquad-.05<h_+<0,
\]
and, at \(a=1/2\),
\[
 -\Psi_{ee}(e)
   =\frac{2\pi}{\sin2\pi e}
       +\frac{2\pi}{\sin\pi e\sqrt{2-e^{-2\pi ie}}}.              \tag{9}
\]
Both terms have positive real part below height zero.
On the segment from \(e_+\) to \(c_R\), put
\[
 d_x=c_R-\Re e_+>\frac2{25},\quad d_y=-h_+<\frac1{20},
                           \rho=d_y/d_x<\frac58.
\]
At a point \(e=x+ih\) on that segment,
\[
 \frac{|\Im(1/\sin2\pi e)|}{\Re(1/\sin2\pi e)}
  <\frac{|h|}{1/2-x}
  \le\frac{|h_+|}{1/2-\Re e_+}<\frac13.                         \tag{10}
\]
For the middle inequality use
\(|h|=\rho(c_R-x)\) and \(c_R<1/2\).
The second term of (9) has imaginary-to-real ratio
less than \(8/31<1/3\), by the explicit argument bounds
in Section 3 of
[the complete half-cap theorem](research_mixed_half_face_complete_cap_packet.md).
Hence, writing \(\Psi_{ee}=-A+iB\), one has
\(A>0\) and \(|B|<A/3\) on this segment. Therefore
\[
 \Re\{\Psi_{ee}(d_x+id_y)^2\}
 <-A d_x^2\left(1-\frac23\frac58-\frac{25}{64}\right)
 =-\frac{37}{192}A d_x^2<0.                                    \tag{11}
\]
The original critical derivative at \(e_+\) is zero.
Twice integrating (11) proves
\[
                         \phi_{1/2}(c_R)<M_{\rm half}.          \tag{12}
\]
The once-integrated derivative also gives
\[
 \phi_{1/2}'(c_R)
  =\Re\int_0^1\Psi_{ee}(e_++s(d_x+id_y))(d_x+id_y)\,ds<0.
                                                                    \tag{13}
\]

At the unchanged lower cut, the old left-cone proof gives
\[
             \phi_{1/2}(c_L)<M_{\rm half},\qquad
                         \phi_{1/2}'(c_L)>0.                    \tag{14}
\]
For the derivative statement explicitly use its ratio
\(|B|<(8/31)A\), displacement \(d_x<0,d_y>0\), and
\(d_y/|d_x|<5/7\). The real part of the once-integrated
derivative is at least
\(\int A(|d_x|-(8/31)d_y)\,ds>0\).

On the entire real interval \((0,1/2)\),
\(\phi_{1/2}''<0\). This follows from the original endpoint
curvature
\[
 \lambda''(e)=-\pi\cot\pi e
     -\frac{2\pi}{\sin\pi e}
                     \Re\frac1{\sqrt{2-e^{-2\pi ie}}}<0
\]
and \(J''(e+1/2)=-\pi\tan\pi e<0\).
Thus (13)--(14) pay the complete compact real tails
\(e\le c_L\) and \(c_R\le e<1/2\), respectively.
The wrapped half at \(a=1/2\) has rate \(b_0<M_{\rm half}\);
the true ends retain their \(3/5\) bound.

The retained rectangle is a subrectangle of \(E_c\).
Its horizontal alias estimates are exactly the corresponding
restrictions of the proved whole half-cap estimates.
Private vertical convexity bounds the new cut's entire
sign-half alias sides by their real and horizontal endpoints.
It bounds each unweighted connector by its real endpoint
and its endpoint on the line through \(e_+\), which has a
strict horizontal gap. Equations (12)--(14) pay the new real
endpoints. The exact residue density remains \(+N\), and
every constant mode, both horizontal aliases, both vertical
alias sides and both main connectors are retained.

Consequently this re-cut complete source has the same
half-face upper rate \(M_{\rm half}\). The statement is
sourcewise: each of its retained currents and physical
tails has that upper rate. For all real ordinary colors,
the sourcewise coefficient bounds in the whole half-cap
proof apply unchanged; dropping their angular gain is
harmless. No subtraction from a signed whole-cap estimate
has been used.

## 3. The fixed coherent contour through \(a=14/25\)

Let
\[
                            \frac12\le a\le\frac{14}{25}.        \tag{15}
\]
On the retained rectangle \(c_L\le\Re e\le c_R\),
\(-.055\le\Im e\le.04\), all marked factorials remain regular:
\[
                         .77\le\Re(a+e)\le.99.
\]
The exact incoming phase derivative is
\[
 \Re\Psi_a(e,a)
  =\log\frac{|1-e^{-2\pi i(a+e)}|}
                    {|1-e^{-2\pi ia}|}.                        \tag{16}
\]
Set \(R=e^{2\pi\Im e}\). One has \(0<R<4/3\), since
\(2\pi/25<2/7<\log(4/3)\). The cosine of twice the real
angle \(a+e\) is positive on the interval just displayed.
Hence the numerator in (16) is less than
\(\sqrt{1+(4/3)^2}=5/3\).
Meanwhile
\[
 2\sin\pi a\ge2\cos(3\pi/50)>\frac{19}{10}.
\]
For the last inequality, \(3\pi/50<1/5\) and
\(\cos x\ge1-x^2/2\) even give \(2\cos(3\pi/50)>49/25\).
It follows that, on every point of every retained current,
\[
                \Re\Psi_a(e,a)<\log(50/57)<0.                  \tag{17}
\]
All alias penalties are independent of \(a\).
Thus every complete retained contour contribution has its
half-face upper rate decreased, with no change of contour
or endpoint-coefficient domain. Uniform factorial symbols
and the original all-real coefficient bounds supply only
polynomial factors and an arbitrary prescribed tolerance.

For the physical compact tails before the wall \(e<1-a\),
\[
 \partial_a\phi_a(e)
   =\log\frac{\sin\pi(a+e)}{\sin\pi a}\le0
                         \qquad(a\ge1/2).                      \tag{18}
\]
Every such row is therefore bounded by its already paid
half-face tail rate. Rows which have passed the wall keep
their independent rate \(b_0\) from (3), rather than being
transported through a zero. The true ends keep rate \(3/5\).
These statements include the new wall locations at
nonphysical incoming values.

We have proved a complete-cap upper rate \(M_{\rm half}\)
on (15), at every real ordinary color, with all original
rows and all finite currents.

## 4. Positive private-row bounds on the remaining arc

Now let \(14/25\le a\le7/10\). Keep wrapped rows and true
ends separate as above. For a regular prewall row, (18)
has the stronger bound
\[
 \begin{split}
 \partial_a\phi_a(e)
 &=\log\{\cos\pi e+\cot\pi a\,\sin\pi e\}\\
 &\le\log\cos\pi e\le-\frac{\pi^2e^2}{2}.
 \end{split}                                                     \tag{19}
\]
The logarithm's argument is positive because \(a+e<1\).
The last inequality follows by integrating
\(\tan x\ge x\).
Thus
\[
       \phi_a(e)\le\phi_{1/2}(e)
                         -\frac{\pi^2e^2}{2}(a-1/2).            \tag{20}
\]
This estimate is applied row by row to the original coherent
\(H_N\) factors. It is not applied to an already summed
oscillatory expression.

For \(e\le c_L\), (14) and real concavity give
\[
                      \phi_a(e)\le\phi_{1/2}(c_L)<M_{\rm half}.
                                                                    \tag{21}
\]
For \(e\ge c_L=27/100\), equations (5), (20) and
\(\pi>3\) give
\[
 \phi_a(e)
 <B_0-\frac92\left(\frac{27}{100}\right)^2\frac3{50}
 =B_0-\frac{19683}{1000000}<\frac{507}{500}.                      \tag{22}
\]
The last comparison is exact:
\(B_0-507/500=7/375\), and
\(19683/1000000>7/375\), with cross-product difference
\(381125>0\).
There is no issue at a numerator zero: the original
zero-safe rate bounds include it, and the wrapped sector
is already retained independently.

Finally
\[
                \widehat M-\frac{507}{500}
                                =\frac{6377}{7680000}>0.        \tag{23}
\]
Equations (6), (21)--(23), together with \(b_0\) and \(3/5\),
pay every row of the complete finite cap on this later arc.

## 5. Uniform complete-source conclusion and limitations

**Theorem.** There is a fixed number \(\delta>0\) such that,
for every \(\tau>0\), both level parities and all sufficiently
large \(N\),
\[
 \sup_{\substack{1/2\le a\le7/10\\-2\le w\le2}}
 |U_{0,N}(w,e^{-2\pi ia})|
 \le C_\tau N^{B_\tau}
                      e^{N(\widehat M-\delta+\tau)}.             \tag{24}
\]
For every fixed derivative order, the same exponential
upper rate is available with polynomial costs. On sufficiently
small fixed complex neighborhoods of the real incoming arc
and of the complete ordinary color, the bound holds with
an arbitrarily small additional prescribed rate tolerance,
and includes all fixed mixed derivatives on smaller neighborhoods.

Indeed one may choose \(\delta\) smaller than the positive
minimum of the gaps between \(\widehat M\) and
\[
                    M_{\rm half},\quad507/500,\quad b_0,\quad3/5.
\]
No value of this minimum is computed. The source decomposition
on (15) is the exact finite contour of Section 2; on the
remaining arc it is the literal positive private-row sum.
The zero-safe factorial and endpoint estimates are uniform,
so their polynomial costs are absorbed after fixing the
single tolerance. Ordinary derivatives on the whole real
interval follow from the original source bounds or Markov's
inequality applied to the full degree-\(O(N)\) polynomial.

For complex incoming continuation, keep the row sets and
contours fixed at each real base parameter. The retained
marked factorials in Section 3 have a fixed wall margin.
All physical-rate upper bounds in Section 4 are uniformly
continuous, including their moving numerator zeros, and
the two endpoint sectors retain their separate bounds.
For their incoming radius just outside the unit disk, the
polynomial degree at most \(N-1\) costs at most
\(\max(0,\log|X|)\) in the exponential rate; taking a
supremum for individual endpoint rows and then summing
adds only a polynomial factor. Thus this cost is arbitrarily
small on a fixed sufficiently thin incoming neighborhood.
The original small
ordinary-color estimates apply sourcewise. Compactness gives
a common fixed neighborhood after choosing the tolerance;
Cauchy's estimate then gives the stated mixed derivatives.
No moving row cutoff is differentiated.

Theorem (24) is a complete-source upper bound. It neither
asserts a nonzero whole-cap asymptotic away from its proved
local domains nor evaluates the original vertical incoming
connector. It can be multiplied by a separately established
whole conditional upper bound, but the resulting selected
comparison must retain the actual following-reference action
and all original weights. That comparison is not inferred
from (24) alone.

