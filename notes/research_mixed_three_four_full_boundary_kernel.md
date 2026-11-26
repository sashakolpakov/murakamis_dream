# The complete ordinary three/four kernel on its full boundary

Research deduction, 7 November 2026. The original internal ordinary
\((3,4)\) block has a whole-real-color angular bound and a nonzero
holomorphic packet on a fixed two-color neighborhood. A polynomial
maximum-principle argument supplies the quadratic complex-strip bound.
These are the analytic kernel hypotheses of the finite two-boundary
closure theorem. The proof estimates the original source before
integrating; it does not deduce a global color bound from the value of
the complete-color asymptotic. No numerical evaluation or certificate
replay is used.

## 1. Original source and statement

Use the unchanged functions of
[complementary-contour completion](research_mixed_three_four_complementary_contour_completion.md):
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{j=0}^{N-1}
                    \frac{H_N(w,r^{-j})p_j(X)}{P_j},\\
 V_{1,N}(w,X)&=\sum_{i=0}^{N-1}
                \frac{X^{-i}p_i(X)}{P_i^2}U_{1,N}(w,r^i),\\
 Z_{34,N}(w_L,w_R)&=\kappa_N^3N^2\int_0^1
 U_{0,N}(w_L,e^{-2\pi ia})V_{1,N}(w_R,e^{-2\pi ia})\,da .
\end{split}                                                     \tag{1}
\]
Here \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), and \(|\kappa_N|=1\). Each endpoint
coefficient and physical cap is its complete original polynomial.
There is no additional diagonal weight, Fourier selection or change
of ordinary observation. The kernel is a polynomial of degree at
most \(N-1\) separately in \(w_L,w_R\).

Let \(a_*=A+ic\), \(\mathcal S=T_0(a_*)+P_1(a_*)\),
and \(M=\Re\mathcal S\) be the actual original reference. We
use the same saved premises as complementary-contour completion:
\[
                 M>27/10,\qquad -7/200<c<0.             \tag{2}
\]
The saved result has SHA256
`fbd429caab1fe76764f35b2e1beaaa5e4a273038d810acabe708d5644ea82b70`.
No value or inequality is recomputed from a root here.

Write \(D(\theta)=1-\cos\theta\) and
\[
 K_{34,N}(\theta_L,\theta_R)
      =Z_{34,N}(-2\cos\theta_L,-2\cos\theta_R).
                                                               \tag{3}
\]

**Theorem 1.** The following constants and neighborhoods are fixed,
independently of \(N\), with both level parities retained.

1. On a neighborhood of a closed complex angular bidisk about zero,
   \[
   K_{34,N}(\boldsymbol\theta)
    =\kappa_N^3N^{-3/2}\mathcal A(\boldsymbol\theta)
       e^{N\Phi(\boldsymbol\theta)}(1+\varepsilon_N(\boldsymbol\theta)),
   \qquad \varepsilon_N=O(N^{-1}),                    \tag{4}
   \]
   where \(\mathcal A\) is holomorphic and zero-free, \(\Phi\)
   is the original calibrated boundary action, and the normalized
   error is holomorphic and uniformly bounded as displayed.
   Every fixed normalized mixed jet has the corresponding
   \(O(N^{-1})\) bound on smaller bidisks. The phase is separately
   even, \(\Phi(0,0)=\mathcal S\), and on a smaller bidisk
   \[
                     -\Re\Phi''\succeq\kappa I_2>0.   \tag{5}
   \]
2. There are \(c_0,B,h>0\), \(C,d<\infty\), such that
   \[
   |K_{34,N}(x+iy,v+iw)|
    \le CN^d e^{N\{M-c_0D(x)-c_0D(v)+B(y^2+w^2)\}}
                                                               \tag{6}
   \]
   for all \(x,v\in[-\pi,\pi]\), \(|y|,|w|\le h\).
   In particular the whole real boundary has strict loss at either
   endpoint away from complete color. Every fixed ordinary-color
   derivative on the real boundary has the same angular exponents,
   with a polynomial change of prefactor.

Thus this exact kernel satisfies hypotheses (5)--(7) of
[finite two-boundary closure](research_finite_two_boundary_kernel_closure.md).
This conclusion supplies a kernel eligible for that theorem's stated
long-power operations; it does not assert closure under arbitrary
adjacent short compositions.

