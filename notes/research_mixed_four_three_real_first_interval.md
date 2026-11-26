# The complete real first interval for an initial four/three pair

Private written deduction, 10 November 2026.

The first real coordinate can approach zero while the second coordinate
retains its actual height, of either sign. The high physical rows are
kept in full. Their regular-cap maximum increases toward the already
calibrated one-tenth face. A separate reserve pays the possible reverse
motion of the true-cap-end maximum. Only after obtaining a complete
real interval do we use the exact Laurent degree to include zero.

## 1. Exact source and profiles

Fix an actual positive three/four word of length at least three beginning
with four and three. Keep its reference, logarithmic lifts, ordinary
color and original normalization. Write
\[
 h_e\in[-.051,-.019],\qquad h_s,d\in[-.065,.068],\qquad
 b=z+id,\quad z\in P=[11/50,9/20],\qquad l=1/10.
\tag{1}
\]
These are containing bounds for the same actual reference. No independent
reference box or moving critical point is introduced.

For \(q_N=e^{-2\pi i/N}\), set \(P_j=(q_N;q_N)_j\),
\(p_j(X)=(q_NX;q_N)_j\), \(X=e^{-2\pi ix}\), and
\(Y=e^{-2\pi ib}\). Retain the complete finite functions
\[
\begin{split}
 U_N(w,X)&=\sum_{i=0}^{N-1}
       H_N(w,q_N^{-i})\frac{p_i(X)}{P_i^2},\\
 C_N(X,Y)&=\sum_{j=0}^{N-1}R_{j,N}(x,b),\qquad
 R_{j,N}=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^2},\\
 K_{\sigma,N}(w;x,b)&=U_N(w,X)C_N(X,Y)d_N(X)X^{-N\sigma},
                                      \qquad\sigma\in\{0,1\}.
\end{split}
\tag{2}
\]
There is no outgoing halfweight at the own-three coordinate. The
first weight is complete, including its forcing; both first monomials
have modulus one on the real interval.

Use the original phases and integrated row rate
\[
\begin{split}
 \Psi(e,x)&=S(e)+g(e+x)-g(x)-g(e)-\tfrac{i\pi}{2}(e-e^2),\\
 Q(s;x,b)&=g(s+x)+g(s+b)-2g(s)-g(x)-g(b)+2\pi ixs,\\
 J(t)&=\Re g(t),\\
 E(t;x,b)&=\int_0^t\log|1-e^{-2\pi i(x+u)}|\,du
       +\int_0^t\log|1-e^{-2\pi i(b+u)}|\,du-2J(t).
\end{split}
\tag{3}
\]
The last expression is continuous through every integrated numerator
zero. Its literal full-period value is
\[
                              E(1;x,b)=2\pi d_+.
\tag{4}
\]
The affine rate \(\Lambda(z)\) is exactly the one in the
[four/three zero-face theorem](research_mixed_selected_four_three_zero_height_face.md):
it is the original value of \(\Psi+Q-g(a)\) at the actual reference
plus its original outgoing derivative times \(z-\Re b_*\).

The regular cap collection \(\mathscr E\) consists of
\[
\begin{array}{c|c}
 e&\text{penalty }p_e\\\hline
 u+ih_e,\quad .27\le u\le.49&0\\
 .27,\ .49&0\\
 u-.055i,\quad .27\le u\le.49&.11\pi\\
 u+.04i,\quad .27\le u\le.49&.08\pi.
\end{array}
\tag{5}
\]
Its separate true-end ceiling is
\[
                         A_* =3/5+\log4/100.
\tag{6}
\]
Keep the entire ordinary central collection \(\mathscr S\): main
\(v+ih_s\), \(.15\le v\le.5\); both zero-mode joins from height
zero to \(h_s\) at the two cuts; horizontal aliases at heights
\(-.2,.2\) with penalty \(.4\pi\); and all four vertical alias
halves between these heights and zero, with penalty
\(2\pi|\Im s|\). The real cuts are included. All these sets
are fixed independently of \(x\) and \(N\).

For \(x>0\), the complete first Fourier upper rate is
\(\max\{-J(x),0\}=-J(x)\). Define the regular and true-end
joint high envelopes by
\[
\begin{split}
 T_e(x,b)&=\Re\Psi(e,x)-p_e-J(x)
                         +\max_{1/2\le t\le1}E(t;x,b),\\
 T_*(x,b)&=A_*-J(x)+\max_{1/2\le t\le1}E(t;x,b).
\end{split}
\tag{7}
\]
No maximum in (7) is replaced by a half or last row when \(d>0\).

