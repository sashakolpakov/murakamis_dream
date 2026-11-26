# The incoming corner on the half-grid side and selected near-half interval

Private research proof candidate, 8 November 2026. This note bounds the
original incoming corner as its exact oriented union. It covers the full
half-grid vertical, both grid-correction horizontals, and the selected
top interval from \(9/20\) to \(1/2\). Every physical row, canonical
current, Fourier forcing term and original measure is retained.
No mathematical numerical evaluation or frozen-source edit is used.

## 1. Actual reference, original source and claim

Use the actual complete words in powers three and four beginning
\(343\), of length \(m\ge5\), and the unchanged reference and planes in
[the right half-grid horizontal](research_mixed_next_three_half_grid_incoming_right_horizontal.md).
Write
\[
\begin{gathered}
(a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3),\qquad
h_a=\Im a_*,\quad h_s=\Im s_*,\quad c=\Im y_*,\\
h_t=\Im t_*,\quad h_z=\Im z_*,\quad H=1/100,\qquad
-.072<h_a<0,\quad -.102<h_s,c<-.001,\\
-.03<h_t,h_z<.02,\qquad 7/10<R_*=e^{2\pi c}<41/50,\\
z=u+ih_z,\qquad 3/10\le u\le39/100,\qquad -2\le w\le2 .
\end{gathered}                                                     \tag{1}
\]
All height correlations remain actual. Keep the original affine plane
\(\Lambda_{123}(z)\), and put \(B_*=B_U(1/2)\). There is no outgoing
halfweight for the next own-three kernel.

For \(D=N-1,\ r=e^{-2\pi i/N}\), retain
\[
P_j=(r;r)_j,\quad p_j(V)=(rV;r)_j,\qquad
C_{\beta,N}(V,W)=\sum_{j=0}^{D}
                 \frac{V^{-j}p_j(V)p_j(W)}{P_j^{2+\beta}} .
\tag{2}
\]
The full forced degree-\(D\) polynomial has
\(d_N(r^b)=P_b^{-1}\). Set \(X=e^{-2\pi ia},Y=e^{-2\pi iy},Z=e^{-2\pi iz}\).
For \(a_L=1/2+ih_a\), use the paths oriented from \(a_L\) to \(7/10\):
\[
\begin{split}
\Gamma_C&=[a_L,1/2]\cup[1/2,7/10],\\
\widetilde\Gamma_C&=[a_L,7/10+ih_a]\cup[7/10+ih_a,7/10],\\
F_N^C(w,Y)&=N\int_{\Gamma_C}U_{0,N}(w,X)C_{1,N}(X,Y)\,da,\\
K_N^C(y)&=\frac{N F_N^C(w,Y)d_N(Y)C_{0,N}(Y,Z)}{1-Y^N},\\
M_N&=\lceil N/2\rceil,\qquad L_N=(M_N-\tfrac12)/N,\\
V_N^C&=i\int_c^H K_N^C(L_N+ih)\,dh,\\
J_N^{C,\mathrm{grid}}
&=\int_{L_N}^{1/2}K_N^C(q+ic)\,dq
  -\int_{L_N}^{1/2}K_N^C(q+iH)\,dq .
\end{split}                                                       \tag{3}
\]
There are two original factors \(N\). The grid term is zero at odd
levels; neither of its even-level integrals is discarded for shortness.

