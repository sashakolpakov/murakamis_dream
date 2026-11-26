# The selected first left connection with the second coordinate selected

Private written proof, 11 November 2026. For an actual word beginning
with \(443\) or \(444\), the complete three-factor source is paid on
the connected first-coordinate path
\[
 0\longrightarrow\frac1{10}\longrightarrow\frac1{10}+\frac{i}{100}
                   \longrightarrow\frac9{20}+\frac{i}{100},
 \tag{1}
\]
while the second coordinate stays on its selected plateau and the
third stays on its original unselected plateau. The first Fourier
sector on the nonreal path is the selected one.

The proof extends the earlier first44 left estimates to a positive
second target height. It does not use their former negative-outgoing
height hypothesis without checking it. The new physical-row step is
a half/last-row principle with a nonzero, small reflected drift;
the last rate is then strictly below the real left-cut rate.
The first unselected negative-height connection and the rest of the
second period are not asserted here.

## 1. Literal source and the existing central anchor

Fix an actual positive three/four word of length \(m\ge4\) with
first flags \((1,1,\beta)\), \(\beta=0,1\). All reference coordinates,
logarithmic lifts and scalar conventions remain original. Put
\[
 H=1/100,\quad P=[11/50,9/20],\quad
 a=x+ih,\quad y=b+iH,\quad z=v+i\Im r_3,\quad b,v\in P.
 \tag{2}
\]
The actual cap and second conditional summation heights satisfy
\[
 h_e\in[-.051,-.019],\qquad h_s\in[-.108,-.001].
 \tag{3}
\]
The reference is still the actual coupled one. In particular the
second and third conditional indices are ordinary also at \(m=4\),
and their following reference is in the original \(K_3\cup K_4\),
attached at \(m=4\).

Write \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iy}\), \(Z=e^{-2\pi iz}\),
\(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\), and
\(p_j(X)=(q_NX;q_N)_j\). Retain
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i<N}H_N(w,q_N^{-i})p_i(X)/P_i^2,\\
 C_{\epsilon,N}(X,Y)&=\sum_{j<N}
                  X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon},\\
 {\cal J}_{N}(w;a,y,z)&=
 U_{1,N}(w,X)C_{1,N}(X,Y)C_{\beta,N}(Y,Z)
                  d_N(X)X^{-N}d_N(Y)Y^{-N}.
\end{split}
 \tag{4}
\]
The coefficient \(H_N\) is complete. The remaining allocation is
\(|d_N(Z)|^{\beta/2}\), defined as one for \(\beta=0\).
No polynomial is divided out at its zeros.

Let \(\Lambda_{123}(z)\) be the original affine action (3) of
the [double-selected plateau completion](research_mixed_double_selected_plateau_completion.md).
Its complete finite source on
\(a\in P+iH,\ y\in P+iH,\ z\in P+i\Im r_3\) has raw gap
\[
                              d_{12}=3/1000.
 \tag{5}
\]
We use the individual profile inequalities in its proof, not a
putative inference from the modulus of a cancelling sum.

Use the original bare phases
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-\frac{i\pi}{2}(e-e^2),\\
 Q(s;a,y)&=g(s+a)+g(s+y)-3g(s)-g(a)-g(y)+2\pi ias.
\end{split}
 \tag{6}