**Theorem 1.** For every fixed \(0<\rho<1/10\) and every
\(\tau>0\), the complete source (2) has rate at most
\(\Lambda(z)-1/1000+\tau\) on \([\rho,1/10]\), with a
polynomial prefactor. On the closed interval \([0,1/10]\) it has
rate at most \(\Lambda(z)-1/2000+\tau\). Both first selections,
both level parities and every real ordinary color are included.
The same conclusions hold on sufficiently small fixed ordinary-color
disks, with fixed derivatives on smaller disks and the same prescribed
rate allowance. The second target is throughout (1), at its unchanged
actual height. Constants may depend on the fixed word and, for the
first assertion, on \(\rho\).

## 2. The complete bare cap still has these profiles

For each fixed \(0<\rho<l\), the complete bare cap is bounded,
uniformly on \(\rho\le x\le l\) and the whole real ordinary-color
interval, by the maximum of (5)--(6), with arbitrary rate allowance
and a polynomial factor. This is precisely the bare-cap argument in
Section 2 of the
[four/four real-interval proof](research_mixed_four_four_real_first_interval.md).
That argument involves only the first type-four source \(U_N\),
the standalone endpoint action \(S\), and the height \(h_e\) in
(1); the next own type and its height are not used.

For clarity, its physical row rate is
\[
             \lambda(t)+J(t+x)-J(x)-J(t),\qquad\lambda=\Re S.
\tag{8}
\]
The original coefficient estimates give increasing compact lower
rows through \(.27\), decreasing upper rows from \(.49\), and
the same all-real-color bounds. The true upper end uses the
minimum integral over an arc of length \(\delta\):
\[
 J(\delta)-2J(\delta/2)
     =\int_0^\delta\log(2\cos(\pi u/2))\,du\le\delta\log2.
\tag{9}
\]
Combined with its original coefficient entropy
\(3/5+\delta\log2\), this yields (6), including when the
omitted numerator arc contains a zero. The small true end has the
smaller rate \(1/4\). All finite-product statements are upper
bounds through zeros; no omitted product is divided out.

On the central cap rectangle the shifted argument has real part
in \([.27+\rho,.59]\). The same original curvature inequality
\(-\Re\Psi_{ee}>2\pi\Re\cot\pi e-\pi\Re\cot\pi(e+x)>0\)
reduces the zero-mode joins and weighted vertical halves to (5).
The complete marked interpolation retains its \(+N\) density and
both aliases. Thus this source transfer changes no finite cap term,
reference calibration or color quantifier.

## 3. Low physical rows and every central current

For a regular cap point in (5) and any fixed private point in
\(\mathscr S\), put
\[
 D=2\sin\pi x,\qquad N_e=|1-e^{-2\pi i(e+x)}|,\qquad
 N_s=|e^{-2\pi\Im s}-e^{-2\pi i(\Re s+x)}|.
\]
The exact derivatives of the fully allocated rates are
\[
\begin{split}
 \partial_x(\Re\Psi(e,x)-p_e+\Re Q(s;x,b)-p_s-J(x))
                    &=\log(N_eN_s/D^3),\\
 \partial_x(A_*+\Re Q(s;x,b)-p_s-J(x))
                    &=\log(N_s/D^2).
\end{split}
\tag{10}
\]
The ordinary chirp is included in \(N_s\); both alias penalties
are constant in \(x\).

Here \(.27<\Re(e+x)\le.59\), so \(N_e>1\).
For every finite private height and
\(.15<\Re(s+x)\le.6\), minimization over its positive radius
gives \(N_s\ge1/\sqrt2>7/10\). Also
\[
                 0<D\le2\sin(\pi/10)<5/8.
\tag{11}
\]
Consequently both derivatives in (10) are positive, uniformly on
each fixed \([\rho,l]\). This includes positive \(h_s\), every
zero-mode join, and all horizontal and vertical alias points. No
new private-curvature or alias comparison at a smaller \(x\) is
needed: these raw profiles are transported individually to \(l\).

For low physical rates \(0\le t\le3/20\), the same formulas
hold with \(N_s=2\sin\pi(x+t)\). Since
\(x\le x+t\le1/4\), this satisfies \(N_s\ge D\).
The regular derivative is therefore at least
\(\log(N_e/D^2)>0\), and the true-end derivative is at least
\(-\log D>0\). Every low rate is kept; no increasing finite-row
ratio at the smaller first angle is assumed.