## 2. The all-real source inputs and the order of deletion

The endpoint real-color theorem gives, for all real ordinary colors,
\[
\begin{split}
 |C_N(e,-2\cos\theta)|
 &\le CN^b e^{N\{\Re S(e)-c_E D(\theta)\}},
        &&e\in E_c=[.27,.49]+i[-.055,.04],\\
 |H_N(-2\cos\theta,r^{-j})|
 &\le C_I N^{b_I}e^{Nh(j/N)},
        &&j/N\in I\Subset(0,1),\\
 h(e)&=J(e)+\Re S(e),
 \qquad J(t)=\int_0^t\log(2\sin\pi u)\,du .
\end{split}                                                     \tag{7}
\]
These are estimates of the whole coefficients, including their
revived Newton rows. They hold on a fixed neighborhood of the
central private rectangle. We may drop their favorable angular loss
when a source-region gap will pay it later.

The exact endpoint arguments in
[terminal real-color decay](research_mixed_terminal_real_color_decay.md),
Section 2, also give the original all-real coherent norms
\[
 \sum_j |H_N(w,r^{-j})|/|P_j|^\alpha
       \le C_\tau N^{b_\tau}e^{N(b_\alpha+\tau)},
 \qquad b_0=101/125,\quad b_1=433/500,                 \tag{8}
\]
and, for every fixed \(\delta,\tau>0\),
\[
 |H_N(w,r^{-j})|\le C_{\delta,\tau}N^{b_{\delta,\tau}}
             e^{N\{h(j/N)+\tau\}},
       \qquad 0\le j/N\le1-\delta.                    \tag{9}
\]
The lower endpoint in (9) follows from its exact finite entropy;
no off-grid endpoint packet near one is asserted.

For clarity the needed support deletion is made at the finite-source
level. In
\[
 V_{1,N}(w,X)=\sum_{i,j<N}
 \frac{X^{-i}p_i(X)}{P_i^2}
 \frac{p_j(r^i)H_N(w,r^{-j})}{P_j^2},                  \tag{10}
\]
first remove the whole transform rows
\(i\le\lfloor N\delta\rfloor\), including all their private
and Newton terms. The
[global transform-end theorem](research_mixed_three_four_global_transform_ends.md)
pays them after multiplication by the complete first cap, uniformly
for all real colors. Put \(i_{\min}=\lfloor N\delta\rfloor+1\).
For every remaining physical row the entire columns
\(j\ge N-i_{\min}\) vanish. Delete these columns before any
transform contour is moved. All remaining physical private columns
satisfy \(j/N<1-\delta\), so (9) applies. Within each retained
column its polynomial \(p_j(e^{-2\pi it})\) is kept literal after
deformation. Its other physical zeros may revive off grid.

On the central private contour insert the first line of (7) into
the exact original interpolant
\[
 e^{2\pi iNat}\Pi_N(a+t)\Pi_N(e+t)
 E_N(a)E_N(t)^3E_N(e)\Delta_N(e)^{-1}C_N(e,w_R).         \tag{11}
\]
All other factors, branches, sampling penalties and current
coefficients are color independent. Therefore every previously
calibrated complete-color upper profile on this contour is also an
all-real-color upper profile. For physical private tails use (9),
whose rate is precisely the old coherent rate. For physical upper
transform rows, the support gives
\(0\le l/N\le j/N<1-i/N\le1/2\). The exact inequality
\(V_\theta(l/N)\le V_0(l/N)\) retains every old positive
triple-row majorant. The complete-color entropy on the upper
Newton half is never used as an all-color majorant.

## 3. True cap ends on the real small-angle sector

The small-angle proof originally used a near-complete-color
whole-index packet for \(H_N\). Its all-real extension needs a
separate treatment of the two extreme cap layers. Here is a direct
calibrated estimate for them on the entire real incoming circle.

The [real-circle cap-end theorem](research_mixed_cap_real_circle_index_ends.md)
gives a fixed \(\delta_0>0\) such that
\[
 U_{\mathrm{end},N}^{\mathrm{abs}}(w,X)
 :=\sum_{j/N\le\delta_0\ \mathrm{or}\ j/N\ge1-\delta_0}
        \frac{|H_N(w,r^{-j})p_j(X)|}{|P_j|}
       \le CN^b e^{3N/5},\qquad |X|=1.                \tag{12}
\]
It holds for every real color, including both endpoints and all
product zeros. Its exact reflected-factorial proof does not use
(7) at a private endpoint.

