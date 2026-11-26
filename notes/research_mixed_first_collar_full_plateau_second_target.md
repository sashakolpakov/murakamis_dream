# The first collar with its second target on the full plateau

Research deduction, 6 November 2026. The second real target in the
[independent-plateau first-collar theorem](research_mixed_first_collar_independent_plateau_middle.md)
can range over all of \(P=[.22,.45]\), for either second type and
every permitted physical height and selection. The actual reference,
its complex affine marginal, and all literal Fourier allocations stay
unchanged. The common raw prefix loss is \(1/500\); a finite-source
loss \(1/1000\) remains after one aggregate tolerance. This proof
uses existing phase witnesses and exact elementary inequalities. It
introduces no root, source evaluation, parameter cover or new contour.

## 1. Scope and the two old target restrictions

Fix an actual mixed open word of length \(m\ge4\), with first
flags \((\alpha,\beta)\in\{0,1\}^2\), and an ordinary cut
\(3\le h\le m-1\). Write its retained references as
\(r_j=a_j+ic_j\). The physical first coordinate is real,
\(x_1\in[0,\rho]\). Take
\[
 y_2,\ldots,y_h\in P,\qquad d_j=y_j-a_j.
 \tag{1}
\]
Coordinates \(3,\ldots,h\) are unselected at their actual reference
heights. The second physical height \(k\) ranges between \(c_2\)
and zero if unselected; for a selected second type four it ranges
over \([0,H]\), \(H=7/500\). All permitted first selections
remain present. The cut carries its original single halfweight.

The old intervals \(I_3=[.267,.433]\), \(I_4=[.24,.363]\)
were target restrictions in two separate arguments. The
[horizontal tangent proof](research_mixed_first_collar_horizontal_tangent.md),
Sections 2--3, used them to continue the comparison phase and prove
a phase floor. The [type-three transport](research_mixed_first_collar_fixed_reference_completion.md),
Section 2, and [enlarged type-four transport](research_mixed_four_enlarged_contour_transport.md)
also used them in their fixed-contour inequalities. By contrast, the
completed [unselected finite-factor planes](research_mixed_full_unselected_plateau.md)
already hold on independent \(P^2\) targets. Their coefficient
\(\kappa_*=1/2500000\) is unchanged here.

For the first pair use precisely
\[
 F(y)=\Re\{\mathcal T_\alpha(r_1,-2)
       +\phi_{0\beta}(r_1,y+ic_2)-\alpha g(r_1)\},
 \quad M_{12}=F(a_2),\quad p=F'(a_2).
 \tag{2}
\]
The complete first weight and one half of the second weight occur
in (2). We prove the needed bounds below its original horizontal
tangent \(M_{12}+pd_2\). The subsequent incidence cancels that
tangent exactly; no replacement reference is chosen.

## 2. Second type three: the actual coupled height removes the obstruction

For first type three, the old endpoint rectangle already gives
\(|\Im\cot\pi r_1|<.37\). For a first type four followed by
type three, the **actual coupled**
[attached-height theorem](research_mixed_first_four_attached_height_bound.md),
Theorem 1, gives
\[
 .246<\Re r_1<.350,\qquad -.070<\Im r_1<-.020.
 \tag{3}
\]
It applies to every actual word of length at least three. It is
stronger than the independent endpoint-map rectangle and is essential
to this proof.

Both outer cotangents belong to the closed half-square chamber on
the whole path from real arguments to
\((r_1,y+ic_2)\), for every \(y\in P\). Here
\(-.065<c_2<.068\). The following elementary bounds verify the
new endpoints. For \(t\le .136\pi<3/7\),
\[
 e^t<20/13,\qquad
 \cosh t-2\sinh t>107/520>33/175>\cos(.44\pi).
 \tag{4}
\]
The last comparison uses \(\cos(.44\pi)=\sin(.06\pi)<.06\pi\)
and \(\pi<22/7\). For the exponential bound, the upper series
\[
 e^x\le1+x+x^2/2+\frac{x^3/6}{1-x/4},\qquad x=3/7,
\]
lies below \(20/13\) by exactly \(107/31850\). Thus
\(|\Im\cot\pi(y+ic_2)|<1/2\). For (3),
\(.14\pi<11/25\), \(\cos(.492\pi)<13/500\), and
\[
 \sinh(11/25)
 \le\frac{11}{25}
    +\frac{(11/25)^3/6}{1-(11/25)^2/20}<23/50.
\]
Since \(23/50<(1-13/500)/2\), its cotangent imaginary part
is also less than \(1/2\). The explicit cotangent formula supplies
the stated comparisons throughout the rectangles, not just at their
corners. All real parts of the cotangents are positive.

