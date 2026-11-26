# The complete first polynomial on the selected 444 shoulder

Private written proof, 11 November 2026. Author-frozen for separate
proof and direct-source review; not adopted.

The previous shoulder estimates bounded the complete cap and two ordinary
kernels only while the first coordinate stayed on one of its two central
horizontal intervals. Here the first coordinate is integrated over its
whole period. The argument moves that coordinate at each fixed value of
the second coordinate. This preserves the small reserve in the
first-unselected shoulder estimate: no further second-coordinate
transport cost is charged to it.

## 1. The original finite product

Fix an actual positive three/four word of length \(m\ge4\) beginning
with \(444\), with its original critical reference and logarithmic
lifts. Use
\[
 P=[11/50,9/20],\qquad H=1/100,\qquad
 y=q+iH,\quad 9/20\le q\le1/2,\qquad z=b+ic_3,\quad b\in P .
 \tag{1}
\]
The original first-coordinate height \(c_1\), first and third ordinary
index heights \(h_2,h_3\), and cap index height \(h_e\) satisfy
\[
 -.078<c_1<-.020,\qquad
 -.102<h_2,h_3,c_3<-.001,\qquad -.051<h_e<-.019.
 \tag{2}
\]
These are necessary bounds on the actual coupled reference, not an
independently chosen rectangular reference. Both conditional indices
are ordinary, including when \(m=4\).

For \(\zeta=e^{-2\pi i/N}\), put
\[
 P_j=(\zeta;\zeta)_j,\qquad p_j(V)=(\zeta V;\zeta)_j,
\]
and retain the original complete finite functions
\[
\begin{split}
 U_N(w,X)&=\sum_{i<N} H_N(w,\zeta^{-i})p_i(X)/P_i^2,\\
 C_N(X,Y)&=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 f_N(w,Y)&=N\operatorname{CT}_X
       [U_N(w,X)d_N(X)(1+X^{-N})C_N(X,Y)],\\
 {\cal D}_N(w,Y,Z)&=f_N(w,Y)d_N(Y)Y^{-N}C_N(Y,Z).
\end{split}                                                     \tag{3}
\]
Here \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iy}\), and \(Z=e^{-2\pi iz}\).
Equivalently,
\[
 f_N(w,Y)=\sum_{k=0}^{N-1}
                U_N(w,\zeta^k)C_N(\zeta^k,Y)/P_k .              \tag{4}
\]
The remaining outgoing allocation is \(|d_N(Z)|^{1/2}\). It is a
modulus allocation, not a chosen square root, and no finite polynomial
is divided out.

Let \(g,\Psi,Q\) be the original primitives, with
\[
 Q(s;a,y)=g(s+a)+g(s+y)-3g(s)-g(a)-g(y)+2\pi ias.
\]
Use the same affine comparison as in the
[double-selected shoulder](research_mixed_444_double_selected_right_shoulder.md):
\[
\begin{split}
 F_{123}&=\Psi(e,a)+Q(s_2;a,y)+Q(s_3;y,z)
                       -g(a)-g(y)-\tfrac12g(z),\\
 p_R&=g'(s_3^*+r_3)-\tfrac32g'(r_3),\\
 \Lambda_{123}(z)&=\Re F_{123,*}+\Re\{p_R(z-r_3)\}.
\end{split}                                                     \tag{5}
\]
Every star is the original coupled reference. Its first internal
marginal vanishes, so \(\Lambda_{123}\) does not change when the
first target moves.

**Theorem.** On a sufficiently small fixed ordinary-color disk about
\(-2\), for every \(\tau>0\),
\[
 |{\cal D}_N(w,Y,Z)|\,|d_N(Z)|^{1/2}
 \le C_\tau N^{A_\tau}
       \exp N\{\Lambda_{123}(z)-1/1000000+\tau\} .               \tag{6}
\]
This is uniform on (1), at both parities. Fixed ordinary-color
derivatives satisfy the corresponding bound on smaller disks.
The first sum is complete. The assertion concerns only the selected
second horizontal interval in (1); it does not include its height
connection or complete period.

## 2. Profile bounds already available on both first plateaux