Set \(L(t)=-2J((1-t)/2)\). The whole physical cap in each
terminal transform row has the all-real bound
\[
 |U_{1,N}(w,r^i)|\le C_\tau N^{b_\tau}
       e^{N\{b_1+L(t)-J(t)+\tau\}},\qquad t=i/N,       \tag{13}
\]
proved in Section 3 of
[complementary real colors](research_mixed_three_four_complementary_real_colors.md).
The all-period numerator estimate is
\(|p_i(X)|\le CN^b e^{NL(t)}\) on \(|X|=1\). Since
\(\max(-J)<1/6\) and \(\max L<1/3\), the complete positive
outer-row majorant consequently satisfies
\[
 \sum_{i<N}\frac{|p_i(X)|}{|P_i|^2}|U_{1,N}(w,r^i)|
 \le C_\tau N^{b_\tau}
 e^{N\{b_1+2/3+1/2+\tau\}}
 =C_\tau N^{b_\tau}e^{N(3049/1500+\tau)}.             \tag{14}
\]
This includes \(i=0,N-1\), their full cap values, both parities
and every ordinary color. The strict elementary integral bound
\(\max(-J)<1/6\) follows from \(2\sin\pi u>6u\) on
\(0<u<1/6\); it is the same witness as in the global transform-end
theorem, rather than a new evaluated maximum.

Multiplying (12) and (14), and using (2), gives raw deficit
\[
 M-\left(\frac35+\frac{3049}{1500}\right)
       >\frac{101}{1500}>\frac1{20}.                  \tag{15}
\]
One common sufficiently small tolerance retains a fixed gap,
for example \(1/25\). Thus the true cap ends are paid even
when multiplied by any remaining part bounded by (14).

This estimate is used only on real incoming points. It does not
silently remove the chirp at a nonzero incoming height. On the left
taper the already proved all-real five-profile theorem, including
its separately calibrated \(E_{\rm end}\), is used instead.

## 4. First-half all-real ledger

Keep the exact incoming path
\[
 a_-(x)=
 \begin{cases}
 x,&0\le x\le.1,\\
 x+ic(x-.1)/.12,&.1\le x\le.22,\\
 x+ic,&.22\le x\le.5.
 \end{cases}                                                   \tag{16}
\]
It is fixed as the real ordinary colors vary. We now verify every
sector separately.

**Seam.** The proof of
[the two-vertex first collar](research_mixed_two_vertex_first_collar.md)
uses only the zero-safe collar inequality
\(|p_i(e^{-2\pi ix})|/|P_i|\le\operatorname{poly}(N)e^{N\Delta_\rho}\),
the all-period numerator bound, and the norms (8). All hold for
all real colors. Its rate for this word is
\[
 b_0+b_1+M_1(0)+2\Delta_\rho+\tau,
 \qquad M_1(0)<7/15,\quad \Delta_\rho\longrightarrow0. \tag{17}
\]
Choose the same sufficiently small fixed \(\rho>0\), then a
common small tolerance. This is strictly below the original action
by at least \(1/20\), using either its old action calibration
or the stronger (2). Thus the whole seam interval, not just its
endpoint value, has an all-real gap.

**Real small angles.** On \([\rho,.1]\), first remove the
complete terminal end rows as in Section 2. Their estimate uses
the whole first cap. In the remaining product split only the cap
physical end layers (12); their positive product is paid by (15).
For all other cap physical indices use (7) on the fixed compact
interval \([\delta_0,1-\delta_0]\). The original rate is
\(\Re S(e)+I_x(e)\), exactly as in
[the real small-angle proof](research_mixed_three_four_real_small_angle_source.md).
Its lower-tail transport to \(.27\), upper-tail transport to
\([.49,.5]\), and bridge at \(x=.1\) therefore remain valid.
The extra real profile \(.49\le e\le.5\) remains present.
It is not replaced by a false \(.49\)-clipping statement near zero.

