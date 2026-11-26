# The double-selected 444 right shoulder

Private written proof, 11 November 2026. Both first retained coordinates
are selected at height \(1/100\). The first real coordinate remains on
its old plateau; the second moves from \(9/20\) to \(1/2\).
The result includes both complete own-four kernels, the complete cap,
both alternatives of each Fourier weight, and the outgoing halfweight.
It does not treat the first-unselected shoulder or the full first period.

## 1. Original source and claim

Fix an actual positive three/four word of length \(m\ge4\) beginning
with \(444\). Retain its original reference, logarithmic lifts and
ordinary color. Put
\[
 P=[11/50,9/20],\quad H=1/100,\quad
 a=x+iH,\ y=q+iH,\ z=b+ic_3,\qquad
 x,b\in P,\quad 9/20\le q\le1/2.                                  \tag{1}
\]
Both private indices are ordinary, including at \(m=4\). Their
actual heights \(h_2,h_3\), and \(c_3\), lie in
\((-51/500,-1/1000)\). The cap's private height stays in its
original interval \((-.051,-.019)\).

With \(\zeta=e^{-2\pi i/N}\), \(P_j=(\zeta;\zeta)_j\),
\(p_j(X)=(\zeta X;\zeta)_j\), use
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i<N}H_N(w,\zeta^{-i})p_i(X)/P_i^2,\\
 C_{1,N}(X,Y)&=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 {\cal B}_N&=
 |U_{1,N}(w,X)d_N(X)X^{-N}C_{1,N}(X,Y)
                  d_N(Y)Y^{-N}C_{1,N}(Y,Z)|\,|d_N(Z)|^{1/2},\\
 X&=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
\end{split}                                                       \tag{2}
\]
Every factor is the complete original finite polynomial or Laurent
polynomial. The last factor is a modulus allocation; no division at
a zero or holomorphic square root is used.

In the normalization of the simultaneous-selection sources, put
\[
\begin{split}
 Q(s;a,b)&=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias,\\
 F_{123}&=\Psi(e,a)+Q(s_2;a,y)+Q(s_3;y,z)
                         -g(a)-g(y)-\tfrac12g(z),\\
 p_R&=g'(s_3^*+r_3)-\tfrac32g'(r_3),\\
 \Lambda_{123}(z)&=\Re F_{123,*}+\Re\{p_R(z-r_3)\}.
\end{split}                                                       \tag{3}
\]
The star is the unchanged actual reference. All five internal
derivatives vanish there. In particular there is no free
\(q\)-marginal in this affine comparison.

**Theorem 1.** For every prescribed \(\tau>0\), on a sufficiently
small fixed ordinary-color disk about \(-2\), uniformly on (1),
\[
 {\cal B}_N\le C_\tau N^{A_\tau}
       \exp N\{\Lambda_{123}(z)-1/20000+\tau\}.                    \tag{4}
\]
Both parities and all sufficiently large levels are included.
Every fixed ordinary-color derivative has the same assertion on a
smaller disk, with its own polynomial factor and allowance.
Integration over the stated first plateau or second shoulder retains
the original \(+N\,da,+N\,dy\) densities and only adds polynomial
cost. No complete \(f_{44,N}\), first-unselected shoulder, second
height connector or whole second period is asserted.

## 2. The old face and each original profile

For each ordinary factor use its bare main, real left, real half,
and full last profiles \(R_0^j,R_L^j,R_R^j,R_1^j\).
The main intervals are \([1/8,1/2]\), at heights \(h_j\);
the left and half profiles have index heights zero. Here
\[
 R_1^2=2\pi H,\qquad R_1^3=0.                                    \tag{5}
\]
They are the literal periodic last-row rates, not evaluations of
the central logarithmic branch at index one.
Any profile at a summed real argument one means the continuous
limit from the original strip. The finite contour itself uses a
fixed right cut below one half, as specified in Section 5.