The [closed cotangent theorem](research_mixed_closed_cotangent_roots.md)
therefore gives the original simple root, zero logarithmic lift,
positive triangle forms and negative real Schur Hessian throughout
the horizontal comparison. Consequently
\[
                         F(y)\le M_{12}+p(y-a_2)\quad(y\in P).
 \tag{5}
\]

The old six real phase-floor vertices can be supplemented without
any evaluation. The [seam-run theorem](research_mixed_seam_run_connector_lower.md),
equation (15), at \((a,b)=(.30,.50)\), gives
\[
 f_{00}(.30,.50)>
 .325066+.02\pi+1/20>7/16.
 \tag{6}
\]
Indeed \(\pi>25/8\), and
\(.325066+1/16+1/20-7/16=33/500000>0\).
The omitted collar allowance in (6) is nonnegative. The six old
vertices all have floor \(11/25>7/16\). Their convex hull together
with \((.30,.50)\) contains
\([.246,.391]\times[.22,.45]\). For example, the new upper-left
edge is \(y=.335+.55x\), above \(.45\) when \(x\ge.246\);
the remaining old supporting edges leave this rectangle inside.
Joint real concavity gives \(f_{00}>7/16\) throughout it.

Vertical convexity and the original acute gradients now give
\[
 F(y)>
 \begin{cases}
 1+7/16-(\pi/2)\{(\Im r_1)_++(-c_2)_+\},&\alpha=0,\\
 1+7/16-(\pi/2)(-c_2)_+,&\alpha=1.
 \end{cases}
 \tag{7}
\]
For \(\alpha=1\), lowering its negative first height increases
the conditional phase, exactly as in the
[four-three proof](research_mixed_four_three_cap_collar.md), Section 3.
The cap remains at its unchanged actual reference, where its real
phase exceeds one; its retained \(-\Re g(r_1)\) is positive.

It remains to check the complete next source, rather than only its
critical phase. On the old fixed contour
\(w=v+iy\in[1/8,1/2]+i[-1/5,5/4]\), put
\(C=\cot\pi w=u+iv_0\), \(P_x=\cot\pi(x+ik)=p_x+i\beta_x\).
The original normalized type-three marginal is
\[
 \partial_a q_\epsilon(w;a,b)
       =\log_{\rm R}(C+P_x)-\log_{\rm R}(C-i).
 \tag{8}
\]
For \(k\le0\), \(\beta_x\ge0\), and
\(p_x\le\cot(.22\pi)<5/4\), the last bound already proved in
the [symmetric-pair theorem](research_mixed_terminal_symmetric_pair_costs.md).
If \(v_0>1\), the old contour calculation gives
\((v_0-1)/u<47/75\). Thus
\[
 u(1+\beta_x)+p_x(1-v_0)
       >u(1-47/60)>0.
 \tag{9}
\]
For \(v_0\le1\) positivity is immediate. Therefore the imaginary
part of (8) is positive on the negative-height path. On a positive
height path only its upper bound \(<\pi\) is needed: both
logarithms have positive-real-part arguments, so their argument
difference lies in \((-\pi,\pi)\). At \(\Re w=1/2\) use the
same continuous boundary limit as the old proof. All factorial
arguments remain in their original regular strips, so (8) retains
its lift throughout the enlarged target domain.

Consequently the complete type-three allowance remains exactly
\[
 A_c(k)=0 (c\le k\le0),\qquad
 A_c(k)=\pi(c-k) (0\le k\le c).
 \tag{10}
\]
The zero-mode and alias kernels have no new \(k\)-dependent
penalty. For every real row the same Poisson identity gives a
nonpositive derivative at \(k<0\) and a derivative at least
\(-\pi\) at \(k>0\), proving (10) also for the complete real
complement, including zeros and wrapped rows. Thus the entire
finite-source transport proof extends, with no extra allowance.