The five central cap currents use (7) directly. Each cap/terminal
profile pair has the same color-independent incoming derivative
\(>\log2\) as equation (12) of that proof, including every
intermediate height. All central terminal currents are bounded by
(11); private physical tails use (9) after fixed-column deletion.
Small-transform transport and upper-triangle entropy are unchanged
by Section 2. Thus all pairs reach exactly the old paid profiles
at \(x=.1\). The new cap end contribution is already separate.
Allocate the common tolerances below a fixed portion of the old
reserves. The whole sector has, for example, gap \(1/640000\).
No bound for a signed complete value was used to estimate one of
its uncontracted pieces.

**Left taper.** Theorem 3 of
[the early-taper cap envelope](research_mixed_cap_early_taper_complex_profiles.md)
already holds for all real left colors. It retains its five
profiles at the actual private height and the true-end alternative
\(E_{\rm end}(h)=3/5+2\pi h_++(\log4)/100\).
The [complete left-taper proof](research_mixed_three_four_left_taper_source_completion.md)
calibrates each of these alternatives, not just the signed cap.
Use (11) on its entire unchanged central terminal rectangle and
(9) on its remaining physical private columns. All its original
height convexities, incoming transports and alias penalties are
therefore inequalities for the same upper profiles at all colors.

In particular all nine constant-mode and seventy-two alias
currents remain, including the upper-transform aliases and all
mixed sides. The original main loss
\((\pi/200+\kappa_*)(A-.22)^2>1/20000\) is unchanged.
The disjoint physical sectors are the complete initial transform
rows, the remaining small-transform rows, the physical private
complements, the central-private rectangle, and the whole upper
triangle. Their old bounds use exactly the all-color inputs in
Section 2. Their parity convention assigns the even half-row to
the upper triangle only. Taking the common tolerances smaller if
necessary gives a whole all-real gap \(1/320000\).

**Plateau.** The actual reference is among the completed source
families of [the full plateau theorem](research_mixed_full_unselected_plateau.md).
There is no halfweight in this word. The complete cap and terminal
all-real estimates, equations (14) and (2) respectively of
[endpoint real-color decay](research_mixed_endpoint_real_color_decay.md)
and [terminal real-color decay](research_mixed_terminal_real_color_decay.md), give
\[
\begin{split}
 |U_0(w_L,e^{-2\pi i(x+ic)})V_1(w_R,e^{-2\pi i(x+ic)})|
 &\le CN^b\exp N\{M-2\kappa_*(x-A)^2\\
 &\hspace{15mm}-c_LD(\theta_L)-c_RD(\theta_R)\},
 \qquad .22\le x\le.45,\quad \kappa_*=1/2500000.
\end{split}                                                     \tag{18}
\]
The linear marginals cancel by the original stationary equation.
The exponents in (18) are the proved supporting planes without a
fixed positive rate tolerance; their polynomial errors are already
included. Thus arbitrarily small outside angles retain their loss.

**Right strip.** The complete all-real theorem
[on the right strip](research_mixed_three_four_right_strip_real_colors.md)
applies on \([.45,.5]+ic\). It keeps the moving-cut partition,
all physical complements and the original numerator-wall treatment.
It gives a fixed regional gap with angular losses at both ends.

For the first three sectors and for any uniformly gapped part of
the right strip, ordinary derivatives may first be taken by Markov
on the entire real ordinary-color interval, at polynomial cost.
Only afterwards spend part of the regional gap on angular losses:
if the gap is \(\gamma>0\), then
\[
 \gamma/2+(\gamma/8)\{D(\theta_L)+D(\theta_R)\}
                         \le\gamma.                    \tag{19}
\]
On the plateau use its already proved fixed-derivative angular
bounds. No real-period statement is inferred from a complex disk.

## 5. Whole real boundary bound