\]
Let \(A_0,A_L,A_R,A_-,A_+\) be the cap profiles at private
heights \(h_e,0,0,-.055,.04\), respectively, with original
penalties \(0,0,0,.11\pi,.08\pi\), and private real interval
\([.27,.49]\). The two real-cut profiles are evaluated at
\(e=.27,.49\), respectively; only the horizontal profiles take
a maximum over that interval. Add the true-end ceiling
\[
                A_*(h)=3/5+2\pi h+\log4/100
                     \qquad(0\le h\le H).
 \tag{7}
\]
For the second factor use the bare profiles
\[
\begin{split}
 B_0(a,y)&=\max_{1/8\le t\le1/2}\Re Q(t+ih_s;a,y),\\
 B_L(a,y)&=\Re Q(1/8;a,y),\qquad
 B_R(a,y)=\Re Q(1/2;a,y).
\end{split}
 \tag{8}
\]
There is no outgoing halfweight in (8): the whole second weight
will be restored in the following constants. Let \(R_k^3(y,z)\),
\(k=0,L,R,1\), be the original four profiles of factor 3, and set
\[
\begin{split}
 W_2^{\rm fac}(y)&=-\Re g(y)-2\pi H,\qquad W_2^{\rm force}(y)=0,\\
 T_{k,\nu}(y,z)&=R_k^3(y,z)+W_2^\nu(y)-\tfrac{\beta}{2}\Re g(z),\\
 W_1(a)&=\max\{-\Re g(a)-2\pi h,0\}.
\end{split}
 \tag{9}
\]
The \(T_{k,\nu}\) are constant as \(a,e,s\) vary. Their two
second Fourier alternatives are never identified or discarded.

At \(a_+=11/50+iH\), for every \(i\in\{0,L,R,-,+,*\}\),
\(j\in\{0,L,R\}\), and \(k,\nu\), the old profile proofs give
\[
 A_i(a_+)+B_j(a_+,y)+W_1(a_+)+T_{k,\nu}(y,z)
                  \le\Lambda_{123}(z)-d_{12}.
 \tag{10}
\]
Here is the precise source passage. The double-selected completion
pays the main and left-cut cap profiles, both first Fourier
alternatives and all right profiles, with gap (5). Its
[last-row proof](research_mixed_double_selected_last_rows.md)
pays the separate right-last-row terms. The
[four-profile reduction](research_mixed_second_selected_four_profile_reduction.md)
dominates every non-main profile of factor 2 by its main profile
at these selected heights. Finally the cap-only comparisons
(9), (12) of the
[early complete44 source](research_mixed_selected_four_four_early_complete_source.md)
give
\[
 A_-,A_+<A_0-1/10,\quad A_R<A_0-1/1250,\quad
 A_0(a_+)>199/250,\quad A_*(H)<69/100.
 \tag{11}
\]
Those assertions involve no outgoing coordinate of the ordinary
factor. Thus they supply the other cap profiles in (10), including
the true ends with reserve greater than \(53/500\).
This justifies the entire Cartesian product in (10).

## 2. High rows at a positive outgoing height

For \(0\le x\le11/50\), \(0\le h\le H\), keep the full
own-four real-row rate
\[
 E(t;a,y)=\int_0^t\log|1-e^{-2\pi i(a+s)}|\,ds
       +\int_0^t\log|1-e^{-2\pi i(y+s)}|\,ds
                       -3J(t)-2\pi ht .
 \tag{12}
\]
All zeros are integrated. Its full-period value is
\[
                        E(1;a,y)=2\pi H=:\lambda<1/2.
 \tag{13}
\]
Indeed the two full numerator integrals are \(2\pi h\) and
\(2\pi H\), and the original chirp cancels the first.

