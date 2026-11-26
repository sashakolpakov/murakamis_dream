# A decreasing upper envelope for the complete cap on the real incoming arc

Research deduction, 8 November 2026. The original finite cap admits
a complete contour bound throughout \(1/2\le a\le7/10\). The bound
retains the larger of its actual critical action and one fixed
departure action. Both decrease with the incoming coordinate.
Consequently the complete cap has a uniform upper rate decreasing
from the half-face action at speed at least \(\log(3/2)\).

No assertion that the departure lies below the critical action is
needed. In fact the fixed-departure obstruction proves that such
an assertion would be false at the far endpoint. All original
physical rows, six weighted currents and unweighted joins remain.
The main-path source is used at complete ordinary color and on
small complex neighborhoods, not at arbitrary real colors.
No numerical evaluation or frozen-source edit is used.

## 1. Source and statement

Retain the exact original polynomial and interpolation
\[
\begin{split}
 U_{0,N}(w,e^{-2\pi ia})
 &=\sum_{j=0}^{N-1}H_N(w,r^{-j})p_j(e^{-2\pi ia})/P_j,\\
 \mathscr A_N(e,a,w)
 &=D_N(e)^{-1}C_N(e,w)\Pi_N(a+e)/\Pi_N(a),\\
 \Psi(e,a,w)&=S(e,w)+J(a+e)-J(a)-i\pi ae.
\end{split}
\tag{1}
\]
At \(e=j/N\), the interpolation is precisely the physical row.
Its original scalar, primitive constants, carrier and source
definitions are those of
[the outer-cap identity](research_mixed_cap_outer_contour_reduction.md).
At \(w=-2\), put
\[
 \mathcal T(a)=\Psi(e_*(a),a,-2),\qquad M(a)=\Re\mathcal T(a),
 \qquad M_{\mathrm{half}}=M(1/2).
 \tag{2}
\]
The actual critical branch is the one in
[original incoming transport](research_mixed_half_face_general_incoming_transport.md).
It has
\[
 6/25<\Re e_*(a)<9/20,\quad -3/50<\Im e_*(a)<0,\quad
                         \Re e_*(a)<1-a.
 \tag{3}
\]

Fix the same departure as in
[the later-point main theorem](research_mixed_cap_later_point_main_contour.md):
\[
 q_d=11/12,\quad
 p_d=23/144+(11\sqrt2/12)i,\quad
 e_d=\Log(p_d)/(2\pi i)=E_d+i h_d,
 \quad 23/100<E_d<6/25.
 \tag{4}
\]
Write
\[
 R_d(a)=\Re\Psi(e_d,a,-2),\qquad
                  \mathcal E(a)=\max\{M(a),R_d(a)\}.
 \tag{5}
\]

**Theorem.** For every \(\tau>0\), there are constants \(C_\tau,B_\tau\)
such that, along both integer parities,
\[
 |U_{0,N}(-2,e^{-2\pi ia})|
       \le C_\tau N^{B_\tau}e^{N(\mathcal E(a)+\tau)}
       \qquad(1/2\le a\le7/10).
 \tag{6}
\]
The envelope obeys the explicit uniform bound
\[
 \boxed{\quad
 \mathcal E(a)\le
 M_{\mathrm{half}}-\log(3/2)(a-1/2).
 \quad}
 \tag{7}
\]
For each \(\tau\), the corresponding bound with an arbitrarily
small additional rate holds on a fixed complex neighborhood
of this incoming arc and ordinary color \(-2\). Every fixed
mixed incoming/ordinary derivative has only polynomial costs.
The precise fixed-base interpretation is given in Section 6.

This is an upper estimate for the complete finite source,
not a nonzero asymptotic expansion along the whole arc.

## 2. The entire early auxiliary-real curve is increasing

Parameterize the proved endpoint-source curve by
\[
 p(q)=1-q^2+i\sqrt2q,\qquad e(q)=\Log p(q)/(2\pi i),
 \quad q_-\le q\le q_d,\qquad
 q_-=(\sqrt6-\sqrt2)/2>1/2.
 \tag{8}
\]
Its left endpoint is \(e_L=1/8-i\eta_L\).
The original auxiliary saddle is real there. For
\(X=e^{-2\pi ia}=c+is\), the exact original multiplier is
\[
 e^{\Psi_e(e(q),a,-2)}=A-iB,
 \tag{9}
\]
where
\[
\begin{split}
 A&=\frac{3-c}{q^2}-1-\frac{\sqrt2s}{q^3},\\
 B&=\frac{1-2q^2-c+(q/\sqrt2)s}{q^3/\sqrt2},\\
 m(q)&=\frac{\sqrt2q^3}{1+q^2}.
\end{split}
\tag{10}
\]
For example, this follows directly from
\(\omega=(1+it)/(1-it)\), \(t=q/\sqrt2\), and
\(e^{\Psi_e}=\omega(p-X)/(p-\omega)\).