Proposition 2 of the zero-face theorem bounds all the corresponding
profile products at \(x=l\) by \(\Lambda(z)-1/1000\).
Integrating (10) and the low-rate derivative proves that same bound
throughout \([\rho,l]\), for every regular cap profile and its
separate true-end alternative.

## 4. Stationary high rows and regular cap transport

At any differentiable stationary high row, write
\[
 v=1-t,\quad Q_v=2\sin\pi v,\quad
 N_x=2|\sin\pi(x-v)|,\quad
 N_b=|1-e^{2\pi d-2\pi i(z-v)}|.
\]
The exact own-three row derivative, including its first-argument
chirp, gives
\[
             N_xN_b=Q_v^2.
\tag{12}
\]
The [reflection lemma](research_mixed_right_tail_reflection.md),
Lemma 1, applies whenever \(0\le v\le x\le z\le1/2\).
It bounds those late rates by (4), retaining the drift \(2\pi d_+\).
At \(v=x>0\) the comparison is strict: its second-leg integral
over \([z-x,z]\) is strictly greater than \(J(x)\), since
\(z>x\). Thus a high maximum can be represented by the last
carrier, the half endpoint, or a stationary row with
\[
                         x<v<1/2,
\qquad Q_v\ge D.
\tag{13}
\]
A row at a real numerator zero cannot be an interior maximum:
its row derivative tends to \(-\infty\) on both sides, so the
integrated rate decreases through that point. This includes the
second wall when \(d=0\).

At a stationary row in (13), the exact joint derivatives are
\[
 \partial_x T_{e,\mathrm{row}}
       =\log(N_eN_x/D^3)
       \ge\log\frac{N_e/D}{N_b},\qquad
 \partial_x T_{*,\mathrm{row}}
       =\log(N_x/D^2)\ge-\log N_b.
\tag{14}
\]
The first comparison is uniformly positive. Here is a fully
written elementary bound on its correlated numerator.
Put \(R=e^{2\pi\Im e}>7/10\) and \(u=\Re e\).
For the radius bound, \(.11\pi<7/20\) and the positive series gives
\(e^{7/20}\le3009/2120<10/7\), using
\(e^t\le1+t+t^2/[2(1-t/3)]\).
For fixed \(R,u\) in (5),
\[
 \frac{N_e^2}{D^2}
   =\frac{(R-1)^2}{4\sin^2\pi x}
            +R\bigl(\cos\pi u+\cot\pi x\sin\pi u\bigr)^2
\tag{15}
\]
decreases in \(x\in(0,l]\). The expression inside the square
is \(\sin\pi(u+x)/\sin\pi x>0\) and has negative derivative.

At \(x=9/100\), the sum \(u+x\) lies in \([.36,.58]\)
and its twice-angle cosine is less than \(-3/5\). For example
\(\cos(.28\pi)>1-(22/25)^2/2=383/625>3/5\);
the other endpoint cosine is smaller. Therefore
\[
 N_e^2>1+49/100+21/25>9/4,\qquad
 D<99/175,\qquad N_e/D>175/66>51/20.
\tag{16}
\]
Since the [original high-row radius bound](research_mixed_unwrapped_stationary_high_row_transport.md) gives
\(e^{2\pi d}<31/20\), one always has \(N_b<51/20\).
Equation (15) and (16) prove positivity for \(x\le9/100\).

At \(x=l\), the sum \(u+x\) lies in \([.37,.59]\), and
its twice-angle cosine is less than \(-2/3\). An elementary
witness is
\[
 \cos(.26\pi)>\cos(5/6)
       >47/72+19/1000>2/3.
\tag{17}
\]
In the alternating cosine series the quartic term at \(5/6\)
is greater than \(1/50\), and the sextic term is less than
\(1/1000\), proving the middle inequality. The opposite angular
endpoint is smaller. It follows that
\[
 N_e^2>727/300>(31/20)^2,\qquad N_e/D>62/25.
\tag{18}
\]
If \(9/100\le x\le l\) and (13) holds, then
\(|z-v|\le9/25\). Hence \(\cos2\pi(z-v)>-2/3\):
use \(.28\pi>6/7\), from \(\pi>25/8\), and
\(\cos(6/7)\le1573/2401<2/3\).
Convexity of the squared modulus in its radius, or its endpoint
bound on \(0\le e^{2\pi d}\le31/20\), gives
\[
 N_b^2<1+961/400+31/15<(47/20)^2.
\tag{19}
\]
Combining (15), (18)--(19) yields
\[
                    \frac{N_e/D}{N_b}>248/235>1.
\tag{20}
\]
This argument treats both sides of the second wall, with either
sign of \(d\). No independent radius or drift is removed.