We extend the proof, rather than the stated \(d\le0\) domain, of
the [own-four high-row theorem](research_mixed_early_own_four_high_rows.md).
For \(G_\eta(t)=\Re g(t-i\eta)\), its exact reflection identity is
\[
\begin{split}
 E(1-v)-E(1)
   =G_h(x-v)-G_h(x)+G_H(b-v)-G_H(b)+3J(v)-\lambda v .
\end{split}
 \tag{14}
\]
For \(0\le v\le v_0=11/50\), the centered minimum-arc
inequality and \(v\le b\) give
\[
 G_h(x-v)-G_h(x)\le-2J(v/2),\qquad
 G_H(b-v)-G_H(b)\le-J(v).
 \tag{15}
\]
The first interval is inside \([-1/2,1/2]\) also when \(x<1/10\).
Exactly as in equations (13)--(14) of that source, Jensen's
inequality then bounds (14) by
\(2[J(v)-J(v/2)]-\lambda v\le0\), since \(v_0<2/9\).
For \(v_0\le v\le1/2\), its all-angle two-leg comparison gives
\[
 E(1-v)-E(1/2)\le J(v)+\lambda(1/2-v)\le0.
 \tag{16}
\]
The last inequality is the same written chord bound:
\(-J(v_0)/(1/2-v_0)>100/(63\pi)>1/2>\lambda\).
It has no sign assumption on either original height after (14)
has been written with its correct drift. Therefore
\[
 \max_{1/2\le t\le1}E(t;a,y)
                 =\max\{E(1/2;a,y),2\pi H\}.
 \tag{17}
\]
Continuity includes \(x=0\) and \(h=0\).
The zero-safe uniform product argument of that source's
Corollary 2 now gives, at both parities,
\[
 \sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(a,y)|
 \le C_\tau N^{B_\tau}
          e^{N\{\max(E(1/2;a,y),2\pi H)+\tau\}} .
 \tag{18}
\]
Every wrapped and revived row is retained, with the literal stop
\(N-1\). No finite half row or last row is divided out.

The new last alternative is itself paid by the real left cut.
For \(1/10\le x\le11/50\), \(0\le h\le H\), put \(\ell=1/8\).
The exact cut formula gives
\[
 B_L=\int_0^\ell\log|1-e^{-2\pi i(a+t)}|\,dt
       +\int_0^\ell\log|1-e^{-2\pi i(y+t)}|\,dt
                     -3J(\ell)-2\pi h\ell .
 \tag{19}
\]
Both radii are at least one. On the first real interval
\([.1,.345]\), \(2\sin\pi t>3/5\); at its smaller endpoint
this follows from \(2\sin(\pi/10)=(\sqrt5-1)/2>3/5\).
On the second interval \([.22,.575]\), \(2\sin\pi t>5/4\).
Using the written logarithmic bounds
\(\log(3/5)>-3/5\), \(\log(5/4)>2/9\), and
\(-3J(1/8)>93/200\), we obtain
\[
 B_L>\frac{93}{200}-\frac3{40}+\frac1{36}
                         -\frac{\pi}{400}>\frac38.
 \tag{20}
\]
The sine and denominator witnesses for these last bounds are
the elementary ones in the near-one first-arc comparison:
\(\sin(.22\pi)>\sin(11/16)>5/8\), \(\sin\pi t\le\pi t\),
\(\pi<22/7\), and \(\log(14/11)>6/25\).
Also \(\log(3/5)>-3/5\) follows from
\(e^{3/5}>1+3/5+(3/5)^2/2>5/3\).

For the real first segment \(0\le x\le1/10\), the first
integral in (19) is at least \(J(\ell)\), since
\(\log(2\sin\pi t)\) increases on \([0,.225]\).
Thus at \(h=0\),
\[
              B_L>\frac{31}{100}+\frac1{36}>\frac13.
 \tag{21}
\]
Since \(2\pi H<2/25\), equations (20)--(21) imply, on both
domains where they will be used,
\[
                          2\pi H<B_L-\frac14 .
 \tag{22}
\]
Consequently all high rows are bounded by \(\max(B_L,B_R)\).
This replaces the zero-drift step of the old early and real-interval
proofs; that zero-drift hypothesis would be false here.

## 3. Extending the selected horizontal interval to one tenth

The cap source and all cap-only inequalities (11) apply throughout
\(a=x+iH\), \(1/10\le x\le11/50\). The
[independent-height cap theorem](research_mixed_cap_early_fixed_height_full_source.md)
has exactly this outgoing rectangle, with zero extra allowance for
own type four and all-real ordinary-color scope.