For the first ordinary kernel use the main, real left, real half,
and full periodic last rates
\[
 R_0^2,\ R_L^2,\ R_R^2,\ R_1^2 .
\]
Their index sets are respectively \([1/8,1/2]+ih_2\),
\(\{1/8\}\), \(\{1/2\}\), and the continuous full-period endpoint.
Use the analogous four third-factor rates \(R_k^3\).
All shifted logarithmic endpoints mean continuous primitive limits;
the finite contour always stops at a fixed \(r_0<1/2\).
For the physical first rows, the notation used below is
\[
 E(t;a,y)=\int_0^t\log|1-e^{-2\pi i(a+u)}|\,du
         +\int_0^t\log|1-e^{-2\pi i(y+u)}|\,du
         -3J(t)-2\pi(\Im a)t,\qquad J(t)=\Re g(t).
\]
The real left and half profiles are its values at \(1/8\) and
\(1/2\); the full last carrier is its continuous value at one.
Possible numerator zeros are integrated in these formulas.

The two full selected second-weight rates are
\[
 W_2^{\rm fac}=-\Re g(y)-2\pi H,\qquad W_2^{\rm force}=0 .
\]
For each third profile and either alternative put
\[
 T_{k,\mu}(y,z)=R_k^3(y,z)+W_2^\mu(y)-\tfrac12\Re g(z).
 \tag{7}
\]
These are constant during all first-coordinate motions below.

The [unselected main comparison](research_mixed_444_first_unselected_positive_shoulder_main.md)
and its [finite completion](research_mixed_444_first_unselected_positive_shoulder_complete.md),
Sections 2--3, give every profile pair on \(a\in P+ic_1\)
with a common raw reserve \(1/72000\), after cap attachment.
In particular the proof pays each cap profile, first profile,
third profile, and second-weight alternative separately.
It is not a bound inferred from a cancelling modulus.

The [double-selected shoulder](research_mixed_444_double_selected_right_shoulder.md),
Sections 2--4, gives the corresponding Cartesian collection on
\(a\in P+iH\) with reserve \(1/20000\).
Its main and left cap profiles pay the other cap alternatives
by the cap-only comparisons recorded in the
[selected first-left proof](research_mixed_complete44_second_selected_first_left_connection.md),
equations (10)--(11). Their use does not involve \(y\).

We shall reserve
\[
                         d=1/100000                            \tag{8}
\]
from either plateau. All subsequent transports preserve this raw
reserve, except for an explicitly chosen arbitrarily small collar
allowance.

The true cap ends require their own margins, which are retained.
At the negative first-left anchor \(a=.22+ic_1\), the constant
\(3/5+\log4/100\) is below the original bare cap plane by more
than \(7/40\). At the positive anchor \(a=.22+iH\), the ceiling
\(3/5+2\pi H+\log4/100\) is below the cap main profile by more
than \(53/500\). At the negative right anchor \(a=.45+ic_1\),
the enlarged ceiling
\[
                      E_*=3/5+2\pi H+\log4/100<69/100           \tag{9}
\]
is below the bare plane \(149/200\).
These are the cap-only comparisons in the negative-left and
right-half connection proofs. They hold at the new \(y\) because
neither their phase nor their comparison plane involves that target.
Multiplication by the new plateau profile bounds therefore preserves
these separate cap margins.

## 3. First negative horizontal interval

Keep \(a=x+ic_1\), \(.1\le x\le.22\).
The negative-left proof, Sections 3--4, supplies two
outgoing-independent transports.

For each regular cap point \(e=u+i\xi\) in its complete rectangle
and each first ordinary point \(s=t+i\eta\) with
\(1/8\le t\le1/2\), \(\eta\le0\), its derivative is
\[
 \partial_x\Re\{\Psi(e,a)+Q(s;a,y)-g(a)\}
  =\log\frac{|1-rR e^{-2\pi i(u+x)}|
                    |p-r e^{-2\pi i(t+x)}|}
                   {|1-r e^{-2\pi ix}|^3}>0,                 \tag{10}
\]
where \(r=e^{2\pi c_1}\), \(R=e^{2\pi\xi}\), \(p=e^{-2\pi\eta}\).
The written polynomial proof uses \(p\ge1\), \(1/2<r<9/10\)
and the cap rectangle. It contains no \(y\). Thus the new plateau
bound at \(x=.22\) pays every main and real-cut profile, together
with each fixed constant (7), throughout this early interval.
For a true cap end its derivative is greater than \(-\log2\).
The backward cost is less than \(21/250\), paid by its separate
\(7/40\) cap margin, leaving the reserve (8) intact.