The complete cap is bounded by its two profiles \(A_0,A_L\).
The selected-four finite reduction, Sections 2--3, pays its real
tails, true ends, right cut and both aliases by these profiles,
pointwise in \(x\), independently of \(q,z\).
For each selected coordinate retain the two rates
\[
 W^{\rm fac}(v)=-\Re g(v+iH)-2\pi H,\qquad
 W^{\rm force}(v)=0.                                             \tag{6}
\]
These are alternatives for one complete Fourier polynomial, not
separately chosen finite sources.

At \(q_0=9/20\), the double-selected tangent theorem gives raw
gap \(1/100\) for \(A_i+R_0^2+R_0^3+W_1+W_2-\Re g(z)/2\),
for \(i=0,L\) and both choices of each weight.
The four-profile reduction supplies
\[
 R_L^2<R_0^2-1/100,\quad
 R_R^2<R_0^2-1/30,\quad R_1^2<R_0^2-1/50,\quad
 R_L^3<R_0^3-1/1000.                                             \tag{7}
\]
The outgoing-four half-row completion supplies
\(R_R^3<R_0^3-1/20\). The double-selected last-row theorem
pays all \(A_i+R_0^2+R_1^3\) alternatives with gap \(3/1000\).
Thus the following conservative old-face reserves are available
for every cap and weight choice:
\[
\begin{array}{c|cccc}
 &R_0^3&R_L^3&R_R^3&R_1^3\\ \hline
 R_0^2&1/100&1/100&1/100&3/1000\\
 R_L^2&1/50&1/100&1/100&3/1000\\
 R_R^2&1/100+1/30&1/100&1/100&3/1000\\
 R_1^2&3/100&1/100&1/100&3/1000 .
\end{array}                                                       \tag{8}
\]
These are profilewise comparisons from the cited proofs. They are
not inferred from a bound for a cancelling complete sum.

## 3. Two maximizing barriers throughout the shoulder

Write \(r=e^{2\pi H}\). The elementary bounds
\[
 1<r<16/15,\qquad \tfrac12<e^{2\pi h_j},e^{2\pi c_3}<1             \tag{9}
\]
follow from
\(\log(16/15)=2\operatorname{artanh}(1/31)>2/31>\pi/50\)
and \(.204\pi<2/3<\log2\).

**First ordinary index.** For \(t_2\in[1/8,11/50]\),
put \(\rho=e^{2\pi h_2}\), \(T=r^{-1}>15/16\).
The exact squared private force, including the incoming chirp, is
\[
 e^{2\Re Q_s}=
 \frac{|T-\rho e^{-2\pi i(x+t_2)}|^2
       |1-r\rho e^{-2\pi i(q+t_2)}|^2}
      {|1-\rho e^{-2\pi it_2}|^6}.                               \tag{10}
\]
The summed intervals are \([.345,.67]\) and \([.575,.72]\).
Their cosines are respectively less than \(-12/25,-9/50\);
the own cosine is greater than \(9/50\).
For example \(\sin(4\pi/25)>12/25\) follows from the sine
cubic at \(314/625\), whose excess has numerator \(1853356\)
over denominator \(1464843750\).
Also \(\sin(3\pi/50)>9/50\), by the sine cubic and
\(47/250<3\pi/50<1/5\).

Set
\[
 D_s=1+\rho^2-9\rho/25,\quad
 A_s=\rho^2+9\rho/10+225/256,\quad
 B_s=1+\rho^2+9\rho/25 .
\]
Then (10) exceeds \(A_sB_s/D_s^3\).
The differences \(A_s-(7/5)D_s\) and \(B_s-(6/5)D_s\)
are concave quadratics. At \(\rho=1/2,1\), their values are,
respectively,
\[
 (2589/32000,15453/32000),\qquad(73/500,49/125).
\]
Hence both are positive on \([1/2,1]\). Since \(D_s\le41/25\),
the squared force exceeds \(42/41>1\) on the whole excluded
interval. Every first main maximum therefore has \(t_2>11/50\).