We verify the changed outgoing height in the main-current argument.
After subtracting the constant outgoing allocation, its objective is
\[
                       f(e,s,x)=\Re\{\Psi(e,a)+Q(s;a,y)-g(a)\}.
 \tag{23}
\]
The fixed-\(y\) Hessian proof in Sections 2--3 of the
[early44 central theorem](research_mixed_selected_four_four_early_central.md)
remains valid. Its cap Schur complement exceeds \(A=\Re\cot\pi a\);
its ordinary guards are
\[
 U>\tfrac12u_0,\quad A>\tfrac{13}{20}p_0,\qquad
 u_0=\cot\pi\Re s,\quad p_0=\cot\pi x.
 \tag{24}
\]
The first strict inequality in (24) is used for
\(\Re s<1/2\); at the endpoint \(U=u_0=0\).
The bounds use only \(|\Im s|\le.108\) and \(H=.01\).
For \(C=\Re\cot\pi(s+a)>0\), its explicit determinant test is
\[
 \frac1{2U}+\frac1{(5/2)A}
 <\frac1{u_0}+\frac8{13p_0}
 <\frac{u_0+p_0}{u_0p_0-1}.
 \tag{25}
\]
If \(C\le0\), positivity is immediate, including at
\(\Re s=1/2\). The remaining fixed-\(y\) entry is
\(U-\Re\cot\pi(s+y)>0\): for a positive shifted cotangent,
\[
 \Re\cot\pi(s+y)
 \le\frac{u_0p_b-1}{u_0+p_b}<u_0/2,\qquad
                  p_b=\cot\pi b<4/3 .
 \tag{26}
\]
This uses no sign of \(\Im y\). Therefore the joint real
concavity in \((\Re e,\Re s,x)\) is unchanged.

At \(x=11/50\), the pointwise proof of the
[optimizer bounds](research_mixed_selected_boundary_optimizer_bounds.md)
allows the full outgoing target-height interval \([-.108,.068]\);
its height-endpoint argument, not an actual-height substitution,
proves \(\Re e<.4,\ \Re s<.44\) for every maximizer also at
\(\Im y=H\). The first-coordinate derivative is
\[
 f_x=\log(N_eN_s/D^3),\quad
 N_e=|1-rR e^{-2\pi i(\Re e+x)}|,\quad
 N_s=|q-r e^{-2\pi i(\Re s+x)}|,
 \tag{27}
\]
where \(r=e^{2\pi H}<43/40,\ R=e^{2\pi h_e}>18/25,\)
\(q=e^{-2\pi h_s}\ge1,\ D=|1-r e^{-2\pi ix}|\).
The original written bounds at that face,
\[
 N_e^2/r>9/4,\qquad N_s^2/r>3,\qquad
 D^6/r^2<387/80<27/4,
 \tag{28}
\]
are independent of \(y\). Concavity and the supporting tangent
therefore transport the main/main maximum from \(x=11/50\)
to every \(x\in[1/10,11/50]\), without increasing it.

For the complementary cap and real ordinary profiles, equations
(14)--(26) of the
[early complete44 proof](research_mixed_selected_four_four_early_complete_source.md)
also transport pointwise: their exact derivative is (27), and it
does not involve \(y\). Their bounds use \(q\ge1\), the cap-only
restriction \(\Re e\le.43\), and the two real cuts \(1/8,1/2\).
For clarity the relevant positive-product witnesses are
\[
\begin{array}{c|c}
 \text{profile pair}&\text{bound compared with }D^6/r^2<569/120\\ \hline
 A_0,\ B_R&N_e^2N_s^2/r^2>267/50\\
 A_0,\ B_L,\ x\ge.16&N_e^2N_s^2/r^2>27/5\\
 A_L,\ B_0,B_L,B_R&N_e^2N_s^2/r^2>50/9 .
\end{array}
 \tag{29}
\]
For \(B_L,\ x\le.16\), that proof instead uses
\(D^6/r^2<6/5\) and \(N_e^2/r>9/4,\ N_s^2/r>5/3\).
The cap aliases and right cut are dominated as in (11).
For the true-end sector its derivative is
\(\log(N_s/D^2)>-3/5\); the backward loss \(9/125\) is
smaller than the reserve \(53/500\) in (11), leaving \(17/500\).
None of these calculations uses the sign of the second target height.

