# The complete selected first four/three source on the early interval

Private written proof, 10 November 2026. The original selected first
four/three product has a strict gap on the whole early fixed-height
rectangle. The central main-current comparison is a separate input.
Here the other cap currents, both ordinary real cuts, every physical
ordinary row, and all ordinary joins and aliases are paid without
changing the source or its selected monomial.

## 1. Source, reference and statement

Fix an actual positive three/four open word of length at least three
beginning with four and three. All reference variables, logarithmic
lifts and additive constants are those of the
[selected finite-source reduction](research_mixed_selected_four_three_finite_reduction.md).
In particular write
\[
 \Im e_*=h_e\in[-.051,-.019],\quad
 \Im s_*=h_s\in[-.065,.068],\quad
 \Im b_*=d\in[-.065,.068].
\tag{1}
\]
Set
\[
 H=7/625,\qquad a=x+iH,\quad b=z+id,\qquad
 x\in[1/10,11/50],\quad z\in P=[11/50,9/20].
\tag{2}
\]
The positive target height is selected; it is not the negative first
height of the actual reference. The actual private heights in (1)
are kept fixed.

For \(q_N=e^{-2\pi i/N}\), put
\[
 P_j=(q_N;q_N)_j,\quad p_j(X)=(q_NX;q_N)_j,\quad
 X=e^{-2\pi ia},\quad Y=e^{-2\pi ib}.
\]
The exact product is
\[
\begin{split}
 \mathcal K_N(w;X,Y)&=U_{1,N}(w,X)C_{0,N}(X,Y)d_N(X)X^{-N},\\
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
                   \frac{H_N(w,q_N^{-i})p_i(X)}{P_i^2},\\
 C_{0,N}(X,Y)&=\sum_{j=0}^{N-1}R_{j,N},\qquad
 R_{j,N}=\frac{X^{-j}p_j(X)p_j(Y)}{P_j^2}.
\end{split}
\tag{3}
\]
Here \(H_N\) is the complete original endpoint coefficient. The
first-coordinate Fourier weight is whole. There is no outgoing
type-three halfweight at \(Y\), no additional scalar, and no division
by a finite Fourier factor.

Retain the bare phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea-g(e),\\
 Q(s;a,b)&=g(s+a)+g(s+b)-2g(s)-g(a)-g(b)+2\pi ias,\\
 \mathcal F&=\Psi+Q-g(a),\quad
 M=\Re\mathcal F(e_*,s_*;a_*,b_*),\quad
 p=\mathcal F_b(e_*,s_*;a_*,b_*),\\
 \Lambda(z)&=M+\Re p\,(z-\Re b_*).
\end{split}
\tag{4}
\]
The two upper rates for the single complete selected Fourier object
are
\[
 W(x)=-\Re g(a)-2\pi H,\qquad W_{\rm force}=0.
\tag{5}
\]
The scalar comparison (26) of the
[early central theorem](research_mixed_selected_four_three_early_central.md)
gives \(W>3/40\) on (2). Thus retaining \(W\) as the larger
upper rate pays both alternatives; it is not an exact splitting of
the finite polynomial.

**Theorem 1.** For every \(\tau>0\), both parities and every
fixed ordinary-color derivative order \(k\), there are a fixed
ordinary-color disk about \(-2\) and constants such that
\[
 |\partial_w^k\mathcal K_N(w;X,Y)|
 \le C_{\tau,k}N^{A_{\tau,k}}
       \exp N\{\Lambda(z)-1/2000+\tau\}
\tag{6}
\]
uniformly on (2) for integers \(N\ge2\), on a smaller disk for the
derivatives. The same
zeroth-order rate holds for the whole real ordinary-color interval.
In particular a fixed positive part of the displayed gap may be
reserved before choosing the disks and all finite-source tolerances.

This is a complete two-factor upper bound at the stated fixed
selected height. It does not estimate height-changing outer joins,
other early selections, the rest of the first period, or an arbitrary
whole open word.

## 2. Complete cap source and the plateau calibrations

