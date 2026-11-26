# The complete central own-three source on the actual cap-343 family

Private finite-source assembly, 8 November 2026. The original cap,
complete first own-four kernel, full shared weight and complete next
own-three kernel have a strict lower-left bound on the central first
incoming segment. The reference is the actual open critical point of
a word beginning \(343\), of length at least five. The two geometric
height inequalities are supplied by their separate correlated-height
theorem; no root or saved mathematical value is evaluated here.

Every next finite index and both parities are retained. This is a
central incoming estimate. It does not replace the complete first
incoming cycle or estimate the remaining signed Fourier contours.
Earlier frozen notes and public manuscripts are unchanged.

## 1. Actual references, geometric inputs and literal source

Take a complete word in the original powers three and four, beginning
\(343\), with length \(m\ge5\). Use its original zero-logarithm-lift
critical point and the notation
\[
 (a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3),\qquad
 P=[11/50,9/20].                                             \tag{1}
\]
Both conditional vertices in (1) are ordinary. The following external
leg is the actual \(b=s_4\), with its inherited role; it is not a freely
chosen replacement for a complete suffix. Put
\[
\begin{gathered}
 h_a=\Im a_*,\quad h_s=\Im s_*,\quad h_y=\Im y_*,
 \quad h_t=\Im t_*,\quad h_z=\Im z_*,\\
 a=x+ih_a,\quad y=q+ih_y,\quad z=u+ih_z,
 \qquad x,u\in P,\quad 0\le q\le11/50,\\
 X=e^{-2\pi ia},\quad Y=Re^{-2\pi iq},\quad Z=\rho e^{-2\pi iu},
 \qquad R=e^{2\pi h_y},\quad r_s=e^{2\pi h_s},\quad
 \rho=e^{2\pi h_z}.
\end{gathered}                                                \tag{2}
\]
All heights remain fixed at their actual reference values while the
three target real coordinates vary independently in the displayed
intervals. In particular the original bounds include
\[
 -.072<h_a<0,\qquad -.102<h_s,h_y<-.001,
 \qquad .24<\Re y_*<.36.                                    \tag{3}
\]
No sign restriction is imposed on the own-three main height \(h_t\).

The [correlated geometric height theorem](research_mixed_cap_343_correlated_height_bounds.md)
supplies, on this actual family,
\[
                 \frac7{10}<R<\frac{41}{50},\qquad
                         r_s>\frac45R.                       \tag{4}
\]
The strict lower bound also follows from the separate
[radius-exclusion theorem](research_mixed_cap_343_radius_exclusion.md).
The first row of
[open-word inheritance, Theorem 1](research_mixed_open_word_window_inheritance.md)
applies at \(j=3\), since \(3\le j\le m-2\). It gives
\[
              -3/100<h_t,h_z<1/50.
\]
Consequently
\[
 \rho>e^{-3\pi/50}>4/5,\qquad \rho<43/28.                    \tag{5}
\]
For the first strict comparison use
\(3\pi/50<33/175<2/9<\log(5/4)\); the upper bound is already
part of the original own-three source domain. The inherited height
bound applies to both legs of vertex three, but its real target
\(u\) in (2) may still range independently over all of \(P\).
The use of (5) is the reason for the length assumption \(m\ge5\).

For \(r=e^{-2\pi i/N}\), \(D=N-1\), retain
\[
\begin{split}
 P_j&=(r;r)_j,\qquad p_j(V)=(rV;r)_j,\\
 U_{0,N}(w,X)&=\sum_{k=0}^{D}H_N(w,r^{-k})p_k(X)/P_k,\\
 C_{1,N}(X,Y)&=\sum_{i=0}^{D}
                \frac{X^{-i}p_i(X)p_i(Y)}{P_i^3},\\
 C_{0,N}(Y,Z)&=\sum_{j=0}^{D}
                \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}.
\end{split}                                                   \tag{6}
\]
Here \(H_N(w,V)\) denotes the original ordinary endpoint polynomial
\(\mathcal H_N(w,V)\) of
[conditional torus composition, Corollary 3, equation (21)](research_mixed_conditional_torus_composition.md),
with its full endpoint color and normalization.
The shared factor is the original polynomial \(d_N\), of degree at
most \(N-1\), with \(d_N(r^b)=P_b^{-1}\). It occurs exactly once.
There is no outgoing halfweight for this next own type, and no
selected \(Y^{-N}\) is inserted.

Use the original cap plane \(B_U(x)\) and following affine plane
\(\Lambda_{123}(z)\) of
[the complete lower plateau](research_mixed_next_complete_lower_plateau.md),
equation (6). To make the allocation explicit, put
\[
\begin{split}
 Q_\gamma(v;b,c)&=g(v+b)+g(v+c)-(2+\gamma)g(v)
                         -g(b)-g(c)+2\pi ibv,\\
 F_1&=Q_1-\tfrac12g(y),\qquad F_2=Q_0-\tfrac12g(y).
\end{split}                                                   \tag{7}
\]
The cap and the two conditional affine planes cancel their internal
marginals and leave exactly \(\Lambda_{123}(z)\). Thus the two
shared halfweights in (7) give the full allocation \(-\Re g(y)\).
At the actual output,
\[
             \Lambda_{123}(z_*)=
                         \Re\mathcal P_0^+(-2,z_*),           \tag{8}
\]
with the original absolute primitive constants and local next action.