**Third ordinary index.** For \(t_3\in[1/8,1/5]\), put
\(\rho=e^{2\pi h_3}\), \(R=e^{2\pi c_3}>1/2\).
The exact force is
\[
 e^{2\Re Q_s}=
 \frac{|r^{-1}-\rho e^{-2\pi i(q+t_3)}|^2
       |1-R\rho e^{-2\pi i(b+t_3)}|^2}
      {|1-\rho e^{-2\pi it_3}|^6}.                               \tag{11}
\]
The incoming, outgoing and own cosine bounds are
\(-3/10,-1/2,3/10\), respectively, in the same directions
as above. Indeed the summed intervals are \([.575,.7]\)
and \([.345,.65]\), and
\(\cos(2\pi/5)=(\sqrt5-1)/4>3/10\).
Put \(D_s=1+\rho^2-3\rho/5\).
The outgoing numerator square is greater than \(D_s\), because
\[
 1+\rho^2/4+\rho/2-D_s
             =\rho(11/10-3\rho/4)>0.
\]
The incoming numerator square exceeds
\(225/256+\rho^2+9\rho/16>D_s^2\).
For \(\rho\le3/4\), use
\(D_s^2\le(89/80)^2<5/4<361/256\).
For \(\rho\ge3/4\), use \(D_s\le1+2\rho/5\); the remaining
difference is at least
\[
 (21/25)\rho^2-(19/80)\rho-31/256,
\]
which increases there and equals \(1109/6400\) at \(3/4\).
Thus (11) exceeds one throughout the lower interval.
Every third main maximum has \(t_3>1/5\).

Both assertions are direct marginal signs on the full omitted
intervals. They require no differentiable maximizing branch or
unproved curvature extrapolation. The main maxima may therefore be
taken over the fixed intervals \([.22,.5]\) and \([.2,.5]\).

## 4. Transport of main and non-main profiles

Put \(D=|1-r e^{-2\pi iq}|\). At fixed ordinary points define
\[
 N_2=|1-r\rho_2e^{-2\pi i(q+t_2)}|,\qquad
 N_3=|T_3-r e^{-2\pi i(q+t_3)}|,\quad T_3=e^{-2\pi h_3}<2.
\]
The exact derivative of a paired forced rate is
\[
                    \log(N_2N_3/D^2).                            \tag{12}
\]
The incoming chirp of the third factor is included in \(T_3\).
The factorial second alternative adds \(-\log D<0\).
The cap, first weight and outgoing halfweight are constant in \(q\).

On the clipped main intervals of Section 3,
\[
 N_2^2\le A=r^2+(49/50)r+1,\quad
 N_3^2\le B=r^2+(12/5)r+4,\quad
 D^2\ge D_0=r^2+(19/10)r+1.                                      \tag{13}
\]
Here \(\cos(.34\pi)<49/100\), \(\cos(.3\pi)<3/5\), and
\(\cos(.1\pi)>19/20\).
For written witnesses, set \(\delta=\pi/150\);
\(\cos(\pi/3+\delta)<1/2-(6/7)(3\delta/4)<49/100\).
Also
\(\cos(\pi/3-\pi/30)<1/2+(7/8)(11/105)<3/5\);
the cosine quadratic with \(\pi<22/7\) gives the third bound.

The exact polynomial identity is
\[
\begin{split}
500(3721D_0^2-2500AB)
={}&610500r^4+2844900r^3+1247405r^2\\
 &-830100r-3139500 .
\end{split}                                                       \tag{14}
\]
It equals \(733205>0\) at one, and its derivative is positive
for \(r\ge1\). Hence \(N_2N_3/D^2<61/50\).
The cubic exponential lower bound gives
\[
 \log(61/50)<199/1000:
 \quad 1+u+u^2/2+u^3/6-61/50
             =683599/6000000000>0,\quad u=199/1000.
\]
Every main/main rate therefore grows by less than
\(199/20000\) across the shoulder. Its old reserve leaves
\[
                         1/100-199/20000=1/20000.                \tag{15}
\]
Take maxima over the fixed clipped intervals only after this
pointwise transport; no differentiation of an optimizing point
is used.