For the full last rate,
\[
                        R_1^2=2\pi(-c_1+H),                  \tag{11}
\]
the cap-plus-weight derivative is \(\log(N_e/D^2)\).
Section 4 of the same source proves it positive for the cap main,
cuts and upper alias, and first reduces the lower alias to its main.
The main cap maximizer is restricted to \(u\le.43\) there.
That restriction and all of the displayed polynomial witnesses
are cap-only. The true-end backward cost is less than \(3/100\),
also paid by \(7/40\). Hence the last profile retains (8).

Use now the
[complete all-angle high-row theorem](research_mixed_all_angle_high_rows_with_small_positive_output.md).
Its drift condition holds since
\[
                       (-\Im a)_++H\le11/125 .
\]
It bounds the entire first high block by the half and last profiles,
with an arbitrary allowance. The older excess \(46/2475\) is not
used. Both required profiles have just been calibrated with (8).

The low rows increase to their real left cut. On this new domain
the outgoing numerator has real argument in \([.45,.625]\) and
radius \(e^{2\pi H}>1\), so its lower bound only improves over the
one in the negative-left source. Its incoming and own factors are
unchanged. The central contour and its corrections are completed
uniformly in Section 6 below. Thus the negative first horizontal
is paid with raw reserve \(d\).

## 4. First positive horizontal, zero face and left joins

Keep \(a=x+iH\), \(.1\le x\le.22\).
The positive first-left proof, Section 3, transports its main
maximum from \(x=.22\) using joint real concavity. On the new
second shoulder its outgoing cotangent is nonpositive:
\[
             \Re\cot\pi(s+y)\le0\qquad
                  (1/8\le\Re s<1/2,\ .45\le q\le.5).
\]
Consequently the Hessian positivity in that proof is unchanged.

Its anchor optimizer bounds also persist. The cap optimization is
independent of \(y\), so \(\Re e<.4\) is unchanged. At the first
ordinary upper test point \(\Re s=.44\), increasing \(q\) from
\(.45\) to \(.5\) decreases the outgoing numerator modulus:
\[
 \partial_q\log|1-R e^{-2\pi i(q+.44)}|
  =\frac{2\pi R\sin 2\pi(q+.44)}
         {|1-R e^{-2\pi i(q+.44)}|^2}<0 .
\]
The other factors in its private derivative do not change.
The negative derivative at this test point is therefore preserved.
Private concavity excludes all maximizers at or beyond .44.
The first-coordinate derivative witnesses (27)--(29) of that
source are independent of \(y\) and now apply unchanged.
They transport the main maximum and all real-cut combinations
without increase toward \(x=.1\).
On this early interval the factorial first-weight rate exceeds
the forced rate by \(3/40\), the same first-coordinate inequality
used in that source. Thus the comparison of the factorial
profile bounds the whole selected first weight.
The cap aliases and right cut reduce by the same cap-only comparisons.
For a true cap end, the cost \(9/125\) is paid by its margin
\(53/500\). Thus every main, left and half profile retains (8).

The last rate equals \(2\pi H\). The direct left-cut integral
comparison in equations (19)--(22) of the positive first-left proof
still gives
\[
                         R_L^2>2\pi H+1/4.                    \tag{12}
\]
The changed outgoing interval is \([.45,.625]\), on which its
old sine lower bound \(5/4\) remains valid. The incoming interval
and all denominators are unchanged. Therefore the last rate, and
by the all-angle theorem every physical high row, is paid as well.

At \(a=.1\) real, the pointwise comparison from the same source,
equation (34), is also independent of \(y\).
For regular cap and first main/cut profiles the horizontal gain
exceeds \(7/100\); the reset cost is at most \(109\pi/5000\).
Their difference exceeds \(1/2000\). For true ends the net gain
likewise exceeds \(1/2000\), after the affine endpoint term cancels
the selected monomial. Thus the zero face has reserve at least
\(d+1/2000\) for every main/cut and every fixed (7).
Equation (12) and the all-angle theorem pay its high block.

