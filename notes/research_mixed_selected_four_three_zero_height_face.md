# The first four/three source at the real left face

Private written proof, 10 November 2026. The first retained coordinate
is set to one tenth on the real axis. The next coordinate remains at
its actual geometric height, which may have either sign. The estimate
below includes the complete two-factor finite source. Its proof first
bounds each contour contribution separately; this stronger statement
is needed for a later vertical connection.

## 1. Source and statement

Fix an actual positive three/four open word of length at least three,
beginning with four and three. Keep the reference and all logarithmic
lifts of the [complete selected early theorem](research_mixed_selected_four_three_early_complete_source.md).
Write
\[
 h_e\in[-.051,-.019],\qquad h_s,d\in[-.065,.068],\qquad
 b=z+id,\quad z\in P=[11/50,9/20],
\]
\[
 l=1/10,\quad r=11/50,\quad H=7/625,
 \qquad a=x+ih.
\tag{1}
\]
These intervals contain the actual reference; they do not define a
larger independent family of geometric references. The conclusion is
at \(a=l\). Intermediate comparisons use \(l\le x\le r\)
and \(0\le h\le H\), with every other height fixed.

For \(q_N=e^{-2\pi i/N}\), put \(P_j=(q_N;q_N)_j\),
\(p_j(X)=(q_NX;q_N)_j\), \(X=e^{-2\pi ia}\), and
\(Y=e^{-2\pi ib}\). The exact functions are
\[
\begin{split}
 U_N(w,X)&=\sum_{i=0}^{N-1}
       \frac{H_N(w,q_N^{-i})p_i(X)}{P_i^2},\\
 C_N(X,Y)&=\sum_{j=0}^{N-1}
       X^{-j}\frac{p_j(X)p_j(Y)}{P_j^2},\\
 K_{\sigma,N}(w;a,b)&=U_N(w,X)C_N(X,Y)d_N(X)X^{-N\sigma},
                         \qquad \sigma\in\{0,1\}.
\end{split}
\tag{2}
\]
Here \(H_N\) is the original complete cap coefficient and \(d_N\)
is the original Fourier interpolation polynomial. There is no
outgoing type-three halfweight. At the real target the two monomials
in (2) have identical modulus.

Use the original phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-\frac{i\pi}{2}(e-e^2),\\
 Q(s;a,b)&=g(s+a)+g(s+b)-2g(s)-g(a)-g(b)+2\pi ias,\\
 \mathcal F&=\Psi+Q-g(a),\qquad J(x)=\Re g(x),\\
 M&=\Re\mathcal F(e_*,s_*;a_*,b_*),\qquad
 p=\mathcal F_b(e_*,s_*;a_*,b_*),\\
 \Lambda(z)&=M+\Re p\,(z-\Re b_*).
\end{split}
\tag{3}
\]
Thus the affine comparison and its outgoing derivative are unchanged.

**Theorem 1.** For every \(\tau>0\), both parities and both choices
of \(\sigma\),
\[
 |K_{\sigma,N}(w;l,b)|\le C_\tau N^{A_\tau}
                 e^{N\{\Lambda(z)-1/1000+\tau\}}.
\tag{4}
\]
The bound holds uniformly for \(z\in P\), every real ordinary
color \(w\in[-2,2]\), and every integer \(N\ge2\). It also holds
on a sufficiently small fixed ordinary-color disk about \(-2\),
with fixed derivatives on smaller disks and the prescribed total
rate allowance. The stronger individual-profile statement is given
in Proposition 2 below.

## 2. The cap profiles and the positive-height calibration

Retain the original five cap profiles
\[
\begin{array}{ll}
 A_0(a)=\max_{.27\le u\le.49}\Re\Psi(u+ih_e,a),&
 A_L(a)=\Re\Psi(.27,a),\quad A_R(a)=\Re\Psi(.49,a),\\
 A_-(a)=\max_u\Re\Psi(u-.055i,a)-.11\pi,&
 A_+(a)=\max_u\Re\Psi(u+.04i,a)-.08\pi.
\end{array}
\tag{5}
\]
The true-end alternative is
\[
                      A_*(h)=3/5+2\pi h+\log4/100.
\tag{6}
\]
The [independent-height cap theorem](research_mixed_cap_early_fixed_height_full_source.md)
includes all cap currents, physical tails and true ends on this
rectangle. Its type-four upper-tail allowance is zero.