The first fixed left and half cuts are not subject to the first
barrier. For every \(t_2\in[1/8,.5]\) and
\(0\le\rho_2\le1\), nevertheless \(N_2\le D\):
\(1-q\le q+t_2\le1\), and convexity in \(\rho_2\) reduces
the assertion to its endpoints, using \(D>1\).
The first last carrier has derivative zero.
For these three first profiles paired with the third main,
\[
 N_3/D<7/5,\qquad
 49D_0-25B=24r^2+(331/10)r-51>0\quad(r\ge1).
\]
The last polynomial is increasing and is \(61/10\) at one.
The exponential cubic at \(17/50\) exceeds \(7/5\)
(the excess is \(3263/750000\)), so
\(\log(7/5)<17/50\). Their transport cost is less than
\(17/1000\). The weakest corresponding reserve in (8),
\(1/50\), leaves \(3/1000\).

For third profile \(L\), its private height is zero and
\[
 N_3/D\le(1+r)/D\le\sqrt{40/39},\qquad
                         \log(N_3/D)<1/78.                       \tag{16}
\]
Indeed \(D^2\ge(1+r)^2-r/10\) and
\(r/(1+r)^2\le1/4\). Since every first profile has
nonpositive outgoing derivative, the total cost is less than
\(1/1560\). The old reserve \(1/100\) easily remains greater
than \(1/20000\).

For the third half profile, \(N_3=|1+r e^{-2\pi iq}|<D\),
since \(\cos2\pi q<0\). Its paired rate cannot increase.
The third last rate is constant in \(q\), so the same holds
for it. Thus the remaining reserves in (8) are unchanged.
This proves the common profile gap \(1/20000\) for every
choice, including both Fourier alternatives.

## 5. Complete finite-source extension to the shoulder

We verify the changed source domain explicitly. Set
\(C(w)=\Re\cot\pi w\), \(A=\cosh(2\pi\eta)\).
For either ordinary factor, at \(s=t+i\eta\),
\(1/8\le t<1/2\), the shifted cotangent involving the
shoulder coordinate \(q\) is nonpositive. If the other shifted
cotangent is positive, then \(t<7/25\), its summed real
argument is at least \(69/200\), and
\[
 3C(t+i\eta)>\frac{21/10}{A+1/5},\qquad
 C(s+\hbox{other argument})<
          \frac1{A/2+1/2}.                                      \tag{17}
\]
The bounds use \(\sin2\pi t>7/10\),
\(\cos2\pi t>-1/5\), and cosine of the other sum less
than \(-1/2\). Also
\(\cosh 2\pi(\eta+h)\ge e^{-2\pi|h|}A>A/2\):
here \(h=H\) or \(h=c_3\) and \(2\pi|h|<\log2\).
Cross multiplication in (17) leaves \(A/20+17/20>0\).
When both shifted cotangents are nonpositive, the result is
immediate. Consequently \(\Re Q_{ss}<0\) at every finite
height on both index intervals.

On the original strip lift, \(\Im Q_s\) decreases with index
height. Its limits at negative and positive infinity are
\(2\pi a_R\) and \(-\pi-2\pi b_R+2\pi t\), respectively.
For factor two and factor three this gives
\[
 -7\pi/4<\Im Q_s^2<9\pi/10,\qquad
 -33\pi/20<\Im Q_s^3<\pi.                                        \tag{18}
\]
These follow directly from their own incoming/outgoing order;
the asymmetric chirp is not swapped.

Use lower and upper alias heights \(-1/5,4\) for both kernels.
Integrating \(\partial_\eta\Re Q=-\Im Q_s\) from the actual
main height, then subtracting the exact cotangent penalties,
bounds the horizontal aliases below their same-real-coordinate
main profiles. Safe gaps are
\[
\begin{array}{c|cc}
 &\text{lower}&\text{upper}\\ \hline
 C_1(X,Y)&11\pi/50&1643\pi/2000\\
 C_1(Y,Z)&\pi/5&6\pi/5 .
\end{array}                                                       \tag{19}
\]
Every weighted vertical half decreases away from its real cut
by (18). Holomorphy and \(\Re Q_{ss}<0\) make each unweighted
vertical join convex in height, so its endpoints suffice.