For both first height joins at \(x=.1\), use one common raw envelope:
all six cap alternatives, all central contour points and sampling
penalties, physical high rates for \(.5\le t\le.9\), and the
literal last rate
\[
                     \lambda_h=2\pi((-h)_++H).
\]
On each of \([c_1,0]\) and \([0,H]\) this last rate is affine.
The final physical rows \(t\ge.9\) are bounded by it by the
reflection argument in the negative-left proof, equation (30),
and its positive counterpart. The needed condition is
\(1-t\le.1\le q\), which is preserved.

The fixed-profile height derivatives in the two left-connection
proofs are independent of \(y\):
\[
\begin{split}
 \partial_h^2\Re\Psi(e,.1+ih)
   &=\pi\{\Re\cot\pi(.1+ih)-\Re\cot\pi(e+.1+ih)\},\\
 \partial_h^2\Re Q(s;.1+ih,y)
   &=\pi\{\Re\cot\pi(.1+ih)-\Re\cot\pi(s+.1+ih)\}.
\end{split}                                                     \tag{13}
\]
Each is positive on its retained private sets.
The first cotangent exceeds \(245/144>3/2\) on the negative join
and \(25/9\) on the positive join, while each positive shifted
cotangent is at most \(3/2\). The physical high profiles are convex
before their first incoming wall, with continuity at \(t=.9,h=0\).
The cap end is affine on either height interval, and the complete
first Fourier upper rate is a maximum of convex functions.
Thus the common raw envelope is convex on each join.
Its endpoints have been paid above; its interior retains reserve
\(d\). This is a statement about explicit rate functions, not
convexity of the modulus of the finite sum.

For \(0<x\le.1\) real, Section 5 of the positive first-left source
gives the outgoing-independent derivative \(>1/3\) for every cap
and first contour pairing, including all sampling points.
It gives the same derivative for a true end. The low comparison
still improves, and (12) and the all-angle theorem replace its
high-block reduction. Hence each fixed interval \([\rho,.1]\)
has reserve
\[
                   d+1/2000+(.1-x)/3,\qquad \rho>0.            \tag{14}
\]
The exact Laurent support of the complete first integrand in either
sector is contained in
\[
                  [-(1+\sigma)N+1,(2-\sigma)N-2].
 \tag{15}
\]
Lemma 1 of the
[endpoint continuation](research_mixed_four_four_real_first_endpoint.md)
extends (14) through zero with arbitrarily small fixed rate cost.
All intervals are chosen before \(N\); every remaining factor,
including the outgoing modulus halfweight, is a constant multiplier
in this continuation. Both first monomials have modulus one on
the real segment.

## 5. Right first connections and the real half calibration

For \(\sigma=0,1\), put \(h_0=c_1,h_1=H\).
We extend the new plateau estimates along
\[
                 .45+ih_\sigma\longrightarrow.5+ih_\sigma
                                            \longrightarrow.5 .
 \tag{16}
\]
The cap, its aliases and the enlarged true-end ceiling (9) are
exactly those in the
[right-half connection proof](research_mixed_complete44_second_selected_right_half_connections.md).
Its derivatives in the first coordinate contain no \(y\).

The only main-index guard needing an enlarged-domain check is
\(t_2>.22\) at the old first face.
Section 3 of the
[complete 443 shoulder proof](research_mixed_443_complete_second_selected_right_shoulder.md)
proves this guard for
\[
 .1\le\Re a\le.5,\quad c_1\le\Im a\le H,\quad .45\le q\le.5 .
\]
That calculation concerns only the first \(C_N(X,Y)\), has exactly
the heights (2), and never uses the third kernel or its type.
Its two numerator polynomials and curvature proof therefore apply
here without a changed allocation. The first cap optimizer and
first-coordinate derivative tests in Sections 3--4 of the
right-half proof now apply at each fixed new \(q\).
Its Hessian guard improves, since the shifted outgoing cotangent
is nonpositive on the entire private interval.
The main maximum consequently cannot increase to the right.

Every physical first cut and high-row comparison is transported
pointwise by the same first-coordinate derivative in Section 4
of that proof; this derivative is independent of \(y\).
The full high block at the new first anchors is paid by the
all-angle theorem, so no unproved old high-row domain is reused.
The selected true-end main comparison may increase by at most
\(1/20\); its separate \(53/500\) cap margin pays this.
The negative true-end comparison is nonincreasing.
The cap aliases reduce to their same-index main profiles as in
the right-half proof, throughout \(c_1\le\Im a\le H\).