## 2. Statement and the source inputs

**Theorem.** Uniformly on (1)--(5), for every real ordinary color
\(w\in[-2,2]\) and all sufficiently large integer levels of both
parities,
\[
\boxed{\quad
 |U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{0,N}(Y,Z)|
 \le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}}.
 \quad}                                                       \tag{9}
\]
More precisely, the positive upper block also satisfies
\[
 |U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)|
 \sum_{j=\lceil N/2\rceil}^{D}
       \left|\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}\right|
 \le C N^B e^{N\{\Lambda_{123}(z)-10^{-11}\}}.
 \tag{9a}
\]
Any subset of that positive upper sum has the same bound. No
arbitrary-subset assertion is made for the signed next lower-half
block.

In particular define only the central part of the first incoming
integral by
\[
 F_N^{\mathrm{cent}}(w,Y)=
 N\int_{11/50+ih_a}^{9/20+ih_a}
        U_{0,N}(w,e^{-2\pi ia})C_{1,N}(e^{-2\pi ia},Y)\,da.
                                                               \tag{10}
\]
The path is oriented toward increasing real part and has \(da=dx\).
Then
\[
 |F_N^{\mathrm{cent}}(w,Y)d_N(Y)C_{0,N}(Y,Z)|
 \le C N^{B+1}e^{N\{\Lambda_{123}(z)-10^{-11}\}}.              \tag{11}
\]
The original factor is \(+N\), not a normalized average. Any fixed
subinterval of this central segment obeys the same estimate.

The proof uses the following complete source statements, with their
scopes unchanged:

| Input | Content used here |
|---|---|
| [Complete-first below half](research_mixed_next_own_three_below_half_complete_first.md) | The signed next block \(0\le j<\lceil N/2\rceil\), with complete first factor, deficit \(10^{-11}\). Both signs of \(h_t\) are included. |
| [Old-face band](research_mixed_next_own_three_upper_band_old_face.md) and [fixed-shared band](research_mixed_next_own_three_upper_band_fixed_shared.md) | Every positive upper row through \(j\le\lfloor N\max(7/10,4/5-q)\rfloor\), with complete first factor and deficit \(10^{-11}\); their continuous controlling profiles have deficit \(10^{-10}\). |
| [Correlated last transport](research_mixed_next_three_correlated_last_row_transport.md) | Under (4), every controlling first main/real-low/real-half/last profile with the actual next last rate is paid; its finite upper-end consequence has deficit \(10^{-11}\). |
| [Shallow upper-strip reduction](research_mixed_next_own_three_shallow_upper_strip_reduction.md) | Its literal positive rows reduce, with the complete first source, to the paid band or its explicitly retained next-last envelope. |
| [Small reflected bound](research_mixed_next_three_small_reflected_logarithmic_bound.md) | Under (4)--(5), every \(0\le v\le1/5\) satisfies \(E_0(1-v)\le L_0-v/600\). |

The small-reflected scalar proof uses its stated analytic radius
hypotheses, not the older, now excluded, condition \(R\le7/10\).

## 3. Payment of the last envelope with all first alternatives

Write the exact last rate and physical rate as
\[
\begin{split}
 L_0&=-\log R+\log_+\rho,\\
 E_0(t)&=\int_0^t\log|1-Ye^{-2\pi ib}|\,db
       +\int_0^t\log|1-Ze^{-2\pi ib}|\,db
                         -2J(t)-t\log R.
\end{split}                                                   \tag{12}
\]
In particular \(E_0(1)=L_0\). This keeps the positive outgoing-height
carrier even when \(h_z>0\).

For the first main segment clipped to \(1/6\le\Re s\le5/12\),
at its actual negative height, and for the real cuts \(1/8,1/2\),
set
\[
 \mathcal L_s(q)=B_U(x)+\Re Q_1(s;a,q+ih_y)
                              +L_0-\Re g(q+ih_y).
                                                               \tag{13}
\]
The correlated transport theorem proves, source by source,
\[
                  \mathcal L_s(q)<
                    \Lambda_{123}(z)-10^{-10}
                      \qquad(0\le q\le11/50).                \tag{14}
\]
Its proof calibrates at \(q=11/50\) with the actual own-three last
certificate, uses the retained first quadratic reserve, and transports
with derivative \(>1/5000\) under (4). The next last certificate is
used only for its sign; no unspecified margin is spent. The first
real low is already paid on the full radius interval. The first real
half is compared to its fixed negative-height profile before clipping.
The first last alternative retains the stronger double-last deficit
\(109/2000\).