On the early interval the first factorial alternative dominates
the forced one by \(3/40\), as in equation (20) of the central
theorem. Applying the original anchor (10) separately to each
unchanged constant \(T_{k,\nu}\) proves
\[
 A_i(a)+B_j(a,y)+W_1(a)+T_{k,\nu}
                    \le\Lambda_{123}(z)-d_{12}
 \quad(a\in[.1,.22]+iH).
 \tag{30}
\]
This is a profile statement, including the separate true ends.

## 4. Ordinary contours, zero face, and positive vertical join

The exact ordinary partition is
\[
 0\le j\le\lfloor N/8\rfloor,\qquad
 \lfloor N/8\rfloor<j<\lceil N/2\rceil,\qquad
 \lceil N/2\rceil\le j<N.
 \tag{31}
\]
The [low-row recurrence](research_mixed_first_attached_low_row_transport.md)
explicitly allows outgoing heights \([-.102,.068]\); it applies
at \(H\), with ratio greater than \(e^{1/200}\).
Thus the low block is reduced to its real cut, including \(j=0\).
The high block is paid by (18), (22).

On the central block retain half-grid cuts at \(1/8,1/2\),
lower alias height \(-1/5\), upper height \(2\), and original
zero-mode height \(h_s\). The real factorial arguments satisfy
\[
 \Re(s+a)\in[.225,.72],\qquad
 \Re(s+y)\in[.345,.95].
 \tag{32}
\]
The [exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md)
permits any fixed compact imaginary interval. The original
[cotangent identity](research_mixed_horizontal_asymmetric_contour.md),
Section 4, therefore has its same coefficient \(N/(2i)\),
zero-mode density \(+N\), both unweighted joins, two horizontal
aliases and four vertical alias halves.

The own-four argument table (29)--(33) of the early complete44
proof is valid at the present outgoing height. It uses only the
ordering \(x\le b\), regular real sums, and the incoming sign
\(h\ge0\); it never uses a sign of the second height. For
\(I=\Im Q_s\) at private height \(\eta\), it gives
\[
 I\le53\pi/50,\qquad
 I\ge-43\pi/40\ (\eta\le0),\qquad
 I\ge-77\pi/40\ (\eta\ge0).
 \tag{33}
\]
Consequently the horizontal aliases are below the same main
point by \(47\pi/250\) and \(339\pi/10000\), respectively;
all vertical alias halves are below their real-cut endpoints.
The unweighted joins use heights between \(h_s\) and zero.
Write \(C=\Re\cot\pi(s+a)\) and \(C_y=\Re\cot\pi(s+y)\).
If \(C>0\), then
\(C\le\cot\pi(\Re s+x)<u_0<2U\); if \(C\le0\), the
same positivity of \(2U-C\) is immediate. Equation (26) gives
\(U-C_y>0\). Thus the bare ordinary phase, without borrowing
any cap curvature, satisfies
\[
              -\Re Q_{ss}/\pi=(2U-C)+(U-C_y)>0.
\]
At \(\Re s=1/2\), both shifted cotangents are negative, so the
same conclusion holds with \(U=0\). Vertical convexity therefore
bounds the unweighted joins by main/cut endpoints.
These facts prove the full finite source from (30).

