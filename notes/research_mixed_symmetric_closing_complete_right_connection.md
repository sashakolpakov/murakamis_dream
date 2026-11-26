# The complete right connection in the symmetric closing trace

Private written finite-source deduction, 10 November 2026. The
original full inner trace has a strict closing-budget upper bound
on the right outer hyperbola. Combining it with the descending
column and the controlled low and far paths bounds the literal
right current in the original two-current identity.

Both inner traces, all Newton rows and Hermite data, the original
prefactors, and both complete double-pole sampling denominators
are retained. The conclusion concerns this right current; no
whole-knot or arbitrary-short-filling theorem is asserted.
No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, test, or frozen-source edit is used.

## 1. Original functions, two distinct cutoffs, and the claim

Put \(D=N-1\), \(m=\lfloor N/2\rfloor\), \(U=m-1\), and retain
\[
 \begin{gathered}
 c_j=2\cos((2j+1)\pi/N),\qquad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 e_j(x)=S_j^{-2}\prod_{\nu<j}(c_\nu-x),\\
 \mathcal K_N(w,x)=\sum_{j=0}^{D}e_j(w)e_j(x),\qquad
 \mathcal K_N^<(w,x)=\sum_{j=0}^{U}e_j(w)e_j(x),\\
 \phi_N(f)=(-1)^{N-1}N^2[x^{N-1}]
          \operatorname{rem}_{2T_N(x/2)+2}f .
 \end{gathered}                                                   \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial and \(R_N\) is the
original crossing element. Define the three exact full traces
\[
 \begin{aligned}
 Q_N(w,u)&=\phi_N[R_N^3\mathcal K_N(w,x)
                             \mathcal K_N(x,-2\cos u)],\\
 Q_N^<(w,u)&=\phi_N[R_N^3\mathcal K_N(w,x)
                             \mathcal K_N^<(x,-2\cos u)],\\
 Q_N^{<<}(w,u)&=\phi_N[R_N^3\mathcal K_N^<(w,x)
                             \mathcal K_N^<(x,-2\cos u)] .
 \end{aligned}                                                    \tag{2}
\]
Only the edges indicated in (2) are shortened. The trace itself
is never changed to an observation at distinct roots.

Use the exact multipliers
\[
 \eta_N=(-1)^{N-1},\qquad
 C_{N,n}=e^{\pi i n(N-1)^2/(4N)},\qquad
 W_N(z)=\frac{e^{-iNz}}{(1-\eta_Ne^{-iNz})^2}.                    \tag{3}
\]
For the inner variable let
\[
 g_N(t;w,u)=\sin t\,
       \mathcal K_N^<(w,-2\cos t)\mathcal K_N^<(-2\cos t,-2\cos u)
                         e^{3iNt^2/(4\pi)}.                    \tag{4}
\]
For the outer variable and \(\mathbf w=(w_L,w_R)\), retain
\[
 F_N(u;\mathbf w)=Q_N(w_L,u)Q_N(w_R,u),\qquad
 G_N(u;\mathbf w)=\sin u\,F_N(u;\mathbf w)e^{iNu^2/\pi}.         \tag{5}
\]
In particular the two factors in (5) are the full functions
in the first line of (2).

The original geometric point and action are
\[
 \begin{gathered}
 u_g=\beta_g-iK_g,\qquad 0<\beta_g<\pi/2,\qquad
 17/30<K_g<7/10,\\
 \Xi(u)=2S_3(0,u)+iu^2/\pi-iu,\qquad M_g=\Re\Xi(u_g)>163/50,\\
 d=\pi/2-\beta_g>0,\qquad
 u(\beta)=\beta-iK(\beta),\quad K(\beta)=\frac{\pi K_g}{2\beta},
                         \quad\pi/2\le\beta\le2\pi/3,\\
 c_{\rm out}(u)=(2\beta/\pi-1)K=K_g-K,\qquad
 B(u)=\frac{M_g-c_{\rm out}(u)}2,\\
 \mu=\min\left\{\frac{d^2}{16\pi},\frac{451}{240000},
                                      \frac1{400}\right\}>0 .
 \end{gathered}                                                   \tag{6}
\]
These are the original cubic branch and calibrated action. The
floor in (6) is the complete action-floor theorem bound, with
the original primitive constant.

The inner cutoff and its fixed small height will be denoted
\[
 \Theta_N=\pi-\frac{2\pi\lfloor N/4000\rfloor}{N},\qquad
                         0<h_{\rm in}\le1/2000 .                \tag{7}
\]
They are those of the fixed-low inner trace identity. The
different, outer cutoff and height from the two-current identity are
\[
 a_N=\pi-\frac{2\pi\lfloor N/400\rfloor}{N},\qquad
                         0<h_{\rm out}\le1/1000 .               \tag{8}
\]
Both are genuine midpoint cutoffs: \(e^{iN\Theta_N}
=e^{iNa_N}=-\eta_N\). No replacement of one cutoff by the other
will be made.

**Theorem.** Uniformly on the hyperbola in (6), at both level
parities and all sufficiently large \(N\),
\[
 \sup_{w\in[-2,2]}|Q_N(w,u)|
                  \le C e^{N(B(u)-\mu/2)}.                     \tag{9}
\]
There is a fixed complex neighborhood \(\mathcal E\) of
\([-2,2]\) on which
\[
                   |Q_N(w,u)|\le C e^{N(B(u)-\mu/4)}.           \tag{10}
\]
Every fixed ordinary incoming derivative has the latter bound
on a smaller neighborhood.

Let the original right current be exactly
\[
 \begin{split}
 \Gamma_{R,N}:&\quad
       \pi/2-iK_g\longrightarrow a_N-iK_g
                              \longrightarrow a_N-ih_{\rm out},\\
 \mathcal C_{R,N}(\mathbf w)
    &=-\frac{N^2C_{N,4}}{\pi i}
           \int_{\Gamma_{R,N}}G_N(u;\mathbf w)W_N(u)\,du .
 \end{split}                                                    \tag{11}
\]
On a fixed ordinary bidisk about \((-2,-2)\), there is
\(\epsilon_R>0\) such that
\[
             |\mathcal C_{R,N}(\mathbf w)|
                          \le C e^{N(M_g-\epsilon_R)}.          \tag{12}
\]
The same holds for every fixed mixed ordinary incoming derivative
on smaller bidisks. If \(\Theta(\mathbf w)\) denotes the original
local outer stationary action in the two-current identity, the
bidisk can be chosen so that
\[
 |\mathcal C_{R,N}(\mathbf w)|
                \le C e^{N(\Re\Theta(\mathbf w)-\epsilon_R/2)} .
                                                                    \tag{13}
\]
All neighborhoods and positive gaps are fixed before \(N\).

## 2. The exact inner trace and its finite boundary corrections

The derivative-sampling identity is algebraic in the coefficients
of the polynomial
\(\mathcal K_N^<(w,x)\mathcal K_N^<(x,-2\cos u)\), whose degree
in \(x\) is \(2U<N\). Its original lower-contour form is
\[
 Q_N^{<<}(w,u)=
 -\frac{N^2C_{N,3}}{\pi i}\int_{\Gamma_N}
                 g_N(t;w,u)W_N(t)\,dt
       +\mathcal V_N(w,u)+\mathcal R_N^{\rm far}(w,u),           \tag{14}
\]
for any piecewise smooth path in the open lower half-plane from
\(-\Theta_N-ih_{\rm in}\) to \(\Theta_N-ih_{\rm in}\).
In the notation \(\tau_j=2\pi(D/2-j)/N\), its retained corrections
are
\[
 \begin{split}
 \mathcal R_N^{\rm far}
   &=\eta_NC_{N,3}
       \sum_{\substack{0\le j\le D\\|\tau_j|\ge\Theta_N}}
                         \partial_tg_N(\tau_j;w,u),\\
 \mathcal V_N
   &=\frac{\eta_NN^2C_{N,3}}{\pi}
       \int_{-h_{\rm in}}^{h_{\rm in}}
       \frac{g_N(\Theta_N+iv;w,u)}
                                  {4\cosh^2(Nv/2)}\,dv .
 \end{split}                                                    \tag{15}
\]
The second line combines the two original short midpoint columns,
with their exact signs. The first line includes the first-normal
terms at the removed double nodes. The odd central simple node
remains in the integral in (14); it is not a removed far sample.

For completeness, the identity is unchanged at arbitrary incoming
\(w\): both kernels in (4) are even in \(t\), so \(g_N\) is odd,
while \(W_N\) is even. The original reflection combining the
upper and lower sampling contours and their endpoint columns
therefore applies without any restriction \(w=-2\).
The poles of \(W_N\) are on the real axis. Lower-half-plane
deformations of \(\Gamma_N\) preserve (14) without residues.

Section 5 of the low-and-far inner theorem proves, uniformly on
(6) and for every real incoming color, that the absolute sample
sum and absolute vertical integral in (15) have rate at most
\(B(u)-1/20\). Its proof first uses the all-index real Newton
bound and the exact outgoing degree \(U\) to give the far source
rate \(2b_2+K/2+1/1000\). The Markov bound controls the first
normal; a fixed filled ellipse controls the two midpoint columns.
Their total attached rate is less than
\[
 \frac{91}{60}+\frac3{2000},\qquad
 \frac{321}{200}
   -\left(\frac{91}{60}+\frac3{2000}\right)-\frac1{20}
                         =\frac{221}{6000}>0 .                 \tag{16}
\]
Thus (14)--(15) retain and estimate precisely the finite corrections,
with the original \(N^2\), for both parities.

We will repeatedly use the all-real incoming slit estimate
\[
 \sup_{w\in[-2,2]}
 |\mathcal K_N^<(w,-2\cos t)|
       \le C_\tau e^{N(\Re\psi(t,0)+\tau)}                      \tag{17}
\]
on each fixed compact first-angle path in this proof, for every
\(\tau>0\). This is Corollary 3 of the slit theorem, obtained from
the exact both-parity cardinal interpolation. Its action has
the original complete constant. It is an upper bound, and
does not assert a relative packet for variable \(w\).
The first-angle sets stay a fixed distance from \(\pm\pi\),
with heights at most one. Their spectral images are compact
subsets of \(\mathbb C\setminus[2,\infty)\); negative first
angles use the same source on the conjugate spectral compact.

## 3. A complete inner path and both source sectors

Write \(t_*(u)=a_*(u)-iH_*(u)\). The wider cubic theorem gives
\[
                 1<a_*<2\pi/3,\qquad 1/10<H_*<1 .              \tag{18}
\]
Set \(h_*=7/10\) and \(A_0=2\pi/3\). Choose \(\Gamma_N\) in
(14) as the following concatenation, in this order.

1. The negative connection
   \(-\Theta_N-ih_{\rm in}\to-\Theta_N-ih_*\to-ih_*\).
2. If \(H_*>h_*\), the axis join
   \(-ih_*\to-iH_*\); otherwise this piece is empty.
3. The positive saddle path from
   \(-i\max(H_*,h_*)\) through \(t_*\) to \(A_0-iH_R\),
   specified below.
4. The vertical \(A_0-iH_R\to A_0-i/10\).
5. The low and far path
   \(A_0-i/10\to5\pi/6-i/10\to
                     \Theta_N-i/10\to\Theta_N-ih_{\rm in}\).

If \(H_*\ge h_*\), piece 3 is horizontal from the axis to \(t_*\),
then \(t=t_*+(1+i)\sigma\), with
\[
       0\le\sigma\le\min\{H_*-h_*,A_0-a_*\}.
                                                                    \tag{19}
\]
If the diagonal first reaches height \(h_*\), continue horizontally
to the right face. Thus \(H_R=\max\{h_*,H_*+a_*-A_0\}\).
If \(H_*<h_*\), first follow the horizontal at height \(h_*\)
to \(t_*+(1+i)(H_*-h_*)\), then that diagonal to \(t_*\), and
then the horizontal to \(A_0-iH_*\). Its left joining angle is
positive by (18), and \(H_R=H_*\). All these paths have uniformly
bounded lengths and remain at fixed positive inner heights.

For these positive pieces define exactly
\[
 \begin{split}
 \Phi(t,u)&=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it,\\
 s(u)&=\Re S_3(0,u)=\Re\Phi(t_*,u),\\
 E(a,H;u)&=\Re\psi(a-iH,0)-H/2+3aH/(2\pi)+K/2
                         =J(a,H)+K/2 .
 \end{split}                                                    \tag{20}
\]
The complete second-short-edge envelope is the maximum of its
geometric rate \(\Re\psi(t,u)\) and its physical endpoint rate
\((H+K)/2\), with arbitrary positive tolerance. After (17) and
the original crossing and full \(W_N(t)\), these give precisely
\(\Re\Phi(t,u)\) and \(E(a,H;u)\). The edge theorem's
reciprocal-factorial interpolation includes both complete rational
aliases, both external columns, the two added unweighted caps,
and both endpoint row groups through the original cutoff \(U\).
None is dropped when using this envelope.

At the initial positive axis, the uniform source is supplied by
the axis-join proof: the outgoing leg retains its strictly positive
imaginary numerator, its simple wire saddle and connected side
sublevels. It supplies the small positive-angle charts too, rather
than taking an \(a_L\)-dependent envelope constant to a limit.
Every part of piece 3 near angle zero has depth at least \(h_*\);
if \(H_*<h_*\), its lower-depth pieces start at an angle greater
than \(2/5\). Thus the positive-angle and axis sources together
give uniform estimates on all of piece 3.

The negative-connection and axis-join theorems bound the absolute
currents of pieces 1 and 2 by
\[
                         C e^{N(B(u)-1/50)}                    \tag{21}
\]
for all real incoming \(w\). They include the negative central
horizontal, the far negative horizontal, and the full midpoint
vertical. In particular no unestimated interval across the
imaginary axis remains.

The positive-path theorem proves on piece 3
\[
                \Re\Phi(t,u)\le s(u),                         \tag{22}
\]
using the original inequalities
\(\Re\Phi_{tt}<-1/(4\pi)\), \(\Im\Phi_{tt}>1/(2\pi)\).
Its low endpoint sector is \(E<123/100+K/2\).
The critical-endpoint reduction and payment give, on the entire
high part,
\[
 \begin{split}
 E_{\rm high}(u)&\le
             \max\{E(a_*,H_*;u),123/100+K/2\},\\
 J(a_*,H_*)&<32/25-451/240000,\\
 E(a_*,H_*;u)&<B(u)-451/240000 .
 \end{split}                                                    \tag{23}
\]
For the last line retain the exact identity
\(2E(a_*,H_*;u)+c_{\rm out}=2J(a_*,H_*)+K_g\) and use
\(M_g>163/50\), \(K_g<7/10\). The low sector has the larger gap
\[
 123/100+K/2+c_{\rm out}/2
                 <123/100+7/20=79/50<M_g/2-1/20 .              \tag{24}
\]
No endpoint rate is replaced by a geometric critical value.

The original outer hyperbola estimate is
\[
 \Re\Xi(u(\beta))
 \le M_g-\frac{d^2}{8\pi}
              -\frac{d}{4\pi}(\beta-\pi/2).
                                                                    \tag{25}
\]
Since \(2s(u)+c_{\rm out}(u)=\Re\Xi(u)\), it implies
\[
                           s(u)\le B(u)-d^2/(16\pi).           \tag{26}
\]
Equations (22)--(26) bound both finite sectors on piece 3
by \(B(u)-\mu\), before its arbitrary rate tolerances.

On piece 4 the strict-edge and vertical theorem gives the
four candidate rates
\[
       s(u),\quad 123/100+K/2,\quad E_{\rm high}(u),
                       R_{\rm row}(u),                       \tag{27}
\]
where
\[
 R_{\rm row}(u)=\Re\psi(A_0-i/10,0)
          +m_{\rm row}(A_0-i/10)+m_{\rm row}(u).                \tag{28}
\]
Here the complete shortened-row profile is
\[
 m_{\rm row}(z)=\max_{0\le y\le1/2}
 \left\{\int_0^y\log|2\cos(2\pi x)+2\cos z|\,dx-2J(y)\right\},
 \qquad J(y)=\int_0^y\log(2\sin\pi x)\,dx .                    \tag{28a}
\]
This statement keeps the whole finite edge source. In particular
its comparison
\[
 \Re\psi(t,u)\le
       \max\{(H+K)/2,m_{\rm row}(t)+m_{\rm row}(u)\}             \tag{29}
\]
was proved by the nonzero original packet on the strict region
\(\Re\psi>(H+K)/2\), followed by exact finite row Cauchy--Schwarz;
on the complementary region the endpoint term already bounds it.
It is not inferred from an upper envelope alone.
Convexity of both rates in the vertical height then reduces
piece 4 to (27).

The low-and-far inner proof, equation (14), gives the pointwise
lower-end comparison
\[
 R_{\rm row}(u)+c_{\rm out}(u)/2
 <321/200-\frac{2261}{554400}
 <M_g/2-\frac1{300}.
                                                                    \tag{30}
\]
Thus all four rates in (27) are at most \(B(u)-\mu\).
Replacing the first shortened kernel by its all-real form
(17) preserves the estimates on pieces 3 and 4: these proofs
use its upper exponent only. All remaining factors are the
unchanged original sine, crossing, and \(W_N\).

Finally the low-and-far theorem bounds the entire absolute
current on piece 5 by \(C e^{N(B(u)-1/400)}\) for real \(w\).
This includes the full low horizontal, the far horizontal,
and the original right midpoint vertical. Together with
(15)--(16) it also retains every finite trace correction.

## 4. Full-edge restoration and ordinary incoming neighborhoods

Choose the total arbitrary rate tolerance on each of pieces
3 and 4 smaller than \(\mu/8\), using (17) and the second-edge
envelope with smaller individual tolerances. Absorb their
polynomial costs, including the original \(N^2/\pi\), in a
further \(\mu/8\). The other pieces have the explicit absolute
bounds just stated. The finite sum in (14) therefore gives,
with room to weaken the gap,
\[
 \sup_{w\in[-2,2]}|Q_N^{<<}(w,u)|
                   \le C e^{N(B(u)-\mu/2)}.                   \tag{31}
\]
All constants are uniform on the compact outer hyperbola.

Restore both full edges by their exact traced differences
\[
       Q_N-Q_N^{<<}=(Q_N-Q_N^<)+(Q_N^<-Q_N^{<<}).               \tag{32}
\]
The right-edge restoration theorem applies to the entire
independent domain \(|\Re u|\le2\pi/3\), \(|\Im u|\le7/10\).
It proves, for all real incoming colors,
\[
 |Q_N-Q_N^{<<}|
       \le CN^A e^{N E_{\rm del}(K)},\qquad
 E_{\rm del}(K)=2b_2+K/2+K^2/(4\pi).                           \tag{33}
\]
The incoming radical sum is the original
\(\sum_{r=0}^{m-1}e_{D-r}(w)
 \sum_{a=0}^{r}b_{ra}R_N(c_a)^3F_{a,N}(-2\cos u)\),
with \(|b_{ra}|\le2\).
At odd levels the separate \(e_m(w)\) interpolation includes
its original simple-node value
\(R_N(-2)^3\mathcal K_N^<(-2,-2\cos u)\).
The outgoing difference likewise retains its whole radical
sum and the odd middle/simple-node term. These are the exact
full Hermite contractions; (32) is not a pointwise equality
between full and shortened edges.

The exact attached comparison is
\[
 2E_{\rm del}(K)+c_{\rm out}
 =4b_2+K^2/(2\pi)+K_g<623/200,
 \qquad E_{\rm del}(K)<B(u)-19/400 .                            \tag{34}
\]
It is stronger than needed in (31). After polynomial
absorption, (32)--(34) prove (9), with both complete traces
and all their original normal data restored.

For fixed \(u\), \(Q_N(w,u)\) is an ordinary polynomial of
degree at most \(D<N\). Expand it in Chebyshev polynomials
on the entire interval \([-2,2]\). Every coefficient is at
most twice its real-interval supremum. On the fixed filled
ellipse of logarithmic parameter \(\mu/16\), the degree costs
at most \(N\mu/16\); its coefficient count can be absorbed
using another \(\mu/16\). Applying this to (9) leaves a gap
at least \(3\mu/8\), hence proves (10).
Cauchy's formula on a smaller ellipse gives every fixed
ordinary incoming derivative with the same weaker gap.
No relative variable-color Gaussian packet is asserted.

On the outer hyperbola the full multiplier obeys
\[
 |e^{iNu^2/\pi}W_N(u)|
 \le\frac{e^{N c_{\rm out}(u)}}{(1-e^{-N K_{\min}})^2},
                         \qquad K_{\min}=3K_g/4>0 .            \tag{35}
\]
The product of (10) for the two independent incoming colors
has, after (35), rate \(M_g-\mu/2\). Its sine and path length
are bounded. Absorb the original outer \(N^2/\pi\) and fixed
constants in a further \(\mu/4\). The complete hyperbola
therefore satisfies
\[
 \frac{N^2}{\pi}\int_{u([\pi/2,2\pi/3])}
             |G_N(u;\mathbf w)W_N(u)|\,|du|
                          \le C e^{N(M_g-\mu/4)} .             \tag{36}
\]
Both occurrences of the original double denominator, in
(14) and (35), have been retained.

## 5. Joining to the literal outer right endpoint

Set \(h_\ell=1/10000\). Replace the path in (11) by the
following concatenation, with the displayed orientations:
\[
 \begin{array}{ll}
 \mathrm{(i)}&
 u(\beta),\quad \pi/2\le\beta\le2\pi/3;\\
 \mathrm{(ii)}&
 2\pi/3-3iK_g/4\ \longrightarrow\ 2\pi/3-ih_\ell;\\
 \mathrm{(iii)}&
 2\pi/3-ih_\ell\ \longrightarrow\ 4\pi/5-ih_\ell;\\
 \mathrm{(iv)}&
 4\pi/5-ih_\ell\ \longrightarrow\ 4\pi/5-i/100;\\
 \mathrm{(v)}&
 4\pi/5-i/100\ \longrightarrow\ a_N-i/100
                                      \longrightarrow a_N-ih_{\rm out}.
 \end{array}                                                    \tag{37}
\]
Piece (ii) is bounded by the complete descending-column
theorem with a fixed gap \(\epsilon_{\rm col}>0\).
That theorem supplies the finite inner bound at outgoing
heights down to \(h_\ell\); no phase-only extrapolation is
used here.
Piece (iii) is bounded by the coupled-column low-outer theorem
with gap \(1/400\). It retains every row of the two full
functions in (5), on fixed ordinary incoming disks.

The same low-outer theorem records the eligible continuation
on piece (iv). More explicitly the earlier far-right proof
has the uniform rate bound
\[
 2(b_2+\lambda_*)+2m_0(a)+(1+2a/\pi)h
 \le\frac{301}{108}+\frac9{25}+\frac3{100}
                       =\frac{8578}{2700}                      \tag{38}
\]
for \(a\ge4\pi/5\), \(0<h\le1/100\), before its arbitrary
incoming allowance. Its complete Newton vector and complete
column estimates remain valid on piece (iv). Its denominator
now has the fixed lower height \(h_\ell\), in place of
\(h_{\rm out}\); this changes only a bounded constant.
The same original tolerance allocation gives gap \(1/50\).
Piece (v) is exactly the earlier far-right path and has that
gap as well. Its endpoint is the original \(a_N-ih_{\rm out}\),
not the inner endpoint \(\Theta_N-ih_{\rm in}\).

Intersect the finitely many fixed incoming neighborhoods
from (36)--(38) and the descending-column theorem. Their
absolute integrals, with the original \(N^2/\pi\), have a
common positive rate gap; for example one may take any
\[
 0<\epsilon_R<
       \min\{\mu/4,\epsilon_{\rm col},1/400,1/50\}.              \tag{39}
\]
Absorb their finite number into the uniform constant.
The integrand \(G_N(u;\mathbf w)W_N(u)\) is holomorphic in
the open lower half-plane: the kernels are ordinary
polynomials in \(-2\cos u\), the sine and crossing are entire,
and all sampling poles are real. That half-plane is simply
connected. Hence (37), with the same two endpoints as (11),
has exactly the same signed integral as \(\Gamma_{R,N}\).
This proves (12), retaining the original scalar
\(-N^2C_{N,4}/(\pi i)\).

For fixed \(N\) the current is holomorphic in both ordinary
incoming variables. The absolute bounds on the larger
bidisks, followed by Cauchy's formula, give the asserted
mixed derivative estimates. Finally \(\Theta(\mathbf w)\)
is the unchanged holomorphic local action from the
two-current identity, with \(\Re\Theta(-2,-2)=M_g\).
Shrink the bidisk so that
\(|\Re\Theta(\mathbf w)-M_g|<\epsilon_R/4\).
Then (12) implies (13), with room in its stated gap.

This bounds the actual right current in that identity.
Its separately identified left current and local coefficient
are not replaced or re-proved here. No theorem for the whole
closed knot, for additional attachments, or for arbitrary
fixed short partial fillings is inferred.

## Frozen direct sources

All sources below were read in these exact versions. Their
finite-source scopes, rather than only their phase conclusions,
are used in the indicated steps.

| Source | SHA-256 |
|---|---|
| research_mixed_symmetric_closing_two_remaining_currents.md | 15c28d0004bfcdebd26e55dfe48419aa54d14c563c95e33e1d32ef5b1ac6cad8 |
| research_mixed_symmetric_closing_fixed_low_remainder.md | 03accd56435b7c00be36b89a5e2ffcee70ae84027ad918a6b3b1dca204825ab0 |
| research_mixed_next_inner_three_far_samples_and_verticals.md | 15a38af35c84cacc940f11a7c22675748d5f9da7fc19424573116dcdbf77c685 |
| research_mixed_next_first_short_edge_slit_plane_bound.md | efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b |
| research_mixed_symmetric_closing_wider_negative_inner_connection.md | 3567e939040545b1551a69e33564704c8e3b0540e3bd31b8b1c021d35460b7f3 |
| research_mixed_symmetric_closing_center_height_join.md | 943a40bd6addadc889b6a4b2629619d4ea6bb780fc5f9e6b25e67431a7ffa65a |
| research_mixed_symmetric_closing_wider_positive_saddle_path.md | 6e362aec94c3ae00bab51e7d4c1d6928a6c4aff8fdcdbd68a475b7e9346d7e8c |
| research_mixed_symmetric_closing_critical_endpoint_reduction.md | 480ba4e4990679a79d16fcc7c16af953ae96ca7afaa85e766baaf145a1c519b1 |
| research_mixed_symmetric_closing_critical_endpoint_payment.md | 57e2d4a3d246397dce0c4c66a797c3bc452f353aa509d0f7ebef1b0d18b2a247 |
| research_mixed_symmetric_closing_action_floor_163.md | f0bfaf90d7e331adf1df3ba59980dea76ebc8347b7244d2b52c4e1c692b5f825 |
| research_mixed_symmetric_closing_wider_edge_packet_and_vertical.md | 5f4ed6a63f91c8ecd683aaf8a9b83233793248e6efa52dee20e7b74a77bafc26 |
| research_mixed_symmetric_closing_right_inner_low_and_far.md | 0bd7207c07dadcf7a448af7ad89e1df71925a824f81dabe696a0cdadbf3fb39e |
| research_mixed_symmetric_closing_right_edge_restoration.md | 7537a3c34ca00b665ae8dd95eb130cede3f6972389b7ff5ed8382737cec4fac8 |
| research_mixed_symmetric_closing_wider_phase_hyperbola.md | e9eadfc87f49741345f33ac73f717a4e1698ccaca5c3ffb824d48bd0444a8cbb |
| research_mixed_symmetric_closing_right_descending_column.md | 3096dde75fc21fcb1e84ac8dce0e652e2271c50780c889a82bdee0cd83b53001 |
| research_mixed_symmetric_closing_coupled_column_and_low_outer.md | f1a8fb899e580c3953136aaa7aeb86530e2c51d25aaecba28e66b16183083b51 |
| research_mixed_symmetric_closing_earlier_far_right_connection.md | 9b62082201e99c73371c19cd82f7279fb3a4a57cecff2135306815f3bc3ad416 |
