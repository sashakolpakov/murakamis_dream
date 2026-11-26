# Original source logarithmic lifts on the positive geometric family

Research theorem, 5 November 2026. At a degree-two unit vertex of power
three or four, the inverse geometric legs satisfy both original
unsummed source equations with zero logarithmic lifts. The shared-wire
equation likewise has its original zero lift. The argument keeps the
own vertex charge equal to one when calibrating the vertex equation;
it does not infer that equation along a fractional own-charge path.
Pair-sum chamber inclusion and absolute action constants remain separate.

## 1. The principal chart is the original source chart

Use the original positive path charge family. On an incidence write
\[
 X=e^{2\pi ix},\qquad U=e^{-2\pi is},
 \qquad s=\frac{i}{2\pi}\Log U .
                                                               \tag{1}
\]
The [inverse-leg theorem](research_mixed_all_leg_half_plane.md) and
[wire-before-leg theorem](research_mixed_wire_before_inverse_leg.md)
give, on an edge incident to an active vertex,
\[
 \Im U<0,\qquad 0<\Re x<\Re s<1/2,\qquad
 0<\Re x<1/4,\quad \Im x>0.                              \tag{2}
\]
Complete edges have \(x=1/4\); the same wire-before-leg inequality
holds there. The leg logarithm is continuous from completeness.

For the original primitive \(g(z)=J(z)+i\pi z(1-z)/2\),
\[
                 g'(z)=\Log(1-e^{-2\pi iz})
                         \qquad(0<\Re z<1)              \tag{3}
\]
with the principal logarithm. Its argument never crosses the
negative real axis in this strip. For the original incidence phase
\[
 \ell_s(x)=2\pi isx-I_X(s)-\pi ix,\qquad
 I_X(s)=\frac{\operatorname{Li}_2(XU)-\operatorname{Li}_2(X)}
                    {2\pi i},                           \tag{4}
\]
the logarithmic derivative is
\[
                 (\ell_s)_s=2\pi ix-\Log(1-XU).           \tag{5}
\]
These are the original branches, rather than new logarithm choices.
Indeed \(X\) is in the first-quadrant disk and \(XU\) is strictly
in the lower half-plane by (2). The two dilogarithms in (4) therefore
avoid their principal cut, including when \(|XU|>1\). The domain
\(0<\Re x<\Re s<1/2,\ \Im x>0\) is convex, and (4) continues
the original formula from its convergent-product subdomain.
This is the same branch argument used in
[the endpoint action calibration](research_mixed_endpoint_action_calibration.md).
No finite interpolation extension is inferred from this analytic identity.

For two inverse legs \(s,t\), their sum has real part in \((0,1)\).
Thus (3) also applies to \(s+t\), even before any stronger
pair-sum inequality is proved.

## 2. The type-three original vertex equations

Let a selected vertex have exactly two original incidences, including
complete outside incidences when it is an endpoint. Let its power
be \(n=3+\epsilon\), its charge be one, and write its angle as
\(\tau\), wires as \(x,y\), and inverse legs as \(s,t\). Put
\[
 U=e^{-2\pi is},\quad V=e^{-2\pi it},\quad
 X=e^{2\pi ix},\quad Y=e^{2\pi iy}.
\]
Its original unsummed vertex phase is
\[
 \mathcal V_n
 =g(s+t)-\epsilon\{g(s)+g(t)\}+\ell_s(x)+\ell_t(y).
                                                               \tag{6}
\]
The [exact unit-period elimination](research_mixed_unit_period_leg_elimination.md)
proves
\[
 X(1-UV)=(1-U)^\epsilon(1-XU),\qquad
 Y(1-UV)=(1-V)^\epsilon(1-YV),                            \tag{7}
\]
with all factors nonzero. Therefore its actual derivatives
\[
\begin{split}
 f_s&=\Log(1-UV)-\epsilon\Log(1-U)
                         +2\pi ix-\Log(1-XU),\\
 f_t&=\Log(1-UV)-\epsilon\Log(1-V)
                         +2\pi iy-\Log(1-YV)
\end{split}                                                   \tag{8}
\]
belong to \(2\pi i\mathbb Z\). Section 1 fixes every logarithm
in (8) to the original principal branch.

For \(n=3\), one has
\(\arg(1-UV)\in(-\pi,\pi)\),
\(\arg(1-XU)\in(0,\pi)\), and \(0<2\pi\Re x<\pi/2\).
It follows that
\[
                    -2\pi<\Im f_s<3\pi/2,               \tag{9}
\]
and similarly for \(f_t\). The only possible integer lifts are zero.

## 3. Type four: keep the own charge fixed during calibration