At \(a=1/10\), the proof of the
[zero-height face](research_mixed_selected_four_four_zero_height_face.md)
transports each regular cap point and each ordinary main point or
real cut from \(a_+=.22+iH\). Its horizontal gain exceeds \(7/100\);
its height-reset cost is at most \(109\pi/5000\), leaving
\[
                  7/100-109\pi/5000>1/2000.
 \tag{34}
\]
Both derivatives in that proof are independent of \(y\):
they differentiate only \(g(e+a)+g(s+a)-3g(a)+2\pi ias\).
The true-end counterpart has gain greater than \(3/100\) and
reset cost at most \(11\pi/2500\), again leaving more than
\(1/2000\). Its affine \(2\pi h\) cancels the selected monomial
exactly. Thus the proof transfers (10) to the zero face with
gap \(d_{12}+1/2000\), for every cap profile and every ordinary
main/cut profile and every \(T_{k,\nu}\).
The aliases and joins follow from (33) and (24)--(26) at \(h=0\);
the high rows follow from (17), (22). No old zero-drift claim
is used.

Finally take the common raw envelope of the
[positive-join theorem](research_mixed_first_positive_join_convex_envelope.md):
its six cap profiles, every ordinary main/join/alias rate with its
exact penalty, every real high rate \(E(t)\), \(1/2\le t\le9/10\),
and the last rate \(2\pi H\). Remove that theorem's outgoing
half allocation and instead add each constant \(T_{k,\nu}\).
Its complete-source proof applies at \(\Im y=H\): low rows use
the just-checked box; all real factorial strips are unchanged;
the final rows \(t\ge9/10\) obey its reflection inequality with
the retained drift \(2\pi H\).
Its height-convexity identities are
\[
\begin{split}
 \partial_h^2\Re\Psi(e,.1+ih)
       &=\pi\{\Re\cot\pi(.1+ih)-\Re\cot\pi(e+.1+ih)\},\\
 \partial_h^2\Re Q(s;.1+ih,y)
       &=\pi\{\Re\cot\pi(.1+ih)-\Re\cot\pi(s+.1+ih)\}.
\end{split}
 \tag{35}
\]
They are positive on every retained point, since the first cotangent
exceeds \(25/9\) and each shifted one is at most \(3/2\).
They are independent of \(y\). The high-row version is positive
before its first wall and continuous at that wall; the last carrier
is constant. The true-end rate is affine, and \(W_1\) is a maximum
of two convex functions. Hence the same complete envelope is convex
in \(0\le h\le H\).
Both endpoint envelopes have been paid individually above.
It follows that the entire vertical face at \(x=1/10\) has
gap \(d_{12}\), with all raw profiles retained.

## 5. The real first interval and its endpoint

For every fixed \(0<\rho<1/10\), use the raw cap and ordinary
collections (5)--(7) of the
[real-first-interval proof](research_mixed_four_four_real_first_interval.md)
on \(\rho\le a=x\le1/10\). Its complete cap proof depends only
on \(x\), so its compact tails, actual endpoint groups and private
contours apply unchanged. Its ordinary low-row ratio uses
only \(\Im y\ge-.102\), and hence still exceeds \(e^{1/10}\).
For the high rows replace its zero-drift step by (17), (22).
The central factorial strips remain
\([1/8+\rho,.6]\) and \([.345,.95]\), and the proof keeps all
their raw currents rather than extrapolating private curvature.

For each retained private pair, including the upper and lower
alias points, that proof's derivative is
\[
 \partial_x\{\Re\Psi(e,x)+\Re Q(s;x,y)-J(x)\}
   =\log(N_eN_s/D^3)>1/3 .
 \tag{36}
\]
Here \(N_e>1\), \(N_s\ge1/\sqrt2>7/10\), and \(D<5/8\).
It is independent of \(y\); the true-end derivative
\(\log(N_s/D^2)>1/3\) is likewise unchanged.
The whole first weight has rate \(-J(x)\), for either first
monomial on the real line. All second weights and third profiles
are constant in this derivative. Consequently the zero-face
calibration proves the full raw envelope bound
\[
 \Lambda_{123}(z)-d_{12}-1/2000-(1/10-x)/3
                     \qquad(\rho\le x\le1/10).
 \tag{37}
\]

