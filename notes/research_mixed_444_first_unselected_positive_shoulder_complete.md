# The complete first-unselected 444 positive shoulder

Private written proof, 11 November 2026. This combines the new
first-unselected main comparison with the original separate reserves
for the other profiles. It bounds the complete cap and both complete
own-four kernels when the first coordinate remains on its unselected
plateau and the second ranges over its positive right shoulder.
It does not complete the first summation or the second period.

## 1. Exact source and statement

Fix an actual positive three/four word of length \(m\ge4\) beginning
with \(444\), with its original reference and logarithmic lifts. Put
\[
 \begin{gathered}
 P=[11/50,9/20],\quad H=1/100,\quad
 a=x+ic_1,\quad y=q+iH,\quad z=b+ic_3,\\
 x,b\in P,\quad q\in[9/20,1/2],\qquad
 -.078<c_1<-.020,\quad -.102<h_2,h_3,c_3<-.001.
 \end{gathered}
 \tag{1}
\]
Here \(h_2,h_3\) are the actual ordinary index heights. Both indices
are ordinary even at \(m=4\), when the following external leg is
attached. Keep the same actual coupled family as in the
[main-profile proof](research_mixed_444_first_unselected_positive_shoulder_main.md).

With \(\zeta=e^{-2\pi i/N}\), \(P_j=(\zeta;\zeta)_j\),
\(p_j(X)=(\zeta X;\zeta)_j\), retain
\[
 \begin{split}
 U_{1,N}(w,X)&=\sum_{i<N}H_N(w,\zeta^{-i})p_i(X)/P_i^2,\\
 C_{1,N}(X,Y)&=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 {\cal B}_N&=
 |U_{1,N}(w,X)C_{1,N}(X,Y)C_{1,N}(Y,Z)
                       d_N(X)d_N(Y)Y^{-N}|\,|d_N(Z)|^{1/2},\\
 X&=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},\qquad Z=e^{-2\pi iz}.
 \end{split}
 \tag{2}
\]
In particular the first monomial \(X^{-N}\) is absent.
The last factor in (2) is a modulus allocation, without division
at a zero or a holomorphic square-root choice.

