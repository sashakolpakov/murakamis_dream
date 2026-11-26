# An upper Fourier-alias branch on the lower-right shared interval

Private research proof, 8 November 2026. The original type-four
conditional cubic has two upper-half-plane roots, counted with
multiplicity, when the incoming exponential is negative real and
the shared outgoing exponential is in the upper half of the unit
disk. One of these roots comes from the positive real root at the
inward seam. On the original logarithmic sheet its critical equation
is \(Q_t=-2\pi i\), rather than \(Q_t=0\).

The corresponding upper-alias action has real part exactly zero at
the seam and positive real part immediately inside the lower-right
interval. This is a phase and source-identification result. It does
not give a finite alias coefficient, dominance, or a failure of the
desired complete transfer estimate. No numerical evaluation is used.

## 1. The literal source and its original phase

Keep the complete finite kernel
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
       \frac{X^{-j}(rX;r)_j(rY;r)_j}{(r;r)_j^3},
 \qquad r=e^{-2\pi i/N}.
 \tag{1}
\]
The phase, including the incoming carrier, is
\[
 Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,
 \qquad g'(z)=\Log(1-e^{-2\pi iz}).
 \tag{2}
\]
Use the original primitive constant and the original logarithms on
\(0<\Re z<1\), as in
[the algebraic conditional domain, Section 1](research_mixed_four_conditional_algebraic_transport_domain.md).
For \(v=e^{2\pi it}\), its exponential critical equation is
\[
 v(v-X)(v-Y)=X(v-1)^3.
 \tag{3}
\]

Fix
\[
 X=-\rho,\qquad \frac58\le\rho\le1,
 \qquad a=\frac12-i\eta,\quad
 \eta=-\frac{\log\rho}{2\pi}.
 \tag{4}
\]
This includes the actual incoming half face. At the outgoing positive
radius put
\[
 Y=R,\qquad \frac12<R<1,
 \qquad y=1-i\xi,\quad \xi=-\frac{\log R}{2\pi}>0.
 \tag{5}
\]
The boundary coordinate in (5) is approached from \(\Re y<1\).
The original primitive is regular there because \(R<1\).

## 2. The real root and the change in the upper root count

At (4)--(5), equation (3) is the real cubic
\[
 P(v,R)=(1+\rho)v^3-(2\rho+R)v^2
                  +\rho(3-R)v-\rho=0.
 \tag{6}
\]
One quarter of the discriminant of its derivative is
\[
 R^2+(7\rho+3\rho^2)R-5\rho^2-9\rho
 <1-2\rho-2\rho^2\le-\frac{33}{32}<0.
 \tag{7}
\]
The first expression increases with \(R\le1\). Consequently
\(P_v>0\) on the real axis, and the cubic has a unique simple real
root and a simple nonreal conjugate pair. These are the same real
seam equations used in
[the closed-seam annulus theorem, Section 1](research_mixed_conditional_corner_root_annulus.md).