Choose a fixed \(r_0<1/2\), arbitrarily close to \(1/2\), and
spend less than \(d/4\) on its physical collar.
At \(a=.5+ih\), the common central-profile envelope is convex:
\[
 \frac{d^2}{dh^2}\{\Re\Psi(e,.5+ih)+\Re Q(s;.5+ih,y)\}
       =-\pi\Re\cot\pi(e+.5+ih)-\pi\Re\cot\pi(s+.5+ih)>0 .
 \tag{17}
\]
The full first-weight upper rate is zero on the appropriate
negative-unselected and positive-selected halves.
For physical indices below one half, the analogous second
derivative is nonnegative. For high rows the cap-plus-row rate
is nonincreasing below zero and nondecreasing above zero by
the reciprocal-radius argument in Section 5 of the right-half
proof. The outgoing numerator contributes no first-height
derivative. Thus (16) and its real half face have raw reserve
at least \(3d/4\).

In particular, the real half face retains an individual bound
for every cap alternative paired with
\[
 M_2(y)=\max_{2/25\le t\le r_0}\Re Q(t+ih_2;.5,y),
 \quad R_L^2(.5,y),\quad E(2/25;.5,y),
 \tag{18}
\]
and with every third profile and second-weight alternative.
The extra main interval \([2/25,1/8]\) increases to \(1/8\),
exactly as in equation (26) of that proof: now the outgoing
sum lies in \([.53,.625]\), so its negative cosine makes the
same force estimate valid. This is a bound on individual
profiles before summation.

## 6. The finite first and third kernels on the changed domain

Here we specify why the transports above control complete finite
sources. For the first kernel, all calculations in Section 5
of the complete 443 shoulder proof involve only \(C_N(X,Y)\).
They apply to the present entire first path before the real half.
The phase, actual height \(h_2\), and outer domains are identical.
The third type is absent from that section's first-kernel formulas.

Explicitly, keep the original main line at \(h_2\), half-grid
cuts tending to \(1/8,r_0\), both zero-mode joins, both horizontal
sampling corrections, and all four weighted vertical halves.
For \(I=\Im Q_s\), that source proves on this enlarged domain
\[
               I<\pi,\qquad I>-2\pi+\pi/120\quad(\Im s\ge0).
 \tag{19}
\]
The second bound includes all incoming heights from \(c_1\) to \(H\)
and every real \(0<x<.1\). Its full-radius argument proof is
independent of the third factor. Thus the weighted vertical
halves decrease away from their real cuts. For each fixed
\(\rho\le x\le.5\), sufficiently tall fixed aliases lie below
the main maximum by one. Use the same chosen heights throughout
each raw-envelope comparison. At a calibrated endpoint the
additional sides above a previously chosen height are controlled
by their strictly decreasing weighted rates.

Both unweighted joins have negative real index Hessian on
heights from \(h_2\) to zero. In the early region the ordinary
guard in (13) and its main-index version apply; on the right
both shifted real parts exceed one half. Convexity in private
height pays each join by its main and real-cut endpoints.
Every shifted factorial argument remains in a compact original
strip, since the right cut is strictly below \(1/2\), even at
\(q=1/2\).

The physical low rows increase to their left cut; the full high
rows are controlled by the exact theorem cited in Section 3,
at every intermediate first height. The right-cut physical
collar has its separately chosen allowance.
The original marked factorial interpolation and cotangent
residue identity therefore keep their coefficient \(N/(2i)\),
zero-mode density \(+N\), all joins and weighted sides, and
every finite row through \(N-1\), at both parities.

This identifies a common complete raw envelope. Its first negative
and positive horizontal endpoint values are paid in Sections 3--4,
and its height-convexity comparisons use exactly this same inventory.
On the real first interval, retain all its sampling points before
using the pointwise derivative leading to (14).

For the third kernel \(C_N(Y,Z)\), use Section 4 of the unselected
shoulder completion, or Section 5 of the double-selected shoulder.
Both give the same complete four-profile bound on (1), including
its original \(-1/5,4\) corrections, joins, low/high physical rows,
and outgoing half allocation. The first coordinate is absent from
this argument. Hence taking every first profile together with
every third profile includes all simultaneous corrections.
No finite factor is replaced by its stationary term alone.