For the ordinary factor set
\[
 B_0(a,b)=\max_{.15\le v\le.5}\Re Q(v+ih_s;a,b),\quad
 B_L=\Re Q(.15;a,b),\quad B_R=\Re Q(.5;a,b),
\]
\[
 B_1=2\pi d_+,\qquad W(a)=-\Re g(a)-2\pi h.
\tag{7}
\]
At \(a=r+iH\), equations (10), (34)--(35) and Section 8 of the
complete selected early theorem give, individually,
\[
 A_i+B_j+W\le\Lambda(z)-1/2000,
 \quad i\in\{0,L,R,-,+,*\},\quad j\in\{0,L,R,1\}.
\tag{8}
\]
They also bound each cap alternative times every physical high-row
rate by this same right side. For regular cap profiles and \(B_1\),
the stronger old-face gap is \(3/100\), by equation (10) and the
last-row comparison cited immediately after it. These are bounds
proved before finite summation, not inferences from a small modulus
of a signed sum.

Two cap reductions will be used at height zero. Sections 3--4 of
that theorem extend as follows:
\[
 A_-,A_+<A_0-1/10,\qquad A_R<A_0-1/1250,
 \qquad \text{every main maximizer has }u<.43.
\tag{9}
\]
Here is the domain check, including the small change needed in the
localization argument. For \(0\le h\le H\), the same canonical
cap identities in the [alias proof](research_mixed_selected_cap_alias_transport.md)
give
\[
 -.46\pi<\Im\Psi_e<.82\pi,\qquad
 \Im\Psi_e>-.29\pi\quad(\Im e\le0).
\tag{10}
\]
Their proof uses only \(.37\le\Re(e+a)\le.71\) and the same
canonical cap root; reducing the nonnegative first height does not
change any argument range. Integrating these inequalities on the
original alias segments gives the first two comparisons in (9),
exactly as in equation (15) of the cited theorem. The right-cut
trial from the [right-cut proof](research_mixed_selected_cap_right_rows.md)
at \(e=.4\) uses \(e^{2\pi h}\le43/40\) and
\(\Im\Psi_e(.4,a)>-\pi/500\). The early-interval comparison
in equation (17) of the complete selected early theorem therefore
gives the third comparison unchanged.

For localization, the real derivative at \(e=.43\) still satisfies
\(\Re\Psi_e< -277/1000\), by equations (19)--(21) of that
same complete selected early theorem.
On \(e=.43+i\xi\), \(-.051\le\xi\le0\), its original
radical estimate gives \(\Im S''<\pi/10\) and
\(\Im\cot\pi e\ge0\). If \(\xi+h<0\), its absolute
value is now at most \(.051\), rather than \(.041\).
Since \(.53\le\Re(e+a)\le.65\),
\[
 \Im\cot\pi(e+a)
 <\frac{\sinh(.102\pi)}{3/2}<\frac29<\frac14.
\tag{11}
\]
Indeed \(.102\pi<13/40\), and the positive series gives
\(\sinh t\le t/(1-t^2/6)\); at \(13/40\) this is
\(3120/9431<1/3\). At nonnegative height the imaginary
cotangent is nonpositive. The exact Hessian identity therefore gives
\(\Im\Psi_{ee}<27\pi/20\). Downward transport costs less
than \((51/1000)(27\pi/20)<11/50\), leaving
\(\Re\Psi_e(.43+ih_e,a)<-57/1000<-1/20\).
The [early cap concavity theorem](research_mixed_cap_joint_early_horizontal_concavity.md)
excludes every larger private real coordinate. This proves (9)
throughout the stated rectangle,
including height zero. It does not choose a new critical point.

## 3. Main ordinary profiles and real cuts at height zero