Extend through \(x=0\) using Lemma 1 of the
[real-endpoint continuation](research_mixed_four_four_real_first_endpoint.md).
For either first sector \(\sigma\), the complete source as a
Laurent polynomial in \(X\) has support in
\[
                 [-(1+\sigma)N+1,(2-\sigma)N-2].
 \tag{38}
\]
The first cap, \(C_{1,N}(X,Y)\), and the whole first weight are
included in this Laurent polynomial. The remaining factor
\(C_{\beta,N}(Y,Z)d_N(Y)Y^{-N}\) and the outgoing half-modulus
are constant multipliers in \(x\). Choose the continuation cost
\(1/4000\), then its small fixed interval radius, then
\(\rho\) sufficiently smaller, all before \(N\).
Apply (37) with total source tolerance \(1/4000\). The endpoint
rate retains gap \(d_{12}\), even after dropping the favorable
linear term. This procedure does not extend an arbitrary prescribed
missing interval from a one-point estimate, and it divides no
source factor at a zero.

## 6. Real boundary colors on the old central plateau

The old double-selected theorem states its final estimate on a
small ordinary-color disk. For the all-real assertion below, retain
its individual complete-color profile comparisons and verify the
finite cap source separately.

On \(a\in P+iH\), the complete cap contour of Section 2 of the
[selected next-four finite reduction](research_mixed_selected_four_four_finite_reduction.md)
has private rectangle \(E_c=[.27,.49]+i[-.055,.04]\), the same
five profiles, two unweighted joins, and all horizontal and vertical
aliases. The
[whole real-color endpoint theorem](research_mixed_endpoint_real_color_decay.md),
equations (6), (10)--(11), gives the original coherent endpoint
rate \(\Re S(e)\) on every point of that rectangle, uniformly for
\(w\in[-2,2]\). Insert that finite coefficient bound before
integrating each unchanged wire contour; every other factor and
sampling penalty is independent of \(w\). The exact density
remains \(+N\). This is a contour bound, not analytic continuation
of a physical-row estimate.

For compact physical tails, the same endpoint theorem supplies
the original complete-color profile on every fixed subinterval
of \(0<i/N<1\), including across one half. Thus the cap-tail
monotonicity in the cited finite reduction applies unchanged.
For \(i/N\le.01\), its original Newton bound uses only
\(V_\theta\le V_0\) below one half and retains the ceiling \(1/4\).
For \(i/N=1-\delta\ge.99\), the endpoint theorem's equation (15)
gives the all-real coefficient entropy at most
\(3/5+\delta\log2\). The same exact outgoing-product estimate
used in the finite reduction contributes at most
\(2\pi H+\delta\log(20/19)\); the remaining reciprocal own
factorial has nonpositive rate. Therefore this entire group
still has ceiling
\[
       3/5+2\pi H+\tfrac1{100}\log(40/19)<3/4.
\]
Both literal end groups are below the old
\(A_0>199/250\). In particular every old profile comparison,
including each Fourier alternative, yields its old finite bound
for all real colors. The other two factors have no ordinary-color
variable. This proves the required all-real version of the old
central plateau bound without a new phase comparison.

## 7. Complete connected-path conclusion

**Theorem.** On the oriented path (1), with first sector selected,
for every \(\tau>0\), both parities and the actual references (2)--(3),
\[
 |{\cal J}_N(w;a,y,z)|\,|d_N(Z)|^{\beta/2}
 \le C_\tau N^{B_\tau}
              e^{N\{\Lambda_{123}(z)-1/400+\tau\}} .
 \tag{39}
\]
This is uniform for \(b,v\in P\) and all real ordinary colors
\(w\in[-2,2]\). A sufficiently small fixed ordinary-color disk
and all fixed jets on smaller disks have the same rate with
polynomial costs. On the real portion \([0,1/10]\) the same
conclusion also holds for the first unselected monomial.