Fix the charge of the present type-four vertex to one. Scale every
other selected charge from zero to its prescribed value, keeping all
original powers, incidences and complete boundary vertices unchanged.
The positive charge theorem supplies this continuous family, including
its zero-charge face. The own vertex stays active throughout.
Equations (2)--(8) hold along the entire family; in particular the
own unit equation and its algebraic consequence (7) are never changed.
The two integers \(f_s/(2\pi i)\), \(f_t/(2\pi i)\) are therefore
constant along the path.

At its initial point both neighbors have complete angle zero.
The two original returns and wires are equal, hence \(U=V\).
The type-four elimination gives
\[
                    2\cos\tau=-U-V,\qquad U=-\cos\tau.   \tag{10}
\]
Each return has negative imaginary part: its hyperbolic sine is
\(\tan(\tau/2)\), whose imaginary part is strictly negative,
and the original return has imaginary part in \((-\pi/2,\pi/2)\).
The own unit equation consequently gives
\[
             \sum g_j=2\Re\tau-\pi<0,\qquad
             0<\Re\tau<\pi/2,\qquad \Re U<0.             \tag{11}
\]

The conditional type-four argument test in
[the preceding half-plane lemma](research_mixed_four_leg_half_plane.md#3-conditional-original-zero-lifts-with-weaker-angle-hypotheses)
now applies at this initial point. Explicitly, for
\(U=a-ib,\ V=c-id\), with \(a,c\le0,\ b,d>0\),
\[
 \Im\frac{1-UV}{1-U}
 =\frac{d(a-a^2-b^2)+b(c-1)}{|1-U|^2}<0.                 \tag{12}
\]
The actual principal argument difference
\(\arg(1-UV)-\arg(1-U)\) lies in \((-2\pi,\pi)\);
its negative sine puts it in \((-\pi,0)\). Together with
(2), this gives \(-2\pi<\Im f_s<\pi/2\), and likewise
for \(f_t\). Both lifts are zero at the initial point and remain
zero along the fixed-own-charge path.

**Theorem 1.** Every degree-two unit vertex of power three or four in
the stated positive path family has
\[
                   (\mathcal V_n)_s=(\mathcal V_n)_t=0   \tag{13}
\]
in the original unsummed source logarithms.

The type-four continuation only uses its left-half-plane leg condition
at the isolated initial vertex. It does not assert that condition
for the final inverse legs. Simultaneously varying the own charge
would not give the proof above, since (7) would then cease to hold.

## 4. The shared-wire equation has a charge-independent calibration

On a shared edge let \(A,B\) be the two geometric cosine squares,
\[
 q^2=A^{-1}+B^{-1}-1,\quad
 X=\frac{q+i}{q-i},\quad
 U=\frac{-i}{2A(q+i)-i},\quad
 V=\frac{-i}{2B(q+i)-i}.
                                                               \tag{14}
\]
Direct substitution gives
\[
              (1-XU)(1-XV)=UV(1-X)^2.                   \tag{15}
\]
Unlike (7), this identity has no vertex charge in it. It holds
throughout simultaneous scaling of all charges from completeness.
The original derivative is
\[
\begin{split}
 \partial_x\{\ell_s(x)+\ell_t(x)\}
   ={}&-\Log U-\Log V+\Log(1-XU)+\Log(1-XV)\\
      &-2\Log(1-X)-2\pi i.
\end{split}                                                   \tag{16}
\]
The individual and wire-before-leg strips keep all these logarithms
on their original branches along the full family. Equation (15)
puts (16) in \(2\pi i\mathbb Z\).

At completeness,
\[
 X=i,\qquad U=V=\frac{-1-2i}{5},\qquad
 1-XU=\frac{3+i}{5}=-U(1-X).                             \tag{17}
\]
The product \(U(1-X)=(-3-i)/5\) lies in the lower-left quadrant,
and its negative \(1-XU\) lies in the upper-right quadrant.
The principal logarithms consequently satisfy
\[
       \Log(1-XU)=\Log U+\Log(1-X)+\pi i.
\]
Both individual incidence derivatives, and hence (16), are exactly
zero there. Their shared sum remains zero along simultaneous charge
scaling. Thus the original shared-wire stationary equation has its
zero lift at every positive configuration in this family.

This theorem supplies the vertex and shared-wire logarithmic
equations on the geometric inverse. It does not identify that point
with the independently localized source critical point: the common
injectivity-chamber inclusion still requires the adjacent-sum
inequalities. Nor does a zero derivative determine an absolute
vertex action constant. The endpoint action identity remains the
separately calibrated result cited above; no global finite-source
or volume-conjecture conclusion is asserted here.