Fix a main cap point with \(.27\le u\le.43\), or the left
cap cut \(e=.27\). Fix an ordinary main point or real cut
\(s=v+i\eta\), with \(.15\le v\le.5\) and
\(-.065\le\eta\le.068\). Put
\[
 D(x)=2\sin\pi x,\quad
 N_e=|1-e^{2\pi\Im e-2\pi i(u+x)}|,\quad
 N_s=|e^{-2\pi\eta}-e^{-2\pi i(v+x)}|.
\tag{12}
\]
The exact first-coordinate derivative, including the ordinary chirp,
is
\[
 \partial_x\Re\mathcal F(e,s;x,b)=\log(N_eN_s/D^3).
\tag{13}
\]
The actual main cap radius exceeds \(18/25\). On its restricted
private interval \(u+x\in[.37,.65]\), the cosine is less than
\(-7/12\), as proved in equation (26) of the complete early source.
For the left cut the stronger squared bound is \(N_e^2>10/3\).
Also \(v+x\in[.25,.72]\) has nonpositive cosine, and the
actual ordinary radius gives \(e^{-2\pi\eta}>13/20\).
Thus in both cases
\[
 N_e^2\ge\frac{1474}{625},\qquad
 N_s^2>\frac{569}{400},\qquad N_e^2N_s^2>\frac{10}{3}.
\tag{14}
\]
The last comparison follows from \(3(1474)(569)>10(625)(400)\).

The elementary midpoint estimate used in Section 3 of the
[four/four real-face proof](research_mixed_selected_four_four_zero_height_face.md)
is
\[
 \int_l^r\log D(x)\,dx<\frac3{25}\log(49/50).
\tag{15}
\]
It follows from concavity of \(\log(2\sin\pi x)\) and
\(2\sin(4\pi/25)<49/50\), with its sine-series witness given
there. Integrating (13) yields a gain greater than
\[
 \frac3{50}\log(10/3)+\frac9{25}\log(50/49)
                         >\frac{393}{5000}.
\tag{16}
\]
For a rational witness, \(\log2>56/81\) is the first two
positive atanh terms, while \(\log(5/3)>1/2\). Hence
\(\log(10/3)>193/162>119/100\). Also
\(\log(50/49)>1/50\).

At \(x=r\), move the first height from zero to \(H\).
Write \(\mathcal A(t,y)=\arg(1-e^{2\pi y-2\pi it})\)
on the original strip. The same argument bounds as in Section 4
of the four/four face proof give
\[
 \mathcal A(r,h)\ge7\pi/25,\qquad
 \mathcal A(u+r,\Im e+h)\le\pi/50,
\]
\[
 \mathcal A(v+r,\eta+h)+2\pi v\le\pi.
\tag{17}
\]
These inequalities do not require a sign for \(\eta\). Therefore
\[
 \partial_h\{\Re\mathcal F(e,s;r+ih,b)-2\pi h\}
                                      \ge-109\pi/50.
\tag{18}
\]
The reset costs less than \(2398/31250\), using \(H=7/625\)
and \(\pi<22/7\). The net gain in (16) is consequently greater
than
\[
 \frac{393}{5000}-\frac{2398}{31250}
                         =\frac{233}{125000}>1/1000.
\tag{19}
\]
Apply (8) at the upper right face, then maximize over the restricted
main private interval only after these pointwise comparisons.
Localization (9) makes that restriction exact at the final zero face.
The left cut follows by the same proof. The other three regular
cap profiles follow from (9). Thus all regular cap alternatives,
times \(B_0,B_L,B_R\), have gap greater than \(1/1000\) at
\(a=l\).

For the true-end cap profile, the real derivative is
\(\log(N_s/D^2)\). Equation (14) gives \(N_s>7/6\), so its
integrated gain is greater than
\[
                  \frac3{25}\frac17+\frac6{25}\frac1{50}.
\tag{20}
\]
Here \(\log(7/6)>1/7\). The term \(2\pi h\) in (6)
cancels the selected monomial rate. Its height derivative is bounded
below by \(-11\pi/25\), by (17). The reset cost is less than
\(242/15625\). The expression in (20) exceeds \(1/50\),
whereas \(242/15625<2/125\), leaving more than \(1/250\).
Together with (8), this proves the same zero-face gap for the
true-end alternative and the three ordinary profiles.