*Proof.* Sections 3--5 prove the result up to \(a=.22+iH\),
with raw gap at least \(d_{12}\) and complete finite inventories.
The old double-selected completion and Section 6 give the remaining
interval \([.22,.45]+iH\) with that same raw gap and all-real scope.
Since \(d_{12}>1/400\), a prescribed fraction of the spare reserve,
together with the final \(\tau\), absorbs the finitely many
source tolerances and polynomial factors. The cap bounds are
uniform for all real colors and the exact source has degree
less than \(N\) in that color. Chebyshev continuation and then
Cauchy's formula give the stated disks and derivatives, exactly
as in the cited endpoint proof. The outgoing half-modulus is
never differentiated or divided out. \(\square\)

Multiplying (39) by the original \(+N\,da\) and integrating along
the three oriented pieces of (1) preserves the exponential gap,
with polynomial cost. A subsequent selected second-plateau
integration likewise keeps its original \(+N\,dy\) density.
The first and second full \(d_N\), both Fourier upper alternatives
of each selected polynomial, the outgoing halfweight and every
original finite current remain present. No new relative coefficient
or noncancellation assertion is needed.

The theorem adds a connected first-selected left path to the
previous central simultaneous-selection theorem. It does not pay
the first unselected path at its negative geometric height, the
first right connection, or any unestimated second-coordinate
piece. It proves neither a complete second-period packet nor a
whole-word or knot theorem.

## Source bindings

All source implications used above were read in their stated versions.
The new arguments are written inequalities, with no mathematical
numerical evaluation.

| Source | SHA-256 |
|---|---|
| research_mixed_double_selected_plateau_completion.md | f205a230e6005a1cb676e635d91aac02f62a30cbb90fb175749f86972f286c4b |
| research_mixed_double_selected_last_rows.md | 7f26988d48cf658e5147a90c2f7c637baa09795658450d73577ca5ba37d36b94 |
| research_mixed_second_selected_four_profile_reduction.md | d084b535d83a08e50c4baddc52249c8495d88cde65f8c81e04baff566560d25e |
| research_mixed_selected_four_four_early_central.md | 7ed3ce53e89313ee0b149c4901a3eb29de7011462aa2d928346db1f233939b48 |
| research_mixed_selected_boundary_optimizer_bounds.md | 13fa176cf8f50054bc2c47e479f85daf0ecb9b22a68d316689ad752f8ca2b603 |
| research_mixed_selected_four_four_early_complete_source.md | 760ab93cc36ccba00eea97c518eb3697f55638b90c43c90d5ce1a9cd029ddc05 |
| research_mixed_selected_four_four_zero_height_face.md | fe99fcefe1618991471f083febcf4c6043418a4387d76be1ae2015542734810f |
| research_mixed_first_positive_join_convex_envelope.md | b1f18bb5a79ff958654190c960c933ac7839f1da3fc86635f6222a1ea58cb774 |
| research_mixed_four_four_real_first_interval.md | b848eb005f99d57259662ef3a864b207e093b6ebfaf4c34c2dbcc1e9727d58fc |
| research_mixed_four_four_real_first_endpoint.md | 4ceec7f835d08ef971b3b3ccadcf7eecd74e48db3d422cbd09e5611c0572c122 |
| research_mixed_early_own_four_high_rows.md | 62c3d5070d15c093ae8ab10cb373e9624a497d29743d6cd909bc5d7a33daebb6 |
| research_mixed_first_attached_low_row_transport.md | 8ef728d3808e1480d85a81c1ed8f7eebda99392d0b11f1262e4a47b5a2b196d3 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| research_mixed_complete44_second_selected_far_first_arc.md | f163f164be985de37d8d10485ec0790fe5057496d94030afdf5c7b48658cc8be |
| research_mixed_selected_four_four_finite_reduction.md | d018c6ad4dd78e6a6c7ac649f0d5d8443b649f1f01d9c6acde586697da1da4e5 |
| research_mixed_endpoint_real_color_decay.md | 44921926dbdccef49c84e02566e86cf175979c8f189e62c7ba2e9b92c0d577eb |