Use the five original bare cap profiles
\[
\begin{array}{ll}
 A_0=\max_{.27\le u\le.49}\Re\Psi(u+ih_e,a),&
 A_L=\Re\Psi(.27,a),\quad A_R=\Re\Psi(.49,a),\\
 A_-=\max_u\Re\Psi(u-.055i,a)-.11\pi,&
 A_+=\max_u\Re\Psi(u+.04i,a)-.08\pi.
\end{array}
\tag{7}
\]
The independent rectangle in the
[complete fixed-height cap theorem](research_mixed_cap_early_fixed_height_full_source.md)
contains (2). Its type-four allowance is identically zero. Its
complete cap bound is therefore the maximum of (7) and the separate
true-end ceiling
\[
 E_*={3\over5}+2\pi H+{\log4\over100}<{69\over100}.
\tag{8}
\]
The inequality uses \(2\pi H<44/625\) and \(\log4<7/5\).
This source includes the two real cuts, both zero-mode joins, both
horizontal aliases and all vertical alias halves, both physical
tails, and every true endpoint row. Its zero-mode density is \(+N\).
It is uniform on the whole real ordinary-color interval; its angular
loss can be dropped in this upper estimate. No endpoint packet is
extrapolated to a true index end.

For the ordinary profiles put
\[
 B_0=\max_{.15\le v\le.5}\Re Q(v+ih_s;a,b),\quad
 B_L=\Re Q(.15;a,b),\quad B_R=\Re Q(.5;a,b),\quad
 B_1=2\pi d_+.
\tag{9}
\]
At \(x_0=11/50\), the
[complete selected plateau theorem](research_mixed_selected_four_three_full_product.md)
and its individual profile proofs give
\[
 A_i+B_j+W\le\Lambda(z)-1/2000
 \quad(i\in\{0,L,R,-,+\},\ j\in\{0,L,R\}),
\tag{10}
\]
and the [selected last-row theorem](research_mixed_selected_four_three_last_rows.md)
gives the larger gap \(3/100\) for every \(A_i+B_1+W\).
These are the individual current inequalities in those proofs,
not consequences inferred from a small signed whole kernel.
The finite reduction also proves, at this same face,
\[
                         A_0(x_0)>199/250.
\tag{11}
\]
Thus the true-end ceiling (8) is below that main profile by more
than \(53/500\).

On the whole early rectangle the separate
[early central theorem](research_mixed_selected_four_three_early_central.md)
already proves
\[
                         A_0+B_0+W<\Lambda(z)-1/500.
\tag{12}
\]
It retains every main private point and both Fourier alternatives.
The rest of the proof supplies the other finite pieces of (3).

## 3. Both cap aliases and the right cut reduce to the main cap