## 4. The ordinary last rate

At every nonnegative first height the physical last rate is
\(B_1=2\pi d_+\), independent of \(a\). For any regular
cap point in (5), the common bound from the four/four face proof is
\[
                  N_e^2>913/500>16/9.
\tag{21}
\]
It uses only \(.27\le u\le.49\), \(-.055\le\Im e\le.04\)
and \(l\le x\le r\). Hence the real derivative of the
cap-times-last profile, including the whole first weight, is
\(\log(N_e/D^2)\). Its integrated gain exceeds
\[
                \frac3{25}\log(4/3)+\frac6{25}\log(50/49)
                          >\frac3{100}.
\tag{22}
\]
For the last inequality, \(\log(4/3)>2/7\) suffices.
At \(x=r\), the corresponding selected height derivative is
\(2\mathcal A(r,h)-\mathcal A(u+r,\Im e+h)-2\pi\),
bounded below by \(-73\pi/50\). Its reset cost is less than
\(1606/31250<13/250\). The old regular last-rate gap is
\(3/100\), so (22) leaves a gap greater than
\(3/100+3/100-13/250=1/125\).

For the true-end alternative the real gain is
\(-\int_l^r\log D>3/1250\). Its selected height derivative
is \(\mathcal A(r,h)>0\), because the two explicit linear
height terms cancel. Thus it has no unfavorable reset cost.
Even the weaker gap in (8) gives the required final \(1/1000\).
This proves the last-rate comparison for all six cap alternatives.

## 5. All high rows before the first leg wraps

Let the continuous physical-row rate be
\[
 E(t;a,b)=\int_0^t\log|1-e^{-2\pi i(a+v)}|\,dv
       +\int_0^t\log|1-e^{-2\pi i(b+v)}|\,dv
                 -2J(t)-2\pi ht.
\tag{23}
\]
It is continuous through the integrated logarithmic zeros.
At height zero, consider \(1/2\le t\le1-z\). The polynomial
estimate in Sections 3--4 of
[stationary high-row transport](research_mixed_unwrapped_stationary_high_row_transport.md)
applies with first radius one and \(13/20<e^{2\pi d}<31/20\).
At every stationary row it gives
\[
                  |1-e^{-2\pi i(t+x)}|>160/81>3/2.
\tag{24}
\]
At the lower endpoint \(t=1/2\), the same numerator has square
\(2+2\cos(2\pi x)>2+18/50>9/4\), so the bound \(3/2\)
also holds there. The upper endpoint cannot maximize: its original
row ratio is less than \(352/375<1\), by equation (22) of that
source. If a numerator vanishes there, its one-sided limiting ratio
has the same exclusion.

For each fixed regular cap private point with its original penalty,
the joint derivative at any maximizing row is therefore greater
than
\[
                         \log2-3\log D(x),
\tag{25}
\]
by (21) and (24). For the true-end profile it is greater than
\(\log(3/2)-2\log D(x)\). These bounds also apply after
maximizing over a compact cap private interval. Apply the elementary
maximum-envelope argument of Section 5 of the same source to the
joint rate minus an antiderivative of (25). Every active profile
has positive derivative after an arbitrarily small relaxation.
Compactness, integration of fixed-profile inequalities and passage
to the maximum prove that the envelope at \(x=l\) is below
its envelope at \(x=r\) by at least the integral of (25).
The argument permits switches and degenerate stationary rows. It
does not assume a differentiable maximizing branch. Both shifted
real numerator arguments stay strictly between zero and one in
the interior of this row interval. Any numerator zero can only
occur at its separately excluded upper boundary.

For regular cap profiles the resulting gain is greater than
\[
       \frac3{25}\log2+\frac9{25}\log(50/49)
                       >\frac{109}{1250},
\tag{26}
\]
using \(\log2>2/3\). For the true-end profile it is greater
than \(33/625\), using \(\log(3/2)>2/5\).

