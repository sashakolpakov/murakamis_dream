# A stronger lower bound for the action before the next transfer

Research deduction, 7 November 2026. The existing complete
following-family comparison contains a stronger action bound than
the constant \(7/4\) used in several later estimates. Combining its
radius-dependent bound with the original Fourier halfweight gives
an allocated action strictly greater than \(9/5\). This permits a
larger polynomial bound in the selected-contour comparison.

All scalar comparisons below are written inequalities. No new
critical point, action, or saved certificate is evaluated. The
result does not bound the remaining full prefix.

## 1. The original reference and its radial comparison

Use the ordinary-next family of
[the selected-plateau theorem, equations (3)--(8)](research_mixed_next_filtered_selected_plateau.md).
Its first three flags are \((0,1,\beta)\), where
\(\beta\in\{0,1\}\). The external coordinate \(c=s_4^*\) lies in
\(K_3\cup K_4\), and the retained type-four reference is \(y_*=r_2\).
For the initial \(34\) half-chain, the following input is instead
\(t_*=s_3^*\). The domain definitions in
[the first-type-three extension, equation (4)](research_mixed_second_selected_first_three_extension.md)
give \(t_*\in O_{3+\beta}\subset P_{3+\beta}\). The original
critical equations and their unique branch identify
\(y_*=q_{34}(t_*)\) with the last-leg map of that half-chain.
The complete following-disk comparison is applied at \(t_*\),
with precisely this outgoing reference. The external coordinate
\(c\) is not substituted for that following input.

Set
\[
 R=e^{2\pi\Im y_*},\qquad
 \nu(y_*)=-\Re g(y_*),\qquad
 A_*=\Re\mathcal P_{34}(-2,y_*)+\frac12\nu(y_*).
 \tag{1}
\]
Here \(\mathcal P_{34}\) is the original absolute pre-Gram action.
No additive constant or boundary factor has changed. The original
type-four enclosure is
\[
 .24<\Re y_*<.36,\qquad -.102<\Im y_*<-.001 .
 \tag{2}
\]
In particular
\[
                         \frac{10}{19}<R<1 .
 \tag{3}
\]
The inequality \(e^{.204\pi}<19/10\) used for (3) is also the
explicit radius witness in
[the ordinary endpoint budget, Section 2](research_mixed_first_four_next_four_endpoint_budget.md).
For a direct elementary verification, use
\[
 \log(19/10)>
 2\left\{\frac9{29}+\frac13\left(\frac9{29}\right)^3
                     +\frac15\left(\frac9{29}\right)^5\right\}
 >\frac{51}{250}\frac{22}{7}>.204\pi .
 \tag{4}
\]
The first inequality is the positive series for twice the inverse
hyperbolic tangent; the second is a rational comparison.

The completed
[following remainder theorem, equation (8)](research_mixed_three_four_following_remainder_gaps.md)
proves, on both full disks \(P_3,P_4\),
\[
 \Re\mathcal P_{34}(-2,y_*)>\mathfrak C(R),\qquad
 \mathfrak C(R)=\frac{350711}{192000}
                   -\frac6{25}b(R)+\frac{b(R)^2}{20},
 \quad b(R)=\frac12\log\frac2{1+R^2}.
 \tag{5}
\]
This uses the already completed source comparison, including its
fixed complementary contour. It is a lower bound on this same
geometric action, not an inference from an upper estimate of a
finite sum alone.

## 2. The allocated action exceeds \(9/5\)

**Theorem 1.** At every reference above,
\[
                     A_*>\frac95+\frac{439}{2112000}.
 \tag{6}
\]

*Proof.* Equation (3) gives
\[
 0<b(R)<\frac12\log\frac{722}{461}<\frac9{40}.
 \tag{7}
\]
For the last inequality, the first five terms of the positive
exponential series give
\[
 e^{9/20}>
 1+\frac9{20}+\frac{81}{800}
       +\frac{729}{48000}+\frac{6561}{3840000}
 =\frac{6021681}{3840000}>\frac{722}{461}.
 \tag{8}
\]
The quadratic in (5) decreases on \(0\le b\le9/40\).
Consequently
\[
 \mathfrak C(R)>
 \frac{350711}{192000}-\frac{27}{500}+\frac{81}{32000}
                         =\frac{340829}{192000}.
 \tag{9}
\]