The old calibrated pair comparisons lose only
\(11/25-7/16=1/400\). After (10), their raw reserves on all \(P\)
are therefore
\[
       3/100-1/400=11/400,\qquad
       3/125-1/400=43/2000
 \tag{11}
\]
for first types three and four, respectively.

## 3. Second type four: a full-plateau pair reserve

Here \(-.102<c_2<-.001\). The first cotangent still satisfies
the old bound \(-1<\Im\cot\pi r_1<2/3\). For every \(y\in P\),
\[
                    0<\Im\cot\pi(y+ic_2)<1.
 \tag{12}
\]
To see the upper bound, put \(t=2\pi|c_2|\le.204\pi\).
It is equivalent to \(\cos(2\pi y)<e^{-t}\). Here
\(\cos(2\pi y)\le\sin(.06\pi)<33/175\), while
\(e^{-t}\ge1-t>1-.204(22/7)>33/175\).
The [one-sided cubic chamber](research_mixed_second_four_cap_collar.md),
Lemma 1, therefore supplies the original branch and (5) on all \(P\).

Use the twelve existing real-phase floors in that note, equation
(15). The corners of \([.246,.391]\times[.22,.45]\) are the
following convex combinations; the listed points and coefficients
have matching order:

| Corner | Existing points | Coefficients | Resulting strict floor |
|---|---|---|---|
| \((.246,.22)\) | \((.30,.27),(.10,.27),(.30,.10)\) | \(741/1700,27/100,5/17\) | \(307757/425000\) |
| \((.246,.45)\) | \((.30,.33),(.10,.33),(.30,.50)\) | \(41/1700,27/100,12/17\) | \(43521/68000\) |
| \((.391,.22)\) | \((.39,.27),(.39,.10),(.50,.27)\) | \(1303/1870,5/17,1/110\) | \(370871/467500\) |
| \((.391,.45)\) | \((.39,.33),(.50,.33),(.39,.50)\) | \(533/1870,1/110,12/17\) | \(1374339/1870000\) |

The original vertical lower support is
\[
 F(y)>1+f_{01}(\Re r_1,y)
       -\frac\pi2\{(\Im r_1)_++(3/2-y)(-c_2)\}.
 \tag{13}
\]
Choose the fixed collar small enough that its original cost
\(C_1(\rho)<1/200\). The angle-independent complete pair ceiling
is \(b_\alpha+57/100+C_\alpha(\rho)\), where
\(b_0=101/125\), \(b_1=433/500\), and \(C_0\le C_1\).
For \(\alpha=1\), replace \(-c_2\) by \(51/500\) and
\(\pi/2\) by \(11/7\). The corner lower bounds for (13) minus
this ceiling are respectively
\[
 \frac{57989}{743750},\quad \frac{10443}{340000},\quad
 \frac{4815197}{32725000},\quad \frac{58737}{467500}.
 \tag{14}
\]
Every number exceeds \(3/100\); the smallest exceeds it by
\(243/340000\). The real phase plus the affine height term in
(13) is concave, so its minimum on the rectangle is bounded by
these corners. For \(\alpha=0\), the ceiling improves by
\(29/500\), while the extra first-height cost is less than
\(21\pi/2000<29/500\). The same conclusion holds. Combining
with (5) proves the actual original-tangent comparison
\[
        U_{\alpha1}(k)<M_{12}+pd_2-3/100,\qquad y_2\in P.
 \tag{15}
\]
No phase value at a new point was evaluated.

## 4. Full type-four height transport on the same contours

Retain all definitions and all currents of the
[enlarged-contour transport proof](research_mixed_four_enlarged_contour_transport.md),
but let its first real target \(x\) range over \(P\). The ordinary
reference height and the original index height obey
\(-.102<c<-.001\), \(y_0\in(-.108,.068)\). The other target
still ranges independently over \(P\) at its actual height.