Consequently the last envelope \(\mathfrak L(q')\) in equation (24)
of the shallow-strip theorem satisfies
\[
          \mathfrak L(q')\le\Lambda_{123}(z)-10^{-10}
                      \quad(0\le q'\le11/50).                 \tag{15}
\]
This is a profile conclusion before any first-index summation, which
is essential when a next physical row remains attached.

## 4. Exact partition of every next finite index

Put
\[
 j_h=\lceil N/2\rceil,\qquad j_b=\lfloor7N/10\rfloor,
 \qquad j_e=\lceil4N/5\rceil,\qquad v_j=1-j/N.                \tag{16}
\]
The literal next lower block \(0\le j<j_h\) is paid by the first
input in the table. The positive upper block splits exactly into
\[
\begin{array}{c|c}
 j_h\le j\le j_b&v_j\ge3/10,\\
 j_b<j<j_e&1/5<v_j<3/10,\\
 j_e\le j\le D&0<v_j\le1/5.
\end{array}                                                   \tag{17}
\]
The first range is a subset of the fixed-shared band, because
\(\max\{7/10,4/5-q\}\ge7/10\) for every current \(q\).
It is therefore already paid with the complete first factor.

In the third range the small reflected bound gives
\(E_0(1-v_j)\le L_0-v_j/600\le L_0\). Attach (14) and the
first last alternative before performing the full first-source
reduction. This comparison requires no ordering between \(q\) and
\(v_j\).

In the middle range, split according to its actual reflected index.
If \(v_j\le q\), the all-radius upper-end rate comparison gives
\(E_0(1-v_j)\le L_0\), and the correlated last transport applies.
Otherwise \(q<v_j<3/10\) and \(v_j>1/5\), exactly the
shallow-strip domain. Its equation (25), followed by (15), bounds
these positive rows with the complete first factor by rate
\(\Lambda_{123}(z)-10^{-10}+\tau\), for every fixed prescribed
\(\tau>0\).

Empty groups are harmless. The conditions exhaust every next index,
without deleting a half-grid, endpoint or threshold equality. At
either parity the lower block ends just before \(j_h\). Equality
\(v_j=3/10\), when present, belongs to the band; equality
\(v_j=1/5\) belongs to the small-reflected group. No finite value is
substituted at a nonintegral transported index.

For the small-reflected group, the uniform numerator and sine-factorial upper
bounds convert each literal row to (12), with \(O(\log N)\) cost
and arbitrarily small total rate tolerance. They retain all numerator
zeros. Near the true last index \(j=D\), \(v_j=1/N\); the additional
debit \(v_j/600\) is not misused as a uniform exponential gap. The
already available profile deficit (14) supplies that gap. The same
zero-safe endpoint treatment is part of the upper-end input. Every
original index remains in the polynomial source, including a row whose
numerator vanishes only at the complete-color or physical reference
and becomes nonzero under the allowed continuation.

Choose the sum of all new rate tolerances smaller than \(10^{-11}\). Then every
new group is paid with room inside the already existing finite loss
\(10^{-11}\). A finite number of such estimates and the sum of at most
\(N\) positive next rows change only the polynomial prefactor. This
proves the positive upper-block assertion. Adding the complete signed
lower block by the triangle inequality proves (9), and integrating
on the stated oriented central segment proves (11).

## 5. The retained first currents, weight and derivative scope

The preceding argument always keeps the full original first factor.
Its positive low physical rows increase to their original real low
cut, including the exact zero row. The complete middle interpolation
retains the horizontal aliases at heights \(-1/5,+4\), all four
weighted vertical halves, and both unweighted zero-mode joins.
These comparisons are made at the same shared \(q\) before any
diagonal transport in the shallow-strip theorem. In particular no
positive-height alias is transported by a negative-main formula.
The positive first upper block retains its real-half and last
alternatives, paid in (14) and by the double-last bound. The complete
cap estimate \(B_U(x)\) already contains every original private row,
end and current. None is replaced by a local cap packet.

The full forced-\(d_N(Y)\) upper envelope supplies \(-\Re g(y)\)
through \(q=0\). The separate canonical factorial continuation across
the inward seam supplies the row symbols there. No relative
asymptotic for \(d_N\), division by a vanishing factor, or deletion of
its forcing term is used. The complete first and next normalizations
are exactly (6); their integral has the original \(+N\) in (10).

The bounds hold for all real ordinary colors. The original
degree-\(O(N)\) polynomial/logarithmic-arc continuation, followed by
Cauchy's formula with a smaller reserved loss, gives all fixed
normalized local mixed derivatives of the corresponding holomorphic
products and central integrals, with deficit \(10^{-12}\) at the
actual output and the original action in (8). Reference labels,
base paths and any partial index subsets are held fixed for this
assertion. It is not a derivative statement for an absolute sum or a
moving floor. The full product in (9) itself has the fixed complete
index sets, so its conclusion requires no moving truncation.

This theorem does not estimate the initial first-input segment,
left taper, right-horizontal segment, incoming corner or far real arc
on the present shallow-radius family. It does not identify
\(F_N^{\mathrm{cent}}\) with the complete prefix \(F_N\), remove the
old cardinal filter, or control the remaining signed Fourier
contributions. Those source and contour obligations remain
separate from this complete **central** finite estimate.