The cap sources are unchanged because they depend only on the
first coordinate. Their ordinary-color bounds and the literal
degree in that color remain those in the first-connection proofs.

## 7. The real first interval after one half

For \(.5\le a\le7/8\), Section 6 of the complete 443 shoulder proof
establishes the unit-incoming conditional estimate
\[
 |C_N(e^{-2\pi ia},Y)|
 \le C_\tau N^{A_\tau}
  e^{N\{\max(\Re\Theta(a,y),L(y))+\tau\}},
 \qquad L(y)=E(2/25;.5,y).                                     \tag{20}
\]
We use only that section's conditional-kernel and cap arguments,
not its type-three calibration. They concern the same \(C_N\)
and cap as here. Its boundary check at \(q=.5\) is the cubic
\[
                 2v^3+(R-2)v^2+(R+3)v-1=0,\qquad R=e^{2\pi H}.
\]
Its strictly positive real derivative gives one real root and
one nonreal conjugate pair; the continued upper root is simple.
The incoming-ray exclusion, compact radius and cut bounds,
and both sampling slopes in that proof consequently hold also
here. Every low, postwall and high row remains in (20).
Neither \(C_N(Y,Z)\) nor a third-type parameter occurs in these
root or finite-source checks.

The same conditional multiplier and half-face convexity give
\[
          \Re\Theta(a,y)\le\Re\Theta(.5,y)\le M_2(y).            \tag{21}
\]
Its complete cap transport is bounded by the same real-half cap
envelope \({\cal A}(0)\). The possible extra endpoint constant
\(9/10\) lies below its main profile, whose cap-only trial
exceeds \(181/200\).
Both first Fourier monomials have unit modulus on this real arc,
and the full weight has rate zero.
Consequently the real-half calibration (18), with the complete
third envelope from Section 6, pays (20)--(21) with reserve
at least \(3d/4\). No new second-coordinate transport is used.

For \(7/8\le a<1\), Section 7 of that same source gives the
angle-independent, all-index first-pair bound
\[
 |U_N(w,X)d_N(X)X^{-\sigma N}C_N(X,Y)|
 \le C_\tau N^{A_\tau}
        e^{N\{89/60+\pi/100+\tau\}}.                            \tag{22}
\]
The cap ceiling and split conditional estimates used there do
not involve the third type. They hold at both parities.

At the original first reference \(a_*=a_0+ic_1\), use the formal
comparison
\[
 B(y)=\Re{\cal T}_1(a_*,-2)-\Re g(a_*)+R_L^2(a_*,y).
 \tag{23}
\]
Here \({\cal T}_1(a_*,-2)=\Psi(e_*,a_*)\) is the original cap
critical value; \(e_*\) belongs to the retained cap main interval.
Its written lower bound throughout the new shoulder is
\[
                 B(y)>1+93/200+1/28+1/36 .
 \tag{24}
\]
Only its outgoing sine interval changes, to \([.45,.625]\);
the lower bound used in that source therefore persists.
At every current \(q\), rather than only at \(q=.45\), the
unselected shoulder profile theorem in Section 2 pays
\[
                   B(y)+T_{k,\mu}(y,z)\le\Lambda_{123}(z)-d .
 \tag{25}
\]
Indeed its cap phase at the original cap critical point is no
larger than its retained cap main maximum, and \(a_*\in P+ic_1\).
Its first left profile and every third alternative are precisely
among the calibrated profiles. This uses no lower bound for a
finite cap.

The difference between the lower benchmark (24) and the
first-pair ceiling (22) exceeds \(173/12600\), by the written
rational comparison in the complete 443 source.
Equations (22)--(25) thus leave more than \(d+173/12600\).
The same Laurent support (15) and the endpoint lemma extend
through \(a=1\) at arbitrarily small fixed cost.
The outgoing halfweight and every other \(X\)-independent
factor are carried as multipliers, also at their zeros.

## 8. Extracting the first coefficient