We compare the old-face envelope at height zero with its paid
value at height \(H\). For fixed \(t\in[1/2,1-z]\),
\[
 \partial_h E(t;r+ih,b)
 =\mathcal A(r,h)-\mathcal A(r+t,h)-2\pi t\ge-\pi t.
\tag{27}
\]
Indeed at nonnegative height the first argument is at least
\(\pi(1/2-r)\), while the second, with \(r+t\ge.72\),
is at most \(\pi(1/2-r-t)\). Apply the inequalities first
at strict interior row arguments and then pass to the continuous
integrated endpoint values.

The cap and full selected first weight have height derivative at
least \(-73\pi/50\), as in Section 4. Since \(t\le.78\),
the complete regular joint reset costs at most
\[
                 \frac{56\pi}{25}H<\frac{1232}{15625}.
\tag{28}
\]
The difference between (26) and this last rational bound is
\(261/31250>1/1000\). For the true-end alternative, its linear
height term again cancels the selected monomial. The remaining
derivative is at least \(7\pi/25-\pi t\ge-\pi/2\).
Its reset cost is less than \(11/625\), leaving gain greater
than \(22/625\).

At \(x=r,h=H\), the complete early source has already paid
every cap alternative times every physical high-row rate by (8),
as explained there. Thus (26)--(28) give gap greater than
\(1/1000\) for every cap alternative and every continuous row
in \([1/2,1-z]\) at \(a=l\).

On \(1-z\le t\le1-l\), the
[nonnegative-height wrapped-row inequality](research_mixed_early_three_nonnegative_first_height.md),
Lemma 1, applies with first radius one. Its proof is an inequality
for the same ordinary type-three row, independent of the cap type.
It gives \(e^{2\partial_tE}<399/400\), so these rates are no
larger than the paid rate at \(1-z\). For \(1-l\le t\le1\),
the [reflection lemma](research_mixed_right_tail_reflection.md) gives
\[
                  E(1-v)-E(1)\le-2\pi d_+v\le0,\qquad 0\le v\le l.
\tag{29}
\]
Section 4 pays that last rate. Every continuous high-row rate is
therefore included, for either sign of \(d\).

## 6. The remaining raw currents and the literal finite bound

The ordinary main line has \(.15\le\Re s\le.5\), with
horizontal aliases at heights \(-.2,.2\). At \(a=l\), the
original argument inequalities in Section 7 of the complete early
source still give, at every finite private height,
\[
                   -7\pi/5<\Im Q_s<24\pi/25.
\tag{30}
\]
The ordinary inequalities use the real ordering \(x\le z\), and no
positive lower bound for the first height. Both aliases are below
the same private main point, with the original positive reserves
from equation (39) there. The four weighted vertical halves
decrease away from their respective real cuts.

The two unweighted joins between zero and \(h_s\) are vertically
convex. A direct check avoids any extension of a selected-height
Hessian theorem. Put \(u_0=\cot\pi v\),
\(U=\Re\cot\pi s\), \(C_a=\Re\cot\pi(s+l)\), and
\(C_b=\Re\cot\pi(s+b)\). The same even height estimate as in
equation (11) of the
[early central theorem](research_mixed_selected_four_three_early_central.md)
gives \(U>4u_0/5\) for \(.15\le v<.5\).
If positive, \(C_a<u_0\). If positive, \(C_b<u_0/2\):
write \(p_b=\cot\pi z<4/3\) and use
\[
 C_b\le\frac{u_0p_b-1}{u_0+p_b}<u_0/2,\qquad
                  u_0^2-p_bu_0+2>0.
\tag{31}
\]
Nonpositive shifted cotangents only improve the comparison. Thus
\(2U-C_a-C_b>0\). At \(v=.5\), \(U=0\) and both shifted
real cotangents are negative. Since
\(-\Re Q_{ss}/\pi=2U-C_a-C_b\), every join is bounded by its
main and real endpoints. Section 3 pays both.