At the half endpoint the incoming numerator is \(2\cos\pi x\),
so both joint derivatives are positive by (11) and \(N_e>1\).
At the last carrier the two derivatives are
\(\log(N_e/D^2)>0\) and \(-\log D>0\), respectively.

It follows that, for every regular cap point and penalty,
\[
                         T_e(x,b)\le T_e(l,b).
\tag{21}
\]
Here is the maximum argument, including switches and degeneracies.
On a fixed compact \([\rho,l]\), the row rate is continuous.
An active row is either one of the two described endpoints or a
stationary row away from numerator zeros; the late wall is strictly
below the included last carrier. Compactness separates active
interior rows from the singular walls. At any current maximizer,
hold its row fixed and increase \(x\) slightly. Equations
(14)--(20) give a positive derivative on a neighborhood of that
active pair. The maximum at the new \(x\) is at least this
fixed-row value. Compactness and a finite covering, or the equivalent
one-sided maximum-envelope argument, show monotonicity on the full
interval. This does not choose a differentiable maximizing branch
and applies equally to a degenerate stationary row. The estimates
are uniform over the compact cap collection, so one may maximize
over that collection afterwards. The zero-face profile theorem
then pays (21) with gap \(1/1000\).

## 5. The larger reserve for true cap ends

The same maximum argument applied to the true-end derivative bound in
(14) gives
\[
                   T_*(x,b)\le T_*(l,b)+(l-x).
\tag{22}
\]
Indeed \(N_b<51/20<e\), the last inequality following from
the first four terms of the positive exponential series, so every
active stationary derivative is greater than \(-1\). The half
and last derivatives are positive. Applying the preceding argument
to \(T_*(x,b)+x\) proves (22).

We must not pay this possible loss with the zero-face theorem's
smaller displayed common gap. Its proof retains a larger true-end
reserve, as follows. At the old face \(a=11/50+iH\),
\(H=7/625\), the
[complete selected early source](research_mixed_selected_four_three_early_complete_source.md)
has
\[
 A_0>199/250,\qquad A_*(H)<69/100,\qquad
                       A_0-A_*(H)>53/500.
\tag{23}
\]
The [selected plateau theorem](research_mixed_selected_four_three_full_product.md)
and the full high-row reduction in Section 3 of its
[finite-source reduction](research_mixed_selected_four_three_finite_reduction.md)
pay \(A_0\) times every old-face high rate with gap \(1/2000\).
They pay the last carrier with the stronger gap \(3/100\).
Subtracting (23) is legitimate before any row sum: the same scalar
\(A_0\) is present for every high profile at that fixed face.

Section 5 of the zero-face proof transports the true-end high maximum
on \([1/2,1-z]\) from that face to \(x=l\). Its written gain
after the height reset is greater than \(22/625\). Thus the
larger starting reserve gives a zero-face gap greater than
\[
                     53/500+1/2000+22/625>1/8.
\tag{24}
\]
The wrapped rates up to \(1-l\) are bounded there by the value at
\(1-z\), in the same proof. The remaining late rates are bounded
by the last carrier. For that carrier, Section 4 of the zero-face
proof gives a favorable real displacement and no unfavorable
true-end height reset. Its starting gap is already
\(53/500+3/100>1/8\). Consequently the entire true-end high
envelope satisfies
\[
                              T_*(l,b)<\Lambda(z)-1/8.
\tag{25}
\]
This is a consequence of the original profile proofs, not an added
assumption or a lower bound for a finite cap. Equation (22) now gives
\[
                   T_*(x,b)<\Lambda(z)-1/40,
                                      \qquad 0<x\le l.
\tag{26}
\]
Thus the high true ends retain a gap larger than the common
\(1/1000\), even though their envelope need not be increasing.

## 6. Complete finite source and the closed real interval

Fix \(\rho>0\). Partition the ordinary physical sum at
\(\lfloor3N/20\rfloor\) and \(\lceil N/2\rceil\).
Every low row is bounded by its retained continuous rate from
Section 3. Every high row is bounded by (3), with all its zeros,
wrapped factors and literal terminal index retained. The original
zero-safe product argument gives these upper rates uniformly on
all indices, at a polynomial cost and any prescribed allowance;
its denominator error is \(O(\log N)\) through \(j=N-1\).
Equations (21), (26) pay the complete high block. Both midpoint
parities are included, and no finite half or last value is divided out.

