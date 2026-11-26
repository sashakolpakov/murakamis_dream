# The unselected negative first-left connection with the second coordinate selected

Private written proof, 11 November 2026. For an actual word beginning
with \(443\) or \(444\), the original unselected first-coordinate
current is paid on
\[
 \frac1{10}\longrightarrow\frac1{10}+ic
                  \longrightarrow\frac9{20}+ic,
 \qquad c=\Im r_1<0,
 \tag{1}
\]
while the second coordinate remains on its selected plateau at height
\(1/100\). The third coordinate stays on its actual unselected
plateau. The first real interval from zero to one tenth is already
paid by the separate selected-left theorem, whose real-interval
conclusion permits either first Fourier monomial.

The reflected drift of the second factor can exceed one half here.
We do not apply the old exact half/last-row principle outside its
stated domain. Instead its written integral inequalities give a
small explicit excess over the maximum of those two rates. The
existing, stronger pointwise half- and last-row reserves absorb
that excess before finite summation.

## 1. Exact source, action and plateau anchors

Fix an actual positive three/four word of length \(m\ge4\) with
first flags \((1,1,\beta)\), \(\beta=0,1\). Retain the original
coupled reference, logarithmic lifts and external scalar. Put
\[
\begin{gathered}
 H=1/100,\quad P=[11/50,9/20],\quad
 r_1=a_0+ic,\quad .246<a_0<.350,\quad -.078<c<-.020,\\
 e_*=u_*+ih_e,\quad .333<u_*<.363,\quad
 -.051<h_e<-.019,\qquad -.102<h_s<-.001,\\
 a=x+ih,\quad y=b+iH,\quad z=v+i\Im r_3,
                         \qquad b,v\in P.
\end{gathered}
\tag{2}
\]
The second and third private indices are ordinary, including at
\(m=4\); the following external leg is attached at \(m=4\) and
ordinary thereafter. It remains in the original \(K_3\cup K_4\).
The ranges in (2) are necessary bounds on this actual reference,
not a replacement by an independent box reference.

With \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\),
\(p_j(X)=(q_NX;q_N)_j\), and \(X=e^{-2\pi ia}\),
\(Y=e^{-2\pi iy}\), \(Z=e^{-2\pi iz}\), retain
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}H_N(w,q_N^{-i})p_i(X)/P_i^2,\\
 C_{\epsilon,N}(X,Y)&=\sum_{j=0}^{N-1}
                  X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon},\\
 {\cal J}^{\,0}_N(w;a,y,z)&=
 U_{1,N}(w,X)C_{1,N}(X,Y)C_{\beta,N}(Y,Z)
                         d_N(X)d_N(Y)Y^{-N}.
\end{split}
\tag{3}
\]
Write \(R_{j,N}(a,y)=X^{-j}p_j(X)p_j(Y)/P_j^3\) for the
literal row of the second factor in (3).
The remaining allocation is \(|d_N(Z)|^{\beta/2}\), defined
to be one when \(\beta=0\). In particular (3) has no first
selected monomial. Neither of its whole Fourier polynomials is
divided out at a zero.

Use the original bare phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-\frac{i\pi}{2}(e-e^2),\\
 Q(s;a,y)&=g(s+a)+g(s+y)-3g(s)-g(a)-g(y)+2\pi ias.