For the physical low rows, the exact
[low-row ratio theorem](research_mixed_first_attached_low_row_transport.md)
holds at first height zero. The block
\(0\le j\le\lfloor3N/20\rfloor\) costs at most 201 times
its last row. Its rate is the paid real-cut value at \(s=.15\),
up to the original rounding tolerance. Its continuous derivative
version also bounds every low physical rate by that cut.
The central rows use the [original exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md)
and half-grid cuts tending to \(.15,.5\). All shifted real
arguments remain in \([.25,.60]\) and \([.37,.95]\), inside
the regular strip. The [cotangent residue identity](research_mixed_horizontal_asymmetric_contour.md) therefore retains
the original zero-mode density \(+N\), both aliases and every
vertical half. The high rows use the [zero-safe physical-product](research_mixed_conditional_contour_allowance.md)
bound before summing, with the continuous rates paid in Section 5.
This includes the literal final index, both midpoint parities and
every numerator zero. No comparison with a possibly zero finite
half-row is made.

**Proposition 2.** At \(a=l\), let \(B\) be any individual
ordinary rate from the main line, the two real cuts, either
zero-mode join, either horizontal alias with its original penalty,
any of the four penalized vertical halves, or any physical-tail
rate \(E(t;l,b)\), \(t\in[0,.15]\cup[.5,1]\).
For every cap alternative in (5)--(6), and for each whole first
Fourier upper alternative \(W_1=-J(l)\), \(W_0=0\),
\[
                       A_i(l)+B+W_\nu<\Lambda(z)-1/1000.
\tag{32}
\]
All individual cap joins and vertical halves are also included,
since the complete cap theorem bounds them by the retained profiles.

Sections 3--5 and (30)--(31) prove (32) for \(W_1\).
The inequality \(J(l)<0\) proves it for \(W_0\). The maxima
are independent, so the statement includes their full Cartesian
product. The [complete Fourier theorem](research_mixed_fourier_weight_continuation.md)
gives exactly the maximum of these two rates at height zero, for
either first choice in (2). The complete finite-source arguments
just given and the independent cap theorem now prove (4), with one
aggregate tolerance and polynomial factors. All estimates for the
cap hold on the whole real ordinary-color interval. Its degree in
that color is less than \(N\), so
[polynomial continuation](research_mixed_horizontal_complex_extension.md)
gives the stated fixed disk at any prescribed extra rate cost;
Cauchy's formula supplies fixed derivatives on a smaller disk.
This proves Theorem 1.

The conclusion is a calibrated real face and its complete raw
profile bound. A vertical connection, the full first period,
other coordinate departures and a closed-knot noncancellation
statement require their respective arguments.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_selected_four_three_early_complete_source.md | c0f4532b7f8d04c3bc4d84f16435029625c469adf1282914f80bf019bd22ebd6 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_selected_four_four_zero_height_face.md | fe99fcefe1618991471f083febcf4c6043418a4387d76be1ae2015542734810f |
| research_mixed_unwrapped_stationary_high_row_transport.md | 24210764f62ef04250a63dbcb5b5e82d4bdf59ede7eacb88889e5318dfc4d4aa |
| research_mixed_early_three_nonnegative_first_height.md | ffa42bf7baeafde8598b1ca87645e4a4069bd3381d80446db70e13d6cffeb5e8 |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_selected_four_three_early_central.md | d9e2797fac0599cdca302ecd22312926b28765f487c8f0d95629d31d28c22405 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_cap_joint_early_horizontal_concavity.md | 1b623741d70402af77287b287aa1e2636b0b8d1abcb7275d5347f14ac75dbb20 |
| research_mixed_selected_cap_alias_transport.md | f69fae6109da41fb6505daaa92d75ecaae6942bc088fe825aadbef94c158f4db |
| research_mixed_selected_cap_right_rows.md | 4cd985cc20670cf8b7a0ac3e90fa1113d87296112c78d850219e2e288379a4c9 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |

The full written proof and directly used source implications were read.
No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was used.