Writing (6) as
\[
 P(v,R)=v(v+\rho)(v-R)+\rho(v-1)^3
\]
shows that
\[
 P(R,R)=\rho(R-1)^3<0,
 \qquad P(1,R)=(1+\rho)(1-R)>0.
\]
Thus the real root, denoted \(r_0\), satisfies
\[
                         R<r_0<1.
 \tag{8}
\]
Implicit differentiation gives
\[
 \frac{dr_0}{dR}=\frac{r_0(r_0+\rho)}{P_v(r_0,R)}>0.
 \tag{9}
\]
There is also a useful strict upper bound. Solving (3) for \(R\)
at this root gives
\[
 R(v)=v-\frac{\rho(1-v)^3}{v(v+\rho)},\qquad 0<v<1.
 \tag{10}
\]
The positive term subtracted from \(v\) is strictly decreasing:
its numerator decreases and its positive denominator increases.
Hence \(R'(v)>1\), so
\[
            0<\frac{dr_0}{dR}<1,
 \qquad 0<\frac{R}{r_0}\frac{dr_0}{dR}<1.
 \tag{11}
\]

The root \(r_0\) therefore moves into the upper half-plane when
\(Y\) is displaced from \(R\) in the positive imaginary direction.
The nonreal pair retains one root in each half-plane under a
sufficiently small displacement. The cubic thus has two upper roots
and one lower root there.

This count holds throughout
\[
                         \Im Y>0,\qquad |Y|<1,
 \tag{12}
\]
for every fixed \(\rho\) in (4), counting multiplicity. Indeed, a
real root would give
\[
 Y=v+\frac{\rho(v-1)^3}{v(v+\rho)}\in\mathbb R.
 \tag{13}
\]
The exceptional values \(v=0,-\rho\) are not roots of (3).
Thus no root crosses the real axis in the connected domain (12).
The leading coefficient \(1+\rho\) stays nonzero and the
coefficients remain bounded on compact paths, so no root escapes
to infinity. This proves the count. It does not exclude collisions
between the two upper roots inside (12), or give two globally
labelled simple branches there.

## 3. The extra root lies on the original upper-alias sheet

For small \(\varepsilon>0\), keep \(R\) fixed and put
\[
 y=1-\varepsilon-i\xi,
 \qquad Y=R e^{2\pi i\varepsilon}.
 \tag{14}
\]
Let \(v_+(Y)\) be the simple local root continuing \(r_0\), and set
\[
 t_+(y)=\frac{\Log v_+(Y)}{2\pi i}.
 \tag{15}
\]
Its expansion and (11) give
\[
 \Re t_+(y)=
 \frac{R}{r_0}\frac{dr_0}{dR}\,\varepsilon+O(\varepsilon^2),
 \qquad 0<\Re t_+(y)<\varepsilon.
 \tag{16}
\]
The last strict inequalities hold for all sufficiently small
positive \(\varepsilon\). At the boundary,
\[
 t_0=i\sigma,\qquad
 \sigma=-\frac{\log r_0}{2\pi},\qquad 0<\sigma<\xi.
 \tag{17}
\]
Equations (16)--(17) ensure, in the same one-sided collar,
\[
 0<\Re t_+<\frac12,
 \quad 0<\Re(a+t_+)<1,
 \quad 0<\Re(y+t_+)<1,
 \quad \Im(y+t_+)<0.
 \tag{18}
\]
In particular the outgoing numerator stays on its original
prewall sheet; no postwall logarithmic reset is being made.

As \(\varepsilon\downarrow0\), the two shifted logarithms in
\(Q_t\) have positive real arguments:
\[
 1-\frac X{r_0}=1+\frac\rho{r_0}>0,
 \qquad 1-\frac R{r_0}>0.
 \tag{19}
\]
The own argument \(1-e^{-2\pi it_+}\) approaches
\(1-r_0^{-1}<0\) from the upper half-plane. Its original argument
therefore tends to \(\pi\). Since \(\Im(2\pi ia)=\pi\),
the original logarithmic derivative satisfies
\[
 \lim_{\varepsilon\downarrow0} Q_t(t_+;a,y)
                             =-2\pi i.
 \tag{20}
\]
Its real part is zero by (3). On the local root branch its
exponential is identically one, and continuity preserves this
integer lift. Thus, throughout that one-sided collar,
\[
 \boxed{\quad Q_t(t_+;a,y)=-2\pi i,\qquad
       \partial_t\{Q(t;a,y)+2\pi it\}\big|_{t=t_+}=0.\quad}
 \tag{21}
\]
All collar statements are uniform on compact subsets of the
\((\rho,R)\) domain (4)--(5), in particular on the closed actual
radius ranges strictly inside \(0<R<1\).

## 4. Exact boundary action and its one-sided sign

Define the local alias action
\[
                  \Phi_+(a,y)=Q(t_+(y);a,y)+2\pi it_+(y).
 \tag{22}
\]
The original primitive has real part zero on the inward positive
radius and on the whole line \(\Re z=1/2\). The former follows
from the real dilogarithm value in
[the forced-weight proof, equation (5)](research_mixed_next_reflected_forced_weight_bound.md);
for the latter, \(g'(1/2+ih)=\log(1+e^{2\pi h})\) is real, so
the real part is constant vertically and equals zero on the real
axis. On the right-hand boundary of the positive imaginary axis,
\[
 \Re g(i\sigma)=-\pi\sigma.
 \tag{23}
\]
Indeed \(g(0)=0\) and the original argument of
\(1-e^{2\pi\sigma}\) is \(\pi\), giving vertical real derivative
\(-\pi\).

At (17), \(y+t_0=1-i(\xi-\sigma)\) is on the inward positive
radius. Therefore
\[
 \Re g(a+t_0)=\Re g(a)=\Re g(y+t_0)=\Re g(y)=0,
 \qquad \Re(2\pi iat_0)=-\pi\sigma.
\]
Together with (23), this yields
\[
 \Re Q(t_0;a,1-i\xi)=2\pi\sigma,
 \qquad \boxed{\ \Re\Phi_+(a,1-i\xi)=0.\ }
 \tag{24}
\]
Stationarity for (22) cancels the derivative of \(t_+\). Hence
the derivative in the outgoing real coordinate at the seam is
\[
 \partial_q\Re\Phi_+(a,1-i\xi)
   =\log\frac{1-R/r_0}{1-R}<0.
 \tag{25}
\]
Both numerator and denominator are positive, and the ratio is less
than one because \(r_0<1\). Thus for sufficiently small
\(\varepsilon>0\),
\[
                 \Re\Phi_+(a,1-\varepsilon-i\xi)>0.
 \tag{26}
\]
No magnitude of a finite contribution is inferred from this sign.

## 5. The negative-radius endpoint also has an entering alias root

At the other end of the same lower-right interval, set
\(Y=-R\) and \(y=1/2-i\xi\). The real cubic is
\[
 (1+\rho)v^3+(R-2\rho)v^2+\rho(3+R)v-\rho.
 \tag{27}
\]
The derivative discriminant divided by four is
\[
 R^2-(7\rho+3\rho^2)R-5\rho^2-9\rho
 <1-5\rho^2-9\rho<0.
 \tag{28}
\]
Its real root \(r_-\) lies in \((0,1)\), since its values at
zero and one are \(-\rho\) and \((1+\rho)(1+R)\).
As a function of the real coordinate \(Y\), this root again has
positive derivative \(v(v+\rho)/P_v\). Along
\(y=1/2+\varepsilon-i\xi\), therefore,
\(Y=-R e^{-2\pi i\varepsilon}\) moves upward, and the root
enters the upper half-plane with \(\Re t>0\).

Both shifted logarithms have positive real arguments at the endpoint,
namely \(1+\rho/r_-\) and \(1+R/r_-\). The own logarithm again
has the boundary argument \(\pi\). All shifted real coordinates
are strictly between zero and one in a sufficiently small one-sided
collar. The original equation on this local branch is consequently
\(Q_t=-2\pi i\), by precisely the lift argument of Section 3.

Here \(a+t\) and \(y+t\) both lie on \(\Re z=1/2\) at the
endpoint. Applying (23) again gives
\[
 \Re\Phi_+(a,1/2-i\xi)=0,
 \qquad
 \partial_q\Re\Phi_+(a,1/2-i\xi)
       =\log\frac{1+R/r_-}{1+R}>0.
 \tag{29}
\]
Thus the real alias action is strictly positive immediately to the
right of \(q=1/2\), as well as immediately to the left of \(q=1\)
in (26). These are two local branch statements. We do not identify
the branches globally, exclude a collision in the intervening
domain, or apply the zero-mode root-annulus bounds to either alias
root.

## 6. What this identifies in the remaining finite problem

On an upper private contour the exact cotangent remainder contains
\(\cot(\pi Nt)+i\). The identity
\[
 \cot(\pi Nt)+i=
                  \frac{2i e^{2\pi iNt}}{e^{2\pi iNt}-1}
 \tag{30}
\]
shows why its leading phase is precisely \(Q+2\pi it\), the
phase in (21). All integer-frequency terms of (30) still belong to
the complete finite contour. An algebraic continuation of the old
unique zero-mode root cannot replace their estimate on (12).

The branch in (16) approaches the private endpoint: for every fixed
positive lower cut it lies to its left sufficiently near the seam.
Thus (21) does not by itself contradict an alias inequality on a
particular retained middle rectangle. Its location must be accounted
for together with the omitted low physical rows and the full
left-cut currents. No contour is deformed across this branch here.

The exact reflected finite observation remains the one in
[the full reflection theorem, Sections 3--6](research_mixed_next_lower_complement_exact_reflection.md).
It reverses the prefix and forced weight, changes the Newton kernel,
and interchanges the two Fourier coefficient observations with their
stated degree shifts. The
[complete forced-weight half-annulus theorem](research_mixed_next_reflected_forced_weight_bound.md)
already bounds the full reversed weight at zero upper exponential
rate, with every forcing term retained. It leaves the coupled
reversed-prefix/complementary-kernel factor to be estimated.

Consequently a useful next estimate must either bound that coupled
factor on the actual reflected contour, or retain the low physical
rows and upper-alias contribution identified by (21)--(30) on a
source-valid direct contour. Neither the new left-domain finite
theorem nor a scalar conjugation identity supplies this estimate.
The results above are valid independently of \(N\) and do not
alter either parity, the original outside \(+N\) measure, any
cardinal filter, or any already frozen source theorem.