For negative \(k\), its equation (8) is still positive. If
\(x+v\ge1/2\), this is immediate. Otherwise \(x<3/8\), and
\[
 \Re\cot\pi(x+ik)>4/11,\qquad
 \Re\cot\pi(w+x+ik)\le\cot(.345\pi)<6/11.
 \tag{16}
\]
For the first inequality use \(\cosh(.204\pi)<49/40\),
monotonicity in \(x\), and \(\sin(3\pi/4)>7/10\).
The bound on cosh follows from
\(1+(z^2/2)/(1-z^2/12)<49/40\) at \(z=561/875\).
For the second, \(.155\pi<49/100\); the upper sine polynomial
\(z-z^3/6+z^5/120\) divided by \(1-z^2/2\) is less than
\(6/11\) there. Thus \(F_k''>0\) as required.

On the zero-mode segment and its joins, the maximum of the old
zero-height derivative (10) is now at \(x=.22,v=1/8,y=-.108\).
It satisfies
\[
 F'_0\le .17\pi-A(.345,-.108)<23/100.
 \tag{17}
\]
Indeed \(e^{-.216\pi}>1/2\),
\(\sin(.69\pi)>41/50\), \(\cos(.69\pi)>-3/5\), so
\(A(.345,-.108)>\arctan(41/130)>41/130-(41/130)^3/3\).
Using \(\pi<22/7\), (17) has rational slack
\(29623/46137000>0\). Consequently the negative-path increase is
less than \((51/500)(23/100)=1173/50000\). On the two horizontal
alias sides, the coarser bound \(F'_0<.17\pi\) gives increase
less than \((51/500)(17\pi/100)\), still below the old alias
reserve \(13/100\).

Both selected branches decrease on the whole fixed contour.
When \(x+v\ge1/2\), the original all-height argument comparison
is unchanged. Otherwise \(\cot\pi x<5/4\) gives
\[
 (F_k^{\rm force})'
 \le \pi(1/2-x-2v+7/400)-A(x+v,-1/5)
 \le 19\pi/400-A(.345,-1/5)<0.
 \tag{18}
\]
The last argument exceeds
\(41/230-(41/230)^3/3\), since \(e^{-2\pi/5}>1/4\)
and the same sine/cosine bounds apply. Its excess over
\(19(22/7)/400\) is \(1730227/63876750>0\).
The factorial derivative is (18) plus \(A(x,k)/2-\pi<0\).
At height zero the forced branch is below the factorial branch
because \(J(x)<0\).

All real rows remain. For \(u\ge1/8\), the negative-path
allocated derivative is at most \(3\pi/200\), and the positive
factorial derivative is at most \(31\pi/200\). Their complete
increases sum to at most
\[
       \frac{153\pi}{100000}+\frac{217\pi}{100000}
                  =\frac{37\pi}{10000}<7/250.
 \tag{19}
\]
The forced positive branch increases by at most \(49\pi/4000\).
Its zero-height credit is now bounded on the full plateau by
\[
 -J(x)/2\ge\frac12\int_{.45}^{.5}\log(2\sin\pi t)\,dt
                                      >2/125.
 \tag{20}
\]
For (20), \(2\sin(.45\pi)>19/10\) and
\(\log(19/10)>2(9/29)+\tfrac23(9/29)^3>16/25\).
Thus this branch's total increase is less than
\[
       \frac{689\pi}{50000}-\frac2{125}<\frac7{250},
 \tag{21}
\]
with rational slack \(121/175000\) after \(\pi<22/7\).
Every lower real row is moved to its left cut by the unchanged
positive row derivative on \(P^2\). Every vertical alias is
bounded by the corresponding moved real cut by the old all-height
index-derivative estimates. Those arguments already had the full
plateau hypothesis. All original logarithmic zeros, wrapped rows,
and the coefficient \(+N\) remain as in the cited proof.

The maximum of these current allowances, rather than their sum,
therefore gives the complete finite bound
\[
 |C_{\epsilon,N}(Y_k,Z)|
 |d_N(Y_k)Y_k^{-N\sigma}|^{1/2}|d_N(Z)|^{\epsilon/2}
 \le C_\eta N^A e^{N\{B(x,z)+7/250+\eta\}}.
 \tag{22}
\]
Here \(B\) is the original supporting plane with its original
quadratic loss. The former real-row excess is zero by the completed
full unselected theorem. Equation (22) holds for both physical paths,
both full-weight alternatives and both parities.

## 5. Prefix and active-collar consequences

For second type four, (15) pays (22), leaving raw loss
\(3/100-7/250=1/500\). For second type three, (11) is stronger.
The first and second tangents cancel against their original neighboring
incidences. Subsequent factors use their unchanged complete planes on
independent \(P^2\); only the complex marginal at the actual cut
remains. Hence the literal prefix of the
[fixed-reference completion](research_mixed_first_collar_fixed_reference_completion.md)
satisfies
\[
 \frac1N\log\mathcal L_{h,N}
 \le M_h+\Re(P_{h,b}d_h)-\frac1{500}
 -\kappa_*\left(d_2^2+2\sum_{j=3}^{h-1}d_j^2+d_h^2\right)
 +\eta+C_{\eta,h}\frac{\log N}{N}.
 \tag{23}
\]
All weights are the literal ones in equation (25) of the enlarged
transport proof; for type three the corresponding selected label and
diagonal exponent are zero. The bound is uniform on all of (1).
The [all-real-color cap upgrade](research_mixed_first_collar_independent_plateau_middle.md),
Section 1, applies unchanged: neither the complete cap nor the
angle-independent adjacent-row estimate was enlarged. Thus (23) is
uniform for the full real color period, and on the already proved
small complex color neighborhood, with fixed ordinary jets and both
parities. Choosing one aggregate \(\eta<1/1000\) leaves finite
loss \(1/1000\).

In particular, the active first-collar pinning assembly in that note
now permits \(y_2\in P\), including all physical second heights
and selections. Its actual-cut tangent, synthetic coherent fee edges,
711-symbol collars and arbitrary middle are unchanged. Its finite
loss becomes
\[
                            1/1000+\tau/5200,
 \tag{24}
\]
where \(\tau=1\) is permitted only under its completed selected
terminal suffix hypotheses. The same disjointness from the old
plateau sources follows from \(x_1\in[0,\rho]\). Therefore the
same nonzero packet, degree and outside-color conclusions hold for
the corresponding enlarged partial source. This is not a whole-source
theorem, nor a statement about short words without the required
collars or arbitrary nonplateau physical buffers.

## 6. Why the independent endpoint rectangle alone does not suffice

For clarity, the stronger actual-reference input (3) cannot be
silently replaced by the old independent endpoint rectangle. Let
\[
 P_0=\frac{380}{461}+i\frac{261}{461},\qquad
 Q_0=\frac{11}{10}-i\frac9{20}.
 \tag{25}
\]
They decode to
\[
 r_1=\frac14-\frac{i}{2\pi}\log(19/10),\qquad
 y+ic=\frac14-\frac{\arctan(3/16)}{2\pi}
                     +\frac{i}{4\pi}\log(265/121).
 \tag{26}
\]
The first point lies in the old type-four attached rectangle, and
\(.22<y<.25\), \(0<c<.068\). For instance, the positive cubic
exponential sums at \(27/40\) and \(17/20\) exceed \(19/10\)
and \(265/121\) by \(6921/128000\) and \(717413/5808000\),
respectively; \(\arctan(3/16)<3/16<.06\pi\). These verify
the claimed bounds without evaluating the logarithms.

Nevertheless the original quadratic polynomial
\(S^2+(P_0+Q_0)S-1+i(Q_0-P_0)\) has no root with
\(\Re S\ge0\). Write \(P_0=p+i\xi,Q_0=q+i\zeta\),
\(A=p+q>0\), \(B=\xi+\zeta\). On its imaginary-zero curve
in \(S=u+iv\),
\[
 v=-B/2+\frac{p-q+BA/2}{2u+A},\qquad u\ge0.
\]
The real residual there is
\[
 R(u)=u^2+Au-1+\xi-\zeta+B^2/4
                  -\frac{(p-q+BA/2)^2}{(2u+A)^2}.
 \tag{27}
\]
It is strictly increasing. At \(u=0\),
\(v=-1271/8871\) and \(R(0)=966020/78694641>0\).
This is an exact obstruction to extending the old comparison branch
over the independent rectangular product. It is **not** a canonical
word or finite-source counterexample: its first height violates the
actual coupled bound (3). The preceding proof uses that established
coupling before enlarging the target domain.