For the central block use the original marked factorial interpolation
with half-grid cuts tending to \(.15,.5\), and alias heights
\(-.2,.2\). Its shifted real arguments lie in
\([.15+\rho,.6]\) and \([.37,.95]\), inside their original
regular strips. Its exact cotangent residue formula has coefficient
\(N/(2i)\), zero-mode density \(+N\), both aliases and four
vertical halves. Moving only the zero mode to the fixed \(h_s\)
retains both joining currents. These are exactly \(\mathscr S\),
already paid pointwise in Section 3, for either sign of \(h_s\).

The cap source in Section 2 includes all its physical indices and
current corrections. Multiply by the whole first Fourier bound
\(-J(x)\), which dominates its other alternative zero. The
selected monomial has unit modulus. Choosing the finite number of
tolerances inside one prescribed \(\tau\), and summing the finite
blocks, proves
\[
 |K_{\sigma,N}(w;x,b)|\le C_{\rho,\tau}N^{A_{\rho,\tau}}
             e^{N\{\Lambda(z)-1/1000+\tau\}},
                       \qquad \rho\le x\le1/10.
\tag{27}
\]
This is uniform for all real ordinary colors and both parities.
It uses the complete original two-factor source, not an extrapolation
of its asymptotic error or a positivity assertion about its coefficients.

The Laurent exponent support of (2) in \(X\) is contained in
\([-(1+\sigma)N+1,(2-\sigma)N-2]\), hence has radius at most
\(2N\). Lemma 1 of the
[real endpoint continuation theorem](research_mixed_four_four_real_first_endpoint.md)
is a statement for any such Laurent polynomial. Apply it with cost
\(1/4000\), choosing its nondegenerate interval
\([\rho,a]\subset(0,1/10)\) before \(N\), and use (27) with
source allowance \(1/4000\). It fills \([0,a]\) at remaining
gap \(1/2000\); the rest of (27) has a larger gap. We obtain
\[
 |K_{\sigma,N}(w;x,b)|\le C_\tau N^{A_\tau}
                  e^{N\{\Lambda(z)-1/2000+\tau\}},
                         \qquad 0\le x\le1/10.
\tag{28}
\]
All choices are fixed before \(N\). This last step starts with a
proved full interval (27), rather than a tiny neighborhood of the
single face \(x=l\); the latter alone would not give the stated
small extrapolation cost over distance \(l\).

The ordinary-color degree is less than \(N\). Uniform interval
polynomial continuation from the whole real color interval gives
a fixed ordinary-color disk at any additional prescribed rate cost.
Cauchy's formula on a smaller disk gives every fixed color derivative
with polynomial cost. The choices are uniform in \(x,z\), with
the actual reference held fixed, and may depend on the fixed word.
At \(x=0\), the exact Laurent polynomial is evaluated at \(X=1\);
no logarithmic factorial symbol is continued through its endpoint.

This proves a complete real first interval for both first selections,
with the second variable throughout its plateau at its actual height
of either sign. It does not change that second height, pay a vertical
first-coordinate join, estimate the remaining first period, or imply
whole-word, knot or finite-exception noncancellation.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_selected_four_three_zero_height_face.md | f2c781f91df31cbb892f34d76c5ca5c4deac6e6cd4eda0ac7514bbe3f1ecdd36 |
| research_mixed_four_four_real_first_interval.md | b848eb005f99d57259662ef3a864b207e093b6ebfaf4c34c2dbcc1e9727d58fc |
| research_mixed_selected_four_three_early_complete_source.md | c0f4532b7f8d04c3bc4d84f16435029625c469adf1282914f80bf019bd22ebd6 |
| research_mixed_selected_four_three_full_product.md | 410c91677327cbea7f856e705b958ae011f93f29321f2c0c2ed7fc7100432c18 |
| research_mixed_selected_four_three_finite_reduction.md | 732d6cbf79894cb1e230e4eefa27762e369d84127d67e9e7c0d66c77901bbd42 |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_unwrapped_stationary_high_row_transport.md | 24210764f62ef04250a63dbcb5b5e82d4bdf59ede7eacb88889e5318dfc4d4aa |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| exact_factorial_interpolation_and_complex_contours.md | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| research_mixed_horizontal_asymmetric_contour.md | 2b0984562d9d3c63e2e366d9dc3b68f557512b71c74290f8ac530fcb4d3e7fce |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_four_four_real_first_endpoint.md | 4ceec7f835d08ef971b3b3ccadcf7eecd74e48db3d422cbd09e5611c0572c122 |

The full written proof and directly used source implications were read.
No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was performed.