The canonical proof in
[selected cap-alias transport](research_mixed_selected_cap_alias_transport.md),
equations (2)--(12), depends on the private rectangle alone. Keep its
canonical \(u_c(e)\), with \(.17<\Re u_c<.28\),
\(\Im u_c>0\), and \(.01<\Re(e-u_c)<.32\).
For \(e=u+i\xi\), the exact lifted identity is
\[
 \Im\Psi_e=\mathcal A(u+x,\xi+H)
                    +\pi-2\Arg(1-D_c),\qquad
 \Arg(1-D_c)<\pi(1-u),
\tag{13}
\]
where \(D_c\) is that source's canonical algebraic quantity and
\(\mathcal A(t,h)=\arg(1-e^{2\pi h-2\pi it})\).
This identity remains on the original lift because every new
\(e+a\) real part is in \([.37,.71]\).
Its elementary radius-argument proof now gives
\[
 -.46\pi<\Im\Psi_e<.82\pi,\qquad
             \Im\Psi_e>-.29\pi\quad(\xi\le0).
\tag{14}
\]
Indeed if \(u+x\ge1/2\), the first lower bound is
\(-2\pi x\ge-.44\pi\); otherwise it is
\(\pi(2u-1)\ge-.46\pi\). For the improved lower bound
at \(\xi\le0\), the two cases are
\(\pi(\Re u_c-2x)>-.27\pi\) and
\(\pi(2u+\Re u_c-1)>-.29\pi\).
For the upper bound use the original identity
\(\Psi_e=g'(e+a)-g'(e)-g'(e-u_c)+2\pi iu_c\).
The two subtracted arguments are positive, the last term contributes
less than \(.56\pi\), and the remaining positive argument is
at most \(.26\pi\).

Integrating (14) on the unchanged private height segments gives
\[
 A_-<A_0-\{.11-.82(.036)\}\pi<A_0-1/10,
\]
\[
 A_+<A_0-\{.08-.29(.051)-.46(.04)\}\pi<A_0-1/10.
\tag{15}
\]
Each comparison is pointwise in the same private real coordinate
before taking its maximum.

For the right cut use the original real trial \(e_0=2/5\).
The exact constants in
[the right-cut proof](research_mixed_selected_cap_right_rows.md)
are \(C>12/5\), \(T>\pi/8\). Since
\(r=e^{2\pi H}<43/40<10/9\), its numerator is below
\(19/9\), and hence
\[
 -\Re\Psi_e(.4,a)>26/203,\qquad
 \Im\Psi_e(.4,a)>
        \pi\{9/40-x+H\cot\pi(.4+x)\}>-\pi/500.
\tag{16}
\]
For the second inequality \(.4+x\le.62\) and
\(\cot(.62\pi)>-1/2\); use
\(\tan(.12\pi)\le(.12\pi)/(1-(.12\pi)^2/2)<1/2\).
The early cap Hessian gives horizontal concavity and vertical
convexity throughout both connecting segments. Its signed tangent
bounds therefore give
\[
 A_0-A_R\ge\Re\Psi(.4+ih_e,a)-\Re\Psi(.49,a)
 >{9\over100}{26\over203}-{51\over1000}{\pi\over500}
 >1/1250.
\tag{17}
\]
Thus it remains to pay the main cap, the left cut and the true ends
against the ordinary profiles.

## 4. Localization of the main cap maximum

We need only a private-real-coordinate restriction, not a new
critical point. Every main maximum in (7) lies in
\[
                              .27\le u\le.43.
\tag{18}
\]
Here is a proof at the positive selected height. Use the original
real/complex cap identities, also written in Lemma 2 of
[the first43 last-row calibration](research_mixed_first_four_three_true_last_row_calibration.md):
\[
 S''(e)=-\pi\cot\pi e
      -{2\pi\over\sin\pi e\sqrt{2-e^{-2\pi ie}}},
\quad
 \Psi_{ee}=S''+\pi\cot\pi(e+a)-\pi\cot\pi e+i\pi.
\tag{19}
\]
The square root is the original positive-real one. On the real
interval \([.43,.49]\), its written bounds give
\[
 (\Re S)'(.43)<-\log2+19/500+231\pi/2600,
 \qquad\sin(.43\pi)>39/40.
\tag{20}
\]
These follow from the original bridge derivative at \(.49\),
\(\cot\pi e<1/4\), \(\sin\pi e>39/40\), and
\(\Re(2-e^{-2\pi ie})>25/9\).
At real \(e=.43\), the exact derivative is
\[
 \Re\Psi_e=(\Re S)'(.43)
             +\log|\sin\pi(e+a)|-\log\sin\pi e+\pi H.
\]
Since \(H<.014\),
\(\log\cosh(\pi H)+\pi H<9/200\).
For example \(\pi H<11/250\) and
\(\log\cosh t\le t^2/2\) give
\(5621/125000<9/200\). Thus, using
\(\log(39/20)>16/25\) and \(231\pi/2600<7/25\),
\[
                         \Re\Psi_e(.43,a)<-277/1000.
\tag{21}
\]

For \(e=.43+i\xi\), \(-.051\le\xi\le0\), the
same original radical calculation gives \(\Im S''<\pi/10\).
More explicitly, its \(w_0=2-e^{2\pi\xi-.86\pi i}\)
obeys \(\Re w_0>64/25\),
\(0<\arg\sqrt{w_0}<11/145\), and
\(|\sin\pi e\sqrt{w_0}|>39/25\); the positive-argument
case costs at most \(110\pi/1131<\pi/10\), and the
other case has favorable sign. Also \(\Im\cot\pi e\ge0\).
Now \(\Re(e+a)\in[.53,.65]\). If its height is negative,
its magnitude is less than \(.041\), so
\[
 \Im\cot\pi(e+a)
  <{\sinh(.082\pi)\over3/2}<1/5.
\]
The denominator uses \(-\cos(2\pi\Re(e+a))>1/2\).
For the numerator, \(.082\pi<13/50\) and
\(\sinh t\le t/(1-t^2/6)\) give
\(\sinh(.082\pi)<3900/14831<27/100\).
At nonnegative height the cotangent imaginary part is nonpositive.
Consequently (19) gives \(\Im\Psi_{ee}<13\pi/10\).
Downward transport in \(\xi\) costs less than
\((51/1000)(13\pi/10)<21/100\) in (21), proving
\[
                   \Re\Psi_e(.43+ih_e,a)<-67/1000<-3/50.
\tag{22}
\]
Strict private horizontal concavity from the early cap Hessian
excludes every larger private real coordinate. This proves (18).

## 5. The real ordinary cuts and the left cap cut

Put
\[
 r=e^{2\pi H},\quad D=|1-r e^{-2\pi ix}|,\quad
 N_e=|1-rR e^{-2\pi i(u+x)}|,\quad R=e^{2\pi\Im e},
\]
\[
 N_s=|q-r e^{-2\pi i(v+x)}|,\qquad q=e^{-2\pi\Im s}.
\tag{23}
\]
Exact differentiation with the complete chirps and first weight gives
\[
 \partial_x\Re\{\Psi(e,a)+Q(s;a,b)-g(a)\}
                         =\log{N_eN_s\over D^3}.
\tag{24}
\]
The selected constant \(-2\pi H\) does not alter this derivative.
Throughout all private main and real-cut comparisons below,
\[
 1\le r<43/40,\quad q>13/20,\quad
 {D^2\over r}<{49\over30},\quad D^2<9/5,\quad
 {D^6\over r^2}<{5058907\over1080000}<{569\over120}.
\tag{25}
\]
Here \(r+r^{-1}\le3449/1720\) and
\(\cos(2\pi x)>14/75\); the last expression is
\((49/30)^3(43/40)\). The radius guards and the cosine bound
are the original written ones used in the early central proof.

For the main cap restricted by (18), \(R>18/25\), and
\(u+x\in[.37,.65]\). Since its cosine is below \(-7/12\),
\[
 N_e^2>1+324r^2/625+21r/25,\qquad
 {N_e^2\over r}>{40\over43}+{324\over625}+{21\over25}>9/4.
\tag{26}
\]
The trigonometric guard follows from
\(\cos^2(3\pi/10)=(5-\sqrt5)/8>11/32>49/144\).

At the ordinary half row \(s=.5\),
\[
 N_s^2\ge1+r^2+28r/75,\qquad {N_s^2\over r}\ge178/75.
\]
Thus the product in (24), after squaring and dividing by \(r^2\),
has numerator greater than \(267/50>569/120\).
The corresponding joint rate is strictly increasing with \(x\).
At the ordinary left cut
\(s=.15\), split into two ranges. For \(x\le.16\),
\(\cos2\pi x>1/2\) gives
\[
 {D^2\over r}<101/100,\qquad
 {D^6\over r^2}<(101/100)^3(43/40)<6/5,
 \qquad N_s^2/r\ge2.
\]
For \(x\ge.16\), \(s+x\in[.31,.37]\) gives
\(\cos2\pi(s+x)<-1/3\), so \(N_s^2/r>8/3\).
Together with (26), these give strict positivity in (24) on both
ranges. One witness for the latter cosine guard is
\[
 \cos(.38\pi)>1-18/25+54/625-324/78125>1/3;
\]
the alternating lower polynomial is decreasing up to \(6/5\),
and \(.38\pi<6/5\).
Transport to \(x_0\), then (10), pays
\[
                         A_0+B_L+W,\quad A_0+B_R+W
                         \le\Lambda(z)-1/2000.
\tag{27}
\]
The restricted private set in (18) is fixed, so taking its maximum
after this pointwise transport is legitimate.

For the left cap cut, \(e=.27\), one has
\(\cos2\pi(e+x)<-2/3\), hence
\[
 N_e^2>1+r^2+4r/3,\qquad N_e^2/r>10/3.
\tag{28}
\]
For clarity, \(.26\pi<33/40\), \(.26\pi>4/5\), and
the cosine series give
\(\cos(.26\pi)>1-1089/3200+32/1875-1/2000>2/3\).
For every \(v\in[.15,.5]\) and every ordinary private height
between \(-.065\) and \(.068\), one has
\(v+x\in[.25,.72]\), whose cosine is nonpositive. Therefore
\[
 N_s^2\ge r^2+169/400,\qquad N_s^2/r\ge569/400.
\tag{29}
\]
For the last inequality minimize
\(r+169/(400r)\) over \(r\ge1\).
Equations (25), (28)--(29) give numerator strictly greater than
\(569/120\) in the squared version of (24).
Pointwise transport to \(x_0\) and (10) now pay
\[
                   A_L+B_0+W,\quad A_L+B_L+W,\quad A_L+B_R+W
                   \le\Lambda(z)-1/2000.
\tag{30}
\]
The actual main height and both real-cut heights are all included.

## 6. Last rows and true cap ends

For a fixed main point in (18), and also for the left cap cut,
the exact last-profile derivative is
\[
           \partial_x\{\Re\Psi(e,a)+W+B_1\}
                              =\log(N_e/D^2)>-1/6.
\tag{31}
\]
Indeed (26), or the stronger (28), gives
\(N_e/D^2>45/(49\sqrt r)>300/343\), since
\(\sqrt r<21/20\). Now
\(\log(300/343)>-43/300>-1/6\).
Transport through a length at most \(3/25\) costs less than
\(1/50\). The old gap \(3/100\) at \(x_0\) therefore yields
\[
                         A_0+B_1+W, A_L+B_1+W
                                  <\Lambda(z)-1/100.
\tag{32}
\]
The other three cap profiles follow pointwise from (15), (17).

For the separate true-end cap ceiling and an ordinary main point
or real cut, the exact derivative instead is
\[
             \partial_x\{E_*+\Re Q(s;a,b)+W\}
                                  =\log(N_s/D^2)>-3/5.
\tag{33}
\]
Equations (25), (29) give \(N_s>7/6\), so
\(N_s/D^2>35/54>3/5\). The elementary exponential series
gives \(\log(3/5)>-3/5\).
Its total early cost is less than \(9/125\). At \(x_0\),
(8), (11) supply reserve greater than \(53/500\) against
the corresponding cap-main profile. After transport this reserve
is still greater than \(17/500\). Applying (10) proves all
true-end times ordinary-main or real-cut bounds with gap \(1/2000\).
For the last profile the derivative is \(-\log D>-3/10\):
\(D^2<9/5<e^{3/5}\). Its transport costs less than
\(9/250\), also smaller than \(53/500\). Thus
\[
                         E_*+B_j+W<\Lambda(z)-1/2000
                          \quad(j=0,L,R,1).
\tag{34}
\]
No true cap end is replaced by a main asymptotic. Only its literal
all-real-color ceiling is compared with the main profile at the
old, independently calibrated face.

Combining (12), (15), (17), (27), (30), (32), (34) proves the
complete finite profile list
\[
 A_i+B_j+W\le\Lambda(z)-1/2000,\qquad
 i\in\{0,L,R,-,+,*\},\quad j\in\{0,L,R,1\},
 \quad A_*=E_*.
\tag{35}
\]

## 7. Ordinary central currents: both signs of the private height

Keep the original conditional interpolation on the half-grid cuts
tending to \(.15,.5\), with horizontal aliases at \(\pm.2i\).
Every original factorial argument is regular: the real intervals for
\(s+a,s+b\) are \([.25,.72],[.37,.95]\). The exact
residue has the unchanged \(+N\) zero-mode density.

For \(s=v+iy\), \(.15\le v\le.5\), the original lift gives
\[
 I:=\Im Q_s=
 \mathcal A(v+x,y+H)+\mathcal A(v+z,y+d)
                     -2\mathcal A(v,y)+2\pi x.
\tag{36}
\]
For every finite height, the radius-angle inequalities imply
\[
                         -7\pi/5<I<24\pi/25.
\tag{37}
\]
Here \(x\le z\), so the two shifted real arguments have only
three ordered cases. Dividing by \(\pi\), their lower and upper
bounds are respectively
\[
\begin{array}{c|c|c}
 (v+x,v+z)&\text{lower}&\text{upper}\\ \hline
 (<1/2,<1/2)&-2+4v+2x\ge-6/5&2-4v-2z\le24/25\\
 (<1/2,\ge1/2)&-1+2v+2x-2z\ge-7/5&1-2v\le7/10\\
 (\ge1/2,\ge1/2)&-2z\ge-9/10&2x\le11/25.
\end{array}
\tag{38}
\]
Equality at a half argument causes no difficulty; finite radii give
the required strict global inequalities.
Comparing with the same point of the main line at \(h_s\) gives
\[
\begin{split}
 \Re Q(v-.2i)-.4\pi
 &<\Re Q(v+ih_s)-\{.4-(24/25)(.268)\}\pi,\\
 \Re Q(v+.2i)-.4\pi
 &<\Re Q(v+ih_s)-\{.4-(7/5)(.265)\}\pi.
\end{split}
\tag{39}
\]
The reserves are \(.14272\pi\) and \(.029\pi\), both
strictly positive. They are unchanged after adding any cap profile
and the entire selected weight. All weighted vertical alias halves
decrease away from their real-cut endpoints, because (37) lies
strictly inside \((-2\pi,2\pi)\).

The joint early-central Hessian proof applies for every ordinary
private height in \([-.065,.068]\). Holding its other variables
fixed shows \(\Re Q_{ss}<0\), hence vertical convexity on each
zero-mode join from zero to \(h_s\). Such a join is bounded by
its real-cut and main-line endpoints. Thus (35), (39) pay the whole
ordinary central inventory, including the two joins, two horizontal
aliases and four vertical alias halves, at either sign of \(h_s\).
The exact cap source (7)--(8) can be multiplied before each of these
bounds; a double alias is controlled at the same two private real
coordinates. No contour remainder is omitted.

## 8. Every ordinary physical row

For clarity the three exact blocks are
\[
 0\le j\le\lfloor3N/20\rfloor,\quad
 \lfloor3N/20\rfloor+1\le j\le\lceil N/2\rceil-1,\quad
 \lceil N/2\rceil\le j<N.
\tag{40}
\]
The middle block is Section 7. The exact ratio proof in
[low-row transport](research_mixed_first_attached_low_row_transport.md),
Lemma 1, holds on an independent height box containing (2).
For \(0<u\le1/5\) it gives ratio \(>e^{1/200}\).
Apply it only up to \(\lfloor3N/20\rfloor\): the whole
absolute low sum is below 201 times its final row. The uniform
finite-product bound gives that row rate \(B_L\), up to an
arbitrarily small tolerance. Equation (35) pays the low block,
including \(j=0\).

Let \(E(s;a,b)\) be the full absolute continuous rate of (3),
with its chirp retained. It is the integrated-logarithm expression
(17) of the finite selected reduction, also across product zeros.
Thus \(E(.5)=B_R\) and \(E(1)=B_1\).
First consider \(.5\le s\le1-z\). The algebra in Sections
2--4 of [stationary high-row transport](research_mixed_unwrapped_stationary_high_row_transport.md)
uses only
\[
       3/5\le r\le23/20,\qquad13/20\le t=e^{2\pi d}\le31/20
\tag{41}
\]
for own type three; these include our positive \(H\).
It does not require a negative type-four first height for its
base derivative \(1/50\). We spell out that application to
avoid importing the stronger, type-three-only derivative in the
last paragraph of that source's Theorem 1.

For real \(s\), write
\(Q_r=2\sin\pi s\),
\(N_s=|1-r e^{-2\pi i(s+x)}|\), and
\(N_b=|1-t e^{-2\pi i(s+z)}|\).
At any stationary row,
\[
 N_sN_b=rQ_r^2,\qquad N_b/Q_r^2<81/160,\qquad
                                      N_s>160r/81.
\tag{42}
\]
The second inequality is the complete polynomial estimate (15)--(17)
of that source on \(1-s\in[z,.5]\), with precisely (41).
For every cap profile in (7), its same elementary bounds give
\[
 N_e^2>1+4r^2/9+8r/25,\quad
 D^2<1+r^2-9r/25,\quad N_e>D,\quad D^2/r<143/75.
\tag{43}
\]
If \(D\ge1\), (42)--(43) give
\(N_s/D^2>4000/3861\); if \(D<1\), they give
\(N_s/D^2>32/27\). Therefore the true-end joint derivative
\(\log(N_s/D^2)\), and the regular one
\(\log(N_eN_s/D^3)\), exceed \(1/50\).
The selected monomial and every alias penalty are constant in \(x\).
At the upper endpoint \(s=1-z\), the row ratio is below
\(352/375<1\), exactly as in (22) of that source. A maximum
cannot occur there; the possible logarithmic zero at \(t=1\)
has the same one-sided conclusion.

At \(x=x_0\), the original
[plateau right-row theorem](research_mixed_right_tail_endpoint_bound.md) bounds
\(E(s)\) by \(\max(B_R,B_1)\), and (10)--(11) pay
every cap profile, including (8), with gap \(1/2000\).
At \(s=.5\), (35) pays the same barrier for every early \(x\).
Take the compact maximum of the regular and true-end joint rates
over this unwrapped row interval and the fixed cap profile sets.
If it exceeded \(\Lambda(z)-1/2000\), neither row endpoint
could maximize. All active rows would be interior stationary rows
with first derivative \(>1/50\). Compactness and integration of
fixed-profile derivatives imply that this maximum increases locally
where it exceeds the barrier, contradicting the paid right face.
This is the envelope argument of the original source, valid also
at switches and degenerate stationary rows. It selects no quartic
root and assumes no differentiable maximizing branch.

On the singly wrapped interval \(1-z<s<1-x\), Lemma 1 of
[the nonnegative-height row theorem](research_mixed_early_three_nonnegative_first_height.md)
is a purely algebraic inequality for \(x,z,r,t\). Its proof
uses no cap type. With \(1\le r<43/40<23/20\), it gives
\[
                         e^{2\partial_sE}<399/400<1.
\tag{44}
\]
Thus these rates are below the already paid left wall \(E(1-z)\).
Finally the exact [reflection identity](research_mixed_right_tail_reflection.md)
gives
\[
 E(1-v)-E(1)\le-2\pi d_+v\le0,\qquad0\le v\le x,
\tag{45}
\]
at positive first height. This pays all \(s\ge1-x\) by
the last profile in (35). Equations (42)--(45) cover the whole
high interval, not merely stationary rates before the wall.

The original zero-safe product estimate is uniform in every physical
index. Applying it to these continuous inequalities and summing at
most \(N\) absolute rows proves the high-block bound with the same
gap and any chosen positive tolerance. Both midpoint conventions,
the literal last stop \(N-1\), all revived rows and all integrable
wall zeros are retained. There is no division by a possibly zero
half or last row.

## 9. Assembly, ordinary colors and scope

The independent cap theorem bounds its complete coherent sum before
it is multiplied by any ordinary row or current. Its complete
endpoint coefficient, every contour correction, and the separate
true ends remain in (7)--(8). Sections 3--8 pay the resulting whole
finite inventory, while (12) supplies precisely its central
main/main entry. The entire Fourier upper bound is (5), so the
original selected monomial is retained in each piece.

Choose all factorial symbol errors, half-grid displacements,
polynomial current densities and finite counts within one prescribed
\(\tau\). The two zero modes each retain their original \(+N\)
density; no external normalization in (3) is altered. This proves
(6) at complete color and, after discarding the favorable cap angular
loss, uniformly on the whole real ordinary-color interval.

For complex ordinary colors, the cap is a polynomial of degree
less than \(N\); all other factors are color independent. Uniform
interval polynomial continuation gives a fixed neighborhood at an
arbitrarily small extra exponential allowance. Choose it before
\(N\), and then use a smaller disk for Cauchy derivatives. This
uses the all-real estimate for the exact source, not a bound at
one complete color or an asymptotic cancellation of individual
errors. It proves the stated common scope for both parities and
every fixed ordinary-color jet.

The outgoing affine term, the original coupled reference, all
later-type eligibility, and the length-three attached next-input
case are unchanged. The theorem pays only (3) on the fixed selected
rectangle (2). No deformation across an unestimated outer join,
whole-period replacement, whole-word noncancellation, knot
identification or finite-exception conclusion is made.

## Direct source versions

All listed files are unchanged. The directly used proofs and finite
source domains were read; the new extensions are justified above.

| Source | SHA-256 |
|---|---|
| research_mixed_selected_four_three_early_central.md | d9e2797fac0599cdca302ecd22312926b28765f487c8f0d95629d31d28c22405 |
| research_mixed_selected_four_three_full_product.md | 410c91677327cbea7f856e705b958ae011f93f29321f2c0c2ed7fc7100432c18 |
| research_mixed_selected_four_three_finite_reduction.md | 732d6cbf79894cb1e230e4eefa27762e369d84127d67e9e7c0d66c77901bbd42 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_cap_joint_early_horizontal_concavity.md | 1b623741d70402af77287b287aa1e2636b0b8d1abcb7275d5347f14ac75dbb20 |
| research_mixed_selected_cap_alias_transport.md | f69fae6109da41fb6505daaa92d75ecaae6942bc088fe825aadbef94c158f4db |
| research_mixed_selected_cap_right_rows.md | 4cd985cc20670cf8b7a0ac3e90fa1113d87296112c78d850219e2e288379a4c9 |
| research_mixed_selected_four_three_last_rows.md | 4448cc41f00adfc34cb337b79a946632358d6426a7c3728edc9d028eff3209f1 |
| research_mixed_first_four_three_true_last_row_calibration.md | a1571017529473e88dad8c0f5ec4f3592984a19040962e8279ca9dadb92257de |
| research_mixed_cap_early_taper_real_rows.md | d82b0506e7e156463360773bc8ab0e798334ee3a733ce9e6275215027c9c7ebc |
| research_mixed_cap_early_taper_complex_profiles.md | 6a7b8cd841d89690a9733c1005a2449ce808ba20a875c2d1f8d8ca0b0a769138 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_unwrapped_stationary_high_row_transport.md | 24210764f62ef04250a63dbcb5b5e82d4bdf59ede7eacb88889e5318dfc4d4aa |
| research_mixed_early_three_nonnegative_first_height.md | ffa42bf7baeafde8598b1ca87645e4a4069bd3381d80446db70e13d6cffeb5e8 |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_right_tail_endpoint_bound.md | ec2027e8c737a8b492750fd5de289e3ade03b3ac67e23e4b381c821915d979c0 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_alias_transport.md | 86bf3551639cafc08813769e32b5fc74ca0e89bc8fce1c17b0fbdc3a0f71a6e5 |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was performed.