For the halfweight, the integral formula in
[Fourier weight continuation, equations (22), (25)--(26)](research_mixed_fourier_weight_continuation.md)
gives, with \(x=\Re y_*\),
\[
 \nu(y_*)\ge\frac{\sin(2\pi x)}{2\pi}\log(1+R).
 \tag{10}
\]
On (2), \(\sin(2\pi x)>3/4\). Moreover
\[
 \log(29/19)>
 2\left\{\frac5{24}+\frac13\left(\frac5{24}\right)^3\right\}
 =\frac{8765}{20736}>\frac{21}{50}.
 \tag{11}
\]
Using \(R>10/19\) and \(\pi<22/7\), (10)--(11) imply
\[
                   \frac12\nu(y_*)>\frac{441}{17600}.
 \tag{12}
\]
Adding (9) and (12) yields exactly
\[
 \frac{340829}{192000}+\frac{441}{17600}
                =\frac95+\frac{439}{2112000}.
 \tag{13}
\]
This proves (6). \(\square\)

## 3. A larger admissible polynomial bound

Let \(E_N(w,Y)\) be a polynomial of degree at most \(N-1\)
in \(Y\), with the uniform bound
\[
 \sup_{|Y|\le1}|E_N(w,Y)|
        \le C_\tau N^{d_\tau}
                     e^{N(25/16+\tau)}
 \tag{14}
\]
for every sufficiently small fixed \(\tau>0\).
The statement below applies on whichever ordinary-color set has
this bound; no complete-color estimate is extrapolated to other
colors.

Keep the selected segment and the independent outgoing plateau
from the selected-plateau theorem:
\[
 y=x+i/100,\quad x\in[.22,.45],\quad Y=e^{-2\pi iy},
 \qquad z=u+i\Im z_*,\quad u\in[.22,.45],\quad Z=e^{-2\pi iz}.
 \tag{15}
\]
Let \(\Lambda_{123}(z)\) be that theorem's absolute action and
outgoing affine marginal, with its original normalization.

**Theorem 2.** For every sufficiently small total tolerance
\(\tau>0\),
\[
 \begin{split}
 &|E_N(w,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|
                         |d_N(Z)|^{\beta/2}\\
 &\hspace{8mm}\le C_\tau N^{D_\tau}
       e^{N\{\Lambda_{123}(z)-1/200+\tau\}}.
 \end{split}
 \tag{16}
\]
It holds at both level parities. For \(\beta=0\) there is no
outgoing weight. A finite exponential gap \(1/400\) remains
after choosing the tolerances and absorbing polynomial factors.

*Proof.* Only the polynomial ceiling changes in the earlier
selected-plateau proof. The exterior maximum principle contributes
\(\pi/50\) to its rate. The remaining selected halfweight has
rate
\[
 H_0(x)=\max\{-J(x)/2-3\pi/400,0\}.
 \tag{17}
\]
The full ordinary third-factor comparison costs \(7/250\)
above its original supporting plane \(B_3(x,u)\).
Both alternatives of the exact Fourier polynomial, every
conditional row, and the outgoing halfweight remain in that
comparison.

Write \(a=\Re y_*\) and
\[
        p=\Re\{g'(s_*+y_*)-\tfrac32g'(y_*)\}.
 \tag{18}
\]
Original stationarity gives
\(A_*+p(x-a)+B_3(x,u)\le\Lambda_{123}(z)\).
If \(p\le0\), the marginal argument in the earlier proof gives
\[
 H_0(x)-p(x-a)<3/25.
 \tag{19}
\]
The total positive cost before subtracting \(A_*\) is therefore
less than
\[
 \frac{25}{16}+\frac7{250}+\frac{11}{175}+\frac3{25}.
 \tag{20}
\]
Its difference from \(9/5\) is \(373/14000>1/200\).

If \(p\ge0\), the same original marginal bound gives
\[
 H_0(x)-p(x-a)
       <\frac1{12}-\frac{3\pi}{400}+\frac{801}{10000}.
 \tag{21}
\]
The total positive cost is then less than
\[
 \frac{25}{16}+\frac7{250}+\frac1{12}
                       +\frac{11}{280}+\frac{801}{10000}.
 \tag{22}
\]
Its difference from \(9/5\) is
\[
                   \frac{89}{13125}
                       =\frac1{200}+\frac{187}{105000}.
 \tag{23}
\]
In both cases Theorem 1 gives the stated strict reserve.
Allocate the finite-source tolerances inside that reserve.
This proves (16), with the same exact factors and independent
outgoing-coordinate scope as the original comparison.
\(\square\)

Theorem 2 supplies a bound when (14) is actually established.
It does not assert (14) for the complete remaining prefix.
On the whole outgoing plateau (16) is a weighted bound; no
division through a zero of \(d_N(Z)\) is asserted. When the
input bound is holomorphic on fixed parameter neighborhoods,
the existing local nonzero factorial weight and fixed-radius
Cauchy argument also give normalized derivative bounds near the
actual outgoing reference.