We prove uniformly on the whole parameter rectangle that
\[
                A>119/100,\qquad B>0,\qquad m<3/5.
 \tag{11}
\]
First \(A_a=-2\pi(qs-\sqrt2c)/q^3<0\), since \(c<0\) and
\(s\ge0\). At the worst endpoint \(a=7/10\), its derivative
in \(q\) changes sign at most once, from positive to negative.
It is therefore enough to bound \(A\) at \(q=1/2,11/12\).
Using
\[
 \sqrt5>559/250,\quad \sqrt2<99/70,\quad
             \sin(3\pi/5)<137/144
 \tag{12}
\]
gives at these endpoints, respectively,
\[
 A>\frac{201}{140},\qquad
 A>\frac{119124}{30250}-1-\frac{162756}{93170}>
                                            \frac{119}{100}.
 \tag{13}
\]
For the last comparison the cross-product difference is
\(6269010>0\). The sine bound in (12) follows by squaring
from \(\sqrt5<161/72\), with \(18756<18769\).

For positivity of \(B\), put \(\vartheta=\Arg X\).
The function \(-\cos\vartheta+(q/\sqrt2)\sin\vartheta\)
is concave on \([3\pi/5,\pi]\). Its endpoint values are
one and a number greater than \(3/10+3q/5\).
Thus its numerator in (10) is greater than the minimum of
\[
                2-2q^2,\qquad 13/10-2q^2+3q/5.
 \tag{14}
\]
Both are positive on \([1/2,11/12]\); the second decreases
there and has final value \(61/360\).
Finally \(m\) increases and \(m(11/12)<3/5\), directly from
\(\sqrt2<99/70\). This proves (11).

The original logarithm in (9) is the principal one throughout:
the multiplier stays in the fourth quadrant with positive real
part, and the selected lift agrees there at the already proved
later-point base. The connected parameter rectangle preserves
that lift. As the curve has positive real derivative,
\[
 \frac{d}{dE}\Re\Psi(e(q),a,-2)
       =\log\sqrt{A^2+B^2}-m\arctan(B/A).
 \tag{15}
\]
The minimum over \(B\ge0\) of the right side with \(m=3/5\)
is attained at \(B=3A/5\). It follows that (15) exceeds
\[
 \log(119/100)+\frac12\log(34/25)-\frac35\arctan(3/5)
                                                >\frac3{10000}.
 \tag{16}
\]
Here a written rational witness is
\[
\begin{gathered}
 \log(119/100)>
 \frac{38}{219}+\frac{2}{3}\left(\frac{19}{219}\right)^3
 >\frac{38}{219}+\frac1{2500},\\
 \frac12\log(34/25)>\frac9{59},\qquad
 \frac35\arctan(3/5)<\frac{25479}{78125},\\
 \frac{38}{219}+\frac9{59}-\frac{25479}{78125}
 =-\frac{73534}{12921\cdot78125}>-\frac1{10000}.
\end{gathered}
\tag{17}
\]
The logarithm uses its positive odd-power series, and the
arctangent uses its alternating upper truncation through degree
five. Consequently the entire early curve has rate at most
\(R_d(a)\), for every incoming parameter in the arc.

## 3. A complete source-valid main contour

The full endpoint asymptotic on a fixed neighborhood of
\[
       [23/100,49/100]+i[-3/50,0]
 \tag{18}
\]
is supplied by the above-curve theorem, the westward below-curve
theorem, and the older lower rectangle, exactly as assembled in
Section 2 of
[the complete later-point cap](research_mixed_cap_later_point_complete_packet.md).
The early curve and its left vertical join have their separate
complete endpoint-source neighborhoods. No unquantified tube is
used to span (18).

For each fixed real base \(a\), use
\[
\begin{gathered}
 b(a)=\min\{49/100,1-a-\delta\}>\Re e_*(a),\\
 L_N=\lfloor N/8\rfloor+1,\quad K_N=\lceil Nb(a)\rceil,\quad
 \ell_N=(L_N-1/2)/N,\quad b_N=(K_N-1/2)/N .
\end{gathered}
\tag{19}
\]
The one fixed positive \(\delta\) obeys all conditions in
[upper-end completion](research_mixed_cap_upper_end_currents.md)
and the long-right estimates. The strict critical separation
is uniform by compactness.

Deform the actual real zero-mode integral, with density \(+N\),
through these pieces:

1. \(\ell_N\) to \(1/8\) on the real line and then vertically to \(e_L\);
2. the full curve (8) from \(e_L\) to \(e_d\);
3. the vertical segment from \(e_d\) to \(E_d+i\Im e_*(a)\);
4. the horizontal segment through \(e_*(a)\) to \(b_N+i\Im e_*(a)\);
5. the vertical segment to \(b_N\).

The first join is paid by
[uniform left completion](research_mixed_cap_uniform_left_component.md).
Piece 2 is bounded by \(R_d(a)\), by (15)--(17).
Pieces 3--5 lie in (18), including its existing fixed neighborhoods
for the half-grid displacements.

On this prewall strip the original endpoint Schur identity gives
\(-\Re S''(e)>0\). Indeed the real part of the negative Hessian
of \(F(e,u)\), in its chamber \(0<\Re u<\Re e<1/2\), is
positive definite; for \(v=(1,u_c')\), its second product
component vanishes, so \(-\Re S''=\Re[v^*(-F'')v]>0\).
The source theorems retain precisely this chamber, including
the western strip. Also
\(\Re\cot\pi(a+e)<0\), since \(1/2<a+\Re e<1\).
Therefore the original \(\Re\Psi\) is strictly horizontally
concave and vertically convex on every part just used.

At the actual critical height, piece 4 has its unique maximum
\(M(a)\) at \(e_*(a)\). Its left endpoint lies strictly to the
left of the saddle, by \(E_d<6/25<\Re e_*(a)\), and hence has
strictly smaller rate. Convexity bounds piece 3 by the larger
of its two endpoint rates, at most \(\mathcal E(a)\).
The complete upper-end theorem pays piece 5 by \(M(a)\).
Thus every point of the main path has rate at most
\(\mathcal E(a)\). No endpoint of this deformation is omitted.

The literal interpolation (1) is holomorphic in the intervening
finite region, with all original reciprocal zeros retained.
Its path integral equals the real zero mode exactly.
The endpoint packet gives its original \(N^{-3/2}\) symbol
times \(e^{N\Psi}\), uniformly on the retained main path.
The density \(+N\), bounded path lengths and finite cover cost
only powers of \(N\). This proves the main-integral part of (6).
No Gaussian approximation to a possibly nonmaximal saddle is
used for this upper estimate.

## 4. All physical and weighted remainder groups

The exact physical partition and cotangent identity are
equations (12)--(14) of
[the complete local assembly](research_mixed_cap_later_point_complete_packet.md),
now with each base cut (19) fixed. The identities themselves
hold at every such incoming parameter. They have:

* the lower physical sector, paid uniformly by
  [the uniform left theorem](research_mixed_cap_uniform_left_component.md);
* the upper physical sector, paid by
  [upper-end completion](research_mixed_cap_upper_end_currents.md);
* the two full horizontal aliases, paid by the
  [upper](research_mixed_cap_tall_upper_alias.md) and
  [lower](research_mixed_cap_tall_lower_alias.md) theorems;
* both entire weighted left sides, paid by the uniform left theorem;
* the short weighted right sides, paid by upper-end completion;
* the long weighted right sides, paid by the
  [upper](research_mixed_cap_upper_right_long_side.md) and
  [lower](research_mixed_cap_lower_right_long_side.md) theorems.

Every one of these estimates holds throughout the real incoming
arc relative to \(M(a)\), with a common positive reserve after
a finite cover and common tolerance choices. The source counts
include all revived auxiliary rows and both true physical ends.
The original half-grid identity has exactly six weighted
currents; subdividing a right side at its short/long height
does not introduce another constant mode.
Since \(M(a)\le\mathcal E(a)\), all these complete remainders
fit (6). This proves (6) for the whole original cap.

## 5. Both branches of the envelope decrease

First the fixed departure is strictly subcritical at the half face:
\[
                         R_d(1/2)<M_{\mathrm{half}}.
 \tag{20}
\]
Here is a direct proof on the actual phase. The half-face critical
point obeys \(17/50<\Re e_+<7/20\) and \(-1/20<\Im e_+<0\).
Also \(23/100<E_d<6/25\) and \(-1/20<h_d<0\);
the latter follows from \(K=35377/20736<7/4<e^{\pi/5}\).
On the rectangle between these points the exact half-face Hessian is
\[
 -\Psi_{ee}
 =\frac{2\pi}{\sin(2\pi e)}
  +\frac{2\pi}{\sin(\pi e)\sqrt{2-e^{-2\pi ie}}}.
 \tag{21}
\]
Both terms have positive real parts, and each has
imaginary-to-real ratio less than \(8/31\).
For the first this follows from
\[
 |\cot(2\pi E)|<3/4,\qquad
             |\tanh(2\pi h)|<11/35.
 \tag{22}
\]
For the second, \(\cot(\pi E)<6/5\) on \(E\ge23/100\);
indeed \(\tan(23\pi/100)>\tan(23/32)>5/6\), using
\(\tan z\ge z+z^3/3\). Thus
\[
 -33/175<\arg\sin\pi e\le0.
 \tag{23}
\]
The number \(2-e^{-2\pi ie}\) has positive imaginary part at
most one and real part greater than \(328/175\).
Since \(175/328<13/24<\tan(1/2)\), its square-root argument
lies in \((0,1/4)\). The total denominator argument in the
second term of (21) therefore has modulus below \(1/4\).
Finally \(\tan(1/4)<8/31\).

Write \(\Psi_{ee}=-A+iB\); then \(|B|<(8/31)A\).
The straight displacement from \(e_+\) to \(e_d\) has
\(|\Delta h|/|\Delta E|<1/2\), because
\(|\Delta E|>1/10\) and \(|\Delta h|<1/20\).
Along that segment,
\[
 \Re\{\Psi_{ee}(\Delta E+i\Delta h)^2\}
 <-A(\Delta E)^2\left(1-\frac14-\frac8{31}\right)<0.
 \tag{24}
\]
Its first derivative at the original saddle is zero.
Twice integration proves (20).

Next the departure action has a uniform exact contraction:
\[
 \left|\exp\Psi_a(e_d,a,-2)\right|
       =\frac{|1-X/p_d|}{|1-X|}<\frac23 .
 \tag{25}
\]
Put \(C=23/144\), \(D=11\sqrt2/12\), and
\(K=|p_d|^2=35377/20736\). Squaring (25) reduces it to
\[
 F=K+9+(8K-18C)c-18Ds<0,
 \qquad X=c+is.
 \tag{26}
\]
Write \(c=-\cos t,\ s=\sin t\), \(0\le t\le2\pi/5\).
Since \(8K-18C>0\), \(18D>0\), and both sine and cosine
are nonnegative there, \(F''(t)>0\). Its maximum is at
one of the endpoints. At zero,
\[
                  F=95/8-7K=-1399/20736<0.
 \tag{27}
\]
At the other endpoint use \(c<-3/10\), \(s>9/10\),
\(K>3/2\), \(C<1/6\), and \(D>5/4\):
\[
 F<9-\frac75K+\frac{27}{5}C-\frac{81}{5}D<0.
 \tag{28}
\]
This proves (25), with the original chirp retained.
Integrating and using (20) gives
\[
 R_d(a)<M_{\mathrm{half}}-\log(3/2)(a-1/2).
 \tag{29}
\]

For the actual critical action, Lemma 3, equation (20), of
[global phase decrease](research_mixed_half_face_global_phase_decrease.md)
proves on the selected branch
\[
       |\exp\mathcal T_a|=|k/p|^2<1/2.
 \tag{30}
\]
Thus \(M(a)\le M_{\mathrm{half}}-\log2\,(a-1/2)\).
Combining this with (29) proves (7).
In particular one may replace \(M_{\mathrm{half}}\) by the
fully written analytic upper bound
\[
       \widehat M=\frac{203}{200}-\frac{1303}{7680000}
 \tag{31}
\]
from [the half-face cap action bound](research_mixed_half_face_cap_action_upper.md).

## 6. Ordinary-color neighborhoods, derivatives, and the next comparison

At each real base \(a\), fix the physical index sets (19),
all six weighted paths, and the full main path before varying
the parameters. All exact finite factors are holomorphic there.
The main endpoint source has a fixed open neighborhood of
the required compact sets. The strict remainder estimates
preserve their original scope under small complex perturbations.
A finite cover of the real incoming arc gives common constants.

For any prescribed \(\tau>0\), shrink these neighborhoods so
that the main phase bounds increase by less than \(\tau\).
The same construction proves (6), with a slightly larger
arbitrarily small rate, on those neighborhoods. Cauchy on
disks of radius \(1/N\) then gives every fixed mixed derivative
with polynomial costs and no derivative of a moving cut.
Equivalently, near a real base the source normalized by
its original \(e^{N\mathcal T(a,w)}\) has upper rate
\(\max\{0,R_d(a)-M(a)\}+\tau\), including all fixed normalized
mixed jets. No nonzero leading coefficient is asserted.

The positive physical and several weighted-current estimates
remain valid at all real ordinary colors by their own source
theorems. This note does not promote the new private main
path to an all-real coherent endpoint estimate.

The cap estimate can now be multiplied by an actually eligible
following conditional source with all its prescribed weights.
The required comparison is with that original following action;
equations (6)--(7) do not supply its sign. In particular the
fact that \(R_d(a)>M(a)\) at some parameters is allowed by
this complete upper theorem. A whole-arc nonzero cap expansion
and a new filling-family conclusion are not claimed.
