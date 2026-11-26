# The right incoming horizontal on the complete half-grid side

Private finite-source proof, 8 November 2026. The original right incoming
horizontal is controlled on the full half-grid side between the actual
lower shared height and the selected height. The two grid-correction
horizontals are bounded separately with their original orientations.
All physical rows, private currents, forcing terms and original measures
remain. No mathematical numerical evaluation or frozen-source edit is used.

## 1. Original source and precise contribution

Use the actual complete words in powers three and four beginning
\(343\), of length \(m\ge5\), and the reference
\((a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3)\).
Keep the original affine plane \(\Lambda_{123}(z)\) and cap plane
\(B_U(x)\) of
[the central half-grid theorem](research_mixed_next_three_central_half_grid_vertical.md).
Write
\[
\begin{gathered}
h_a=\Im a_*,\quad h_s=\Im s_*,\quad c=\Im y_*,
\quad h_t=\Im t_*,\quad h_z=\Im z_*,\quad H=1/100,\\
-.072<h_a<0,\quad -.102<h_s,c<-.001,\quad
-.03<h_t,h_z<.02,\quad 7/10<R_*=e^{2\pi c}<41/50,\\
\Gamma_H=[9/20+ih_a,1/2+ih_a],\qquad
a=x+ih_a,\quad z=u+ih_z,\quad 3/10\le u\le39/100 .
\end{gathered}                                                     \tag{1}
\]
The heights retain their actual reference correlations. There is no
outgoing halfweight for the next own-three factor.

Put \(D=N-1,\ r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(V)=(rV;r)_j\), and retain the literal kernels
\[
C_{\beta,N}(V,W)=
\sum_{j=0}^{D}\frac{V^{-j}p_j(V)p_j(W)}{P_j^{2+\beta}},
\qquad X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
\tag{2}
\]
The cap \(U_{0,N}(w,X)\) is complete and coherent. The full forced
polynomial \(d_N\), of degree at most \(D\), has
\(d_N(r^b)=P_b^{-1}\). Define, with the increasing incoming orientation,
\[
\begin{split}
F_N^H(w,Y)&=N\int_{\Gamma_H}U_{0,N}(w,X)C_{1,N}(X,Y)\,da,\\
K_N^H(y)&=\frac{N F_N^H(w,Y)d_N(Y)C_{0,N}(Y,Z)}{1-Y^N},\\
M_N&=\lceil N/2\rceil,\qquad L_N=(M_N-\tfrac12)/N,\\
V_N^H&=i\int_c^H K_N^H(L_N+ih)\,dh,\\
J_N^{H,\mathrm{grid}}
&=\int_{L_N}^{1/2}K_N^H(q+ic)\,dq
 -\int_{L_N}^{1/2}K_N^H(q+iH)\,dq .
\end{split}                                                       \tag{3}
\]
There are two original factors \(N\) in this definition. At odd levels
the grid term is zero; at even levels each horizontal has length
\(1/(2N)\).