The full incoming contour consists of (16), the vertical segment
from \(.5+ic\) to \(.5\), and the real interval from \(.5\)
to one. The source in (1) is entire and one-periodic in \(a\),
so this deformation is exact for every ordinary color.
The [complementary all-real theorem](research_mixed_three_four_complementary_real_colors.md)
bounds the latter two segments, including their original finite
row majorants, by
\[
 CN^b e^{N\{M-1/600-[D(\theta_L)+D(\theta_R)]/2400\}}.
                                                               \tag{20}
\]
Combining (18)--(20) with all sectors of Section 4, and decreasing
a common positive \(c_r\), proves
\[
 |K_{34,N}(\theta_L,\theta_R)|
       \le CN^b e^{N\{M-c_r[D(\theta_L)+D(\theta_R)]\}}
                 \qquad (\theta_L,\theta_R\in[-\pi,\pi]).
                                                               \tag{21}
\]
Every contour length and the original \(N^2\) in (1) costs only
a polynomial factor. Both parities and every physical row occur
once. The fixed ordinary derivatives have the same angular rates,
by the profilewise derivative statements and (19), or by the
weighted-polynomial argument in Section 7 below.

## 6. The full local holomorphic packet and curvature

This step uses the previously proved holomorphic plateau germ, not
analytic continuation of a pointwise asymptotic. Section 4 of
[full unselected plateau](research_mixed_full_unselected_plateau.md)
proves a uniform holomorphic ordinary-color packet for its entire
plateau integral. Its local factors are
\(N^{-1}b_Ue^{NT_0}\) and \(N^{-2}b_Ve^{NP_1}\), with
nonvanishing symbols and holomorphic normalized errors. The actual
shared Hessian is accretive and invertible. Consequently the
critical point \(a_\#(w_L,w_R)\), action \(\mathcal W\),
and coefficient
\[
 \mathcal A_w(w_L,w_R)=
 \frac{\sqrt{2\pi}\,b_U(a_\#,w_L)b_V(a_\#,w_R)}
      {\sqrt{-\partial_a^2(T_0+P_1)(a_\#;w_L,w_R)}}
                                                               \tag{22}
\]
are holomorphic, with \(\mathcal A_w\ne0\), on a fixed
ordinary bidisk about \((-2,-2)\). The square root is the
continued original accretive Gaussian branch.

More explicitly, a small fixed main interval centered at \(A\)
on height \(c\) can be translated by \(a_\#-a_*\).
Cauchy's theorem retains both endpoint connectors. For sufficiently
small parameter disks these connectors lie in the original strict
plateau-complement gap. The translated interval contains the moved
saddle at its center, and the accretive Gaussian estimate is uniform.
This is the contour deformation used in the plateau germ; it does
not leave a complex shifted saddle off the integration contour.

All remaining first-half sectors and the complete complementary
contour have fixed exponential gaps uniformly on sufficiently small
ordinary-color disks, by their original complex-color theorems.
Intersect these finitely many disks. For a fixed \(\gamma>0\),
write the exact whole kernel as its plateau integral plus remainder:
\[
 Z_{34,N}=\kappa_N^3N^{-3/2}\mathcal A_w e^{N\mathcal W}
                         (1+O_{\rm hol}(N^{-1}))+R_N,
 \qquad |R_N|\le CN^b e^{N(M-\gamma)}.                 \tag{23}
\]
Shrink once more so \(\Re\mathcal W\ge M-\gamma/2\)
and \(|\mathcal A_w|\) has a positive lower bound. The normalized
remainder is then holomorphic and
\[
 \left|\frac{R_N}
 {\kappa_N^3N^{-3/2}\mathcal A_w e^{N\mathcal W}}\right|
       \le CN^{b+3/2}e^{-N\gamma/2}.                  \tag{24}
\]
This proves the whole holomorphic packet on a neighborhood of a
closed smaller bidisk. Nested Cauchy estimates give all fixed
normalized mixed jets there. It is the original ordinary polynomial,
so these are its actual ordinary derivatives, not derivatives of a
different Fourier interpolant.

Set \(\Phi(\boldsymbol\theta)=
\mathcal W(-2\cos\theta_L,-2\cos\theta_R)\), and compose
the coefficient in the same way. This proves (4), including separate
evenness. The exact power is
\(N^2N^{-1}N^{-2}N^{-1/2}=N^{-3/2}\).

The [original geometric boundary germ](research_mixed_geometric_boundary_germ.md),
equation (20), identifies the actual complete-color Hessian:
\[
 \Phi''(0,0)=-\frac1{2\pi}
   \begin{pmatrix}\tan(\pi u_L)&0\\0&\tan(\pi u_R)\end{pmatrix},
 \qquad \Re\tan(\pi u_L),\Re\tan(\pi u_R)>0.          \tag{25}
\]
The outside wires retain their original regular chamber
\(0<\Re u_L,u_R<1/2\); explicitly
\(\Re\tan\pi u=\sin(2\pi\Re u)/
[\cosh(2\pi\Im u)+\cos(2\pi\Re u)]>0\).
Continuity supplies (5) on a fixed smaller closed bidisk and a
neighborhood thereof. The absolute action and its original imaginary
constant are unchanged.

## 7. A two-variable polynomial strip reset

Here is the short maximum-principle argument which upgrades (21),
together with (4)--(5), to (6). It is useful to state it for the
whole two-variable polynomial, so no assumption about a distant
complex-color packet is needed.

Let \(z_1=e^{i\theta_L}\), \(z_2=e^{i\theta_R}\).
The angular polynomial is a Laurent polynomial of degrees at most
\(D_N=N-1\) in each variable, invariant under each
\(z_j\mapsto z_j^{-1}\). For \(|z_j|\le1\), apply the
bidisk maximum principle to
\[
 z_1^{D_N}z_2^{D_N}
       e^{-Nc_r(z_1+z_2)} K_{34,N}(z_1,z_2).
                                                               \tag{26}
\]
On the distinguished boundary its modulus is at most
\(CN^b e^{N(M-2c_r)}\), by (21). Each inversion symmetry
handles the opposite half-strip independently. Therefore
\[
 |K_{34,N}(x+iy,v+iw)|\le CN^b
 e^{N\{M-c_r[D(x)+D(v)]+(1+c_r)(|y|+|w|)\}}.         \tag{27}
\]
For instance when \(y\ge0\), the exact disk estimate uses
\(D_Ny+Nc_r(e^{-y}-1)\cos x\le N(1+c_r)y\).
The same computation applies independently to the second variable.

Choose a fixed small \(r>0\) inside the bidisk in (4)--(5).
When \(|x|,|v|\le r\), Taylor's formula, the vanishing gradient
at zero, the negative real Hessian, and a fixed bound on all second
derivatives give
\[
 \Re\Phi((x,v)+i(y,w))
 \le M-\frac\kappa4(x^2+v^2)+B_0(y^2+w^2)             \tag{28}
\]
for sufficiently small \(|y|,|w|\). One may see this by first
integrating the real Hessian along the real segment, bounding the
linear imaginary displacement by
\(L\sqrt{x^2+v^2}\sqrt{y^2+w^2}\), and applying Young's
inequality. The remaining imaginary quadratic term is bounded by
a fixed multiple of \(y^2+w^2\). Equation (4) then gives (6)
in this region, after reducing the angular constant.

If at least one of \(|x|,|v|\) is at least \(r\), then
\(D(x)+D(v)\ge D(r)>0\). Choose the strip width so that
\(2(1+c_r)h\le c_rD(r)/2\). Equation (27) then retains
at least half the real angular loss. Combining this with (28),
and taking \(c_0\le\min(c_r/2,\kappa/4)\), proves (6).

For fixed ordinary derivatives at real colors, an ordinary-color
circle of radius \(N^{-2}\) changes each inverse-cosine angle
by \(O(N^{-1})\), uniformly even at the quadratic branch points.
Apply (27) on those circles and Cauchy's formula. The angular
exponents change by only \(O(1)\), and a fixed derivative costs
a polynomial factor. This gives all actual first normals and all
fixed higher ordinary mixed jets without dividing any finite source
zero or replacing a Hermite observation by physical point values.

## 8. The resulting insertion input and its limits

Equations (4)--(6), the degree bound following (1), and the exact
source normalization verify the analytic hypotheses of the finite
two-boundary closure theorem for this internal ordinary \((3,4)\)
block. Its two calibrated outside estimates, relative to
\(\Phi(0,u)\) and \(\Phi(s,0)\), then follow from that theorem's
Section 2. The original quotient-algebra trace and all first normals
remain the ones in (1); no new adapter is introduced here.

This result supplies the previously missing all-real and complex-strip
requirements for this one complete block. Any use in a long-power
word must still use the exact finite contraction order, original
marked interfaces, and the thresholds stipulated by the closure
theorem. It neither proves short-step invariance nor settles the
finite-exception problem for arbitrary short clusters.