**Theorem.** Uniformly in (1), at both parities and all sufficiently
large levels,
\[
\begin{aligned}
|F_N^C(w,Y)d_N(Y)Y^{-N}C_{0,N}(Y,Z)|
&\le CN^B e^{N\{\Lambda_{123}(z)-1/4000\}},
&&y=q+iH,\quad 9/20\le q\le1/2,\\
|K_N^C(L_N+ih)|
&\le CN^B e^{N\{\Lambda_{123}(z)-10^{-12}\}},
&&c\le h\le H .
\end{aligned}                                                     \tag{4}
\]
The same rate bounds each grid horizontal in (3) pointwise. Hence
\[
|V_N^C|+|J_N^{C,\mathrm{grid}}|
\le CN^{B'}e^{N\{\Lambda_{123}(z)-10^{-12}\}}.                 \tag{5}
\]
The top \(K\)-integral over any subinterval of \([9/20,1/2]+iH\),
and the upper grid horizontal separately, retain the stronger
gap \(1/4000\). These are complete contributions of the original
corner union. No bound on either old incoming side separately, outside
jets, or coherent middle insertion is claimed.

## 2. Complete cap, next profiles and actual calibration

The cap-only statements in
[the original corner transport, (18),(21)--(22)](research_mixed_next_selected_incoming_corner_union.md)
give
\[
|U_{0,N}(w,X)|\le C_\tau N^{B_\tau}e^{N(B_*+\tau)}
\quad(a\in\widetilde\Gamma_C),\qquad B_*>7/8 .
\tag{6}
\]
The right column actually has rate \(3907/4500<B_*\).
The independent complete absolute cap bound on the full rectangle is
\[
|U_{0,N}(w,X)|\le C_\tau N^{B_\tau}e^{N(1549/1500+\tau)} .
\tag{7}
\]
Its full-radius coefficient and true-end proof is traced in
[selected-left corner, Section 2](research_mixed_next_three_selected_left_incoming_corner.md).
Neither bound depends on the present shared target.

Keep \(g'(\zeta)=\operatorname{Log}(1-e^{-2\pi i\zeta})\), its original
primitive constant, and
\[
Q_\beta(v;b_1,b_2)=g(b_1+v)+g(b_2+v)-(2+\beta)g(v)
                  -g(b_1)-g(b_2)+2\pi i b_1v .
\tag{8}
\]
The next controlling family \(\mathscr P_0(y,z)\) is
\[
\begin{split}
&\Re Q_0(v+ih_t;y,z),\quad 3/20\le v\le1/2,\\
&\Re Q_0(3/20;y,z),\quad \Re Q_0(1/2;y,z),\quad
L_0(h)=2\pi(-h)_++2\pi(h_z)_+ .
\end{split}                                                       \tag{9}
\]
At the selected height retain both weight rates
\[
W_{\rm fac}(y)=-\Re g(y)-2\pi H,\qquad W_{\rm force}(y)=0 .
\tag{10}
\]
The complete next reduction in
[half-grid bounded prefix, Section 4](research_mixed_next_three_half_grid_bounded_prefix.md)
reduces every physical row and current to (9), independently of its
preceding factor. Its cuts are \(3/20,1/2\), main height \(h_t\),
alias heights \(-1/5,8\), four weighted sides and two unweighted
joins. Its entire upper block reduces positively to half and last
by [transformed upper rows, Lemma 1](research_mixed_transformed_upper_rows.md).
The actual output range and all intermediate shared heights satisfy
that lemma's full-square hypotheses.

For every first fixed main index \(1/20\le v\le1/2\), at height
\(h_s\), and for its real half profile, the proof in
[right half-grid horizontal, Sections 3--4](research_mixed_next_three_half_grid_incoming_right_horizontal.md)
gives at \(a_L\), before any coherent summation,
\[
\begin{aligned}
B_*+\phi_1+\phi_0+W_\nu
&<\Lambda_{123}(z)-1/1000,
&&y=q+iH,\quad 9/20\le q\le1/2,\\
B_*+\phi_1+\phi_0-\Re g(y)
&<\Lambda_{123}(z)-10^{-10},
&&y=q+ic,\quad 9/20\le q\le1/2,\\
B_*+\phi_1+\phi_0
&<\Lambda_{123}(z)-10^{-10},
&&y=1/2+ih,\quad c\le h\le H .
\end{aligned}                                                     \tag{11}
\]
Here \(\phi_0\) ranges over (9); the top line has both choices (10).
The bottom line is its equation (23), proved by convexity of each
fixed joint profile, not of an eliminated critical action. The
second line is its original lower calibration and decreasing
\(q\)-transport before setting \(q=1/2\).
The added first indices below \(1/8\) increase to \(1/8\), since
both shifted cosines are nonpositive and the own square is below \(3/5\).

For raw groups use
[half-grid bounded prefix, Theorem 1](research_mixed_next_three_half_grid_bounded_prefix.md).
Any preceding factor of rate at most
\[
B_f=77/50+\pi/50                                             \tag{12}
\]
is paid against the complete next factor and the appropriate forced
weight/paired denominator on the needed contour pieces, with gap
\(1/1000\). All raw bounds below are strictly below (12), so their
finite tolerances are absorbed before this attachment.

## 3. The original root on the closed near-half rectangle

This section concerns the geometric rectangle
\[
a=x-i\eta,\quad 1/2\le x\le7/10,\quad 0\le\eta\le9/125,
\qquad y=q+ih,\quad9/20\le q\le1/2,\quad c\le h\le H .
\tag{13}
\]
It does not assert a source bound on all interior points of this
two-dimensional shared rectangle. Write \(R=|Y|\); then
\[
5/8<|X|\le1,\quad \Re X<0,\quad \Im X\ge0,\qquad
7/10<R<16/15,\quad \Re Y<0 .
\tag{14}
\]
For \(q<1/2\), these parameters lie in the original
[algebraic transport domain](research_mixed_four_conditional_algebraic_transport_domain.md).
There is a unique simple upper root of
\[
v(v-X)(v-Y)=X(v-1)^3,\qquad
(1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0 .                             \tag{15}
\]
Its original lift \(s_c=\operatorname{Log}v/(2\pi i)\), distinguished
from the fixed reference \(s_*\) in (1), satisfies
\[
Q_{1,s}(s_c;a,y)=0,\quad 0<\Re s_c<1-x,\qquad
\omega=\frac{v-X}{1-X},\quad \Im\omega>0,\quad |\omega|<1 .
\tag{16}
\]
In particular \(\Theta(a,y)=Q_1(s_c;a,y)\) has
\(\Theta_a=\operatorname{Log}\omega\).

These assertions extend to \(q=1/2,\ Y=-R\).
For \(\Im X>0\), a real root would obey
\[
\Im Y=-\frac{(v-1)^3\Im X}{|v-X|^2}.                         \tag{17}
\]
The exceptional values \(0,1,X\) are not roots, so (17) excludes
every real root at this boundary. For \(X=-\rho\), (15) is
\[
(1+\rho)v^3+(R-2\rho)v^2+\rho(3+R)v-\rho .
\]
One quarter of its derivative discriminant is
\[
R^2-(7\rho+3\rho^2)R-5\rho^2-9\rho
<(16/15)^2-45/8<0 .                                        \tag{18}
\]
It has one simple real root in \((0,1)\), and a simple conjugate
pair. Approach \(Y=-R\) from \(\Im Y<0\). No root escapes or
crosses the real axis, so the upper count one persists, including
multiplicity. The incoming-ray and multiplier exclusions remain
strict: they contradict either \(\Re Y<1\) or \(\Im Y\le0\).
Thus (16), with its original zero lift, holds on (13).
Every shifted critical real coordinate remains in \((0,1)\).

Sufficient uniform radius guards are
\[
                         2/5<|v|<2 .                       \tag{19}
\]
For \(|v|\ge2\), the radii in
\(\operatorname{Log}(1-X/v)+\operatorname{Log}(1-Y/v)
-3\operatorname{Log}(1-1/v)+2\pi ia\)
are at most \(1/2,4/7,1/2\). Its imaginary part exceeds
\(\pi-2\pi/3-\pi/5>0\), using the original
\(\arcsin(4/7)<\pi/5\) witness, contradicting (16).

For \(|v|=\rho\le2/5,\ \arg v=\phi\), the exact original
strip factorization is
\[
Q_{1,s}=\operatorname{Log}v+\operatorname{Log}Y-i\pi
 +\operatorname{Log}(1-v/X)+\operatorname{Log}(1-v/Y)
 -3\operatorname{Log}(1-v).                                 \tag{20}
\]
At \(q=1/2\), use \(\arg Y=-\pi\). As proved in
[negative-height branch, (18)--(20)](research_mixed_conditional_negative_height_branch.md),
the core argument
\[
B_\rho(\phi)=\phi+3\Arg(1-\rho e^{-i\phi}),\qquad
B_\rho'(\phi)=
\frac{1+\rho\cos\phi-2\rho^2}{1-2\rho\cos\phi+\rho^2}>0
\]
is at most \(\pi\). Now \(|v/X|<16/25<1/\sqrt2\) and
\(|v/Y|<4/7\), so the two remaining arguments in (20) have
sum less than \(\pi/4+\pi/5\). Since \(\arg Y\le-9\pi/10\),
\(\Im Q_{1,s}<-9\pi/20<0\), another contradiction.
This checks the two radius hypotheses for the original factorization
on the present domain; no new integer lift is selected.

The real critical index obeys
\[
                         1/20<\Re s_c<1-x .                \tag{21}
\]
Suppose \(0<b=\Re s_c\le1/20\), and put
\(U=e^{2\pi\Im s_c}=|v|^{-1}\in(1/2,5/2)\).
Its own square is strictly below
\[
D_0=1+U^2-19U/10,\qquad 0<D_0\le U,\quad U\le5/2 .
\]
Indeed \(U+U^{-1}\le29/10\) on this interval, by convexity and
its endpoint values. Here \(\cos(2\pi b)>19/20\),
\(x+b\in[1/2,3/4]\), and \(q+b\in[9/20,11/20]\). Thus
\[
\begin{split}
|T-Ue^{-2\pi i(x+b)}|^2&\ge1+U^2=D_0+19U/10,\quad T=e^{2\pi\eta},\\
|1-RUe^{-2\pi i(q+b)}|^2
&>1+\frac{49}{100}U^2+\frac{133}{100}U
 >\frac{49}{100}D_0+2U .
\end{split}
\]
The cosine witnesses follow from
\(\cos(\pi/10)>1-(11/35)^2/2>19/20\).
The exact squared force is therefore greater than
\[
\frac{(D_0+19U/10)(49D_0/100+2U)}{D_0^3}
\ge\frac{29}{10}\frac{249}{100}\frac25
=\frac{7221}{2500}>1,                                      \tag{22}
\]
contradicting stationarity. Compactness makes the guards uniform.
No old \(2/25\) index bound or selected-left root count was imported.

For \(1/20\le b<1-x\), both shifted real coordinates \(x+b,q+b\)
lie in \([1/2,1)\). At every private height \(\sigma\),
\[
\Re Q_{1,ss}(b+i\sigma;a,y)
\le-3\pi\,\frac{\sin(2\pi b)}
                  {\cosh(2\pi\sigma)-\cos(2\pi b)}<0 .       \tag{23}
\]
This follows from the signs of both shifted cotangents. It makes
no assertion of convexity for the eliminated critical action.

## 4. Physical groups and both real cuts

Use first cuts \(b=1/20,1/2\), with the exact partition
\[
A_N=\lfloor N/20\rfloor+1,\quad
\ell_N=(A_N-\tfrac12)/N,\quad b_N=(M_N-\tfrac12)/N;
\qquad [0,A_N),\ [A_N,M_N),\ [M_N,N).                         \tag{24}
\]
The complete low positive block has whole-\(Y\)-disk rate \(169/400\).
Together with (7) this is
\[
1549/1500+169/400=77/50-509/6000 .                            \tag{25}
\]
Each row has \(Y\)-degree at most \(D\); radial growth adds at most
\(\log_+R\le\pi/50\). The real lower cut obeys the same bound
directly, adding only \(b\log_+R\). Both fit (12).
The complete first last rate is
\[
L_1(h)=2\pi\eta+2\pi h_+,\qquad
77/50-1549/1500-18\pi/125>23/420 .                            \tag{26}
\]
It too fits the raw attachment after the complete cap (7).

At the real half, the incoming-dependent part is exactly
\[
\int_0^{1/2}\log|T-e^{-2\pi i(x+s)}|\,ds,\qquad T=e^{2\pi\eta}.
\tag{27}
\]
Its derivative in \(x\) is negative on \([1/2,7/10]\), since
the endpoint cosines are \(-\cos2\pi x>0>\cos2\pi x\).
The integrand increases with \(T\ge1\). Thus (27) decreases
on both replacement segments, giving
\[
E_1(1/2;a,y)\le E_1(1/2;a_L,y)
\quad(a\in\widetilde\Gamma_C).                              \tag{28}
\]
Equations (6),(11) pay this half alternative with every next
profile. Integrable zeros use continuous integral limits.

Every first upper physical row reduces positively to this half
or to (26), even beyond the old input square. Put
\(\Phi(v)=E_1(1-v)-L_1\). Exact reflection, retaining both means, is
\[
\Phi(v)=3J(v)
 -\int_0^v\log|T-e^{-2\pi i(x-s)}|\,ds
 -\int_0^v\log|1-Re^{-2\pi i(q-s)}|\,ds .                     \tag{29}
\]
The first integral is nonnegative by the original complementary-arc
lemma. The centered second arc is at least \(2J(v/2)\) for
\(R\le1\), and at least \(v\log R+2J(v/2)\) for \(R\ge1\),
after folding its radius. The centered-arc monotonicity and
exact duplication bound in
[whole-disk upper block, Sections 2--3](research_mixed_conditional_lower_output_upper_block.md)
give
\[
\Phi(v)\le3J(v)-2J(v/2)\le0\qquad(0\le v\le1/3).              \tag{30}
\]
For \(1/4\le v\le1/2\), the two omitted-arc logarithms are
less than \(24/25,3/4\), respectively, since \(T\le8/5,R<16/15\).
The exact exponential witnesses in
[selected-left corner, (18)--(19)](research_mixed_next_three_selected_left_incoming_corner.md)
and its convex envelope give
\[
\Phi(v)-\Phi(1/2)
\le\frac{171}{100}(1/2-v)+3J(v)\le0 .                         \tag{31}
\]
At \(v=1/4\) the envelope is less than \(-9/4400\); it vanishes
at \(1/2\). These overlapping intervals exhaust the upper half.
The original zero-safe physical products give the positive finite
comparison with arbitrarily small tolerances, including the even
half row, odd first upper row, \(j=D\), and every zero.
The last alternative uses (26); the half uses (28),(11).

## 5. All six weighted middle currents

Keep the original canonical interpolant
\[
T_N(s;a,y)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                            E_N(a)E_N(y)E_N(s)^3 .           \tag{32}
\]
At \(s=j/N\) it is the literal row. Its continuous upper rate is
\[
\begin{split}
\widehat R(v,\sigma)&=\mathfrak p(a+s)+
 \Re\{g(y+s)-3g(s)-g(a)-g(y)+2\pi ias\},\quad s=v+i\sigma,\\
\mathfrak p(\zeta)&=
\begin{cases}
\Re g(\zeta),&0<\Re\zeta\le1,\\
\Re g(\zeta-1)+2\pi(\Im\zeta)_+,&1\le\Re\zeta<2 .
\end{cases}
\end{split}                                                       \tag{33}
\]
At \(q=v=1/2\), the outgoing term uses its continuous boundary
value. The exact identity
\(\Pi_N(\zeta+1)=(1-e^{-2\pi iN\zeta})\Pi_N(\zeta)\)
retains both period terms. The original global numerator and
reciprocal midpoint bounds give
\[
|T_N(v+i\sigma)|\le C_\tau N^{B_\tau}
                         e^{N\{\widehat R(v,\sigma)+\tau\}} .
\tag{34}
\]
Every denominator has real argument strictly between zero and one.
There is no new seam symbol for \(y\), nor any division by a
period factor at \(\eta=0\).

Put \(J_{\rm eff}=-\partial_\sigma\widehat R\). On (13),
\[
J_{\rm eff}\le19\pi/10\quad(\sigma\le0),\qquad
J_{\rm eff}\ge-19\pi/10\quad(\sigma\ge0),\quad1/20\le v\le1/2 .
\tag{35}
\]
Before the incoming wall and below zero, both shifted arguments
are nonpositive, and the own argument is nonnegative. Hence
\(J_{\rm eff}\le2\pi x\). After that wall \(v\ge3/10\);
the reduced incoming argument is at most \(\pi/2\), the outgoing
one still nonpositive, and there is no period derivative below zero.
This proves the first bound.

Above zero before the wall, the original argument bounds give
\[
J_{\rm eff}/\pi\ge
(1-2x-2v)+(1-2q-2v)-3(1-2v)+2x
=-1+2v-2q\ge-19/10 .                                        \tag{36}
\]
After the wall and for \(0\le\sigma\le\eta\), its incoming
argument is nonnegative with no period term; the bound is stronger.
For \(\sigma\ge\eta\), put \(r_0=x+v-1\in[0,1/5]\).
The reduced incoming radius is at least one, giving argument
at least \(\pi(1/2-r_0)\). With the exact period subtraction
\(-2\pi\), this yields
\[
J_{\rm eff}/\pi\ge-\frac52+3v+x-2q
\ge-\frac32+2v-2q\ge-19/10 .                                 \tag{37}
\]
The middle inequality uses \(x+v\ge1\). At the outgoing wall
\(q=v=1/2\), both one-sided arguments satisfy the same bounds.

Choose first alias heights \(-8,+8\).
Each weighted vertical rate \(\widehat R-2\pi|\sigma|\)
decreases away from its real cut with reserve at least \(\pi/10\).
The four weighted half-sides are paid by the real lower and upper
alternatives. For either horizontal, (35) gives loss at least
\(4\pi/5>12/5\) from its real index. The real-row ceiling is
\[
\widehat R(v,0)<(7/4)v-3J(v)\le11/8 .
\]
After the complete cap (7), either horizontal has preceding rate
less than
\[
1549/1500+11/8-12/5=23/3000<B_f .                            \tag{38}
\]
The complete next attachment therefore pays both alias integrals.

The exact cotangent identity now leaves
\[
C_{1,N}(X,Y)=N\int_{\ell_N}^{b_N}T_N(s;a,y)\,ds+\mathcal E_N .
\tag{39}
\]
The error consists of all low and upper physical rows, two
horizontal aliases and four weighted sides. Every term is paid
after attachment of the literal outside source, with its own
finite tolerance. No unweighted join has yet been included.

## 6. Critical line, both joins and local Gaussian

By (19)--(23), the prewall line at the original critical height
\(h_*=\Im s_c\) increases to \(s_c\) and decreases after it.
The root is strictly between both actual half grids for large \(N\).
Put \(U=e^{2\pi h_*}\in(1/2,5/2)\) and \(T=e^{2\pi\eta}\le8/5\).
The postwall squared force is exactly
\[
\exp(2\partial_v\widehat R)=
\frac{|T-Ue^{-2\pi i(x+v)}|^2
      |1-RUe^{-2\pi i(q+v)}|^2}
     {|1-Ue^{-2\pi iv}|^6},\qquad1-x\le v\le1/2 .             \tag{40}
\]
The period contribution is independent of \(v\).
For every \(U\ge1\), the difference polynomial in
[original corner deformation, (15)](research_mixed_next_lower_left_corner_gaussian_deformation.md)
is bounded below by \(138/175\). Its hypotheses are only
\(R<8/7,\ x+v\in[1,6/5],\ v\ge3/10,\ T\le8/5\); it has no
upper restriction \(U\le2\).
For \(1/2\le U\le1\), use \(1+RU\le(31/30)(1+U)\).
The two exact differences in
[selected-left corner, (29)--(30)](research_mixed_next_three_selected_left_incoming_corner.md)
increase and are positive, with values \(961/20000\) and
\(18641/10000\) at \(U=1/2\). They split \(v\) at \(2/5\) and
use no outgoing angular restriction. Thus the complete postwall
line decreases. The whole critical-height upper rate has its
unique maximum \(M(a,y)=\Re\Theta(a,y)\) at the regular root,
with a uniform strict loss outside a fixed critical chart.

Deform the middle integral with both full sides:
\[
\begin{split}
N\int_{\ell_N}^{b_N}T_N(s)\,ds
={}&N\int_{\ell_N}^{\ell_N+ih_*}T_N(s)\,ds\\
&+N\int_{\ell_N+ih_*}^{b_N+ih_*}T_N(s)\,ds
+N\int_{b_N+ih_*}^{b_N}T_N(s)\,ds .
\end{split}                                                       \tag{41}
\]
The original interpolant is holomorphic across its numerator
walls; there are no added residues. The lower join is vertically
convex by (23) at every height between zero and \(h_*\).
Its endpoints are the paid real low cut and a strict-loss main point.

At the limiting half cut,
\[
\partial_\sigma\widehat R(1/2,\sigma)
\le-2\pi(x-q)\le0\quad(\sigma<\eta),\qquad
\partial_\sigma\widehat R(1/2,\sigma)\ge0\quad(\sigma>\eta).
\tag{42}
\]
Below \(\eta\), the reduced incoming argument is nonnegative,
the outgoing argument is at least \(-2\pi q\), and the own
argument is zero. Above \(\eta\), the incoming argument is at
most \(\pi-2\pi(x-1/2)\), the outgoing one is nonpositive, and
the period term adds \(2\pi\) to the height derivative.
These prove (42), including its weak case \(x=q=1/2\).
When \(q=1/2\), the outgoing numerator is also on its wall.
Its one-sided arguments are zero or \(-\pi\); its upward
height-derivative jump preserves the same inequalities.
The half join is therefore bounded by its endpoints, paid by
(28),(11) and the strict-loss main endpoint.

Only the fixed prewall critical chart requires a nonzero symbol.
All its arguments have real parts in \((0,1)\), and
\[
\begin{split}
T_N(s)&=N^{-3/2}b(s;a,y)e^{NQ_1(s;a,y)}
                            (1+O_{\rm hol}(N^{-1})),\\
b(s;a,y)&=\frac{a_0(a+s)a_0(y+s)}
                  {a_0(s)^3a_0(a)a_0(y)},\qquad
a_0(z)=\sqrt{2\sin\pi z}\,e^{-i\pi z/2}.
\end{split}                                                       \tag{43}
\]
The increasing Gaussian contribution is
\[
N^{-1}\frac{\sqrt{2\pi}\,b(s_c;a,y)}
                 {\sqrt{-Q_{1,ss}(s_c;a,y)}}e^{N\Theta(a,y)}
+O(N^{-2})e^{N\Theta(a,y)},                                   \tag{44}
\]
with nonzero coefficient and original square root. Its power is
\(N\,N^{-3/2}N^{-1/2}=N^{-1}\).
This local statement is not a whole-kernel relative packet:
the real-end alternatives remain separately attached source errors.

## 7. Critical-action calibration and exact incoming cancellation

At \(a_L\), every fixed profile
\(\sigma\mapsto\widehat R(v,\sigma)\), \(1/20\le v\le1/2\),
is convex by the two cotangent signs in (23). Upward derivative
jumps at either wall preserve convexity. Thus
\[
f(\sigma)=\max_{1/20\le v\le1/2}\widehat R(v,\sigma)
\]
is convex. At \(\sigma=h_*\) its unique maximum is the interior
critical index, and \(f'(h_*)=0\) by the original zero lift.
Consequently
\[
M(a_L,y)=f(h_*)\le f(h_s).                                   \tag{45}
\]
Apply (11) with each next profile still fixed. This replaces
\(\phi_1\) by \(M(a_L,y)\) in every stated profile bound.
No estimate is extracted from the value of a signed sum.

The original multiplier in (16) gives
\[
\partial_x M=\log|\omega|<0,\qquad
\partial_{\Im a}M=-\Arg\omega<0 .                            \tag{46}
\]
Hence \(M(a,y)\le M(a_L,y)\) on \(\widetilde\Gamma_C\).
The complete cap (6), same-coordinate next reduction (9), and
(45)--(46) pay (44) and all strict-loss main errors. The real
join alternatives use (25),(28); Sections 4--5 pay every other
physical and weighted group.

At \(q=1/2\), these profile bounds precede the full forced \(d_N\).
Its retained Fourier estimate is
\[
|d_N(Y)|\le C_\tau N^B
 e^{N\{\max(-\Re g(y),\,2\pi(\Im y)_+)+\tau\}} .              \tag{47}
\]
Exactly on the shared half grid,
\[
\Re g(L_N+ih)=O(N^{-1}),\qquad
Y^N=-e^{2\pi Nh},\qquad |1-Y^N|=1+e^{2\pi Nh}.               \tag{48}
\]
Thus the forced quotient has arbitrarily small exponential cost,
including height zero. On the lower grid horizontal use
\(|1-Y^N|\ge1-R_*^N\) and the second line of (11).
On the upper grid horizontal and the whole top interval use
\[
\frac{d_N(Y)}{1-Y^N}
=-\frac{d_N(Y)Y^{-N}}{1-Y^{-N}},                              \tag{49}
\]
whose denominator is bounded away from zero. The first line
of (11) retains both branches (10). No homogeneous approximation
to the forced polynomial is used.

All private cut shifts and \(L_N-1/2\) are \(O(N^{-1})\).
The original integrated-log upper envelopes are uniformly
continuous on the bounded retained rectangles, with wall cost
\(O((\log N)/N)\), hence only polynomial finite cost.
No all-height sign assertion outside the limiting cut strip is
needed for its half-grid excursion. Both numerator zeros,
including their simultaneous half-period limit, use (34).
Choose all tolerances inside the smallest reserve in (11),
then weaken to \(10^{-12}\) on the vertical and lower horizontal.
On the top, every nonraw controlling profile has reserve \(1/1000\),
as does each complete raw attachment after its preceding strict
allowance. The same proof therefore retains the stronger finite
gap \(1/4000\) there. This proves the pointwise attached bounds
on the replacement path.

Finally the literal incoming integrand is holomorphic in \(a\).
Its finite Laurent powers of \(X=e^{-2\pi ia}\) introduce no
finite-\(a\) singularity. Cauchy's theorem gives exactly
\[
N\int_{\Gamma_C}U_{0,N}C_{1,N}\,da
=N\int_{\widetilde\Gamma_C}U_{0,N}C_{1,N}\,da .                \tag{50}
\]
The right replacement side has \(da=i\,d(\Im a)\).
The shared measures in (3) remain upward \(i\,dh\) and increasing
\(dq\), with the lower-minus-upper grid signs unchanged.
Bounded lengths and both factors \(N\) add only polynomial costs.
Equations (47)--(50) prove (4)--(5), and the top \(K\)-integral
statement with its exact minus sign.

The old incoming pieces are bounded only in their exact union.
This supplies their half-grid and near-half-top contributions,
without replacing the old filter or either Fourier coefficient.
Other first incoming pieces and the coherent middle insertion
retain their separate source obligations.