Both physical low blocks increase to \(1/8\). On this real
interval the numerator associated with a plateau real target
has modulus at least \(49/50\), and that associated with the
shoulder target has modulus greater than one, after folding
the incoming chirp. The denominator modulus is less than
\((4/5)^3\). For the only cosine-positive part of a plateau
sum, use \(\sin(11\pi/25)>49/50\); otherwise the modulus
is at least one. The incoming selected radius inverse is
less than one, so in the negative-cosine shoulder case the
squared folded numerator \(r^{-2}+1-2r^{-1}\cos\theta\)
is greater than one. These give a uniform ratio greater than
one, including the zero-row transition.

The full high-row theorem, Lemma 1 of transformed_upper_rows,
applies on the enlarged angular square \([.22,.5]^2\)
and both indicated height signs. It bounds every high row
through index \(N-1\) by its half and last profiles.
Thus no support zero or revived row is omitted.

Choose a fixed right cut \(r_0<1/2\) sufficiently close to
\(1/2\). The physical collar up to \(1/2\) is bounded by
the continuous half-row rate with any prescribed allowance.
On the remaining fixed contours every factorial argument
\(s,s+a,s+b,a,b\) has real part strictly between zero and
one. The exact factorial interpolation and cotangent residue
identity therefore retain the \(+N\) main density, both
zero-mode joins, both horizontal aliases and all four
weighted vertical halves. Their uniform symbols and half-grid
rounding cost one arbitrarily small total tolerance.
The two parity endpoints and literal low/high row groups are
included. This proves the complete four-profile ordinary bound
on the new shoulder, rather than applying an old bound outside
its printed domain.

Finally multiply the two ordinary bounds by the unchanged
complete cap profile bound, the two full Fourier bounds (6),
and the outgoing modulus halfweight. Section 4 pays every
resulting profile. Only the cap depends on \(w\); its original
fixed disk and Cauchy estimates give the derivative assertion.
This proves Theorem 1 with the original constants and allocations.

The other half of the outgoing weight belongs to the next
original factor, including its terminal incidence at \(m=4\).
No exterior unit scalar changes. The first-unselected
\(\beta=1\) main comparison has a weaker previously proved
reserve; (15) cannot be applied to that case.

## Direct source bindings

The new rational comparisons and complete contour extension above
are written deductions. No mathematical numerical evaluation,
saved-value arithmetic, import, test or compilation is used.
The borrowed old-face margins are the stated adopted theorems,
not recomputed certificate values.
The complete author proof and all ten directly used source implications
have been read back; all ten bindings match. The note is author-frozen
for independent proof and source review.

| Source in notes/ | SHA-256 |
|---|---|
| research_mixed_second_selected_plateau_reduction.md | 015c85c322ff3563ec6752b5c499080c3e906360920aaeed2063508ef2db868f |
| research_mixed_second_selected_four_profile_reduction.md | d084b535d83a08e50c4baddc52249c8495d88cde65f8c81e04baff566560d25e |
| research_mixed_double_selected_tangent_completion.md | ad2012d03f5022abbb593ab3c80659b8b778a6d55fedf980c7d4ead2eb7726b8 |
| research_mixed_double_selected_last_rows.md | 7f26988d48cf658e5147a90c2f7c637baa09795658450d73577ca5ba37d36b94 |
| research_mixed_second_selected_outgoing_four_half_row_completion.md | ce795f3dbf2cab22244994fa7e881ec3017387e4515f138a41809bfedd72aa75 |
| research_mixed_selected_four_four_finite_reduction.md | d018c6ad4dd78e6a6c7ac649f0d5d8443b649f1f01d9c6acde586697da1da4e5 |
| research_mixed_transformed_upper_rows.md | bdfc604c945926f257278a15c1383df228cf5238754fada7bbfd278b6aedd603 |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