**Theorem.** Uniformly on (1), for every real ordinary color
\(w\in[-2,2]\), both parities and all sufficiently large levels,
\[
\left|\frac{N U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{0,N}(Y,Z)}
                 {1-Y^N}\right|
\le CN^B e^{N\{\Lambda_{123}(z)-10^{-12}\}},
\quad a\in\Gamma_H,\quad y=L_N+ih,\quad c\le h\le H .
\tag{4}
\]
The same rate holds on both grid horizontals in (3). Consequently
\[
|V_N^H|+|J_N^{H,\mathrm{grid}}|
\le CN^{B'}e^{N\{\Lambda_{123}(z)-10^{-12}\}}.                 \tag{5}
\]
No outside-parameter jets, incoming-corner bound, or estimate for the
coherent middle insertion is asserted.

## 2. Complete cap and raw first alternatives

The whole cap has its original supporting rate \(B_U(x)\) on
\(9/20\le x\le1/2\). All its own physical tails, private currents
and true ends are included. We also use the independently proved
positive ceiling in
[selected right horizontal, Section 2](research_mixed_next_three_selected_left_incoming_right_horizontal.md):
\[
|U_{0,N}(w,X)|\le C_\tau N^{B_\tau}
                  e^{N(3203/3000+\tau)} .                    \tag{6}
\]
That proof is valid at every actual height in (1), and sums complete
coherent coefficients before taking its positive cap bound.

Fix the first lower cut
\[
b=1/20,\qquad A_N=\lfloor N/20\rfloor+1,\qquad
\ell_N=(A_N-\tfrac12)/N,\qquad b_N=(M_N-\tfrac12)/N .
\tag{7}
\]
The entire first low block through \(j=\lfloor N/20\rfloor\),
including \(j=0\), has whole-\(Y\)-disk rate \(169/400\).
Its product with (6) has rate
\[
3203/3000+169/400=77/50-299/6000 .                             \tag{8}
\]
Each row is a polynomial in \(Y\) of degree at most \(D\).
Thus the reciprocal-polynomial maximum principle adds at most
\(\pi/50\) on \(|Y|\le e^{\pi/50}\), before the positive row sum.
The limiting real cut has the same bound directly: its outgoing
modulus changes from at most two to at most \(2e^{\pi/50}\), adding
only \(b\pi/50\).

At any shared height \(h\in[c,H]\), the complete first last rate is
\[
L_1(h)=-2\pi h_a+2\pi h_+ .
\tag{9}
\]
The period means and original incoming chirp are included. Its
cap-times-last upper envelope is strictly below
\[
B_f=77/50+\pi/50,\qquad
B_f-\{3203/3000+18\pi/125+\pi/50\}>83/4200 .                  \tag{10}
\]
The strict reserves in (8),(10) absorb their own finite tolerances.

Apply
[the half-grid bounded-factor theorem](research_mixed_next_three_half_grid_bounded_prefix.md)
to these complete raw groups. It pays an index-independent preceding
upper envelope of rate at most \(B_f\) against the full
\(d_N(Y)C_{0,N}(Y,Z)/(1-Y^N)\), on this vertical and both endpoint
horizontals, with gap \(1/1000\). In particular the first low block,
its real-cut alternative and the full first last alternative are
already paid. This application does not divide by any weight or
source that may vanish.

## 3. Original profile calibration at the lower endpoint

Retain the original primitive and bare phase
\[
g'(\zeta)=\operatorname{Log}(1-e^{-2\pi i\zeta}),\qquad
Q_\beta(v;b_1,b_2)=g(b_1+v)+g(b_2+v)-(2+\beta)g(v)
                 -g(b_1)-g(b_2)+2\pi i b_1v .
\tag{11}
\]
The nonraw first family consists of
\[
\Re Q_1(s;a,y),\quad s=v+ih_s,\ b\le v\le1/2,
\qquad\text{and}\qquad \Re Q_1(1/2;a,y).
\tag{12}
\]
The next controlling family consists of
\[
\Re Q_0(t;y,z),\quad t=v+ih_t,\ 3/20\le v\le1/2,
\quad \Re Q_0(3/20;y,z),\quad\Re Q_0(1/2;y,z),\quad
L_0(h)=2\pi(-h)_++2\pi(h_z)_+ .
\tag{13}
\]

At \(y=9/20+ic\), the proof in
[unselected right tail, Sections 2--4](research_mixed_next_unselected_incoming_right_tail.md)
gives the full allocated supporting bound for every first main
with \(1/8\le\Re s\le1/2\). After adding the complete cap plane
it retains
\[
\kappa_0(x-\Re a_*)^2
\ge\frac{3481}{2500000000000}>10^{-9},
\qquad \kappa_0=1/2500000 .
\tag{14}
\]
The first real half keeps its original \(1/2000\) deficit:
its incoming derivative is independent of the shared target and
is strictly negative throughout this right segment.
The ordinary next profiles in (13), including their allocated last
alternative, obey their original supporting plane by
[three-row source assembly, Sections 1--2](research_mixed_three_row_source_assembly.md).
Its proof bounds each profile before summation. For the last profile
only the already established strict sign is used; no unspecified
numerical margin is spent. Combining the two original halfweights
leaves the full shared term \(-\Re g(y)\). Thus all these paired
profiles have a common reserve greater than \(10^{-10}\).

The added first main indices \(b\le v\le1/8\) increase to \(1/8\).
Indeed, put \(r_s=e^{2\pi h_s}\in(1/2,1)\). On
\(x,q\in[9/20,1/2]\), both shifted real coordinates \(x+v,q+v\)
are at least \(1/2\) and at most \(5/8\). Both folded numerator
moduli therefore exceed one, for every positive shared radius.
The own squared modulus is less than \(3/5\), by convexity in
\(r_s\) and \(\cos(2\pi v)\ge\sqrt2/2>7/10\).
The exact index force is greater than one. This clipping is valid
at both shared endpoints and throughout the height interval.

Transport from \(q=9/20\) to \(1/2\) at height \(c\), retaining
all private heights and cuts. Put
\[
R=R_*,\quad A=e^{-2\pi h_t}<11/9,\quad
D_q=|1-Re^{-2\pi iq}|^2
 >(39/40)(1+R)^2 .
\tag{15}
\]
For a first nonlast profile and a next nonlast profile the
exponential of their joint derivative, with \(-\Re g(y)\), is
at most
\[
\frac{(1+R)(A+R)}{D_q^{3/2}}<20/27<1 .
\tag{16}
\]
At a real next cut use \(A=1\). The written rational witnesses are
\[
\frac{A+R}{(1+R)^2}
\le\frac{1730}{2601}<2/3,\qquad
(39/40)^{3/2}>9/10 ,
\]
exactly as in the central half-grid proof. The first index enters
only through its nonpositive height; the incoming real coordinate
\(x\) cancels from this derivative. For the next-last profile the
derivative exponential is at most \((1+R)/D_q<1\).
At \(q=1/2\), \(\Re g(1/2+ic)=0\). Hence for every pair in
(12),(13),
\[
B_U(x)+\phi_1(c)+\phi_0(c)
 <\Lambda_{123}(z)-10^{-10}.                                 \tag{17}
\]

## 4. The selected upper endpoint and shared-height convexity

At \(q=9/20,\ h=H\), Sections 2--4 of
[the original selected right segment](research_mixed_second_selected_first_three_right_segment.md)
give the pointwise first-main/next-main gap \(1/100\), the next-half
gap \(1/20\), and next-low reduction to its main. The first real
half is below its trial main by \(1/30\) on the whole right incoming
interval. The next-last comparison retains gap \(1/400\).
Both selected weight alternatives are retained:
\[
W_{\rm fac}=-\Re g(y)-2\pi H,\qquad W_{\rm force}=0 .
\tag{18}
\]
These are the sourcewise bounds from that proof, not a decomposition
of a signed finite-kernel estimate. The lower first indices in (12)
clip as in Section 3.

The transport from \(q=9/20\) to \(1/2\) in
[near-half central, Section 2](research_mixed_next_three_selected_near_half_central.md)
is independent of \(x\). Explicitly every nonlast first profile has
\[
\partial_q\phi_1\le\tfrac12\log(40/39).
\tag{19}
\]
The next main clips upward to \(11/50\). For that clipped main and
both real cuts its derivative is less than
\(\tfrac12\log(39/40)\). These statements use the actual
\(u\in[.30,.39]\), \(e^{-2\pi h_t}<11/9\); all heights are unchanged.
The factorial branch in (18) has an additional negative derivative.
Thus both joint nonlast rates decrease. For next last, the possible
increase over the interval is less than
\[
\frac1{40}\log(40/39)<1/1560 .
\tag{20}
\]
The old \(1/400\) reserve leaves more than \(1/1000\).
In particular the forcing choice in (18) gives at \(q=1/2\)
\[
B_U(x)+\phi_1(H)+\phi_0(H)
 <\Lambda_{123}(z)-1/1000 .                                  \tag{21}
\]

At \(y=1/2+ih\), the real part of \(g(y)\) is zero for every
\(h\). For every fixed private main or real-cut index,
\[
\begin{split}
\partial_h^2\Re Q_1(s;a,1/2+ih)
 &=-\pi\Re\cot\pi(1/2+ih+s)\ge0,\\
\partial_h^2\Re Q_0(t;1/2+ih,z)
 &=-\pi\Re\cot\pi(1/2+ih+t)\ge0 .
\end{split}                                                       \tag{22}
\]
The next chirp is affine in \(h\). At a half index take the
continuous zero-safe numerator limit; its upward height-derivative
jump preserves convexity. The full next last carrier in (13) is
convex as well. Each fixed sum in (17),(21) is therefore convex
on \([c,H]\), and
\[
B_U(x)+\phi_1(h)+\phi_0(h)
 <\Lambda_{123}(z)-10^{-10}\qquad(c\le h\le H).
\tag{23}
\]
No eliminated critical action is declared convex.

## 5. Complete physical rows and private currents

For the first upper physical block use
[transformed upper rows, Lemma 1](research_mixed_transformed_upper_rows.md).
Its proved domain is the full independent square \([.22,.5]^2\)
with absolute external heights at most \(.108\). Thus every
present first upper row is bounded positively by its real-half or
full last rate, including the even half row, the odd first upper
row and \(j=D\). Its half alternative uses (23); its last uses
the complete raw attachment (10). Individual upper-row rates are
not assumed convex in the shared height.

For the first middle retain the exact interpolation
\[
T_N(s;a,y)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(y+s)
                              E_N(a)E_N(y)E_N(s)^3 .
\tag{24}
\]
Initially take the limiting cuts \(b,1/2\) and \(q=1/2\).
For \(b\le v<1/2\), both shifted real coordinates \(x+v,q+v\)
are at least one half and at most one. Their real cotangents
are nonpositive at every height, whereas the own real cotangent
is positive. Consequently
\[
\Re Q_{1,ss}(v+i\sigma;a,y)<0\qquad(-\infty<\sigma<\infty).
\tag{25}
\]
The original argument \(J_1=\Im Q_{1,s}\) decreases in \(\sigma\).
Its two original strip limits are
\[
\lim_{\sigma\to-\infty}J_1=2\pi x\le\pi,\qquad
\lim_{\sigma\to+\infty}J_1=\pi(-1-2q+2v)\ge-19\pi/10 .
\tag{26}
\]
At either numerator wall use the one-sided continued upper rate;
its upward height-derivative jump has the same monotonicity.
Thus the same integrated bounds hold at the half cut.

Keep first alias heights \(-1/5,+4\). Relative to the same-index
main at \(h_s\), their losses are at least
\[
2\pi/5-\pi/5=\pi/5,\qquad
8\pi-(19\pi/10)(4+51/500)
 =1031\pi/5000>\pi/5 .
\tag{27}
\]
Both weighted half-sides at each real cut decrease away from zero;
the lower and upper derivative reserves are respectively \(\pi\)
and \(\pi/10\). The real lower cut uses the raw attachment, and
the real half uses (23). By (25), each unweighted join from zero
to \(h_s\) is convex and is bounded by its two endpoint profiles.
At the half cut weak convexity suffices. The full incoming or
outgoing numerator zero uses the original period/reflection
upper rate, not a nonzero local symbol.

The next kernel retains exactly the complete half-grid reduction
of the central theorem: cuts \(3/20,1/2\), main height \(h_t\),
alias heights \(-1/5,+8\), both horizontal currents, four weighted
half-sides, and both unweighted joins. Its argument bounds
\(-39\pi/50\le\Im Q_{0,t}\le11\pi/10\) do not impose a sign on
the shifted heights. Its low join has own cotangent greater than
\(3/2\), incoming cotangent nonpositive and outgoing positive
cotangent less than \(1/5\). Its half join is weakly convex.
The whole next low block increases to its real low cut.
Its upper block obeys the same full-square upper-row theorem,
and reduces positively to (13). These are same-coordinate
comparisons, valid with each fixed first profile still attached.

For the first kernel keep all physical indices
\[
0\le j<A_N,\qquad A_N\le j<M_N,\qquad M_N\le j<N
\tag{28}
\]
with (7); use the analogous partition for the next cut \(3/20\).
The exact middle cotangent identity has its original \(+N\) main
measure, two horizontal aliases and four weighted pieces.
Deforming the constant mode retains the two unweighted joins
just estimated. There is no additional frequency truncation.

The source estimates in (23) are before \(d_N\) is attached.
For the supporting-cap groups, uniform factorial and zero-safe
numerator bounds give rate \(\Lambda_{123}-10^{-10}+\tau\)
for each resulting finite group at \(q=1/2\).
Raw low, real-low and last groups instead use the complete
bounded-factor attachment directly. No forced polynomial is
divided out of an estimate. All sums and canonical integrals
have only polynomial prefactors.

## 6. Actual half grids, forced denominator, and orientations

The private half grids in (7) and their next analogues differ from
the limiting cuts by \(O(1/N)\); the shared coordinate \(L_N\)
differs from \(1/2\) by at most \(1/(2N)\).
The displayed strict comparisons persist with arbitrarily small
rate tolerance on the bounded retained rectangles. At a numerator
wall use the original integrated-log continuity and zero-safe
midpoint period/reflection bound. Its displacement cost is
\(O((\log N)/N)\) in the action, hence polynomial in the finite
source. Every denominator argument remains regular. In particular
the small possible excursion of the lower private cut does not
require an all-height sign assertion outside the limiting strip.

The full forced estimate, with its interpolation remainder, is
\[
|d_N(e^{-2\pi iy})|\le C_\tau N^B
 e^{N\{\max(-\Re g(y),\,2\pi(\Im y)_+)+\tau\}} .
\tag{29}
\]
Near the present half-period side \(g'\) is bounded and
\(\Re g(1/2+ih)=0\). On the exact shared half grid,
\[
\Re g(L_N+ih)=O(N^{-1}),\qquad
Y^N=-e^{2\pi Nh},\qquad |1-Y^N|=1+e^{2\pi Nh}.
\tag{30}
\]
Thus \(d_N(Y)/(1-Y^N)\) has arbitrarily small exponential
upper rate throughout the vertical, including height zero.
Multiplying the supporting-cap source groups from Section 5
by this bound pays them. The raw groups were already paid with
this same quotient.

On the lower grid horizontal use
\(|1-Y^N|\ge1-R_*^N\). On the upper one write exactly
\[
\frac{d_N(Y)}{1-Y^N}
 =-\frac{d_N(Y)Y^{-N}}{1-Y^{-N}} .
\tag{31}
\]
Its denominator is uniformly away from zero, and the forced
numerator on this \(O(1/N)\) interval has arbitrarily small
rate by (29). The profile endpoint comparisons and their
zero-safe displacements pay both horizontals separately.

Choose common tolerances inside (23), and then weaken to
\(10^{-12}\). This proves (4). The incoming measure is the
original \(+N\,da=+N\,dx\); the shared measure on the vertical
is upward \(i\,dh\). Bounded path lengths and the second factor
\(N\) give only polynomial cost. The bottom-minus-top signs
are exactly those in (3), proving (5).

This is a contribution of the original unfiltered first prefix.
It may be subtracted linearly in the old filtered source; no
new cardinal filter is applied to this partial incoming path.
The old filter correction has its separate half-grid theorem.
The incoming corner, other missing first paths, and the
coherent middle insertion remain separate from this result.