\end{split}
\tag{4}
\]
Let \(L_1\) be the original allocated cap action, whose phase is
\(\Xi_1=\Psi-g(a)/2\). Let \(F_{23}\), \(p_L,p_R\) and
\(\Lambda_{23}\) be exactly (3)--(4) of the
[second-selected plateau completion](research_mixed_second_selected_plateau_completion.md).
The original stationarity gives \(L_1'(r_1)+p_L=0\). Therefore
\[
 \Lambda_{123}(z)=\Re L_1(r_1)+\Re F_{23,*}
                         +\Re\{p_R(z-r_3)\}
\tag{5}
\]
is precisely the same three-factor affine action used in the
double-selected source. No additive constant or peripheral
marginal is changed.

Write \(A_i(a)\), \(i=0,L,R,-,+\), for the original five bare
cap profiles: main private line \(u+ih_e\), real cuts \(.27,.49\),
lower line \(u-.055i\) with penalty \(.11\pi\), and upper line
\(u+.04i\) with penalty \(.08\pi\), with \(.27\le u\le.49\).
Include the separate true-end profile
\[
                  A_*=3/5+\log4/100<123/200.
\tag{6}
\]
It is independent of \(x,h\) for \(h\le0\). These are the
complete cap profiles of the
[fixed-height source](research_mixed_cap_early_fixed_height_full_source.md),
including its joins, aliases, physical tails and both true ends.
Its own-four extra upper-row allowance is zero.

For the second factor write \(R^2_0,R^2_L,R^2_R,R^2_1\) for
its bare main maximum on \([1/8,1/2]+ih_s\), real cuts
\(1/8,1/2\), and full-period last rate. The analogous third
profiles are \(R^3_k(y,z)\), \(k=0,L,R,1\). Set
\[
\begin{split}
 T_{k,\nu}(y,z)&=R^3_k(y,z)+W_2^\nu(y)-\frac\beta2\Re g(z),\\
 W_2^{\rm fac}(y)&=-\Re g(y)-2\pi H,\qquad
 W_2^{\rm force}(y)=0.
\end{split}
\tag{7}
\]
These quantities are constant while \(a,e,s\) vary. The last
allocation in (7) is the original unselected third halfweight;
there is no halfweight at the selected second coordinate, whose
whole polynomial has both displayed alternatives.

At \(a\in P+ic\), the
[four-profile reduction](research_mixed_second_selected_four_profile_reduction.md)
and its completed comparisons give, pointwise in \(k,\nu\),
\[
\begin{split}
 R^2_0-\tfrac12\Re g(a)+T_{k,\nu}
                        &\le\Lambda_{23}-\delta_\beta,\\
 R^2_L&<R^2_0-1/100,\qquad
 R^2_R<R^2_0-1/30,\qquad
 R^2_1<R^2_0-1/50,\\
 \delta_0&=1/400,\qquad\delta_1=1/3200.
\end{split}
\tag{8}
\]
For the first line, the right main and half profiles use their
completed central/half comparisons, the right left cut is dominated
by its main profile, and the right last profile has its separate
gap \(1/400\). Thus it holds for each of the four third profiles,
not merely for their signed finite sum. All these statements allow
the present positive outgoing height of factor 2.

The [complete cap plane](research_mixed_first_cap_plateau_completion.md)
pays each \(A_i-\Re g(a)/2\) individually at the actual
height \(c\). Its affine marginal cancels \(p_L\), retaining
the cap quadratic. At
\(a_c=11/50+ic\), multiplication with (8) yields
\[
 A_i(a_c)+R^2_j(a_c,y)-\Re g(a_c)+T_{k,\nu}
 \le\Lambda_{123}-\delta_\beta-d_j,
 \quad d_0=0, d_L=1/100, d_R=1/30, d_1=1/50.
\tag{9}
\]
We have dropped a nonnegative cap quadratic. The true-end version
of (9) has the additional reserve \(7/40\): the original bare
cap plane exceeds \(79/100\), whereas (6) is below \(123/200\).
The halfweight restoration is exactly that in Section 3 of the
[joint low-row proof](research_mixed_early_joint_low_tail.md).

## 2. The high physical rows with their correct nonzero drift

For \(c\le h\le0\), keep the full physical rate
\[
 E(t;a,y)=\int_0^t\log|1-e^{-2\pi i(a+s)}|\,ds
       +\int_0^t\log|1-e^{-2\pi i(y+s)}|\,ds
                            -3J(t)-2\pi ht.
\tag{10}
\]
Its continuous last rate is
\[
          E(1;a,y)=\lambda_h=2\pi(-h+H)<22\pi/125.
\tag{11}
\]
No value of a possibly zero finite last row is used.

For \(x\in[.1,.22]\), put \(v=1-t\), \(v_0=11/50\).
The exact reflected identity in the
[own-four high-row proof](research_mixed_early_own_four_high_rows.md)
now has the two radial primitives \(G_{|h|},G_H\) and drift
\(\lambda_h\). Its centered-arc and positive-interval
inequalities give, exactly as in (11)--(14) of that proof,
\[
 E(1-v)-E(1)\le2[J(v)-J(v/2)]-\lambda_hv\le0
                         \quad(0\le v\le v_0).
\tag{12}
\]
For \(v_0\le v\le1/2\), its separate all-angle leg inequality
gives
\[
 E(1-v)-E(1/2)\le J(v)+\lambda_h(1/2-v).
\tag{13}
\]
The right side is convex in \(v\), so its maximum is at
\(v_0\) or \(1/2\). The original alternating-series proof
gives \(J(v_0)<-4/(9\pi)<-14/99\). Also
\[
 (1/2-v_0)\lambda_h<\frac{154\pi}{3125}
                  <\frac{484}{3125}<\frac4{25}.
\]
Consequently, with
\[
       \eta_0=\frac4{25}-\frac{14}{99}=\frac{46}{2475}
                         <\frac1{50},
       \qquad\frac1{50}-\eta_0=\frac7{4950},
\tag{14}
\]
we have the complete continuous bound
\[
 \max_{1/2\le t\le1}E(t;a,y)
       \le\max\{E(1/2;a,y),E(1;a,y)\}+\eta_0.
\tag{15}
\]
The estimate does not assert that the maximum occurs at an endpoint.
Both changes of height and the chirp remain in (10)--(13).

Corollary 2 of the same source applies its zero-safe numerator
regularization and unchanged denominator factorial to every physical
index. The identical argument using (15) proves
\[
 \sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(a,y)|
 \le C_\tau N^{B_\tau}
   e^{N\{\max(E(1/2),E(1))+\eta_0+\tau\}}.
\tag{16}
\]
This includes both parity stops, all wrapped and revived rows, and
both endpoint groups. It compares integrated rates and divides no
finite numerator or Fourier value.

## 3. Transport of the main, low and half profiles

Keep the first height \(h=c\). For a cap point
\(e=u+i\xi\) in its entire retained rectangle and an ordinary
point \(s=t+i\eta\), \(1/8\le t\le1/2\), \(\eta\le0\),
write \(r=e^{2\pi c}\), \(R=e^{2\pi\xi}\),
\(q=e^{-2\pi\eta}\ge1\). Exact differentiation gives
\[
 \partial_x\Re\{\Psi(e,a)+Q(s;a,y)-g(a)\}
   =\log\frac{|1-rR e^{-2\pi i(u+x)}|
                   |q-r e^{-2\pi i(t+x)}|}
                  {|1-r e^{-2\pi ix}|^3}>0.
\tag{17}
\]
The strict inequality is the polynomial proof in Section 2 of the
[joint central source](research_mixed_early_joint_central_source.md).
It uses \(1/2<r<9/10\), \(R>2/3\), and the displayed real
intervals. Increasing \(q\ge1\) increases the second numerator.
Most importantly, the derivative and every inequality in that proof
are independent of \(y\). Thus this is a direct reuse of the
written pointwise calculation at the new outgoing height, not of
its former final theorem with \(d<0\).

For the true cap ends the derivative is instead
\[
                 \log\frac{|q-r e^{-2\pi i(t+x)}|}
                                  {|1-r e^{-2\pi ix}|^2}
                            >-\log2.
\tag{18}
\]
Indeed the numerator exceeds the single denominator because
\(x<t+x<1-x\); it increases with \(q\), and the remaining
denominator is below two. The total possible backward loss on
\([.1,.22]\) is less than \((3/25)\log2<21/250\), smaller
than the reserve \(7/40\) in (9).

At \(x=.22\), the original positive-outgoing ordinary contour
proof in the [second-selection reduction](research_mixed_second_selected_plateau_reduction.md)
bounds each downward zero-mode join by its main-line or real-cut
endpoint. It applies on the full printed outer-height box and uses
the actual unchanged \(h_s<0\). Each endpoint is paid by (9).
Apply (17)--(18) pointwise along the entire same join while moving
\(x\) left. Hence the main line, both joins and both real cuts,
with every cap alternative, are paid by
\(\Lambda_{123}-\delta_\beta\). For the half profile the
extra reserve \(1/30\) is retained; for the left cut \(1/100\)
is retained. The larger true-end reserve pays its transport cost
without using either of these extra row reserves.

The original low-row recurrence applies on the independent
outgoing-height interval \([-.102,.068]\), which contains \(H\).
It reduces the literal low block \(0\le j\le\lfloor N/8\rfloor\)
to its left cut. No reference height is changed in that recurrence.

## 4. Cap times the last rate: an outgoing-independent transport

Here \(E(1;a,y)=2\pi(-c+H)\) is independent of \(x\).
For a regular cap point the exact joint derivative is
\[
 \partial_x\{\Re\Psi(e,a)-\mathfrak p_e-\Re g(a)+E(1;a,y)\}
                  =\log(N_e/D^2),
 \quad N_e=|1-r e^{2\pi\xi}e^{-2\pi i(u+x)}|,
 \quad D=|1-r e^{-2\pi ix}|.
\tag{19}
\]
The first-four/three last-row proof contains a cap-only argument
for this derivative. We explicitly check its extension to the
present \(c>-.078\), rather than invoking its narrower theorem.

First the main maximum is attained at \(u\le.43\). The exact
endpoint radical and its original branch, used in Section 2 of
that [last-row proof](research_mixed_first_four_three_true_last_row_calibration.md),
give at the real point \(e=.43\)
\[
 \Re\Xi_{1,e}(.43,a)
 <-\log(39/20)-1/50+231\pi/2600.
\tag{20}
\]
This estimate uses only \(c<-1/50\), through the increasing
function \(\log\cosh(\pi c)+\pi c\), and the unchanged
interval \(.53\le\Re(e+a)\le.65\). On
\(e=.43+i\xi\), \(-.051\le\xi\le0\), its exact radical
argument proof gives \(\Im S''<\pi/10\). Both \(e\) and
\(e+a\) have nonpositive height; the latter has negative cosine
of twice its real angle, so \(0\le\Im\cot\pi(e+a)<1\),
regardless of how far \(c\) lies below \(-.07\). Thus
\(\Im\Xi_{1,ee}<21\pi/10\) on this whole segment. Downward
transport raises (20) by less than \(17/50\). The same rational
logarithm and angle bounds as in that proof yield
\[
                    \Re\Xi_{1,e}(.43+ih_e,a)<-1/25.
\tag{21}
\]
The [joint cap curvature](research_mixed_cap_joint_early_horizontal_concavity.md)
holds on the larger outgoing-height interval \([-.108,.021]\),
so its private concavity excludes every \(u>.43\) from the
main maximum. No equation involving the next own type was used.

Now \(e^{2\pi h_e}>18/25\), \(r<9/10\), and \(u\le.43\).
For \(x\le.16\), \(D^2<1\) and \(N_e>1\). For
\(.16\le x\le.22\), the same written trigonometric witnesses
give
\[
 N_e^2>1+324r^2/625+21r/25,\qquad
 D^2<1+r^2-28r/75.
\]
Their difference after squaring the second bound is \(rQ(r)\),
where
\[
 Q(r)=119/75-(9118/5625)r+(56/75)r^2-r^3>0.
\tag{22}
\]
The derivative discriminant is \(-96872/5625<0\), and
\(Q(9/10)=269/75000>0\). Hence every retained main point
increases in \(x\) after adding the last rate and full first
weight.

For both real cuts and the upper alias, the private radius is
at least one. The original angular bounds on the full private
interval yield
\[
 N_e^2-D^4>
 r\{6/5-(706/625)r+(18/25)r^2-r^3\}>0.
\tag{23}
\]
This cubic decreases, since its derivative discriminant is
\((1296-8472)/625<0\); its value at \(9/10\) is
\(939/25000>0\). Their exact penalties stay unchanged.

The lower alias is handled before any transport by the same
source-specific derivative identity:
\[
 \Im\Xi_{1,e}<59\pi/50
 \quad\Longrightarrow\quad
 \Re\Xi_1(u-.055i,a)-.11\pi
 <\Re\Xi_1(u+ih_e,a)-211\pi/3125.
\tag{24}
\]
Its proof uses only the original complete-end root chamber,
the regular real sine arguments, and \(\Re a\ge.1\).
In particular it has no lower bound \(-.07\) on \(c\).
The interval length is less than \(9/250\). Equation (24)
therefore holds on the current entire interval; (21) bounds the
whole main maximum after the comparison.

For the true ends the derivative in (19) is \(-\log D>-1/4\),
because \(D^2<1+r^2-9r/25\le743/500<3/2\).
Its backward cost is less than \(3/100\). At the comparison
point \(x=.22\), the extra true-end reserve \(7/40\) in (9)
therefore still leaves \(29/200\).

We have proved, for every complete cap alternative,
\[
 A_i(a)+E(1;a,y)-\Re g(a)+T_{k,\nu}
                 \le\Lambda_{123}-\delta_\beta-1/50
                  \qquad(.1\le x\le.22, h=c).
\tag{25}
\]
For the regular main/cuts/upper alias this transports their own
old-face values in (9); the lower alias uses (24) and that main
bound. The separate true-end reserve pays its transport loss.
The positive \(2\pi H\) in the last rate was retained throughout
and contributes zero to (19); it is already present in the
plateau last-row comparison (8).

Combining the retained half reserve \(1/30\), (25), and (15)
shows that every high profile on the negative horizontal is
below \(\Lambda_{123}-\delta_\beta-7/4950\).
Equation (16) upgrades this to the complete finite high block.

## 5. Every ordinary correction on the negative horizontal

Use the same central rows and contours as in the
[joint central source](research_mixed_early_joint_central_source.md):
\[
\begin{array}{c|c}
 \text{physical central block}&\lfloor N/8\rfloor<j<\lceil N/2\rceil\\
 \text{main}&[1/8,1/2]+ih_s\\
 \text{lower and upper aliases}&[1/8,1/2]-i/5,\quad[1/8,1/2]+4i .
\end{array}
\tag{26}
\]
Retain both unweighted joins and all four weighted vertical halves.
The proof of its argument bounds does not use the outgoing height:
each shifted argument is bounded at every radius on its regular
strip. It uses \(c>-.078\), the real intervals, and \(h_s<0\).
Thus at the present \(y=b+iH\) it still gives
\[
 -11\pi/5<\Im Q_s<53\pi/50,\qquad
                  \Im Q_s>-77\pi/40\quad(\Im s\ge0).
\tag{27}
\]
The lower alias is below the same main point by \(47\pi/250\).
For the upper alias the total added rate, including the whole
sampling penalty, is less than
\[
 (11/5)(27/250)\pi+4(77/40)\pi-8\pi=-39\pi/625.
\tag{28}
\]
The lower and upper vertical alias halves decrease away from
their real cuts, by (27). The main and unweighted joins were
already paid in Section 3. These are pointwise comparisons
before multiplying any of the cap or third-factor profiles.

All real factorial arguments stay in the same compact regular
strips; the [exact factorial theorem](exact_factorial_interpolation_and_complex_contours.md)
permits every fixed compact imaginary interval, including height
four. Its original marked interpolant and cotangent formula have
coefficient \(N/(2i)\), constant-mode density \(+N\), and
the original residue signs. Thus (26)--(28), (16), and the low
block form a complete finite partition through \(N-1\), at both
parities.

For \(h=c<0\), the unselected first Fourier upper rate is
\(W_0(a)=\max\{-\Re g(a),0\}=-\Re g(a)\).
Both alternatives are retained by this inequality; no selected
first monomial has been inserted. Multiplication by (7), with
both second alternatives, proves the full horizontal bound
\[
 |{\cal J}^{\,0}_N(w;a,y,z)|\,|d_N(Z)|^{\beta/2}
       \le C_\tau N^{B_\tau}
                e^{N\{\Lambda_{123}-\delta_\beta+\tau\}}
                   \quad(.1\le x\le.22, h=c).
\tag{29}
\]
On \(.22\le x\le.45\), the original singly selected plateau
completion and complete cap plane give the same bound. This uses
the original tangent cancellation in (5) and all half allocations,
not a two-factor theorem with the outgoing height silently changed.

## 6. The vertical face at one tenth

Keep \(x=.1\) and \(c\le h\le0\). Use the common raw
envelope of the
[negative-height face proof](research_mixed_first_four_four_negative_height_face.md):
the five cap profiles and constant (6), every ordinary point in
(26), both unweighted joins, all four weighted vertical halves,
every physical rate \(E(t)\) with \(.5\le t\le.9\), and
the last carrier \(\lambda_h=2\pi(-h+H)\). Add the complete
first Fourier rate \(W_0\) and each fixed \(T_{k,\nu}\).
No outgoing half allocation at \(y\) is borrowed.

This is a complete envelope at every intermediate height. The low
row ratio still applies at positive outgoing height \(H\). The
central interpolation keeps all its currents. For \(t\ge.9\),
the same reflection integral proof, using \(1-t\le.1\le b\),
gives
\[
                    E(t)-E(1)\le J(1-t)-\lambda_h(1-t)\le0.
\tag{30}
\]
Thus the raw high collection and affine last carrier cover all
physical high rows, without invoking (15) at interior heights.

Every height-convexity calculation in Sections 2--3 of that face
proof is independent of the outgoing \(y\). In particular
\[
 \Re\cot\pi(.1+ih)>245/144>3/2,
 \qquad \Re\cot\pi(t+i\eta)\le3/2\quad(1/5\le t<1),
\]
and the two second derivatives for each fixed private point are
\[
\begin{split}
 \partial_h^2\Re\Psi(e,a)
 &=\pi\{\Re\cot\pi a-\Re\cot\pi(e+a)\}>0,\\
 \partial_h^2\Re Q(s;a,y)
 &=\pi\{\Re\cot\pi a-\Re\cot\pi(s+a)\}>0.
\end{split}
\tag{31}
\]
This includes the full upper sides through height four. For
\(.5\le t<.9\), the first physical numerator has no wall,
and its same second derivative is positive. Continuity handles
\(t=.9,h=0\). The second numerator is independent of \(h\).
The true-end rate is constant, \(\lambda_h\) is affine, and
\(W_0\) is the maximum of two convex functions. The full raw
envelope is therefore convex on \([c,0]\).

At \(h=c\), Sections 3--5 pay every member of this envelope
by \(\Lambda_{123}-\delta_\beta\), including all raw high
profiles and the stronger last reserve. At \(h=0\), Sections
4--6 of the [selected-left theorem](research_mixed_complete44_second_selected_first_left_connection.md)
pay every member with the raw zero-face gap \(3/1000+1/2000\).
That zero-face construction originally uses upper height two,
but its pointwise bound \(\Im Q_s\ge-77\pi/40\) for every
positive private height makes the weighted upper rate decrease
above two. Hence the additional horizontal and vertical pieces
through height four are also paid. At \(h=0\) the selected and
unselected first monomials have the same modulus; the first Fourier
rate is exactly \(W_0(0)\).

The smaller of these two endpoint reserves is at least \(1/3200\).
Convexity therefore pays the complete vertical source by
\(\Lambda_{123}-1/3200\), with its full original finite inventory.

## 7. Colors, complete path and scope

All cap envelopes above hold for every real ordinary color. The
early complete cap theorem states this directly. On the old
unselected plateau use the
[whole endpoint real-color theorem](research_mixed_endpoint_real_color_decay.md):
its coherent coefficient bound holds throughout the original cap
wire rectangle, and its compact physical assertion includes both
halves. Both literal endpoint groups retain their old ceilings,
below the bare cap plane. This is the same direct finite-source
replacement used in Section 6 of the selected-left theorem, now
at a negative first height. It gives all-real color control before
any complex continuation. The other factors are independent of
that color.

**Theorem.** On the oriented path (1), for every \(\tau>0\),
both level parities satisfy
\[
 |{\cal J}^{\,0}_N(w;a,y,z)|\,|d_N(Z)|^{\beta/2}
 \le C_\tau N^{B_\tau}
              e^{N\{\Lambda_{123}(z)-1/6400+\tau\}}.
\tag{32}
\]
This holds uniformly for \(b,v\in P\), every actual reference
in (2), and all real ordinary colors \(w\in[-2,2]\). It also
holds on sufficiently small fixed ordinary-color disks about
\(-2\), with every fixed jet on smaller disks and polynomial cost.

Indeed the raw bounds above leave at least \(1/3200\). Allocate
their finitely many source tolerances within the spare half and
the displayed \(\tau\). The exact source is a polynomial of
degree less than \(N\) in \(w\). The interval continuation and
Cauchy argument in the
[horizontal complex-extension theorem](research_mixed_horizontal_complex_extension.md)
give the stated disks and derivatives with arbitrarily small
additional rate cost. Carry every color-independent factor,
including the outgoing modulus halfweight, as a multiplier; none
is divided out or differentiated.

The already proved real segment \(0\to.1\) from the selected-left
theorem can be prepended, since that segment permits the first
unselected monomial. Integrating (32) with the unchanged \(+N\,da\)
density costs only a polynomial, as does a subsequent selected
second-plateau integral with its original \(+N\,dy\). The
external scalar, whole first and second Fourier polynomials,
both upper alternatives, third outgoing halfweight, and all
finite signs remain those of (3).

This pays the unselected first-left path with the second coordinate
selected. It asserts no full second-period packet, nonzero signed
coefficient, other second-coordinate region, or whole-word/knot
theorem. The separate selected-first and right-connection results
keep their own exact hypotheses.

## Direct source bindings

The complete written proof and the directly used source implications
were read. No mathematical numerical evaluation, saved-value
arithmetic, import, test, compilation or frozen-source edit is used.

| Source | SHA-256 |
|---|---|
| research_mixed_second_selected_plateau_completion.md | f11d52d95fdf9cd87976ef5979a81d0009e151586051bdca2ddf0424329765df |
| research_mixed_second_selected_four_profile_reduction.md | d084b535d83a08e50c4baddc52249c8495d88cde65f8c81e04baff566560d25e |
| research_mixed_second_selected_plateau_reduction.md | 015c85c322ff3563ec6752b5c499080c3e906360920aaeed2063508ef2db868f |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_first_four_three_true_last_row_calibration.md | a1571017529473e88dad8c0f5ec4f3592984a19040962e8279ca9dadb92257de |
| research_mixed_cap_joint_early_horizontal_concavity.md | 1b623741d70402af77287b287aa1e2636b0b8d1abcb7275d5347f14ac75dbb20 |
| research_mixed_early_own_four_high_rows.md | 62c3d5070d15c093ae8ab10cb373e9624a497d29743d6cd909bc5d7a33daebb6 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_first_four_four_negative_height_face.md | f50598305505a5dde4537fc15d6ed114b8e3a01eb87d69cff5ac36e0829b40a3 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_complete44_second_selected_first_left_connection.md | f91bbac2d0843fec8fd5e9ddc29b4d35efbbdf708f2e5bd8d4db6c686b58c702 |
| research_mixed_endpoint_real_color_decay.md | 44921926dbdccef49c84e02566e86cf175979c8f189e62c7ba2e9b92c0d577eb |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