For sector \(\sigma\) use the oriented path
\[
 0\to .1\to .1+ih_\sigma\to .45+ih_\sigma
       \to .5+ih_\sigma\to .5\to7/8\to1 .
 \tag{26}
\]
Each integrand
\[
 U_N(w,X)d_N(X)X^{-\sigma N}C_N(X,Y)
                   d_N(Y)Y^{-N}C_N(Y,Z)
\]
is entire and one-periodic as a function of \(a\): it is a finite
Laurent polynomial in \(X=e^{-2\pi ia}\).
Its integral with density \(N\,da\) is therefore its original
constant coefficient integral. The two sector integrals add
exactly to (3), with no factor two or root-average convention.

Every part of (26) has a complete raw bound with reserve at least
\(3d/4\), before the finitely many adjustable source tolerances.
Choose their sum, including both endpoint continuations and
ordinary-color continuation, less than \(d/4\).
The remaining reserve exceeds \(1/1000000\).
All path lengths, row counts and the original density cost only
polynomial factors. This proves (6).

The first-connection proofs provide all-real ordinary-color bounds
for the cap profiles. On the two plateau pieces their same
coherent coefficient estimate can be inserted into the unchanged
cap contours, as in Section 6 of the positive first-left proof.
Its literal endpoint groups remain below the cap main profile.
The integer-weighted finite product has color degree less than \(N\);
Chebyshev continuation gives a fixed disk with arbitrarily small
exponential cost. Cauchy's formula on smaller disks gives the
fixed derivatives in the theorem. The outgoing modulus halfweight
is neither divided out nor differentiated.

The completed first polynomial is now controlled on the indicated
444 second shoulder. This does not give a nonzero full-period
coefficient, an estimate on the other second-coordinate pieces,
or a new knot family by itself.

## Direct source versions

The proof uses written inequalities only. No numerical mathematical
evaluation, test, import, compilation, or frozen-source edit is used.

| Direct source | SHA-256 | Implication used |
|---|---|---|
| research_mixed_444_first_unselected_positive_shoulder_main.md | 72f42d601fd30e30af4d3efdf3d1a0efb0d5834a4ffd3e9438ddf39ba26a38e7 | Actual reference and cap attachment with its original affine action |
| research_mixed_444_first_unselected_positive_shoulder_complete.md | 57c7d7ca3742be1bd7166c9b43d56b624ee467eecf909da7fa15130a69192103 | Every unselected plateau profile and the complete third kernel on the shoulder |
| research_mixed_444_double_selected_right_shoulder.md | 204313ab2b8d7e4076c516c6ee41b3a588504c4bf51530777a89deb7609792f1 | Every selected plateau profile and its complete finite-source bound |
| research_mixed_complete44_second_selected_first_left_connection.md | f91bbac2d0843fec8fd5e9ddc29b4d35efbbdf708f2e5bd8d4db6c686b58c702 | Cap-only margins; outgoing-independent selected transports, zero-face comparison, joins, real first interval and color bounds |
| research_mixed_complete44_second_selected_negative_left_connection.md | 878cbd67c6035f6fb9903e76d0b719cae599874d852710d979282e711d7fbf77 | Outgoing-independent negative transports and common-envelope height convexity |
| research_mixed_complete44_second_selected_right_half_connections.md | 49358cc1d991a59a8fbf38c64306e9d88e64b127e2e8a5229d741972036d00d5 | First right motion and real-half profile calibration, with changed outgoing guard checked here |
| research_mixed_443_complete_second_selected_right_shoulder.md | e001e0681e6e5cc52ff62040201f9bd9db6fa09b2a892a1e05495000287b8277 | Its first-kernel-only enlarged-domain barrier, finite corrections, unit-incoming branch and far-first all-index estimate; its type-three profile calibration is not used |
| research_mixed_all_angle_high_rows_with_small_positive_output.md | d74aecddc265f534d1a5af266df8565536e331f92ae36eef595cb3ab0dab2e0c | Complete finite high block without the former excess allowance |
| research_mixed_four_four_real_first_endpoint.md | 4ceec7f835d08ef971b3b3ccadcf7eecd74e48db3d422cbd09e5611c0572c122 | Arbitrarily small-cost continuation using the complete Laurent support |

The complete author proof and all nine directly used source implications
have been read, and all nine source hashes match. The final text has
been read back in full. Separate proof and direct-source review remains
required before adoption.