Use the original \(Q,F_{23},\Lambda_{23}\) of the main-profile proof,
and the original allocated cap action \(L_1\). Thus
\[
 \Lambda_{123}(z)=
 \Re\{L_1(r_1)+F_{23,*}+p_R(z-r_3)\}.
 \tag{3}
\]
The identity \(L_1'(r_1)+p_L=0\) retains the original boundary
marginal cancellation.

**Theorem.** For every \(\tau>0\), on a sufficiently small fixed
ordinary-color disk about \(-2\), uniformly on (1),
\[
 {\cal B}_N\le C_\tau N^{A_\tau}
       \exp N\{\Lambda_{123}(z)-1/100000+\tau\}.
 \tag{4}
\]
Both level parities and every finite row are included. Fixed
ordinary-color derivatives have the same assertion on smaller disks,
with their own polynomial factors. Integrating over either indicated
target interval retains the original \(+N\,da\) or \(+N\,dy\)
density. The full first polynomial \(f_{44,N}\), its complementary
first paths, a second height connector, and a full second period are
outside this theorem.

## 2. The old face and its separate reserves

For \(j=2,3\), retain the bare ordinary main, real left, real half,
and full periodic last profiles \(R_0^j,R_L^j,R_R^j,R_1^j\).
Main heights are \(h_j\), the real cuts are \(1/8,1/2\), and
\[
 R_1^2=2\pi(-c_1+H),\qquad R_1^3=0.
 \tag{5}
\]
These are periodic physical last rates, not evaluations of the
central logarithmic branch at index one. Let
\[
 W^{\rm fac}(y)=-\Re g(y)-2\pi H,\qquad W^{\rm force}(y)=0,
 \quad \delta=1/3200.
 \tag{6}
\]
The continuous main profiles use the interval \([1/8,1/2]\).
At a shifted argument on the line of real part one they mean the
limit from the original strip. The real part of the primitive is
continuous there, including its integrable logarithmic endpoint.
The main comparison is uniform in every fixed right cut \(r_0<1/2\);
taking \(r_0\uparrow1/2\) therefore gives the same profile bound
for this continuous endpoint convention. The finite contour in
Section 4 always keeps \(r_0<1/2\).

At \(q_0=9/20\), the original central theorem, as recorded in the
main-profile proof, pays
\[
 R_0^2+R_0^3+W^\nu-\tfrac12\Re g(a)-\tfrac12\Re g(z)
                   \le\Lambda_{23}-\delta.
 \tag{7}
\]
The [four-profile reduction](research_mixed_second_selected_four_profile_reduction.md)
and the
[outgoing-four half completion](research_mixed_second_selected_outgoing_four_half_row_completion.md)
give separate extra losses
\[
 \begin{gathered}
 R_j^2<R_0^2-d_j,\quad
 d_0=0,\ d_L=1/100,\ d_R=1/30,\ d_1=1/50,\\
 R_k^3<R_0^3-e_k,\quad
 e_0=0,\ e_L=1/1000,\ e_R=1/20.
 \end{gathered}
 \tag{8}
\]
For subscript zero the corresponding statement is equality.
Consequently the old-face reserve for every \(j\) and
\(k=0,L,R\) is at least \(\delta+d_j+e_k\).
For \(k=1\), the
[original last-row comparison](research_mixed_second_selected_outgoing_last_rows.md)
gives the separate reserve \(1/400\), initially with \(j=0\).
The first-factor reductions in (8) also give it for the other \(j\).

These are bounds for individual profiles with both Fourier alternatives,
not deductions from the modulus of a cancelling finite sum.
Only first-unselected reserves are used.

## 3. Transport of every profile

Write \(r=e^{\pi/50}\), \(D=|1-re^{-2\pi iq}|\), and
\[
 D_0=r^2+\frac{19}{10}r+1.
 \tag{9}
\]
The main proof establishes \(17/16<r<16/15\), \(D^2\ge D_0\),
and, at maximizing ordinary indices, the bounds
\[
 \begin{gathered}
 q+s_R\ge7/10,\qquad
 N_2^2\le A_f=r^2+\frac58r+1,\\
 N_3^2\le B_s=r^2+\frac{703}{500}r+\frac{361}{100}
       \quad(\rho_3\le5/8),\\
 N_3^2\le B_l=r^2+\frac{48}{25}r+\frac{64}{25}
       \quad(\rho_3\ge5/8),
 \end{gathered}
 \tag{10}
\]
where \(\rho_3=e^{2\pi h_3}\). The quantities \(N_2,N_3\)
are its exact outgoing and chirp-folded incoming numerators.
Since
\[
 B_s-B_l=\frac{21}{20}-\frac{257}{500}r>0,
 \tag{11}
\]
the bound \(N_3^2\le B_s\) is valid in both cases.

**Main/main.** The main proof already gives the paired reserve
\(1/72000\) over the entire shoulder, including both weight
alternatives and nondifferentiable changes of maximizer.

**First left with third main.** At the first real left cut,
\[
 N_2^2=|1-re^{-2\pi i(q+1/8)}|^2
 \le A_L:=r^2+\frac95r+1.
 \tag{12}
\]
Here \(q+1/8\in[.575,.625]\), and
\(\cos(3\pi/20)<25/28<9/10\). For the first inequality,
write \(3\pi/20=\pi/6-\pi/60\), use
\(\sqrt3<26/15\), \(\sin(\pi/60)<\pi/60\), and
\(\pi<22/7\). The resulting upper bound is
\(13/15+11/420=25/28\).

The exact polynomial
\[
 \begin{split}
 P_L(r)&=\frac32D_0^2-A_LB_s\\
 &=\frac12r^4+\frac{1247}{500}r^3
       +\frac{6371}{5000}r^2-\frac{551}{250}r-\frac{211}{100}
 \end{split}
 \tag{13}
\]
satisfies \(P_L(1)=-229/5000\) and \(P_L'(r)>9\) for
\(r\ge1\). Indeed \(P_L''>0\) there, and
\(P_L'(1)=24566/2500>9\). Since \(r>17/16\), \(P_L(r)>0\).
Therefore the paired forced derivative is less than
\(\tfrac12\log(3/2)\). The factorial derivative is smaller by
\(\log D>0\). The positive atanh series, with its tail bounded
by a geometric series, gives
\[
 \log(3/2)=2\operatorname{atanh}(1/5)
 \le\frac25+\frac{2(1/5)^3}{3(1-1/25)}
 =\frac{73}{180}<\frac{13}{32}.
 \tag{14}
\]
Transport over length \(1/20\) costs less than \(13/1280\).
The old reserve in (8) leaves
\[
                 \delta+\frac1{100}-\frac{13}{1280}
                         =\frac1{6400}.
 \tag{15}
\]

**First half or last with third main.** For any first regular index
\(s_R\in[1/8,1/2]\) at height at most zero,
\[
             N_2=|1-r\rho_2e^{-2\pi i(q+s_R)}|\le D.
 \tag{16}
\]
To prove this, \(1-q\le q+s_R\le1\), so its cosine is at least
\(\cos2\pi q\); convexity in \(0\le\rho_2\le1\) reduces the
modulus square to the endpoints, using \(D>1\).
The first last rate (5) is constant in \(q\).
The cruder universal third-main bound from the
[double-selected shoulder](research_mixed_444_double_selected_right_shoulder.md),
Sections 3--4, is
\[
 N_3^2\le B=r^2+\frac{12}{5}r+4,\qquad
 49D_0-25B=24r^2+\frac{331}{10}r-51>0\quad(r\ge1).
 \tag{17}
\]
Its private barrier \(t_R\ge1/5\) depends only on the second
selected and third actual arguments, so it is unchanged here.
Thus the paired derivative is less than
\(\log(7/5)<17/50\), and the transport cost is less than
\(17/1000\). For a direct logarithm witness, the exponential
cubic at \(17/50\) exceeds \(7/5\) by \(3263/750000\).
The weaker of the relevant old reserves still leaves
\[
                    \delta+\frac1{50}-\frac{17}{1000}
                      >\frac1{72000}.
 \tag{18}
\]

**Third left, half, or last.** Every first profile is nonincreasing
in \(q\), by (16) or the constancy of (5). At the third real left cut,
\[
 N_3\le1+r,\qquad
 \frac{N_3}{D}\le\sqrt{\frac{40}{39}},\qquad
                    \log(N_3/D)<\frac1{78}.
 \tag{19}
\]
Indeed \(D^2\ge(1+r)^2-r/10\) and \(r/(1+r)^2\le1/4\).
The total shoulder cost is less than \(1/1560\). Even with
the weakest first profile, the remaining reserve is
\[
                  \delta+\frac1{1000}-\frac1{1560}
                              >\frac1{72000}.
 \tag{20}
\]
At the third half profile,
\(N_3=|1+re^{-2\pi iq}|<D\). The third last profile is zero.
These paired rates do not increase, and retain their original
reserves. The factorial second alternative only decreases the
derivatives further.

For main maxima the derivative estimates have the fixed-compact
maximum interpretation proved in Section 5 of the main note.
Fixed-cut profiles need no optimizer argument. We have therefore
paid all sixteen pairs and both second-weight alternatives with
common raw reserve \(1/72000\).

## 4. The complete finite source on the changed height domain

We check the first-negative-height change in the finite contour
argument of the double-selected shoulder, Section 5. Let
\(s=t+i\eta\), \(1/8\le t<1/2\), and put
\[
                         C(w)=\Re\cot\pi w,\quad
                         A=\cosh(2\pi\eta).
 \tag{21}
\]
For either ordinary kernel, the shifted cotangent involving
\(q\in[.45,.5]\) is nonpositive. If the other shifted cotangent
is positive, then \(t<.28\), its real argument is at least
\(.345\), and
\[
 3C(s)>\frac{21/10}{A+1/5},\qquad
 C(s+\hbox{other argument})<
                         \frac1{A/2+1/2}.
 \tag{22}
\]
The sine and cosine bounds here are
\(\sin2\pi t>7/10\), \(\cos2\pi t>-1/5\), and cosine
of the other sum less than \(-1/2\).
For its height \(h=c_1\) or \(c_3\),
\[
 \cosh2\pi(\eta+h)\ge e^{-2\pi|h|}A>A/2
 \tag{23}
\]
because \(2\pi|h|<\log2\). Thus the previously positive first
height is not required. Cross multiplication in (22) leaves
\(A/20+17/20>0\). If both shifted cotangents are nonpositive,
the conclusion is immediate. Hence \(\Re Q_{ss}<0\) at every
finite index height for both kernels.

On the original logarithmic lift, \(I=\Im Q_s\) decreases with
index height. Its limits are \(2\pi a_R\) at negative infinity
and \(-\pi-2\pi b_R+2\pi t\) at positive infinity, with the
incoming and outgoing order preserved. Therefore
\[
 -7\pi/4<I_2<9\pi/10,\qquad
 -33\pi/20<I_3<\pi.
 \tag{24}
\]
The bounds depend on the real angles, not the sign of \(c_1\).

Keep alias heights \(-1/5\) and \(4\). Integrating
\(\partial_\eta\Re Q=-I\) from the actual main heights
\(-.102<h_j<-.001\), then including the exact cotangent
penalties, gives the following safe gaps below the main profile
at the same real index:
\[
 \begin{array}{c|cc}
 &\text{lower alias}&\text{upper alias}\\ \hline
 C_{1,N}(X,Y)&11\pi/50&1643\pi/2000\\
 C_{1,N}(Y,Z)&\pi/5&6\pi/5 .
 \end{array}
 \tag{25}
\]
Every weighted vertical half decreases away from its real cut,
by \(-I-2\pi<0\) on the upper half and \(-I+2\pi>0\) on
the lower half. Every unweighted zero-mode join is convex in
height, since \(\partial_\eta^2\Re Q=-\Re Q_{ss}>0\).
Its real cut and original main endpoint therefore bound it.

The physical low blocks increase to \(1/8\). On \(0\le t\le1/8\),
the numerator attached to a plateau angle has modulus at least
\(49/50\), after folding the incoming chirp if necessary.
For a positive cosine use the radial minimum and
\(\sin(11\pi/25)>49/50\); otherwise the modulus is at least
one. For the first incoming leg the folded radius is
\(T_a>1\), so the same lower bound holds. The shoulder
numerator has negative cosine and modulus greater than one,
also for the third incoming folded radius \(r^{-1}\).
The own denominator is less than \((4/5)^3\). This yields a
strict uniform step ratio greater than one, including the
zero-row transition, with its exact finite shifted arguments.

For both kernels the
[full high-row lemma](research_mixed_transformed_upper_rows.md),
Lemma 1, permits both angular coordinates in \([.22,.5]\)
and both height moduli at most \(.108\). It therefore reduces
every physical row from \(\lceil N/2\rceil\) through \(N-1\)
to the half and the literal last rates (5). Both parity endpoints
and every revived off-grid row remain included.

Choose a fixed right cut \(r_0<1/2\), sufficiently close to \(1/2\).
The physical collar between that cut and the half row is bounded
by the continuous half-row profile with an arbitrarily small
allowance. This is the same zero-safe physical-row step used in
the double-selected shoulder proof. On the remaining fixed
contour, every factorial argument \(s,s+a,s+b,a,b\) has real
part strictly between zero and one.

For precision, the negative-root interpolant is
\[
 \Pi_N(w)=G_N(Nw)\exp\{\tfrac{\pi i}{2}[N(w-w^2)-w]\},\qquad
 {\cal R}_N(s;a,b)=
 \frac{e^{2\pi iNas}\Pi_N(s+a)\Pi_N(s+b)}
      {\Pi_N(a)\Pi_N(b)\Pi_N(s)^3}.
 \tag{26}
\]
The factorial construction and its marked unit recurrence give
the literal row at \(s=j/N\). The exact contour coefficient is
\(N/(2i)\) multiplying \({\cal R}_N(s)\cot(\pi Ns)\,ds\).
Its decomposition has original zero-mode coefficient \(+N\),
both unweighted joins, two horizontal aliases and four weighted
vertical halves. The original half-grid cuts avoid physical
poles; their rounding and the fixed-contour symbols cost one
arbitrarily small total allowance. Thus (25) and the physical
row bounds establish the complete four-profile upper bound,
not only an estimate for a stationary phase.

## 5. Original weights, cap, colors, and scope

The [exact Fourier continuation](research_mixed_fourier_weight_continuation.md)
gives both second alternatives (6), and the unselected halfweight
rates \(-\Re g(a)/2\), \(-\Re g(z)/2\) at their negative heights.
No factor is divided out. Applying Section 3 to the complete
four-profile bound just proved gives
\[
 \begin{split}
 &|C_{1,N}(X,Y)C_{1,N}(Y,Z)d_N(Y)Y^{-N}|\,
                         |d_N(X)|^{1/2}|d_N(Z)|^{1/2}\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
           e^{N(\Lambda_{23}-1/100000+\tau)}.
 \end{split}
 \tag{27}
\]
The strict difference between \(1/72000\) and \(1/100000\)
allows all collar, symbol and rounding tolerances.

Multiply (27) by the
[complete cap plane](research_mixed_first_cap_plateau_completion.md)
for \(|U_{1,N}(w,X)|\,|d_N(X)|^{1/2}\).
Its original complex marginal cancels \(p_L\), giving (3)--(4);
its nonpositive quadratic may be retained or dropped. The two
modulus halves restore the full \(d_N(X)\) without choosing a
branch or dividing by a possible zero. The other half at \(Z\)
belongs to the original following factor, including the terminal
incidence when \(m=4\).

Only the cap depends on \(w\). Its original fixed ordinary-color
disk, followed by Cauchy estimates on a smaller disk, gives the
stated derivatives. All finite sums, both Fourier alternatives,
original scalar factors and both level parities remain unchanged.
The first coordinate is still restricted to \(P+ic_1\). In
particular no bound for its complete period is inferred from (4).

## 6. Direct-source bindings

All new estimates are written inequalities. No mathematical numerical
evaluation, saved-value arithmetic, test, import or compilation is
used. The old reserves are imported as theorems with their original
allocations.

| Direct source | SHA256 | Implication |
|---|---|---|
| [New unselected main comparison](research_mixed_444_first_unselected_positive_shoulder_main.md) | 72f42d601fd30e30af4d3efdf3d1a0efb0d5834a4ffd3e9438ddf39ba26a38e7 | Actual heights, exact derivative, radius split and main/main reserve |
| [Double-selected shoulder](research_mixed_444_double_selected_right_shoulder.md) | 204313ab2b8d7e4076c516c6ee41b3a588504c4bf51530777a89deb7609792f1 | Third barrier, scalar transports and exact finite-contour inventory, with the first-height change proved here |
| [Second-selection source](research_mixed_second_selected_plateau_reduction.md) | 015c85c322ff3563ec6752b5c499080c3e906360920aaeed2063508ef2db868f | Literal allocated product, tangents, four profiles and original normalization |
| [Four-profile reduction](research_mixed_second_selected_four_profile_reduction.md) | d084b535d83a08e50c4baddc52249c8495d88cde65f8c81e04baff566560d25e | Old separate first and outgoing-left reserves |
| [Outgoing-four half completion](research_mixed_second_selected_outgoing_four_half_row_completion.md) | ce795f3dbf2cab22244994fa7e881ec3017387e4515f138a41809bfedd72aa75 | Old outgoing-half reserve |
| [Outgoing last rows](research_mixed_second_selected_outgoing_last_rows.md) | d634f87205e3273ba5845f8f9586df3fe1a197fae8eae765d010278ff1809c91 | Original first-unselected last-profile action bound |
| [Transformed upper rows](research_mixed_transformed_upper_rows.md) | bdfc604c945926f257278a15c1383df228cf5238754fada7bbfd278b6aedd603 | Complete physical high-row domain and endpoints |
| [Exact factorial construction](exact_factorial_interpolation_and_complex_contours.md) | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 | Marked interpolation, compact symbols and exact residues |
| [Cap plateau](research_mixed_first_cap_plateau_completion.md) | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d | Complete actual-reference cap plane and ordinary-color neighborhood |
| [Fourier continuation](research_mixed_fourier_weight_continuation.md) | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e | Exact negative-root normalization and complete polynomial weights |
